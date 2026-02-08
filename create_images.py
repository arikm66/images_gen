import json
import os
import requests
import time
from dotenv import load_dotenv
from rembg import remove
from PIL import Image
import io

# Load environment variables
load_dotenv()

# Hugging Face API setup (free tier, generous limits)
# Get your free token at: https://huggingface.co/settings/tokens
HF_API_TOKEN = os.getenv('HF_API_TOKEN', 'your-huggingface-token-here')
API_URL = "https://router.huggingface.co/hf-inference/models/black-forest-labs/FLUX.1-schnell"

headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}

# Read the nouns_short.json file
with open('nouns_short.json', 'r', encoding='utf-8') as f:
    nouns = json.load(f)

# Create images directory if it doesn't exist
os.makedirs('images', exist_ok=True)

# Prompt template
prompt_template = (
    "Create A high-quality 2D drawing of a {nameEn}. The drawing is intended for children aged 5-10. "
    "The drawing should be of the entire object, not a close-up. Not a face only. "
    "The viewer should see the object from the side and not the front. "
    "Vibrant colors. The object must be centered on a pure solid white background. "
    "Minimal white margins: the object should fill most of the frame without touching "
    "the edges. "
    "1:1 square aspect ratio, clean minimalist digital art."
)

# Counters for summary
generated_count = 0
skipped_count = 0
failed_count = 0

# Generate images for each noun
for i, noun in enumerate(nouns, 1):
    name_en = noun['nameEn']
    
    # Check if image already exists
    filename = f"images/{name_en.lower().replace(' ', '_')}.png"
    if os.path.exists(filename):
        print(f"[{i}/{len(nouns)}] ⊙ Skipping {name_en} (already exists)")
        skipped_count += 1
        continue
    
    # Create the prompt with the actual nameEn
    prompt = prompt_template.format(nameEn=name_en)
    
    print(f"[{i}/{len(nouns)}] Generating image for: {name_en}")
    
    # Retry logic for API rate limits and model loading
    max_retries = 5
    retry_count = 0
    success = False
    
    while retry_count < max_retries and not success:
        try:
            # Call Hugging Face Inference API
            response = requests.post(
                API_URL,
                headers=headers,
                json={"inputs": prompt},
                timeout=120
            )
            
            if response.status_code == 200:
                # Remove background from the generated image
                input_image = Image.open(io.BytesIO(response.content))
                output_image = remove(input_image)
                
                # Save the image with transparent background
                output_image.save(filename, 'PNG')
                print(f"  ✓ Saved with transparent background: {filename}")
                success = True
                generated_count += 1
            elif response.status_code == 503:
                # Model is loading, wait and retry
                retry_count += 1
                wait_time = 20
                print(f"  ⚠ Model loading, waiting {wait_time} seconds... (Attempt {retry_count}/{max_retries})")
                time.sleep(wait_time)
            elif response.status_code == 429:
                # Rate limit, wait longer
                retry_count += 1
                wait_time = 30
                print(f"  ⚠ Rate limited, waiting {wait_time} seconds... (Attempt {retry_count}/{max_retries})")
                time.sleep(wait_time)
            else:
                error_msg = response.json() if response.headers.get('content-type') == 'application/json' else response.text
                print(f"  ✗ Failed (Status: {response.status_code}): {error_msg}")
                break
            
        except Exception as e:
            retry_count += 1
            if retry_count < max_retries:
                wait_time = 10
                print(f"  ⚠ Error: {str(e)}, retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                print(f"  ✗ Error generating image for {name_en}: {str(e)}")
    
    # Track failed generations
    if not success:
        failed_count += 1
    
    # Small delay between successful requests to avoid rate limiting
    if success:
        time.sleep(2)

print(f"\nCompleted! Generated: {generated_count}, Skipped: {skipped_count}, Failed: {failed_count} (Total: {len(nouns)} nouns)")

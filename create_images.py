import json
import os
import requests
import time
import sys
import argparse
from dotenv import load_dotenv
from rembg import remove
from PIL import Image
import io

# Load environment variables
load_dotenv()

# Parse command line arguments
parser = argparse.ArgumentParser(
    description='Generate images for nouns using Hugging Face AI models with transparent backgrounds.',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog='''
Examples:
  python create_images.py                    # Process default file (nouns_short.json) with HF model
  python create_images.py -f nouns.json      # Process custom file
  python create_images.py -m dalle           # Use DALL-E instead of Hugging Face
  python create_images.py -m together        # Use Together.ai
  python create_images.py -m segmind         # Use Segmind
  python create_images.py -f nouns.json -m dalle  # Custom file with DALL-E
    '''
)
parser.add_argument(
    '-f', '--file',
    default='nouns_short.json',
    help='JSON file containing nouns to process (default: nouns_short.json)'
)
parser.add_argument(
    '-m', '--model',
    choices=['hf', 'dalle', 'together', 'segmind'],
    default='hf',
    help='AI model to use: hf (Hugging Face), dalle (DALL-E), together (Together.ai), or segmind (Segmind) (default: hf)'
)
args = parser.parse_args()

# API Configuration
if args.model == 'hf':
    # Hugging Face API setup (free tier, generous limits)
    # Get your free token at: https://huggingface.co/settings/tokens
    HF_API_TOKEN = os.getenv('HF_API_TOKEN', 'your-huggingface-token-here')
    API_URL = "https://router.huggingface.co/hf-inference/models/black-forest-labs/FLUX.1-schnell"
    headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}
    print(f"Using Hugging Face model: FLUX.1-schnell")
elif args.model == 'dalle':
    # DALL-E API setup
    # Get your API key at: https://platform.openai.com/api-keys
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'your-openai-api-key-here')
    API_URL = "https://api.openai.com/v1/images/generations"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    print(f"Using OpenAI DALL-E model")
elif args.model == 'together':
    # Together.ai API setup ($5 free credits)
    # Get your API key at: https://api.together.xyz/settings/api-keys
    TOGETHER_API_KEY = os.getenv('TOGETHER_API_KEY', 'your-together-api-key-here')
    API_URL = "https://api.together.xyz/v1/images/generations"
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }
    print(f"Using Together.ai model")
else:  # segmind
    # Segmind API setup (1,000 free credits/month)
    # Get your API key at: https://www.segmind.com/
    SEGMIND_API_KEY = os.getenv('SEGMIND_API_KEY', 'your-segmind-api-key-here')
    API_URL = "https://api.segmind.com/v1/sdxl1.0-txt2img"
    headers = {
        "x-api-key": SEGMIND_API_KEY,
        "Content-Type": "application/json"
    }
    print(f"Using Segmind model")

# Read the specified JSON file
input_file = args.file
if not os.path.exists(input_file):
    print(f"Error: File '{input_file}' not found.")
    sys.exit(1)

print(f"Processing file: {input_file}")
with open(input_file, 'r', encoding='utf-8') as f:
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
            if args.model == 'hf':
                # Call Hugging Face Inference API
                response = requests.post(
                    API_URL,
                    headers=headers,
                    json={"inputs": prompt},
                    timeout=120
                )
            elif args.model == 'dalle':
                # Call OpenAI DALL-E API
                response = requests.post(
                    API_URL,
                    headers=headers,
                    json={
                        "model": "dall-e-3",
                        "prompt": prompt,
                        "n": 1,
                        "size": "1024x1024",
                        "quality": "standard"
                    },
                    timeout=120
                )
            elif args.model == 'together':
                # Call Together.ai API
                response = requests.post(
                    API_URL,
                    headers=headers,
                    json={
                        "model": "black-forest-labs/FLUX.1-schnell-Free",
                        "prompt": prompt,
                        "width": 1024,
                        "height": 1024,
                        "steps": 4,
                        "n": 1
                    },
                    timeout=120
                )
            else:  # segmind
                # Call Segmind API
                response = requests.post(
                    API_URL,
                    headers=headers,
                    json={
                        "prompt": prompt,
                        "negative_prompt": "blurry, low quality, distorted, ugly",
                        "samples": 1,
                        "scheduler": "UniPC",
                        "num_inference_steps": 25,
                        "guidance_scale": 7.5,
                        "seed": -1,
                        "img_width": 1024,
                        "img_height": 1024,
                        "base64": False
                    },
                    timeout=120
                )
            
            if response.status_code == 200:
                if args.model == 'hf':
                    # Remove background from the generated image
                    input_image = Image.open(io.BytesIO(response.content))
                    output_image = remove(input_image)
                    
                    # Save the image with transparent background
                    output_image.save(filename, 'PNG')
                    print(f"  ✓ Saved with transparent background: {filename}")
                elif args.model == 'dalle':
                    # DALL-E returns a URL to the image
                    image_url = response.json()['data'][0]['url']
                    
                    # Download the image
                    img_response = requests.get(image_url, timeout=30)
                    img_response.raise_for_status()
                    
                    # Remove background
                    input_image = Image.open(io.BytesIO(img_response.content))
                    output_image = remove(input_image)
                    
                    # Save the image with transparent background
                    output_image.save(filename, 'PNG')
                    print(f"  ✓ Saved with transparent background: {filename}")
                elif args.model == 'together':
                    # Together.ai returns a URL or base64 depending on response_format
                    result = response.json()
                    if 'data' in result and len(result['data']) > 0:
                        # Get the image URL or b64_json
                        if 'url' in result['data'][0]:
                            image_url = result['data'][0]['url']
                            img_response = requests.get(image_url, timeout=30)
                            img_response.raise_for_status()
                            input_image = Image.open(io.BytesIO(img_response.content))
                        elif 'b64_json' in result['data'][0]:
                            import base64
                            image_data = base64.b64decode(result['data'][0]['b64_json'])
                            input_image = Image.open(io.BytesIO(image_data))
                        
                        # Remove background
                        output_image = remove(input_image)
                        
                        # Save the image with transparent background
                        output_image.save(filename, 'PNG')
                        print(f"  ✓ Saved with transparent background: {filename}")
                    else:
                        print(f"  ✗ Unexpected response format from Together.ai")
                        break
                else:  # segmind
                    # Segmind returns the image directly as bytes
                    input_image = Image.open(io.BytesIO(response.content))
                    
                    # Remove background
                    output_image = remove(input_image)
                    
                    # Save the image with transparent background
                    output_image.save(filename, 'PNG')
                    print(f"  ✓ Saved with transparent background: {filename}")
                
                success = True
                generated_count += 1
            elif response.status_code == 402:
                # Credit balance depleted - abort script
                print(f"  ✗ Credit balance depleted (Status: 402)")
                failed_count += 1
                print(f"\n⚠ Aborting script due to insufficient credits.")
                print(f"Summary: Generated: {generated_count}, Skipped: {skipped_count}, Failed: {failed_count}")
                sys.exit(1)
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

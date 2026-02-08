import json
import nltk
from nltk.corpus import wordnet as wn
from deep_translator import GoogleTranslator

# Download necessary WordNet datasets
nltk.download('wordnet')
nltk.download('omw-1.4')

def get_concrete_nouns(limit=100):
    """
    Extracts physical nouns from WordNet, translates them to Hebrew, 
    and organizes them into nouns and categories JSON files.
    """
    translator = GoogleTranslator(source='en', target='iw')
    categories_set = set()
    
    # Curated list of common, everyday concrete nouns organized by category
    # These are tangible objects everyone knows and encounters regularly
    common_concrete_nouns = {
        'Animals': [
            'dog', 'cat', 'bird', 'fish', 'horse', 'cow', 'pig', 'sheep', 'chicken', 'rabbit',
            'mouse', 'lion', 'tiger', 'bear', 'elephant', 'monkey', 'snake', 'frog', 'duck', 'fox',
            'wolf', 'deer', 'owl', 'eagle', 'butterfly', 'bee', 'ant', 'spider', 'turtle', 'whale'
        ],
        'Food': [
            'apple', 'banana', 'orange', 'bread', 'milk', 'cheese', 'egg', 'meat', 'rice', 'potato',
            'tomato', 'carrot', 'onion', 'pizza', 'cake', 'cookie', 'chocolate', 'coffee', 'tea', 'water',
            'juice', 'soup', 'sandwich', 'salad', 'butter', 'sugar', 'salt', 'pepper', 'fish', 'chicken'
        ],
        'Household Items': [
            'table', 'chair', 'bed', 'sofa', 'lamp', 'door', 'window', 'mirror', 'clock', 'television',
            'phone', 'computer', 'book', 'pen', 'pencil', 'paper', 'cup', 'plate', 'spoon', 'fork',
            'knife', 'bottle', 'glass', 'bowl', 'box', 'bag', 'towel', 'blanket', 'pillow', 'carpet'
        ],
        'Clothing': [
            'shirt', 'pants', 'dress', 'skirt', 'jacket', 'coat', 'shoes', 'boots', 'hat', 'cap',
            'gloves', 'socks', 'belt', 'tie', 'scarf', 'sweater', 'jeans', 'shorts', 'suit', 'uniform'
        ],
        'Vehicles': [
            'car', 'bus', 'truck', 'bicycle', 'motorcycle', 'train', 'airplane', 'boat', 'ship', 'taxi',
            'van', 'helicopter', 'scooter', 'subway', 'ambulance', 'tractor', 'rocket', 'balloon'
        ],
        'Tools': [
            'hammer', 'saw', 'screwdriver', 'nail', 'screw', 'axe', 'shovel', 'rake', 'ladder', 'brush',
            'scissors', 'needle', 'thread', 'key', 'lock', 'rope', 'chain', 'tape', 'glue', 'drill'
        ],
        'Nature': [
            'tree', 'flower', 'grass', 'leaf', 'branch', 'root', 'stone', 'rock', 'mountain', 'hill',
            'river', 'lake', 'ocean', 'cloud', 'rain', 'snow', 'sun', 'moon', 'star', 'wind',
            'fire', 'water', 'soil', 'sand', 'ice', 'wave', 'forest', 'beach', 'island', 'valley'
        ],
        'Body Parts': [
            'head', 'face', 'eye', 'ear', 'nose', 'mouth', 'tooth', 'tongue', 'hand', 'finger',
            'arm', 'leg', 'foot', 'toe', 'knee', 'shoulder', 'chest', 'back', 'neck', 'hair'
        ],
        'Buildings & Places': [
            'house', 'building', 'school', 'hospital', 'store', 'restaurant', 'hotel', 'church', 'park', 'garden',
            'street', 'road', 'bridge', 'tower', 'castle', 'museum', 'library', 'factory', 'farm', 'market'
        ],
        'Musical Instruments': [
            'piano', 'guitar', 'drum', 'flute', 'violin', 'trumpet', 'saxophone', 'harp', 'bell'
        ],
        'Sports & Games': [
            'ball', 'bat', 'racket', 'goal', 'net', 'chess', 'cards', 'dice', 'puzzle', 'toy'
        ]
    }
    
    # Flatten the list with category information
    concrete_nouns_with_categories = []
    for category, words in common_concrete_nouns.items():
        for word in words:
            concrete_nouns_with_categories.append((word, category))
    
    # Limit to requested number of words
    concrete_nouns_with_categories = concrete_nouns_with_categories[:limit]
    
    # Open nouns.json file and write opening bracket
    with open('nouns.json', 'w', encoding='utf-8') as nouns_file:
        nouns_file.write('[\n')
        
        count = 0
        # Iterate through the curated list of concrete nouns
        for english_word, eng_category in concrete_nouns_with_categories:
            try:
                # Translate both word and category to Hebrew
                hebrew_word = translator.translate(english_word)
                hebrew_category = translator.translate(eng_category)
                
                # Create noun entry
                noun_entry = {
                    "word": hebrew_word, 
                    "category": hebrew_category
                }
                categories_set.add(hebrew_category)
                
                # Write to file immediately with proper comma handling
                if count > 0:
                    nouns_file.write(',\n')
                json.dump(noun_entry, nouns_file, ensure_ascii=False, indent=2)
                nouns_file.flush()  # Ensure it's written to disk
                
                count += 1
                print(f"Found ({count}/{limit}): {english_word} -> {hebrew_word} (Category: {eng_category})")
            except Exception as e:
                # Skip words that fail translation
                print(f"Skipped {english_word}: {e}")
                continue
        
        # Close the JSON array
        nouns_file.write('\n]')
    
    # Create the categories structure for the categories JSON file
    categories_list = [
        {"name": cat, "description": f"Words belonging to the {cat} group"} 
        for cat in categories_set
    ]
    
    return count, categories_list

# Set the desired number of words (e.g., 100)
# Note: Higher limits will take longer due to translation API calls
word_limit = 100
word_count, cats = get_concrete_nouns(limit=word_limit)

# nouns.json is already written incrementally by the function

# Save the categories to categories.json
with open('categories.json', 'w', encoding='utf-8') as f:
    json.dump(cats, f, ensure_ascii=False, indent=2)

print(f"\nSuccess! Generated {word_count} words in 'nouns.json' and 'categories.json'.")
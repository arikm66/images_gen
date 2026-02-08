import json

# Read the export_categories.json file to get category mappings
with open('export_categories.json', 'r', encoding='utf-8') as f:
    categories = json.load(f)

# Create a mapping from categoryHe to category ID
category_map = {}
for category in categories:
    category_he = category['categoryHe']
    category_id = category['_id']['$oid']
    category_map[category_he] = category_id

print(f"Loaded {len(category_map)} categories")
print("Category mappings:")
for cat_he, cat_id in category_map.items():
    print(f"  {cat_he} -> {cat_id}")

# Read the current nouns.json file
with open('nouns.json', 'r', encoding='utf-8') as f:
    nouns = json.load(f)

print(f"\nProcessing {len(nouns)} nouns...")

# Transform the nouns
new_nouns = []
unmapped_categories = set()

for noun in nouns:
    category_he = noun.get('categoryHe', '')
    
    # Check if category exists in mapping
    if category_he in category_map:
        new_noun = {
            "nameEn": noun['nameEn'],
            "nameHe": noun['nameHe'],
            "category": {
                "$oid": category_map[category_he]
            }
        }
        new_nouns.append(new_noun)
    else:
        unmapped_categories.add(category_he)
        print(f"Warning: No mapping found for category '{category_he}' for word '{noun['nameEn']}'")

# Report unmapped categories
if unmapped_categories:
    print(f"\nUnmapped categories found: {unmapped_categories}")
    print("These nouns will be skipped in the output.")

# Write the new nouns to a new file
with open('nouns_new.json', 'w', encoding='utf-8') as f:
    json.dump(new_nouns, f, ensure_ascii=False, indent=2)

print(f"\n✓ Successfully converted {len(new_nouns)} nouns")
print(f"✓ New file saved as 'nouns_new.json'")

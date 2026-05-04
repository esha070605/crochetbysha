import re

# Read the clean base64 data, stripping BOM if present
with open('logo_base64_utf8.txt', 'r', encoding='utf-8-sig') as f:
    base64_data = f.read().strip()

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the full data URL
data_url = 'data:image/png;base64,' + base64_data

# Use regex to find the img tag with class="hero-logo" and replace its src
# This handles cases where src already contains a (possibly broken) base64 string or "logo.png"
pattern = r'(<img\s+src=")([^"]*)(" \s*alt="Crochet by Sha Logo" \s*class="hero-logo">)'
new_content = re.sub(pattern, r'\1' + data_url + r'\3', content, flags=re.VERBOSE)

# If the first pattern didn't match (maybe attributes are in different order), try a simpler one
if new_content == content:
    pattern_simple = r'src="data:image/png;base64,[^"]*"\s+alt="Crochet by Sha Logo"\s+class="hero-logo"'
    replacement_simple = f'src="{data_url}" alt="Crochet by Sha Logo" class="hero-logo"'
    new_content = re.sub(pattern_simple, replacement_simple, content)

# Write the fixed content back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Logo updated successfully (BOM-aware).")

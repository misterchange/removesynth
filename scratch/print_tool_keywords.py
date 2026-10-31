import json

with open('scratch/excel_keywords_summary.json', 'r', encoding='utf-8') as f:
    tools = json.load(f)

for t in tools:
    name = t['tool']
    if any(k in name.lower() for k in ['photoshop', 'audio', 'mp3', 'exif', 'camera', 'date', 'bulk', 'docx', 'word', 'pdf', 'gps', 'location', 'anonymous']):
        print(f"Tool: {name} ({t['group']})")
        print(f"  US: {t['us_keywords']}")
        print(f"  IN: {t['in_keywords']}")
        if t['extra']:
            print(f"  Extra: {t['extra']}")
        print("-" * 40)

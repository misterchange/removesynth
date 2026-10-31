import os
import re
import pandas as pd

pages_dir = r'd:\Nitin\removesynth\apps\removesynth\src\pages'
results = []

for f in sorted(os.listdir(pages_dir)):
    if not f.endswith('.astro') or f.startswith('['):
        continue
    path = os.path.join(pages_dir, f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Title
    t_match = re.search(r'const title\s*=\s*[\'"`](.*?)[\'"`]', content)
    title = t_match.group(1) if t_match else 'NO_TITLE'
    
    # Desc
    d_match = re.search(r'const description\s*=\s*[\'"`](.*?)[\'"`]', content, re.DOTALL)
    desc = d_match.group(1).replace('\n', ' ').strip() if d_match else 'NO_DESC'
    
    # Em/en dashes
    dashes = len(re.findall(r'[—–]', content))
    
    # Schema check
    has_graph = '@graph' in content
    
    # Emojis (unicode emoji range)
    emojis = len(re.findall(r'[\U0001F300-\U0001FAFF]', content))
    
    results.append({
        'file': f,
        'title_len': len(title),
        'desc_len': len(desc),
        'title': title,
        'dashes': dashes,
        'emojis': emojis,
        'has_graph': has_graph,
        'lines': len(content.splitlines())
    })

df = pd.DataFrame(results)
print(df.to_string())
df.to_csv('scratch/audit_pages_results.csv', index=False)

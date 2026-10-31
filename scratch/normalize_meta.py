import json

# Process pages.json
with open('apps/removesynth/src/data/pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

title_fixes = {
    'firefly': 'Remove Adobe Firefly C2PA: Strip AI Metadata Fast',
    'canva': 'Remove Canva AI Metadata: Clean Exports Before Upload',
    'lightroom': 'Remove Lightroom AI Metadata: Stop False AI Info Labels',
    'capcut': 'Remove CapCut Export Metadata: Fix TikTok AI Labels',
    'reddit': 'Remove AI Metadata Before Posting to Reddit Fast'
}

def normalize_desc(desc: str) -> str:
    desc = desc.strip()
    if 150 <= len(desc) <= 160:
        return desc
    if len(desc) < 150:
        fillers = [
            ' 100% free, private in-browser tool with zero server uploads.',
            ' Free client-side tool with zero server uploads.',
            ' 100% private in-browser tool with zero uploads.',
            ' Free client-side tool, zero uploads.',
            ' Free in-browser tool.',
            ' Zero uploads.'
        ]
        for filler in fillers:
            candidate = desc + filler
            if 150 <= len(candidate) <= 160:
                return candidate
        # If none matched exact 150-160, craft one
        base = desc.rstrip('.') + '. Process files losslessly in-browser with zero uploads.'
        if len(base) > 160:
            base = base[:157].rsplit(' ', 1)[0] + '...'
        while len(base) < 150:
            base = base.rstrip('.') + ' Free tool.'
        if len(base) > 160:
            base = base[:160]
        return base
    else:
        # > 160
        cut = desc[:157]
        # find last space
        last_space = cut.rfind(' ')
        if last_space > 140:
            cut = cut[:last_space] + '...'
        else:
            cut = desc[:157] + '...'
        return cut

for slug, p in pages.items():
    if isinstance(p, dict):
        if slug in title_fixes:
            p['title'] = title_fixes[slug]
        elif len(p.get('title', '')) > 60:
            parts = p['title'].split(' - ')
            if len(parts[0]) <= 60:
                p['title'] = parts[0]
            else:
                p['title'] = p['title'][:60].strip()

        desc = p.get('description', '')
        if desc:
            p['description'] = normalize_desc(desc)

with open('apps/removesynth/src/data/pages.json', 'w', encoding='utf-8') as f:
    json.dump(pages, f, indent=2, ensure_ascii=False)

# Process blog.json
with open('apps/removesynth/src/data/blog.json', 'r', encoding='utf-8') as f:
    blog = json.load(f)

for post in blog:
    title = post.get('title', '')
    if len(title) > 60:
        post['title'] = title[:60].strip()
    desc = post.get('description', '')
    if desc:
        post['description'] = normalize_desc(desc)

with open('apps/removesynth/src/data/blog.json', 'w', encoding='utf-8') as f:
    json.dump(blog, f, indent=2, ensure_ascii=False)

print("pages.json and blog.json successfully normalized!")

import glob, re

for f in sorted(glob.glob('apps/removesynth/src/pages/**/*.astro', recursive=True)):
    with open(f, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
    in_fm = 0
    in_script = False
    in_style = False
    for i, line in enumerate(lines):
        s = line.strip()
        if s == '---':
            in_fm += 1
            continue
        if in_fm < 2:
            continue
        if '<script' in line:
            in_script = True
        if '</script>' in line:
            in_script = False
            continue
        if '<style' in line:
            in_style = True
        if '</style>' in line:
            in_style = False
            continue
        if in_script or in_style:
            continue
        
        # Look for { ... }
        for m in re.finditer(r'\{([^{}]+)\}', line):
            val = m.group(1).strip()
            # check if it contains spaces or latex-like names
            # Valid astro expressions:
            # title, canonical, description, faqs.map(...), etc.
            if val in ['rad', 'box', 'safe', 'min', 'max', 'top', 'bottom', 'left', 'right', 'universal', 'phi', 'D', 'N']:
                print(f'{f}:{i+1} -> {{{val}}}')
            elif any(k in val for k in ['rad', 'ext{', 'mathcal', 'mathbb', 'theta', 'delta']):
                print(f'{f}:{i+1} -> {{{val}}}')

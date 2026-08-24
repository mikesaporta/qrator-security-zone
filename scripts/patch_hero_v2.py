from pathlib import Path
import re

path = Path('site/index.html')
html = path.read_text(encoding='utf-8')

hero_css = '''
.heroVisual .heroPhoto{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center center;display:block}
.heroVisual:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(3,9,18,.02),rgba(3,9,18,.08));pointer-events:none}
'''
html = html.replace('</style></head><body>', hero_css + '</style></head><body>', 1)

# Replace the existing schematic hero with a clean image and remove the overlaid package-price card entirely.
pattern = r'<div class="heroVisual"><svg.*?</svg><div class="priceBox">.*?</div></div>'
replacement = '<div class="heroVisual"><img class="heroPhoto" src="assets/qrator-ft-hero-clean.webp?v=2" alt="Qrator Labs × FT Community"></div>'
html, count = re.subn(pattern, replacement, html, count=1, flags=re.S)

# If a previous hero patch already ran before this one, handle that markup as well.
if count == 0:
    pattern = r'<div class="heroVisual"><img class="heroPhoto"[^>]*><div class="priceBox">.*?</div></div>'
    html, count = re.subn(pattern, replacement, html, count=1, flags=re.S)

if count != 1:
    raise SystemExit(f'Hero replacement count: {count}')

path.write_text(html, encoding='utf-8')

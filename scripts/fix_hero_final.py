from pathlib import Path
import re

path = Path('site/index.html')
html = path.read_text(encoding='utf-8')

hero_css = '''
.heroVisual .heroPhoto{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center center;display:block}
'''
if '.heroVisual .heroPhoto' not in html:
    html = html.replace('</style></head><body>', hero_css + '</style></head><body>', 1)

replacement = '<div class="heroVisual"><img class="heroPhoto" src="assets/qrator-ft-community-hero.jpg?v=final" alt="Qrator Labs × FT Community"></div>'

patterns = [
    r'<div class="heroVisual"><svg.*?</svg><div class="priceBox">.*?</div></div>',
    r'<div class="heroVisual"><img[^>]*><div class="priceBox">.*?</div></div>',
    r'<div class="heroVisual"><svg.*?</svg></div>',
    r'<div class="heroVisual"><img[^>]*></div>',
]

count = 0
for pattern in patterns:
    html, n = re.subn(pattern, replacement, html, count=1, flags=re.S)
    if n:
        count = n
        break

if count != 1:
    raise SystemExit('Hero block was not found')

# Safety: remove any leftover package-price overlay inside hero.
html = re.sub(r'<div class="priceBox">.*?</div>', '', html, flags=re.S)

path.write_text(html, encoding='utf-8')

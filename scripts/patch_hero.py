from pathlib import Path
import re

path = Path('site/index.html')
html = path.read_text(encoding='utf-8')

hero_css = '''
.heroVisual .heroPhoto{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center center;display:block}
.heroVisual:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(3,9,18,.04),rgba(3,9,18,.16));pointer-events:none}
.heroVisual .priceBox{z-index:2}
'''
html = html.replace('</style></head><body>', hero_css + '</style></head><body>', 1)

pattern = r'<div class="heroVisual"><svg.*?</svg><div class="priceBox">'
replacement = '<div class="heroVisual"><img class="heroPhoto" src="assets/qrator-hero-entrance.jpg" alt="Welcome-зона Qrator Labs"><div class="priceBox">'
html, count = re.subn(pattern, replacement, html, count=1, flags=re.S)
if count != 1:
    raise SystemExit(f'Hero visual replacement count: {count}')

path.write_text(html, encoding='utf-8')

from pathlib import Path
import re

path = Path('site/index.html')
html = path.read_text(encoding='utf-8')

# Card images are unpacked into site/assets/images before this script runs.
image_map = {
    'Welcome-зона': 'assets/images/welcome-zone.jpg',
    'Ковер': 'assets/images/neutral-carpet.jpg',
    'Флаги-виндеры': 'assets/images/winders.jpg',
    'Оградительные ленты': 'assets/images/barrier-tapes.jpg',
    'Деревянные стойки': 'assets/images/wooden-stands.jpg',
    'Мольберт': 'assets/images/easel.jpg',
    'Боковой вход': 'assets/images/side-entrance.jpg',
    'Аксессуары охраны': 'assets/images/security-accessories.jpg',
    'Брендинг девайсов': 'assets/images/device-branding.jpg',
}

items_match = re.search(r"const items=\[(.*?)\];", html, flags=re.S)
if not items_match:
    raise SystemExit('Catalog items array not found')

items = [
    ['WELCOME','Welcome-зона','Центральный вход: стойки, виндеры, ленты и ковер','carpet', image_map['Welcome-зона']],
    ['WELCOME','Ковер','','carpet', image_map['Ковер']],
    ['WELCOME','Флаги-виндеры','Вертикальные акценты по краям welcome-пути','flag', image_map['Флаги-виндеры']],
    ['SECURITY','Оградительные ленты','Айдентика бренда в элементе зонирования','tape', image_map['Оградительные ленты']],
    ['BRANDING','Деревянные стойки','Аккуратное оформление стоек хостес','desk', image_map['Деревянные стойки']],
    ['WELCOME','Мольберт','Постер на входе с информацией о партнере','easel', image_map['Мольберт']],
    ['WELCOME','Боковой вход','Два флага виндера','flag', image_map['Боковой вход']],
    ['SECURITY','Аксессуары охраны','Повязка, ланьярд + бейдж, значок, галстук','guard', image_map['Аксессуары охраны']],
    ['BRANDING','Брендинг девайсов','Планшеты, мониторы и RFID-считыватели','device', image_map['Брендинг девайсов']],
]

items_js = 'const items=[' + ','.join(
    "['%s','%s','%s','%s','%s']" % tuple(x) for x in items
) + '];'
html = html[:items_match.start()] + items_js + html[items_match.end():]

old_cards = "function cards(arr,id){document.getElementById(id).innerHTML=arr.map(x=>`<article class=\"card\"><div class=\"thumb\">${icon(x[3])}</div><div class=\"cardBody\"><span class=\"pill\">${x[0]}</span><h3>${x[1]}</h3><p>${x[2]}</p></div></article>`).join('')}"
new_cards = "function cards(arr,id){document.getElementById(id).innerHTML=arr.map(x=>`<article class=\"card\"><div class=\"thumb\">${x[4]?`<img src=\"${x[4]}\" alt=\"${x[1]} — Qrator Labs\" loading=\"lazy\">`:icon(x[3])}</div><div class=\"cardBody\"><span class=\"pill\">${x[0]}</span><h3>${x[1]}</h3><p>${x[2]}</p></div></article>`).join('')}"
if old_cards not in html:
    raise SystemExit('Catalog render function not found')
html = html.replace(old_cards, new_cards, 1)

card_css = '.thumb img{width:100%;height:100%;object-fit:cover;object-position:center;display:block}'
if card_css not in html:
    html = html.replace('.thumb svg{width:100%;height:100%}', '.thumb svg{width:100%;height:100%}'+card_css, 1)

path.write_text(html, encoding='utf-8')

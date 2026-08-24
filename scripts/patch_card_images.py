from pathlib import Path
import re

path = Path('site/index.html')
html = path.read_text(encoding='utf-8')

# Full-resolution PNG originals are committed directly to site/assets/images.
image_map = {
    'Welcome-зона': 'assets/images/welcome-zone.png',
    'Ковер': 'assets/images/neutral-carpet.png',
    'Флаги-виндеры': 'assets/images/winders.png',
    'Оградительные ленты': 'assets/images/barrier-tapes.png',
    'Деревянные стойки': 'assets/images/wooden-stands.png',
    'Мольберт': 'assets/images/easel.png',
    'Боковой вход': 'assets/images/side-entrance.png',
    'Аксессуары охраны': 'assets/images/security-accessories.png',
    'Брендинг девайсов': 'assets/images/device-branding.png',
}

lounge_image_map = {
    'Уютная зона ожидания': 'assets/images/security-lounge.png',
    'Коктейльные столы': 'assets/images/cocktail-tables.png',
    'Текстильные накладки': 'assets/images/table-covers.png',
    'Charging Hub': 'assets/images/charging-hub.png',
    'Refresh Station': 'assets/images/refresh-station.png',
}

package_image_map = {
    'Security package': 'assets/images/security-package-collage.png',
    'Security + Lounge': 'assets/images/security-lounge-package-collage.png',
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

lounge_match = re.search(r"const lounge=\[(.*?)\];", html, flags=re.S)
if not lounge_match:
    raise SystemExit('Lounge items array not found')

# Keep the cards in the guest journey order and pair every service with the
# matching full-resolution visual supplied for the Security Lounge.
lounge = [
    ['LOUNGE','Уютная зона ожидания','Комфортная точка ожидания у входа','table', lounge_image_map['Уютная зона ожидания']],
    ['LOUNGE','Коктейльные столы','+Напиток в фирменном цвете Qrator Labs','table', lounge_image_map['Коктейльные столы']],
    ['LOUNGE','Текстильные накладки','Фирменные накладки / скатерти','table', lounge_image_map['Текстильные накладки']],
    ['LOUNGE','Charging Hub','USB-C, Lightning, USB-A','hub', lounge_image_map['Charging Hub']],
    ['LOUNGE','Refresh Station','Шоты, салфетки, мятные конфеты, фрукты','refresh', lounge_image_map['Refresh Station']],
]

lounge_js = 'const lounge=[' + ','.join(
    "['%s','%s','%s','%s','%s']" % tuple(x) for x in lounge
) + '];'
html = html[:lounge_match.start()] + lounge_js + html[lounge_match.end():]

old_cards = "function cards(arr,id){document.getElementById(id).innerHTML=arr.map(x=>`<article class=\"card\"><div class=\"thumb\">${icon(x[3])}</div><div class=\"cardBody\"><span class=\"pill\">${x[0]}</span><h3>${x[1]}</h3><p>${x[2]}</p></div></article>`).join('')}"
new_cards = "function cards(arr,id){document.getElementById(id).innerHTML=arr.map(x=>`<article class=\"card\"><div class=\"thumb\">${x[4]?`<img src=\"${x[4]}\" alt=\"${x[1]} — Qrator Labs\" loading=\"lazy\" decoding=\"async\">`:icon(x[3])}</div><div class=\"cardBody\"><span class=\"pill\">${x[0]}</span><h3>${x[1]}</h3><p>${x[2]}</p></div></article>`).join('')}"
if old_cards not in html:
    raise SystemExit('Catalog render function not found')
html = html.replace(old_cards, new_cards, 1)

# Preserve the full composition of the two portrait/square catalog visuals.
for image_path in ('assets/images/security-accessories.png', 'assets/images/device-branding.png'):
    html = html.replace(
        f'<article class="card"><div class="thumb"><img src="{image_path}"',
        f'<article class="card card--contain"><div class="thumb"><img src="{image_path}"',
        1,
    )

# Use a taller media area. Lounge visuals intentionally use cover so the photo
# always reaches every edge without letterboxing or escaping the rounded card.
card_css = (
    '.thumb{aspect-ratio:1.2;background:#0b121b}'
    '.thumb img{width:100%;height:100%;object-fit:cover;object-position:center;display:block;'
    'padding:0;background:#0b121b;image-rendering:auto}'
    '.card--contain .thumb img{object-fit:contain;object-position:center;padding:0;background:#0b121b}'
    '.lounge .thumb{background:#0b121b}'
    '.lounge .thumb img{width:100%;height:100%;object-fit:cover;object-position:center;display:block;'
    'padding:0;background:#0b121b;image-rendering:auto}'
)
if card_css not in html:
    html = html.replace('.thumb svg{width:100%;height:100%}', '.thumb svg{width:100%;height:100%}'+card_css, 1)

# The compact package chooser below the comparison table is the primary
# add-to-cart surface. Use the same full-resolution collages there as well and
# remove the temporary "Фото пакета" placeholders added by patch_site.py.
quick_package_media = {
    '17000': (
        '<div class="quickMedia quickMedia--photo" data-package-media="17000">'
        '<img src="%s" alt="Security package — визуализация Qrator Labs" '
        'width="1925" height="1925" loading="lazy" decoding="async"></div>'
        % package_image_map['Security package']
    ),
    '20000': (
        '<div class="quickMedia quickMedia--photo" data-package-media="20000">'
        '<img src="%s" alt="Security + Lounge — визуализация Qrator Labs" '
        'width="1536" height="1024" loading="lazy" decoding="async"></div>'
        % package_image_map['Security + Lounge']
    ),
}

for package_value, media_html in quick_package_media.items():
    placeholder = (
        f'<div class="quickMedia" data-package-media="{package_value}">'
        '<span>Фото пакета</span></div>'
    )
    if placeholder not in html:
        raise SystemExit(f'Quick package media {package_value} not found')
    html = html.replace(placeholder, media_html, 1)

# The original quick chooser used a very wide banner crop. A 6:5 frame mirrors
# the gallery cards, preserves the important content in both differently shaped
# collages, and gives both package cards identical geometry at every breakpoint.
html = html.replace(
    '.quickMedia{position:relative;aspect-ratio:16/6;min-height:150px;',
    '.quickMedia{position:relative;aspect-ratio:1.2;min-height:0;',
    1,
)
html = html.replace(
    '.quickMedia{aspect-ratio:16/7;min-height:140px}',
    '.quickMedia{aspect-ratio:1.2;min-height:0}',
    1,
)

package_css = (
    '.package{display:flex;flex-direction:column}'
    '.packageMedia{width:100%;aspect-ratio:1.2;border-radius:15px;overflow:hidden;'
    'margin:0 0 24px;background:#0b121b;border:1px solid #2f4254}'
    '.packageMedia img{width:100%;height:100%;object-fit:cover;object-position:center;'
    'display:block;background:#0b121b;image-rendering:auto}'
    '.quickMedia--photo{padding:0}.quickMedia--photo:after{display:none}'
    '.quickMedia--photo img{display:block;object-fit:contain;object-position:center;background:#0b121b;image-rendering:auto}'
    '.package ul{flex:1}'
    '@media(max-width:560px){.packageMedia{margin-bottom:20px;border-radius:13px}}'
)
if package_css not in html:
    html = html.replace('</style>', package_css + '</style>', 1)

path.write_text(html, encoding='utf-8')

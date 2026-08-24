from pathlib import Path

path = Path('site/index.html')
html = path.read_text(encoding='utf-8')

replacements = [
    (
        'Два уровня присутствия. Пакет 20 000 USDT включает весь security-пакет и дополняет его гостевой Security Lounge.',
        '<strong>Security Package представлен в двух форматах.</strong> Пакет за <strong>17 000 USDT</strong> охватывает welcome-зону, службу безопасности и ключевые точки внутри площадки. Пакет за <strong>20 000 USDT</strong> включает всё перечисленное и дополнительно предусматривает интеграцию отдельного <strong>Security Lounge</strong>.'
    ),
    (
        'Welcome-зона: стойки, виндеры, нейтральный ковер и мольберт',
        'Welcome-зона: стойки, флаги-виндеры, ковер и мольберт с постером'
    ),
    (
        'Охрана: повязки, нагрудные бейджи, опционально галстуки',
        'Охрана: повязки, нагрудные бейджи, галстуки'
    ),
    (
        'Боковой вход и минимальная айдентика хостес',
        'Легкий фирменный декор на боковом входе'
    ),
    (
        'Текстильные накладки / скатерти',
        'Накладки / скатерти на столы'
    ),
]

for old, new in replacements:
    if old not in html:
        raise SystemExit(f'Target text not found: {old}')
    html = html.replace(old, new, 1)

path.write_text(html, encoding='utf-8')

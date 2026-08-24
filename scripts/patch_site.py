from pathlib import Path

path = Path('site/index.html')
html = path.read_text(encoding='utf-8')

old = 'Два уровня присутствия. Пакет 20 000 USDT включает весь security-пакет и дополняет его гостевой Security Lounge.'
new = '<strong>Security Package представлен в двух форматах.</strong> Пакет за <strong>17 000 USDT</strong> охватывает welcome-зону, службу безопасности и ключевые точки внутри площадки. Пакет за <strong>20 000 USDT</strong> включает всё перечисленное и дополнительно предусматривает интеграцию отдельного <strong>Security Lounge</strong>.'

if old not in html:
    raise SystemExit('Target sponsorship intro text not found')

path.write_text(html.replace(old, new, 1), encoding='utf-8')

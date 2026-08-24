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
    (
        'Каждая интеграция вынесена отдельно, чтобы быстро оценить путь гостя и точки контакта.',
        'Каждую позицию мы вынесли отдельно, чтобы вы могли быстро увидеть путь гостя и все точки контакта.'
    ),
    (
        "['WELCOME','Welcome-зона','Центральный вход: стойки, виндеры, ленты и нейтральный ковер','carpet']",
        "['WELCOME','Welcome-зона','Центральный вход: стойки, виндеры, ленты и ковер','carpet']"
    ),
    (
        "['WELCOME','Ковер','Сдержанный графитовый дизайн, адаптированный к интерьеру','carpet']",
        "['WELCOME','Ковер','','carpet']"
    ),
    (
        "['SECURITY','Оградительные ленты','Айдентика в функциональном элементе зонирования','tape']",
        "['SECURITY','Оградительные ленты','Айдентика бренда в элементе зонирования','tape']"
    ),
    (
        "['BRANDING','Деревянные стойки','Аккуратное оформление существующей архитектуры','desk']",
        "['BRANDING','Деревянные стойки','Аккуратное оформление стоек хостес','desk']"
    ),
    (
        "['WELCOME','Мольберт','Информационная точка на входе','easel']",
        "['WELCOME','Мольберт','Постер на входе с информацией о партнере','easel']"
    ),
    (
        "['WELCOME','Боковой вход','Два виндера и очищенная входная композиция','flag']",
        "['WELCOME','Боковой вход','Два флага виндера','flag']"
    ),
    (
        "['SECURITY','Охрана и хостес','Повязки, бейджи, опциональный галстук, минимальные акценты','guard'],",
        ''
    ),
    (
        "['SECURITY','Аксессуары охраны','Повязка, ланьярд + бейдж, опциональный галстук','guard']",
        "['SECURITY','Аксессуары охраны','Повязка, ланьярд + бейдж, значок, галстук','guard']"
    ),
    (
        'Спокойный hospitality-слой сразу после security checkpoint: ожидание, зарядка устройств и refresh-сервис.',
        'Комфортное lounge-пространство: место, где гость может спокойно подождать, освежиться и зарядить устройства.'
    ),
    (
        "['LOUNGE','Коктейльные столы','Высокие столы для короткого ожидания','table']",
        "['LOUNGE','Коктейльные столы','+Напиток в фирменном цвете Qrator Labs','table']"
    ),
    (
        "['LOUNGE','Зона зарядки','Практичный сервис для гаджетов гостей','hub'],",
        ''
    ),
    (
        "['LOUNGE','Входная зона lounge','Спокойная визуальная навигация в lounge','flag']",
        ''
    ),
    (
        "const rows=[['Welcome-зона: стойки, виндеры, ковер, мольберт',1,1],['Оградительные ленты',1,1],['Брендинг деревянных стоек',1,1],['Охрана: повязки, бейджи, опционально галстуки',1,1],['Брендинг девайсов: планшеты, мониторы, RFID',1,1],['Боковой вход',1,1],['Хостес: минимальная айдентика',1,1],['Уютная зона ожидания',0,1],['Коктейльные столы',0,1],['Текстильные накладки / скатерти',0,1],['Charging Hub',0,1],['Refresh Station',0,1]];",
        "const rows=[['Welcome-зона: стойки, флаги-виндеры, ковер, мольберт с постером',1,1],['Оградительные ленты',1,1],['Оформление стоек хостес',1,1],['Аксессуары охраны: повязки, ланьярды + бейджи, значки, галстуки',1,1],['Брендинг девайсов: планшеты, мониторы, RFID-считыватели',1,1],['Боковой вход: два флага-виндера',1,1],['Уютная зона ожидания',0,1],['Коктейльные столы + напиток в фирменном цвете Qrator Labs',0,1],['Накладки / скатерти на столы',0,1],['Charging Hub',0,1],['Refresh Station',0,1]];"
    ),
    (
        '<div class="help">@FT_Mikhail · кнопка открывает Telegram с подготовленным текстом заявки.</div>',
        ''
    ),
    (
        '</style></head><body>',
        '''.quickSelect{margin-top:22px}.quickSelectLabel{margin:0 0 12px;color:#91a1b1;font-size:13px}.quickPackages{display:grid;grid-template-columns:1fr 1fr;gap:12px}.quickPackage{display:grid;grid-template-columns:minmax(0,1fr) auto auto;align-items:center;gap:18px;padding:17px 18px;border:1px solid #304255;border-radius:15px;background:#091724}.quickPackageName{min-width:0}.quickPackageName strong{display:block;font-size:16px}.quickPackageName span{display:block;margin-top:4px;color:#8293a3;font-size:12px}.quickPrice{white-space:nowrap;font-size:17px}.quickPick{min-height:40px;padding:0 15px;border:1px solid #52667b;border-radius:10px;background:transparent;color:#fff;font-weight:700;cursor:pointer;transition:.2s}.quickPick:hover{border-color:#8a58ff;background:#111e2d}@media(max-width:760px){.quickPackages{grid-template-columns:1fr}.quickPackage{grid-template-columns:1fr auto}.quickPick{grid-column:1/-1;width:100%}}
</style></head><body>'''
    ),
    (
        '<section class="section"><div class="wrap"><h2>Сравнение пакетов</h2><div class="compare" id="compare"></div></div></section>',
        '''<section class="section"><div class="wrap"><h2>Сравнение пакетов</h2><div class="compare" id="compare"></div><div class="quickSelect"><p class="quickSelectLabel">Выберите пакет и добавьте его в корзину</p><div class="quickPackages"><div class="quickPackage"><div class="quickPackageName"><strong>Security package</strong><span>Welcome + Security</span></div><strong class="quickPrice">17 000 USDT</strong><button class="quickPick pick" data-value="17000">Добавить</button></div><div class="quickPackage"><div class="quickPackageName"><strong>Security + Lounge</strong><span>Security package + Security Lounge</span></div><strong class="quickPrice">20 000 USDT</strong><button class="quickPick pick" data-value="20000">Добавить</button></div></div></div></div></section>'''
    ),
]

for old, new in replacements:
    if old not in html:
        raise SystemExit(f'Target text not found: {old}')
    html = html.replace(old, new, 1)

path.write_text(html, encoding='utf-8')

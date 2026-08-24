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
        '''.quickSelect{margin-top:30px}.quickSelectLabel{margin:0 0 16px;color:#91a1b1;font-size:14px}.quickPackages{display:grid;grid-template-columns:1fr 1fr;gap:18px}.quickPackage{overflow:hidden;border:1px solid #3a5065;border-radius:20px;background:linear-gradient(145deg,#0b1a29,#091521);box-shadow:0 16px 45px #0003;transition:.22s}.quickPackage:hover{transform:translateY(-2px);border-color:#6f55cc}.quickMedia{position:relative;aspect-ratio:16/6;min-height:150px;display:flex;align-items:flex-end;padding:18px;background:radial-gradient(circle at 80% 10%,#3f2d7440,transparent 38%),linear-gradient(135deg,#101d2c,#0a111a);border-bottom:1px solid #2a3e51;overflow:hidden}.quickMedia:after{content:"";position:absolute;inset:auto -8% -45% 38%;height:150%;background:linear-gradient(120deg,#2e7aff22,#8b37ef30,#d72f9b22);transform:skewX(-18deg)}.quickMedia span{position:relative;z-index:1;font-size:11px;letter-spacing:.11em;text-transform:uppercase;color:#8497aa}.quickMedia img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}.quickBody{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:18px;align-items:end;padding:22px}.quickPackageName strong{display:block;font-size:22px;letter-spacing:-.02em}.quickPackageName span{display:block;margin-top:7px;color:#8293a3;font-size:13px}.quickPrice{white-space:nowrap;font-size:25px;letter-spacing:-.02em}.quickPick{grid-column:1/-1;width:100%;min-height:48px;margin-top:2px;padding:0 18px;border:0;border-radius:11px;background:linear-gradient(100deg,#a62ce8,#326df4);color:#fff;font-weight:800;cursor:pointer;box-shadow:0 9px 26px #5025c233;transition:.2s}.quickPick:hover{filter:brightness(1.08)}@media(max-width:760px){.quickPackages{grid-template-columns:1fr}.quickMedia{aspect-ratio:16/7;min-height:140px}.quickBody{padding:18px}.quickPackageName strong{font-size:20px}.quickPrice{font-size:22px}}
</style></head><body>'''
    ),
    (
        '<section class="section"><div class="wrap"><h2>Сравнение пакетов</h2><div class="compare" id="compare"></div></div></section>',
        '''<section class="section"><div class="wrap"><h2>Сравнение пакетов</h2><div class="compare" id="compare"></div><div class="quickSelect"><p class="quickSelectLabel">Выберите пакет и добавьте его в корзину</p><div class="quickPackages"><article class="quickPackage"><div class="quickMedia" data-package-media="17000"><span>Фото пакета</span></div><div class="quickBody"><div class="quickPackageName"><strong>Security package</strong><span>Welcome + Security</span></div><strong class="quickPrice">17 000 USDT</strong><button class="quickPick pick" data-value="17000">Добавить в корзину</button></div></article><article class="quickPackage"><div class="quickMedia" data-package-media="20000"><span>Фото пакета</span></div><div class="quickBody"><div class="quickPackageName"><strong>Security + Lounge</strong><span>Security package + Security Lounge</span></div><strong class="quickPrice">20 000 USDT</strong><button class="quickPick pick" data-value="20000">Добавить в корзину</button></div></article></div></div></div></section>'''
    ),
]

for old, new in replacements:
    if old not in html:
        raise SystemExit(f'Target text not found: {old}')
    html = html.replace(old, new, 1)

path.write_text(html, encoding='utf-8')

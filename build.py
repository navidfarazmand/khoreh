"""Builds the khoreh.com site.

The pages in src/ are written the way the Claude artifact preview wants them (no <html>/<head>/<body>); this wraps
each one into a full page for GitHub Pages, with its own head (title, description, icons, link preview), and writes
the CNAME for khoreh.com.

  src/home.html         -> index.html and 404.html   Khoreh: the two games
  src/due-by-dusk.html  -> due-by-dusk/index.html    Due by Dusk, the farming game
  src/maplewick.html    -> maplewick/index.html      Maplewick, the focus game (in development)

privacy.html and support.html (Maplewick's, linked from its App Store listing), due-by-dusk/privacy.html (linked from
the Play listing) and app-ads.txt are already full files. Pages link with absolute paths (/img/..., /due-by-dusk/...),
so 404.html works at any depth.
"""
import re, pathlib

root = pathlib.Path(__file__).parent
SITE = 'https://khoreh.com'
PAGES = [
    dict(src='home.html', out=['index.html'], url='/', theme='#2B1708',
         icon='/img/khoreh-icon-64.png', touch='/img/khoreh-touch.png', image='/img/khoreh-og.png',
         desc='Khoreh makes Due by Dusk, a farming game about a very big debt, and Maplewick, a focus app for ADHD minds where your town grows while you focus.',
         og_title='Khoreh: two little worlds',
         og_desc='Due by Dusk, a farming game for Android, and Maplewick, a focus app for ADHD minds, in development.'),
    dict(src='due-by-dusk.html', out=['due-by-dusk/index.html'], url='/due-by-dusk/', theme='#5C4E94',
         icon='/due-by-dusk/img/icon-64.png', touch='/due-by-dusk/img/apple-touch-icon.png', image='/due-by-dusk/img/og.png',
         desc='Due by Dusk is a farming game for Android: swipe to cut crops, keep the chain going and pay the bills before sundown, across 30 farms in seven countries.',
         og_title='Due by Dusk: a little farm, a very big debt',
         og_desc='Swipe to cut, chain for more, pay by dusk. A farming game for Android, now in testing.'),
    dict(src='maplewick.html', out=['maplewick/index.html'], url='/maplewick/', theme='#5B2DB8',
         icon='/img/icon-64.png', touch='/img/apple-touch-icon.png', image='/img/og.png',
         desc='Maplewick is a focus app made for ADHD minds: a cozy island town that only grows while you focus. In development.',
         og_title='Maplewick: your focus builds a town',
         og_desc='A cozy island town that only grows while you focus. Made for ADHD minds. In development.'),
]


def head(title, p, extra=''):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{title}
<meta name="description" content="{p['desc']}">
<meta name="theme-color" content="{p['theme']}">
<link rel="icon" href="{p['icon']}">
<link rel="apple-touch-icon" href="{p['touch']}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Khoreh">
<meta property="og:title" content="{p['og_title']}">
<meta property="og:description" content="{p['og_desc']}">
<meta property="og:url" content="{SITE}{p['url']}">
<meta property="og:image" content="{SITE}{p['image']}">
<meta name="twitter:card" content="summary_large_image">
{extra}<style>html{{color-scheme:light dark}}body{{margin:0}}img{{max-width:100%}}[hidden]{{display:none!important}}:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}</style>
'''


def build(p, extra=''):
    src = (root / 'src' / p['src']).read_text()
    title = re.search(r'<title>.*?</title>', src).group(0)
    rest = src.replace(title, '', 1)
    cut = rest.index('</style>') + len('</style>')  # the page's own styles end the head
    return head(title, p, extra) + rest[:cut] + '\n</head>\n<body>' + rest[cut:] + '\n</body>\n</html>\n'


for p in PAGES:
    html = build(p, f'<link rel="canonical" href="{SITE}{p["url"]}">\n')
    for out in p['out']:
        f = root / out
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(html)
        print('built', out, len(html), 'bytes')
# a missing page shows the home page, but is not itself a page to index
(root / '404.html').write_text(build(PAGES[0], '<meta name="robots" content="noindex">\n'))
print('built 404.html')
(root / 'CNAME').write_text('khoreh.com\n')

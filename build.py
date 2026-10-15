"""Builds the khoreh.com site.

src/home.html is written the way the Claude artifact preview wants it (no <html>/<head>/<body>);
this wraps it into a full index.html for GitHub Pages, and writes the CNAME for khoreh.com.
privacy.html and support.html are already full pages.
"""
import re, pathlib

root = pathlib.Path(__file__).parent
body = (root / 'src' / 'home.html').read_text()
title = re.search(r'<title>.*?</title>', body).group(0)
rest = body.replace(title, '', 1)
head = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{title}
<meta name="description" content="Maplewick is a cozy island town that only grows while you focus. A free focus game made for ADHD minds.">
<meta name="theme-color" content="#5B2DB8">
<link rel="icon" href="img/icon-64.png">
<link rel="apple-touch-icon" href="img/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:title" content="Maplewick: your focus builds a town">
<meta property="og:description" content="A cozy island town that only grows while you focus. Free, no ads, made for ADHD minds.">
<meta property="og:url" content="https://khoreh.com/">
<meta property="og:image" content="https://khoreh.com/img/og.png">
<meta name="twitter:card" content="summary_large_image">
<style>html{{color-scheme:light dark}}body{{margin:0}}img{{max-width:100%}}[hidden]{{display:none!important}}:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}</style>
'''
html = head + rest.replace('<canvas id="scene"', '</head>\n<body>\n<canvas id="scene"', 1) + '\n</body>\n</html>\n'
(root / 'index.html').write_text(html)
(root / 'CNAME').write_text('khoreh.com\n')
(root / '404.html').write_text(html)
print('built index.html', len(html), 'bytes')

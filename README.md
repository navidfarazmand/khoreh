# khoreh.com

The website for Khoreh's games: a front page with both games, and one page for each.

- `index.html` (and `404.html`) is the Khoreh front page, built from `src/home.html`.
- `due-by-dusk/index.html` is the Due by Dusk page, built from `src/due-by-dusk.html`. Scrolling plays one farm day on a canvas, with the game's own crops (`due-by-dusk/img/crops`) and country skylines (`due-by-dusk/img/bands`).
- `maplewick/index.html` is the Maplewick page, built from `src/maplewick.html`. Maplewick is still in development.
- Run `python3 build.py` after changing anything in `src/`, and do not edit the built pages by hand.
- `due-by-dusk/privacy.html` is Due by Dusk's privacy policy (the Play listing links to it).
- `privacy.html` and `support.html` are Maplewick's pages for its App Store listing; they stay at the site root.
- `app-ads.txt` authorizes Google AdMob to sell ads in apps that list khoreh.com as their developer website (Due by Dusk).
- `CNAME` tells GitHub Pages to serve this site on khoreh.com.
- `src/og-khoreh.html` is the front page's link-preview image, saved as `img/khoreh-og.png`.

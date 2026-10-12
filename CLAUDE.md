# KennedyJohnson.github.io

Personal portfolio. Hand-written static site in `docs/` (`index.html`, `styles.css`, `images/`, `videos/`, résumé + capstone PDFs), served by GitHub Pages at https://kennedyjohnson.github.io. Each project card links to a live site + repo; other projects are separate repos under `C:\Users\Ken\Documents\Github\`.

## Automation
- `.github/workflows/health.yml` - weekly (Sun 14:00 UTC): `.github/scripts/health.py` checks every live project loads and its data-freshness file is within limits (the `CHECKS` table there - add new projects to it), plus lychee link check of `docs/index.html`. Failure opens a `stale-data` issue. Keepalive job keeps the cron enabled.
- `dependabot.yml` - monthly GitHub Actions updates.

## Before changing the site
- Check mobile every time, not just desktop. Before and after any change to `docs/`, load the page at 375px wide (browser pane `resize_window` mobile preset, or playwright 360px @2x), confirm no horizontal scroll (`documentElement.scrollWidth <= innerWidth`) and that text in images is readable.
- Screenshots that are wide two-panel images (`*-wide.webp`) need a narrow single-column variant (`*-mobile.webp`) served via `<picture>` with `media="(max-width:600px)"`. Render mobile variants at 360px CSS width @2x so text stays legible.
- Bump the `styles.css?v=N` and image `?v=N` cache-busters when changing them.

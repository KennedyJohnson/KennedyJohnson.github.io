# KennedyJohnson.github.io

Personal portfolio. Hand-written static site in `docs/` (`index.html`, `styles.css`, `images/`, `videos/`, résumé + capstone PDFs), served by GitHub Pages at https://kennedyjohnson.github.io. Each project card links to a live site + repo; other projects are separate repos under `C:\Users\Ken\Documents\Github\`.

## Automation
- `.github/workflows/health.yml` - weekly (Sun 14:00 UTC): `.github/scripts/health.py` checks every live project loads and its data-freshness file is within limits (the `CHECKS` table there - add new projects to it), plus lychee link check of `docs/index.html`. Failure opens a `stale-data` issue. Keepalive job keeps the cron enabled.
- `dependabot.yml` - monthly GitHub Actions updates.

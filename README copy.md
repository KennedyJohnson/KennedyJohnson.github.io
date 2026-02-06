# personalWebsite

Starter personal website scaffold. Files added:

- `index.html` — home page with projects and contact
- `resume.html` — editable resume page
- `styles.css` — starter styles with dark/light variables
- `script.js` — theme toggle + small helpers

Run locally (open `index.html` in your browser) or serve via a simple static server:

```powershell
# from this folder
python -m http.server 8000
# then open http://localhost:8000
```

To deploy on GitHub Pages:

1. Create a repo and push this folder
2. In the repository settings enable GitHub Pages (use `main` branch or `gh-pages`)

Next steps you might want me to do:

- Add a projects page with links to GitHub repos
- Convert this to a small React/Vite app or use a static site generator
- Add a downloadable PDF resume and contact form

Deployment options
------------------

1) GitHub Pages (recommended for simple static sites)

	- Create a repository and push this folder (or the site files) to the repo.
	- In GitHub repo Settings → Pages, choose the branch (`main`) and folder (`/ (root)` or `/docs`).
	- Save; the site will be available at `https://<username>.github.io/<repo>` (or your user site if using `main` on a repo named `<username>.github.io`).

2) GitHub Pages via `gh-pages` branch (automated)

	- Install `gh-pages` (for Node projects) or use a CI action to push built files to `gh-pages`.

3) Netlify / Vercel (easy drag-and-drop or connect repo)

	- Connect your GitHub repo to Netlify or Vercel and set the build settings (for plain HTML there is no build step).
	- They provide automatic deploy previews and free HTTPS.

4) Manual upload (for quick testing)

	- Serve locally with `python -m http.server` or upload files to any static host.

Compiling your LaTeX resume to PDF
----------------------------------

If you want to include a downloadable PDF on the site, compile `kenresume.tex` to `kenresume.pdf` locally and place the PDF into this folder.

Common commands (Windows with MiKTeX or any system with `pdflatex`):

```powershell
# from the repo root or the folder containing kenresume.tex
pdflatex kenresume.tex
# or run twice if you have references
pdflatex kenresume.tex
```

If you prefer Docker (isolated build):

```powershell
docker run --rm -v "%cd%":/work -w /work blang/latex pdflatex kenresume.tex
```

After compiling, copy `kenresume.pdf` to `personalWebsite/` so the `resume.html` download link works.

Need help deploying? I can:

- Create a GitHub repo and push these files for you,
- Configure GitHub Pages or create a GitHub Action to publish to `gh-pages`, or
- Deploy via Netlify/Vercel and connect a custom domain.

Edit the HTML files in this folder to customize your content and replace placeholders.

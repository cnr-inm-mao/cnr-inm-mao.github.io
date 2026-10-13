# MAO Research Group Website

This repository hosts the source code for the **MAO Research Group website**, maintained by the **Institute of Marine Engineering (CNR-INM)**.

🌐 **Live website:**
https://cnr-inm-mao.github.io/

The website is built using **MkDocs** with the **Material theme**, and automatically deployed via **GitHub Pages**.

## Structure

```
docs/        # Website pages (Markdown)
assets/      # Images, logos, and CSS
mkdocs.yml   # Site configuration
```

## Development

From the repository root, install the dependencies and regenerate the publication pages and data before starting a local preview:

```bash
pip install mkdocs mkdocs-material "bibtexparser>=1.4,<2"
python scripts/generate_publications.py
mkdocs serve
```

Then open:

```
http://127.0.0.1:8000
```

For a local production build:

```bash
python scripts/generate_publications.py
mkdocs build
```

Publication records are maintained in `data/publications.bib`, `data/conference.bib`, and `data/books.bib`. Run `python scripts/generate_publications.py` again after changing these sources, including while `mkdocs serve` is running. The generator synchronizes the publication lists, overview counts, and BibTeX/JSON assets; MkDocs alone does not regenerate them. The GitHub Actions workflow runs this generation step automatically before building the site.

## License

The source code of this website is released under the MIT License.

All website content (texts, images, and logos) is © MAO Research Group – CNR-INM unless otherwise stated.


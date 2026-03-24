from __future__ import annotations

import html
import json
import re
from collections import defaultdict
from pathlib import Path

try:
    import bibtexparser
except ImportError as e:
    raise SystemExit("bibtexparser is required. Install with: pip install bibtexparser") from e

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs"
PUBDIR = DOCS / "publications"
ASSET_DATA = DOCS / "assets" / "data"
ASSET_DATA.mkdir(parents=True, exist_ok=True)

CATEGORY_MAP = {
    "journal": DATA / "publications.bib",
    "conference": DATA / "conference.bib",
    "books": DATA / "books.bib",
}

TITLE = {
    "journal": "Journal Articles",
    "conference": "Conference Proceedings",
    "books": "Books & Book Chapters",
}

INTRO = {
    "journal": "Peer-reviewed journal publications.",
    "conference": "Conference papers and proceedings contributions.",
    "books": "Books, edited volumes, and book chapters.",
}

FILTERS = ["PME", "DMD", "UQ"]


def read_bib(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as f:
        db = bibtexparser.load(f)
    return db.entries


def year_key(entry: dict) -> int:
    try:
        return int(entry.get("year", 0))
    except ValueError:
        return 0


def sort_entries(entries: list[dict]) -> list[dict]:
    return sorted(entries, key=lambda e: (year_key(e), e.get("title", "")), reverse=True)


def split_keywords(entry: dict) -> list[str]:
    raw = entry.get("keywords", "")
    if not raw:
        return []
    parts = [p.strip() for p in re.split(r"[;,]", raw) if p.strip()]
    return parts


def infer_filters(entry: dict) -> list[str]:
    blob = " ".join(
        [
            entry.get("title", ""),
            entry.get("journal", ""),
            entry.get("keywords", ""),
        ]
    ).lower()
    tags = []
    if any(t in blob for t in ["parametric model embedding", "design-space dimensionality reduction", "physics-informed dimensionality reduction", "pme"]):
        tags.append("PME")
    if any(t in blob for t in ["dynamic mode decomposition", "hankel-dmd", "hankel dynamic mode decomposition", "dmd"]):
        tags.append("DMD")
    if any(t in blob for t in ["uncertainty quantification", "u q", " uq", "stochastic optimization"]):
        tags.append("UQ")
    return sorted(set(tags))


def format_authors(author_field: str) -> str:
    authors = [a.strip() for a in author_field.split(" and ") if a.strip()]
    formatted = []
    for a in authors:
        if "," in a:
            last, first = [p.strip() for p in a.split(",", 1)]
            initials = " ".join(part[0] + "." for part in first.replace("-", " ").split() if part)
            name = f"{initials} {last}".strip()
        else:
            name = a
        name = html.escape(name)
        formatted.append(name)
    return ", ".join(formatted)


def format_venue(entry: dict) -> str:
    parts = [html.escape(entry.get("journal", ""))]
    if entry.get("volume"):
        vol = html.escape(entry["volume"])
        if entry.get("number"):
            vol += f"({html.escape(entry['number'])})"
        parts.append(vol)
    elif entry.get("number"):
        parts.append(f"({html.escape(entry['number'])})")
    if entry.get("pages"):
        parts.append(html.escape(entry["pages"]))
    if entry.get("year"):
        parts.append(html.escape(entry["year"]))
    return ", ".join([p for p in parts if p])


def link_html(entry: dict) -> str:
    links = []

    if entry.get("doi"):
        doi = html.escape(entry["doi"])
        links.append(
        f'''<a class="pub-icon doi"
               href="https://doi.org/{doi}"
               target="_blank"
               rel="noopener noreferrer"
               title="DOI">
               <img src="../../assets/icons/doi.svg" alt="DOI" width="14" height="14">
            </a>'''
            )

    if entry.get("ID"):
        key = html.escape(entry["ID"])
        links.append(
        f'''<a class="pub-icon bibtex"
               href="../../assets/data/publications.bib#key-{key}"
               title="BibTeX">
               <img src="../../assets/icons/bibtex.svg" alt="BibTeX" width="16" height="16">
            </a>'''
            )
    return "".join(links)

def render_entry(entry: dict) -> str:
    title = html.escape(entry.get("title", "Untitled"))
    authors = format_authors(entry.get("author", ""))
    venue = format_venue(entry)
    filters = infer_filters(entry)
    keywords = sorted(set(filters + split_keywords(entry)))
    data_keywords = " ".join(k.lower() for k in keywords)
    tags_html = "".join(f'<span class="pub-tag">{html.escape(tag)}</span>' for tag in filters)
    return f'''<article class="pub-item" data-year="{html.escape(entry.get("year", ""))}" data-keywords="{html.escape(data_keywords)}">
  <div class="pub-title">{title}</div>
  <div class="pub-authors">{authors}</div>
  <div class="pub-venue"><i>{venue}</i></div>
  <div class="pub-meta">{tags_html}</div>
  <div class="pub-links">{link_html(entry)}</div>
</article>'''


def render_page(kind: str, entries: list[dict]) -> str:
    title = TITLE[kind]
    intro = INTRO[kind]
    if not entries:
        body = f"# {title}\n\n{intro}\n\nContent will be added soon.\n"
        return body

    by_year = defaultdict(list)
    for e in sort_entries(entries):
        by_year[e.get("year", "Unknown")].append(e)

    sections = []
    if kind == "journal":
        filter_buttons = ''.join(
            f'<button class="pub-filter-button" type="button" data-filter="{f.lower()}">{f}</button>' for f in FILTERS
        )
        sections.append(
            f'''<div class="pub-toolbar">
  <input id="pub-search" class="pub-search" type="search" placeholder="Search title, authors, venue..." aria-label="Search publications">
  <div class="pub-filters">
    <button class="pub-filter-button is-active" type="button" data-filter="all">All</button>
    {filter_buttons}
  </div>
</div>'''
        )

    for year in sorted(by_year.keys(), reverse=True):
        items = "\n".join(render_entry(e) for e in by_year[year])
        sections.append(f"## {year}\n\n<div class=\"pub-list\">\n{items}\n</div>")

    return f"# {title}\n\n{intro}\n\n" + "\n\n".join(sections) + "\n"


def render_index(stats: dict[str, int]) -> str:
    return f'''# Publications

<div class="card-grid">

  <div class="info-card">
    <h3><a href="journal/">Journal Articles</a></h3>
    <p>Peer-reviewed journal publications.</p>
    <p><strong>{stats.get('journal', 0)}</strong> entries</p>
  </div>

  <div class="info-card">
    <h3><a href="conference/">Conference Proceedings</a></h3>
    <p>Conference papers and proceedings contributions.</p>
    <p><strong>{stats.get('conference', 0)}</strong> entries</p>
  </div>

  <div class="info-card">
    <h3><a href="books/">Books &amp; Book Chapters</a></h3>
    <p>Books, edited volumes, and book chapters.</p>
    <p><strong>{stats.get('books', 0)}</strong> entries</p>
  </div>

</div>

The lists are generated automatically from BibTeX sources and sorted by year.
'''


def write_bib_index(path: Path):
    if not path.exists():
        return
    lines = []
    for line in path.read_text(encoding='utf-8').splitlines():
        m = re.match(r'@\w+\{([^,]+),', line)
        if m:
            lines.append(f'<a id="key-{m.group(1)}"></a>')
        lines.append(html.escape(line))
    out = ASSET_DATA / path.name
    out.write_text("\n".join(lines), encoding='utf-8')


def main() -> None:
    stats = {}
    for kind, path in CATEGORY_MAP.items():
        entries = read_bib(path)
        stats[kind] = len(entries)
        (PUBDIR / f"{kind}.md").write_text(render_page(kind, entries), encoding="utf-8")
        if path.exists():
            write_bib_index(path)
    (DOCS / "publications.md").write_text(render_index(stats), encoding="utf-8")
    payload = {kind: [e for e in sort_entries(read_bib(path))] for kind, path in CATEGORY_MAP.items()}
    (ASSET_DATA / 'publications.json').write_text(json.dumps(payload, indent=2), encoding='utf-8')


if __name__ == "__main__":
    main()

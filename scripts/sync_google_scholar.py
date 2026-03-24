from __future__ import annotations

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description='Fetch publications from a public Google Scholar profile and export a BibTeX draft.')
    parser.add_argument('--user-id', required=True, help='Google Scholar user id, e.g. _Tz_sf8AAAAJ')
    parser.add_argument('--output', default='data/publications_scholar.bib')
    args = parser.parse_args()

    try:
        from scholarly import scholarly
    except ImportError as e:
        raise SystemExit('Install scholarly first: pip install scholarly') from e

    author = scholarly.search_author_id(args.user_id)
    author = scholarly.fill(author, sections=['publications'])
    publications = author.get('publications', [])

    out = []
    for i, pub in enumerate(publications, start=1):
        filled = scholarly.fill(pub)
        bib = filled.get('bib', {})
        title = bib.get('title', f'untitled_{i}')
        year = bib.get('pub_year', '')
        venue = bib.get('venue', '')
        author_field = bib.get('author', '')
        key = f"scholar{year}_{i}"
        lines = [f"@article{{{key},", f"  title = {{{title}}},"]
        if author_field:
            lines.append(f"  author = {{{author_field}}},")
        if venue:
            lines.append(f"  journal = {{{venue}}},")
        if year:
            lines.append(f"  year = {{{year}}},")
        url = filled.get('pub_url') or filled.get('author_pub_id')
        if url:
            lines.append(f"  url = {{{url}}},")
        lines[-1] = lines[-1].rstrip(',')
        lines.append('}')
        out.append('\n'.join(lines))

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text('\n\n'.join(out) + '\n', encoding='utf-8')
    print(f'Wrote {len(out)} entries to {output}')
    print('Review the exported file before merging it into data/publications.bib. Google Scholar scraping can be incomplete or rate-limited.')


if __name__ == '__main__':
    main()

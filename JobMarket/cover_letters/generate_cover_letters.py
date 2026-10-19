#!/usr/bin/env python3
"""Generate one personalized cover letter per application.

Reads applications.csv, picks the macro or finance template, fills the three
bracketed placeholders and writes letters/NN_slug_letter.tex. Everything outside
the placeholders is copied byte for byte from the template; the archived draft
inside \\begin{comment} ... \\end{comment} is left untouched.

Usage:
    python3 generate_cover_letters.py          # write .tex files only
    python3 generate_cover_letters.py --pdf    # also compile each letter with pdflatex into pdf/
    python3 generate_cover_letters.py --only 12 29   # restrict to the given ids
"""
import argparse
import csv
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CSV = HERE / "applications.csv"
TEMPLATES = {
    "macro": HERE / "templates" / "cover_letter_macro.tex",
    "finance": HERE / "templates" / "cover_letter_finance.tex",
}
TEX_DIR = HERE / "letters"
PDF_DIR = HERE / "pdf"

OPEN = "[POSITION] at [INSTITUTION]"
CLOSE = "[INSTITUTION]"
FIT = "[FIT for the INSTITUTION -- for places with strong interest; brief, one paragraph]"
COMMENT = "\\begin{comment}"


def fill(template: str, row: dict) -> str:
    body, sep, archived = template.partition(COMMENT)
    if body.count(OPEN) != 1 or body.count(CLOSE) != 2 or body.count(FIT) != 1:
        raise ValueError("template placeholders changed; update generate_cover_letters.py")
    body = body.replace(OPEN, f"{row['position_phrase']} at {row['institution_opening']}")
    body = body.replace(CLOSE, row["institution_closing"])
    fit = row["fit_paragraph"].strip()
    body = body.replace("\n\n" + FIT + "\n\n", ("\n\n" + fit + "\n\n") if fit else "\n\n")
    return body + sep + archived


def compile_pdf(tex: Path) -> bool:
    PDF_DIR.mkdir(exist_ok=True)
    build = PDF_DIR / "_build"
    build.mkdir(exist_ok=True)
    for _ in range(2):
        r = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
             "-output-directory", str(build), str(tex)],
            capture_output=True, text=True,
        )
        if r.returncode != 0:
            print(f"  pdflatex FAILED for {tex.name}; see {build / (tex.stem + '.log')}", file=sys.stderr)
            return False
    shutil.copy(build / (tex.stem + ".pdf"), PDF_DIR / (tex.stem + ".pdf"))
    return True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", action="store_true", help="compile each letter with pdflatex")
    ap.add_argument("--only", nargs="*", help="application ids to generate (default: all)")
    args = ap.parse_args()

    templates = {k: p.read_text(encoding="utf-8") for k, p in TEMPLATES.items()}
    TEX_DIR.mkdir(exist_ok=True)
    with CSV.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    if args.only:
        wanted = {x.zfill(2) for x in args.only}
        rows = [r for r in rows if r["id"] in wanted]

    failed = []
    for row in rows:
        out = TEX_DIR / f"{row['id']}_{row['slug']}_{row['letter']}.tex"
        out.write_text(fill(templates[row["letter"]], row), encoding="utf-8")
        print(f"{out.name:60s} {row['institution']}")
        if args.pdf and not compile_pdf(out):
            failed.append(out.name)
    print(f"\n{len(rows)} letters written to {TEX_DIR}")
    if args.pdf:
        print(f"{len(rows) - len(failed)} PDFs in {PDF_DIR}" + (f"; FAILED: {failed}" if failed else ""))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())

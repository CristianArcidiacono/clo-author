# Plan: Personalized job market cover letters

**Status:** APPROVED (user request, autonomous session)
**Date:** 2026-10-19

## Goal
Produce one personalized cover letter (.tex, compiled to PDF) for each of the 84 applications in
`JobMarket/Arcidiacono_reference_letters_2026-27.xlsx`, from the two uploaded templates
(macro, finance). Only the bracketed placeholders change; the rest of each letter is byte-identical.

## Approach
1. `JobMarket/cover_letters/templates/` holds the two uploaded templates untouched.
2. `JobMarket/cover_letters/applications.csv` lists every application with the text that fills
   `[POSITION]`, the two `[INSTITUTION]` slots, and the optional fit paragraph.
   Letter choice: track "Academic · Finance" -> finance template; everything else
   (Macro/economics, Policy, Fellowship, Research institute) -> macro template.
   Fit paragraph: Priority A rows plus two Priority B rows with a personal tie
   (LSE Finance, Geneva GSEM). Other rows drop the placeholder paragraph.
3. `JobMarket/cover_letters/generate_cover_letters.py` reads the CSV and writes
   `letters/NN_slug_macro|finance.tex`; replacements are restricted to the live letter body
   (the old draft inside `\begin{comment}` is left as is).
4. Compile every letter with pdflatex; check page counts, overfull boxes, leftover brackets.

## Verification
- 84 .tex files written, 84 PDFs compile without errors.
- `diff` of a generated letter against its template shows changes only on the three placeholder lines.
- No `[` placeholder left in the live body (Humboldt host is the one deliberate exception).

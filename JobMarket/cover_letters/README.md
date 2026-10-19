# Job market cover letters (2026–27)

One personalized letter per application in `../Arcidiacono_reference_letters_2026-27.xlsx`.

| Path | What it is |
|------|------------|
| `templates/cover_letter_macro.tex`, `templates/cover_letter_finance.tex` | The two master letters, unchanged. Edit these to change the shared text. |
| `applications.csv` | One row per application: which template, the text for `[POSITION]`, the two `[INSTITUTION]` slots, and the optional fit paragraph. Values are LaTeX (e.g. `Texas A\&M`). |
| `generate_cover_letters.py` | Fills the placeholders and writes `letters/NN_slug_macro|finance.tex`; `--pdf` also compiles to `pdf/`. |
| `letters/` | Generated `.tex` files (regenerate, do not hand-edit). |
| `pdf/` | Compiled letters. |

## Rules used

- **Template choice:** track "Academic · Finance" gets the finance letter; macro/economics, policy,
  fellowship and research-institute rows get the macro letter.
- **Fit paragraph:** written for every Priority A row, plus LSE Finance and Geneva GSEM (personal ties).
  All other rows drop the placeholder paragraph. To add one, fill `fit_paragraph` in the CSV and rerun.
- **Humboldt (row 47):** the host is still to be chosen, so the letter keeps `[HOST INSTITUTION]`.

## Regenerate

```bash
python3 generate_cover_letters.py --pdf          # everything
python3 generate_cover_letters.py --pdf --only 12 29   # just BIS MED and Bocconi Finance
```

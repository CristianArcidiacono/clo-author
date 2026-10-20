# Job market cover letters (2026–27)

One personalized letter per application in `../Arcidiacono_reference_letters_2026-27.xlsx` (141 rows, version of 19 October 2026).
Files are named `ARCIDIACONO_Cristian_CL_<Place>.tex` / `.pdf`, with underscores instead of spaces; the place part is the `file_name` column of the CSV.

| Path | What it is |
|------|------------|
| `templates/cover_letter_macro.tex`, `templates/cover_letter_finance.tex` | The two master letters, unchanged. Edit these to change the shared text. |
| `applications.csv` | One row per application (`id` = row number in the spreadsheet): which template, the output `file_name`, the text for `[POSITION]`, the two `[INSTITUTION]` slots, and the optional fit paragraph. Values are LaTeX (e.g. `Texas A\&M`). |
| `generate_cover_letters.py` | Fills the placeholders and writes `letters/ARCIDIACONO_Cristian_CL_<file_name>.tex`; `--pdf` also compiles to `pdf/`; `--clean` removes previously generated files first. |
| `letters/` | Generated `.tex` files (regenerate, do not hand-edit). |
| `pdf/` | Compiled letters. |

## Rules used

- **Template choice:** track "Academic · Finance" gets the finance letter; macro/economics, policy,
  fellowship and research-institute rows get the macro letter.
- **Fit paragraph:** every finance letter has one. Macro letters have one for the Priority A rows of the
  first spreadsheet version, for Geneva GSEM (personal tie), and for added rows whose ad names Cristian's
  fields explicitly (Danmarks Nationalbank, IE Economics, DePaul Economics, Rochester, UT Austin).
  Other macro rows drop the placeholder paragraph. To add one, fill `fit_paragraph` in the CSV and rerun.
- **Spacing:** both templates use `\onehalfspacing`.

## Regenerate

```bash
python3 generate_cover_letters.py --pdf --clean        # everything, removing stale files first
python3 generate_cover_letters.py --pdf --only 16 35   # just rows 16 (BIS) and 35 (Bocconi Finance)
```

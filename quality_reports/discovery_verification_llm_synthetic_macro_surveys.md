# Discovery Verification — LLM Synthetic Macro Surveys

**Date:** 2026-11-22
**By:** orchestrator, after network access to arxiv.org and ec.europa.eu was granted
**Purpose:** close the decision-critical unverified items raised by explorer-critic (V1, V2, V4) and librarian-critic (issue 1) by reading primary sources. Everything below was read or computed directly from the source named; nothing is from search snippets.

---

## 1. Competitor papers read in full

### Anesti, Hill and Joseph, "Inflation Attitudes of Large Language Models" (arXiv 2512.14306, 16 Dec 2025)
- **Model:** GPT-3.5-turbo-0613 only (cutoff September 2021).
- **Survey:** Bank of England Inflation Attitudes Survey, UK only, two waves (November 2022, February 2023).
- **Targets:** inflation perceptions and expectations at 1, 2 and 5 years. These are the banded percentage questions ("gone down by 1-2%" ... "risen by more than 15%"), mapped to interval midpoints and treated as numbers. Not sentiment or purchase items.
- **Elicitation:** direct multiple choice ("Please choose one option, no explanation"), options scrambled per respondent. No free text, no embedding mapping.
- **Conditioning:** demographics (gender, age, income, tenure, social class, region) plus the three-month average of year-on-year inflation for food, restaurants, energy and other CPIH components.
- **Out-of-time logic:** the waves postdate the cutoff, so supplying post-cutoff inflation data is treated as a quasi-experimental information treatment.
- **Reported weakness:** individual-level correlation with humans is low; a high temperature (1.5) is needed to match dispersion, with side effects.

**Implication.** This is the paper to beat on design, but it does not occupy our target. Open relative to it: qualitative five-option items, free-text plus SSR elicitation, many countries, many waves, several models. Worth borrowing: giving personas a dated information set of recent price data.

### Huang et al., "HouseholdBench" (arXiv 2610.07563, 6 Oct 2026)
- **Authors confirmed:** Huang, Ferreras Garrucho, Xie, Yuan, Mei, Lian, Hazell. arXiv ID and date are correct. The NBER number was not checked.
- **Scope:** six US surveys (CEX, CPS, Michigan, SCE, PSID, Census), 32 tasks, 13 models.
- **Task type:** individual-level prediction of a respondent's answer from past behaviour, demographics and macro conditions, scored against a no-change baseline and gradient-boosted trees. Macro-expectation tasks are numeric inflation expectations (Michigan) and probabilities (SCE).
- **Leakage handling:** everything released after 16 February 2026 is held out as a post-cutoff test set.
- **Findings relevant to us:** most models beat no-change; boosted trees usually rank first; fine-tuning and averaging 16 draws lifts a small open model to proprietary level.

**Implication.** US only, individual-level, direct elicitation. It does not cover aggregate answer shares, Europe, or SSR. It sets the standard a referee will expect: a no-change baseline, a statistical benchmark, and a dated post-cutoff split.

### Maier et al., SSR paper (arXiv 2510.08338)
- **Authors confirmed:** Maier, Aslak, Fiaschi, Rismal, Fletcher, Luhmann, Dow, Pappas, Wiecki.
- **Models:** GPT-4o and Gemini-2.0-flash, temperature 0.5; embeddings from text-embedding-3-small.
- **What SSR actually buys:** direct Likert rating already reaches about 80% correlation attainment; SSR reaches about 88-90%. The large gain is in distributional similarity (KS similarity 0.26-0.39 direct vs 0.80-0.88 SSR). SSR is mainly a fix for too-narrow response distributions.
- **Caution:** mean purchase intent across the 57 surveys is 4.0 with standard deviation 0.1, so the ranking test is over a narrow range. Without demographics the model matched the distribution but lost ranking ability.

---

## 2. European Commission consumer survey: files inspected

Source: DG ECFIN time-series download page, release of 26 October 2026 (`nace2_ecfin_2610`).

| Item | Result |
|---|---|
| **V1. Answer shares for totals** | **Confirmed.** `datashares_consumers_nsa_m_nace2.xlsx` holds monthly, non-seasonally-adjusted shares for each answer option (PP, P, E, M, MM, N = don't know) for Q1-Q9, Q11, Q12, for 33 countries plus EU and EA, from January 1985 to October 2026. |
| **V2. Answer shares by demographic group** | **Negative.** The "Categories" files hold balances only (series codes end in `.BS.M` or `.B.M`). Groups available: income quartile (RE1-4), occupation (PR0-9), education (ED1-3), age (AG1-4), sex, plus work-status groups. No answer shares, no cell sizes. |
| Balance definition | User guide: B = (PP + ½P) − (½M + MM). A synthetic distribution can be collapsed to a balance, so demographic validation is possible in this degraded form. |
| Verbatim questionnaire | In `bcs_user_guide.pdf`, Annex 2.3.1 and section 3.6. Confirmed wording for Q1, Q2, Q4, Q9 (five options plus don't know). National-language versions not checked. |
| Breaks in the window | INFO sheet: Poland changed provider in May 2026 (data replaced back to 2018, possible break in shares); Estonia suspended from May 2026. Spain's reported May 2025 break was not re-checked. |

---

## 3. How much do shares move after a plausible cutoff? (V4, first look)

Computed from the totals file for 30 countries. Baseline = each series' mean over January-June 2025; evaluation window = July 2025 to October 2026 (16 waves). Pooled over answer options, excluding don't know.

| Question | Topic | Cross-country SD of baseline levels (pp) | RMS deviation from baseline in window (pp) | Variance explained by baseline |
|---|---|---|---|---|
| Q1 | Financial situation, past | 16.5 | 3.3 | 0.96 |
| Q2 | Financial situation, expected | 17.1 | 3.2 | 0.97 |
| Q3 | General economy, past | 13.9 | 4.8 | 0.89 |
| Q4 | General economy, expected | 12.5 | 4.6 | 0.88 |
| Q5 | Prices, past | 18.7 | 5.0 | 0.92 |
| Q6 | Prices, expected | 13.4 | 5.6 | 0.85 |
| Q7 | Unemployment, expected | 14.7 | 3.9 | 0.93 |
| Q8 | Major purchases, now | 18.0 | 4.2 | 0.95 |
| Q9 | Major purchases, next 12 months | 14.0 | 3.0 | 0.95 |
| Q11 | Savings, next 12 months | 12.7 | 2.9 | 0.95 |
| Q12 | Household financial statement | 18.0 | 2.3 | 0.98 |

**Reading.** A "last known value" forecast explains 85-98% of the variance in post-cutoff shares. Both critics' concern is confirmed with data: matching post-cutoff levels proves almost nothing. The usable signal is the 2-6 percentage point movement around the baseline, against sampling error of roughly 1-1.5 points for a share at typical national sample sizes (nominal sizes not yet tabulated per country). The general-economy and price questions (Q3-Q6) move most and are the best targets. The variance-explained figure is inflated by pooling across answer options; a per-option version should replace it in any strategy memo.

---

## 4. Consequences for the design

1. The cross-country totals design is feasible as specified: shares exist, are public, and are current to last month.
2. The demographic dimension cannot be validated on answer shares with EC data. Options: validate demographic groups on balances only; or use microdata (ECB CES, NY Fed SCE) for the demographic dimension. CES facts (V3) remain unverified.
3. The headline metric must be skill over a no-change baseline on changes, not fit to levels.
4. Still open: V3 (CES), V5 (full break list), V6 (effective sample sizes), choice of reference models and their cutoffs.

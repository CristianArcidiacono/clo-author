# Discovery Critic Reviews — LLM Synthetic Macro Surveys

**Date:** 2026-11-22
**Phase:** Discovery (severity: LOW)
**Project idea:** transfer semantic similarity rating (Maier et al. 2025, arXiv 2510.08338) to macro household expectation surveys, validated on post-cutoff waves.

Condensed from the critics' reports as returned to the orchestrator. Neither critic had network access; both reviewed the reports only and did not check claims against sources.

---

## 1. explorer-critic — data assessment

**Target:** `quality_reports/data_exploration_llm_synthetic_macro_surveys.md`
**Score:** 82/100 (round 1, passes the 80 gate)
**Verdict:** Sound and honestly labelled. The EC survey holds as primary for country x month totals, but the demographic dimension and the noise ceiling rest on unverified facts. Do not commit to the EC survey as primary until V1-V4 are confirmed.

### Deductions
| Issue | Points |
|---|---|
| Out-of-sample validation compatibility only partly checked | -5 |
| Noise-ceiling logic wrong in direction and level | -4 |
| Compound failure case not traced; ranking inconsistent with fallback role | -3 |
| Population definition and aggregation weights not addressed | -3 |
| External validity only implicit | -3 |

### Issues
1. **Validation compatibility.** No count of post-cutoff waves under plausible model cutoffs. Answer shares are persistent and cross-country levels are in pre-cutoff training data, so a model can match post-cutoff shares from memorised levels. The real test is on changes relative to a persistence baseline; the report never asks whether 2025-26 shares move enough. Some items look near-degenerate (e.g., Japan, 93.6% expecting price rises). EC breaks beyond Spain (May 2025) are uncounted.
2. **Noise ceiling.** A panel re-interview ceiling understates reliability, which flatters the LLM (not "conservative"). It is also an individual-level quantity, while the target is an aggregate cell share. The EC survey has no microdata, so no split-sample ceiling; cell n, design effects and weights by demographic category are not established. CES as a second human measurement gives a house-plus-wording effect, not a clean ceiling.
3. **Compound failure.** If EC demographic cells are balances only and CES is late or coarsened, validation shrinks to US SCE through about February 2026 with cells of 100-400: no longer a cross-country design. For the demographic dimension CES is the de facto primary. Unexplored: collapsing the synthetic distribution to a balance as a degraded test; national-partner microdata.
4. **Population and weights.** EC cells are one-way margins; the source of the joint demographic composition for personas and aggregation is unstated. Reference populations differ across sources.
5. **External validity.** The window is a single macro regime (post-inflation-surge). Transfer of SSR to asymmetric, non-Likert scales (EC Q5/Q6) limits which questions results generalise to.

### Facts to confirm before committing to the primary benchmark
- **V1.** EC "Detailed data by answer category (totals)" file: covers Q1-Q9 for all countries, not seasonally adjusted, includes "don't know", updated monthly through late 2026.
- **V2.** Whether the EC "Categories" file holds answer shares or balances only by age, income, education, sex; whether cell n or weights exist anywhere.
- **V3.** ECB CES public-use file: latest wave and lag, demographics retained, access conditions, verbatim qualitative items and scales.
- **V4.** Reference LLM cutoff date(s), resulting count of post-cutoff waves per source, and whether shares move over that window.
- **V5.** Full list of EC country-level breaks from 2024 onward.
- **V6.** Per-country effective sample sizes and survey modes.

Not blocking the benchmark choice: verbatim EC wording in national languages (blocks prompt and anchor writing); SCE qualitative item wording and latest microdata month; BoE/Ipsos reuse clause; Japan CCS shares by household attribute.

### Scenario table
| Scenario | Consequence |
|---|---|
| EC demographic shares are balances only | EC stays first for country x month totals; the demographic dimension moves to CES and SCE, and CES becomes co-primary |
| The above, and CES is late or coarsened | Cross-country demographic design fails; what remains is a totals paper plus US-only demographic validation. Scope decision for the user |
| EC totals-by-answer-category file is incomplete, not monthly, or lacks "don't know" | Primary recommendation fails entirely |
| More EC countries than Spain have 2024-26 breaks | Usable country count shrinks; cross-country claim weakens |
| SCE qualitative wording is wrong | SCE becomes mainly a quantitative source |

**Escalation question if V1 or V2+V3 come back negative:** narrow to country x month totals, or accept demographic validation on a smaller, lagged set of microdata sources?

---

## 2. librarian-critic — literature review

**Target:** `quality_reports/lit_review_llm_synthetic_macro_surveys.md`
**Score:** 78/100 (round 1, below the 80 gate; strike 1 of 3)
**Verdict:** Candid, well organised and current. The "gap is open" claim is a search-hit absence, not an established fact, and it leans on a numeric-vs-qualitative contrast that the Bank of England paper may already break. One targeted round should clear the gate.

### Deductions
| Issue | Points |
|---|---|
| Human-side foundations for the actual target questions missing | -5 |
| Methods literature partially covered | -3 |
| Over 50% unpublished (about 37 of 59 entries) | -3 |
| Scope too narrow in two places | -5 |
| Proximity scores mildly inconsistent | -2 |
| Annotated items with no BibTeX entry | -4 |

### Issues
1. **Gap claim hardens between §2 and §3.** Anesti, Hill and Joseph (BoE SWP 1190 / arXiv 2512.14306) is the main threat: the BoE Inflation Attitudes Survey is largely banded and qualitative, so that paper may already validate against categorical shares by subgroup with a cutoff-based out-of-time test, leaving only cross-country coverage and SSR as differentiators. Lin, Sun and Yan and HouseholdBench are also unresolved. Searches were too narrow (no "consumer confidence", "consumer sentiment", "open-ended elicitation", "embedding mapping"). Post-cutoff novelty is a difference of degree. Safe wording for now: "no paper located".
   Read in full, in order: Anesti-Hill-Joseph; HouseholdBench; Lin-Sun-Yan v4; Zarifhonarvar (JME version); Wu-Xi-Xie; arXiv 2610.29645; Vera Pichardo (2602.13862); arXiv 2608.30522.
2. **Post-cutoff validation does not remove leakage of persistent cross-sectional structure.** With 12-18 post-cutoff waves most validation variance is cross-sectional, which is the memorised part. The positioning must say what is evaluated beyond memorised levels: changes, turning points, skill over last-wave and country-group fixed-effect baselines. A referee will raise this first.
3. **Theme 4 covers inflation expectations only**, but the target questions are consumer-confidence items. Missing (from the critic's memory, to be verified): Carroll-Fuhrer-Wilcox 1994; Ludvigson 2004; Barsky-Sims 2012; Batchelor-Orr 1988; Pesaran-Weale 2006; Nardo 2003; Duca-Radu-Kenny-Reuter 2021; Andrade-Gautier-Mengus 2023; Das-Kuhnen-Nagel 2020; D'Acunto-Malmendier-Weber 2021; Bruine de Bruin et al. 2010; DG ECFIN BCS User Guide; ECB Occasional Paper 287. Unsearched leads: Carroll 2003; Coibion-Gorodnichenko 2015; Bachmann-Berg-Sims 2015; Andre et al. 2022.
4. **Two adjacent LLM literatures absent.** (a) Predicting subgroup answer-option distributions: Kim-Lee 2023; Suh et al. 2025 (SubPOP); Meister-Guestrin-Hashimoto; Cao et al. 2025. (b) Cross-country and multilingual fidelity: Durmus et al. 2023 (GlobalOpinionQA); von der Heyde-Haensch-Wenz; Qu-Wang 2024; Atari et al. Smaller gaps: post-cutoff forecasting evaluation (Halawi et al.; ForecastBench; Paleka et al.; Schoenegger et al.), prediction-powered inference, response-bias critiques (Tjuatja et al.).
5. **Positioning not yet sharp.** It is a combination of three design features, not a question. Sharper candidates: does SSR fix under-dispersion against a public multi-country benchmark; do personas add anything for households given the null for professionals; is there skill over persistence. Name the paper to beat (currently Anesti et al.).

### Citations needing verification
- **Number inconsistent with date:** Huang et al., HouseholdBench, NBER WP 35927 (trend implies about 35,770 today); arXiv 2610.07563 dated 6 October 2026.
- **Beyond the critic's knowledge, specific numbers from snippets:** Graham-Harvey-Jha (arXiv 2606.13812); Alam et al. (FRBSF WP 2026-04 / CEPR DP 21057); Vera Pichardo (2602.13862); Lukauskas-Šarkauskaitė (2608.14606); Taday Morocho et al. (2602.18462); Kelly et al. (NBER 35247); Krsteski et al.; Collodel (CB Malta WP 4/26); Wohlfart (ECONtribute DP 402); Zarifhonarvar JME 157, 103859; Kazinnik Management Science DOI.
- **No authors or thin provenance, do not cite until resolved:** arXiv 2608.30522; 2610.29645; 2605.24564; 2610.04412; Utama-Andina-Oktavia; Yan-Tang "DatedGPT"; six title-only arXiv leads (2609.07305, 2606.09013, 2607.26348, 2608.29455, 2611.00256, 2610.25158); the Prolific preprint; the Cleveland Fed discussant deck.
- **Likely corrections (confirm):** Wang-Morgenstern-Dickerson in Nature Machine Intelligence 2025; Coibion-Georgarakos-Gorodnichenko-Weber in JEEA 21(5) 2023; He-Lv-Manela-Wu has four authors; Drinkall et al. author list and venue; StoriesLM authorship; Gui-Toubia venue; which RCT Wu-Xi-Xie replicate.

### What clears the gate in round 2
1. Read the competitors in full, or downgrade the gap wording.
2. Add the consumer-confidence and qualitative-survey block and the two missing LLM literatures.
3. Resolve the NBER 35927 number.
4. Restate the positioning around persistence and memorised levels, with Anesti et al. as the named benchmark.

---

## 3. librarian-critic — literature review, round 2

**Score:** 92/100 (round 1: 78). Gate cleared; no strike 2.
**Verdict:** Coverage and positioning are now sound; what remains is syncing the text to the verified facts and cleaning the bibliography. The critic checked no citation against sources.

### Deductions
| Issue | Points |
|---|---|
| Methods: nothing on inference for skill over a no-change baseline (Diebold-Mariano, Clark-West, Giacomini-White; scoring rules for categorical shares) | -3 |
| Eight BibTeX entries with empty author placeholders | -2 |
| [V] tags on entries whose author names are admitted unconfirmed | -2 |
| Two proximity scores off the stated rule (Bybee, Lukauskas) | -1 |

All round 1 deductions were judged cleared or largely cleared.

### Contradictions with `discovery_verification_llm_synthetic_macro_surveys.md` (not penalised)
1. Anesti et al. target format is still described as unresolved; it is verified (banded percentages treated as numbers, direct multiple choice, GPT-3.5, two waves).
2. HouseholdBench's six surveys are now known; its macro tasks are numeric or probabilistic.
3. The contribution statement promises answer distributions across demographic groups; EC demographic files hold balances only.
4. Maier et al. author list is confirmed; the review omits that direct rating already reaches about 80% correlation attainment.
5. EC file has 33 countries, not a 27-country panel.

### Open
1. Add the forecast-evaluation and scoring-rule methods block.
2. Update Sections 1A, 2, 3, 4 to the verified facts.
3. Fill or remove placeholder BibTeX authors; align [V] tags.
4. Note that Anesti et al. needed temperature 1.5 to match dispersion.
5. Resolve the Zarifhonarvar JME page and the HouseholdBench NBER number.

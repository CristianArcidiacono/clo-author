# Literature Review: LLM Synthetic Respondents for Macroeconomic Household Surveys (SSR Transfer)

**Agent:** librarian | **Phase:** Discovery | **Date:** 2026-11-22
**Status:** Round 2 revision (round 1 scored 78/100 by librarian-critic; this version awaits re-review). Changes are listed in Section 6.

## 0. How to read this file

**Evidence standard.** Network access was limited to web search; no paper full text was opened in either round (arxiv.org and most hosts are blocked for fetching). Every entry therefore rests on search-result snippets (abstract pages, RePEc/NBER/publisher listings). Each entry carries a verification tag:

- **[V]** bibliographic details confirmed by a search result from a primary listing (publisher, NBER, RePEc, arXiv, ACL Anthology, central bank site).
- **[V-partial]** paper confirmed to exist; one or more details (authors, venue, numbers) come only from a secondary source or are inconsistent across sources. The uncertain detail is named.
- **[U]** not confirmed by any search; marked `% UNVERIFIED` in BibTeX. Do not cite before checking.

Summaries describe abstracts, not full papers. Magnitudes are quoted only where a snippet reported them. Anything about a paper's internal design that the abstract did not state is flagged as not established. Items with no retrievable authors or thin provenance are held in a separate list (Section 1L, "Leads, do not cite") and have no BibTeX entry.

**Proximity score** (1-5), applied with one rule per level:
- 5 = simulates or predicts household survey answers on economic expectations (direct competitor).
- 4 = LLM-simulated respondents for another economic survey population (forecasters, CFOs, depositors) or for central bank communication to households.
- 3 = same method in a different context, a methods/critique paper the design must answer, or a human benchmark the paper would replicate or validate against.
- 2 = human-side or LLM-side context that shapes interpretation but is not a design input.
- 1 = foundational background.

**Corrections to the items you recalled**

| Recalled item | Status | Correction |
|---|---|---|
| Bybee, "Surveying Generative AI's Economic Expectations" | [V] | arXiv 2305.02823 (May 2023), J. Leland Bybee. Later retitled "The Ghost in the Machine: Generating Beliefs with Large Language Models" (NBER conference version dated December 2023). No journal version found. |
| Horton, "homo silicus" | [V] | Three authors in current versions: Horton, Filippas, Manning. NBER WP 31122 (April 2023), arXiv 2301.07543; arXiv revised as late as February 2026 with more models. |
| Hansen et al., simulating the SPF | [V] | Hansen, Horton, Kazinnik, Puzzello, Zarifhonarvar, "Simulating the Survey of Professional Forecasters". Working paper (Dec 2024 / Feb 2025 drafts). No journal version found. |
| Faria-e-Castro and Leibovici | [V] | "Artificial Intelligence and Inflation Forecasts", St. Louis Fed WP 2023-015; published in Federal Reserve Bank of St. Louis *Review* 106(12), 2024. Uses Google PaLM; forecasts are in-sample (2019-2023). |
| Zarifhonarvar on LLM inflation expectations | [V-partial] | Earlier titles: "Experimental Evidence on Large Language Models" and "Evidence on Inflation Expectations Formation Using Large Language Models". Current title: "Generating Inflation Expectations with Large Language Models". Cited by other papers as *Journal of Monetary Economics* vol. 157, article 103859; a ScienceDirect listing with a JME-format identifier appeared in results, but the landing page was not retrieved in either round. |
| Argyle et al., "Out of One, Many" | [V] | *Political Analysis* 31(3), 2023, pp. 337-351, DOI 10.1017/pan.2023.2. Six authors. |

---

## 1. Annotated bibliography

### Theme 1 — LLMs as simulated respondents for economic expectations and macro surveys

#### 1A. Households and consumers (closest to the proposed paper)

**Anesti, Hill and Joseph (2026), "Inflation attitudes of large language models"** — [V] — Proximity 5 — **the paper to beat**
- Summary: Bank of England Staff Working Paper No. 1,190 (19 June 2026); arXiv 2512.14306 (16 Dec 2025). A synthetic survey that mimics the information set and demographic characteristics of the Bank of England Inflation Attitudes Survey (IAS), run primarily on GPT-3.5 Turbo. Introduces a Shapley-value decomposition of synthetic survey outputs that traces answers to prompt content.
- Out-of-time design (round 2 finding, from abstract-level snippets): the authors call it a quasi-experiment. GPT-3.5's training cut-off is September 2021, so the model "has no knowledge of the subsequent UK inflation surge". They replicate **two samples of the IAS around the peak of consumer price inflation in late 2022**, that is, post-cutoff waves, and feed the model macroeconomic price signals. The abstract says this setting "turns out to be crucial to track aggregate survey results and official statistics at short horizons".
- Validation targets: aggregate survey results and official statistics; household patterns by income, housing tenure and social class; and a micro-level comparison with human answers, which the authors describe as "rather weak and partially unstable".
- **Not established:** whether the comparison is on banded/categorical answer shares or on derived numeric means, and whether subgroup results are shares or regression gradients. No snippet in two rounds of targeted searching showed the question wording, response options, or the fit metric. From my recollection only (unverified this session), the IAS perception and expectation questions offer banded response options, so the critic's concern stands: this paper may already validate banded answers by subgroup on post-cutoff waves.
- Main result: tracks aggregates at short horizons; replicates some household regularities; heightened sensitivity to food-price information, like humans; lacks a consistent model of consumer price inflation (unexplained kinks in component sensitivity).
- What differs for certain, on the evidence available: one country, one model (GPT-3.5), two waves, direct (not free-text) elicitation as far as the abstract indicates.

**Zarifhonarvar (2025/2026), "Generating Inflation Expectations with Large Language Models"** — [V-partial] — Proximity 5
- Summary: Single-author paper (Indiana University job market paper; SSRN 4825076). LLM agents whose personas mimic the demographic composition of the NY Fed Survey of Consumer Expectations; survey experiments on inflation expectations with proprietary and open-source models; randomized information treatments following the Coibion et al. designs. Argues central banks could use such models to pre-test messaging.
- Identification / design: Simulated survey experiment; randomized information treatments across LLM personas; comparison to SCE moments.
- Data: NY Fed SCE demographic structure; GPT-4 Turbo in the early version, multiple models later.
- Main result: Some LLMs report inflation expectations above actual inflation, as households do; information treatments shift expectations (mortgage rates in the early version, forward guidance on inflation later); proprietary models show less disagreement than open-source ones. No magnitudes in snippets.
- Elicitation: numeric point expectations as far as abstracts show. Post-cutoff validation: not established.
- Why it matters: occupies both second-step ideas (in-silico information RCTs, communication pre-testing) for US households. The Bank of England paper names it as its closest relative.

**Wu, Xi and Xie (2025), "LLM Survey Framework: Coverage, Reasoning, Dynamics, Identification"** — [V] — Proximity 5
- Summary: NBER WP 34308 (October 2025). LLM-based survey framework offering retrospective coverage, elicited reasoning, dynamic effects and clean identification, at roughly 0.5 cents per response.
- Identification / design (round 2): the benchmark is confirmed as the multi-wave RCT in Weber et al. (2025, *Econometrica*). The LLM version uses 200 personas across treatment arms and waves and mirrors the prior-treatment-posterior sequence, with control, past inflation, Fed target and Fed forecast arms. The human survey (10 waves, 2018-2023) is then extended to over 50 waves back to 1990.
- Main result: the authors report human-comparable treatment effects. A conference discussion deck (thin provenance, see 1L) reports treatment-effect correlations that differ sharply by arm and criticizes validation on central tendencies only.
- Why it matters: the direction is retrospective (back to 1990), which is maximally exposed to look-ahead.

**Lin, Sun and Yan (2025), "Simulating Macroeconomic Expectations using LLM Agents"** — [V] — Proximity 5
- Summary: arXiv 2505.17648 (v1 23 May 2025; later versions through at least v4, 25 Nov 2025). Versions carry two titles; the other is "Simulating Macroeconomic Expectations in Survey Experiments with LLM-based Economic Agents". Modular LLM-agent framework (traits, prior expectations, knowledge modules) replicating three survey experiments; one version reports 6,032 household agents and 435 expert agents.
- Michigan exercise (round 2): agents answer the **2025 Michigan Survey of Consumers questions on short- and long-term inflation and home price expectations** and explain their answers in open-ended text. A search summary describes this as after the models' knowledge cutoff. These are numeric expectation questions, not the qualitative sentiment items.
- Fit metric: simulated and human answer distributions compared with kernel density plots and a shape-similarity score averaging about 0.8 (from a third-party aggregator page; **unverified against the paper**).
- Main result: agent expectations are more homogeneous than human ones but outperform plain prompting.
- Why it matters: forward, post-cutoff prediction of a household survey already exists for numeric items, with free-text used for explanation rather than for elicitation.

**Huang, Ferreras Garrucho, Xie, Yuan, Mei, Lian and Hazell (2026), "HouseholdBench: Evaluating Large Language Models as Predictors of Household Economic Behavior"** — [V] — Proximity 5
- Summary: NBER WP 35927 (October 2026); arXiv 2610.07563 (submitted 6 Oct 2026). 6 US household surveys and 32 prediction tasks (numeric, categorical, probabilistic) across consumption, income, labor, expectations and housing; 13 LLMs against a no-change baseline and gradient-boosted trees. Inputs are past behavior, demographics and macroeconomic conditions.
- Number check (round 2): nber.org/papers/w35927 and the NBER social-media post both give 35927; one third-party aggregator lists w35955. I treat 35927 as correct but cannot explain the critic's observation that it sits above the recent numbering trend.
- Temporal design (round 2): the authors' GitHub repository states an evaluation cutoff of 16 February 2026, with 3,200 pre-cutoff and 1,500 post-cutoff test prompts, the post-cutoff rows being data released after that date. So a pre/post-cutoff split exists. How the paper uses it was not established.
- Main result: most models beat no-change; best model cuts numeric error by 12.2%; gradient-boosted trees rank first on most tasks; fine-tuned 4B open-weight model with 16-draw averaging matches proprietary models.
- **Not established:** which six surveys (whether the SCE or Michigan are among them) and whether any task is a qualitative sentiment item.
- Why it matters: senior macro authors, categorical tasks, a no-change baseline, and a post-cutoff split. It sets the baseline standard a referee will apply. It is individual-level prediction given the respondent's own past answers, which is a different object from population response shares.

**Graham, Harvey and Jha (2026), "CFOs Meet LLMs"** — [V] — Proximity 4
- Summary: arXiv 2606.13812 (June 2026; PDF dated 8 Sept 2026). Synthetic answers to the Duke-Fed CFO Survey optimism question for 6,075 firm-quarter responses (2002-2025), matched to the actual CFO at the same firm and quarter.
- Main result: synthetic optimism predicts the actual response conditional on firm and year-quarter fixed effects and the lagged response; accuracy rises with information supplied. Secondary snippets: LLM mean 56.6 vs actual 60.1; synthetic panel under-disperses by roughly 25%; comparison with the Michigan sentiment index.
- Why it matters: the only located paper whose test is explicitly skill beyond fixed effects and the lagged response, which is the standard Section 3 proposes.

**Kazinnik (2023/2025), "Bank Run, Interrupted: Modeling Deposit Withdrawals with Generative AI"** — [V] — Proximity 4
- SSRN 4656722; listed at *Management Science* (DOI 10.1287/mnsc.2024.06807). Synthetic depositors exposed to a panic post and randomized bank/Fed communication; validated against human benchmarks; feeds a contagion model. Direct, personalized reassurance reduces withdrawal intent.

#### 1B. Professional forecasters and LLM macro forecasts

**Hansen, Horton, Kazinnik, Puzzello and Zarifhonarvar (2024/2025), "Simulating the Survey of Professional Forecasters"** — [V] — Proximity 4
- Synthetic forecaster personas from hand-collected SPF participant characteristics, fed real-time macro data; quarterly forecasts for 23 variables, 1999-2023. Reproduces accuracy, median levels, revision dynamics and dispersion (author page). Cutoff handling not established.

**Iadisernia and Camassa (2025), "Prompting for Policy: Forecasting Macroeconomic Scenarios with Synthetic LLM Personas"** — [V] — Proximity 4
- Banca d'Italia authors; arXiv 2511.02458; ICAIF 2025. GPT-4o with 2,368 economics personas replicates the ECB SPF over 50 quarterly rounds (2013-2025) against 100 no-persona baseline forecasts.
- Main result: similar accuracy to humans; **persona descriptions add no measurable accuracy**; homogeneous forecasts.
- Why it matters: the null that motivates question candidate B in Section 3.

**Bybee (2023), "Surveying Generative AI's Economic Expectations" / "The Ghost in the Machine"** — [V] — Proximity 3
- LLM expectations generated from Wall Street Journal articles (1984-2021) track the SPF, AAII and Duke CFO surveys; correlations hold on articles after the training period.

**Faria-e-Castro and Leibovici (2023/2024), "Artificial Intelligence and Inflation Forecasts"** — [V] — Proximity 3
- PaLM retrospective inflation forecasts, 2019-2023; lower MSE than the SPF in most years; slower reversion to 2%. In-sample by the authors' description.

**Alam, Boyle, Li and Sekhposyan (2026), "ChatMacro: Evaluating Inflation Forecasts of Generative AI"** — [V] — Proximity 3
- FRBSF WP 2026-04 (5 Feb 2026); CEPR DP 21057. Pseudo out-of-sample forecasts are comparable to benchmarks, but **true out-of-sample predictions are largely inaccurate and stale**.
- Why it matters: "stale" is the persistence problem in another guise. An LLM without fresh information behaves like a no-change forecast.

**Kazinnik and Sinclair (2025/2026), "FOMC In Silico"** — [V-partial] — Proximity 2. Multi-agent LLM simulation of FOMC deliberation, benchmarked against a Monte Carlo voting model. Second author's first name not confirmed by a snippet.

**Collodel (2025/2026), "Interpreting the Interpreter: Can We Model post-ECB Conferences Volatility with LLM Agents?"** — [V] — Proximity 3. arXiv 2508.13635; Central Bank of Malta WP 4/26. Thirty synthetic traders read ECB press conference transcripts; simulated disagreement correlates with realized OIS volatility.

**Hansen and Kazinnik (2023), "Can ChatGPT Decipher Fedspeak?"** — [V-partial] — Proximity 2. GPT classifies FOMC statement stance better than BERT and dictionaries. Venue beyond Richmond Fed / SSRN 4399406 not confirmed.

#### 1C. Foundations of the "silicon sample" approach

**Horton, Filippas and Manning (2023)** — [V] — Proximity 1. NBER WP 31122. LLMs as implicit computational models of humans.

**Argyle, Busby, Fulda, Gubler, Rytting and Wingate (2023), "Out of One, Many"** — [V] — Proximity 1. "Algorithmic fidelity" and "silicon samples".

**Aher, Arriaga and Kalai (2023)** — [V] — Proximity 1. ICML 2023, PMLR 202:337-371. "Turing Experiments"; "hyper-accuracy distortion".

**Brand, Israeli and Ngwe (2023), "Using LLMs for Market Research"** — [V] — Proximity 2. HBS WP 23-062, SSRN 4395751. LLM-derived WTP sometimes close to human estimates, often inaccurate, occasionally wrong-signed.

**Park, Zou, Shaw, Hill, Cai, Morris, Willer, Liang and Bernstein (2024), "Generative Agent Simulations of 1,000 People"** — [V] — Proximity 2. arXiv 2411.10109. Interview-based agents replicate GSS answers 85% as accurately as participants replicate themselves two weeks later. Origin of the test-retest-normalized metric.

**Hewitt, Ashokkumar, Ghezae and Willer (2024), "Predicting Results of Social Science Experiments Using Large Language Models"** — [V-partial] — Proximity 3. Working paper; no journal version located in round 2. GPT-4 simulated responses predict treatment effects across 70 pre-registered US survey experiments (r = 0.85; r = 0.90 for unpublished studies); effect sizes overestimated. Counts differ across listings.

---

### Theme 2 — Look-ahead bias, temporal leakage, memorization, and post-cutoff evaluation

#### 2A. Leakage and memorization in economics and finance

**Ludwig, Mullainathan and Rambachan (2025), "Large Language Models: An Applied Econometric Framework"** — [V] — Proximity 3
- NBER WP 33344; arXiv 2412.07031. Prediction problems require "no training leakage"; estimation problems require a human-labelled validation sample.

**Lopez-Lira, Tang and Zhu (2025), "The Memorization Problem: Can We Trust LLMs' Economic Forecasts?"** — [V] — Proximity 3
- arXiv 2504.14765; SSRN 5217505. LLMs recall exact values of key economic variables before their cutoff; no recall after it; memorization evidence is a lower bound.
- Relevance to Section 3: the recalled objects are levels. Persistent cross-sectional structure (which countries and groups are pessimistic) is a level and is not removed by evaluating later waves.

**Sarkar and Vafa (2024), "Lookahead Bias in Pretrained Language Models"** — [V-partial] — Proximity 3
- Working paper dated 28 June 2024 (NBER conference PDF); also listed at an ICML 2025 workshop. Direct tests for lookahead bias; limits of prompting-based fixes. SSRN id not confirmed. StoriesLM is attributed to "Sarkar and Vafa (2024)" in one snippet and to "Sarkar (2024)" in another; authorship of the model unresolved.

**Glasserman and Lin (2023), "Assessing Look-Ahead Bias in Stock Return Predictions Generated By GPT Sentiment Analysis"** — [V] — Proximity 2
- Paul Glasserman and Caden Lin (Columbia); arXiv 2309.17322 (29 Sep 2023). Anonymized headlines outperform in-sample: a distraction effect outweighs look-ahead bias. No journal version located.

**He, Lv, Manela and Wu (2025), "Chronologically Consistent Large Language Models"** — [V] — Proximity 3
- arXiv 2502.21206 (v3 July 2025). ChronoBERT / ChronoGPT, annual vintages 1999-2024. Lookahead bias modest in a return-forecasting test but model- and application-specific. The arXiv abstract page lists four authors; one summary of a different paper added a fifth name, which I treat as an error.

**Drinkall, Rahimikia, Pierrehumbert and Zohren (2024), "Time Machine GPT"** — [V] — Proximity 2
- Findings of NAACL 2024, pp. 3281-3292; arXiv 2404.18543. Point-in-time models (TiMaGPT) with yearly corpora 2011-2022.

**Kelly, Malamud, Schwab and Xu (2026), "Scaling Point-in-Time Language Models: Economic Evaluation of Embeddings"** — [V-partial] — Proximity 3
- NBER WP 35247; arXiv 2607.11889; NeurIPS 2026 poster. Monthly point-in-time checkpoints 2013-2024. Relevant because SSR needs an embedding model, a second leakage channel. First names of two authors not confirmed.

**Gao, Jiang and Yan (2025/2026), "Detecting Lookahead Bias in LLM Forecasts"** — [V-partial] — Proximity 2. arXiv 2512.23847. "Lookahead Propensity" test. First names not confirmed.

**Benhenda (2026), "Look-Ahead-Bench"** — [V-partial] — Proximity 2. arXiv 2601.13770. First name and full title not confirmed.

#### 2B. Post-cutoff forecasting evaluation (added in round 2)

**Halawi, Zhang, Yueh-Han and Steinhardt (2024), "Approaching Human-Level Forecasting with Language Models"** — [V] — Proximity 3. NeurIPS 2024; arXiv 2402.18563. Test set restricted to questions published after 1 June 2023, after the models' knowledge cutoffs.

**Karger, Bastani and co-authors (2025), "ForecastBench: A Dynamic Benchmark of AI Forecasting Capabilities"** — [V-partial] — Proximity 3. ICLR 2025. Static post-cutoff test sets go stale as new models are released; proposes a continuously updated benchmark. Full author list not retrieved.

**Paleka, Goel, Geiping and Tramèr (2025), "Pitfalls in Evaluating Language Model Forecasters"** — [V] — Proximity 3. arXiv 2506.00723; listed as an ICLR 2026 poster. Temporal leakage in backtests and the difficulty of extrapolating from evaluation to real forecasting skill. First names not confirmed.

**Schoenegger, Tuminauskaite, Park and Tetlock (2024), "Wisdom of the Silicon Crowd"** — [V] — Proximity 2. *Science Advances*, DOI 10.1126/sciadv.adp1528. Twelve-LLM ensemble statistically indistinguishable from a 925-person human crowd on 31 questions; beats a no-information benchmark.

Cross-references: Bybee (post-training check), Alam et al. (true out-of-sample stale), Anesti et al. (cutoff as quasi-experiment), Lin et al. (2025 Michigan), HouseholdBench (pre/post split), Hewitt et al. (unpublished studies). Read together, these show that post-cutoff evaluation is by now a common element. It is a requirement, not a contribution.

---

### Theme 3 — Methodological critiques and adjacent LLM survey-simulation literatures

#### 3A. Critiques of silicon samples

**Bisbee, Clinton, Dorff, Kenkel and Larson (2024), "Synthetic Replacements for Human Survey Data? The Perils of Large Language Models"** — [V] — Proximity 3. *Political Analysis* 32, 401-416. Means close to ANES, but less variation, 48% of regression coefficients significantly different, sensitivity to prompt wording and timing.

**Dominguez-Olmedo, Hardt and Mendler-Dünner (2024), "Questioning the Survey Responses of Large Language Models"** — [V] — Proximity 3. NeurIPS 2024 (oral). Closed-form answers driven by option ordering and labelling; after randomizing order, responses tend to uniform.

**Tjuatja, Chen, Wu, Talwalkar and Neubig (2024), "Do LLMs Exhibit Human-like Response Biases? A Case Study in Survey Design"** — [V] — Proximity 3 (added round 2). *TACL* 2024 (2024.tacl-1.56). Nine models generally fail to show human-like response biases to question wording changes.

**Santurkar, Durmus, Ladhak, Lee, Liang and Hashimoto (2023), "Whose Opinions Do Language Models Reflect?"** — [V] — Proximity 2. ICML 2023, PMLR 202:29971-30004. OpinionQA; misalignment persists after demographic steering.

**Gui and Toubia (2023/2025), "The Challenge of Using LLMs to Simulate Human Behavior: A Causal Inference Perspective"** — [V] — Proximity 3. arXiv 2312.15524 (v3 Nov 2025). Varying a treatment in the prompt shifts unspecified context. No journal version located in round 2.

**Wang, Morgenstern and Dickerson (2025), "Large language models that replace human participants can harmfully misportray and flatten identity groups"** — [V-partial] — Proximity 2. arXiv 2402.01908. *Nature Machine Intelligence* 7:400-411, DOI 10.1038/s42256-025-00986-z per a citing paper's reference list; journal page not retrieved.

**Krsteski, Russo, Chang, West and Gligorić (2026), "Valid Survey Simulations with Limited Human Data: The Roles of Prompting, Fine-Tuning, and Rectification"** — [V] — Proximity 3. ACL 2026; arXiv 2510.11408. Combining LLM synthesis with rectification using human responses.

**Angelopoulos, Bates, Fannjiang, Jordan and Zrnic (2023), "Prediction-powered inference"** — [V] — Proximity 2 (added round 2). *Science* 382(6671), 669-674. Valid inference when gold-standard data are supplemented with machine predictions; the statistical basis for rectification.

**Lukauskas and Šarkauskaitė (2026), "Plausible but Not Valid"** — [V-partial] — Proximity 2. arXiv 2608.14606. Statistical baselines without a language model match or beat LLM respondents; scale compression. Authors from a secondary bibliography.

**Taday Morocho et al. (2026), "Assessing the Reliability of Persona-Conditioned LLMs as Synthetic Survey Respondents"** — [V-partial] — Proximity 2. arXiv 2602.18462; WWW Companion '26. Demographic conditioning can redistribute error. Full author list not retrieved.

Critiques internal to the macro papers: Iadisernia and Camassa (personas add nothing); Lin, Sun and Yan (more homogeneous than humans); Graham, Harvey and Jha (about 25% under-dispersion); Anesti, Hill and Joseph (weak, unstable micro-level match); Hewitt et al. (effect sizes overestimated); Alam et al. (stale out-of-sample).

#### 3B. Predicting subgroup answer-option distributions (added in round 2)

This literature has the same target object as the proposed paper: the distribution over answer options for a demographic subgroup.

**Kim and Lee (2023/2024), "AI-Augmented Surveys: Leveraging Large Language Models and Surveys for Opinion Prediction"** — [V] — Proximity 3. arXiv 2305.09620 (v3 April 2024). Fine-tunes LLMs on repeated cross-sections of the General Social Survey (1972-2021): strong on retrodiction (AUC 0.86; rho 0.98 for public opinion), weaker on unasked questions (AUC 0.73; rho 0.67). First names not confirmed.

**Suh et al. (2025), "Language Model Fine-Tuning on Scaled Survey Data for Predicting Distributions of Public Opinions"** — [V-partial] — Proximity 3. ACL 2025, pp. 21147-21170; arXiv 2502.16761. SubPOP: 3,362 questions and 70K subpopulation-response pairs from Pew ATP and GSS; fine-tuning reduces Wasserstein distance to human distributions by 32-46%. Author list beyond the first author (Joseph Jeesung Suh, from the repository name) not retrieved.

**Meister, Guestrin and Hashimoto (2025), "Benchmarking Distributional Alignment of Large Language Models"** — [V] — Proximity 3. NAACL 2025, pp. 24-49, DOI 10.18653/v1/2025.naacl-long.2. Log-probability metrics understate alignment; models may "know" a group's distribution but struggle to sample from it. Supports eliciting distributions by a route other than sampling option labels.

**Cao, Liu, Arora, Augenstein, Röttger and Hershcovich (2025), "Specializing Large Language Models to Simulate Survey Response Distributions for Global Populations"** — [V] — Proximity 3. NAACL 2025, pp. 3141-3154; arXiv 2502.07068. Fine-tuning on first-token probabilities against country-level World Values Survey distributions; outperforms zero-shot, including on unseen countries and questions, but "even our best models struggle". (The critic's recalled author list was incorrect; this is the confirmed one.)

#### 3C. Cross-country and multilingual fidelity (added in round 2)

**Durmus, Nguyen, Liao, Schiefer and co-authors (2023), "Towards Measuring the Representation of Subjective Global Opinions in Language Models"** — [V-partial] — Proximity 3. arXiv 2306.16388. GlobalOpinionQA; default responses are closer to the US and some European and South American countries. Full author list not retrieved.

**von der Heyde, Haensch and Wenz (2025), "Vox Populi, Vox AI? Using Language Models to Estimate German Public Opinion"** — [V-partial] — Proximity 3. *Social Science Computer Review*, DOI 10.1177/08944393251337014; arXiv 2407.08563. GPT-3.5 personas matched to the 2017 German Longitudinal Election Study; bias towards Green and Left parties. Volume/year differ across listings (2025 vs. 44(3), 2026); first names not confirmed.

**Qu and Wang (2024), "Performance and biases of Large Language Models in public opinion simulation"** — [V] — Proximity 3. *Humanities and Social Sciences Communications* 11, 1095, DOI 10.1057/s41599-024-03609-x. ChatGPT simulates public opinion better in Western, English-speaking contexts; biases by gender, ethnicity, age, education and class.

**Atari, Xue, Park, Blasi and Henrich (2023), "Which Humans?"** — [V] — Proximity 2. PsyArXiv / Harvard working paper. LLM responses resemble WEIRD populations; similarity falls with cultural distance (r = -0.70).

Implication for a 27-country panel: fidelity is likely to vary systematically by country and language, and country fixed effects in the errors should be expected.

---

### Theme 4 — Human-side benchmarks

#### 4A. Household inflation expectation formation

**Malmendier and Nagel (2016), "Learning from Inflation Experiences"** — [V] — Proximity 2. *QJE* 131(1), 53-87.

**D'Acunto, Malmendier, Ospina and Weber (2021), "Exposure to Grocery Prices and Inflation Expectations"** — [V] — Proximity 2. *JPE* 129(5), 1615-1639.

**Cavallo, Cruces and Perez-Truglia (2017), "Inflation Expectations, Learning, and Supermarket Prices"** — [V] — Proximity 2. *AEJ: Macroeconomics* 9(3), 1-35.

**Armantier, Nelson, Topa, van der Klaauw and Zafar (2016), "The Price Is Right"** — [V-partial] — Proximity 2. *REStat* 98(3), 503-523 from an ambiguous listing; not re-checked in round 2.

**Carroll (2003), "Macroeconomic Expectations of Households and Professional Forecasters"** — [V] — Proximity 2 (searched round 2). *QJE* 118(1), 269-298. Household expectations derive from news reports of professional forecasts, with occasional attention, generating stickiness.

**Coibion and Gorodnichenko (2015), "Information Rigidity and the Expectations Formation Process: A Simple Framework and New Facts"** — [V] — Proximity 2 (searched round 2). *AER* 105(8), 2644-2678. Content not shown in snippets.

**Andre, Pizzinelli, Roth and Wohlfart (2022), "Subjective Models of the Macroeconomy: Evidence From Experts and Representative Samples"** — [V] — Proximity 2 (searched round 2). *REStud* 89(6), 2958-2991. Beliefs about the effects of shocks are widely dispersed and differ between 6,500 households and 1,500 experts. Lin, Sun and Yan appear to borrow its recall-channel coding.

**Coibion, Gorodnichenko and Weber (2022), "Monetary Policy Communications and Their Effects on Household Inflation Expectations"** — [V] — Proximity 3. *JPE* 130(6), 1537-1584.

**Weber et al. (2025), "Tell Me Something I Don't Already Know: Learning in Low- and High-Inflation Settings"** — [V] — Proximity 3. *Econometrica* 93(1), 229-264. Confirmed as the benchmark Wu, Xi and Xie replicate.

**Coibion, Georgarakos, Gorodnichenko and Weber (2023), "Forward Guidance and Household Expectations"** — [V] — Proximity 2. *JEEA* 21(5), 2131-2171 (confirmed round 2). About 20,000 Nielsen Homescan consumers; 22 information types.

**Haaland, Roth and Wohlfart (2023), "Designing Information Provision Experiments"** — [V] — Proximity 3. *JEL* 61(1), 3-40.

**Wohlfart (2026), "Do People Have Economic Expectations?"** — [V-partial] — Proximity 2. ECONtribute DP 402. On respondents who form expectations from scratch when asked. Author list from a RePEc snippet.

#### 4B. Central bank communication with the public

**Haldane and McMahon (2018)** — [V] — Proximity 2. *AEA P&P* 108, 578-583.

**Bholat, Broughton, Ter Meer and Walczak (2019)** — [V] — Proximity 3. *JME* 108, 1-15. Representative UK experiment on a "Relatable Summary".

**Blinder, Ehrmann, de Haan and Jansen (2024)** — [V] — Proximity 2. *JEL* 62(2), 425-457.

**Haldane, Macaulay and McMahon (2020), "The 3 E's of central bank communication with the public"** — [V-partial] — Proximity 2. Bank of England working paper confirmed by title; author list from memory.

#### 4C. Consumer confidence and the quantification of qualitative surveys (added in round 2)

The target questions are consumer-confidence items. This block is the human-side foundation for them.

**Carroll, Fuhrer and Wilcox (1994), "Does Consumer Sentiment Forecast Household Spending? If So, Why?"** — [V] — Proximity 2. *AER* 84(5), 1397-1408. Sentiment improves consumption forecasts beyond other macro variables (per a secondary summary).

**Ludvigson (2004), "Consumer Confidence and Consumer Spending"** — [V] — Proximity 2. *JEP* 18(2), 29-50. Much of the information in confidence is already in other indicators; its independent predictive contribution is modest.

**Barsky and Sims (2012), "Information, Animal Spirits, and the Meaning of Innovations in Consumer Confidence"** — [V] — Proximity 2. *AER* 102(4), 1343-1377. Confidence innovations mostly reflect news about future fundamentals.

**Bachmann, Berg and Sims (2015), "Inflation Expectations and Readiness to Spend: Cross-Sectional Evidence"** — [V] — Proximity 3 (searched round 2). *AEJ: Economic Policy* 7(1), 1-35. Michigan microdata; relates expected inflation to the qualitative "good time to buy" item. The published abstract reports that at the zero lower bound a one-point rise in expected inflation lowers the probability of a positive spending attitude by about 0.5 points (the working paper reports a smaller figure).

**Carlson and Parkin (1975), "Inflation Expectations"** — [V] — Proximity 2. *Economica* 42, 123-138. Quantification of qualitative response shares.

**Batchelor and Orr (1988), "Inflation Expectations Revisited"** — [V] — Proximity 2. *Economica* 55(219), 317-331. Extends Carlson-Parkin to four- and five-category survey data, the format of the EC consumer questions.

**Pesaran and Weale (2006), "Survey Expectations"** — [V] — Proximity 2. *Handbook of Economic Forecasting*, vol. 1, ch. 14, pp. 715-776.

**Nardo (2003), "The Quantification of Qualitative Survey Data: A Critical Assessment"** — [V] — Proximity 2. *Journal of Economic Surveys* 17(5), 645-668.

Why the block matters for the design: Ludvigson and Barsky-Sims imply that movements in confidence are largely predictable from public macro information, which is the information a prompt would contain. A synthetic panel that tracks changes may therefore be reproducing a macro-to-sentiment mapping, and the relevant comparison is a simple regression on the same public indicators.

#### 4D. EC consumer survey and ECB CES: microdata papers and documentation (added in round 2)

**Arioli, Bates, Dieden, Duca, Friz, Gayer, Kenny, Meyler and Pavlova (2017)** — [V] — Proximity 3. ECB Occasional Paper 186. Evaluation of the EC consumer survey's quantitative inflation questions.

**Duca-Radu, Kenny and Reuter (2021), "Inflation expectations, consumption and the lower bound: Micro evidence from a large multi-country survey"** — [V] — Proximity 3. *JME* 118, 120-134. EC consumer survey microdata; a one-point rise in expected inflation relative to perceived inflation raises the probability of being ready to spend by 0.26 points in normal times and 0.33 at the lower bound (ECB Research Bulletin summary). Uses the qualitative major-purchases item as an outcome.

**Andrade, Gautier and Mengus (2023), "What matters in households' inflation expectations?"** — [V] — Proximity 3. *JME* 138, 50-68. French household survey microdata, 2004-2018: the qualitative regime (prices stable versus rising) matters for durable spending; the reported rate among those expecting positive inflation does not. Direct evidence that the qualitative answer is the economically relevant object.

**European Commission, DG ECFIN, "The Joint Harmonised EU Programme of Business and Consumer Surveys: User Guide"** — [V-partial] — Proximity 3. Updated January 2023 (PDF on economy-finance.ec.europa.eu); the methodology page also lists a user guide dated 6 March 2026, not opened. One source states the consumer survey uses a five-point answering scale with 12-month backward and forward reference periods. Question-by-question answer options were not confirmed by a snippet.

**Bańkowska et al. (2021), "ECB Consumer Expectations Survey: an overview and first evaluation"** — [V] — Proximity 3. ECB Occasional Paper 287, DOI 10.2866/310866; fifteen authors. Pilot from January 2020 in the six largest euro area countries; about 10,000 respondents by June 2020.

#### 4E. Demographic gradients in expectations (added in round 2)

These supply the cross-sectional gradients a synthetic panel should reproduce, and also the ones most likely to be memorised.

**Das, Kuhnen and Nagel (2020), "Socioeconomic Status and Macroeconomic Expectations"** — [V] — Proximity 3. *RFS* 33(1), 395-432. Higher-income and more-educated respondents are more optimistic about business conditions, unemployment and stock returns; the gap narrows in recessions. The time-varying gap is a test that goes beyond memorised levels.

**D'Acunto, Malmendier and Weber (2021), "Gender roles produce divergent economic expectations"** — [V] — Proximity 2. *PNAS* 118(21), e2008534118. The gender gap in inflation expectations tracks who does the grocery shopping.

**Bruine de Bruin, van der Klaauw, Downs, Fischhoff, Topa and Armantier (2010), "Expectations of Inflation: The Role of Demographic Variables, Expectation Formation, and Financial Literacy"** — [V] — Proximity 2. *Journal of Consumer Affairs* 44(2), 381-402. Higher expectations among women, lower-income, single and less-educated respondents.

---

### Theme 5 — SSR itself: follow-ups, critiques, applications outside marketing

**Maier et al. (2025), "LLMs Reproduce Human Purchase Intent via Semantic Similarity Elicitation of Likert Ratings"** — [V-partial] — Proximity 3 (source method)
- arXiv 2510.08338 (v1 9 Oct 2025; v3 27 Oct 2025). Benjamin F. Maier and eight co-authors, PyMC Labs and Colgate-Palmolive; **full author list not retrieved**.
- Method detail (round 2 snippet): each scale point's probability is proportional to the cosine similarity between the response embedding and that point's reference statement, with a temperature parameter controlling sharpness; the arXiv version uses the `text-embedding-3-small` embedder.
- Result per snippets: 57 personal-care product surveys, 9,300 US respondents; GPT-4o and Gemini-2.0-flash; SSR with GPT-4o reaches 90.2% correlation attainment and mean KS similarity 0.88. Sensitive to embedder, similarity measure and anchors. No peer-reviewed version found.

**Vera Pichardo (2026), "Measuring Self-Rating Bias in LLM-Generated Survey Data: A Semantic Similarity Framework for Independent Scale Mapping"** — [V] — Proximity 3
- arXiv 2602.13862. Validates SSR as a mapping channel independent of the generating model. Pre-registered experiment (N=345): LLM self-rating has 4x compressed error variance (0.21 vs 0.87 for SSR). SSR achieves 65-77% exact match and 91-100% within one point on 69 test cases in 8 domains. Single author; not peer reviewed.
- Direct evidence for question candidate A in Section 3 (SSR and dispersion), in a non-macro setting.

**Not located:** any independent replication of the SSR headline numbers; any application of SSR or embedding-based mapping to categorical answers in any macroeconomic or consumer-confidence survey. Round 2 added searches on "open-ended" elicitation with classification into response categories and on embedding-based mapping; they returned only Maier et al., Vera Pichardo, and the leads in 1L.

---

### 1L. Leads, do not cite

No retrievable authors or thin provenance. None has a BibTeX entry. Each needs the primary source before use.

| Item | What a snippet said | Why it might matter |
|---|---|---|
| arXiv 2610.29645, "LLMs as survey respondents: Comparison to simple semantic baselines" | Short paper; LLMs do not always beat embedding-similarity baselines with no generation step. Authors not retrieved; model names in snippet looked fragmentary. | Would imply an embedding-only baseline. |
| arXiv 2608.30522, "Tariff Threats, Macroeconomic Expectations, and Policy Communication Strategies: Experiments Based on a Multi-Agent System" | 300 Michigan households as persistent LLM agents; central bank explanations coordinate beliefs. Authors not retrieved; aggregator pages only. | Occupies communication pre-testing on Michigan households. |
| Utama, Andina and Oktavia (2026), "Effects of Information Treatments on Household Inflation Expectations in Indonesia: A Generative AI Experiment" | BIS-hosted conference PDF; 5,400 GPT/Gemini personas; information treatments. Affiliation, conference and results not confirmed. | Central-bank-side communication testing without a human survey. |
| arXiv 2607.00403, "A Penny for Your Prompts: Experiments Detecting and Mitigating LLM Usage by Survey Respondents" | A search summary says LLM open-ended answers are more semantically homogeneous than human ones. | If free text is homogeneous, SSR's dispersion gain may come from the mapping temperature, not the text. |
| arXiv 2605.24564, "Summoning the Oracle to Slay It" | Inference-time correction for look-ahead bias. Authors not retrieved. | Alternative to post-cutoff evaluation. |
| arXiv 2610.04412 (title containing "Large Language Models and Augmented Democracy") | Reportedly applies SSR to lawmaker agents. Attribution unconfirmed. | Only reported SSR use outside marketing. |
| Yan and Tang (2026), "DatedGPT" | Named in another paper's text. | Point-in-time model. |
| "Argyle et al. (2024)" as an embedding-to-Likert precursor | Cited inside arXiv 2610.29645's snippet. Not located; possibly a mis-citation. | If real, it predates SSR. |
| Prolific preprint on persona-level error | A search summary: persona simulation tripled distributional error versus asking for the aggregate distribution. Not located in a dedicated search. | Bears on whether personas help. |
| Cleveland Fed 2026 conference discussion of Wu, Xi and Xie (deck by D. Puzzello per file name) | Critique that validation covers central tendencies and treatment effects; arm-specific correlations. Slides only. | States the referee objection the proposed paper answers. |
| Towards Data Science post, "Can LLMs Replace Survey Respondents?" | Blog: a Llama-3 variant matched the SCE median but was far less dispersed; argues papers should report distributional accuracy. | Grey literature on dispersion. |
| PyMC Labs blog on synthetic consumers and GSS questions | Smaller models fall below a naive baseline. | Grey literature from the SSR authors' firm. |
| Six title-only arXiv items: 2609.07305, 2606.09013, 2607.26348, 2608.29455, 2611.00256, 2610.25158 | Titles only (marginal fidelity; distributional-level evaluation; cross-domain failures; item-mean surrogates; validation framework; European survey age gap). | Critique literature; 2610.25158 uses European survey data. |
| arXiv 2609.13148, "When Can You Trust Your Synthetic Users? Diagnostics and Corrections for LLM Consumer Panels" | Aggregate agreement can conceal subgroup errors. | Subgroup validation. |
| Dillion, Tandon, Gu and Gray (2023), *Trends in Cognitive Sciences* | Not searched in either round. | Early overview. |

---

## 2. Frontier map

### What has been done

| Paper | Population / survey | Model(s) | Elicitation | Validation target | Temporal design |
|---|---|---|---|---|---|
| Anesti, Hill, Joseph (BoE SWP 1190) | UK households / BoE Inflation Attitudes Survey | GPT-3.5 Turbo | Synthetic survey replica | Aggregates, official statistics, subgroup regularities, micro-level match | **Two survey samples around late 2022, after the Sept 2021 cutoff** |
| Zarifhonarvar (JME, per citations) | US households / NY Fed SCE | GPT-4 Turbo; later several | Numeric; info treatments | SCE moments; RCT effects | Not established |
| Wu, Xi, Xie (NBER 34308) | US households / Weber et al. RCT | Not established | Survey + elicited reasoning | Treatment effects, central tendencies | Retrospective, back to 1990 |
| Lin, Sun, Yan (arXiv) | US households + experts; Michigan | LLM agents | Numeric; open-ended explanations | Experiment results; 2025 MSC distributions | **2025 Michigan survey, described as post-cutoff** |
| HouseholdBench (NBER 35927) | 6 US household surveys, 32 tasks | 13 LLMs | Numeric, categorical, probabilistic | Individual outcomes vs no-change and GBT | **Pre/post split at 16 Feb 2026** |
| Graham, Harvey, Jha | Duke-Fed CFO Survey | Not established | Optimism score | Matched individual answers, with FE and lag | 2002-2025 |
| Hansen et al. | US SPF | Not established | Numeric, 23 variables | Accuracy, dispersion, revisions | 1999-2023, real-time data |
| Iadisernia, Camassa | ECB SPF | GPT-4o | Numeric | SPF panel; no-persona baseline | 2013-2025 |
| Bybee | SPF, AAII, CFO | GPT-3.5-class | Expectations from WSJ text | Survey series | Includes post-training articles |
| Faria-e-Castro, Leibovici; Alam et al. | None (model as forecaster) | PaLM; several | Numeric forecast | Realized inflation, SPF | In-sample; pseudo vs true out-of-sample |
| Maier et al. (SSR) | US consumers / 57 product surveys | GPT-4o, Gemini-2.0-flash | Free text mapped to Likert via embeddings | Response distributions, rankings | Not a concern in their setting |
| Suh et al.; Cao et al.; Meister et al. | Opinion surveys (ATP, GSS, WVS) | Fine-tuned and zero-shot LLMs | Option probabilities | Subgroup / country answer distributions | Held-out questions, not held-out time |

### Patterns

1. **Geography.** Household work located is US (SCE, Michigan) plus one UK paper. No paper located uses the EC Business and Consumer Survey, the ECB CES, or a multi-country household panel. Euro-area work located concerns professionals and market participants.
2. **Outcome type.** The located macro papers describe numeric expectations or forecasts. Whether Anesti et al. validate on banded shares is unresolved (Section 1A). No paper located targets consumer-confidence items (financial situation, general economic situation, major purchases, unemployment expectations).
3. **Elicitation.** No macro paper located uses free-text elicitation with embedding-based mapping. Lin et al. use open-ended text for explanations only.
4. **Temporal validity.** Post-cutoff evaluation is present in at least three of the five closest papers (Anesti et al., Lin et al., HouseholdBench) and in Bybee and Hewitt et al. It is no longer a differentiator.
5. **Baselines.** Only HouseholdBench (no-change, gradient-boosted trees) and Graham et al. (fixed effects, lagged response) are described as testing skill beyond persistence.
6. **Recurring weakness.** Under-dispersion and homogeneity in nearly every paper that checks; personas added nothing for professional forecasters.
7. **Second-step ideas are occupied.** In-silico information RCTs: Zarifhonarvar; Wu, Xi and Xie; Lin, Sun and Yan. Communication pre-testing: Zarifhonarvar; Kazinnik; plus two leads in 1L.

### Has anyone already applied SSR-style free-text-to-Likert elicitation to macro expectation surveys with post-cutoff validation?

**No paper located.** This is an absence of search hits, not an established fact. Stated by component:

| Component | Status after round 2 |
|---|---|
| SSR or embedding-based mapping in a macro survey | No paper located (searches: SSR with inflation/consumer expectations/macroeconomic; open-ended elicitation with category classification; embedding mapping). |
| Consumer-confidence items as the target | No paper located (searches: "consumer confidence", "consumer sentiment", "Index of Consumer Sentiment", "financial situation"/"major purchases"/"buying conditions"). |
| EC Business and Consumer Survey or ECB CES as the benchmark | No paper located (searches: "business and consumer survey", "consumer confidence indicator", euro area). |
| Post-cutoff validation of a synthetic household survey | **Exists**: Anesti et al. (two late-2022 IAS samples); Lin et al. (2025 Michigan); HouseholdBench (post-16 Feb 2026 rows). |
| Qualitative/banded answer shares by subgroup as the target | **Unresolved**: possibly Anesti et al.; HouseholdBench has categorical tasks at individual level. |
| Skill over persistence baselines | **Exists in part**: HouseholdBench (no-change), Graham et al. (FE and lag). |

Limits: snippet-based; SSRN and conference programmes covered partially; at least six relevant papers appeared between June and October 2026. Reading Anesti et al. and HouseholdBench in full remains a precondition for any stronger wording.

---

## 3. Positioning recommendation

### The problem the positioning has to answer first

Post-cutoff waves alone do not identify skill. Survey response shares are highly persistent, and their cross-sectional structure (which countries and which demographic groups are more pessimistic) is stable over years and well documented in text the model was trained on (Lopez-Lira et al. on memorised levels; Das et al., Bruine de Bruin et al. on stable gradients). With roughly a dozen post-cutoff monthly waves, most of the variance in a country x group x month panel is cross-sectional. A model that has memorised pre-cutoff levels will fit post-cutoff levels well and show no skill. Alam et al.'s "stale" forecasts are the same phenomenon in the time dimension.

The contribution therefore has to be stated as skill beyond memorised levels:
- relative to a last-wave (no-change) baseline and to country x group fixed effects estimated on pre-cutoff data;
- on changes, and on turning points, in response shares;
- and, given Ludvigson and Barsky-Sims, relative to a simple mapping from the same public macro indicators supplied in the prompt.

Precedents in the located literature: HouseholdBench (no-change, gradient-boosted trees), Graham et al. (fixed effects and lagged response), Halawi et al. and Schoenegger et al. (no-information benchmarks), Paleka et al. (why backtests overstate skill). Das et al.'s finding that the socioeconomic gap narrows in recessions is an example of a time-varying gradient that fixed effects cannot reproduce.

### Sharper question candidates

A combination of three design features is not a question. Three candidates, each tied to located evidence:

- **A. Does free-text elicitation with semantic mapping remove the under-dispersion of synthetic macro respondents?** Under-dispersion is documented by Bisbee et al., Lin et al., Graham et al. and Iadisernia-Camassa; Vera Pichardo reports direct LLM rating compresses variance fourfold relative to SSR; Meister et al. find models know distributions but cannot sample them. The benchmark would be public, multi-country and distributional. Risk: the lead 2607.00403 (homogeneous open-ended answers) suggests any gain could be a temperature artefact of the mapping.
- **B. Do demographic and country personas carry information for households?** Iadisernia and Camassa find none for professional forecasters. Households differ more by demographics (Das et al.; D'Acunto et al.; Bruine de Bruin et al.), so the prior differs, and the test is persona versus no-persona versus fixed-effect baselines. Country conditioning has known weak spots (Durmus et al.; Qu and Wang; von der Heyde et al.).
- **C. Is there skill over persistence?** Do synthetic panels predict post-cutoff changes and turning points in qualitative response shares beyond last-wave, fixed-effect and macro-indicator baselines? This is the question a referee will ask of any answer to A or B, and Alam et al. suggest the answer may be no without fresh information in the prompt.

These are candidates from the literature; choosing among them is for the Strategist and the user.

### The paper to beat

**Anesti, Hill and Joseph (2026, Bank of England SWP 1190).** It already has a household expectations survey, demographic conditioning, a central bank imprimatur, and post-cutoff waves framed as a quasi-experiment. On current evidence the proposed paper differs from it by: many countries and waves rather than one country and two samples; consumer-confidence items rather than inflation attitudes; SSR rather than direct elicitation; newer models; and explicit persistence baselines. If its targets turn out to be banded shares by subgroup, "qualitative response shares" drops out of that list.

### The five closest competitors

1. Anesti, Hill and Joseph (2026) — as above.
2. Huang et al. (2026, HouseholdBench) — baselines, categorical tasks, post-cutoff split; individual-level, US.
3. Lin, Sun and Yan (2025) — post-cutoff Michigan prediction with distributional comparison; numeric items.
4. Zarifhonarvar — SCE personas, information treatments, communication pitch.
5. Wu, Xi and Xie (2025) — in-silico multi-wave RCT; retrospective.

Next tier: Iadisernia and Camassa; Graham, Harvey and Jha; Hansen et al.; Alam et al.

### Contribution statement (draft for the Writer, deliberately hedged)

"We ask whether LLM-based synthetic respondents predict changes in the distribution of answers to the qualitative questions of harmonised consumer surveys, across countries and demographic groups, beyond what persistence and group fixed effects already deliver. We elicit free-text answers and map them to response categories by semantic similarity, and we evaluate only on waves fielded after the model's training cutoff. To our knowledge, no paper located to date applies this elicitation to macroeconomic surveys or evaluates synthetic respondents against the European Commission consumer survey."

Do not write "unlike existing work, which evaluates within the training window" or "which elicits only numeric expectations": Anesti et al., Lin et al. and HouseholdBench evaluate post-cutoff, and the numeric-only claim is unresolved for Anesti et al.

### What the literature implies referees will expect (reported, not recommended)

- Baselines: last-wave shares; country x group fixed effects; gradient-boosted trees or a regression on public macro indicators; no-persona prompts; direct option elicitation; possibly embedding-only similarity (lead).
- SSR introduces a second model (the embedder) with its own cutoff, and researcher-chosen anchors and temperature.
- Cross-country fidelity is uneven; expect country-specific bias.
- Rectification with a small human sample (Krsteski et al.; Angelopoulos et al.) is the constructive response if raw synthetic shares are biased.

### Candidate outlets seen in this literature

JME (Zarifhonarvar per citations; Bholat et al.; Duca-Radu et al.; Andrade et al.), Management Science (Kazinnik), central bank working paper series, NBER, ICAIF. No top-5 general-interest publication of an LLM-synthetic-survey macro paper was located.

---

## 4. Could not verify (consolidated, after round 2)

- **Anesti, Hill and Joseph:** question format and response options used, the fit metric, and whether subgroup validation is on answer shares. This is the single most consequential open item.
- **HouseholdBench:** the six surveys; how the post-cutoff split is used; why the NBER number sits above trend (nber.org shows 35927).
- **Lin, Sun and Yan:** the shape-similarity figure (aggregator source); which title is current; the models' actual cutoffs.
- **Zarifhonarvar:** JME volume 157 / article 103859 from citing papers; publisher page not retrieved.
- **Maier et al.:** full author list.
- **Journal details from secondary sources:** Wang-Morgenstern-Dickerson (*Nature Machine Intelligence* 7:400-411); von der Heyde et al. (volume/year); Armantier et al. (*REStat* pages).
- **No journal version located:** Gui and Toubia; Hewitt et al.; Glasserman and Lin; Sarkar and Vafa; Hansen et al.
- **Author first names or full lists not confirmed:** Kelly et al.; Gao et al.; Benhenda; Paleka et al.; Karger et al.; Suh et al.; Durmus et al.; Kim and Lee; Taday Morocho et al.; von der Heyde et al.; Kazinnik and Sinclair; Aher et al.; Santurkar et al.; Hewitt et al.; Brand et al.; Haldane-Macaulay-McMahon. Flagged in BibTeX.
- **EC User Guide:** per-question answer options not confirmed by a snippet.
- **Central banks:** no ECB, Bundesbank, BIS-series or Federal Reserve Board paper on LLM synthetic households located. Absence of hits only.
- Everything in Section 1L.

---

## 5. BibTeX

For copying into the project bibliography later; `Bibliography_base.bib` was not modified. Lines beginning `% UNVERIFIED` name what is unconfirmed. Items in Section 1L have no entry.

```bibtex
%% ---------- Theme 1: LLM respondents for economic expectations ----------

@techreport{anesti_hill_joseph_2026,
  author      = {Anesti, Nikoleta and Hill, Edward and Joseph, Andreas},
  title       = {Inflation Attitudes of Large Language Models},
  institution = {Bank of England},
  type        = {Staff Working Paper},
  number      = {1190},
  year        = {2026},
  month       = jun,
  note        = {arXiv:2512.14306}
}

% UNVERIFIED: volume/article number from citing papers; publisher page not retrieved; year may be 2025 or 2026
@article{zarifhonarvar_generating,
  author  = {Zarifhonarvar, Ali},
  title   = {Generating Inflation Expectations with Large Language Models},
  journal = {Journal of Monetary Economics},
  volume  = {157},
  pages   = {103859},
  year    = {2026},
  note    = {SSRN 4825076. Earlier versions titled ``Experimental Evidence on Large Language Models'' and ``Evidence on Inflation Expectations Formation Using Large Language Models''}
}

@techreport{wu_xi_xie_2025,
  author      = {Wu, Jing Cynthia and Xi, Jin and Xie, Shihan},
  title       = {{LLM} Survey Framework: Coverage, Reasoning, Dynamics, Identification},
  institution = {National Bureau of Economic Research},
  type        = {Working Paper},
  number      = {34308},
  year        = {2025},
  month       = oct
}

@unpublished{lin_sun_yan_2025,
  author = {Lin, Jianhao and Sun, Lexuan and Yan, Yixin},
  title  = {Simulating Macroeconomic Expectations using {LLM} Agents},
  year   = {2025},
  note   = {arXiv:2505.17648. Some versions titled ``Simulating Macroeconomic Expectations in Survey Experiments with LLM-based Economic Agents''}
}

@techreport{huang_etal_householdbench_2026,
  author      = {Huang, Jin and Ferreras Garrucho, Diego and Xie, Yutong and Yuan, Walter M. and Mei, Qiaozhu and Lian, Chen and Hazell, Jonathon},
  title       = {{HouseholdBench}: Evaluating Large Language Models as Predictors of Household Economic Behavior},
  institution = {National Bureau of Economic Research},
  type        = {Working Paper},
  number      = {35927},
  year        = {2026},
  month       = oct,
  note        = {arXiv:2610.07563}
}

@unpublished{graham_harvey_jha_2026,
  author = {Graham, John R. and Harvey, Campbell R. and Jha, Manish},
  title  = {{CFOs} Meet {LLMs}},
  year   = {2026},
  note   = {arXiv:2606.13812}
}

% UNVERIFIED: volume/issue/pages and year not retrieved (DOI listing confirmed)
@article{kazinnik_bankrun,
  author  = {Kazinnik, Sophia},
  title   = {Bank Run, Interrupted: Modeling Deposit Withdrawals with Generative {AI}},
  journal = {Management Science},
  year    = {2025},
  doi     = {10.1287/mnsc.2024.06807},
  note    = {SSRN 4656722}
}

@unpublished{hansen_etal_spf_2025,
  author = {Hansen, Anne Lundgaard and Horton, John J. and Kazinnik, Sophia and Puzzello, Daniela and Zarifhonarvar, Ali},
  title  = {Simulating the Survey of Professional Forecasters},
  year   = {2025},
  note   = {Working paper, February 2025 draft (Stanford Digital Economy Lab)}
}

@inproceedings{iadisernia_camassa_2025,
  author    = {Iadisernia, Giulia and Camassa, Carolina},
  title     = {Prompting for Policy: Forecasting Macroeconomic Scenarios with Synthetic {LLM} Personas},
  booktitle = {Proceedings of the ACM International Conference on AI in Finance (ICAIF)},
  year      = {2025},
  note      = {arXiv:2511.02458}
}

@unpublished{bybee_2023,
  author = {Bybee, J. Leland},
  title  = {Surveying Generative {AI}'s Economic Expectations},
  year   = {2023},
  note   = {arXiv:2305.02823. Later circulated as ``The Ghost in the Machine: Generating Beliefs with Large Language Models''}
}

@article{fariaecastro_leibovici_2024,
  author  = {Faria-e-Castro, Miguel and Leibovici, Fernando},
  title   = {Artificial Intelligence and Inflation Forecasts},
  journal = {Federal Reserve Bank of St. Louis Review},
  volume  = {106},
  number  = {12},
  year    = {2024},
  note    = {Working Paper 2023-015, doi:10.20955/wp.2023.015}
}

@techreport{alam_etal_chatmacro_2026,
  author      = {Alam, M. Jahangir and Boyle, Shane and Li, Huiyu and Sekhposyan, Tatevik},
  title       = {{ChatMacro}: Evaluating Inflation Forecasts of Generative {AI}},
  institution = {Federal Reserve Bank of San Francisco},
  type        = {Working Paper},
  number      = {2026-04},
  year        = {2026},
  doi         = {10.24148/wp2026-04},
  note        = {Also CEPR Discussion Paper 21057}
}

% UNVERIFIED: second author's first name and initial (from memory); series number from RePEc handle
@unpublished{kazinnik_sinclair_fomc,
  author = {Kazinnik, Sophia and Sinclair, Tara M.},
  title  = {{FOMC} In Silico: A Multi-Agent System for Monetary Policy Decision Modeling},
  year   = {2025},
  note   = {GWU working paper 2025-005}
}

@techreport{collodel_2026,
  author      = {Collodel, Umberto},
  title       = {Interpreting the Interpreter: Can We Model Post-{ECB} Conferences Volatility with {LLM} Agents?},
  institution = {Central Bank of Malta},
  type        = {Working Paper},
  number      = {4/26},
  year        = {2026},
  note        = {arXiv:2508.13635}
}

% UNVERIFIED: working paper number and any journal version
@unpublished{hansen_kazinnik_fedspeak_2023,
  author = {Hansen, Anne Lundgaard and Kazinnik, Sophia},
  title  = {Can {ChatGPT} Decipher {Fedspeak}?},
  year   = {2023},
  note   = {SSRN 4399406}
}

@techreport{horton_filippas_manning_2023,
  author      = {Horton, John J. and Filippas, Apostolos and Manning, Benjamin S.},
  title       = {Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?},
  institution = {National Bureau of Economic Research},
  type        = {Working Paper},
  number      = {31122},
  year        = {2023},
  doi         = {10.3386/w31122},
  note        = {arXiv:2301.07543}
}

@article{argyle_etal_2023,
  author  = {Argyle, Lisa P. and Busby, Ethan C. and Fulda, Nancy and Gubler, Joshua R. and Rytting, Christopher and Wingate, David},
  title   = {Out of One, Many: Using Language Models to Simulate Human Samples},
  journal = {Political Analysis},
  volume  = {31},
  number  = {3},
  pages   = {337--351},
  year    = {2023},
  doi     = {10.1017/pan.2023.2}
}

% UNVERIFIED: authors' first names
@inproceedings{aher_arriaga_kalai_2023,
  author    = {Aher, Gati and Arriaga, Rosa I. and Kalai, Adam Tauman},
  title     = {Using Large Language Models to Simulate Multiple Humans and Replicate Human Subject Studies},
  booktitle = {Proceedings of the 40th International Conference on Machine Learning},
  series    = {PMLR},
  volume    = {202},
  pages     = {337--371},
  year      = {2023}
}

% UNVERIFIED: authors' first names
@techreport{brand_israeli_ngwe_2023,
  author      = {Brand, James and Israeli, Ayelet and Ngwe, Donald},
  title       = {Using {LLMs} for Market Research},
  institution = {Harvard Business School},
  type        = {Marketing Unit Working Paper},
  number      = {23-062},
  year        = {2023},
  note        = {SSRN 4395751}
}

@unpublished{park_etal_2024,
  author = {Park, Joon Sung and Zou, Carolyn Q. and Shaw, Aaron and Hill, Benjamin Mako and Cai, Carrie and Morris, Meredith Ringel and Willer, Robb and Liang, Percy and Bernstein, Michael S.},
  title  = {Generative Agent Simulations of 1,000 People},
  year   = {2024},
  note   = {arXiv:2411.10109}
}

% UNVERIFIED: first names; no journal version located; effect/participant counts differ across listings
@unpublished{hewitt_etal_2024,
  author = {Hewitt, Luke and Ashokkumar, Ashwini and Ghezae, Isaias and Willer, Robb},
  title  = {Predicting Results of Social Science Experiments Using Large Language Models},
  year   = {2024},
  note   = {Working paper}
}

%% ---------- Theme 2: Look-ahead, leakage, post-cutoff evaluation ----------

@techreport{ludwig_mullainathan_rambachan_2025,
  author      = {Ludwig, Jens and Mullainathan, Sendhil and Rambachan, Ashesh},
  title       = {Large Language Models: An Applied Econometric Framework},
  institution = {National Bureau of Economic Research},
  type        = {Working Paper},
  number      = {33344},
  year        = {2025},
  note        = {arXiv:2412.07031}
}

@unpublished{lopezlira_tang_zhu_2025,
  author = {Lopez-Lira, Alejandro and Tang, Yuehua and Zhu, Mingyin},
  title  = {The Memorization Problem: Can We Trust {LLMs}' Economic Forecasts?},
  year   = {2025},
  note   = {arXiv:2504.14765; SSRN 5217505}
}

% UNVERIFIED: venue (working paper dated June 2024; ICML 2025 workshop listing); SSRN id
@unpublished{sarkar_vafa_2024,
  author = {Sarkar, Suproteem K. and Vafa, Keyon},
  title  = {Lookahead Bias in Pretrained Language Models},
  year   = {2024}
}

@unpublished{glasserman_lin_2023,
  author = {Glasserman, Paul and Lin, Caden},
  title  = {Assessing Look-Ahead Bias in Stock Return Predictions Generated By {GPT} Sentiment Analysis},
  year   = {2023},
  note   = {arXiv:2309.17322}
}

@unpublished{he_etal_chrono_2025,
  author = {He, Songrun and Lv, Linying and Manela, Asaf and Wu, Jimmy},
  title  = {Chronologically Consistent Large Language Models},
  year   = {2025},
  note   = {arXiv:2502.21206}
}

@inproceedings{drinkall_etal_2024,
  author    = {Drinkall, Felix and Rahimikia, Eghbal and Pierrehumbert, Janet and Zohren, Stefan},
  title     = {Time Machine {GPT}},
  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2024},
  pages     = {3281--3292},
  year      = {2024},
  note      = {arXiv:2404.18543}
}

% UNVERIFIED: first names of third and fourth authors (first two from memory)
@techreport{kelly_etal_pit_2026,
  author      = {Kelly, Bryan and Malamud, Semyon and Schwab, {} and Xu, {}},
  title       = {Scaling Point-in-Time Language Models: Economic Evaluation of Embeddings},
  institution = {National Bureau of Economic Research},
  type        = {Working Paper},
  number      = {35247},
  year        = {2026},
  note        = {arXiv:2607.11889}
}

% UNVERIFIED: authors' first names
@unpublished{gao_jiang_yan_2025,
  author = {Gao, {} and Jiang, {} and Yan, {}},
  title  = {Detecting Lookahead Bias in {LLM} Forecasts},
  year   = {2025},
  note   = {arXiv:2512.23847. First version titled ``A Test of Lookahead Bias in LLM Forecasts''}
}

% UNVERIFIED: first name and exact full title
@unpublished{benhenda_2026,
  author = {Benhenda, {}},
  title  = {Look-Ahead-Bench},
  year   = {2026},
  note   = {arXiv:2601.13770}
}

@inproceedings{halawi_etal_2024,
  author    = {Halawi, Danny and Zhang, Fred and Yueh-Han, Chen and Steinhardt, Jacob},
  title     = {Approaching Human-Level Forecasting with Language Models},
  booktitle = {Advances in Neural Information Processing Systems},
  year      = {2024},
  note      = {arXiv:2402.18563}
}

% UNVERIFIED: full author list (Karger and Bastani are co-first authors)
@inproceedings{karger_etal_2025,
  author    = {Karger, Ezra and Bastani, Houtan and others},
  title     = {{ForecastBench}: A Dynamic Benchmark of {AI} Forecasting Capabilities},
  booktitle = {International Conference on Learning Representations},
  year      = {2025}
}

% UNVERIFIED: authors' first names; ICLR 2026 listing seen
@unpublished{paleka_etal_2025,
  author = {Paleka, {} and Goel, {} and Geiping, {} and Tram{\`e}r, {}},
  title  = {Pitfalls in Evaluating Language Model Forecasters},
  year   = {2025},
  note   = {arXiv:2506.00723}
}

% UNVERIFIED: authors' first names; volume/issue
@article{schoenegger_etal_2024,
  author  = {Schoenegger, {} and Tuminauskaite, {} and Park, {} and Tetlock, {}},
  title   = {Wisdom of the Silicon Crowd: {LLM} Ensemble Prediction Capabilities Rival Human Crowd Accuracy},
  journal = {Science Advances},
  year    = {2024},
  doi     = {10.1126/sciadv.adp1528}
}

%% ---------- Theme 3: Critiques and adjacent LLM survey literatures ----------

@article{bisbee_etal_2024,
  author  = {Bisbee, James and Clinton, Joshua D. and Dorff, Cassy and Kenkel, Brenton and Larson, Jennifer M.},
  title   = {Synthetic Replacements for Human Survey Data? The Perils of Large Language Models},
  journal = {Political Analysis},
  volume  = {32},
  pages   = {401--416},
  year    = {2024},
  doi     = {10.1017/pan.2024.5}
}

@inproceedings{dominguezolmedo_etal_2024,
  author    = {Dominguez-Olmedo, Ricardo and Hardt, Moritz and Mendler-D{\"u}nner, Celestine},
  title     = {Questioning the Survey Responses of Large Language Models},
  booktitle = {Advances in Neural Information Processing Systems},
  volume    = {37},
  year      = {2024},
  note      = {arXiv:2306.07951}
}

% UNVERIFIED: volume and pages
@article{tjuatja_etal_2024,
  author  = {Tjuatja, Lindia and Chen, Valerie and Wu, Tongshuang and Talwalkar, Ameet and Neubig, Graham},
  title   = {Do {LLMs} Exhibit Human-like Response Biases? A Case Study in Survey Design},
  journal = {Transactions of the Association for Computational Linguistics},
  year    = {2024},
  note    = {ACL Anthology 2024.tacl-1.56}
}

% UNVERIFIED: authors' first names
@inproceedings{santurkar_etal_2023,
  author    = {Santurkar, Shibani and Durmus, Esin and Ladhak, Faisal and Lee, Cinoo and Liang, Percy and Hashimoto, Tatsunori},
  title     = {Whose Opinions Do Language Models Reflect?},
  booktitle = {Proceedings of the 40th International Conference on Machine Learning},
  series    = {PMLR},
  volume    = {202},
  pages     = {29971--30004},
  year      = {2023}
}

@unpublished{gui_toubia_2023,
  author = {Gui, George and Toubia, Olivier},
  title  = {The Challenge of Using {LLMs} to Simulate Human Behavior: A Causal Inference Perspective},
  year   = {2023},
  note   = {arXiv:2312.15524}
}

% UNVERIFIED: journal volume, pages and DOI from a citing paper's reference list; journal page not retrieved
@article{wang_morgenstern_dickerson_2025,
  author  = {Wang, Angelina and Morgenstern, Jamie and Dickerson, John P.},
  title   = {Large Language Models That Replace Human Participants Can Harmfully Misportray and Flatten Identity Groups},
  journal = {Nature Machine Intelligence},
  volume  = {7},
  pages   = {400--411},
  year    = {2025},
  doi     = {10.1038/s42256-025-00986-z},
  note    = {arXiv:2402.01908}
}

@inproceedings{krsteski_etal_2026,
  author    = {Krsteski, Stefan and Russo, Giuseppe and Chang, Serina and West, Robert and Gligori{\'c}, Kristina},
  title     = {Valid Survey Simulations with Limited Human Data: The Roles of Prompting, Fine-Tuning, and Rectification},
  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics (ACL)},
  year      = {2026},
  note      = {arXiv:2510.11408}
}

% UNVERIFIED: authors' first names
@article{angelopoulos_etal_2023,
  author  = {Angelopoulos, Anastasios N. and Bates, Stephen and Fannjiang, Clara and Jordan, Michael I. and Zrnic, Tijana},
  title   = {Prediction-Powered Inference},
  journal = {Science},
  volume  = {382},
  number  = {6671},
  pages   = {669--674},
  year    = {2023},
  doi     = {10.1126/science.adi6000}
}

% UNVERIFIED: authors from a secondary bibliography
@unpublished{lukauskas_sarkauskaite_2026,
  author = {Lukauskas, Mantas and {\v{S}}arkauskait{\.e}, Viktorija},
  title  = {Plausible but Not Valid: A Psychometric Audit of {LLMs} as Synthetic Survey Respondents},
  year   = {2026},
  note   = {arXiv:2608.14606}
}

% UNVERIFIED: full author list
@unpublished{tadaymorocho_etal_2026,
  author = {Taday Morocho, {} and others},
  title  = {Assessing the Reliability of Persona-Conditioned {LLMs} as Synthetic Survey Respondents},
  year   = {2026},
  note   = {arXiv:2602.18462}
}

% UNVERIFIED: authors' first names
@unpublished{kim_lee_2023,
  author = {Kim, {} and Lee, {}},
  title  = {{AI}-Augmented Surveys: Leveraging Large Language Models and Surveys for Opinion Prediction},
  year   = {2023},
  note   = {arXiv:2305.09620}
}

% UNVERIFIED: author list beyond the first author
@inproceedings{suh_etal_2025,
  author    = {Suh, Joseph Jeesung and others},
  title     = {Language Model Fine-Tuning on Scaled Survey Data for Predicting Distributions of Public Opinions},
  booktitle = {Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},
  pages     = {21147--21170},
  year      = {2025},
  note      = {arXiv:2502.16761}
}

@inproceedings{meister_guestrin_hashimoto_2025,
  author    = {Meister, Nicole and Guestrin, Carlos and Hashimoto, Tatsunori},
  title     = {Benchmarking Distributional Alignment of Large Language Models},
  booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},
  pages     = {24--49},
  year      = {2025},
  doi       = {10.18653/v1/2025.naacl-long.2}
}

@inproceedings{cao_etal_2025,
  author    = {Cao, Yong and Liu, Haijiang and Arora, Arnav and Augenstein, Isabelle and R{\"o}ttger, Paul and Hershcovich, Daniel},
  title     = {Specializing Large Language Models to Simulate Survey Response Distributions for Global Populations},
  booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},
  pages     = {3141--3154},
  year      = {2025},
  doi       = {10.18653/v1/2025.naacl-long.162}
}

% UNVERIFIED: full author list (first four from the arXiv v2 listing)
@unpublished{durmus_etal_2023,
  author = {Durmus, Esin and Nguyen, Karina and Liao, Thomas I. and Schiefer, Nicholas and others},
  title  = {Towards Measuring the Representation of Subjective Global Opinions in Language Models},
  year   = {2023},
  note   = {arXiv:2306.16388}
}

% UNVERIFIED: authors' first names; volume and year differ across listings
@article{vonderheyde_etal_2025,
  author  = {von der Heyde, {} and Haensch, {} and Wenz, {}},
  title   = {Vox Populi, Vox {AI}? Using Language Models to Estimate {German} Public Opinion},
  journal = {Social Science Computer Review},
  year    = {2025},
  doi     = {10.1177/08944393251337014},
  note    = {arXiv:2407.08563}
}

@article{qu_wang_2024,
  author  = {Qu, Yao and Wang, Jue},
  title   = {Performance and Biases of Large Language Models in Public Opinion Simulation},
  journal = {Humanities and Social Sciences Communications},
  volume  = {11},
  pages   = {1095},
  year    = {2024},
  doi     = {10.1057/s41599-024-03609-x}
}

@unpublished{atari_etal_2023,
  author = {Atari, Mohammad and Xue, Mona J. and Park, Peter S. and Blasi, Dami{\'a}n E. and Henrich, Joseph},
  title  = {Which Humans?},
  year   = {2023},
  note   = {PsyArXiv; Harvard working paper}
}

%% ---------- Theme 4: Human-side benchmarks ----------

@article{malmendier_nagel_2016,
  author  = {Malmendier, Ulrike and Nagel, Stefan},
  title   = {Learning from Inflation Experiences},
  journal = {Quarterly Journal of Economics},
  volume  = {131},
  number  = {1},
  pages   = {53--87},
  year    = {2016},
  doi     = {10.1093/qje/qjv037}
}

@article{dacunto_etal_2021,
  author  = {D'Acunto, Francesco and Malmendier, Ulrike and Ospina, Juan and Weber, Michael},
  title   = {Exposure to Grocery Prices and Inflation Expectations},
  journal = {Journal of Political Economy},
  volume  = {129},
  number  = {5},
  pages   = {1615--1639},
  year    = {2021}
}

@article{cavallo_cruces_pereztruglia_2017,
  author  = {Cavallo, Alberto and Cruces, Guillermo and Perez-Truglia, Ricardo},
  title   = {Inflation Expectations, Learning, and Supermarket Prices: Evidence from Survey Experiments},
  journal = {American Economic Journal: Macroeconomics},
  volume  = {9},
  number  = {3},
  pages   = {1--35},
  year    = {2017},
  doi     = {10.1257/mac.20150147}
}

% UNVERIFIED: volume, issue and pages (ambiguous listing); title and year confirmed
@article{armantier_etal_2016,
  author  = {Armantier, Olivier and Nelson, Scott and Topa, Giorgio and van der Klaauw, Wilbert and Zafar, Basit},
  title   = {The Price Is Right: Updating Inflation Expectations in a Randomized Price Information Experiment},
  journal = {Review of Economics and Statistics},
  volume  = {98},
  number  = {3},
  pages   = {503--523},
  year    = {2016}
}

@article{carroll_2003,
  author  = {Carroll, Christopher D.},
  title   = {Macroeconomic Expectations of Households and Professional Forecasters},
  journal = {Quarterly Journal of Economics},
  volume  = {118},
  number  = {1},
  pages   = {269--298},
  year    = {2003}
}

@article{coibion_gorodnichenko_2015,
  author  = {Coibion, Olivier and Gorodnichenko, Yuriy},
  title   = {Information Rigidity and the Expectations Formation Process: A Simple Framework and New Facts},
  journal = {American Economic Review},
  volume  = {105},
  number  = {8},
  pages   = {2644--2678},
  year    = {2015}
}

@article{andre_etal_2022,
  author  = {Andre, Peter and Pizzinelli, Carlo and Roth, Christopher and Wohlfart, Johannes},
  title   = {Subjective Models of the Macroeconomy: Evidence From Experts and Representative Samples},
  journal = {Review of Economic Studies},
  volume  = {89},
  number  = {6},
  pages   = {2958--2991},
  year    = {2022},
  doi     = {10.1093/restud/rdac008}
}

@article{coibion_gorodnichenko_weber_2022,
  author  = {Coibion, Olivier and Gorodnichenko, Yuriy and Weber, Michael},
  title   = {Monetary Policy Communications and Their Effects on Household Inflation Expectations},
  journal = {Journal of Political Economy},
  volume  = {130},
  number  = {6},
  pages   = {1537--1584},
  year    = {2022},
  doi     = {10.1086/718982}
}

@article{weber_etal_2025,
  author  = {Weber, Michael and Candia, Bernardo and Afrouzi, Hassan and Ropele, Tiziano and Lluberas, Rodrigo and Frache, Serafin and Meyer, Brent and Kumar, Saten and Gorodnichenko, Yuriy and Georgarakos, Dimitris and Coibion, Olivier and Kenny, Geoff and Ponce, Jorge},
  title   = {Tell Me Something {I} Don't Already Know: Learning in Low- and High-Inflation Settings},
  journal = {Econometrica},
  volume  = {93},
  number  = {1},
  pages   = {229--264},
  year    = {2025},
  doi     = {10.3982/ECTA22764}
}

@article{coibion_etal_forwardguidance_2023,
  author  = {Coibion, Olivier and Georgarakos, Dimitris and Gorodnichenko, Yuriy and Weber, Michael},
  title   = {Forward Guidance and Household Expectations},
  journal = {Journal of the European Economic Association},
  volume  = {21},
  number  = {5},
  pages   = {2131--2171},
  year    = {2023}
}

@article{haaland_roth_wohlfart_2023,
  author  = {Haaland, Ingar and Roth, Christopher and Wohlfart, Johannes},
  title   = {Designing Information Provision Experiments},
  journal = {Journal of Economic Literature},
  volume  = {61},
  number  = {1},
  pages   = {3--40},
  year    = {2023},
  doi     = {10.1257/jel.20211658}
}

% UNVERIFIED: full author list; number and year from RePEc snippet
@techreport{wohlfart_2026,
  author      = {Wohlfart, Johannes},
  title       = {Do People Have Economic Expectations?},
  institution = {ECONtribute},
  type        = {Discussion Paper},
  number      = {402},
  year        = {2026}
}

@article{haldane_mcmahon_2018,
  author  = {Haldane, Andrew and McMahon, Michael},
  title   = {Central Bank Communications and the General Public},
  journal = {AEA Papers and Proceedings},
  volume  = {108},
  pages   = {578--583},
  year    = {2018},
  doi     = {10.1257/pandp.20181082}
}

@article{bholat_etal_2019,
  author  = {Bholat, David and Broughton, Nida and Ter Meer, Janna and Walczak, Eryk},
  title   = {Enhancing Central Bank Communications Using Simple and Relatable Information},
  journal = {Journal of Monetary Economics},
  volume  = {108},
  pages   = {1--15},
  year    = {2019},
  doi     = {10.1016/j.jmoneco.2019.08.007}
}

@article{blinder_etal_2024,
  author  = {Blinder, Alan S. and Ehrmann, Michael and de Haan, Jakob and Jansen, David-Jan},
  title   = {Central Bank Communication with the General Public: Promise or False Hope?},
  journal = {Journal of Economic Literature},
  volume  = {62},
  number  = {2},
  pages   = {425--457},
  year    = {2024},
  doi     = {10.1257/jel.20231683}
}

% UNVERIFIED: author list and working paper number; title and series/year confirmed
@techreport{haldane_macaulay_mcmahon_2020,
  author      = {Haldane, Andrew and Macaulay, Alistair and McMahon, Michael},
  title       = {The 3 {E}'s of Central Bank Communication with the Public},
  institution = {Bank of England},
  type        = {Staff Working Paper},
  year        = {2020}
}

%% 4C consumer confidence and quantification

@article{carroll_fuhrer_wilcox_1994,
  author  = {Carroll, Christopher D. and Fuhrer, Jeffrey C. and Wilcox, David W.},
  title   = {Does Consumer Sentiment Forecast Household Spending? If So, Why?},
  journal = {American Economic Review},
  volume  = {84},
  number  = {5},
  pages   = {1397--1408},
  year    = {1994}
}

@article{ludvigson_2004,
  author  = {Ludvigson, Sydney C.},
  title   = {Consumer Confidence and Consumer Spending},
  journal = {Journal of Economic Perspectives},
  volume  = {18},
  number  = {2},
  pages   = {29--50},
  year    = {2004},
  doi     = {10.1257/0895330041371222}
}

% UNVERIFIED: authors' first names
@article{barsky_sims_2012,
  author  = {Barsky, Robert B. and Sims, Eric R.},
  title   = {Information, Animal Spirits, and the Meaning of Innovations in Consumer Confidence},
  journal = {American Economic Review},
  volume  = {102},
  number  = {4},
  pages   = {1343--1377},
  year    = {2012}
}

% UNVERIFIED: authors' first names
@article{bachmann_berg_sims_2015,
  author  = {Bachmann, R{\"u}diger and Berg, Tim O. and Sims, Eric R.},
  title   = {Inflation Expectations and Readiness to Spend: Cross-Sectional Evidence},
  journal = {American Economic Journal: Economic Policy},
  volume  = {7},
  number  = {1},
  pages   = {1--35},
  year    = {2015},
  doi     = {10.1257/pol.20130292}
}

@article{carlson_parkin_1975,
  author  = {Carlson, John A. and Parkin, Michael},
  title   = {Inflation Expectations},
  journal = {Economica},
  volume  = {42},
  pages   = {123--138},
  year    = {1975}
}

@article{batchelor_orr_1988,
  author  = {Batchelor, Roy A. and Orr, Adrian B.},
  title   = {Inflation Expectations Revisited},
  journal = {Economica},
  volume  = {55},
  number  = {219},
  pages   = {317--331},
  year    = {1988}
}

@incollection{pesaran_weale_2006,
  author    = {Pesaran, M. Hashem and Weale, Martin},
  title     = {Survey Expectations},
  booktitle = {Handbook of Economic Forecasting},
  editor    = {Elliott, Graham and Granger, Clive W. J. and Timmermann, Allan},
  volume    = {1},
  chapter   = {14},
  pages     = {715--776},
  publisher = {Elsevier},
  year      = {2006}
}

@article{nardo_2003,
  author  = {Nardo, Michela},
  title   = {The Quantification of Qualitative Survey Data: A Critical Assessment},
  journal = {Journal of Economic Surveys},
  volume  = {17},
  number  = {5},
  pages   = {645--668},
  year    = {2003},
  doi     = {10.1046/j.1467-6419.2003.00208.x}
}

%% 4D EC survey and ECB CES

@techreport{arioli_etal_2017,
  author      = {Arioli, Rodolfo and Bates, Colm and Dieden, Heinz and Duca, Ioana and Friz, Roberta and Gayer, Christian and Kenny, Geoff and Meyler, Aidan and Pavlova, Iskra},
  title       = {{EU} Consumers' Quantitative Inflation Perceptions and Expectations: An Evaluation},
  institution = {European Central Bank},
  type        = {Occasional Paper},
  number      = {186},
  year        = {2017}
}

@article{ducaradu_kenny_reuter_2021,
  author  = {Duca-Radu, Ioana and Kenny, Geoff and Reuter, Andreas},
  title   = {Inflation Expectations, Consumption and the Lower Bound: Micro Evidence from a Large Multi-Country Survey},
  journal = {Journal of Monetary Economics},
  volume  = {118},
  pages   = {120--134},
  year    = {2021},
  doi     = {10.1016/j.jmoneco.2020.03.005}
}

@article{andrade_gautier_mengus_2023,
  author  = {Andrade, Philippe and Gautier, Erwan and Mengus, Eric},
  title   = {What Matters in Households' Inflation Expectations?},
  journal = {Journal of Monetary Economics},
  volume  = {138},
  pages   = {50--68},
  year    = {2023},
  doi     = {10.1016/j.jmoneco.2023.05.007}
}

% UNVERIFIED: edition to cite (January 2023 PDF confirmed; a March 2026 guide is listed but was not opened)
@manual{ec_bcs_userguide,
  organization = {{European Commission, Directorate-General for Economic and Financial Affairs}},
  title        = {The Joint Harmonised {EU} Programme of Business and Consumer Surveys: User Guide},
  year         = {2023}
}

@techreport{bankowska_etal_2021,
  author      = {Ba{\'n}kowska, Katarzyna and Borlescu, Ana Maria and Charalambakis, Evangelos and Dias Da Silva, Ant{\'o}nio and Di Laurea, Davide and Dossche, Maarten and Georgarakos, Dimitris and Honkkila, Juha and Kennedy, Neale O. and Kenny, Geoff and Kolndrekaj, Aleksandra and Meyer, Justus and Rusinova, Desislava and Teppa, Federica and T{\"o}rm{\"a}lehto, Veli-Matti},
  title       = {{ECB} Consumer Expectations Survey: An Overview and First Evaluation},
  institution = {European Central Bank},
  type        = {Occasional Paper},
  number      = {287},
  year        = {2021},
  doi         = {10.2866/310866}
}

%% 4E demographic gradients

@article{das_kuhnen_nagel_2020,
  author  = {Das, Sreyoshi and Kuhnen, Camelia M. and Nagel, Stefan},
  title   = {Socioeconomic Status and Macroeconomic Expectations},
  journal = {Review of Financial Studies},
  volume  = {33},
  number  = {1},
  pages   = {395--432},
  year    = {2020},
  doi     = {10.1093/rfs/hhz041}
}

@article{dacunto_malmendier_weber_2021,
  author  = {D'Acunto, Francesco and Malmendier, Ulrike and Weber, Michael},
  title   = {Gender Roles Produce Divergent Economic Expectations},
  journal = {Proceedings of the National Academy of Sciences},
  volume  = {118},
  number  = {21},
  pages   = {e2008534118},
  year    = {2021},
  doi     = {10.1073/pnas.2008534118}
}

@article{bruinedebruin_etal_2010,
  author  = {Bruine de Bruin, W{\"a}ndi and van der Klaauw, Wilbert and Downs, Julie S. and Fischhoff, Baruch and Topa, Giorgio and Armantier, Olivier},
  title   = {Expectations of Inflation: The Role of Demographic Variables, Expectation Formation, and Financial Literacy},
  journal = {Journal of Consumer Affairs},
  volume  = {44},
  number  = {2},
  pages   = {381--402},
  year    = {2010},
  doi     = {10.1111/j.1745-6606.2010.01174.x}
}

%% ---------- Theme 5: SSR and follow-ups ----------

% UNVERIFIED: full author list (nine authors; Maier first; Aslak and Fiaschi among them, first names from memory)
@unpublished{maier_etal_2025,
  author = {Maier, Benjamin F. and Aslak, Ulf and Fiaschi, Luca and others},
  title  = {{LLMs} Reproduce Human Purchase Intent via Semantic Similarity Elicitation of {Likert} Ratings},
  year   = {2025},
  note   = {arXiv:2510.08338}
}

@unpublished{verapichardo_2026,
  author = {Vera Pichardo, Eduardo},
  title  = {Measuring Self-Rating Bias in {LLM}-Generated Survey Data: A Semantic Similarity Framework for Independent Scale Mapping},
  year   = {2026},
  note   = {arXiv:2602.13862}
}
```

---

## 6. Round 2 changes

**What changed**

1. *Gap claim.* Section 2 and Section 3 now use "no paper located" throughout; the "unlike existing work" sentence is removed and explicitly ruled out. The gap answer is restated by component: post-cutoff validation and persistence baselines already exist; SSR in macro, consumer-confidence items and the EC survey are not located; qualitative shares by subgroup is unresolved. Post-cutoff evaluation is reclassified from differentiator to requirement.
2. *Anesti, Hill and Joseph.* Entry rewritten with the round 2 findings (two IAS samples around late 2022, after the September 2021 cutoff; quasi-experiment framing; weak and unstable micro-level match) and named as the paper to beat. Whether targets are banded shares remains not established.
3. *HouseholdBench.* NBER number rechecked (35927 on nber.org; one aggregator shows 35955); arXiv id and date confirmed; pre/post-cutoff split at 16 February 2026 added; proximity raised to 5.
4. *Lin, Sun and Yan.* Michigan questions identified (short- and long-term inflation and home price expectations, numeric); distributional comparison and open-ended explanations added.
5. *Wu, Xi and Xie.* Replicated RCT confirmed as Weber et al. (2025); design details added.
6. *Positioning.* Rebuilt around the persistence and memorised-levels problem, with three question candidates (SSR and under-dispersion; personas for households; skill over persistence) and a hedged contribution statement.
7. *New blocks, each item searched:* 2B post-cutoff forecasting evaluation; 3B subgroup answer-distribution prediction; 3C cross-country fidelity; 4C consumer confidence and quantification; 4D EC survey and CES microdata and documentation; 4E demographic gradients; plus prediction-powered inference and Tjuatja et al. Previously unsearched leads (Carroll 2003; Coibion-Gorodnichenko 2015; Bachmann-Berg-Sims 2015; Andre et al. 2022) searched and confirmed.
8. *Citations.* Confirmed and updated: Coibion et al. in *JEEA* 21(5), 2131-2171; Drinkall et al. in Findings of NAACL 2024; Glasserman and Caden Lin; He et al. four authors; Cao et al. author list corrected against the critic's recollection. Wang et al. updated to *Nature Machine Intelligence* from a secondary source and flagged. About thirty-one BibTeX entries added. Four round 1 entries for no-author or thin-provenance items removed (Utama et al., the tariff paper, the semantic-baselines paper, Dillion et al.) and the items moved to Section 1L. Proximity scores re-assigned under one explicit rule.
9. *New searches run for the gap:* consumer confidence, consumer sentiment, Index of Consumer Sentiment, business and consumer survey, consumer confidence indicator, open-ended elicitation with category classification, embedding mapping. None returned a macro application.

**What remains unverified**

- The question format and fit metric in Anesti, Hill and Joseph. The gap claim cannot be upgraded until that paper is read.
- The six HouseholdBench surveys and the use of its post-cutoff split.
- Everything in Section 1L and every `% UNVERIFIED` line in Section 5.
- Critic items confirmed only in part: the EC User Guide's per-question options; the ForecastBench and Durmus et al. author lists; journal status of Gui-Toubia and Hewitt et al. (none located).
- Not searched in either round: Dillion et al. (2023); the Armantier et al. *REStat* pages; SCE documentation (Armantier et al. 2017).

**Process note.** This agent has no in-place edit tool, so the file was re-saved in full with round 1 content carried over and revised; the structure and evidence tags are unchanged. The share of unpublished entries has fallen because the added blocks are mostly journal articles, but Theme 1 remains almost entirely working papers, which reflects the field.

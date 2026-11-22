# Literature Review: LLM Synthetic Respondents for Macroeconomic Household Surveys (SSR Transfer)

**Agent:** librarian | **Phase:** Discovery | **Date:** 2026-11-22
**Status:** Unscored (awaiting librarian-critic)

## 0. How to read this file

**Evidence standard.** Network access was limited to web search; no paper full text was opened (arxiv.org and most hosts are blocked for fetching). Every entry therefore rests on search-result snippets (abstract pages, RePEc/NBER/publisher listings). Each entry carries a verification tag:

- **[V]** bibliographic details confirmed by a search result from a primary listing (publisher, NBER, RePEc, arXiv, central bank site).
- **[V-partial]** paper confirmed to exist; one or more details (authors, venue, numbers) come only from a secondary source or are inconsistent across sources. The uncertain detail is named.
- **[U]** not confirmed by any search in this session; included from the requester's or my recollection. Marked `% UNVERIFIED` in BibTeX. Do not cite before checking.

Summaries describe abstracts, not full papers. Magnitudes are quoted only where a snippet reported them. Anything about a paper's internal design that the abstract did not state (for example, exactly how a training cutoff was handled) is flagged as not established.

**Proximity score** (1-5): 5 = directly competes; 4 = closely related, different angle; 3 = related method or context; 2 = tangential; 1 = background.

**Corrections to the items you recalled**

| Recalled item | Status | Correction |
|---|---|---|
| Bybee, "Surveying Generative AI's Economic Expectations" | [V] | arXiv 2305.02823 (May 2023), J. Leland Bybee. Later retitled "The Ghost in the Machine: Generating Beliefs with Large Language Models" (NBER conference version dated December 2023). No journal version found. |
| Horton, "homo silicus" | [V] | Three authors in current versions: Horton, Filippas, Manning. NBER WP 31122 (April 2023), arXiv 2301.07543; arXiv revised as late as February 2026 with more models. |
| Hansen et al., simulating the SPF | [V] | Hansen, Horton, Kazinnik, Puzzello, Zarifhonarvar, "Simulating the Survey of Professional Forecasters". Working paper (Dec 2024 / Feb 2025 drafts). No journal version found. |
| Faria-e-Castro and Leibovici | [V] | "Artificial Intelligence and Inflation Forecasts", St. Louis Fed WP 2023-015; published in Federal Reserve Bank of St. Louis *Review* 106(12), 2024. Uses Google PaLM; forecasts are in-sample (2019-2023), which matters for the look-ahead theme. |
| Zarifhonarvar on LLM inflation expectations | [V-partial] | Earlier titles: "Experimental Evidence on Large Language Models" and "Evidence on Inflation Expectations Formation Using Large Language Models". Current title: "Generating Inflation Expectations with Large Language Models". Reported as published in *Journal of Monetary Economics* vol. 157, article 103859; the publisher landing page itself was not retrieved, so volume/article number are from secondary citations. |
| Argyle et al., "Out of One, Many" | [V] | *Political Analysis* 31(3), 2023, pp. 337-351, DOI 10.1017/pan.2023.2. Six authors. |

---

## 1. Annotated bibliography

### Theme 1 — LLMs as simulated respondents for economic expectations and macro surveys

#### 1A. Households and consumers (closest to the proposed paper)

**Zarifhonarvar (2025/2026), "Generating Inflation Expectations with Large Language Models"** — [V-partial] — Proximity 5
- Summary: Single-author paper (Indiana University job market paper). Builds LLM agents whose personas mimic the demographic composition of the NY Fed Survey of Consumer Expectations and runs survey experiments on inflation expectations with proprietary and open-source models. Compares generated expectations with SCE patterns and randomizes information treatments following the Coibion et al. designs. Argues central banks could use such models to pre-test messaging.
- Identification / design: Simulated survey experiment; randomized information treatments across LLM personas; comparison to SCE moments.
- Data: NY Fed SCE demographic structure; GPT-4 Turbo in the early version, multiple proprietary and open-source models later.
- Main result: Some LLMs report inflation expectations above actual inflation, as households do; information treatments shift expectations (mortgage-rate information in the early version, forward guidance on inflation in the later version); proprietary models show less disagreement than open-source ones; the information available to the model affects the variance of responses. No magnitudes in snippets.
- Elicitation: numeric point expectations as far as the abstracts show. Whether any post-cutoff validation is included was not established.
- Why it matters: occupies both of your second-step ideas (in-silico information RCTs and communication pre-testing) for US households.

**Anesti, Hill and Joseph (2026), "Inflation attitudes of large language models"** — [V] — Proximity 5
- Summary: Bank of England Staff Working Paper No. 1,190 (19 June 2026); arXiv 2512.14306 (16 Dec 2025). Uses a synthetic survey to replicate the Bank of England Inflation Attitudes Survey with GPT-3.5 Turbo, conditioning on household characteristics and macroeconomic price signals. Introduces a Shapley-value decomposition of synthetic survey outputs.
- Identification / design: A snippet from the paper states it exploits GPT's training cutoff (September 2021) to test out-of-time behaviour and replicates two waves of the IAS. The extent and strictness of the post-cutoff evaluation is not established beyond that sentence.
- Data: Bank of England/Ipsos Inflation Attitudes Survey; official price statistics.
- Main result: Tracks aggregate survey results and official statistics at short horizons; reproduces some differences by income, housing tenure and social class; shows heightened sensitivity to food-price information, like humans; lacks a consistent model of consumer price inflation (unexplained kinks in component sensitivity).
- Why it matters: the only central bank working paper found that simulates a household expectations survey and explicitly uses the training cutoff. Describes itself as closest to Zarifhonarvar.

**Wu, Xi and Xie (2025), "LLM Survey Framework: Coverage, Reasoning, Dynamics, Identification"** — [V] — Proximity 5
- Summary: NBER WP 34308 (October 2025). Proposes an LLM-based survey framework offering retrospective coverage, elicited reasoning, dynamic effects and clean identification, at roughly 0.5 cents per response. Validates by replicating a multi-wave inflation expectations RCT, then extends the human benchmark from 10 waves (2018-2023) to over 50 waves back to 1990.
- Identification / design: In-silico replication of a multi-wave information-provision RCT, attributed to Weber et al. (2025); one snippet noted inconsistent attribution across versions (Coibion et al. 2022 also cited).
- Main result: LLM respondents update in patterns comparable to humans. A discussant deck from a 2026 Cleveland Fed conference criticized the validation for covering mainly central tendencies and treatment effects.
- Why it matters: the direction is retrospective (backcasting to 1990), the opposite of your post-cutoff design, and so is maximally exposed to look-ahead. That contrast is a positioning asset. Also presented at an ECB forecasting conference (23 March 2026).

**Lin, Sun and Yan (2025), "Simulating Macroeconomic Expectations using LLM Agents"** — [V] — Proximity 5
- Summary: arXiv 2505.17648 (v1 23 May 2025; v4 25 Nov 2025). Earlier title: "Simulating Macroeconomic Expectations in Survey Experiments with LLM-based Economic Agents". Modular LLM-agent framework (personal traits, prior expectations, knowledge modules) replicating three survey experiments across households and experts; one version reports 6,032 household agents and 435 expert agents.
- Identification / design: Replication of published survey experiments; plus a pre-estimation of long- and short-term inflation and home price expectations in the 2025 Michigan Survey of Consumers "to examine out-of-sample performance".
- Main result: Agent expectations are more homogeneous than human ones but outperform plain prompt engineering and retain key heterogeneity. Accuracy of the 2025 MSC predictions was not reported in snippets.
- Why it matters: the closest existing instance of forward, out-of-sample prediction of a household survey. Targets numeric expectations, not qualitative response shares.

**Huang, Ferreras Garrucho, Xie, Yuan, Mei, Lian and Hazell (2026), "HouseholdBench: Evaluating Large Language Models as Predictors of Household Economic Behavior"** — [V] — Proximity 4
- Summary: arXiv 2610.07563 (6 Oct 2026); NBER WP 35927. Benchmark of 6 US household surveys and 32 prediction tasks (numeric, categorical, probabilistic) across consumption, income, labor, expectations and housing; 13 LLMs against a no-change baseline and gradient-boosted trees.
- Main result: Most models beat no-change; best model cuts numeric error by 12.2%; gradient-boosted trees rank first on most tasks; a fine-tuned 4B open-weight model with 16-draw averaging can match proprietary models.
- Why it matters: very recent, senior macro authors, includes categorical outcomes and expectations. This is individual-level prediction rather than aggregate response shares. Which surveys are included and how leakage is handled was not established; check before finalizing positioning.

**Utama, Andina and Oktavia (2026), "Effects of Information Treatments on Household Inflation Expectations in Indonesia: A Generative AI Experiment"** — [V-partial] — Proximity 4
- Summary: Paper on the BIS website for a 2026 conference (file `accconf2026/Paper_1_ID_251216.pdf`). Generates household inflation expectations for 5,400 personas with GPT and Gemini where no household expectations survey exists, and tests central bank and media information treatments.
- Unverified: author affiliations (presumably Bank Indonesia), exact conference name, results.
- Why it matters: central-bank-side use of synthetic households for communication testing; no human benchmark by construction.

**"Tariff Threats, Macroeconomic Expectations, and Policy Communication Strategies: Experiments Based on a Multi-Agent System" (2026)** — [V-partial] — Proximity 4
- Summary: arXiv 2608.30522 (31 Aug 2026). Converts 300 Michigan Survey of Consumers households into persistent LLM agents exposed to social-media information over simulated months; a second experiment finds central bank explanations can coordinate beliefs, with effects on mean expectations depending on message content.
- Unverified: **authors not retrieved**. Details from aggregator pages only.

**Graham, Harvey and Jha (2026), "CFOs Meet LLMs"** — [V] — Proximity 3
- Summary: arXiv 2606.13812 (June 2026; PDF dated 8 Sept 2026). Generates synthetic answers to the Duke-Fed CFO Survey optimism question for 6,075 firm-quarter responses (2002-2025), matched to the actual CFO at the same firm and quarter.
- Main result: Synthetic optimism predicts the actual response conditional on firm and year-quarter fixed effects and the lagged response; accuracy rises with information supplied. Secondary snippets: LLM mean 56.6 vs actual 60.1; synthetic panel under-disperses by roughly 25%.
- Why it matters: firm-side analogue with individual-level matching; documents under-dispersion.

**Kazinnik (2023/2025), "Bank Run, Interrupted: Modeling Deposit Withdrawals with Generative AI"** — [V] — Proximity 3
- Summary: SSRN 4656722; listed at *Management Science* (DOI 10.1287/mnsc.2024.06807). Synthetic depositors with demographic attributes are exposed to a panic post and randomized bank/Fed communication interventions; responses validated against human benchmarks; feeds a contagion model.
- Main result: Direct, personalized reassurance with explicit survival clauses reduces withdrawal intent.
- Why it matters: precedent for in-silico communication RCTs on households in a top management journal.

#### 1B. Professional forecasters and LLM macro forecasts

**Hansen, Horton, Kazinnik, Puzzello and Zarifhonarvar (2024/2025), "Simulating the Survey of Professional Forecasters"** — [V] — Proximity 4
- Summary: Synthetic forecaster personas from hand-collected SPF participant characteristics, fed real-time macro data; quarterly forecasts for 23 variables, 1999-2023.
- Main result: Reproduces forecast accuracy, median levels, revision dynamics and cross-sectional dispersion of the human panel (per author page). How the knowledge cutoff is handled was not established from snippets.

**Iadisernia and Camassa (2025), "Prompting for Policy: Forecasting Macroeconomic Scenarios with Synthetic LLM Personas"** — [V] — Proximity 4
- Summary: Banca d'Italia authors; arXiv 2511.02458; ICAIF 2025. GPT-4o with 2,368 economics personas (PersonaHub) replicates the ECB SPF over 50 quarterly rounds (2013-2025), four variables, four horizons, against 100 no-persona baseline forecasts.
- Main result: GPT-4o and human forecasters reach similar accuracy; **persona descriptions add no measurable accuracy**; diverse personas produce relatively homogeneous forecasts.
- Why it matters: a euro-area central bank paper with a direct negative result on the value of personas. Your design must show that demographic conditioning does work for households, or explain why it should differ.

**Bybee (2023), "Surveying Generative AI's Economic Expectations" / "The Ghost in the Machine"** — [V] — Proximity 4
- Summary: Feeds Wall Street Journal articles (1984-2021) to an LLM to generate expectations of financial and macro variables.
- Main result: Generated expectations track the SPF, AAII and Duke CFO surveys; return expectations are extrapolative and negatively related to future realized returns; correlations hold on articles after the training period.
- Why it matters: first macro paper to use a post-training sample as a memorization check.

**Faria-e-Castro and Leibovici (2023/2024), "Artificial Intelligence and Inflation Forecasts"** — [V] — Proximity 3
- Summary: PaLM-generated retrospective conditional inflation forecasts, 2019-2023, against the SPF.
- Main result: Lower mean-squared errors than the SPF in most years and horizons; slower reversion to the 2% anchor. In-sample by the authors' own description.

**Alam, Boyle, Li and Sekhposyan (2026), "ChatMacro: Evaluating Inflation Forecasts of Generative AI"** — [V] — Proximity 4
- Summary: FRBSF WP 2026-04 (5 Feb 2026); CEPR DP 21057.
- Main result: Forecasts in pseudo out-of-sample settings are comparable to benchmarks, but **true out-of-sample predictions are largely inaccurate and stale**.
- Why it matters: the strongest warning that pre-cutoff performance does not carry over. Directly motivates your post-cutoff-only design and is a risk to your results.

**Kazinnik and Sinclair (2025/2026), "FOMC In Silico: A Multi-Agent System for Monetary Policy Decision Modeling"** — [V] — Proximity 2
- Summary: LLM agents representing FOMC members deliberate and vote, benchmarked against a Monte Carlo Bayesian voting model. Backtest over 215 (or 218, by draft) meetings; within 25bp in 93% of meetings per one abstract.

**Collodel (2025/2026), "Interpreting the Interpreter: Can We Model post-ECB Conferences Volatility with LLM Agents?"** — [V] — Proximity 3
- Summary: arXiv 2508.13635; Central Bank of Malta WP 4/26 (12 June 2026). Thirty synthetic traders with heterogeneous risk preferences and biases read ECB press conference transcripts and forecast euro swap rates; simulated disagreement correlates with realized OIS volatility.
- Why it matters: synthetic-audience reading of central bank communication, market side.

**Hansen and Kazinnik (2023), "Can ChatGPT Decipher Fedspeak?"** — [V-partial] — Proximity 2
- Summary: GPT models classify the stance of FOMC statement sentences better than BERT and dictionaries. LLM as reader/classifier, not as respondent. Venue details not confirmed beyond Richmond Fed / SSRN 4399406.

#### 1C. Foundations of the "silicon sample" approach

**Horton, Filippas and Manning (2023), "Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?"** — [V] — Proximity 3. NBER WP 31122. LLMs as implicit computational models of humans; replicates Charness-Rabin, Kahneman-Knetsch-Thaler and Samuelson-Zeckhauser experiments qualitatively.

**Argyle, Busby, Fulda, Gubler, Rytting and Wingate (2023), "Out of One, Many: Using Language Models to Simulate Human Samples"** — [V] — Proximity 3. Introduces "algorithmic fidelity" and "silicon samples": GPT-3 conditioned on sociodemographic backstories from US surveys.

**Aher, Arriaga and Kalai (2023), "Using Large Language Models to Simulate Multiple Humans and Replicate Human Subject Studies"** — [V] — Proximity 2. ICML 2023, PMLR 202:337-371. "Turing Experiments"; documents a "hyper-accuracy distortion".

**Brand, Israeli and Ngwe (2023), "Using LLMs for Market Research"** — [V] — Proximity 3. HBS WP 23-062, SSRN 4395751 (revised April 2026). WTP from LLM conjoint responses is sometimes close to human estimates but often inaccurate and occasionally wrong-signed. The marketing precursor to SSR.

**Park, Zou, Shaw, Hill, Cai, Morris, Willer, Liang and Bernstein (2024), "Generative Agent Simulations of 1,000 People"** — [V] — Proximity 3. arXiv 2411.10109. Interview-based agents for 1,052 people replicate General Social Survey answers 85% as accurately as participants replicate themselves two weeks later. The source of the test-retest-normalized metric that SSR also uses.

**Hewitt, Ashokkumar, Ghezae and Willer (2024), "Predicting Results of Social Science Experiments Using Large Language Models"** — [V-partial] — Proximity 4. Working paper. GPT-4 simulated responses predict treatment effects across 70 pre-registered US survey experiments (r = 0.85), and r = 0.90 for unpublished studies that could not be in training data; effect sizes systematically overestimated. Counts of effects and participants differ across listings. Journal venue not confirmed.

---

### Theme 2 — Look-ahead bias, temporal leakage, memorization

**Ludwig, Mullainathan and Rambachan (2025), "Large Language Models: An Applied Econometric Framework"** — [V] — Proximity 4 (methods)
- NBER WP 33344; arXiv 2412.07031. For prediction problems, valid conclusions require "no training leakage" between the LLM's training data and the researcher's sample; for estimation problems, a human-labelled validation sample is required, without which model and prompt choices produce very different estimates. The core econometric reference for the post-cutoff design.

**Lopez-Lira, Tang and Zhu (2025), "The Memorization Problem: Can We Trust LLMs' Economic Forecasts?"** — [V] — Proximity 4
- arXiv 2504.14765; SSRN 5217505. LLMs can recall exact values of key economic variables before their knowledge cutoff; no recall after the cutoff; evidence of memorization is only a lower bound; instructing the model to ignore later information is not a reliable fix. Supports validating only on post-cutoff waves.

**Sarkar and Vafa (2024), "Lookahead Bias in Pretrained Language Models"** — [V-partial] — Proximity 3
- Direct tests for lookahead bias (earnings-call risk factors, election winners from biographies); discusses limits of prompting-based fixes. Source of StoriesLM. Venue/SSRN id not confirmed (an ICML 2025 listing appeared in results).

**Glasserman and Lin (2023), "Assessing Look-Ahead Bias in Stock Return Predictions Generated By GPT Sentiment Analysis"** — [V-partial] — Proximity 3
- arXiv 2309.17322. Anonymizing company identifiers; finds a "distraction effect" that can outweigh look-ahead bias in-sample. First names not confirmed in snippets.

**He, Lv, Manela and Wu (2025), "Chronologically Consistent Large Language Models"** — [V-partial] — Proximity 3
- arXiv 2502.21206. ChronoBERT / ChronoGPT trained only on text available at each date, annual vintages 1999-2024. In a return-forecasting test, lookahead bias appears modest but is model- and application-specific. One snippet listed a fifth author (Liu); check the author list.

**Kelly, Malamud, Schwab and Xu (2026), "Scaling Point-in-Time Language Models: Economic Evaluation of Embeddings"** — [V] — Proximity 3
- NBER WP 35247; arXiv 2607.11889; NeurIPS 2026 poster. Decoder models up to 4B parameters on chronologically filtered web text with monthly checkpoints 2013-2024, pipeline released. Relevant twice: as point-in-time generators, and because SSR also needs an **embedding model**, which is a second leakage channel.

**Gao, Jiang and Yan (2025/2026), "A Test of Lookahead Bias in LLM Forecasts" / "Detecting Lookahead Bias in LLM Forecasts"** — [V] — Proximity 3
- arXiv 2512.23847. "Lookahead Propensity" measure; positive correlation with forecast accuracy signals bias.

**Benhenda (2026), "Look-Ahead-Bench"** — [V-partial] — Proximity 2. arXiv 2601.13770. Benchmark for look-ahead bias in point-in-time LLMs for finance. Exact full title and first name not confirmed.

**Drinkall et al. (2024), "Time Machine GPT"; Yan and Tang (2026), "DatedGPT"** — [U] — Proximity 2. Known only through a citation inside another paper's snippet.

**"Summoning the Oracle to Slay It: Mitigating Look-Ahead Bias in Financial Backtesting with Large Language Models" (2026)** — [V-partial] — Proximity 2. arXiv 2605.24564. Inference-time decoding correction. Authors not retrieved.

Cross-references from Theme 1 that belong here as evidence: Bybee (post-training sample check), Alam et al. (true out-of-sample forecasts stale), Anesti et al. (cutoff used as a design feature), Hewitt et al. (unpublished studies).

---

### Theme 3 — Methodological critiques of silicon samples

**Bisbee, Clinton, Dorff, Kenkel and Larson (2024), "Synthetic Replacements for Human Survey Data? The Perils of Large Language Models"** — [V] — Proximity 4
- *Political Analysis* 32, 401-416, DOI 10.1017/pan.2024.5. ChatGPT 3.5 personas from ANES respondents: means close to human averages, but less variation, 48% of regression coefficients significantly different from ANES counterparts, and sensitivity to prompt wording and timing. The standard citation for reduced variance and non-reproducibility.

**Dominguez-Olmedo, Hardt and Mendler-Dünner (2024), "Questioning the Survey Responses of Large Language Models"** — [V] — Proximity 4
- NeurIPS 2024 (oral). On the American Community Survey, model answers are driven by option ordering and labelling biases; after randomizing order, responses tend to uniform. A critique of closed-form option elicitation, which is exactly what SSR's free-text step sidesteps; 3-5 option macro questions are the exposed case.

**Santurkar, Durmus, Ladhak, Lee, Liang and Hashimoto (2023), "Whose Opinions Do Language Models Reflect?"** — [V] — Proximity 3
- ICML 2023, PMLR 202:29971-30004. OpinionQA across 60 US demographic groups; substantial misalignment persists after demographic steering.

**Gui and Toubia (2023/2025), "The Challenge of Using LLMs to Simulate Human Behavior: A Causal Inference Perspective"** — [V] — Proximity 4
- arXiv 2312.15524. Varying a treatment in the prompt shifts unspecified context, violating unconfoundedness (implausibly flat demand curves). Directly relevant to in-silico information-provision RCTs.

**Wang, Morgenstern and Dickerson (2024/2025), "Large language models that replace human participants can harmfully misportray and flatten identity groups"** — [V-partial] — Proximity 3
- arXiv 2402.01908. Identity prompts misportray and flatten subgroup heterogeneity. Publication in *Nature Machine Intelligence* **not confirmed** by search.

**Krsteski, Russo, Chang, West and Gligorić (2025/2026), "Valid Survey Simulations with Limited Human Data: The Roles of Prompting, Fine-Tuning, and Rectification"** — [V] — Proximity 3
- arXiv 2510.11408; ACL 2026. Combining synthesis with rectification (debiasing estimates using human responses). A constructive route if raw synthetic shares are biased.

**Lukauskas and Šarkauskaitė (2026), "Plausible but Not Valid: A Psychometric Audit of LLMs as Synthetic Survey Respondents"** — [V-partial] — Proximity 3
- arXiv 2608.14606. LLMs reproduce the direction of psychometric relationships but statistical baselines without a language model match or beat them; synthetic respondents compress the scale. Authors from a secondary bibliography only.

**Taday Morocho et al. (2026), "Assessing the Reliability of Persona-Conditioned LLMs as Synthetic Survey Respondents"** — [V-partial] — Proximity 3
- arXiv 2602.18462; WWW Companion '26. World Values Survey; demographic conditioning can redistribute error and undermine subgroup fidelity. Full author list not retrieved.

Additional 2026 arXiv titles surfaced but **not characterized** (titles only; treat as leads, [U]): "Marginal Fidelity Does Not Establish User Simulation in Demographic Synthetic Survey Panels" (2609.07305); "Beyond Averages: Evaluating LLMs on Human Survey Replication at the Distributional Level" (2606.09013); "When Synthetic Users Fail: A Cross-Domain Benchmark" (2607.26348); "Item-Mean Surrogates" (2608.29455); "Validating LLM-Generated Synthetic Survey Samples" (2611.00256); "Do LLMs Reproduce the Age Gap in Loneliness? Evaluating Survey Simulation against European Survey Data" (2610.25158). One search summary mentioned a Prolific preprint reporting that persona-level simulation tripled distributional error relative to asking for the aggregate distribution; I could not locate that paper and it is **unverified**.

Critiques internal to the macro papers themselves: Iadisernia and Camassa (personas add nothing; homogeneous forecasts); Lin, Sun and Yan (more homogeneous than humans); Graham, Harvey and Jha (about 25% under-dispersion); Anesti, Hill and Joseph (no consistent model of inflation); Hewitt et al. (effect sizes overestimated); Alam et al. (stale out-of-sample).

**Dillion, Tandon, Gu and Gray (2023), "Can AI language models replace human participants?"** (*Trends in Cognitive Sciences*) — [U] — Proximity 2. Not searched this session.

---

### Theme 4 — Human-side benchmarks

#### 4A. Household inflation expectation formation

**Malmendier and Nagel (2016), "Learning from Inflation Experiences"** — [V] — Proximity 2. *QJE* 131(1), 53-87, DOI 10.1093/qje/qjv037. Individuals overweight inflation experienced in their lifetimes; Michigan Survey microdata. Provides the cohort gradient a synthetic panel should reproduce.

**D'Acunto, Malmendier, Ospina and Weber (2021), "Exposure to Grocery Prices and Inflation Expectations"** — [V] — Proximity 2. *JPE* 129(5), 1615-1639. Expectations respond to prices of goods households actually buy, weighted by purchase frequency. Pairs with the Bank of England finding of food-price sensitivity in GPT.

**Cavallo, Cruces and Perez-Truglia (2017), "Inflation Expectations, Learning, and Supermarket Prices: Evidence from Survey Experiments"** — [V] — Proximity 2. *AEJ: Macroeconomics* 9(3), 1-35, DOI 10.1257/mac.20150147. Weaker priors in low-inflation contexts; reliance on memories of supermarket prices.

**Armantier, Nelson, Topa, van der Klaauw and Zafar (2016), "The Price Is Right: Updating Inflation Expectations in a Randomized Price Information Experiment"** — [V-partial] — Proximity 2. Title and year confirmed; *Review of Economics and Statistics* 98(3), 503-523 is from an ambiguous listing. Check.

**Coibion, Gorodnichenko and Weber (2022), "Monetary Policy Communications and Their Effects on Household Inflation Expectations"** — [V] — Proximity 3. *JPE* 130(6), 1537-1584, DOI 10.1086/718982. RCT on about 20,000 Nielsen Homescan individuals with eight information treatments; the FOMC statement moves expectations about as much as simply stating the inflation target; news coverage about half as much. The canonical target for in-silico replication.

**Weber, Candia, Afrouzi, Ropele, Lluberas, Frache, Meyer, Kumar, Gorodnichenko, Georgarakos, Coibion, Kenny and Ponce (2025), "Tell Me Something I Don't Already Know: Learning in Low- and High-Inflation Settings"** — [V] — Proximity 3. *Econometrica* 93(1), 229-264, DOI 10.3982/ECTA22764. Treatment effects of information shrink as inflation rises (endogenous attention). State-dependence is a demanding test for synthetic respondents and the benchmark Wu, Xi and Xie replicate.

**Haaland, Roth and Wohlfart (2023), "Designing Information Provision Experiments"** — [V] — Proximity 3 (methods). *JEL* 61(1), 3-40, DOI 10.1257/jel.20211658.

**Coibion, Georgarakos, Gorodnichenko and Weber, "Forward Guidance and Household Expectations"** — [V-partial] — Proximity 2. NBER WP 26778 (2020) confirmed; *JEEA* 2023 publication **not confirmed**.

**Arioli, Bates, Dieden, Duca, Friz, Gayer, Kenny, Meyler and Pavlova (2017), "EU consumers' quantitative inflation perceptions and expectations: an evaluation"** — [V] — Proximity 3. ECB Occasional Paper 186. Evaluates the EC consumer survey's inflation questions; quantitative estimates exceed HICP over 2004-2015. Core data-source reference for the EC survey.

**Carlson and Parkin (1975), "Inflation Expectations"** — [V] — Proximity 2. *Economica* 42, 123-138. Quantification of qualitative response shares; the tradition that makes 3-5 option response shares (balance statistics) an object of study in their own right.

Not searched this session, listed as leads only ([U]): Carroll (2003, *QJE*) on epidemiological expectations; Coibion and Gorodnichenko (2015, *AER*) on information rigidity; Bachmann, Berg and Sims (2015, *AEJ: Economic Policy*) on inflation expectations and readiness to spend (directly relevant to the "major purchases" question); D'Acunto, Malmendier and Weber's handbook chapter "What Do the Data Tell Us About Inflation Expectations?"; Andre, Pizzinelli, Roth and Wohlfart (2022, *REStud*) on subjective models of the macroeconomy; survey documentation for the NY Fed SCE (Armantier et al. 2017) and ECB CES (Georgarakos and Kenny 2022). A new item surfaced incidentally: Wohlfart (2026), "Do People Have Economic Expectations?", ECONtribute DP 402 [V-partial], on respondents who form expectations from scratch when asked; relevant to what a survey answer measures.

#### 4B. Central bank communication with the public

**Haldane and McMahon (2018), "Central Bank Communications and the General Public"** — [V] — Proximity 3. *AEA Papers and Proceedings* 108, 578-583, DOI 10.1257/pandp.20181082.

**Bholat, Broughton, Ter Meer and Walczak (2019), "Enhancing central bank communications using simple and relatable information"** — [V] — Proximity 3. *JME* 108, 1-15, DOI 10.1016/j.jmoneco.2019.08.007. Online experiment on a representative UK sample comparing the Monetary Policy Summary with a "Relatable Summary"; improved comprehension, modest trust gains. A natural human benchmark for communication pre-testing.

**Blinder, Ehrmann, de Haan and Jansen (2024), "Central Bank Communication with the General Public: Promise or False Hope?"** — [V] — Proximity 3. *JEL* 62(2), 425-457, DOI 10.1257/jel.20231683.

**Haldane, Macaulay and McMahon (2020), "The 3 E's of central bank communication with the public"** — [V-partial] — Proximity 2. Bank of England working paper (2020) confirmed by title; author list from memory.

---

### Theme 5 — SSR itself: follow-ups, critiques, applications outside marketing

**Maier et al. (2025), "LLMs Reproduce Human Purchase Intent via Semantic Similarity Elicitation of Likert Ratings"** — [V-partial] — Proximity 4 (source method)
- arXiv 2510.08338 (v1 9 Oct 2025; v3 27 Oct 2025). Benjamin F. Maier and eight co-authors, PyMC Labs and Colgate-Palmolive; Aslak and Fiaschi appear as second and third authors in one snippet; **full author list not retrieved**.
- Result per snippets: 57 personal-care product surveys, 9,300 US respondents; GPT-4o and Gemini-2.0-flash; SSR with GPT-4o reaches 90.2% correlation attainment relative to test-retest reliability and mean KS similarity 0.88. Authors note dependence on the embedding model, similarity measure and anchor statements. Reference implementation: `pymc-labs/semantic-similarity-rating` (Apache 2.0, per a secondary source).
- No peer-reviewed version found.

**Vera Pichardo (2026), "Measuring Self-Rating Bias in LLM-Generated Survey Data: A Semantic Similarity Framework for Independent Scale Mapping"** — [V] — Proximity 4
- arXiv 2602.13862. Calibrates and validates SSR as a measurement channel independent of the generating model. Pre-registered circularity experiment (N=345): LLM self-rating has 4x compressed error variance (0.21 vs 0.87 for SSR) and directional bias. SSR achieves 65-77% exact match and 91-100% within one point across two embedding providers on 69 test cases in 8 domains (satisfaction, likelihood, agreement items among them). The only methodological follow-up found; single author, not peer reviewed.

**"LLMs as survey respondents: Comparison to simple semantic baselines" (2026)** — [V-partial] — Proximity 4
- arXiv 2610.29645. Short paper; LLMs do not always beat embedding-similarity baselines that involve no generation step. **Authors not retrieved**; the model names in the snippet looked fragmentary and should be checked against the PDF. A snippet from this paper credits "Argyle et al. (2024)" with showing that embedding similarity can map LLM text to Likert distributions; I could not identify that reference and it may be a mis-citation of Maier et al. **Unverified.**
- Why it matters: implies a required baseline for your paper (embedding-only prediction without a persona-conditioned LLM).

**Applications outside marketing.** One arXiv paper on simulated lawmaker agents (title containing "Large Language Models and Augmented Democracy", arXiv 2610.04412) reportedly converts agent reactions to 1-5 ratings with SSR using the original hyperparameters — [V-partial], attribution of this description to that arXiv id is from a search summary and not confirmed. A PyMC Labs blog post evaluates synthetic consumers on General Social Survey political and lifestyle questions (grey literature; smaller models fall below a naive baseline).

**Not found:** any independent replication of the SSR headline numbers; any application of SSR or embedding-based Likert mapping to inflation expectations, consumer confidence, or any macroeconomic survey.

---

## 2. Frontier map

### What has been done

| Paper | Population / survey | Model(s) | Elicitation | Validation target | Temporal design |
|---|---|---|---|---|---|
| Zarifhonarvar (JME) | US households / NY Fed SCE | GPT-4 Turbo; later proprietary + open-source | Numeric expectations; info treatments | SCE moments; human RCT effects | Not established |
| Anesti, Hill, Joseph (BoE SWP 1190) | UK households / BoE Inflation Attitudes Survey | GPT-3.5 Turbo | Synthetic survey replica | Aggregate survey results, subgroup patterns | Uses Sept 2021 cutoff for out-of-time test (extent not established) |
| Wu, Xi, Xie (NBER 34308) | US households / multi-wave RCT | Not established | Survey + elicited reasoning | Central tendencies, treatment effects | Retrospective, back to 1990 |
| Lin, Sun, Yan (arXiv) | US households + experts / 3 survey experiments, Michigan | LLM agents with modules | Numeric expectations | Experiment results; 2025 MSC | Forward pre-estimation of 2025 MSC |
| HouseholdBench (NBER 35927) | 6 US household surveys, 32 tasks | 13 LLMs | Numeric, categorical, probabilistic prediction | Individual outcomes vs GBT | Not established |
| Tariff multi-agent (arXiv 2608.30522) | 300 Michigan households | LLM agents | Multi-month simulation | Not established | Not established |
| Utama et al. (BIS conf.) | Indonesian households (no survey) | GPT, Gemini | Numeric; info treatments | None (no human survey) | n/a |
| Hansen et al. | US SPF | Not established | Numeric forecasts, 23 variables | SPF accuracy, dispersion, revisions | 1999-2023 with real-time data |
| Iadisernia, Camassa (Banca d'Italia) | ECB SPF | GPT-4o | Numeric forecasts | SPF panel | 2013-2025 |
| Bybee | SPF, AAII, CFO | GPT-3.5-class | Expectations from WSJ text | Survey series | Includes post-training articles |
| Graham, Harvey, Jha | Duke-Fed CFO Survey | Not established | Optimism score (0-100) | Matched individual CFO answers | 2002-2025 |
| Faria-e-Castro, Leibovici; Alam et al. | None (model as forecaster) | PaLM; several | Numeric forecast | Realized inflation, SPF | In-sample; pseudo vs true out-of-sample |
| Maier et al. (SSR) | US consumers / 57 product surveys | GPT-4o, Gemini-2.0-flash | **Free text mapped to Likert via embeddings** | Response distributions, product ranking | Not a concern in their setting |

### Patterns

1. **Geography.** Household work is concentrated on the US (SCE, Michigan) with one UK paper. Nothing found on the EC Business and Consumer Survey, the ECB CES, or any multi-country household panel. Euro-area work exists only for professionals (ECB SPF) and market participants.
2. **Outcome type.** Almost everything targets numeric point expectations or forecasts. The qualitative 3-5 option questions and their published response shares or balances are not a target in any macro paper found (HouseholdBench includes categorical tasks, at the individual level).
3. **Elicitation.** Direct numeric or closed-form elicitation throughout. No macro paper uses free-text elicitation with embedding-based mapping.
4. **Temporal validity.** Mostly retrospective. Exceptions are partial: Bybee's post-training check, the Bank of England's use of the 2021 cutoff, Lin et al.'s 2025 MSC pre-estimation, Hewitt et al.'s unpublished studies. No paper found is organized around strictly post-cutoff validation as its primary design, and Alam et al. show true out-of-sample LLM macro forecasts deteriorate.
5. **Recurring weakness.** Under-dispersion and homogeneity are reported in nearly every paper that checks, and personas were found to add nothing for professional forecasters.
6. **Second-step ideas are already occupied.** In-silico information-provision RCTs: Zarifhonarvar; Wu, Xi and Xie; Lin, Sun and Yan; Utama et al. Communication pre-testing on synthetic households: Zarifhonarvar; Kazinnik; the tariff multi-agent paper; Utama et al.

### Has anyone already applied SSR-style free-text-to-Likert elicitation to macro expectation surveys with post-cutoff validation?

**Not that I could find.** Targeted searches combining "semantic similarity rating" with inflation expectations, consumer expectations and macroeconomic surveys returned only the original SSR paper, the Vera Pichardo calibration paper, and the semantic-baselines paper. No macro paper found uses SSR or any embedding-based Likert mapping. Separately, no paper found validates synthetic household panels against published qualitative response shares, and none uses the EC consumer survey.

Limits on that answer: it rests on search snippets, not full texts; coverage of SSRN and of conference programmes (ECB, BIS, Fed 2026 events on AI and forecasting) is partial; the field is moving monthly (at least five relevant papers appeared between June and October 2026). The individual components do exist separately: household survey simulation (several), cutoff-aware evaluation (Bank of England, Lin et al.), SSR (marketing). The open space is the combination, and it could close quickly. HouseholdBench and the Bank of England paper are the two most likely to contain overlapping elements that snippets did not reveal; read both in full before committing.

---

## 3. Positioning recommendation

### The gap

A cross-country (euro area / EU) synthetic household panel for the **qualitative** questions of harmonised consumer surveys, elicited by **free text and mapped by SSR**, and validated **only on survey waves after the generating model's training cutoff** against published response shares. Each of the three elements differentiates from a specific competitor:

- Qualitative response shares and distributional fit (versus numeric means in Zarifhonarvar; Wu, Xi and Xie; Lin, Sun and Yan). This also answers the Cleveland Fed discussant critique that validation has covered central tendencies only.
- SSR elicitation as a response to the documented under-dispersion and option-order artefacts (Bisbee et al.; Dominguez-Olmedo et al.; Graham et al.), tested head-to-head against direct option elicitation.
- Post-cutoff validation as the design principle, grounded in Ludwig, Mullainathan and Rambachan and Lopez-Lira, Tang and Zhu (versus retrospective designs, especially Wu, Xi and Xie).

### The five closest competitors

1. **Anesti, Hill and Joseph (2026, Bank of England SWP 1190)** — household survey replica with a cutoff-based out-of-time test; UK only, GPT-3.5, direct elicitation.
2. **Zarifhonarvar (JME)** — SCE personas, information treatments, communication pre-testing pitch; US, numeric.
3. **Wu, Xi and Xie (2025, NBER 34308)** — LLM survey framework replicating a multi-wave inflation RCT; retrospective.
4. **Lin, Sun and Yan (2025, arXiv 2505.17648)** — agent framework with forward pre-estimation of the 2025 Michigan survey; numeric.
5. **Huang et al. (2026, HouseholdBench, NBER 35927)** — benchmark across six US household surveys including categorical and expectations tasks; individual-level.

Next tier: Iadisernia and Camassa (ECB SPF, personas add nothing); Hansen et al. (SPF); Graham, Harvey and Jha (CFO survey); Alam et al. (out-of-sample staleness).

### Suggested contribution statement (draft for the Writer)

"We test whether LLM-based synthetic respondents can reproduce the distribution of answers to the qualitative questions of harmonised household expectation surveys across countries and demographic groups. Unlike existing work, which elicits numeric expectations and evaluates largely within the model's training window, we elicit free-text answers, map them to response categories by semantic similarity, and evaluate exclusively on survey waves fielded after the model's training cutoff."

### Points the Strategist should know from the literature (reported, not recommended)

- Baselines that existing papers use and referees will expect: no-change / last-wave shares (HouseholdBench), gradient-boosted trees on demographics (HouseholdBench), no-persona prompts (Iadisernia and Camassa), direct option elicitation (Maier et al.), embedding-only similarity without generation (arXiv 2610.29645).
- The no-change baseline is demanding for monthly response shares, which are highly persistent; Alam et al.'s "stale" finding suggests an LLM without fresh information will resemble a no-change forecast. Existing papers handle this by feeding real-time information into the prompt (Hansen et al.; Graham et al.), which changes what is being tested.
- SSR introduces a second model (the embedder) with its own training cutoff, and anchor statements chosen by the researcher (Maier et al. flag sensitivity to both).
- The first-paper gap appears open; the second-step ideas are not, and would need a distinct angle (euro area, qualitative outcomes, state-dependence as in Weber et al. 2025, or the Gui-Toubia confounding critique).

### Candidate outlets seen in this literature

JME (Zarifhonarvar; Bholat et al.), Management Science (Kazinnik), central bank working paper series (BoE, FRBSF, St. Louis, Banca d'Italia authors, Malta), NBER, ICAIF. No top-5 general-interest publication of an LLM-synthetic-survey macro paper was found.

---

## 4. Could not verify (consolidated)

- Zarifhonarvar: JME volume 157 / article 103859 and publication year come from secondary citations; publisher page not retrieved.
- Maier et al.: full author list; all numbers are from abstract-level snippets.
- Authors of arXiv 2608.30522 (tariff multi-agent), 2610.29645 (semantic baselines), 2605.24564 (FINCAD), 2610.04412 (lawmaker agents).
- Whether Zarifhonarvar, Hansen et al., Wu-Xi-Xie, HouseholdBench or Graham et al. include any post-cutoff evaluation, and how extensive the Bank of England's is.
- Which six surveys HouseholdBench covers.
- Wang, Morgenstern and Dickerson in *Nature Machine Intelligence*; Coibion et al. "Forward Guidance" in *JEEA*; Armantier et al. *REStat* volume and pages; Sarkar and Vafa venue; He et al. author list (four or five authors); Hewitt et al. final venue and counts.
- "Argyle et al. (2024)" as an embedding-to-Likert precursor; the Prolific preprint on persona-level error. Neither located.
- No ECB, Bundesbank, BIS working-paper-series, or Federal Reserve Board paper on LLM synthetic households was found. This is absence of search hits, not evidence of absence. (The BIS-hosted Indonesia paper is a conference paper; Banca d'Italia authors appear via arXiv/ICAIF, not the Bank's own series.)
- Items tagged [U] in Themes 2-4 were not searched.

---

## 5. BibTeX

Entries are for copying into the project bibliography later; `Bibliography_base.bib` was not modified. Lines beginning `% UNVERIFIED` name what is unconfirmed.

```bibtex
%% ---------- Theme 1: LLM respondents for economic expectations ----------

% UNVERIFIED: volume/article number from secondary citations; publisher page not retrieved; year may be 2025 or 2026
@article{zarifhonarvar_generating,
  author  = {Zarifhonarvar, Ali},
  title   = {Generating Inflation Expectations with Large Language Models},
  journal = {Journal of Monetary Economics},
  volume  = {157},
  pages   = {103859},
  year    = {2026},
  note    = {Earlier versions titled ``Experimental Evidence on Large Language Models'' and ``Evidence on Inflation Expectations Formation Using Large Language Models''; SSRN 4825076}
}

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
  note   = {arXiv:2505.17648. Earlier title: ``Simulating Macroeconomic Expectations in Survey Experiments with LLM-based Economic Agents''}
}

@techreport{huang_etal_householdbench_2026,
  author      = {Huang, Jin and Ferreras Garrucho, Diego and Xie, Yutong and Yuan, Walter M. and Mei, Qiaozhu and Lian, Chen and Hazell, Jonathon},
  title       = {{HouseholdBench}: Evaluating Large Language Models as Predictors of Household Economic Behavior},
  institution = {National Bureau of Economic Research},
  type        = {Working Paper},
  number      = {35927},
  year        = {2026},
  note        = {arXiv:2610.07563}
}

% UNVERIFIED: affiliations, conference name, results; known from BIS-hosted PDF listing only
@unpublished{utama_andina_oktavia_2026,
  author = {Utama, Ginanjar and Andina, Neva and Oktavia, Dina},
  title  = {Effects of Information Treatments on Household Inflation Expectations in {Indonesia}: A Generative {AI} Experiment},
  year   = {2026},
  note   = {Conference paper hosted at bis.org/events/accconf2026/Paper\_1\_ID\_251216.pdf}
}

% UNVERIFIED: authors not retrieved; details from aggregator pages only
@unpublished{tariff_multiagent_2026,
  author = {{Authors not verified}},
  title  = {Tariff Threats, Macroeconomic Expectations, and Policy Communication Strategies: Experiments Based on a Multi-Agent System},
  year   = {2026},
  note   = {arXiv:2608.30522}
}

@unpublished{graham_harvey_jha_2026,
  author = {Graham, John R. and Harvey, Campbell R. and Jha, Manish},
  title  = {{CFOs} Meet {LLMs}},
  year   = {2026},
  note   = {arXiv:2606.13812}
}

% UNVERIFIED: volume/issue/pages not retrieved (DOI listing confirmed)
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

@unpublished{kazinnik_sinclair_fomc,
  author = {Kazinnik, Sophia and Sinclair, Tara M.},
  title  = {{FOMC} In Silico: A Multi-Agent System for Monetary Policy Decision Modeling},
  year   = {2025},
  note   = {GWU working paper 2025-005. % UNVERIFIED: second author's first name and middle initial}
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

@inproceedings{aher_arriaga_kalai_2023,
  author    = {Aher, Gati and Arriaga, Rosa I. and Kalai, Adam Tauman},
  title     = {Using Large Language Models to Simulate Multiple Humans and Replicate Human Subject Studies},
  booktitle = {Proceedings of the 40th International Conference on Machine Learning},
  series    = {PMLR},
  volume    = {202},
  pages     = {337--371},
  year      = {2023},
  note      = {% UNVERIFIED: authors' first names}
}

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

% UNVERIFIED: first names, final venue, and effect/participant counts (differ across listings)
@unpublished{hewitt_etal_2024,
  author = {Hewitt, Luke and Ashokkumar, Ashwini and Ghezae, Isaias and Willer, Robb},
  title  = {Predicting Results of Social Science Experiments Using Large Language Models},
  year   = {2024},
  note   = {Working paper}
}

%% ---------- Theme 2: Look-ahead, leakage, memorization ----------

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

% UNVERIFIED: venue and year (cited as 2024 elsewhere; an ICML 2025 listing appeared)
@unpublished{sarkar_vafa_2024,
  author = {Sarkar, Suproteem K. and Vafa, Keyon},
  title  = {Lookahead Bias in Pretrained Language Models},
  year   = {2024}
}

% UNVERIFIED: authors' first names
@unpublished{glasserman_lin_2023,
  author = {Glasserman, Paul and Lin, Caden},
  title  = {Assessing Look-Ahead Bias in Stock Return Predictions Generated By {GPT} Sentiment Analysis},
  year   = {2023},
  note   = {arXiv:2309.17322}
}

% UNVERIFIED: author list (one source lists a fifth author, Liu)
@unpublished{he_etal_chrono_2025,
  author = {He, Songrun and Lv, Linying and Manela, Asaf and Wu, Jimmy},
  title  = {Chronologically Consistent Large Language Models},
  year   = {2025},
  note   = {arXiv:2502.21206}
}

% UNVERIFIED: authors' first names
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

% UNVERIFIED: known only via citation in another paper's snippet
@unpublished{drinkall_etal_2024,
  author = {Drinkall, {} and others},
  title  = {Time Machine {GPT}},
  year   = {2024}
}

%% ---------- Theme 3: Critiques of silicon samples ----------

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

@inproceedings{santurkar_etal_2023,
  author    = {Santurkar, Shibani and Durmus, Esin and Ladhak, Faisal and Lee, Cinoo and Liang, Percy and Hashimoto, Tatsunori},
  title     = {Whose Opinions Do Language Models Reflect?},
  booktitle = {Proceedings of the 40th International Conference on Machine Learning},
  series    = {PMLR},
  volume    = {202},
  pages     = {29971--30004},
  year      = {2023},
  note      = {% UNVERIFIED: authors' first names}
}

@unpublished{gui_toubia_2023,
  author = {Gui, George and Toubia, Olivier},
  title  = {The Challenge of Using {LLMs} to Simulate Human Behavior: A Causal Inference Perspective},
  year   = {2023},
  note   = {arXiv:2312.15524}
}

% UNVERIFIED: journal publication (Nature Machine Intelligence) not confirmed; arXiv version confirmed
@unpublished{wang_morgenstern_dickerson_2024,
  author = {Wang, Angelina and Morgenstern, Jamie and Dickerson, John P.},
  title  = {Large Language Models That Replace Human Participants Can Harmfully Misportray and Flatten Identity Groups},
  year   = {2024},
  note   = {arXiv:2402.01908}
}

@inproceedings{krsteski_etal_2026,
  author    = {Krsteski, Stefan and Russo, Giuseppe and Chang, Serina and West, Robert and Gligori{\'c}, Kristina},
  title     = {Valid Survey Simulations with Limited Human Data: The Roles of Prompting, Fine-Tuning, and Rectification},
  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics (ACL)},
  year      = {2026},
  note      = {arXiv:2510.11408}
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

% UNVERIFIED: not searched this session; all fields from memory
@article{dillion_etal_2023,
  author  = {Dillion, Danica and Tandon, Niket and Gu, Yuling and Gray, Kurt},
  title   = {Can {AI} Language Models Replace Human Participants?},
  journal = {Trends in Cognitive Sciences},
  year    = {2023}
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

% UNVERIFIED: journal publication (JEEA 2023) not confirmed; NBER WP confirmed
@techreport{coibion_etal_forwardguidance_2020,
  author      = {Coibion, Olivier and Georgarakos, Dimitris and Gorodnichenko, Yuriy and Weber, Michael},
  title       = {Forward Guidance and Household Expectations},
  institution = {National Bureau of Economic Research},
  type        = {Working Paper},
  number      = {26778},
  year        = {2020}
}

@techreport{arioli_etal_2017,
  author      = {Arioli, Rodolfo and Bates, Colm and Dieden, Heinz and Duca, Ioana and Friz, Roberta and Gayer, Christian and Kenny, Geoff and Meyler, Aidan and Pavlova, Iskra},
  title       = {{EU} Consumers' Quantitative Inflation Perceptions and Expectations: An Evaluation},
  institution = {European Central Bank},
  type        = {Occasional Paper},
  number      = {186},
  year        = {2017}
}

@article{carlson_parkin_1975,
  author  = {Carlson, John A. and Parkin, Michael},
  title   = {Inflation Expectations},
  journal = {Economica},
  volume  = {42},
  pages   = {123--138},
  year    = {1975}
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

%% ---------- Theme 5: SSR and follow-ups ----------

% UNVERIFIED: full author list (nine authors; Maier first, Aslak and Fiaschi among them)
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

% UNVERIFIED: authors not retrieved
@unpublished{semantic_baselines_2026,
  author = {{Authors not verified}},
  title  = {{LLMs} as Survey Respondents: Comparison to Simple Semantic Baselines},
  year   = {2026},
  note   = {arXiv:2610.29645}
}
```

Several BibTeX author first names above (Aher, Santurkar, Hewitt, Glasserman/Lin, Kelly et al., Brand et al.) were filled from memory or left blank because snippets gave surnames only; they are flagged inline and must be checked before the entries are moved into the project bibliography.

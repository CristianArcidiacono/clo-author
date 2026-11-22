# Data Exploration: Human Benchmarks for LLM Synthetic Macro Survey Panels

**Date:** 2026-11-22
**Agent:** explorer (Discovery phase)
**Research idea:** Transfer Semantic Similarity Rating (SSR; Maier et al. 2025, arXiv 2510.08338) to qualitative household expectation questions; validate synthetic country x demographic x month panels against human answer-option shares on post-training-cutoff waves.
**Status:** Awaiting explorer-critic review. No score is given here.

---

## 0. How to read this report (evidence labels)

Network access in this session was restricted: `WebFetch` failed for every host tried (economy-finance.ec.europa.eu, data.sca.isr.umich.edu, www.newyorkfed.org, www.ecb.europa.eu, db.nomics.world, stat.ee). Nothing below was read from a primary document in full. Every claim carries one of three labels:

| Label | Meaning |
|-------|---------|
| **[S]** | Supported by a web-search result snippet from the cited source in this session. Still second-hand: the search tool summarised the page, I did not read it. |
| **[M]** | From my own memory of the source. Plausible, not checked this session. **All question wordings marked [M] must be replaced by verbatim text from the official questionnaire before any prompt or anchor statement is written.** |
| **[U]** | UNVERIFIED: I could not establish this either way. Treat as an open question. |

To close most of the [M]/[U] items, the hosts listed above need to be allowed in the session's network settings, or the researcher can open the linked documents manually.

---

## 1. Ranked table

| Rank | Source | Grade | Answer shares public? | Demographic cells in public data | Freq. / lag | 2025-26 waves available now? | Role |
|------|--------|-------|----------------------|----------------------------------|-------------|------------------------------|------|
| 1 | European Commission harmonised consumer survey (DG ECFIN BCS) | **A** for country totals; **B** for demographic cells until verified | Yes for totals: a "Detailed data by answer category (totals)" file exists [S] | Balances by income quartile, age, education, sex, occupation in a "Categories" file [S]; shares x demographics [U] | Monthly; published end of the reference month [M] | Yes, through Oct/Nov 2026 [M] | Primary benchmark |
| 2 | NY Fed Survey of Consumer Expectations (SCE) | **A-** (public microdata, 9-month lag) | Yes, any tabulation from microdata | Any (age, income, education, region, gender, numeracy) | Monthly; microdata lag 9 months [S] | 2025 complete, roughly to Feb 2026 [inferred from lag] | Secondary: 5-point Likert items, panel reliability |
| 3 | ECB Consumer Expectations Survey (CES) | **A-/B** (public-use microdata, quarterly release, lag [U]) | Yes from microdata; portal aggregates are net percentages [S] | Any available in the public-use file (country, age band, gender, education, income) [M] | Monthly; microdata released quarterly [S] | Likely well into 2026; exact last wave [U] | Secondary: euro-area microdata, cross-check on EC results |
| 4 | Univ. of Michigan Surveys of Consumers | **B** | Yes in public tables (response percentages per question) [M]; microdata via archive [S] | Tables: limited cuts [U]; microdata: any | Monthly; prelim mid-month, final end-month; microdata lag [U] | Tables yes; microdata 2025 reported available by a third party [S], 2026 [U] | US timely aggregate benchmark; 6-month re-interview |
| 5 | Bank of England Inflation Attitudes Survey | **B** | Yes; respondent-level xlsx files are published [S] | Any from individual responses (age, gender, region, work status; income [U]) | Quarterly; released about 4-6 weeks after fieldwork [M] | Yes through Aug 2026 [S] | UK benchmark; but provider break Aug 2026 |
| 6 | Japan Cabinet Office Consumer Confidence Survey | **B** | Yes; monthly report includes a table of response-category shares [S] | By household attributes on e-Stat [U] | Monthly; about 2-4 weeks [M] | Yes through at least Sep 2026 [S] | Non-Western benchmark; language caveat |
| 7 | Bank of Japan Opinion Survey | **B-** | Yes; full distributions in PDF and CSV [S] | Limited [U] | Quarterly; about 5 weeks [S] | Yes through Sep 2026 survey [S] | Supplementary |
| 8 | Bundesbank Online Panel Households (BOP-HH) | **C+** | From SUF microdata after application | Any | Monthly; SUF release lag [U]; latest SUF found: 202502, waves 1-63 [S] | Post-early-2025 waves [U] | RCT benchmarks and panel reliability, not timeliness |
| 9 | Bank of Canada CSCE | **C** | Aggregates only; microdata access [U] | Published data by age, geography, income, education [S] | Quarterly; about 2-3 weeks [S] | Yes through Q3 2026 [S] | Low priority: mostly quantitative items |
| 10 | Info-provision RCT replication packages | **B/C** (varies) | Microdata where public | Varies | One-off | n/a (pre-cutoff by construction) | In-silico treatment-effect benchmark only |

Grades are my feasibility assessment under the A-D rubric, not a quality score.

---

## 2. Per-source detail

### 2.1 European Commission harmonised consumer survey (Joint Harmonised EU Programme of Business and Consumer Surveys)

**Coverage.** Monthly. EU-27 plus candidate countries (Montenegro, North Macedonia, Albania, Serbia, Türkiye) [M]; UK dropped after 2020 [M]. Series back to 1985 for older members [M]. Results for month t are published at the end of month t with a flash consumer confidence figure about a week earlier [M], so there is effectively no publication lag. 2025-2026 waves are in the standard files [M]; a March 2026 reading is cited in press coverage found this session [S].

**Sample size.** Nominal EU-wide monthly consumer sample about 33,000 according to the Commission's overview page [S]; other official pages give 24,000 (ECB summary) and "almost 40,000" (2010 Commission document) [S], so use the per-country metadata sheets rather than any total. Per-country example: Luxembourg contacts 2,376 units and gets 504 replies per month [S]. Large countries are roughly 1,500-2,000 completed interviews per month [M]. For a 6-option question, n = 1,000 gives a standard error of at most 1.6 pp per share, n = 500 at most 2.2 pp (before design effects); demographic cells within a country will be several times noisier. Per-country metadata: "Metadata of partner institutes" page on the DG ECFIN BCS site [S].

**Question wording.** Official source: BCS User Guide (January 2023 update), section 3.1 "Consumer survey - questionnaire", from about p. 39 [S]: https://economy-finance.ec.europa.eu/system/files/2023-02/bcs_user_guide.pdf . National institutes field translated versions; the English master text is a reference wording, not what a German or Italian respondent actually saw. Translated national questionnaires must be collected per country (example located: Statistics Estonia consumer survey form, https://stat.ee/sites/default/files/2026-04/1514%20Consumer%20survey.pdf [S]).

Wording below is [M] unless marked. Q5 and Q6 options were corroborated by a search snippet of a Commission Summer 2022 forecast box and the Estonian form [S], but not read verbatim.

| Q | Wording [M] | Options [M] |
|---|-------------|-------------|
| Q1 | How has the financial situation of your household changed over the last 12 months? It has... | got a lot better / got a little better / stayed the same / got a little worse / got a lot worse / don't know |
| Q2 | How do you expect the financial position of your household to change over the next 12 months? It will... | get a lot better / get a little better / stay the same / get a little worse / get a lot worse / don't know |
| Q3 | How do you think the general economic situation in this country has changed over the past 12 months? | same 5-point + don't know |
| Q4 | How do you expect the general economic situation in this country to develop over the next 12 months? | same 5-point + don't know |
| Q5 | How do you think that consumer prices have developed over the last 12 months? They have... [S for stem] | risen a lot / risen moderately / risen slightly / stayed about the same / fallen / don't know [S] |
| Q6 | By comparison with the past 12 months, how do you expect that consumer prices will develop in the next 12 months? They will... | increase more rapidly / increase at the same rate / increase at a slower rate / stay about the same / fall / don't know [S] |
| Q7 | How do you expect the number of people unemployed in this country to change over the next 12 months? The number will... | increase sharply / increase slightly / remain the same / fall slightly / fall sharply / don't know |
| Q8 | In view of the general economic situation, do you think that now it is the right moment for people to make major purchases such as furniture, electrical/electronic devices, etc.? | yes, it is the right moment now / it is neither the right moment nor the wrong moment / no, it is not the right moment now / don't know |
| Q9 | Compared to the past 12 months, do you expect to spend more or less money on major purchases (furniture, electrical/electronic devices, etc.) over the next 12 months? I will spend... | much more / a little more / about the same / a little less / much less / don't know |
| Q10-Q12 | Savings now / likelihood of saving / statement best describing household financial situation | 4-5 options + don't know |

Q5.1 and Q6.1 are follow-up open-ended percentage questions, asked only of those answering codes 1, 2, 3 or 5 [S].

**Fit notes for SSR.** (i) Q5 and Q6 scales are asymmetric (four "rise" gradations, one "fall") and Q6 is phrased relative to the past rate of increase, not as a level; these are not Likert scales in the Maier et al. sense, so anchor statements cannot be a simple agree-disagree ladder. (ii) "Don't know" is a published category and is non-trivial for some questions; the design must decide whether the synthetic panel can produce it. (iii) Q8 has only 3 substantive options; Q1-Q4, Q7, Q9 are symmetric 5-point scales and are the cleanest SSR targets.

**Answer shares vs balances.** The Commission's time-series download page lists, for consumers: "Seasonally Adjusted Data (total sector)", "Non-Seasonally Adjusted Data (total sector)", "Categories", and "Qualitative and Quantitative Inflation perceptions" ZIPs, plus a separate section "Detailed data by answer category (totals)" [S]. A Commission methodological note refers to "CONS categories and detailed data by answer category" as distinct disaggregate products [S]. So full answer-option shares exist publicly for country totals. Balance definition: B = (PP + 0.5 P) - (0.5 M + MM) [S].
- Whether the "Categories" file carries answer shares or only balances for the demographic categories: **[U]**. The wording "detailed data by answer category (totals)" suggests shares are published for totals only, which would mean demographic cells are available only as balances. This is the single most important item to verify.
- Internal series codes (CONS.cc.TOT.q.PP.M etc.) are [M] and were not confirmed.

**Demographic breakdowns.** Respondents are categorised by five criteria: income, occupation, education, age, sex [S]. ECB Data Portal mirrors confirm the cells: age A1-A4 (A3 = 50-64, A4 = 65+ [S]; A1 = 16-29, A2 = 30-49 [M]), income quartiles R1-R4 [S], education E1-E3 [S], sex SM/SF [S], total TT. No sub-national region in the Commission files [M]. Cells are one-way margins only (no age x income crossing) [M].

**Access.** Free download, no registration [M]: https://economy-finance.ec.europa.eu/economic-forecast-and-surveys/business-and-consumer-surveys/download-business-and-consumer-survey-data/time-series_en . Reuse under the Commission's general reuse policy (CC BY 4.0) [M]. Mirrors: ECB Data Portal datasets ECS and SUR (SUR is API-only [S]; these mirror balances and the quantitative-inflation quartiles, not obviously answer shares), DBnomics provider EC. Microdata are held by national institutes and are not distributed by the Commission [M].

**Known issues.**
- Spain: disaggregate series (categories and answer-category data) show a break in May 2025 [S]. This sits exactly in the validation window.
- Survey mode and institute changes create breaks in several countries (documented in the metadata sheets and the methodology notes page) [M].
- Mode differs across countries (CATI, web, mixed) [M], which affects "don't know" shares and comparability.
- Seasonally adjusted balances are revised; answer-category data are NSA [M], which is what the validation needs anyway.

**Who used it.** Commission forecast boxes on inflation perceptions (Summer 2022, Summer 2023) [S]; ECB Economic Bulletin boxes; the Carlson-Parkin quantification literature [M].

---

### 2.2 NY Fed Survey of Consumer Expectations (SCE)

**Coverage.** US; monthly since June 2013 [M]; internet rotating panel of about 1,300 household heads, each staying up to 12 months [S, from a 2017 NY Fed presentation; current size [U]].

**Access and lag.** Public microdata download from the NY Fed Center for Microeconomic Data "Data Bank" (https://www.newyorkfed.org/microeconomics/databank.html [M for exact URL]); questionnaires posted on the same page [S]. Core SCE and Credit Access microdata are posted with a nine-month lag; Household Spending, Public Policy, Housing and Labor Market modules with an eighteen-month lag [S, NY Fed SCE FAQ]. As of November 2026 the core microdata should therefore run to about February 2026. Terms of use on the download page [U]. Free.

**Wording [M, verify against posted questionnaire].**
- Q1: "Do you think you (and any family members living with you) are financially better or worse off these days than you were 12 months ago?" Much worse off / Somewhat worse off / About the same / Somewhat better off / Much better off.
- Q2: same, "12 months from now".
- Credit access, backward and forward: "...generally harder or easier these days for people to obtain credit or loans..." Much harder / Somewhat harder / Equally easy or hard / Somewhat easier / Much easier.
- Inflation: binary "inflation or deflation" followed by a point forecast and a bin-probability density; not a Likert item.
- A search snippet attributed the 5-point better/worse wording to the Fed Board's SHED rather than the SCE; I could not retrieve the SCE text itself, so treat the wording above as unconfirmed.

**Shares.** Monthly releases report shares better/worse off [S]. The downloadable chart data include response shares for the qualitative items [M]; demographic cuts in chart data (age under 40 / 40-60 / over 60; education; income under 50k / 50-100k / over 100k; region) exist for headline series [M], for qualitative shares [U]. From microdata any cell can be built.

**Known issues.** 9-month lag (acceptable for 2025 waves, not for near-real-time tracking); panel conditioning (expectations and uncertainty fall with tenure) [M]; household heads only; n per month small for fine cells (1,300 total implies demographic cells of 100-400).

**Who used it for similar questions.** Several LLM-persona papers already draw personas or benchmarks from SCE microdata: Wu, Xi and Xie (2025), Zarifhonarvar (job-market paper) and at least one critical benchmark paper [S]. Novelty relative to these needs to be established by the librarian.

---

### 2.3 ECB Consumer Expectations Survey (CES)

**Coverage.** Monthly online panel since January 2020; initially BE, DE, ES, FR, IT, NL; extended in 2022 to IE, GR, AT, PT, FI (11 countries) [S]. Target about 19,000 respondents per wave [S]. Fieldwork by Ipsos [S]. Any further country expansion [U]. Panel tenure rules [U].

**Access and lag.** Public-use microdata files on the CES web page [S]; published on a quarterly schedule since November 2022 [S]; must be cited as "ECB Consumer Expectations Survey" [S]. Whether registration is required, and the exact lag of the latest file: [U]. Aggregate results appear monthly in the last 10 days of the month on the ECB site and Data Portal [S], but qualitative items are reported there as net percentages [S], not full shares. Portal: https://www.ecb.europa.eu/stats/ecb_surveys/consumer_exp_survey/html/data_methodological.en.html . Contact: ECB-CES@ecb.europa.eu [S].

**Documentation.** Microdata guide, 2025 version 5 [S]: https://www.ecb.europa.eu/stats/ecb_surveys/consumer_exp_survey/shared/pdf/ecb.CES_microdata_guide.en.pdf ; sample questionnaire: .../shared/pdf/CES_sample_questionnaire.en.pdf [S]; aggregate statistics guide and methodological guide on the same path [S].

**Qualitative items.** C1010 is listed as a qualitative up/down/same item and C1110 as "Expectation for prices in general next 12 months" (qualitative), with C1120 the open-ended version [S; the mapping of C1010 to perception vs expectation was garbled in the snippet]. Answer scale: increased a lot / increased a little / stayed exactly the same / decreased a little / decreased a lot [M], a symmetric 5-point scale and a much better SSR target than EC Q5/Q6. Other qualitative items on household finances, credit access and the economy exist [M]; exact list [U].

**Known issues.** Online panel with conditioning; some variables coarsened or omitted in the public-use file for disclosure control [M]; aggregates under 50 observations are flagged unreliable in ECB's own tables [S]; questionnaire is fielded in national languages.

---

### 2.4 University of Michigan Surveys of Consumers

**Coverage.** US; monthly since 1978 (quarterly earlier). Mode changed from RDD cell-phone to web with address-based sampling, phased in April-July 2024; all interviews online from July 2024 [S]. Sample rose from about 600 phone interviews to 900-1,000 web interviews per month [S]. Estimated mode effect on the sentiment index: -6.6 points (Michigan) to -8.9 points (Cummings and Tedeschi) [S]. The validation window (2025+) is entirely web mode, which is convenient; any pre-2024 comparison is not.

**Wording [M unless noted; verify against the questionnaire on data.sca.isr.umich.edu "Survey Information"; web-mode wording may differ slightly from the phone script].**
- PAGO: "We are interested in how people are getting along financially these days. Would you say that you (and your family living there) are better off or worse off financially than you were a year ago?" Better / Same / Worse / DK [S for the substance].
- PEXP: "Now looking ahead--do you think that a year from now you (and your family living there) will be better off financially, or worse off, or just about the same as now?" [S, verbatim in snippet].
- BUS12: "Now turning to business conditions in the country as a whole--do you think that during the next twelve months we'll have good times financially, or bad times, or what?"
- DUR: "About the big things people buy for their homes--such as furniture, a refrigerator, stove, television, and things like that. Generally speaking, do you think now is a good or bad time for people to buy major household items?" Good / Pro-con / Bad / DK.
- PX1Q1: "During the next 12 months, do you think that prices in general will go up, or go down, or stay where they are now?" followed by the percentage follow-up.
- UNEMP, RATEX: more/same/less unemployment; interest rates up/same/down.
Most items are 3-option; fewer scale points than SSR's 5-point setting.

**Shares and breakdowns.** Public tables at https://data.sca.isr.umich.edu/tables.php give response percentages per question with monthly/quarterly/yearly views; e.g. Table 35 "Buying Conditions for Large Household Durables" [S]. Demographic cuts in the standard tables: [U] (index-level cuts by age/income/education/region exist [M]; share-level cuts probably require microdata). Microdata: Cross-Section Archive / SDA at https://data.sca.isr.umich.edu/sda.php with customised subset download; some years only via ICPSR [S]. Household and adult weights included [S].

**Lag.** Preliminary release mid-month, final end of month. A search snippet states the public site posts the newest data after a four-week embargo [S; scope of that embargo unclear]. Microdata lag: [U]. A third-party blog reports individual-level files covering 1978-2025 [S], implying 2025 microdata are obtainable; 2026 [U].

**Access.** Public; site data, tables and charts usable without permission [S]. Free registration may be needed for the archive [U].

**Re-interview design.** Historically a rotating panel: each monthly cross-section is re-interviewed six months later [S, 2005 ICPSR documentation]. Post-transition web design reportedly targets a 125 fresh / 90 recontact split per week [S, secondary wiki copy of the technical report]. A 2026 arXiv paper (HouseholdBench) links respondents to an earlier interview six, seven or eight months before [S], which indicates panel linkage keys are still in the public microdata.

**Who used it.** At least one arXiv paper simulates Michigan-survey households with LLM agents and tests out-of-sample on 2025 data; HouseholdBench uses the microdata as an LLM prediction benchmark [S].

---

### 2.5 Bank of England Inflation Attitudes Survey

**Coverage.** UK; quarterly (Feb, May, Aug, Nov) since 1999/2001 [M]; adults 16-75; online omnibus since 2020, about 2,000-2,200 per wave [S]; face-to-face before May 2020 [S].

**Provider break.** Ipsos ran the survey through May 2026; Savanta took over from August 2026 after re-tendering. A parallel run in May 2026 produced medians of 3.6/3.1/3.3% (Savanta) against 4.0/3.5/3.9% (Ipsos) for 1/2/5-year expectations, and the Bank warns against comparing May and August headline results [S]. Any validation spanning mid-2026 needs a break dummy or must use the parallel-run wave.

**Shares and microdata.** Question-by-question results in each release; "Individual survey responses" xlsx files (46-49 MB) are listed for 2026 [S]; the Stata version was discontinued in 2023 [S]. Pages: https://www.bankofengland.co.uk/inflation-attitudes-survey/2026/august-2026 and https://www.bankofengland.co.uk/statistics/research-datasets . Demographics in the individual file: age band, gender, region, working status (quota variables [S]); income, tenure, education [M/U].

**Wording [M].** Q1 perceived price change over the last 12 months and Q2a expected over the next 12 months use binned numeric options (gone down / not changed / up by 1% or less / ... / up by 5% or more / no idea), i.e. ordered bins rather than verbal Likert. Qualitative items: interest rates over the past 12 months (risen a lot / risen a little / stayed about the same / fallen a little / fallen a lot / no idea) and expected over the next 12 months [S for existence]; "if prices started to rise faster... would Britain's economy end up stronger, weaker, or make little difference"; satisfaction with the Bank (very satisfied to very dissatisfied). "Don't know / No idea" has been on the showcard since August 2020 [S]. Official questionnaire: release tables and "Methodology and notes" PDF (https://www.bankofengland.co.uk/-/media/boe/files/inflation-attitudes-survey/methodology-and-notes.pdf) [S].

**Access.** Public download. The methodology note says no publication of findings "without the advance approval of Ipsos" [S]; whether that clause binds academic reuse of the published individual-response file is [U] and should be checked.

**Who used it.** Bank of England working paper "Inflation attitudes of large language models" (2026; arXiv 2512.14306) compares GPT output with IAS data using IAS demographics [S]. Direct overlap with this project on UK data.

---

### 2.6 Japan: Cabinet Office Consumer Confidence Survey

**Coverage.** Monthly; 8,400 sampled households (5,376 two-or-more-person, 3,024 single-person); 15-month rotating panel with about 560 households rotating monthly; about 6,700 valid responses (79.7% in September 2026) [S]. Mail survey since 2013 [S]; online response option [M].

**Shares.** Monthly report (e.g. https://www.esri.cao.go.jp/jp/stat/shouhi/honbun202609.pdf) includes a reference table of response-category shares (raw) and a price-outlook section [S]. Items: overall livelihood, income growth, employment, willingness to buy durable goods; 5 options from "will improve" to "will get worse" [M]; price outlook one year ahead in binned ranges plus "don't know" [M]. Share expecting prices to rise: 93.6% in April 2026 [S].

**Breakdowns.** Tables by household attribute (age and income of head, household type) on e-Stat, statistics code 00100405 (https://www.e-stat.go.jp/en/statistics/00100405) [U for the exact cuts and whether shares or only indices are cut]. Some items are Japanese-only [S].

**Access.** Public, free; government open-data terms [M]. Microdata: not public; older waves may be in the SSJDA archive (University of Tokyo) [S for the archive listing, U for coverage].

**Fit.** Largest per-wave sample of any single-country source here, prompt release, clean 5-point scales. Questionnaire is Japanese; the LLM should be prompted in Japanese with the official 調査票 wording, which I did not locate.

### 2.7 Japan: Bank of Japan Opinion Survey on the General Public's Views and Behavior

Quarterly (Mar, Jun, Sep, Dec); individuals aged 20+; stratified two-stage random sample, mail with mail/online return [S]; 4,000 sampled [S, undated press article], about half respond [M]. June 2026 survey fielded 7 May-9 June, published 16 July 2026 [S]; a results file dated October 2026 exists [S]. Full distributions in PDF plus CSV (https://www.boj.or.jp/en/research/o_survey/index.htm) [S]. Scales are 5-point: e.g. present price levels "have gone up significantly" 68.5% in June 2026; outlook "will go up significantly" 40.5%, "will go up slightly" 49.9% [S]. Demographic breakdowns [U]. Official English translations are published, which helps. Free.

---

### 2.8 Bundesbank Online Panel Households (BOP-HH)

Monthly since April 2020 (pilots April-June 2019); 2,500-5,000 individuals per wave aged 16+, with a panel component; fieldwork by forsa from the forsa.omninet panel [S]. Scientific use file by application to the RDSC (informal email to fdsz-data@bundesbank.de, then application form) [S]; free for non-commercial research [M]. Latest SUF located: version 202502 with waves 1-63, DOI 10.12757/bbk.bophh.202502.01 [S]; any later release and the standing release lag [U]. Portal: https://www.bundesbank.de/en/bundesbank/research/rdsc/research-data/bop-hh-757542 .

Qualitative core block [M]: expected development over the next twelve months of the inflation rate, rents, lending and savings rates, property prices, unemployment, economic growth, fuel prices, on a 5-point scale (decrease significantly / decrease slightly / stay roughly the same / increase slightly / increase significantly). Wording was not confirmed this session. Questionnaires per wave are published on the Bundesbank site in German and English [M].

Value for this project: (i) clean 5-point qualitative block for Germany, comparable with EC and CES Germany; (ii) many embedded information-provision experiments submitted by external researchers [S for the external-question mechanism]; (iii) panel for stability measures. Weakness: application step and uncertain timeliness for post-cutoff waves. The Bundesbank also publishes monthly aggregate results from the survey on its website [M]; whether these include qualitative shares is [U].

### 2.9 Bank of Canada Canadian Survey of Consumer Expectations (CSCE)

Quarterly since 2014 Q4 [M]; internet rotating panel of about 2,000 household heads [S]. Published survey data page with aggregate tables; data also by age, geography, income and education [S]: https://www.bankofcanada.ca/publications/canadian-survey-of-consumer-expectations/canadian-survey-of-consumer-expectations-survey-data/ . Latest: Q3 2026, released 19 October 2026 [S]. Modelled on the NY Fed SCE, so the core is quantitative (point and density forecasts) [M]; few 3-5 option items. Public microdata: [U], probably not available. Low priority.

---

### 2.10 (a) Information-provision RCTs for in-silico treatment-effect benchmarks

| Study | Data location | Status |
|-------|---------------|--------|
| Haldane and McMahon (2018, AEA P&P), "Central Bank Communications and the General Public" | openICPSR project 114474 [S] | Public deposit confirmed to exist; contents not inspected |
| Coibion, Gorodnichenko and Weber (2022, JPE 130(6)), "Monetary Policy Communications and Their Effects on Household Inflation Expectations" | Nielsen Homescan panel, about 20,000 individuals [S] | Replication package location [U]; underlying Nielsen/Kilts data are licence-restricted [M] |
| Weber et al. (2025, Econometrica 93(1), 229-264), "Tell Me Something I Don't Already Know" | Econometric Society supplement exists (DOI 10.3982/ECTA22764) [S] | Data availability [U]. Already replicated in silico by Wu, Xi and Xie (2025) [S] |
| Weber, D'Acunto, Gorodnichenko and Coibion (2022, JEP), "Subjective Inflation Expectations of Households and Firms" | openICPSR project 169781 [S] | Survey article package, not an RCT |
| Cavallo, Cruces and Perez-Truglia (2017, AEJ Macro) | AEA/openICPSR [M] | [U] |
| Roth and Wohlfart (2020, REStat) | Harvard Dataverse [M] | [U] |
| Armantier, Nelson, Topa, van der Klaauw and Zafar (2016, REStat), "The Price Is Right" | RAND American Life Panel [M] | [U] |
| Coibion, Georgarakos, Gorodnichenko and van Rooij (2023, AEJ Macro) | Dutch CentERpanel (DNB Household Survey) [M] | [U] |
| Bholat, Broughton, Ter Meer and Walczak (2019, JME); "Data for: Central bank communication with the general public: Promise or false hope?" (Princeton DSS catalog entry) | Catalog entry found [S] | [U] |
| Experiments embedded in BOP-HH and ECB CES | Inside the respective microdata (treatment-arm variables) [M] | Depends on 2.3 / 2.8 access |

Caveat for the validation design: all of these were fielded before current LLM training cutoffs, and the papers themselves are in training data. They can benchmark whether in-silico treatment effects have the right sign and magnitude, but not out-of-sample.

### 2.11 (b) Panels for a human reliability ceiling

None of these is a true test-retest (same question, short interval, nothing changed). Re-interview gaps are one to six months, during which real conditions and beliefs change, so the within-person agreement they give is a lower bound on reliability, and the corresponding "ceiling" on achievable LLM-human agreement is conservative.

| Panel | Re-interview gap | Public linkage | Notes |
|-------|------------------|----------------|-------|
| NY Fed SCE | 1 month, up to 12 waves | Yes, respondent ID in public microdata [M] | Shortest gap among US sources; best candidate |
| ECB CES | 1 month | Yes in public-use file [M] | Large n; 11 countries |
| BOP-HH | 1 month or longer (panel component) [S] | In SUF | Application needed |
| Michigan | about 6 months (6-8 in recent data) [S] | Yes [S, via HouseholdBench description] | Long gap; mode change in 2024 |
| Japan CCS | 1 month, 15 waves [S] | No public microdata [U] | Not usable without restricted access |

For repeated cross-sections (EC, IAS, BoJ) the only ceiling available is sampling noise from n per cell, plus month-to-month autocorrelation of the shares.

---

## 3. Recommendation for the validation design

**Primary benchmark: European Commission harmonised consumer survey.** It is the only source that delivers the target structure (country x month, about 30 countries, identical questionnaire) with full answer-option shares for totals, published in the reference month, free and without registration. It keeps arriving every month, so post-cutoff waves accumulate automatically for any model. Its weaknesses are specific and checkable: demographic cells may be balances only, Q5/Q6 scales are asymmetric, wording is fielded in national languages, and Spain has a break in May 2025.

**Secondary 1: NY Fed SCE microdata.** True 5-point Likert items on household finances and credit, respondent-level data so any demographic cell and joint distribution can be built, and a monthly panel for the reliability lower bound. The 9-month lag means only waves up to about February 2026 are usable today, which is still post-cutoff for many models.

**Secondary 2: ECB CES public-use microdata.** Symmetric 5-point qualitative price items for 11 euro-area countries that overlap the EC survey, giving (i) respondent-level demographic cells where the EC files may only have balances and (ii) a second, independent human measurement of the same populations, which helps separate LLM error from survey-house effects.

**Useful add-ons, not core:** Michigan public tables for a timely US aggregate series; Japan Cabinet Office CCS for a large-sample non-Western check; Haldane-McMahon and BOP-HH/CES embedded experiments for treatment-effect benchmarks.

**Deprioritise:** BoC CSCE (quantitative, no confirmed microdata); BoE IAS as a core series because of the August 2026 provider break, though its public respondent-level file makes it a reasonable UK robustness check on pre-break 2025 waves.

---

## 4. Main data risks

1. **Demographic answer shares in the EC data may not be public.** If the "Categories" file holds balances only, the country x demographic x month validation against full distributions is not possible with EC data alone and shifts to CES/SCE microdata.
2. **Verbatim wording not secured.** No official questionnaire was read this session. All wordings above are from memory or snippets. National-language questionnaires differ from the English master.
3. **Structural breaks inside the validation window.** Spain (EC, May 2025), BoE IAS provider change (August 2026), Michigan web transition (2024, just before the window).
4. **Lags vs training cutoffs.** SCE (9 months) and CES/BOP-HH (quarterly or slower) microdata may leave few post-cutoff waves for the newest models; only EC, Michigan tables, IAS and the Japanese surveys are near-real-time.
5. **No true test-retest benchmark.** Panel re-interviews give only a conservative reliability bound; repeated cross-sections give sampling noise only.
6. **Small cells.** SCE has about 1,300 respondents per month; EC small countries about 500. Fine demographic cells will be dominated by sampling noise.
7. **Crowded field.** Several 2025-2026 papers already benchmark LLM personas against SCE, Michigan and IAS data, including a Bank of England working paper. Not a data problem, but it affects which benchmark adds something new; EC cross-country shares appear unused in what I found (not an exhaustive search).

---

## 5. Open access questions the researcher must resolve

1. EC "Categories" ZIP: does it contain answer-option percentages by income/age/education/sex, or balances only? If balances only, will DG ECFIN supply category-level answer shares on request?
2. EC "Detailed data by answer category (totals)": confirm it covers Q1-Q9 for all countries, is NSA, and includes the "don't know" share; record the series-code convention.
3. Obtain the BCS User Guide section 3.1 and replace every [M] wording in section 2.1; collect national-language questionnaires for the countries to be simulated (partner-institute metadata sheets).
4. Per-country effective sample sizes and survey modes from the partner-institute metadata sheets; note all documented breaks from 2024 onward.
5. NY Fed SCE: confirm the latest microdata month, terms of use, and the exact wording and codes of the qualitative items from the posted questionnaire; confirm current panel size.
6. ECB CES: latest wave in the public-use file and standing lag; registration requirement; which demographics survive disclosure control; verbatim qualitative items and codes from microdata guide v5; panel tenure rule.
7. Michigan: microdata lag and latest month in the Cross-Section Archive; whether tables give share-level demographic cuts; current web-mode question text; panel linkage variable after 2024.
8. BoE IAS: licence terms for the individual-response xlsx (the Ipsos approval clause); variables included; whether the Savanta file keeps the same layout; verbatim questionnaire.
9. Japan CCS: locate the official questionnaire (調査票) and the e-Stat tables by household attribute; confirm whether shares or only indices are cut by attribute.
10. BOP-HH: latest SUF vintage, release lag, application turnaround, and which embedded experiments are included in the SUF.
11. RCT packages: check each deposit for respondent-level treatment arm, pre/post expectations and demographics; confirm whether the Coibion-Gorodnichenko-Weber Nielsen data can be shared at all.
12. Decide the reference LLM(s) and their cutoff dates, since this determines which sources have enough post-cutoff waves.

---

## 6. Sources consulted (search results; none read in full)

- DG ECFIN BCS time-series download page: https://economy-finance.ec.europa.eu/economic-forecast-and-surveys/business-and-consumer-surveys/download-business-and-consumer-survey-data/time-series_en
- BCS User Guide (2023): https://economy-finance.ec.europa.eu/system/files/2023-02/bcs_user_guide.pdf
- BCS methodological concepts: https://economy-finance.ec.europa.eu/economic-forecast-and-surveys/business-and-consumer-surveys/overarching-methodological-concepts_en
- Eurostat BCS metadata: https://ec.europa.eu/eurostat/cache/metadata/en/ei_bcs_esms.htm
- Commission Summer 2022 forecast thematic box: https://ec.europa.eu/economy_finance/forecasts/2022/summer/ip183_en_thematic_box_2.pdf
- Luxembourg consumer metadata sheet: https://ec.europa.eu/economy_finance/db_indicators/surveys/documents/metadata/metadata_lu_cons_en.pdf
- Statistics Estonia consumer survey form: https://stat.ee/sites/default/files/2026-04/1514%20Consumer%20survey.pdf
- ECB Data Portal ECS / SUR: https://data.ecb.europa.eu/data/datasets/ECS/data-information , https://data.ecb.europa.eu/data/datasets/SUR/structure
- NY Fed SCE FAQ: https://www.newyorkfed.org/microeconomics/sce/sce-faq ; overview article: https://www.newyorkfed.org/research/epr/2017/epr_2017_overview-of-sce_armantier
- ECB CES data and methodology: https://www.ecb.europa.eu/stats/ecb_surveys/consumer_exp_survey/html/data_methodological.en.html ; microdata guide: https://www.ecb.europa.eu/stats/ecb_surveys/consumer_exp_survey/shared/pdf/ecb.CES_microdata_guide.en.pdf ; sample questionnaire: https://www.ecb.europa.eu/stats/ecb_surveys/consumer_exp_survey/shared/pdf/CES_sample_questionnaire.en.pdf
- Michigan: https://data.sca.isr.umich.edu/tables.php , https://data.sca.isr.umich.edu/sda.php , https://data.sca.isr.umich.edu/faq.php , https://www.sca.isr.umich.edu/files/methodtransitionannouncement2024.pdf , https://news.umich.edu/u-m-consumer-sentiment-surveys-remain-robust-measurement-of-economic-behavior
- Bank of England IAS: https://www.bankofengland.co.uk/inflation-attitudes-survey/2026/august-2026 , https://www.bankofengland.co.uk/inflation-attitudes-survey/2026/may-2026 , https://www.bankofengland.co.uk/statistics/research-datasets , https://www.bankofengland.co.uk/-/media/boe/files/inflation-attitudes-survey/methodology-and-notes.pdf
- Bundesbank BOP-HH: https://www.bundesbank.de/en/bundesbank/research/rdsc/research-data/bop-hh-757542 ; SUF record: https://doi.org/10.12757/bbk.bophh.202502.01
- Bank of Canada CSCE: https://www.bankofcanada.ca/publications/canadian-survey-of-consumer-expectations/
- Japan Cabinet Office CCS: https://www.esri.cao.go.jp/en/stat/shouhi/shouhi-e.html , https://www.esri.cao.go.jp/jp/stat/shouhi/honbun202609.pdf , https://www.e-stat.go.jp/en/statistics/00100405
- Bank of Japan Opinion Survey: https://www.boj.or.jp/en/research/o_survey/index.htm , https://www.boj.or.jp/en/research/o_survey/ishiki2607.htm
- Haldane-McMahon replication data: https://www.openicpsr.org/openicpsr/project/114474/version/V1/view
- Weber et al. (2025): https://www.econometricsociety.org/doi/10.3982/ECTA22764
- Coibion-Gorodnichenko-Weber: https://www.nber.org/papers/w25482
- Related LLM-survey papers: https://arxiv.org/pdf/2505.17648v3 , https://arxiv.org/pdf/2512.14306 , https://arxiv.org/pdf/2610.07563

# Course 01: What is Data Science?

> Sub-course 01 of 12 in the IBM Data Science Professional Certificate
> 4 modules (3 + 1 optional) · 45 lectures · ~12 hours
> Source transcripts: `notes/transcripts/01-what-is-data-science/` (local, gitignored)

## TL;DR
Foundational survey of the field. Covers: what data science *is* and isn't, what data scientists actually do day-to-day, the **5 Vs of Big Data**, cloud computing fundamentals and the Hadoop/HDFS/Hive/Spark stack, the **AI taxonomy** (AI ⊃ ML ⊃ DL, with GenAI alongside), real applications across business and life-saving domains, careers + recruiting realities, and the data ecosystem (structured/semi/unstructured, RDBMS vs NoSQL, warehouses/marts/lakes, ETL, pipelines). Lots of definitions, not much math. The course's recurring theme is **curiosity + storytelling beat raw technical skill**.

## Module 1: Defining Data Science + What Data Scientists Do

### What is data science? ([[data-science]])

> "The art of uncovering the insights and trends hiding behind data."
> "Data science is the study of data. Like biological sciences is a study of biology."

It is a **process, not an event**: clarify a question, gather data, analyse, find patterns, tell a story.

| Old world | Data-science world |
|---|---|
| Lack of data | Data deluge (~2.5 quintillion bytes/day globally) |
| Expensive proprietary software | Open source: Python, R, Hadoop, Spark |
| Limited compute, sampling required | Cheap distributed compute, work on the whole population |
| Hypothesis-test on a sample | Find patterns in the full data, generate hypotheses |

### The DS process (5 steps) ([[ds-process]])
1. **Clarify** the business question
2. **Acquire** data (structured + unstructured)
3. **Analyse** using multiple models to reveal patterns, archetypes, outliers
4. **Verify** insight against the business context
5. **Communicate** via storytelling + visualisation

### What makes a great data scientist ([[ds-traits]])

| Trait | Why it matters |
|---|---|
| **Curiosity** | Drives what questions to ask of the data |
| **Argumentation** | Lets you take a position, then update it as data shows otherwise |
| **Judgement** | Tells you where to start when everything looks like signal |
| **Storytelling** | Without it, findings stay buried and unactioned |
| **Computational thinking** | Not "be a programmer day 1", but think in algorithms |
| **Domain expertise** | A retail DS will struggle in IT/health data and vice versa |

> Curiosity is the single most-cited trait across every guest expert. Expect a quiz question on it.

### The many paths in
Backgrounds quoted: statistics, math, business, civil/transportation engineering, mechanical engineering, physics, economics, computer applications/IS, even singer-turned-doctor. "Data science" as a term only stabilised around **2009-2011** (Patil, Gelman). Before that, it was statistics + business analytics.

### What data scientists actually do (vignettes)

| Person | Story | Lesson |
|---|---|---|
| Dr. Murtaza Haider | Toronto Transit Commission had ~500k complaints. He couldn't find a pattern until he stepped in a puddle: complaints spiked on days with unexpected rain/snow/wind | Real-world variables (weather) explain noisy systems |
| Norman White (NYU Stern) | Algae bloom prediction with artificial neural networks to help water-treatment companies | Cross-domain ML for environment |
| Anonymous "recommendation engine" builder | Simple solution beat the complex one across all stakeholder layers | Don't overengineer |

### Common file formats DS work with ([[file-formats]])

| Format | Use | Notes |
|---|---|---|
| **Delimited text (CSV / TSV)** | Standard tabular interchange | Simple schema; first row = header; TSV when commas appear inside fields |
| **XLSX** | Excel spreadsheets | XML-based; multi-sheet workbooks; cannot save malicious code |
| **XML** | Web data exchange | Self-descriptive, custom tags, platform-independent |
| **JSON** | API + web data | Lightweight, language-agnostic; human + machine readable; default for RESTful APIs |
| **PDF** | Final-form documents | Same view everywhere; legal/financial use; can fill forms |

### Regression intuition (the taxi-fare analogy) ([[regression]])
- Base fare ($2.50 when you sit down): the **intercept / constant**
- Per-meter charge: relationship between **distance** and fare
- Per-minute (stuck in traffic): relationship between **time** and fare
- Regression backs out the unknown constant and the two coefficients from observed (distance, time, fare) tuples

### Algorithms practitioners actually like
- **Regression** as the gateway concept
- **k-nearest neighbour**: simple, often beats overblown algos, less likely to overfit
- **Decision trees, naive Bayes, Bayesian analysis**: classic predictive analytics
- **Artificial neural networks**: where deep learning starts
- **Data visualisation in R**

## Module 2: Data Science Topics

### Lesson 2.1: Big Data + Data Mining

### Digital transformation
Driven primarily by data science, especially big data. Org-wide change involving the CEO + CIO + emerging **Chief Data Officer**.

| Org | Pre-transformation | Post-transformation |
|---|---|---|
| Netflix | Postal DVD rental | World's foremost streamer; predicts hit shows before filming |
| Houston Rockets | Traditional NBA team | Video-tracking analytics: 2-pt dunks + 3-pt shots beat mid-range 2-pt → most three-pointers made in NBA history (2017-18 season) |
| Lufthansa | Standard service | Customer-data analytics drives service improvements |

### The 5 Vs of Big Data ([[5-vs-of-big-data]])

| V | Definition | Example given |
|---|---|---|
| **Volume** | Scale of the data | ~2.5 quintillion bytes/day = ~10M Blu-rays |
| **Velocity** | Speed of accumulation | Hours of YouTube footage every 60 seconds |
| **Variety** | Diversity of sources + types | Text, images, video, IoT sensor data |
| **Veracity** | Quality, origin, accuracy, integrity | ~80% of data is unstructured, trust must be established |
| **Value** | Ability to convert data into business / medical / social benefit | The whole point |

### Cloud computing ([[cloud-computing]])

> On-demand delivery of compute resources (network, servers, storage, apps, data centres) over the Internet, pay-for-use.

**5 essential characteristics** (memorise):
1. **On-demand self-service**
2. **Broad network access**
3. **Resource pooling**
4. **Rapid elasticity**
5. **Measured service**

**3 deployment models:** public, private, hybrid
**3 service models:** **IaaS**, **PaaS**, **SaaS** (mapped to the infra / platform / app layers of the stack)

Why cloud is "a godsend" for DS (Haider):
- Bypass local compute + storage limits
- Use advanced algos you don't own
- Multi-region teams collaborate on the same data
- Always-current open-source tooling (Spark, Hadoop, Hive)
- Major providers: IBM Cloud, AWS, Google Cloud Platform. IBM Skills Network labs (Jupyter, Spark) are free for learners.

### Hadoop / big-data processing tools ([[hadoop-stack]])

| Tool | Role |
|---|---|
| **Hadoop** | Java-based, distributed storage + processing of large datasets across clusters of commodity hardware |
| **HDFS** | Hadoop Distributed File System: partitions files across nodes, replicates blocks 3x by default for fault tolerance and **data locality** (compute moves to data) |
| **Hive** | SQL-like data-warehouse layer on top of Hadoop/HBase. Read-based, high latency, good for ETL + reporting, bad for fast-response or transactional workloads |
| **Spark** | General-purpose engine; in-memory processing (spills to disk when constrained); APIs in Java/Scala/Python/R/SQL; standalone or on Hadoop; real-time streaming + ML + ETL |

Origin: Google's PageRank scaling problem (Page + Brin) led to the **MapReduce** paradigm. Doug Cutting cloned it at Yahoo, named it Hadoop. Big-data clusters **scale linearly**: 2x servers → 2x throughput → 2x data handled.

### Data mining: 6-step process ([[data-mining]])
1. **Goal setting**: identify the questions, weigh cost vs benefit
2. **Selecting data sources**
3. **Preprocessing**: flag irrelevant + erroneous data
4. **Transforming**: choose the right storage format
5. **Mining**: pick algorithms + run the analysis
6. **Evaluating**: test predictive power on observed data, share with stakeholders, iterate

### Lesson 2.2: AI + ML + DL + Generative AI

### The AI taxonomy ([[ai-taxonomy]])

```
AI ⊃ ML ⊃ Deep Learning
AI ⊃ Generative AI   (uses deep-learning models under the hood)
```

| Term | Definition | Key point |
|---|---|---|
| **AI** | Computer systems that mimic tasks associated with human intelligence | Umbrella term |
| **ML** | Subset of AI: algorithms that learn from data without being explicitly programmed | Trained on examples, not rules |
| **Deep Learning** | Subset of ML: layered neural networks simulating decision-making | **Gets more efficient as data grows** (other ML often plateaus) |
| **Neural Network** | Collection of small computing units ("neurons") that learn over time | Loosely inspired by biology |
| **Generative AI** | Subset of AI focused on **producing new data**, not just analysing | Examples: GPT (text), VAE/GAN (images, synthetic data) |

### Why deep learning suddenly works
Theory existed 20-30 years ago but was computationally intractable. Multi-layer NNs + cheap GPU compute (each GPU ≈ 600 CPU cores for the linear-algebra ops) made face recognition, speech, image classification possible.

### How DS use these techniques
| Task | Typical approach |
|---|---|
| Recommendation engines (Netflix, Amazon, Spotify) | ML + matrix factorisation, collaborative filtering |
| Fraud detection (real-time credit card) | ML classifier scoring each transaction |
| Image / speech recognition | Deep learning |
| Synthetic data for small / imbalanced datasets | GenAI (GANs, VAEs) |
| Automated insights + reports | LLM + tools like IBM Cognos Analytics |
| Code generation for analytical models | LLMs (GPT, Copilot) |

### Regression in DS
Identifies the strength + size of correlation between one or more inputs and an output. "How much does house price rise per extra sqft + per extra bedroom, and how confident are we?"

## Module 3: Applications + Careers

### Lesson 3.1: Application Domains

### Why companies use DS
Always for the same reason: **discover optimal solutions to existing problems**.

### Get-started checklist (Haider's advice to firms)
1. **Measure first.** "If you can't measure it, you can't improve it."
2. **Capture + archive.** Never overwrite old data; data never gets old.
3. **Garbage in, garbage out**: consistency + documentation matter from day one.
4. Build a **team** of curious people. Don't look for a single unicorn.

### Old problems, new solutions

| Org | Old problem | DS approach |
|---|---|---|
| Uber | Driver-rider matching, dynamic pricing | Real-time data + surge model |
| Toronto Transit Commission | Congestion / streetcar planning | Probe data + complaints analytics. Monthly hours lost to congestion dropped from 4.75 → 3.0 (2010 → mid-2014) |
| US East-Coast research consortium | Toxic cyanobacterial blooms | Robotic boats + buoys + drones + algorithmic prediction models |

### Consumer + business applications
- **Recommendation engines** (Amazon, Netflix, Spotify)
- **Personal assistants** (Siri, Google Assistant)
- **UPS** route guidance (driver + vehicle + customer data) for fuel + time savings
- **Netflix** predicted *House of Cards* success before filming by joining Fincher fans, Wright fans, and UK House of Cards viewer data
- **Wearables** (Fitbit, Apple Watch, Android Watch) stream continuous health data

### Data science saving lives

| Domain | How |
|---|---|
| **Healthcare** | Predictive analytics on gene markers + comorbidities + environment → tailored tests/treatment. Equalises access to latest knowledge across all physicians. Boston Consulting Group + AdvaMedDx cancer study cited: the oncologist's awareness of a diagnostic test was the single biggest factor in whether the patient was offered it |
| **Disaster prep** | Predict earthquakes, hurricanes, tornados, floods, eruptions. University of Warwick: social-media photos + keywords + scientific weather data improve localised flood/hurricane prediction |
| **Electronic Medical Records (EMR)** | NorthShore University HealthSystem (Chicago) was the first US provider awarded top-level EMR deployment for inpatient + outpatient. Anonymised data enables analytics research |

### Deliverables
- Academia: research papers + reports
- Business: analytics-driven decks + reports with tables + plots, evidence-based narratives

### Lesson 3.2: Careers + Recruiting

### Career outlook (numbers cited)
- US Bureau of Labor Statistics: **35% projected growth**
- Median annual salary ~$103,000 (US)
- LinkedIn / Glassdoor / Indeed / Dice: **DS = #1 most-promising job since 2016**, top 3 through 2020
- Global Industry Analysts: data-science platform market growing to ~$314.8B by 2025 at 38.2% CAGR
- McKinsey Global Institute warned of talent shortages by 2018
- Forrester (Brandon Purcell, Jan 2019): demand keeps rising with data-driven decision-making

### Haider's hiring hierarchy (top to bottom)
1. **Curiosity** about everything, not just data
2. **Sense of humour** so you don't take findings too seriously
3. **Storytelling ability**: know there *is* a story
4. **Technical skills last**: analytics can be taught; curiosity cannot

### Skills inventory (technical + soft)

**Technical:**
- Programming: **Python** (primary), **R** (statistical)
- Math: algebra, linear algebra, calculus, probability, statistics
- ML algorithms: decision trees, naive Bayes, Bayesian analysis, k-NN, regression
- Data storage + retrieval: RDBMS, NoSQL, big-data systems
- Domain tooling: R / Stata / Python for structured + predictive; Python for unstructured; **Hadoop + Spark** for big data

**Soft + cross-cutting:**
- Communication, presentation, storytelling
- Analytical + computational thinking
- Domain passion ("excited about *this* kind of business")
- Self-learning + tinkering attitude
- Awareness of trade-offs: precision vs recall, oversampling, overfitting

### Why a team beats a unicorn
The "data scientist with every skill" is rare. Build complementary teams: someone who understands the domain, someone who loves to play with the data, stats/math/ML/programming expertise, and a strong storyteller.

### Where DS sit in an org
- Best home: **research-leaning** depts of pharma, finance, any tech company
- Worst home: under a finance/accounting-background CIO who "doesn't get it"
- Heavy demand from Facebook, LinkedIn, Uber, Lyft

### Storytelling test (Haider's mountain metaphor)
> Your audience drives on a mountain, can't see past the sharp turn. They round it; suddenly a tremendous valley appears, a great sense of awe. Good data-science findings + good narration produce that feeling.

### Required report content

| What | Why |
|---|---|
| Clear goals | What was investigated |
| Significance of contribution | Why this matters |
| Context / background | Enough for non-experts to follow |
| Practical usefulness | Will someone act on this? |
| Plausible future developments | Where this could go next |

## Module 4 (optional): Data Literacy

### Lesson 4.1: Understanding Data

### Data structure trichotomy ([[data-structure-trichotomy]])

| Type | Definition | Storage | Sources |
|---|---|---|---|
| **Structured** | Well-defined schema, rows + columns | RDBMS, spreadsheets | OLTP, SQL DBs, GPS / RFID sensors, online forms, web + server logs |
| **Semi-structured** | Some organisation via tags + metadata, no rigid schema | XML / JSON files, NoSQL | Emails, XML/JSON, binary executables, TCP/IP packets, ZIPs |
| **Unstructured** | No identifiable structure, heterogenous | Files, NoSQL with AI-based analysis | Web pages, social-media feeds, images, video, audio, PDFs, slides, media logs, surveys |

### Sources of data ([[data-sources]])

| Source | Typical formats | Use case |
|---|---|---|
| Internal RDBMS (SQL Server, Oracle, MySQL, DB2) | Tables | Transactions, CRM, HR, workflows |
| Public + private datasets (gov demographics, paid weather, POS, financial) | Flat files, spreadsheets, XML | Strategy, forecasting, segmentation |
| **APIs + web services** (Twitter, Facebook, stock-market, address validation) | JSON, XML, plain text | Sentiment analysis, market data, data cleansing |
| **Web scraping** (BeautifulSoup, Scrapy, Selenium, Pandas) | HTML → structured | Price comparison, lead gen, ML datasets |
| **Data streams** (Kafka, Spark Streaming, Storm) | Real-time timestamped + geotagged | Financial tickers, IoT, sentiment, click feeds, traffic, surveillance |
| **RSS feeds** | XML | News + forum aggregation |

### Metadata categories ([[metadata]])
- **Technical** (schema, types)
- **Process** (lineage, provenance)
- **Business** (semantic meaning, ownership)

Managed in a **data catalog** for discoverability, governance, repeatability.

### Lesson 4.2: Data Literacy (Repositories + Pipelines)

### Repository taxonomy

| Repo | Best for | Examples |
|---|---|---|
| **RDBMS** | Structured data, OLTP, ACID guarantees | DB2, MS SQL Server, MySQL, Oracle, PostgreSQL. Cloud: Amazon RDS, Google Cloud SQL, DB2 on Cloud, SQL Azure |
| **NoSQL** | Schema flexibility, high volume, varied data | (4 sub-types below) |
| **Data warehouse** | Cleansed, modeled historical data for reporting + OLAP | Single source of truth |
| **Data mart** | Sub-section of warehouse for one business function | Sales mart, finance mart |
| **Data lake** | Raw data in native format, metadata-tagged, no pre-defined use | Predictive + advanced analytics, ML staging |

### NoSQL sub-types ([[nosql-types]])

| Type | Model | Good for | Avoid for | Examples |
|---|---|---|---|---|
| **Key-value** | Unique key → value | Session data, user prefs, real-time recommendations, in-memory caching | Querying by value, multi-key relationships | Redis, Memcached, DynamoDB |
| **Document** | JSON-like docs in collections | eCommerce, medical records, CRM, analytics | Complex multi-operation transactions | MongoDB, DocumentDB, CouchDB, Cloudant |
| **Column** | Data grouped in column families on disk | Heavy write loads, time-series, IoT, weather | Frequently-changing query patterns | Cassandra, HBase |
| **Graph** | Nodes + edges with properties | Social networks, recommendations, fraud detection, access management | High-volume analytical queries | Neo4j, CosmosDB |

### Why NoSQL emerged
RDBMSes struggle with: heavy write loads (B-tree slowdown on random writes from IoT / social media), semi-structured + unstructured data, schema evolution, and field-length limits. Google's BigTable whitepaper (2006) inspired Cassandra + HBase.

### ACID (the RDBMS guarantee) ([[acid]])
**A**tomicity, **C**onsistency, **I**solation, **D**urability. Data stays accurate and transactions remain reliable despite failures. NoSQL generally trades ACID for scale.

### RDBMS strengths
- Joining tables creates new info from old
- Schema flexibility while running (add cols, rename, change relations)
- Reduced redundancy via linked tables
- Easy export + import; continuous mirroring on cloud
- ACID compliance

### RDBMS limitations
- Bad with semi/unstructured data
- Migration requires schema + type identity between source + destination
- Field-length limits silently drop overflowing data
- B-tree slowdown on write-heavy IoT / social-media workloads

### ETL ([[etl-process]])

| Step | What happens | Tools |
|---|---|---|
| **Extract** | Pull from source. Batch OR streaming | Batch: Stitch, Blendo. Stream: Apache Kafka, Storm, Samza |
| **Transform** | Normalise formats + units, dedupe, filter, enrich (split name into first/last), enforce key relationships, apply business rules | (any ETL tool) |
| **Load** | Push to destination: initial / incremental / full refresh. Verify: missing values, server perf, load failures | Watch for load failures + ensure recovery |

### Data pipelines vs ETL ([[data-pipeline]])

| | Data Pipeline | ETL |
|---|---|---|
| Scope | Entire source-to-destination journey | Subset focused on transforming into analysis-ready |
| Mode | Batch + streaming + hybrid | Historically batch, increasingly streaming |
| Destination | Anywhere (lake, app, viz tool) | Usually a warehouse |
| Tools | Apache Beam, DataFlow | (any ETL stack) |

### Data integration ([[data-integration]])
Gartner: practices + architecture + tools that ingest, transform, combine, and provision data across types. Modern platforms support:
- Pre-built connectors (DBs, flat files, social, APIs, CRM, ERP)
- Open-source architecture (avoid vendor lock-in)
- Batch + stream optimisation
- Big-data integration
- Quality, governance, compliance, security
- Portability across single / multi / hybrid cloud

**Vendors:** IBM (Information Server, Cloud Pak for Data/Integration, InfoSphere DataStage), Talend (Data Fabric, Cloud, Catalog), SAP, Oracle, Denodo, Microsoft, Qlik, TIBCO. Open source: Dell Boomi, Jitterbit, SnapLogic. Cloud iPaaS: Adeptia, Google Cloud, IBM App Integration Suite, Informatica Integration Cloud.

### Choosing a repository: the practitioner heuristic
1. **Use case**: structured / semi / unstructured? Known schema?
2. **Performance**: data at rest vs in motion / streaming?
3. **Security**: encryption needed?
4. **Volume**: big-data tooling required?
5. **Access pattern**: short interactive queries vs long analytical runs? OLTP vs OLAP?
6. **Compatibility** with existing langs / tools / processes
7. **Scalability**: not just today's load but growth trajectory
8. **Org standards + in-house skills inventory + cost** of operating

## Exam-relevant takeaways

- **5 Vs of big data**: Volume, Velocity, Variety, Veracity, Value
- **5 cloud essential characteristics**: on-demand self-service, broad network access, resource pooling, rapid elasticity, measured service
- **3 cloud deployment models**: public, private, hybrid
- **3 cloud service models**: IaaS, PaaS, SaaS
- **AI taxonomy**: AI ⊃ ML ⊃ DL; GenAI is a parallel subset of AI that *produces* new data
- **Structured vs semi-structured vs unstructured** data, with example sources for each
- **4 NoSQL sub-types** + canonical use case + an example DB for each
- **Data-mining 6-step process**: goal → select → preprocess → transform → mine → evaluate
- **ETL vs data pipeline**: ETL is a subset of pipeline; pipelines can be batch, streaming, or hybrid
- **ACID**: Atomicity, Consistency, Isolation, Durability
- **Hadoop / HDFS / Hive / Spark** roles and what each is best for
- **DS process steps**: clarify question → gather data → analyse with multiple models → communicate via storytelling
- **#1 trait** every guest cites: **curiosity**. Second: **storytelling**. Technical skills are teachable, these are not.

## Related concepts (KB stubs)

- [[data-science]] [[ds-traits]] [[ds-process]]
- [[big-data]] [[5-vs-of-big-data]] [[data-mining]]
- [[cloud-computing]] [[iaas]] [[paas]] [[saas]] [[public-cloud]] [[private-cloud]] [[hybrid-cloud]]
- [[hadoop-stack]] [[hdfs]] [[apache-hive]] [[apache-spark]] [[mapreduce]]
- [[ai-taxonomy]] [[machine-learning]] [[deep-learning]] [[neural-network]] [[generative-ai]]
- [[regression]] [[k-nearest-neighbour]] [[recommendation-engine]]
- [[structured-data]] [[semi-structured-data]] [[unstructured-data]]
- [[rdbms]] [[nosql]] [[nosql-types]] [[acid]]
- [[data-warehouse]] [[data-mart]] [[data-lake]] [[etl-process]] [[data-pipeline]] [[data-integration]]
- [[metadata]] [[data-catalog]]
- [[csv]] [[tsv]] [[xml]] [[json]] [[xlsx]] [[pdf]]
- [[apache-kafka]] [[apache-storm]] [[apache-spark-streaming]]
- [[oltp]] [[olap]]

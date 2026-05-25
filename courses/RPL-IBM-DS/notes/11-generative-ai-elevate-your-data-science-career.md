# Course 11: Generative AI, Elevate Your Data Science Career

> Sub-course 11 of 12 in the IBM Data Science Professional Certificate
> 3 modules · 24 lectures · ~14 hours
> Source transcripts: `notes/transcripts/11-generative-ai-elevate-your-data-science-career/` (local, gitignored)

## TL;DR
GenAI is reshaping the data science workflow at **every phase**, from problem definition to deployment monitoring. The course covers: what GenAI is, the **four main model families** (GANs, VAEs, autoregressive, flow-based), how to apply GenAI at each stage of the DS lifecycle, hands-on demos (data prep, querying, insights, visualization, model dev), and importantly what to watch out for (bias, hallucinations, black-box behaviour, regulation, ROI). Treat GenAI as an **augmentation** tool that multiplies expert productivity, not a replacement for judgement.

## What is Generative AI? ([[generative-ai]])

> A subset of AI focused on **producing new data** rather than just analysing existing data. Uses deep-learning models that learn patterns from large datasets and generate new instances replicating the underlying distribution.

| Without GenAI | With GenAI |
|---|---|
| Analyse existing data | **Create** new data with similar properties |
| Limited to what you've collected | Augment, synthesise, simulate |
| Manual code, manual reports | Natural-language interfaces (text → code, text → SQL, text → chart) |

### Cross-industry applications

| Industry | GenAI use cases |
|---|---|
| **Healthcare** | Drug discovery, medical image synthesis, personalised treatment, risk prediction |
| **Finance** | Risk management, fraud detection, scenario simulation, investment portfolios |
| **Retail** | Personalised recommendations, product design, supply-chain optimisation |
| **Manufacturing** | Production simulation, design optimisation, quality control |
| **Media + entertainment** | Content generation, personalisation, creative workflows |
| **Education** | Personalised learning, adaptive materials, real-time feedback |
| **Transportation** | Traffic prediction, route optimisation, safety analysis |

## How data scientists use GenAI

| Use | Examples |
|---|---|
| **Synthetic data** | Augment small/imbalanced datasets; preserve privacy in sensitive domains |
| **Code generation** | Boilerplate Jupyter notebooks, scikit-learn snippets, debugging, translating between languages |
| **Hypothesis exploration** | Test more hypotheses than a human analyst could manually |
| **Automated insights/reports** | Generate narrative summaries from raw data (e.g. IBM Cognos Analytics) |
| **Natural-language data access** | Ask the database a question in English; LLM converts to SQL |
| **Documentation** | One-pagers, README files, architecture diagrams, presentations |

## Skills data professionals need ([[ds-skills-for-genai]])

**Technical:**
- **Programming**: Python (essential), R
- **ML frameworks**: TensorFlow, PyTorch, scikit-learn, Hugging Face, Keras
- **Architectures**: transformers, encoders/decoders, embeddings, diffusion models
- **Prompt engineering**: zero/few-shot, RAG (retrieval-augmented generation), agentic workflows
- **Fine-tuning techniques**: instruction tuning, PEFT (parameter-efficient fine-tuning)
- **Math/stats**: linear algebra, probability, regression, classification
- **Visualisation**: Matplotlib, Plotly, Seaborn
- **Deployment**: Docker, Kubernetes, cloud platforms (Azure, GCP, AWS)

**Soft / cross-cutting:**
- Problem solving + adaptability
- Ethical decision-making
- Ability to **evaluate** AI output quickly (faster iteration → better solutions)
- Domain expertise to spot when GenAI is wrong

## GenAI in the Data Science Lifecycle ([[data-science-lifecycle]])

The 5 phases and where GenAI helps:

| Phase | What it is | GenAI contribution |
|---|---|---|
| **1. Problem definition + business understanding** | Define the problem and the business context | Idea generation, synthetic customer profiles, scenario simulation (market trends, competitor actions) |
| **2. Data acquisition + preparation** | Collect and preprocess data | Imputation (missing values), augmentation (synthetic data), anomaly detection |
| **3. Model development + training** | Select + train ML algorithms | Feature engineering, AutoML/hyperparameter exploration, interpretability explanations |
| **4. Model evaluation + refinement** | Test performance, robustness | Adversarial/edge-case generation, uncertainty estimation, counterfactual reasoning ("what if?") |
| **5. Model deployment + monitoring** | Run in production | Data-drift detection, personalised content, A/B test variant generation |

> Memorise these 5 phases. The course quiz will almost certainly ask about them.

## The four common GenAI model types ([[genai-model-families]])

| Model | How it works | Best at | Notable example |
|---|---|---|---|
| **GANs** (Generative Adversarial Networks) | Two competing nets: **generator** creates fake, **discriminator** judges real vs fake. Adversarial loop drives realism | High-fidelity images, music, text, data augmentation | StyleGAN (faces) |
| **VAEs** (Variational Autoencoders) | Encode data into a **latent representation**, then decode to generate new samples | Anomaly detection, data compression, collaborative filtering, style transfer | VAEGAN |
| **Autoregressive** | Generate one element at a time, predicting next based on previous | Sequential data: text, speech, time-series forecasting | **GPT** family |
| **Flow-based** | Directly model the **probability distribution** of the data | Image generation, anomaly detection, density estimation | RealNVP |

### Quick decision guide
- Need realistic images / music? → **GAN**
- Anomaly detection / dimensionality reduction? → **VAE**
- Sequential text / time-series? → **Autoregressive**
- Density estimation / probabilistic sampling? → **Flow-based**

## GenAI tools for data scientists

### Open source
- **Hugging Face Transformers**, model library, datasets, evaluation
- **LangChain**, build LLM-powered pipelines (RAG, summarisation, agents)
- **TensorFlow / PyTorch / MLflow**, modelling + lifecycle

### Proprietary chat / code assistants
- **ChatGPT** (OpenAI), text + code, fine-tunable
- **Claude** (Anthropic), reasoning + code
- **Microsoft Copilot**, productivity + code
- **GitHub Copilot**, IDE code-completion (VS Code chat)
- **IBM watsonx Code Assistant**, code generation tuned for enterprise

### ML / AutoML platforms
| Tool | Strength | Limitation |
|---|---|---|
| **DataRobot** | Enterprise auto-ML, easy UI, on-prem or cloud | Expensive; less customisable |
| **AutoGluon** | Open source, auto model selection + tuning | Needs Python skills; limited customisation |
| **H2O Driverless AI** | Drag-and-drop, built-in explainability | Costly for individuals; cloud-locked |
| **Amazon SageMaker Autopilot** | AWS-integrated; pay-as-you-go | Vendor lock-in to AWS |
| **Google Vertex AI** | Deep-learning support, explainability | Complex for beginners; pricey |

### BI + visualisation
- **Tableau GPT**, auto-generate dashboards from prompts
- **Power BI Copilot**, text-to-visualisation

## Module 2: GenAI for the DS workflow

### Data generation + augmentation

| Data type | Tools / techniques |
|---|---|
| **Structured** (tabular) | **CTGAN**, **SDV** (Synthetic Data Vault) |
| **Semi-structured** (text, code) | GPT, Copilot |
| **Unstructured: images** | **StyleGAN2**, **BigGAN** |
| **Unstructured: audio** | **SoundGAN** (NVIDIA) |

Demo tools: Universal Data (`generate.universaldata.io`), MostlyAI (`synthetic.mostly.ai`), CTGAN in a Colab notebook.

### Data preparation: which model for which problem?

| Problem | Best GenAI tool | Why |
|---|---|---|
| **Missing values** | **VAE** | Learns underlying distribution, plausibly fills gaps |
| **Outlier detection** | **GAN** | Discriminator learns the "normal" data boundary |
| **Noise reduction** | **Autoencoder** | Compresses to core info, drops noise |
| **Data translation** (formats, languages) | **NMT** (Neural Machine Translation, RNN-based) | Sequence-to-sequence learning |

Hands-on tools demo'd: **ChatCSV**, **Tomat.AI** (joins, filters, if-then rules, AI assistant for missing-value suggestions).

### Data querying: text → SQL

| Capability | GenAI model |
|---|---|
| Translate **natural language** to SQL | **LLMs** (context-aware) |
| **Query recommendation** based on history | **RNNs** (sequential patterns) |
| **Query optimisation** | **GNNs** (graph neural networks model data + relationships) |

Demo: **SQL through AI**, plus emerging tools like **Gen SQL** that lets DB users do stats / anomaly detection without writing SQL.

### Data insights (EDA)
- Use ChatGPT/GPT-3.5 to generate Python code for `describe()`, univariate, bivariate, multivariate analysis
- Use `SelectKBest` for feature selection, `PolynomialFeatures` for feature engineering, all via prompted code
- Demo platform: **hal9** (free plan, prompted EDA on uploaded CSV)

### Data visualisation
- **columns.AI**, story-driven chart generation
- **Akkio**, chat-driven scatter plots, bar charts, correlation matrices, box plots, histograms
- All from natural-language prompts, no code needed

### Model development with GenAI

GenAI helps with:
- **Architecture selection**, VAE latent reps to pick linear vs tree vs neural
- **Feature importance**, MINN (mutual information neural networks)
- **Ensembles**, GANs to generate diverse data representations
- **Interpretability**, interpretable autoencoders explain predictions
- **Generalisation / overfitting prevention**, denoising autoencoders

## Module 3: Considerations, challenges, future

### Three key considerations when using GenAI ([[genai-considerations]])

| Dimension | What to watch |
|---|---|
| **Data** | Quality, representativeness, **bias** in training data, privacy |
| **Model** | **Explainability** (decision-making clarity) + **interpretability** (output clarity); use feature attribution, partial dependence plots |
| **Ethical** | Deepfakes, misinformation, malicious use; need clear guidelines + human oversight |

### Industry-specific considerations

| Industry | Key risks / constraints |
|---|---|
| **Finance** | Regulatory (encryption, data privacy laws); robust against adversarial inputs; bias in loan approvals |
| **Healthcare** | HIPAA compliance; anonymisation; informed consent; high accuracy required (misdiagnosis risk) |
| **Retail** | Customer-data privacy; bias in product recommendations |

### Challenges in 3 categories ([[genai-challenges]])

**Technical:**
- Data quality + availability
- Model interpretability (black-box)
- **AI hallucinations** (plausible-sounding but wrong output)
- Compute cost (large models = expensive infra)
- Lack of standardisation across model architectures / evaluation

**Organisational:**
- IP + copyright concerns (some firms ban public GenAI tools)
- Skill gaps (ML engineers with GenAI experience are scarce)
- Integration with existing pipelines + decision processes
- Change management (job-displacement fears)
- Measuring ROI (intangible benefits hard to quantify)

**Cultural:**
- Risk aversion / hesitation to adopt
- Data-sharing reluctance (security worries)
- Trust + transparency (stakeholders don't trust opaque outputs)
- Continuous-learning culture required

### What experts say about the next 5 years
- **Automation** of mundane DS tasks (data extraction, cleaning, normalisation, imputation)
- **Democratisation**, low-code / no-code AutoML reaches non-experts
- **Agentic workflows** abstract away parts of the pipeline (prompt → script → data, no manual code in between)
- **Synthetic data** becomes central, especially for privacy-sensitive or rare-event domains
- Specialised expertise still needed for complex problems (GenAI raises baseline, doesn't replace experts)

### How to stay current
- Follow companies + executives: IBM, Meta, OpenAI, Anthropic, Mistral, Hugging Face, NVIDIA, Google, AWS
- Read papers from NeurIPS, ICML, CVPR; arXiv
- Continuous learning: Coursera, edX, Udemy, NVIDIA, Microsoft, Google, AWS courses
- Hands-on: GitHub repos, SDKs, experiment with new tools
- Newsletters: Towards Data Science (Medium), AI-focused newsletters

## Common pitfalls / exam-relevant takeaways

- **Hallucinations**: GenAI generates plausible but wrong output, always verify against ground truth.
- **Bias**: training data bias gets baked into generated output; needs fairness checks (e.g. fairness-aware algorithms, adversarial training).
- **Black-box**: many GenAI models are hard to explain; in regulated industries (finance, healthcare), this is a deployment blocker.
- **Plagiarism**: using AI-generated code verbatim is plagiarism, always personalise/modify.
- **GenAI is not 100% autonomous**: human oversight is required at every step.
- **GenAI augments experts, doesn't replace novices**: a beginner using GenAI won't do data science well; an expert using GenAI does it faster.
- The **5 lifecycle phases** are the cleanest exam target: memorise them and what GenAI does at each.
- The **4 model types** (GAN/VAE/Autoregressive/Flow-based) and **what each is best for** is the other obvious exam target.

## Required skills for data scientists (course wrap-up)

1. Math + statistics foundations (probability, distributions, linear algebra)
2. Programming (Python primarily)
3. **Data preparation** (cleaning, normalising, handling missing values)
4. Statistical analysis (feature engineering, hypothesis testing)
5. **ML principles** (knowing which algorithm fits which data)
6. Hands-on practice (Kaggle, real datasets)
7. **Continuous learning** (especially GenAI, the landscape moves monthly)

## Related concepts (KB stubs)
- [[generative-ai]]
- [[gan]], [[vae]], [[autoregressive-model]], [[flow-based-model]]
- [[data-science-lifecycle]]
- [[synthetic-data]], [[data-augmentation]]
- [[hallucination]], [[ai-bias]], [[deepfake]]
- [[prompt-engineering]], [[rag]], [[agentic-workflow]], [[few-shot-prompting]]
- [[automl]]
- [[explainable-ai]], [[interpretability]]
- [[ctgan]], [[sdv]], [[stylegan]], [[soundgan]]
- [[natural-language-to-sql]]
- [[mlops]], [[llm-ops]]
- [[hipaa]], [[gdpr]] (already in CM2025 notes)

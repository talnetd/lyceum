# Practice Quiz: Generative AI, Elevate Your Data Science Career

> RPL-IBM-DS sub-course 11 · self-test before the graded quizzes
> Source of truth: [`../notes/11-generative-ai-elevate-your-data-science-career.md`](../notes/11-generative-ai-elevate-your-data-science-career.md)
> Format mirrors the 3 graded module quizzes. Answers + explanations at the bottom; cover them while you test.

---

## Module 1: GenAI fundamentals, lifecycle, models, tools

**Q1.** What most clearly distinguishes generative AI from traditional (discriminative) AI?
- A) It runs faster on GPUs
- B) It produces new data resembling the training distribution, rather than only analysing existing data
- C) It never needs training data
- D) It only works on images

**Q2.** Put the 5 data science lifecycle phases in order.
- A) Data acquisition → Problem definition → Deployment → Model development → Evaluation
- B) Problem definition → Data acquisition + preparation → Model development → Evaluation + refinement → Deployment + monitoring
- C) Model development → Problem definition → Data acquisition → Deployment → Evaluation
- D) Problem definition → Model development → Data acquisition → Deployment → Evaluation

**Q3.** Match the model family to what it is best at.
1. GAN  2. VAE  3. Autoregressive  4. Flow-based
- a) Sequential data (text, time-series)
- b) High-fidelity image/music generation, augmentation
- c) Density estimation / probabilistic sampling
- d) Anomaly detection, compression, latent representations

**Q4.** A GAN's two competing networks are:
- A) Encoder and decoder
- B) Generator and discriminator
- C) Actor and critic
- D) Teacher and student

**Q5.** Which model family does the GPT family belong to?
- A) GAN
- B) VAE
- C) Autoregressive
- D) Flow-based

**Q6.** In phase 4 (model evaluation + refinement), a typical GenAI contribution is:
- A) Imputing missing values
- B) Generating adversarial / edge-case examples and counterfactual ("what if") reasoning
- C) Defining the business problem
- D) Detecting data drift in production

**Q7.** Which of these is an open-source GenAI tooling option (not a proprietary chat/code assistant)?
- A) ChatGPT
- B) Microsoft Copilot
- C) Hugging Face Transformers
- D) IBM watsonx Code Assistant

**Q8.** A key limitation of AutoML platforms like DataRobot or H2O Driverless AI is:
- A) They cannot do classification
- B) Cost and vendor lock-in / limited customisation
- C) They require no data
- D) They only run on-premises

---

## Module 2: GenAI across the DS workflow

**Q9.** To fill **missing values** by learning the data's underlying distribution, the note recommends:
- A) GAN
- B) VAE
- C) NMT
- D) GNN

**Q10.** For **outlier / anomaly detection** during data prep, which model's design fits best?
- A) GAN (discriminator learns the "normal" boundary)
- B) Autoregressive
- C) NMT
- D) Flow-based only

**Q11.** Translating a natural-language question into SQL is best handled by:
- A) RNNs
- B) GNNs
- C) Context-aware LLMs
- D) CTGAN

**Q12.** Query **optimisation** that models data and its relationships uses:
- A) LLMs
- B) RNNs
- C) GNNs (graph neural networks)
- D) VAEs

**Q13.** For generating **synthetic tabular (structured) data**, the appropriate tools are:
- A) StyleGAN2 / BigGAN
- B) CTGAN / SDV (Synthetic Data Vault)
- C) SoundGAN
- D) GPT / Copilot

**Q14.** Which tool pairing matches "natural-language EDA on an uploaded CSV" and "chat-driven charts"?
- A) ChatCSV and Tomat.AI
- B) hal9 and Akkio
- C) DataRobot and SageMaker
- D) LangChain and MLflow

**Q15.** In model development, a denoising autoencoder is used mainly to:
- A) Select the learning rate
- B) Prevent overfitting / improve generalisation
- C) Translate languages
- D) Optimise SQL queries

---

## Module 3: Considerations, challenges, future

**Q16.** The "three key considerations" framework when using GenAI is:
- A) Speed, cost, accuracy
- B) Data, model, ethical
- C) Hardware, software, network
- D) Train, test, validate

**Q17.** "Explainability" vs "interpretability" in this course:
- A) They are identical
- B) Explainability = clarity of the decision-making process; interpretability = clarity of the output
- C) Explainability only applies to images
- D) Interpretability is a type of hallucination

**Q18.** An **AI hallucination** is:
- A) A hardware fault
- B) Output that sounds plausible but is factually wrong
- C) A type of GAN
- D) A privacy breach

**Q19.** "Measuring ROI" and "skill gaps" fall under which challenge category?
- A) Technical
- B) Organisational
- C) Cultural
- D) Regulatory

**Q20.** "Trust and transparency" and "risk aversion to adoption" fall under which category?
- A) Technical
- B) Organisational
- C) Cultural
- D) Legal

**Q21.** In healthcare specifically, a named constraint is:
- A) HIPAA compliance, anonymisation, informed consent, high accuracy
- B) Loan-approval bias
- C) Supply-chain optimisation
- D) Per-stream royalty rates

**Q22.** Which statement best matches the course's overall stance on GenAI?
- A) GenAI fully replaces data scientists
- B) GenAI augments experts to work faster but still needs human oversight and domain judgement
- C) GenAI should never be used in industry
- D) GenAI removes the need for any verification

**Q23.** Using AI-generated code verbatim in your work is described as:
- A) Best practice
- B) Plagiarism; you must personalise / modify it
- C) Required by Coursera
- D) Impossible

**Q24.** Experts predict that over the next ~5 years, GenAI will most likely:
- A) Eliminate the need for math and statistics
- B) Automate mundane tasks, democratise via low/no-code, and push agentic workflows, while experts stay essential for complex problems
- C) Make synthetic data illegal
- D) Replace all cloud platforms

---

## Answer key

| Q | Ans | Why |
|---|---|---|
| 1 | **B** | GenAI *creates* new data matching the learned distribution; discriminative AI only analyses/classifies existing data. |
| 2 | **B** | Problem definition → Data acquisition+prep → Model dev → Evaluation+refinement → Deployment+monitoring. |
| 3 | **1-b, 2-d, 3-a, 4-c** | GAN=images/music; VAE=anomaly/compression/latent; Autoregressive=sequential; Flow-based=density estimation. |
| 4 | **B** | Generator creates fakes, discriminator judges real vs fake; adversarial loop drives realism. |
| 5 | **C** | GPT generates one token at a time conditioned on previous tokens = autoregressive. |
| 6 | **B** | Adversarial/edge-case generation + counterfactual reasoning belong to evaluation/refinement. (D is deployment; A is data prep.) |
| 7 | **C** | Hugging Face Transformers is open source; A/B/D are proprietary assistants. |
| 8 | **B** | Enterprise AutoML is powerful but costly, less customisable, and often cloud/vendor-locked. |
| 9 | **B** | VAE learns the underlying distribution to plausibly fill gaps. |
| 10 | **A** | GAN's discriminator learns the "normal" data boundary, flags outliers. |
| 11 | **C** | Context-aware LLMs do natural-language-to-SQL. |
| 12 | **C** | GNNs model data + relationships for query optimisation. (RNNs = query recommendation from history.) |
| 13 | **B** | CTGAN / SDV generate synthetic structured/tabular data. (StyleGAN/BigGAN=images, SoundGAN=audio.) |
| 14 | **B** | hal9 = prompted EDA on a CSV; Akkio = chat-driven charts. |
| 15 | **B** | Denoising autoencoders improve generalisation / reduce overfitting. |
| 16 | **B** | The trio is Data, Model, Ethical. |
| 17 | **B** | Explainability = decision-process clarity; interpretability = output clarity. |
| 18 | **B** | Plausible-sounding but wrong output; always verify against ground truth. |
| 19 | **B** | ROI measurement and skill gaps are organisational challenges. |
| 20 | **C** | Trust/transparency and risk aversion are cultural challenges. |
| 21 | **A** | Healthcare: HIPAA, anonymisation, informed consent, high accuracy (misdiagnosis risk). |
| 22 | **B** | GenAI augments experts; human oversight + domain judgement remain essential. |
| 23 | **B** | Verbatim AI code = plagiarism; modify and personalise. |
| 24 | **B** | Automation of mundane tasks, democratisation, agentic workflows; experts still needed. |

### Weak-spot tracker
Note any question you missed and the topic, then re-read that section of the note before the graded quiz:
- [ ] Lifecycle phases (Q2, Q6)
- [ ] Model families + what each is best at (Q3, Q4, Q5)
- [ ] Data-prep / querying model mapping (Q9-Q12)
- [ ] Synthetic-data + demo tools (Q13, Q14)
- [ ] Considerations / challenge categories (Q16-Q21)

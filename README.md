# Intelligent Automation for Customer Support Tickets

This project explores the design and implementation of an **intelligent, human-in-the-loop automation system** for customer support ticket triage in a **multilingual (Arabic + English) telecommunications context**.

The objective is to improve **ticket categorization, priority assignment, and routing consistency**, while explicitly preserving human oversight for ambiguous, low-confidence, or high-risk cases.

This repository is structured as a **phase-based project**, mirroring how real-world data and automation systems are designed and built incrementally.

---

## Project Phases

- **Phase 1** – Domain understanding & problem framing  
- **Phase 1.5** – Ticket schema & decision-flow design  
- **Phase 2** – Dataset design & realism (Arabic + English) ✅  

Upcoming phases will cover:
- Bilingual text preprocessing
- Feature engineering
- Classification models
- Automation logic
- Evaluation and human-in-the-loop design

---

## Repository Structure


intelligent-support-ticket-automation/
│
├── data/
│ └── raw/
│ └── telco_support_tickets_dataset.csv
│
├── docs/
│ └── phase_02_data_design.md
│
├── dataset_generator/
│ └── dataset_generator.html
│
├── README.md
└── .gitignore


---

## Current Contents

### `data/raw/`
Contains the **raw bilingual support ticket dataset** designed in Phase 2.

- The dataset is **synthetic but operationally realistic**
- Includes Arabic, English, and mixed-language tickets
- Intentionally contains:
  - Noise and typos
  - Ambiguous tickets
  - An explicit **“Other”** category
  - Missing values with documented logic

⚠️ The CSV in this folder is treated as the **source of truth** and should not be edited directly.

---

### `docs/phase_02_data_design.md`
Comprehensive documentation for **Phase 2 – Dataset Design & Realism**, including:

- Dataset purpose and design philosophy  
- Exact schema and column definitions  
- Category definitions (including the intentional “Other” category)  
- Priority logic and distributions  
- Arabic, English, and mixed-language text design  
- Missing value strategy  
- Temporal patterns and realism assumptions  
- Known limitations of synthetic data  

This document should be read **before** working with the dataset.

---

### `dataset_generator/`
Contains an **auxiliary HTML-based dataset generator** used to create the Phase 2 synthetic dataset.

- The generator was used strictly as an **execution tool**
- All design decisions (schema, distributions, noise, missingness, language logic) are documented in `docs/phase_02_data_design.md`
- The generator itself does **not** define the dataset logic — it implements a predefined specification

The generated CSV stored in `data/raw/` is considered the authoritative dataset for all subsequent phases.

---

## How to Use This Repository

### 1️⃣ Start with the documentation
Read `docs/phase_02_data_design.md` to understand:
- What the dataset represents
- Why certain imperfections exist
- How categories, priorities, and missing values were designed

This context is essential before any preprocessing or modeling.

---

### 2️⃣ Inspect the raw dataset
Use the CSV in `data/raw/` for:
- Exploratory analysis
- Preprocessing design
- Model development in later phases

The file is stored using **UTF-8 encoding** to ensure correct handling of Arabic text.

Excel may be used for **visual inspection only**.  
Do not re-save or overwrite the CSV from spreadsheet tools.

---

### 3️⃣ (Optional) Regenerate the dataset
If you want to regenerate a dataset using the same design logic:

1. Open `dataset_generator/dataset_generator.html` in a browser
2. Generate a new dataset using the predefined controls
3. Export as CSV (UTF-8)
4. Treat regenerated datasets as **new versions** and do not overwrite existing committed data without versioning

⚠️ Regeneration should be done intentionally and documented, as it affects reproducibility.

---

### 4️⃣ Follow the phase order
Each phase builds logically on the previous one.

- Do **not** jump directly to modeling
- Preprocessing and automation logic will be introduced incrementally in future commits
- Each phase will include documentation and code aligned with the project narrative

---

## Notes & Constraints

- The dataset is **synthetic** and must not be treated as real customer data
- No personally identifiable information (PII) is included
- Ambiguity and noise are intentional and should not be “cleaned away” prematurely
- The “Other” category is a first-class label and is critical for evaluating low-confidence and human-in-the-loop scenarios

---

## Current Status

**Current phase:** Phase 2 – Dataset Design & Realism  
Next planned step: Phase 2 dataset audit and exploratory analysis, followed by bilingual text preprocessing design.

---

## License

This project is intended for educational, research, and portfolio purposes.  
No real customer data is used.

# Phase 2 – Dataset Design & Realism (Arabic + English)


## Project Context

This document corresponds to **Phase 2** of the project *Intelligent Automation for Customer Support Tickets*.

Phase 2 focuses on **designing a realistic, bilingual support ticket dataset** that reflects real-world telco operations, including noise, ambiguity, multilingual complexity, and missing data. The dataset serves as the foundation for later phases involving text preprocessing, classification, and automation logic.



## Design Philosophy

The dataset was designed and generated to prioritize operational realism over academic cleanliness.

### 1. **Realism Over Cleanliness**
- Real customer support data is messy, inconsistent, and contains errors
- Dataset should feel operational, not academic

### 2. **Intentional Imperfection**
- Missing values are strategic, not random
- "Other" category represents genuine ambiguity
- Imbalanced distribution mirrors real ticket volumes

### 3. **Multilingual Complexity**
- Arabic and English tickets with realistic distribution
- Mixed-language tickets (code-switching) are common in real telco operations
- Both formal and informal language patterns included

---

## Specification Requirements

The following specifications were defined *before* dataset generation to ensure consistency, realism, and reproducibility.

### Dataset Structure

**Target Size**: 2,000–3,000 rows

**Schema** (7 columns):

| Column Name | Type | Description | Missing Allowed |
|------------|------|-------------|-----------------|
| `ticket_id` | string | Unique identifier (format: TKT000001) | ❌ No |
| `created_at` | datetime | Ticket creation timestamp | ❌ No |
| `channel` | string | Contact channel (call, email, chat, app, web) | ✅ Yes (1-5%) |
| `ticket_text` | string | Raw customer message (messy, unedited) | ❌ No |
| `language` | string | Language code ("en", "ar") | ✅ Yes (5-10%) |
| `true_category` | string | Ground-truth category label | ❌ No |
| `true_priority` | string | Ground-truth priority label (P1-P4) | ✅ Yes (5-15%) |

### Language Distribution

- **60-70% English** (pure + mixed)
- **30-40% Arabic** (pure + mixed)
- **~15% Mixed** (code-switching: "internet فاصل من الصبح")

### Category Definitions

Eight distinct categories with specific operational meanings:

1. **Network / Connectivity** (~25%)
   - Internet outages, slow speed, signal loss, disconnections

2. **Billing & Payments** (~20%)
   - Wrong charges, double billing, invoice complaints, payment problems

3. **Account & Authentication** (~15%)
   - Login issues, SIM registration, account access, PIN/verification problems

4. **Roaming & International Services** (~10%)
   - No service abroad, international data, roaming charges

5. **Service Activation / Changes** (~12%)
   - Plan activation, cancellation, upgrades, downgrades

6. **Device / Hardware** (~8%)
   - Router problems, SIM card issues, modem/hardware faults

7. **Complaints & Service Quality** (~8%)
   - General dissatisfaction, poor service, repeated unresolved issues

8. **Other** (~10%) ⚠️ **CRITICAL CATEGORY**

   - Genuinely ambiguous tickets
   - Multi-topic without clear dominant issue
   - Out of scope complaints
   - Too vague to categorize confidently

**Note**: The "Other" category is intentionally preserved as a first-class label to support later analysis of ambiguity, low-confidence predictions, and human-in-the-loop decision-making.

### Priority Scale

| Priority | Meaning | Distribution |
|----------|---------|--------------|
| **P1** | Critical — service outage, major impact | ~5% (rare) |
| **P2** | High — individual service down, billing error | ~15% |
| **P3** | Medium — degraded service, repeated issue | ~40% (most common) |
| **P4** | Low — general inquiry, informational | ~40% (most common) |

### Temporal Distribution Requirements

A fixed 90-day window was chosen to capture realistic operational patterns (business hours, weekends, and off-hours incidents) without introducing artificial seasonality effects that would complicate downstream analysis.

**Date Range**: 2024-12-01 to 2025-02-28 (90 days, fixed for reproducibility)

**Time-of-Day Pattern** (realistic operational load):
- **Peak**: 09:00–18:00 (~70% of tickets)
- **Moderate**: 18:00–22:00 (~20% of tickets)
- **Low**: 22:00–09:00 (~10% of tickets, but non-zero)

**Day-of-Week Pattern**:
- **Highest**: Monday–Thursday
- **Slight drop**: Friday
- **Lower but present**: Saturday–Sunday

**Priority-Time Interaction** (advanced realism):
- **P1/P2 tickets**: Slightly more likely during off-hours (outages happen anytime)
- **P3/P4 tickets**: Concentrated during business hours (customers report routine issues)

### Text Characteristics

Ticket text was intentionally generated to reflect how customers actually write, rather than how they are expected to write.

**English Tickets**:
- Informal tone
- Typos allowed and encouraged
- Short sentences common
- Emotional language ("very bad", "terrible", "urgent")
- Examples: "internet not working since morning", "charged twice pls fix"

**Arabic Tickets**:
- Mix of Modern Standard Arabic and dialect
- Informal spelling patterns
- No diacritics (realistic for user input)
- Emotional expressions
- Examples: "النت فاصل من امبارح", "الخدمة سيئة جدا"

**Mixed Arabic + English**:
- Realistic code-switching patterns
- Not rare — reflects actual telco customer behavior
- Examples: "internet فاصل من الصبح", "billing مشكلة urgent"

### Intentional Noise

The dataset MUST include:
- Typos ("teh", "problm")
- Very short tickets ("help pls", "urgent")
- Emotional language ("worst service ever", "fed up")
- Repeated words
- Inconsistent punctuation ("!!!", "???")
- Mixed scripts within single ticket
- Inconsistent capitalization

### Missing Values Strategy

Missing values are **intentional and strategic**, not random:

| Column | Missing Rate | Reason |
|--------|-------------|---------|
| `language` | 5-10% | Language detection failed or not labeled |
| `true_priority` | 5-15% | Agent did not assign priority during triage |
| `channel` | 1-5% | System integration issues |

**Never missing**: `ticket_text`, `ticket_id`, `created_at`, `true_category`

This missingness pattern is later used to test robustness of preprocessing, imputation strategies, and automation fallback logic.

---

## ## Dataset Generation Approach

To efficiently generate a large, controlled, and multilingual dataset while maintaining realism, an AI-assisted synthetic data generation approach was used.

A detailed written specification (covering schema, distributions, language patterns, noise, and missingness) served as the single source of truth. Claude AI was used strictly as an execution tool to instantiate this specification, not to make independent design decisions.


#### Process Flow

```
┌─────────────────────────────────────┐
│  1. Design Specification Document   │
│     (Detailed requirements)         │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  2. Specification Review with AI    │
│     (Clarify temporal patterns)     │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  3. Interactive React Generator     │
│     (Built by Claude)               │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  4. Dataset Generation              │
│     (Click button → instant CSV)    │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  5. Statistics & Quality Check      │
│     (Verify distributions)          │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  6. CSV Export                      │
│     (UTF-8 with BOM for Excel)      │
└─────────────────────────────────────┘
```

### Generation Algorithm

The React-based generator implements:

1. **Weighted Random Sampling** for categories and priorities
2. **Template-Based Text Generation** with placeholder substitution
3. **Realistic Temporal Distribution** using rejection sampling
4. **Strategic Noise Injection** (15% probability per ticket)
5. **Controlled Missing Value Introduction** based on specified rates
6. **Language Distribution Control** with mixed-language support

---

## Dataset Characteristics - Illustrative Examples

These examples are illustrative and do not represent actual customer data.

### Sample Tickets

**Example 1: English, Network Issue, P2**
```
ticket_id: TKT000123
created_at: 2024-12-15T14:32:18
channel: chat
ticket_text: "internet not working since morning pls fix urgent"
language: en
true_category: Network / Connectivity
true_priority: P2
```

**Example 2: Arabic, Billing Issue, P3**
```
ticket_id: TKT000456
created_at: 2025-01-08T10:15:42
channel: call
ticket_text: "حاسبوني مرتين هالشهر"
language: ar
true_category: Billing & Payments
true_priority: P3
```

**Example 3: Mixed Language, Ambiguous, P4**
```
ticket_id: TKT000789
created_at: 2025-02-20T16:45:33
channel: app
ticket_text: "help محتاج urgent"
language: en
true_category: Other
true_priority: P4
```

### Statistical Profile (Typical Generation)

**Total Tickets**: 2,000–3,000 (randomized)

**Language Distribution**:
- English: 50-55%
- Arabic: 35-40%
- Missing: 7%

**Category Distribution** (intentionally imbalanced):
- Network / Connectivity: ~25%
- Billing & Payments: ~20%
- Account & Authentication: ~15%
- Service Activation / Changes: ~12%
- Roaming & International: ~10%
- Other: ~10%
- Device / Hardware: ~8%
- Complaints & Service Quality: ~8%

**Priority Distribution**:
- P1: ~5%
- P2: ~15%
- P3: ~40%
- P4: ~40%

**Channel Distribution** (roughly uniform):
- call, email, chat, app, web: ~19-21% each
- missing: ~3%

**Temporal Patterns**:
- Weekday tickets: ~75%
- Weekend tickets: ~25%
- Business hours (9-18): ~70%
- Evening (18-22): ~20%
- Off-hours: ~10%

---

## Generation Process

### Step 1: Specification Document

A comprehensive 2,400+ word specification was created defining:
- Dataset purpose and use case
- Exact schema and column names
- Category and priority definitions
- Language requirements and examples
- Noise and imperfection requirements
- Missing value logic
- Overall design philosophy

### Step 2: AI Consultation

The specification was provided to Claude with a single instruction:
> "Create the dataset exactly according to this specification. Ask clarifying questions only if absolutely necessary."

Claude identified **one critical missing requirement**: temporal distribution details.

### Step 3: Temporal Requirements Refinement

Additional specifications provided:
- Fixed date range (2024-12-01 to 2025-02-28)
- Time-of-day distribution with business hours bias
- Day-of-week patterns with weekend reduction
- Priority-time interaction (urgent tickets more likely off-hours)

### Step 4: Generator Implementation

Claude created an interactive React application with:
- One-click dataset generation
- Real-time statistics display
- Sample ticket preview
- CSV export with UTF-8 encoding
- Full specification compliance

### Step 5: Validation

Generated datasets were validated against:
- ✅ Correct column names and types
- ✅ Distribution targets (categories, priorities, languages)
- ✅ Missing value rates
- ✅ Temporal pattern realism
- ✅ Text quality (both languages)
- ✅ Noise and imperfection presence

---

## Quality Assurance

Basic validation checks were performed to ensure the generated dataset adhered strictly to the predefined specification.


### Validation Checklist

- [x] **Schema Compliance**: All 7 columns present with correct names
- [x] **Size Target**: 2,000-3,000 rows generated
- [x] **Language Distribution**: 60-70% English, 30-40% Arabic achieved
- [x] **Category Balance**: Distribution matches specification weights
- [x] **Priority Balance**: P3/P4 dominant, P1 rare
- [x] **Missing Values**: Strategic, not random; rates within target ranges
- [x] **Text Quality**: Realistic, informal, with intentional typos
- [x] **Mixed Language**: Present and realistic
- [x] **"Other" Category**: 5-15% with genuinely ambiguous content
- [x] **Temporal Patterns**: Business hours peak, weekend reduction
- [x] **Priority-Time Correlation**: Urgent tickets slightly more off-hours
- [x] **No Hallucination**: No predicted labels or model outputs included

### Known Limitations

1. **Synthetic Nature**: While realistic, this is generated data, not actual customer tickets
2. **Template-Based**: Some repetition in phrasing patterns may occur
3. **Simplified Arabic**: Dialect mixing is simplified compared to real-world variety
4. **Limited Context**: Tickets are independent; no conversation threads or follow-ups
5. **No PII**: No personally identifiable information (by design, for safety)

### Recommendations for Use

**✅ DO:**
- Use for model training and evaluation
- Test multilingual preprocessing pipelines
- Evaluate categorization algorithms
- Simulate human-in-the-loop workflows
- Benchmark model performance

**❌ DON'T:**
- Treat as real customer data for business decisions
- Use for final model validation without real data testing
- Assume perfect label accuracy (some ambiguity is intentional)
- Ignore the "Other" category in evaluation

---

## Usage & Next Steps

### How to Generate

1. Open the React generator application
2. Click "Generate Dataset (2,000-3,000 rows)"
3. Review statistics and sample tickets
4. Click "Download CSV Dataset"
5. CSV file includes UTF-8 BOM for Excel compatibility


## Alignment with Project Phases

- **Phase 3**: Bilingual text preprocessing and missing value handling

- **Phase 4**: Feature engineering and representation learning

- **Phase 5**: Classification models and automation logic

- **Phase 6**: Evaluation, confidence analysis, and human-in-the-loop design





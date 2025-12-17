
# Phase 2 — Dataset Audit Summary

## 1. Dataset Shape & Structure

* **Total rows:** 2,743 support tickets
* **Total columns:** 7
* **Memory footprint:** ~150 KB

The dataset size is realistic for a **pilot / proof-of-concept automation system**, large enough to expose patterns while remaining manageable for experimentation and iteration.

### Columns audited:

* `ticket_id`
* `created_at`
* `channel`
* `ticket_text`
* `language`
* `true_category`
* `true_priority`

All columns align with the intended ticket schema and downstream automation goals.

---

## 2. Data Types & Schema Consistency

* All columns are currently loaded as `object` type
* `created_at` is consistently parseable into datetime format
* Text fields (`ticket_text`) preserve UTF-8 content (Arabic + English intact)

This is acceptable at the audit stage; type coercion is intentionally deferred to preprocessing (Phase 3).

---

## 3. Missing Values (Intentional Imperfection Check)

Missing values are **present, controlled, and realistic**:

| Column        | Missing Count |
| ------------- | ------------- |
| channel       | 76            |
| language      | 195           |
| true_priority | 265           |
| ticket_id     | 0             |
| created_at    | 0             |
| ticket_text   | 0             |
| true_category | 0             |

### Interpretation:

* Missing `channel` reflects incomplete logging across touchpoints
* Missing `language` reflects real-world cases where language detection fails or is skipped
* Missing `true_priority` simulates untriaged or pending tickets

No critical structural columns are missing (`ticket_id`, `created_at`, `ticket_text`), ensuring dataset usability.

---

## 4. Language Safety & Multilingual Integrity

### Language distribution:

* **English (`en`)**: 1,256 tickets
* **Arabic (`ar`)**: 983 tickets
* **Missing language label**: 195 tickets

### Observations:

* Arabic text renders correctly (RTL preserved, no encoding corruption)
* English text remains intact
* Missing language labels still contain valid text (often mixed or ambiguous)

This confirms the dataset is suitable for:

* Bilingual preprocessing pipelines
* Language detection experiments
* Realistic multilingual noise handling

---

## 5. Category Distribution

Top categories (descending):

* Network / Connectivity — 611
* Billing & Payments — 517
* Account & Authentication — 397
* Service Activation / Changes — 313
* Roaming & International Services — 251
* Other — 247
* Device / Hardware — 209
* Complaints & Service Quality — 198

### “Other” category audit:

* Represents ~9% of tickets
* Contains ambiguous, multi-issue, or underspecified complaints
* Text examples confirm genuine category uncertainty, not labeling errors

This supports later work on:

* Category confidence
* Reclassification logic
* Escalation fallback handling

---

## 6. Priority Distribution

| Priority | Count |
| -------- | ----- |
| P4       | 1,018 |
| P3       | 973   |
| P2       | 366   |
| P1       | 121   |
| Missing  | 265   |

### Interpretation:

* Distribution is heavily skewed toward P3/P4 (expected in real support systems)
* P1 tickets are rare but present
* Missing priority aligns with untriaged or newly created tickets

This mirrors operational ticket queues and avoids synthetic over-balancing.

---

## 7. Channel Distribution

| Channel | Count |
| ------- | ----- |
| app     | 564   |
| email   | 564   |
| chat    | 544   |
| web     | 505   |
| call    | 490   |
| missing | 76    |

Channels are:

* Well balanced
* Slightly biased toward digital self-service (app/chat), which is realistic
* Missing values simulate integration gaps

---

## 8. Temporal Coverage

### Date range:

* **Earliest:** 2024-12-01
* **Latest:** 2025-02-28

Covers ~3 months, sufficient to capture:

* Weekday vs weekend patterns
* Time-of-day variation
* Operational rhythm without seasonal overfitting

---

## 9. Time-of-Day Pattern

Observed distribution:

* **Peak volume:** 09:00–18:00
* **Moderate:** early evening
* **Low but non-zero:** overnight hours

This confirms realistic customer behavior and 24/7 system availability.

---

## 10. Weekday vs Weekend Behavior

* **Weekdays:** 2,481 tickets
* **Weekends:** 262 tickets

Clear volume drop on weekends, while still retaining:

* P1 and P2 tickets
* Non-zero activity across all hours

This confirms urgency is **not artificially constrained to business hours**.

---

## 11. Priority × Time Sanity Check

Urgent tickets (P1/P2):

* Appear during weekdays **and** weekends
* Occur outside business hours
* Scale proportionally with overall volume

This validates that priority assignment is logically independent of timestamp, as expected in real systems.

---

## 12. Overall Audit Conclusion

✅ Dataset structure is sound
✅ Multilingual content is preserved
✅ Missingness is intentional and realistic
✅ Temporal and priority patterns align with real support operations

**Phase 2 — Dataset Audit: PASSED**

The dataset is suitable for:

* Text preprocessing
* Language-aware modeling
* Classification and automation logic
* Intelligent routing and prioritization experiments



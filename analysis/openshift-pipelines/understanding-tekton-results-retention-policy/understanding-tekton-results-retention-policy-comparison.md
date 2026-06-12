# Understanding the Tekton Results Retention Policy - TOC Comparison

**Current Feature-Based vs. Proposed JTBD-Based Structure**

**Analysis Date:** 2026-06-11
**JTBD Records:** 6 (4 main_jobs, 2 user_stories)
**Main Jobs:** 4 (rolled up from records)
**Document Size:** 227 lines (small, focused document)

---

## Current Structure (Feature-Based)

**Understanding the Tekton Results retention policy**
- Abstract (lines 63-67)
  - Overview of Retention Policy Agent
  - Configuration via config map
- Sample YAML configuration (lines 68-136)
  - TektonConfig with retention settings
  - Field table: runAt, defaultRetention, maxRetention, policies (lines 114-136)
- **Fine-grained retention policies** (concept module, lines 143-177)
  - Policy field definitions
  - Selector types and AND logic
  - Field reference table
- Example config map with multiple policies (lines 178-226)
  - 4-policy example configuration
  - Policy application scenarios

**Total:** 1 assembly with 1 embedded concept module, organized by feature (global defaults → fine-grained policies).

---

## Proposed JTBD-Based Structure

## Set Up & Configure

**Job 1: Understand Retention Policy Architecture**

When: I need to manage how long pipeline results are kept

Personas: Cluster administrator

- **1.1. Understanding the System** `[concept]`
  → Lines 63-67: Abstract - Retention Policy Agent overview
  Source: Assembly header
  - How the agent manages pruning
  - Global vs fine-grained configuration

- **1.2. Basic Configuration Structure** `[concept]`
  → Lines 68-136: Sample YAML configuration
  Source: Assembly body
  - TektonConfig structure
  - Key fields overview

---

**Job 2: Configure Global Retention Defaults**

When: I need to set default retention periods for all results

Personas: Cluster administrator

Requires: Understanding of retention policy architecture

- **2.1. Configuration Field Reference** `[reference]`
  → Lines 114-136: Config map field definitions
  Source: Field reference table
  - runAt, defaultRetention, maxRetention, policies
  - Defaults and cron format

- **2.2. Setting Global Defaults** `[procedure]`
  → Lines 68-112: Sample TektonConfig with global settings
  Source: YAML example
  - Configure defaultRetention and runAt
  - Duration string formats

---

**Job 3: Define Fine-Grained Retention Policies**

When: I need different retention periods for specific results

Personas: Cluster administrator

Requires: Understanding of retention policy architecture, global defaults configured

- **3.1. Understanding Policy Selectors** `[concept]`
  → Lines 143-177: Fine-grained retention policies concept
  Source: Module op-fine-grained-retention-policies
  - Policy evaluation order
  - Selector types and AND logic
  - Field reference table

- **3.2. Implementing Multi-Policy Strategies** `[procedure]`
  → Lines 178-217: Example ConfigMap with multiple policies
  Source: YAML example
  - 4-policy configuration
  - Precedence demonstration

  → Lines 219-226: Policy application examples
  Source: Scenario descriptions
  - Matching scenarios by namespace/label/status
  - Fallback to defaultRetention

---

## Reference

**Job 4: Reference Retention Configuration Fields**

When: I need to understand available retention configuration options

Personas: Cluster administrator

- **4.1. Complete Field Definitions** `[reference]`
  → Lines 114-136: Config map field table
  Source: Field definitions
  - All fields with defaults
  - Deprecation warnings

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | By feature (global settings → fine-grained policies) | By user goal (understand → configure global → configure fine-grained → reference) |
| **Top-level items** | 1 assembly + 1 concept module | 4 main jobs with nested approaches |
| **Navigation** | Linear: read intro → global config → fine-grained config | Goal-directed: choose based on task (quick setup vs complex policies) |
| **Retention configuration** | Scattered across abstract, YAML, field table | Job 2 consolidates global configuration |
| **Policy configuration** | Concept module + example separate | Job 3 consolidates concept and implementation |
| **Reference material** | Field table embedded in main flow | Job 4 isolates reference for quick lookup |
| **Prerequisites** | Implicit (linear reading) | Explicit (Job 2 requires Job 1) |

---

## Hierarchy Levels

### Level 1: Main Jobs (4 total)
- Stable, outcome-focused goals
- Organized by workflow stage (Configure → Reference)
- Clean titles: "Understand Retention Policy Architecture", "Configure Global Retention Defaults"

### Level 2: User Stories (2 total)
- Implementation approaches under Job 3
- "Understanding Policy Selectors" (concept)
- "Implementing Multi-Policy Strategies" (procedure)

### Level 3: References
- Line numbers from source document
- Topic type tags: `[concept]`, `[procedure]`, `[reference]`

---

## Example Consolidation

### Example: Retention Configuration (Fragmented → Consolidated)

**Current (Fragmented):**
- Abstract (lines 63-67): High-level retention overview
- YAML example (lines 68-136): Configuration structure + field table
- Concept module (lines 143-177): Fine-grained policy details
- Example config map (lines 178-226): Multi-policy implementation

**User Pain Point:** To configure retention, users must read linearly through abstract, extract fields from YAML example, understand concept module, then study example. Reference material (field table) is embedded in YAML example section.

**Proposed (Consolidated):**
- **Job 1:** Understand Retention Policy Architecture
  - Abstract overview + basic YAML structure
- **Job 2:** Configure Global Retention Defaults
  - Field definitions + global configuration procedure
- **Job 3:** Define Fine-Grained Retention Policies
  - Policy concept (selectors, AND logic) + multi-policy implementation
- **Job 4:** Reference Retention Configuration Fields
  - Isolated field table for quick lookup

**Benefit:** Clear separation between learning (Job 1), configuring global settings (Job 2), configuring fine-grained policies (Job 3), and looking up fields (Job 4). Users can go directly to Job 2 for simple setup or Job 3 for complex policies without re-reading foundational material.

---

## Navigation Improvement Metrics

**Current:** Browse 4 sections linearly (abstract → YAML → concept → example) to configure retention

**Proposed:** Navigate 4 jobs → choose configuration path:
- Simple setup: Job 1 → Job 2
- Complex policies: Job 1 → Job 3
- Quick lookup: Job 4

**Reduction:** 0% reduction in top-level items (small document already well-structured)

**Benefit:** 
- Find global configuration in 1 click (Job 2) vs 3 sections (abstract + YAML + field table)
- Find policy configuration in 1 click (Job 3) vs 2 sections (concept + example)
- Find field reference in 1 click (Job 4) vs navigating to field table within YAML section

**Quick lookup improvement:** 
- Field definitions: Direct access via Job 4 instead of scrolling to line 114 within YAML section
- Policy examples: Consolidated in Job 3.2 instead of separate from concept in Job 3.1

---

## Workflow Coverage Comparison

| Stage | Current | Proposed | Gap Status |
|-------|---------|----------|------------|
| Configure | ✅ Main content | ✅ Jobs 1, 2, 3 | Well-covered |
| Reference | ✅ Field table | ✅ Job 4 | Elevated to dedicated job |
| Monitor | ❌ Missing | ❌ Missing | Gap remains |
| Troubleshoot | ❌ Missing | ❌ Missing | Gap remains |
| Upgrade | ❌ Missing | ❌ Missing | Gap remains (maxRetention deprecation) |

### Coverage Summary

**Current structure gaps:** Monitor (pruning job execution), Troubleshoot (policy issues), Upgrade (maxRetention migration)

**Proposed structure gaps:** Same gaps remain

**Gaps NOT addressed by restructure:** Monitor, Troubleshoot, Upgrade (would require new content)

### Recommendations for Gap Closure

| Gap | Recommendation | Priority |
|-----|----------------|----------|
| Monitor | Add section on viewing pruning cron job logs, checking retention policy status | Medium |
| Troubleshoot | Add troubleshooting section for policy matching failures, common pruning errors | Medium |
| Upgrade | Add migration procedure from maxRetention to defaultRetention | Low (field is deprecated but still functional) |

---

## UX Research Alignment

**Note:** No UX research extension fields were populated for this document. The following alignment is based on documentation best practices and common user pain points.

### Potential Pain Points Addressed by Restructure

| Pain Point (Inferred) | How New Structure Helps |
|----------------------|------------------------|
| "Must read entire document to understand simple global config" | Job 2 isolates global configuration with direct path from Job 1 |
| "Field definitions buried in YAML example section" | Job 4 elevates reference material to dedicated job for quick lookup |
| "Concept and implementation examples separated" | Job 3 consolidates policy concept (3.1) and implementation (3.2) in one place |

### Navigation Pattern Improvement

| Task | Current Navigation | Proposed Navigation | Improvement |
|------|-------------------|---------------------|-------------|
| Set simple global retention | Read abstract → scroll to YAML → find field table → configure | Job 1 → Job 2 (field ref + procedure) | Faster access to field definitions |
| Create namespace-based policy | Read abstract → read concept module → read example → configure | Job 1 → Job 3 (concept + example together) | Reduced context switching |
| Look up field default | Scroll to line 114 in field table | Jump to Job 4 | Direct reference access |

---

## Success Criteria Assessment

**Strengths of proposed structure:**
- Clear task-based navigation (understand → configure → reference)
- Reference material isolated for quick lookup
- Explicit prerequisite chain (Job 1 → Job 2 → Job 3)
- Concept and implementation consolidated (Job 3.1 + 3.2)

**Limitations:**
- Small document already well-organized, restructure provides incremental improvement
- Gap coverage unchanged (would require new content)
- Only 4 jobs (near minimum for JTBD restructuring to add value)

**Recommendation:** Proposed structure improves navigation for task-specific access patterns (global config, policy config, quick reference) but provides limited benefit over current linear structure due to document's small size and focus.

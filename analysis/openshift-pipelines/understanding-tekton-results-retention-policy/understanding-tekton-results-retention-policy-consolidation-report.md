# Understanding the Tekton Results Retention Policy — Consolidation Report

**Document:** understanding-tekton-results-retention-policy-self-managed-reduced.adoc
**JTBD Records:** 6 pre-consolidated (4 main_jobs, 2 user_stories) → 4 final jobs (no adjustments needed)

---

## Executive Summary

### What's Changing

The current document is organized by feature progression: introduction to retention policies → global configuration → fine-grained policies. While logical for linear reading, this structure embeds reference material (field definitions) within procedural sections and separates conceptual understanding from implementation examples.

The proposed JTBD-based structure reorganizes by user goal: understand the system → configure global defaults → configure fine-grained policies → reference fields. This separation allows users to jump directly to their task (simple global configuration vs complex policy setup) without re-reading foundational material, and elevates reference material to a dedicated job for quick lookup.

Given the document's small size (227 lines, 4 main sections), the restructuring provides incremental rather than transformational improvement. The primary value is in task-based navigation and explicit prerequisite chains.

### Key Improvements

- **Reference isolation:** Field definitions table elevated from embedded position (line 114 within YAML section) to dedicated Job 4 for direct lookup access
- **Concept-implementation consolidation:** Policy selectors concept (lines 143-177) and multi-policy examples (lines 178-226) unified under Job 3 with clear progression (3.1 concept → 3.2 implementation)
- **Task-based access paths:** Users needing simple global configuration can follow Job 1 → Job 2 path; users needing complex policies follow Job 1 → Job 3 path
- **Explicit prerequisites:** Job 2 explicitly requires Job 1; Job 3 requires Jobs 1 and 2, making configuration sequence clear
- **Configuration scope clarity:** Job 2 (global) vs Job 3 (fine-grained) distinction makes configuration scope explicit in job titles

---

## Current Structure (Feature-Based)

**Understanding the Tekton Results retention policy** (Assembly)

- **Abstract** (lines 63-67) — Overview of Retention Policy Agent, config map location
- **Sample YAML configuration** (lines 68-136)
  - TektonConfig example with retention settings (lines 68-112)
  - Field table: runAt, defaultRetention, maxRetention, policies (lines 114-136)
- **Fine-grained retention policies** (Concept module, lines 143-177)
  - Policy evaluation order and selector types
  - Field reference table for policy fields
- **Example config map with multiple policies** (lines 178-226)
  - 4-policy ConfigMap example (lines 178-217)
  - Policy application scenarios (lines 219-226)

**Total:** 1 assembly with 1 embedded concept module (4 main content sections), organized by feature progression (global → fine-grained).

---

## Proposed JTBD-Based Structure

### Quick Overview

- **Set Up & Configure**
  - Job 1: Understand Retention Policy Architecture
  - Job 2: Configure Global Retention Defaults
  - Job 3: Define Fine-Grained Retention Policies
- **Reference**
  - Job 4: Reference Retention Configuration Fields

---

### Detailed Job Descriptions

#### Set Up & Configure

**Job 1: Understand Retention Policy Architecture**

*When I need to manage how long pipeline results are kept, I want to understand the retention policy system, so I can configure data retention according to my organization's needs.*

Prerequisites: None

- **1.1. Retention Policy Agent Overview** `[concept]`
  - Lines 63-67 (Assembly abstract): How the Retention Policy Agent manages database pruning, global defaults vs fine-grained rules, configuration via config map
- **1.2. Basic Configuration Structure** `[concept]`
  - Lines 68-136 (Sample YAML): TektonConfig structure, key fields overview (defaultRetention, policies, runAt)

---

**Job 2: Configure Global Retention Defaults**

*When I need to set default retention periods for all results, I want to configure global retention settings, so I can establish baseline data retention without defining policies for every namespace.*

Prerequisites: Understanding of retention policy architecture (Job 1)

- **2.1. Configuration Field Reference** `[reference]`
  - Lines 114-136 (Field table): runAt (cron schedule), defaultRetention (fallback period), maxRetention (deprecated), policies (fine-grained list)
  - Context: Use this section for quick field lookup during configuration
- **2.2. Setting Global Defaults Procedure** `[procedure]`
  - Lines 68-112 (Sample TektonConfig): Configure defaultRetention (30d, 24h, or numeric), set runAt cron schedule, understand duration string formats
  - Context: Follow this procedure for organization-wide baseline retention

---

**Job 3: Define Fine-Grained Retention Policies**

*When I need different retention periods for specific results, I want to define fine-grained retention policies based on namespaces, labels, annotations, or statuses, so I can optimize storage costs while retaining critical results longer.*

Prerequisites: Understanding of retention policy architecture (Job 1), global defaults configured (Job 2)

- **3.1. Understanding Policy Selectors** `[concept]`
  - Lines 143-177 (Fine-grained retention policies concept): Policy evaluation order (first match wins), selector fields (matchNamespaces, matchLabels, matchAnnotations, matchStatuses), AND logic across selectors, omitting selectors to match all
  - Context: Read this section before creating complex multi-criteria policies
- **3.2. Implementing Multi-Policy Strategies** `[procedure]`
  - Lines 178-217 (Example ConfigMap): 4-policy configuration (retain-critical-failures-long-term, retain-annotated-for-debug, default-production-policy, short-term-ci-retention)
  - Lines 219-226 (Policy application examples): Matching scenarios by namespace/label/status combinations, precedence demonstration, fallback to defaultRetention
  - Context: Use these examples as templates for your organization's retention strategy

---

#### Reference

**Job 4: Reference Retention Configuration Fields**

*When I need to understand available retention configuration options, I want to reference field definitions and defaults, so I can configure retention settings correctly.*

Prerequisites: None

- **4.1. Complete Field Definitions** `[reference]`
  - Lines 114-136 (Field table): All config map fields with descriptions and defaults, deprecation warnings (maxRetention), cron format requirements, duration string formats
  - Context: Quick lookup for field syntax and defaults during configuration

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | By feature progression (global → fine-grained) | By user goal (understand → configure → reference) |
| **Top-level items** | 4 sections (abstract, YAML, concept, example) | 4 main jobs with nested approaches |
| **Navigation** | Linear reading (intro → config → policy) | Goal-directed (choose job based on task) |
| **Reference material** | Field table embedded in YAML section (line 114) | Job 4 isolates reference for direct access |
| **Configuration scope** | Implicit (global in YAML, fine-grained in module) | Explicit (Job 2 = global, Job 3 = fine-grained) |
| **Concept-implementation link** | Separated (concept module, then example config) | Consolidated (Job 3.1 concept → 3.2 implementation) |
| **Prerequisites** | Implicit (linear structure) | Explicit (Job 2 requires Job 1, Job 3 requires Jobs 1 & 2) |

### Job List Adjustments from Suggested Input

The suggested 4 main jobs required **no adjustments** for the following reasons:

1. **Jobs are correctly scoped:** Each job represents a stable, outcome-focused goal (understand, configure global, configure fine-grained, reference)
2. **No consolidation needed:** Jobs cover distinct tasks with minimal overlap
3. **Granularity is appropriate:** 4 jobs for a 227-line document is reasonable given configuration complexity (global vs fine-grained policies)
4. **User stories properly nested:** The 2 user stories (3.1 Understanding Policy Selectors, 3.2 Implementing Multi-Policy Strategies) are correctly nested under Job 3

**Final job count: 4** (no reduction from suggested 4 main jobs).

---

## Consolidation Examples

### Example 1: Reference Material (Embedded → Isolated)

**Current (Fragmented):**
- Field definitions table embedded within "Sample YAML configuration" section (lines 114-136)
- Users must scroll through YAML example to reach field table
- No direct navigation to reference material

**User Pain Point:** When configuring retention, users need to reference field defaults and syntax. Current structure requires navigating to line 114 within a larger YAML example section, making quick lookup difficult.

**Proposed (Consolidated):**
- **Job 4: Reference Retention Configuration Fields**
  - 4.1. Complete Field Definitions (lines 114-136)
  - Direct navigation to reference material
  - Isolated from procedural content

**Benefit:** Users can jump directly to Job 4 for quick field lookup without navigating through YAML examples or scrolling to embedded table. Reference material is elevated to a dedicated job with clear purpose.

---

### Example 2: Policy Configuration (Concept-Implementation Separated → Unified)

**Current (Fragmented):**
- Concept module "Fine-grained retention policies" (lines 143-177) explains selectors and AND logic
- Example config map with multiple policies (lines 178-226) shows implementation
- User must read concept, then jump to separate example section

**User Pain Point:** To configure fine-grained policies, users must understand selector concepts (module), then switch context to implementation examples (separate section). The separation makes it harder to connect concept to practice.

**Proposed (Consolidated):**
- **Job 3: Define Fine-Grained Retention Policies**
  - 3.1. Understanding Policy Selectors (concept - lines 143-177)
  - 3.2. Implementing Multi-Policy Strategies (procedure - lines 178-226)
  - Clear progression: learn concept → see implementation

**Benefit:** Job 3 consolidates policy concept and implementation in one place with explicit progression (3.1 → 3.2). Users can understand selectors and immediately see implementation examples without switching between disconnected sections.

---

## Content Gaps Identified

| Gap | JTBD Reference | Current Coverage | Impact |
|-----|---------------|-----------------|--------|
| Pruning job monitoring | Job 1, Job 2 | Not covered | **Medium** — Users cannot verify retention policies are executing correctly; likely causes support questions about "why aren't old results being pruned?" |
| Policy matching troubleshooting | Job 3 | Not covered | **Medium** — Users cannot debug when policies don't match expected results; likely causes misconfiguration and unintended data retention |
| maxRetention migration procedure | Job 2 | Deprecation mentioned (line 129) but no migration steps | **Low** — Field is deprecated but still functional; users need migration guidance for future-proofing |
| Retention policy validation | Job 3 | Not covered | **Medium** — Users cannot verify policy selectors are correct before applying; likely causes trial-and-error configuration |
| Cron schedule examples | Job 2 | Generic cron format mentioned (line 121) | **Low** — Users may struggle with cron syntax; examples would reduce configuration errors |
| Storage impact estimation | Job 2, Job 3 | Not covered | **Low** — Users cannot estimate storage savings from retention changes; helpful for capacity planning but not critical |
| Retention policy rollback | Job 2, Job 3 | Not covered | **Medium** — Users who accidentally set aggressive retention cannot recover pruned data; guidance on safe testing would prevent data loss |

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 4 sections | 4 jobs | No change (already compact) |
| Sections to browse for global configuration | 3 (abstract + YAML + field table) | 1 (Job 2) | ~67% reduction |
| Sections to browse for policy configuration | 2 (concept module + example) | 1 (Job 3) | ~50% reduction |
| Clicks to reference field definitions | Navigate to line 114 in YAML section | 1 (Job 4) | Direct access |
| Prerequisite clarity | Implicit (linear reading) | Explicit (Job 2 requires Job 1, Job 3 requires Jobs 1 & 2) | Prerequisites visible in job headers |
| Configuration scope clarity | Inferred from section titles | Explicit in job titles (Job 2 = global, Job 3 = fine-grained) | Scope clear from TOC |

**Final job count: 4** (no reduction needed from suggested 4 main jobs). The document's small size and focused scope make 4 jobs appropriate — further consolidation would reduce task-based navigation value.

**Consolidation rationale:** No merges required. Each job represents a distinct user goal:
- Job 1: Foundational understanding
- Job 2: Global configuration task
- Job 3: Fine-grained configuration task
- Job 4: Reference lookup

---

## UX Research Alignment

**Note:** No UX research extension fields were populated for this document. The following alignment is based on inferred user needs from documentation structure and common configuration pain points.

### Inferred Pain Points Addressed by Restructure

| Pain Point (Inferred) | How New Structure Helps |
|----------------------|------------------------|
| "I just need to set a simple 30-day retention, why must I read about fine-grained policies?" | Job 2 provides direct path to global configuration; Job 3 is clearly marked for users needing fine-grained control |
| "Where's the field reference? I keep scrolling through YAML examples" | Job 4 elevates field table to dedicated reference job with direct navigation |
| "I read the concept module but where are the examples?" | Job 3 consolidates concept (3.1) and implementation (3.2) in one place |
| "What order should I configure things?" | Explicit prerequisites: Job 1 (understand) → Job 2 (global) → Job 3 (fine-grained if needed) |

### Configuration Workflow Visibility

The new structure makes two common configuration workflows explicit:

| Workflow | Current Navigation | Proposed Navigation | Improvement |
|----------|-------------------|---------------------|-------------|
| **Simple setup** (global retention only) | Read abstract → find YAML → locate field table → configure defaultRetention | Job 1 (overview) → Job 2 (global config with field ref) | Reduced from 3 sections to 2 jobs |
| **Complex setup** (namespace/label policies) | Read abstract → YAML → concept module → example config → configure | Job 1 (overview) → Job 3 (concept + implementation) | Concept and example unified |

---

## Document Statistics

**Workflow Coverage:**
- Configure: 3 jobs (Jobs 1, 2, 3)
- Reference: 1 job (Job 4)
- Monitor: Gap identified (no pruning job observability)
- Troubleshoot: Gap identified (no policy troubleshooting)
- Upgrade: Gap identified (maxRetention migration)

**Main Jobs:** 4
**User Stories/Paths:** 2 (nested under Job 3)
**Source Sections:** 4 (abstract, YAML, concept module, example config)
**Platform/Tool Variations:** 1 (TektonConfig only)
**Total Lines:** 227 (small, focused document)
**Topic Types:**
- Concept: 3 sections (abstract, basic config structure, policy selectors)
- Procedure: 2 sections (global defaults, multi-policy implementation)
- Reference: 1 section (field definitions)

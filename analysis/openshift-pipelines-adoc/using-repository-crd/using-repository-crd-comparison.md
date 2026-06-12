# Using the Repository Custom Resource - TOC Comparison

**Current Feature-Based vs. Proposed JTBD-Based Structure**

**Analysis Date:** 2026-06-11
**JTBD Records:** 13 (12 user stories rolled up into 5 main jobs)
**Main Jobs:** 5
**Coverage:** 100% enhanced schema

---

## Current Structure (Feature-Based)

Using the Repository custom resource
- Creating the Repository custom resource
- Creating the global Repository custom resource
- Setting concurrency limits
- Changing the source branch for the pipeline definition
- Custom parameter expansion

**Total:** 1 assembly with 5 procedural/reference modules, organized by Repository CR features and settings.

**Organizing Principle:** By Repository CR feature area (creation, global configuration, settings)

---

## Proposed JTBD-Based Structure

### Quick Overview

- **Set Up & Configure**
  - Job 1: Create a Repository CR That Matches Events from My Git Repository
  - Job 2: Create a Global Repository CR with Shared Configuration
  - Job 3: Set Concurrency Limits on a Repository CR
  - Job 5: Define Custom Parameters in the Repository CR

- **Secure Your Environment**
  - Job 4: Configure the Repository CR to Fetch Pipeline Definitions from the Default Branch

**Organizing Principle:** By user goal and workflow stage (Configure, Secure)

---

### Detailed Job Descriptions

#### Set Up & Configure

**Job 1: Create a Repository CR That Matches Events from My Git Repository**

*When I need to enable Pipelines as Code for my source repository, I want to create a Repository CR that matches events from my Git repository, so I can automate pipeline runs triggered by repository events.*

Prerequisites: Namespace created for pipeline runs, access to create CRs in the target namespace

- **1.1. Create Repository CR Using tkn pac CLI or kubectl** `[procedure]`
  - Lines 80-96: Creating the Repository custom resource (Module op-creating-repository-cr.adoc)
  - Define repository URL and namespace
  - Use kubectl create or tkn pac CLI
  - Context: Quick method for connecting single Git repository to Pipelines as Code

- **1.2. Use Explicit Namespace Targeting for Multi-Repository Scenarios** `[procedure]`
  - Lines 98-103: Creating the Repository custom resource (Module op-creating-repository-cr.adoc)
  - Add pipelinesascode.tekton.dev/target-namespace annotation
  - Context: Required in multi-tenant environments to prevent unauthorized pipeline runs

---

**Job 2: Create a Global Repository CR with Shared Configuration**

*When I manage multiple repositories with common settings, I want to create a global Repository CR with shared configuration, so I can avoid repeating the same settings across multiple repository-specific CRs.*

Prerequisites: Administrator access to openshift-pipelines namespace, common settings identified (secrets, git provider config)

- **2.1. Create Global Repository CR Named pipelines-as-code** `[procedure]`
  - Lines 134-164: Creating the global Repository custom resource (Module op-creating-global-repository-cr.adoc)
  - Create Repository CR named "pipelines-as-code" in openshift-pipelines namespace
  - Include common git_provider and webhook_secret settings
  - All subsequently created Repository CRs inherit these settings
  - Context: Technology Preview feature for centralized configuration management

---

**Job 3: Set Concurrency Limits on a Repository CR**

*When I need to control resource usage for pipeline runs, I want to set concurrency limits on a Repository CR, so I can prevent too many pipeline runs from executing simultaneously and overwhelming cluster resources.*

Prerequisites: Repository CR created, understanding of cluster resource capacity

- **3.1. Configure concurrency_limit in Repository CR Spec** `[procedure]`
  - Lines 179-196: Setting concurrency limits (Module op-setting-concurrency-limits-in-repository-crd.adoc)
  - Add concurrency_limit field to Repository CR spec
  - Pipeline runs execute in alphabetical order when queued
  - Context: Essential for preventing resource exhaustion when multiple pipeline runs match an event

---

**Job 5: Define Custom Parameters in the Repository CR**

*When I need to manage pipeline parameters centrally without modifying pipeline runs in Git, I want to define custom parameters in the Repository CR, so I can control values like registry URLs or account identifiers from the Repository CR location.*

Prerequisites: Pipeline runs using custom parameters, understanding of difference between Tekton parameters and custom parameters

- **5.1. Define Static Custom Parameters** `[procedure]`
  - Lines 254-280: Custom parameter expansion (Module op-custom-parameter-expansion.adoc)
  - Add params field with name and value or secret_ref
  - Values replace custom parameters in pipeline runs and remote tasks
  - Context: Use for administrator-managed values that should not be in Git repository

- **5.2. Define Event-Specific Parameters with CEL Filters** `[procedure]`
  - Lines 288-304: Custom parameter expansion (Module op-custom-parameter-expansion.adoc)
  - Add filter field with CEL expression to params
  - First matching filter wins
  - Context: Use when parameter values differ between event types (push vs pull request)

---

#### Secure Your Environment

**Job 4: Configure the Repository CR to Fetch Pipeline Definitions from the Default Branch**

*When I need to enforce pipeline definition review before execution, I want to configure the Repository CR to fetch pipeline definitions from the default branch, so I can ensure all pipeline changes are reviewed and merged before they can execute.*

Prerequisites: Repository CR created, default branch defined in Git repository, merge review process established

- **4.1. Set pipelinerun_provenance to default_branch** `[procedure]`
  - Lines 211-223: Changing the source branch for the pipeline definition (Module op-changing-source-branch-in-repository-crd.adoc)
  - Add settings.pipelinerun_provenance: "default_branch" to Repository CR
  - Overrides default behavior of fetching from event branch
  - Context: Security precaution ensuring merge reviews verify all pipeline definition changes

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | By Repository CR feature area (creation types, settings) | By user goal and workflow stage (Configure, Secure) |
| **Top-level items** | 5 modules (procedural/reference) | 5 main jobs with 8 nested approaches |
| **Security content** | Mixed with configuration (setting within "Changing source branch") | Dedicated security job (Job 4) |
| **Global vs specific** | Separate sections (Creating vs Creating global) | Consolidated under configuration goals (Jobs 1 & 2) |
| **Parameters** | Single concept module with examples | Structured job with static vs event-specific approaches (Job 5.1 vs 5.2) |
| **Namespace targeting** | Buried in note at end of creation section | Elevated to dedicated approach (Job 1.2) with security context |
| **Prerequisites visibility** | Stated in procedure sections | Explicit prerequisite chains showing Job 2 before repository-specific CRs |

### Job List Adjustments from Suggested Input

The suggested 13 jobs (from JSONL records) were consolidated to **5 jobs** for the following reasons:

1. **Jobs 1 and 3 ("Create Repository CR" user stories) merged** → Both user stories (basic creation and namespace targeting) are approaches within the same main job of creating a Repository CR
2. **Jobs 4 and 5 ("Create global Repository CR" user stories) merged** → User story about creating global CR absorbed into main job 2 as single approach
3. **Jobs 6 and 7 ("Set concurrency limits" user stories) merged** → User story about configuring concurrency_limit absorbed into main job 3 as single approach
4. **Jobs 8 and 9 ("Configure pipeline provenance" user stories) merged** → User story about setting pipelinerun_provenance absorbed into main job 4 as single approach
5. **Jobs 10, 11, and 12 ("Define custom parameters" user stories) merged** → Three user stories (main job, static parameters, event-specific parameters) consolidated into main job 5 with two approaches (5.1 static, 5.2 event-specific)

**Consolidation Rationale:** Original JSONL records contained both main_job granularity records and user_story granularity records. The proposed structure elevates true main jobs to Level 1 and nests user stories as approaches (Level 2), following JTBD TOC guidelines.

---

## Consolidation Examples

### Example 1: Custom Parameters (2 implementation approaches → 1 unified job)

**Current (Fragmented):**
- Section "Custom parameter expansion" (lines 237-306): Single concept module mixing static values and CEL filters
- Static parameter example at lines 254-266
- Secret reference example at lines 268-280
- CEL filter example at lines 288-304

Users must parse a 69-line concept module to understand when to use static vs event-specific parameters.

**Proposed (Consolidated):**
- **Job 5: Define Custom Parameters in the Repository CR**
  - 5.1. Define Static Custom Parameters (lines 254-280)
  - 5.2. Define Event-Specific Parameters with CEL Filters (lines 288-304)

**Benefit:** Clear separation between static and event-conditional parameter approaches with explicit "Context:" guidance on when to use each.

---

### Example 2: Security Configuration (scattered security notes → dedicated security job)

**Current (Fragmented):**
- Security note about namespace targeting buried in note at lines 98-103 (Creating Repository CR section)
- Security rationale for pipeline provenance buried in note at lines 225-228 (Changing source branch section)

Users must read two separate sections and extract security implications from notes.

**Proposed (Consolidated):**
- **Job 1.2:** Use Explicit Namespace Targeting (security approach elevated)
- **Job 4:** Configure the Repository CR to Fetch Pipeline Definitions from the Default Branch (dedicated security job)
  - "Why:" field explicitly states security benefit
  - "Timing:" field warns about configuring before accepting external contributions

**Benefit:** Security concerns are findable and explicit, not buried in notes within feature documentation.

---

### Example 3: Repository CR Creation (basic + global → 2 distinct jobs with clear prerequisites)

**Current (Fragmented):**
- Section "Creating the Repository custom resource" (lines 76-104)
- Section "Creating the global Repository custom resource" (lines 113-164)

Both titled "Creating..." but serve fundamentally different purposes (single repo enablement vs centralized configuration).

**Proposed (Consolidated):**
- **Job 1:** Create a Repository CR That Matches Events from My Git Repository
  - Focused on single repository enablement
- **Job 2:** Create a Global Repository CR with Shared Configuration
  - Focused on multi-repository centralized management
  - "Timing:" field explicitly states this should be done BEFORE creating repository-specific CRs

**Benefit:** Clear distinction between single-repository and global configuration patterns with explicit prerequisite guidance.

---

## Content Gaps Identified

| Gap | JTBD Reference | Current Coverage | Impact |
|-----|---------------|-----------------|--------|
| Repository CR status observation | Monitoring stage | Assembly abstract mentions "Show the last pipeline run status for a repository" (line 68) but no procedure provided | **High** — Users have no guidance for viewing Repository CR state or troubleshooting event matching |
| Event matching troubleshooting | Troubleshoot stage | No content | **High** — Common issue: events not matching, no troubleshooting steps provided |
| Complete Repository CR field reference | Reference stage | Fields mentioned in context of procedures but no comprehensive reference | **Medium** — Users must extract field details from procedure examples |
| Namespace conflict resolution | Troubleshoot stage | Note mentions "oldest one" wins behavior (line 101) but no troubleshooting for conflicts | **Medium** — Users may create conflicting Repository CRs without understanding resolution |
| Git provider-specific configuration | Configure stage | Example shows GitLab (lines 153-160) but other providers not covered | **Medium** — Users need provider-specific webhook and secret configuration examples |
| Custom parameter naming conflicts | Troubleshoot stage | Note mentions "last parameter" wins (line 286) but no guidance on avoiding conflicts | **Low** — Edge case but could cause confusion with multiple params |

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 5 modules | 5 jobs | Same count but reorganized by goal |
| Sections to browse for "securing pipeline definitions" | 1 module + extract security note | 1 dedicated job (Job 4) | Security concerns elevated, not buried |
| Sections to browse for "parameter management" | 1 concept module (69 lines) | 1 job, 2 approaches with clear context | ~50% reduction in content to parse |
| Clicks to find "namespace targeting" | Browse creation section → find note at lines 98-103 | Navigate to Job 1.2 directly | Direct navigation vs buried note |
| Clicks to find "global vs specific configuration" | Compare two "Creating" sections | Jobs 1 and 2 with explicit prerequisite chain | Relationship made explicit |

**Final job count: 5** (reduced from suggested 13 user story records). All user-story-granularity records consolidated as approaches under appropriate main jobs, following JTBD hierarchy (Job → User Story/Approach → Procedure).

---

## Workflow Coverage Comparison

| Stage | Current | Proposed | Gap Status |
|-------|---------|----------|------------|
| Get Started | ⚠️ Abstract only | ⚠️ Abstract only | Remains scattered |
| Configure | ✅ Modules 1, 2, 3, 5 | ✅ Jobs 1, 2, 3, 5 | Reorganized by goal |
| Secure | ⚠️ Mixed in modules | ✅ Job 4 (dedicated) | Elevated and findable |
| Monitor | ❌ Missing | ❌ Missing | Gap remains |
| Troubleshoot | ❌ Missing | ❌ Missing | Gap remains |
| Reference | ⚠️ Scattered | ⚠️ Quick reference only | Partial improvement |

### Coverage Summary

**Current structure gaps:** Get Started (no quickstart), Monitor (no status observation), Troubleshoot (no procedures), Reference (no comprehensive spec)

**Proposed structure gaps:** Get Started (no quickstart), Monitor (no status observation), Troubleshoot (no procedures), Reference (quick reference table only)

**Gaps addressed by restructure:** Security (elevated from notes to dedicated job)

**Gaps remaining:** Monitor, Troubleshoot, Reference, Get Started

### Recommendations for Gap Closure

| Gap | Recommendation | Priority |
|-----|----------------|----------|
| Monitor | Add section on viewing Repository CR status and last pipeline run information | High |
| Troubleshoot | Add common issues: event not matching, namespace conflicts, parameter resolution | High |
| Reference | Add comprehensive Repository CR spec reference table | Medium |
| Get Started | Add quickstart example showing end-to-end repository connection | Medium |

---

## Coverage Indicators

| Symbol | Meaning |
|--------|---------|
| ✅ | Stage fully covered with dedicated content |
| ⚠️ | Partial coverage - content exists but scattered or limited |
| ❌ | Stage not covered - content gap identified |

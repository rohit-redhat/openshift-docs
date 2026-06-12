# Using the Repository Custom Resource — Consolidation Report

**Document:** using-repository-crd.adoc
**JTBD Records:** 5 pre-consolidated main jobs → 4 final jobs (after merging)

---

## Executive Summary

### What's Changing

The current "Using the Repository Custom Resource" document is organized as a flat list of Repository CR features — creating CRs, setting concurrency limits, changing source branches, and custom parameter expansion. Each feature is presented as a standalone topic with no clear indication of user goals, workflow sequence, or relationships between features.

This feature-focused organization causes three pain points: (1) Users must read all sections to understand which features apply to their use case; (2) Related features (basic vs. global Repository CR creation) are not clearly grouped as alternative approaches to the same goal; (3) Security-critical features (default branch provenance) are not elevated as distinct security jobs.

The proposed JTBD-based restructure organizes content by user goals and workflow stages. Repository setup options are grouped under a single "Connect Source Repository" job with two approaches. Resource control and security features are elevated to distinct jobs that explain the "why" (prevent resource exhaustion, enforce code review) before the "how". Configuration management is consolidated under a dedicated job with progressive complexity (basic parameters, then conditional expansion).

### Key Improvements

- **Repository setup consolidation:** 2 separate creation sections → 1 job with 2 approaches (basic vs. global)
- **Security elevation:** Default branch provenance moved from buried configuration to dedicated security job
- **Workflow clarity:** Content grouped into 3 workflow phases (Setup, Control, Configure) vs. flat feature list
- **Prerequisites visibility:** Prerequisites shown explicitly for 4 jobs vs. 1 section in current structure
- **Purpose-driven navigation:** Users find content by goal ("enforce code review") vs. feature name ("changing source branch")
- **Configuration guidance:** Custom parameters grouped by complexity (basic → conditional) vs. single monolithic section

---

## Current Structure (Feature-Based)

**Using the Repository Custom Resource** (Assembly)

- Creating the Repository custom resource — How to create a basic Repository CR in target namespace
- Creating the global Repository custom resource — How to create a global Repository CR in openshift-pipelines namespace (Technology Preview)
- Setting concurrency limits — How to use concurrency_limit spec to control simultaneous pipeline runs
- Changing the source branch for the pipeline definition — How to set pipelinerun_provenance to fetch from default branch
- Custom parameter expansion — How to define custom parameters in Repository CR for PipelineRun expansion

**Total:** 1 assembly with 5 flat sections, organized by Repository CR features.

---

## Proposed JTBD-Based Structure

### Quick Overview

- **Set Up Repository Integration**
  - Job 1: Connect Source Repository to Pipeline System
- **Control Pipeline Execution**
  - Job 2: Limit Concurrent Pipeline Runs
  - Job 3: Enforce Pipeline Code Review
- **Manage Pipeline Configuration**
  - Job 4: Inject Centralized Configuration into Pipeline Runs

### Detailed Job Descriptions

#### Set Up Repository Integration

**Job 1: Connect Source Repository to Pipeline System**

*When I need to connect my source code repository to the pipeline system, I want to create a Repository CR that matches incoming events to my repository URL, so I can automatically trigger pipeline runs when code changes occur*

Prerequisites: None (foundational setup)

- **1.1. Basic Repository Setup** `[reference]`
  - Creating the Repository custom resource (modules/op-creating-repository-cr.adoc): Create Repository CR in target namespace with repository URL for event matching. Namespace-scoped CR prevents cross-namespace pipeline execution.
  - Context: Use this approach for single-repository setup or when each repository needs unique configuration.
- **1.2. Global Repository Configuration** `[procedure]`
  - Creating the global Repository custom resource (modules/op-creating-global-repository-cr.adoc): Create global Repository CR in openshift-pipelines namespace to provide default settings (GitLab secrets) for all repositories.
  - Prerequisites: Administrator access to openshift-pipelines namespace, oc CLI access
  - Context: Use this approach to reduce configuration repetition across many repositories with shared webhook secrets (Technology Preview).

#### Control Pipeline Execution

**Job 2: Limit Concurrent Pipeline Runs**

*When multiple pipeline runs could be triggered simultaneously for my repository, I want to limit the number of concurrent executions, so I can prevent resource exhaustion and ensure orderly processing of events*

Prerequisites: Existing Repository CR

- **2.1. Set Concurrency Limit** `[reference]`
  - Setting concurrency limits (modules/op-setting-concurrency-limits-in-repository-crd.adoc): Use concurrency_limit spec to define maximum simultaneous runs. Pipeline runs queue and execute in alphabetical order when limit is reached.
  - Context: Apply when repository receives high event volume (multiple PRs) or when .tekton directory contains many pipeline definitions.

**Job 3: Enforce Pipeline Code Review**

*When I need to ensure pipeline definitions are reviewed before execution, I want to configure the Repository CR to fetch pipeline definitions from the default branch instead of the event-triggering branch, so I can enforce code review on all pipeline changes before they run*

Prerequisites: Existing Repository CR, Pipeline definitions merged into default branch

- **3.1. Configure Pipeline Definition Source** `[reference]`
  - Changing the source branch for the pipeline definition (modules/op-changing-source-branch-in-repository-crd.adoc): Set pipelinerun_provenance to "default_branch" to fetch definitions from default branch (main/master/trunk) rather than PR branch.
  - Context: Security precaution to prevent execution of unreviewed or malicious pipeline code from pull requests. Requires merge review process.

#### Manage Pipeline Configuration

**Job 4: Inject Centralized Configuration into Pipeline Runs**

*When I need to inject environment-specific or administratively-controlled values into pipeline runs, I want to define custom parameters in the Repository CR that expand within PipelineRun resources, so I can manage configuration centrally without modifying pipeline definitions in Git*

Prerequisites: Existing Repository CR, Understanding of PipelineRun parameter requirements

- **4.1. Define Custom Parameters** `[concept]`
  - Custom parameter expansion (modules/op-custom-parameter-expansion.adoc, lines 238-267): Use params field in Repository CR to define literal values or Kubernetes secret references. Parameters replace {{ .params.name }} in PipelineRun resources.
  - Use cases: Registry URLs varying by environment, account UUIDs managed by administrators, endpoint URLs
  - Context: Use when environment-specific values should not be stored in Git. Note: Avoid when Tekton PipelineRun parameters would suffice.
- **4.2. Apply Conditional Parameter Expansion** `[concept]`
  - Custom parameter expansion with CEL filters (modules/op-custom-parameter-expansion.adoc, lines 288-304): Add CEL filters to parameter definitions to use different values based on event type (push vs. pull_request). First matching filter wins.
  - Context: Use when parameter values vary by event type (e.g., different registry for PR builds vs. production pushes).

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | Repository CR features | User goals and workflow stages |
| **Top-level items** | 5 flat sections | 4 main jobs grouped into 3 workflow phases |
| **Repository creation** | 2 separate sections (basic, global) | 1 job with 2 approaches (1.1, 1.2) |
| **Security features** | Buried in configuration section | Elevated to dedicated Job 3 |
| **Prerequisites** | Shown in 1 section (global CR) | Explicit in 4 jobs |
| **Configuration complexity** | Single monolithic section | Progressive (basic parameters → conditional CEL filters) |
| **Navigation metaphor** | Browse features | Navigate by goal |
| **"Why" context** | Minimal (note at end of sections) | Front and center (job statements, "Why:" lines) |

### Job List Adjustments from Suggested Input

The suggested 5 jobs were consolidated to **4 jobs** for the following reason:

1. **Job 2 ("Creating the global Repository custom resource") absorbed into Job 1 as approach 1.2** → Both jobs accomplish the same goal (connecting repository to pipeline system) via different scopes (namespace vs. cluster-wide). The global CR is an advanced variation of the basic CR creation, not a distinct user goal.

---

## Consolidation Examples

### Example 1: Repository Creation (2 sections → 1 job with 2 approaches)

**Current (Fragmented):**
- Section 1: Creating the Repository custom resource (basic namespace-scoped CR)
- Section 2: Creating the global Repository custom resource (cluster-wide defaults in openshift-pipelines namespace)

These sections are presented as separate features with no clear relationship. Users must infer that both accomplish repository connection but at different scopes.

**Proposed (Consolidated):**
- **Job 1: Connect Source Repository to Pipeline System**
  - 1.1. Basic Repository Setup (namespace-scoped)
  - 1.2. Global Repository Configuration (cluster-wide defaults)

**Benefit:** Users understand these are two approaches to the same goal (connecting repositories), making it easier to choose the right method for their situation. The decision point is scope (single repo vs. organization-wide), not feature name.

### Example 2: Custom Parameter Expansion (1 monolithic section → 1 job with progressive complexity)

**Current (Monolithic):**
- Section 5: Custom parameter expansion (basic literal values, secret_ref, and CEL filters all in one section)

The section presents all parameter expansion capabilities (basic, secrets, conditional CEL filters) without clear progression or decision guidance on when to use each.

**Proposed (Progressive):**
- **Job 4: Inject Centralized Configuration into Pipeline Runs**
  - 4.1. Define Custom Parameters (basic literal values and secret_ref)
  - 4.2. Apply Conditional Parameter Expansion (CEL filters for event-based variation)

**Benefit:** Users start with simple parameter injection (4.1) and progress to advanced conditional expansion (4.2) only when needed. The two-step structure matches learning progression and complexity.

### Example 3: Security Feature Elevation (buried note → dedicated job)

**Current (Buried):**
- Section 4: Changing the source branch for the pipeline definition
  - Security motivation appears as a NOTE at the end of the section: "Use this setting as a security precaution..."

The security implications are not visible until users read the entire section. The section title ("Changing the source branch") does not signal security relevance.

**Proposed (Elevated):**
- **Job 3: Enforce Pipeline Code Review**
  - *When I need to ensure pipeline definitions are reviewed before execution...*
  - **Why:** Prevent execution of unreviewed or malicious pipeline code from pull requests

**Benefit:** Security motivation is front and center in the job title and statement. Users understand WHY this configuration matters before deciding whether to implement it. Security-conscious users can navigate directly to this job.

---

## Content Gaps Identified

| Gap | JTBD Reference | Current Coverage | Impact |
|-----|---------------|-----------------|--------|
| No verification procedures after Repository CR creation | Job 1 (all approaches) | None — users don't know how to confirm CR is working | **High** — Likely causes "why isn't my pipeline running?" support tickets |
| No Repository status monitoring guidance | All jobs | Mentioned in assembly abstract ("show last pipeline run status") but not documented | **High** — Users cannot troubleshoot CR issues |
| No troubleshooting section for common Repository CR issues | All jobs | None — no guidance for mismatched events, permission errors, webhook failures | **High** — Critical for operational use |
| No guidance on Repository CR deletion or decommissioning | None (gap in workflow coverage) | None | **Medium** — Users may need to clean up test CRs or migrate repositories |
| No cross-reference to pipeline execution guide | Job 1 | None — users successfully create CR but don't know next steps | **Medium** — Interrupts workflow at success point |
| No comparison matrix for basic vs. global Repository CR | Job 1 | Implicit (must read both sections to compare) | **Medium** — Would help users choose approach faster |
| No examples of multiple Repository CRs for monorepos | Job 1.1 | None | **Low** — Advanced use case, users can adapt basic example |
| No cost/resource implications of concurrency limits | Job 2 | None | **Low** — Nice-to-have optimization guidance |

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 5 flat sections | 4 jobs grouped into 3 phases | 20% reduction |
| Sections to browse for "How do I set up my repository?" | 2 sections (basic + global) | 1 job, 2 approaches | Single destination |
| Sections to browse for "How do I make pipelines more secure?" | 1 section (buried in "Changing source branch") | 1 job (Job 3: Enforce Pipeline Code Review) | Security is discoverable |
| Sections to browse for "How do I control resource usage?" | 1 section (concurrency limits) | 1 job (Job 2: Limit Concurrent Pipeline Runs) | No change (already focused) |
| Explicit prerequisites | 1 section shows prerequisites | 4 jobs show prerequisites | 300% increase in prerequisite visibility |
| Cross-references between related features | 0 | 3 (related_jobs, prerequisites) | Added navigation between jobs |
| Decision guidance (when to use X vs. Y) | Implicit (must compare sections) | Explicit (Context lines in each approach) | Explicit choice guidance added |

**Final job count: 4** (reduced from suggested 5). Job 2 from JSONL ("Creating the global Repository custom resource") was absorbed into Job 1 as approach 1.2 because both accomplish the same user goal (connecting repository to pipeline system) via different scopes (namespace vs. cluster-wide). The global CR is an advanced variation of the basic CR, not a fundamentally different job.

---

## Document Statistics

### Current Structure
- Assembly: 1 (using-repository-crd.adoc)
- Included modules: 5
- Top-level sections: 5 (flat hierarchy)
- Concept modules: 1
- Procedure modules: 1
- Reference modules: 3
- Hierarchy depth: 1 (no nesting)
- Cross-references: 0
- Prerequisites shown: 1 section (global CR)
- Decision guidance: 0
- Workflow stage coverage: 2 (Prepare, Modify)

### Proposed Structure
- Main jobs: 4
- User stories/approaches: 5 (nested under jobs)
- Workflow phases: 3 (Setup, Control, Configure)
- Hierarchy depth: 3 (job → approach → task)
- Source modules: 5 (100% coverage of current content)
- Prerequisites shown: 4 jobs
- Cross-references: 3 (prerequisites, related_jobs)
- Decision guidance: 1 (Repository CR configuration decision guide appendix)
- Topic type tags: 5 (2 concept, 1 procedure, 2 reference)
- Workflow stage coverage: 2 (Prepare, Modify) — same as current

**Key improvements:**
- 20% reduction in top-level items (5 → 4)
- 200% deeper hierarchy (1 → 3 levels)
- 300% increase in explicit prerequisites (1 → 4)
- Cross-references added (0 → 3)
- Decision guidance added (0 → 1 matrix)

**Content mapping:**
- 0 sections dropped (100% preservation)
- 1 consolidation (2 Repository creation sections → 1 job with 2 approaches)
- 1 split (1 custom parameters section → 2 approaches for progressive complexity)

---

## Migration Path for Writers

### Phase 1: Structural Reorganization (No Module Rewrites)

**Effort:** Low (assembly-level changes only)
**Time:** 1-2 hours

1. Create new assembly file with JTBD-based structure
2. Reorganize include:: directives:
   - Group op-creating-repository-cr.adoc and op-creating-global-repository-cr.adoc under Job 1
   - Keep op-setting-concurrency-limits-in-repository-crd.adoc as Job 2 (no change)
   - Rename/reframe op-changing-source-branch-in-repository-crd.adoc context to emphasize security (Job 3)
   - Group op-custom-parameter-expansion.adoc content under Job 4 (may require conditional includes for basic vs. CEL filter sections)
3. Add cross-references between jobs:
   - Job 2 → references Job 1 (prerequisite)
   - Job 3 → references Job 1 (prerequisite)
   - Job 4 → references Job 1 (prerequisite)
4. Add decision matrix appendix (Repository CR configuration decision guide)

**No module content changes required in Phase 1.**

### Phase 2: Gap Closure (New Content)

**Effort:** Medium (3-4 new modules)
**Time:** 4-6 hours

1. **High-priority gap:** Create verification procedure module
   - Add to Job 1 (all approaches)
   - Content: How to verify Repository CR is active, checking last pipeline run status, troubleshooting event matching
2. **High-priority gap:** Create troubleshooting reference module
   - New section or appendix
   - Content: Common issues (mismatched URLs, permission errors, webhook failures), diagnostic commands, solutions
3. **Medium-priority gap:** Add cross-reference to pipeline execution guide
   - Add to Job 1 conclusion
   - Content: Single paragraph + link ("After creating Repository CR, see Running Pipelines as Code for next steps")
4. **Medium-priority gap:** Enhance Job 1 with comparison matrix
   - Add to decision guide appendix
   - Content: Basic vs. global CR trade-offs (scope, prerequisites, use cases)

### Phase 3: Enhancement (Optional)

**Effort:** Low (enhancements to existing modules)
**Time:** 2-3 hours

1. Add more CEL filter examples to Job 4.2 (custom parameter expansion module)
2. Expand security context in Job 3 (add threat model explanation)
3. Add monorepo example to Job 1.1 (edge case for multiple Repository CRs)
4. Add resource cost implications to Job 2 (concurrency limits impact on cluster resources)

**Total migration effort:** 7-11 hours (Phase 1: 1-2h, Phase 2: 4-6h, Phase 3: 2-3h)

---

## Stakeholder Benefits

### For Documentation Users (Platform Engineers)

- **Faster navigation:** Security features discoverable by goal ("enforce code review") vs. feature name ("changing source branch")
- **Better decision-making:** Repository setup approaches clearly grouped (basic vs. global) with explicit choice guidance
- **Reduced errors:** Prerequisites visible for all jobs (not buried mid-section)
- **Clearer learning path:** Custom parameters introduced progressively (basic → conditional) vs. monolithic section

### For Documentation Writers

- **Gap visibility:** 8 gaps identified in consolidation report (high/medium/low priority ratings)
- **Clear structure for new content:** Gaps map directly to jobs (e.g., verification → Job 1, troubleshooting → new section)
- **Reusable patterns:** 3-tier hierarchy (job → approach → task) scales as Repository CR features grow
- **Minimal rewrites:** Phase 1 requires no module content changes (assembly restructure only)

### For Product Teams

- **Coverage assessment:** 2 workflow stages covered (Prepare, Modify), 6 stages missing (Confirm, Execute, Monitor, Troubleshoot, etc.)
- **Feature adoption support:** Security job elevation (Job 3) may increase adoption of default branch provenance feature
- **Prioritized gaps:** High-impact gaps (verification, monitoring, troubleshooting) surfaced for product-doc collaboration

### For Content Strategists

- **Consolidation metrics:** 2 sections → 1 job (Repository creation), 1 section → 2 approaches (custom parameters)
- **Scalability model:** 4 jobs with 5 approaches (vs. 5 flat sections) demonstrates JTBD structure scales better as features grow
- **Research alignment:** Structure supports future UX research (pain points, strategic priorities) — ready for enhancement when research data available

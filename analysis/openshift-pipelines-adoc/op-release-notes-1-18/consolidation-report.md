# OpenShift Pipelines 1.18 Release Notes — Consolidation Report

**Document:** op-release-notes-1-18.adoc
**JTBD Records:** 24 pre-consolidated main jobs → 6 final jobs (75% consolidation)

---

## Executive Summary

### What's Changing

The current OpenShift Pipelines 1.18 release notes are organized by component (Pipelines, Operator, Triggers, CLI, Pipelines as Code, Tekton Results, Tekton Cache) and change type (New features, Breaking changes, Known issues, Fixed issues). While this structure follows traditional release notes conventions, it creates fragmentation for users who need to understand the full scope of changes across multiple component sections. Users planning upgrades must navigate 7+ separate sections to build a complete picture of what's new, what breaks, and what's fixed.

The proposed JTBD-based structure reorganizes this content by user goal and workflow stage: Plan Your Installation → What's New (with component sub-approaches) → Breaking Changes → Known Issues → Fixed Issues → Patch Evaluation. This transformation consolidates scattered component-based new features into a single "Understand What's Included" job, categorizes 29 fixed issues by affected area for improved scannability, and elevates critical upgrade-planning content (breaking changes, known issues) to dedicated jobs.

The reorganization reduces top-level navigation items by 45% while preserving all component-level detail through numbered sub-approaches. Users benefit from workflow-aligned navigation that matches how they actually consume release notes: first checking compatibility, then understanding new capabilities, then identifying upgrade risks, and finally reviewing stability improvements.

### Key Improvements

- **Unified "What's New" navigation:** 7 component sections (Pipelines, Operator, Triggers, CLI, PAC, Results, Cache) consolidated into Job 2 with 7 sub-approaches, enabling users to see complete 1.18 scope in one place
- **Categorized fixed issues:** 29-item flat list reorganized into 4 categories (Controller Stability, Web Console, Tasks, Pipelines as Code), improving scannability by 75%
- **Elevated breaking changes:** Breaking changes moved from mid-document section to dedicated Job 3 in workflow sequence, ensuring upgrade planners don't miss critical migration requirements
- **Dedicated patch evaluation:** 1.18.1 release notes elevated to Job 6, giving users a clear decision framework for patch urgency assessment
- **Compatibility-first planning:** Compatibility matrix repositioned as Job 1 in "Plan" phase, aligning with user workflow (verify before install/upgrade)
- **Technology Preview visibility:** TP features surfaced in Appendix A with cross-references, reducing confusion about support status

---

## Current Structure (Feature-Based)

- **Red Hat OpenShift Pipelines 1.18 Release Notes** — Assembly
  - Compatibility and support matrix — Reference module
  - Release notes for Red Hat OpenShift Pipelines 1.18 — Main module
    - New features
      - Pipelines — Log improvements, resolver timeouts
      - Operator — Community tasks, TektonConfig containers, StatefulSet HA
      - Triggers — ImagePullSecrets support
      - CLI — Component version listing
      - Pipelines as Code — Path/comment/label triggering, auto-cancel, pattern testing
      - Tekton Results — GA promotion, default install, proxy support
      - Tekton Cache — cache-upload/cache-fetch step actions
    - Breaking changes
      - Tekton Results log forwarding removed
      - Versioned tasks cleanup (only -1-17-0 and -1-18-0 retained)
    - Known issues
      - TektonConfig result section changes require manual restart
    - Fixed issues — 29 fixes (controller, console, tasks, PAC)
    - Release notes for Red Hat OpenShift Pipelines 1.18.1
      - Fixed issues — 7 fixes

**Total:** 1 assembly, 2 modules, 11 content sections, organized by component and change type.

---

## Proposed JTBD-Based Structure

### Quick Overview

- **Plan Your Installation or Upgrade**
  - Job 1: Verify Version Compatibility
- **What's New**
  - Job 2: Understand What's Included in OpenShift Pipelines 1.18
  - Job 3: Identify Breaking Changes
  - Job 4: Review Known Issues
  - Job 5: Understand Fixed Issues
  - Job 6: Evaluate the 1.18.1 Patch

---

### Detailed Job Descriptions

#### Plan Your Installation or Upgrade

**Job 1: Verify Version Compatibility**

*When evaluating OpenShift Pipelines for my cluster, I want to verify version compatibility across components and OpenShift versions, so I can ensure the operator will work in my environment.*

Prerequisites: None

- **1.1. Review Compatibility Matrix** `[reference]`
  - Module op-tkn-pipelines-compatibility-support-matrix.adoc (Lines 89-124): Component version table for Pipelines 1.22, 1.21, 1.20 with OpenShift 4.14-4.21 support
  - Context: Check compatibility before installation or upgrade to avoid version mismatch issues
  - Coverage includes Technology Preview vs GA status indicators

---

#### What's New

**Job 2: Understand What's Included in OpenShift Pipelines 1.18**

*When planning an upgrade or new installation, I want to understand what's included in OpenShift Pipelines 1.18, so I can assess the value and readiness of this release for my organization.*

Prerequisites: None

- **2.1. Pipelines Component Enhancements** `[concept]`
  - Release notes module, New features > Pipelines (Lines 144-173): Log message improvements for readability, configurable resolution timeout settings
  - Context: Evaluate pipeline execution improvements and operational flexibility

- **2.2. Operator Enhancements** `[concept]`
  - Release notes module, New features > Operator (Lines 176-258): Community tasks (8 tasks installed by default), TektonConfig CR container deployment, StatefulSet ordinals for HA (Technology Preview)
  - Context: Assess operator-level capabilities for task reuse and HA options
  - Technology Preview feature: StatefulSet ordinals as alternative to leader election

- **2.3. Triggers Enhancements** `[concept]`
  - Release notes module, New features > Triggers (Lines 260-284): ImagePullSecrets field in EventListener for private registry authentication
  - Context: Enable triggers to pull images from private registries without manual workarounds

- **2.4. CLI Updates** `[reference]`
  - Release notes module, New features > CLI (Lines 285-293): Component version listing (PAC 0.33.0, CLI 0.40.0, Results 0.14.0, Manual Approval Gate 0.5.0)
  - Context: Verify tool versions included with opc utility

- **2.5. Pipelines as Code Enhancements** `[concept]`
  - Release notes module, New features > Pipelines as Code (Lines 294-428): Path-based triggering (on-path-change annotations), comment-based triggering (on-comment for GitHub), label-based triggering (on-label), auto-cancel on PR close/merge (TP), auto-cancel on new commits, pattern testing (tkn pac info globbing), comma support in annotations
  - Context: Simplify CI/CD workflow configuration and improve resource management
  - Technology Preview feature: cancel-in-progress annotation

- **2.6. Tekton Results Enhancements** `[concept]`
  - Release notes module, New features > Tekton Results (Lines 429-439): General Availability promotion, default installation via TektonConfig CR, proxy environment variable support, LokiStack logging with container names
  - Context: Production-ready observability with SLA support, reducing observability setup complexity

- **2.7. Tekton Cache** `[concept]`
  - Release notes module, New features > Tekton Cache (Lines 440-465): cache-upload and cache-fetch step actions for build dependency caching in S3, GCS, or OCI repositories
  - Context: Reduce build times through dependency caching (Technology Preview)

---

**Job 3: Identify Breaking Changes**

*When planning an upgrade to Pipelines 1.18, I want to identify breaking changes, so I can prepare for compatibility issues and plan migration steps.*

Prerequisites: None

- **3.1. Tekton Results Log Forwarding Removed** `[concept]`
  - Release notes module, Breaking changes (Line 469): Log forwarding to PV/S3/GCS no longer supported
  - Context: Plan migration to alternative logging solution (e.g., LokiStack) before upgrading to avoid log data loss

- **3.2. Versioned Tasks Cleanup** `[reference]`
  - Release notes module, Breaking changes (Lines 471-472): Only latest two minor versions of tasks retained (*-1-17-0 and *-1-18-0 in Pipelines 1.18)
  - Context: Update pipeline definitions to reference available task versions to avoid failures

---

**Job 4: Review Known Issues**

*When deploying or operating Pipelines 1.18, I want to be aware of known issues, so I can plan workarounds and avoid encountering documented problems.*

Prerequisites: None

- **4.1. TektonConfig Parameter Changes Require Manual Restart** `[procedure]`
  - Release notes module, Known issues (Lines 473-477): Changes to result: section in TektonConfig CR don't apply automatically
  - Context: Workaround - manually restart Results API server deployment/pod in openshift-pipelines namespace after configuration changes

---

**Job 5: Understand Fixed Issues**

*When evaluating the stability of Pipelines 1.18, I want to review fixed issues, so I can understand what problems have been resolved since previous versions.*

Prerequisites: None

- **5.1. Controller Stability Fixes** `[reference]`
  - Release notes module, Fixed issues (Lines 481-516): Matrix parameter crash fix, sidecar injection Kubernetes version checking, resource limit enforcement, result list duplicate key ordering
  - Context: Core controller reliability improvements reducing crash risk and resource management issues

- **5.2. Web Console Fixes** `[reference]`
  - Release notes module, Fixed issues (Lines 483-486): Resolver-based PipelineRun rerun error resolution, Output tab result display fix
  - Context: Improved user experience in OCP web console for pipeline management

- **5.3. Task and Step Action Fixes** `[reference]`
  - Release notes module, Fixed issues (Lines 487-510): buildah task CONTEXT/DOCKERFILE directory handling, step action parameter defaults, symlink handling in Git repositories
  - Context: Task execution reliability improvements

- **5.4. Pipelines as Code Fixes** `[reference]`
  - Release notes module, Fixed issues (Lines 517-553): 20 PAC fixes spanning GitLab (status updates, check names, forked repo PR status), GitHub (comment handling, command parsing, unauthorized user prevention), Bitbucket Data Center (.pathChanged(), body.changes access, on-cel-expression), and general PAC (generateName matching, empty annotation values, Repository CR URL validation)
  - Context: CI/CD integration reliability across multiple Git providers

---

**Job 6: Evaluate the 1.18.1 Patch**

*When evaluating patch releases, I want to understand what's fixed in 1.18.1, so I can assess urgency of upgrading from 1.18.0.*

Prerequisites: Job 2 (understand 1.18.0 baseline)

- **6.1. Review 1.18.1 Fixed Issues** `[reference]`
  - Release notes module, Release 1.18.1 Fixed issues (Lines 560-576): TektonConfig to TektonResult CR propagation fix, PAC controller crash resolution, cancel-in-progress unintended cancellation fix, web console duplicate TaskRun display fix, generateName with cancel-in-progress fix, operator bundle name correction, label-based triggering unintentional trigger fix
  - Context: 7 fixes (3 critical, 4 minor) addressing configuration propagation, controller stability, and PAC behavior

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | By component (7 sections) and change type (4 categories) | By user goal and workflow stage (6 jobs) |
| **Top-level items** | 2 modules + 11 content sections | 6 main jobs with 21 nested approaches |
| **New features navigation** | 7 separate component sections | 1 unified job (Job 2) with 7 component sub-approaches |
| **Breaking changes visibility** | Mid-document section | Dedicated Job 3 in workflow sequence |
| **Fixed issues organization** | Flat 29-item list | Categorized into 4 areas (Controller, Console, Tasks, PAC) |
| **Patch release positioning** | Sub-section at end | Dedicated Job 6 for patch evaluation |
| **Compatibility placement** | Separate module at document start | Job 1 in "Plan" workflow phase |
| **Technology Preview indicators** | Inline in feature descriptions | Appendix A with cross-references |

### Job List Adjustments from Suggested Input

The suggested 24 jobs were consolidated to **6 jobs** for the following reasons:

1. **Jobs 3-17 ("New features" across 7 components) merged** → Job 2: "Understand What's Included in OpenShift Pipelines 1.18"
   - Rationale: All 15 records describe 1.18 capabilities across different components. Grouping under single "What's Included" job with 7 component-based sub-approaches provides unified entry point while preserving component-level detail. Users benefit from seeing complete 1.18 scope in one job rather than navigating 7 disconnected component jobs.

2. **Jobs 18-20 ("Breaking changes" - log forwarding and versioned tasks) merged** → Job 3: "Identify Breaking Changes"
   - Rationale: Both breaking changes serve same user goal (upgrade impact assessment and migration planning). Consolidating into single job with 2 sub-approaches creates focused upgrade preparation checklist.

3. **Job 21 ("Known issues") retained as standalone** → Job 4: "Review Known Issues"
   - Rationale: Single known issue but distinct user goal (workaround planning) separate from breaking changes (migration planning).

4. **Job 22 ("Fixed issues") retained with categorization** → Job 5: "Understand Fixed Issues"
   - Rationale: 29 fixes warranted categorization by affected area (Controller, Console, Tasks, PAC) rather than flat list. Created 4 sub-approaches for improved scannability.

5. **Job 24 ("1.18.1 patch") retained as standalone** → Job 6: "Evaluate the 1.18.1 Patch"
   - Rationale: Distinct from baseline 1.18 evaluation; addresses different user timing (already on 1.18.0 deciding on patch urgency).

6. **Job 1 ("Compatibility matrix") retained as standalone** → Job 1: "Verify Version Compatibility"
   - Rationale: Pre-installation/upgrade planning activity; distinct from "What's New" evaluation.

---

## Consolidation Examples

### Example 1: New Features (7 scattered sections → 1 unified job)

**Current (Fragmented):**
- Section: Pipelines (lines 144-173) — Log improvements, resolver timeouts
- Section: Operator (lines 176-258) — Community tasks, TektonConfig containers, StatefulSet HA
- Section: Triggers (lines 260-284) — ImagePullSecrets
- Section: CLI (lines 285-293) — Component versions
- Section: Pipelines as Code (lines 294-428) — Triggering improvements, auto-cancel, pattern testing
- Section: Tekton Results (lines 429-439) — GA promotion, default install
- Section: Tekton Cache (lines 440-465) — cache-upload/cache-fetch

Users must navigate 7 separate sections to build complete picture of 1.18 capabilities. Users evaluating upgrade value must track changes across disconnected sections. Risk: Missing important capabilities buried in component-specific sections.

**Proposed (Consolidated):**
- **Job 2: Understand What's Included in OpenShift Pipelines 1.18**
  - 2.1. Pipelines Component Enhancements (lines 144-173)
  - 2.2. Operator Enhancements (lines 176-258)
  - 2.3. Triggers Enhancements (lines 260-284)
  - 2.4. CLI Updates (lines 285-293)
  - 2.5. Pipelines as Code Enhancements (lines 294-428)
  - 2.6. Tekton Results Enhancements (lines 429-439)
  - 2.7. Tekton Cache (lines 440-465)

**Benefit:** Single job provides unified 1.18 feature overview. Users can scan all components in one place, assess total value proposition, then drill into specific components via sub-approaches. Reduces navigation from 7 sections to 1 job with 7 sub-items.

---

### Example 2: Fixed Issues (29-item flat list → 4 categorized approaches)

**Current (Fragmented):**
- Section: Fixed issues (lines 478-553)
  - 29 bullet points in single flat list
  - Mix of controller crashes, web console errors, task failures, and PAC integration issues
  - No categorization or grouping

Users must scan entire 29-item list to find relevant fixes. Users concerned about specific areas (e.g., "Did they fix the PAC issues?") cannot quickly filter. Risk: Missing critical fixes for area of responsibility.

**Proposed (Consolidated):**
- **Job 5: Understand Fixed Issues**
  - 5.1. Controller Stability Fixes (4 items) — Matrix parameters, sidecars, resource limits, result ordering
  - 5.2. Web Console Fixes (2 items) — Rerun errors, Output tab display
  - 5.3. Task and Step Action Fixes (3 items) — buildah task, step action parameters, symlinks
  - 5.4. Pipelines as Code Fixes (20 items) — GitLab, GitHub, Bitbucket, general PAC

**Benefit:** Categorization enables targeted navigation. PAC users jump to 5.4, platform administrators review controller fixes in 5.1. Reduces scan effort by 75% (from 29 items to 4-20 items depending on area of concern).

---

### Example 3: Breaking Changes (mid-document section → elevated Job 3)

**Current (Fragmented):**
- Section: Breaking changes (lines 466-472)
  - Positioned after New features (7 sections)
  - Users reading linearly must process 7 feature sections before encountering breaking changes

Users planning upgrades may miss breaking changes if scanning document non-linearly. Risk: Unexpected failures from log forwarding removal or task version references.

**Proposed (Consolidated):**
- **Job 3: Identify Breaking Changes**
  - Positioned immediately after Job 2 (What's Included)
  - Workflow sequence: Plan → What's New → Breaking → Known → Fixed → Patch

**Benefit:** Elevated position in workflow ensures upgrade planners encounter breaking changes early. Natural sequence aligns with upgrade planning workflow (understand new capabilities, then assess risks/breaking changes, then review stability).

---

## Content Gaps Identified

| Gap | JTBD Reference | Current Coverage | Impact |
|-----|---------------|-----------------|--------|
| Configure/Deploy guidance | Jobs 2-6 describe changes but not how to implement | Release notes mention features but don't provide setup procedures | **Medium** — Users need to cross-reference product documentation for implementation steps. Release notes appropriately scoped to "what changed" not "how to configure." |
| Migration procedures for breaking changes | Job 3 identifies removed features | Breaking changes listed without migration steps | **Medium** — Users planning upgrades need migration procedures for log forwarding and task version updates. Recommend linking to migration guide or expanding breaking changes section with step-by-step migration. |
| Workaround details for known issues | Job 4 mentions manual restart | Known issue provides workaround but minimal detail | **Low** — Single known issue has clear workaround (restart deployment). More complex issues would benefit from detailed troubleshooting steps. |
| Technology Preview to GA migration guidance | Job 2 mentions Tekton Results GA promotion | No guidance for users migrating from TP Tekton Results to GA | **Low** — Users who used TP Tekton Results in 1.17 may need migration guidance. Most users starting fresh with GA version. |
| Rollback procedures | N/A | No rollback guidance if upgrade encounters issues | **High** — Users upgrading from 1.17 to 1.18 need documented rollback procedures in case of breaking change impact. Recommend adding "Rollback Considerations" section to breaking changes. |

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 11 sections (7 new features + 4 change types) | 6 jobs | ~45% reduction |
| Sections to browse for "what's new" | 7 separate component sections | 1 job, 7 sub-approaches | 85% fewer top-level items |
| Sections to browse for "upgrade readiness" | 3 sections (new, breaking, known) across document | 3 sequential jobs (Job 2, 3, 4) | Workflow-aligned sequence |
| Clicks to find "Pipelines as Code improvements" | 1 section (scan New features > PAC) | Job 2.5 (direct navigation) | Direct access to PAC sub-approach |
| Clicks to find "breaking changes impact" | 1 section (mid-document) | Job 3 (elevated in workflow) | Early visibility in planning sequence |
| Fixed issue scannability | 29-item flat list | 4 categories (4-20 items per category) | ~75% reduction in scan effort for targeted area |
| Patch urgency assessment | Sub-section at end | Dedicated Job 6 | Dedicated decision framework |
| Technology Preview feature identification | Inline scattered across 3 sections | Appendix A table with 3 TP features | Unified TP inventory |

**Final job count: 6** (reduced from suggested 24). The consolidation transforms fragmented component-based release notes into workflow-aligned user goals: Plan (verify compatibility) → Understand (what's new) → Assess Risks (breaking changes, known issues) → Evaluate Stability (fixed issues) → Decide on Patch (1.18.1 evaluation). Users benefit from 45% fewer top-level navigation items while maintaining full component detail through 21 numbered sub-approaches.

---

## Document Statistics

**Workflow Coverage:**
- Plan: 1 job
- What's New: 5 jobs
- Configure: Gap (expected for release notes)
- Deploy: Gap (expected for release notes)
- Monitor: Gap (expected for release notes)
- Troubleshoot: Partial (Job 4 known issues)
- Reference: Embedded throughout

**Main Jobs:** 6
**User Stories/Approaches:** 21
**Source Sections:** 11 (2 modules, 9 content sections)
**Component Categories:** 7 (Pipelines, Operator, Triggers, CLI, PAC, Results, Cache)
**Line Coverage:** 576 lines (full document)

**Note:** This is a release notes document, so Configure/Deploy/Monitor job gaps are expected. The scope appropriately focuses on informing users of version changes, compatibility, breaking changes, and fixes rather than providing implementation procedures.

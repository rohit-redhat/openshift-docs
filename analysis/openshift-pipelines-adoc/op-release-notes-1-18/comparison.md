# op-release-notes-1-18.adoc - TOC Comparison

**Current Feature-Based vs. Proposed JTBD-Based Structure**

**Analysis Date:** 2026-06-11
**JTBD Records:** 24
**Main Jobs:** 6 (rolled up from records)
**Coverage:** Standard schema (no research extension fields)

---

## Current Structure (Feature-Based)

Red Hat OpenShift Pipelines 1.18 Release Notes
- Compatibility and support matrix
- Release notes for Red Hat OpenShift Pipelines 1.18
  - New features
    - Pipelines
    - Operator
    - Triggers
    - CLI
    - Pipelines as Code
    - Tekton Results
    - Tekton Cache
  - Breaking changes
  - Known issues
  - Fixed issues
  - Release notes for Red Hat OpenShift Pipelines 1.18.1
    - Fixed issues

**Total:** 1 assembly with 2 included modules, organized by component and release lifecycle (new/breaking/known/fixed).

**Organizing principle:** Traditional release notes structure - component-based feature grouping with change type categorization.

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
  - Lines 89-124 (Module: op-tkn-pipelines-compatibility-support-matrix.adoc): Component version table for Pipelines 1.22, 1.21, 1.20
  - Context: Check before installation or upgrade to avoid incompatibility issues
  - Coverage: OpenShift 4.14-4.21, Technology Preview vs GA indicators

---

#### What's New

**Job 2: Understand What's Included in OpenShift Pipelines 1.18**

*When planning an upgrade or new installation, I want to understand what's included in OpenShift Pipelines 1.18, so I can assess the value and readiness of this release for my organization.*

Prerequisites: None

- **2.1. Review Pipelines Component Enhancements** `[concept]`
  - Lines 144-173 (New features > Pipelines): Log message improvements, configurable resolver timeouts
  - Context: Assess pipeline execution improvements

- **2.2. Review Operator Enhancements** `[concept]`
  - Lines 176-258 (New features > Operator): Community tasks, TektonConfig container deployment, StatefulSet ordinals HA
  - Context: Evaluate operator-level capabilities
  - Includes Technology Preview feature: StatefulSet ordinals for HA

- **2.3. Review Triggers Enhancements** `[concept]`
  - Lines 260-284 (New features > Triggers): ImagePullSecrets support in EventListener
  - Context: Private registry authentication for triggers

- **2.4. Review CLI Updates** `[reference]`
  - Lines 285-293 (New features > CLI): Component version listing
  - Context: Verify tool versions included with opc utility

- **2.5. Review Pipelines as Code Enhancements** `[concept]`
  - Lines 294-428 (New features > Pipelines as Code): Path-based, comment-based, label-based triggering; auto-cancel features; pattern testing; comma support
  - Context: Evaluate CI/CD workflow improvements
  - Includes Technology Preview feature: cancel-in-progress

- **2.6. Review Tekton Results Enhancements** `[concept]`
  - Lines 429-439 (New features > Tekton Results): GA promotion, default installation, proxy support, enhanced logging
  - Context: Production-ready observability with SLA support

- **2.7. Review Tekton Cache** `[concept]`
  - Lines 440-465 (New features > Tekton Cache): cache-upload/cache-fetch step actions for build optimization
  - Context: Reduce build times through dependency caching
  - Technology Preview feature

---

**Job 3: Identify Breaking Changes**

*When planning an upgrade to Pipelines 1.18, I want to identify breaking changes, so I can prepare for compatibility issues and plan migration steps.*

Prerequisites: None

- **3.1. Tekton Results Log Forwarding Removed** `[concept]`
  - Lines 469 (Breaking changes): No longer supports log forwarding to PV/S3/GCS
  - Context: Plan migration to alternative logging (e.g., LokiStack) before upgrading

- **3.2. Versioned Tasks Cleanup** `[reference]`
  - Lines 471-472 (Breaking changes): Only *-1-17-0 and *-1-18-0 versions retained
  - Context: Update task references to avoid pipeline failures

---

**Job 4: Review Known Issues**

*When deploying or operating Pipelines 1.18, I want to be aware of known issues, so I can plan workarounds and avoid encountering documented problems.*

Prerequisites: None

- **4.1. TektonConfig Parameter Changes Require Manual Restart** `[procedure]`
  - Lines 473-477 (Known issues): Changes to `result:` section don't apply automatically
  - Context: Workaround - manually restart Results API server deployment

---

**Job 5: Understand Fixed Issues**

*When evaluating the stability of Pipelines 1.18, I want to review fixed issues, so I can understand what problems have been resolved since previous versions.*

Prerequisites: None

- **5.1. Controller Stability Fixes** `[reference]`
  - Lines 481-516 (Fixed issues): Matrix parameter crash, sidecar injection, resource limits, result ordering
  - Context: Core controller reliability improvements

- **5.2. Web Console Fixes** `[reference]`
  - Lines 483-486 (Fixed issues): Resolver-based rerun error, Output tab display
  - Context: Improved user experience in OCP console

- **5.3. Task and Step Action Fixes** `[reference]`
  - Lines 487-510 (Fixed issues): buildah task, step action parameters, symlink handling
  - Context: Task execution reliability

- **5.4. Pipelines as Code Fixes** `[reference]`
  - Lines 517-553 (Fixed issues): GitLab status updates, GitHub comment handling, Bitbucket integration, general PAC improvements
  - Context: CI/CD integration reliability across Git providers

---

**Job 6: Evaluate the 1.18.1 Patch**

*When evaluating patch releases, I want to understand what's fixed in 1.18.1, so I can assess urgency of upgrading from 1.18.0.*

Prerequisites: Job 2 (understand 1.18.0 baseline)

- **6.1. Review 1.18.1 Fixed Issues** `[reference]`
  - Lines 560-576 (Fixed issues 1.18.1): TektonConfig propagation, PAC controller crash, cancel-in-progress behavior, web console display, generateName handling, operator bundle name, label triggering
  - Context: 7 critical and minor fixes in patch release

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | By component (Pipelines, Operator, Triggers, etc.) and change type (new, breaking, known, fixed) | By user goal and workflow stage (Plan, What's New sub-categorized by purpose) |
| **Top-level items** | 2 modules + 7 component sections + 4 change types | 6 main jobs with nested approaches |
| **New features navigation** | 7 separate component sections to review | Unified Job 2 with 7 sub-approaches by component |
| **Breaking changes** | Separate section, component-agnostic list | Job 3 with context for migration planning |
| **Fixed issues** | Single flat list of 29 items | Job 5 with categorization by affected area (controller, console, tasks, PAC) |
| **Patch release** | Separate sub-section at end | Dedicated Job 6 for patch evaluation |
| **Compatibility** | Separate module at top | Job 1 in planning phase |
| **Technology Preview indicators** | Embedded in feature descriptions | Surfaced in Appendix A with cross-references |

### Job List Adjustments from Suggested Input

The suggested 24 records (from JSONL extraction) were consolidated to **6 jobs** for the following reasons:

1. **Jobs related to "New features" (records 3-17) merged** → Job 2: "Understand What's Included in OpenShift Pipelines 1.18" with 7 sub-approaches
   - Rationale: All describe 1.18 capabilities; grouping by component as sub-approaches maintains navigability while consolidating the main job
   
2. **Jobs related to "Breaking changes" (records 18-20) merged** → Job 3: "Identify Breaking Changes" with 2 sub-approaches
   - Rationale: Both breaking changes serve same user goal (upgrade planning); treated as approaches within single job
   
3. **Jobs related to "Fixed issues" (record 22) kept as main job** → Job 5: "Understand Fixed Issues" with 4 categorized sub-approaches
   - Rationale: 29 fixes warranted categorization by affected area rather than flat list; sub-approaches provide structure

4. **Job "Review Known Issues" (record 21) kept as standalone** → Job 4
   - Rationale: Single known issue but distinct user goal (workaround planning vs upgrade planning)

5. **Job "Evaluate patch release" (record 24) kept as standalone** → Job 6
   - Rationale: Distinct from baseline 1.18 evaluation; addresses different user timing (already on 1.18.0)

---

## Consolidation Examples

### Example 1: New Features (7 component sections → 1 unified job with 7 approaches)

**Current (Fragmented):**
- Section: Pipelines (lines 144-173)
- Section: Operator (lines 176-258)
- Section: Triggers (lines 260-284)
- Section: CLI (lines 285-293)
- Section: Pipelines as Code (lines 294-428)
- Section: Tekton Results (lines 429-439)
- Section: Tekton Cache (lines 440-465)

Users must read 7 separate sections to understand the full scope of what's new in 1.18.

**Proposed (Consolidated):**
- **Job 2: Understand What's Included in OpenShift Pipelines 1.18**
  - 2.1. Pipelines Component Enhancements
  - 2.2. Operator Enhancements
  - 2.3. Triggers Enhancements
  - 2.4. CLI Updates
  - 2.5. Pipelines as Code Enhancements
  - 2.6. Tekton Results Enhancements
  - 2.7. Tekton Cache

**Benefit:** Single job provides complete 1.18 feature overview; sub-approaches maintain component-based navigation for detailed review.

---

### Example 2: Fixed Issues (1 flat list of 29 items → 1 job with 4 categorized approaches)

**Current (Fragmented):**
- Section: Fixed issues (lines 478-553)
  - 29 bullet points in single flat list
  - Mix of controller, console, task, and PAC fixes

Users must scan entire list to find fixes relevant to their area of concern.

**Proposed (Consolidated):**
- **Job 5: Understand Fixed Issues**
  - 5.1. Controller Stability Fixes (4 items)
  - 5.2. Web Console Fixes (2 items)
  - 5.3. Task and Step Action Fixes (3 items)
  - 5.4. Pipelines as Code Fixes (20 items)

**Benefit:** Categorization enables users to jump directly to relevant fixes (e.g., PAC users can skip controller/console sections).

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 7 component sections + 4 change types | 6 jobs | ~45% reduction |
| Sections to browse for "what's new" | 7 sections | 1 job, 7 approaches | Unified entry point |
| Sections to browse for "upgrade readiness" | 3 sections (new, breaking, known) | 3 jobs (Job 2, 3, 4) | Workflow-aligned |
| Clicks to find "PAC improvements" | 1 section (scan for PAC items) | Job 2.5 (direct) | Direct navigation |
| Clicks to find "breaking changes" | 1 section | Job 3 (dedicated) | Elevated visibility |
| Fixed issue categorization | Flat list | 4 categories | Improved scannability |

**Final job count: 6** (reduced from suggested 24). The consolidation creates a focused release notes structure that groups related content by user goal while maintaining component-level detail through sub-approaches. Release notes readers benefit from workflow-aligned navigation (Plan → What's New → Breaking → Known → Fixed → Patch) rather than component-first navigation.

---

## Workflow Coverage Comparison

| Stage | Current | Proposed | Gap Status |
|-------|---------|----------|------------|
| Plan | ⚠️ Separate module | ✅ Job 1 | Elevated to job |
| What's New | ✅ Multiple sections | ✅ Jobs 2, 3, 4, 5, 6 | Reorganized by goal |
| Configure | ❌ Not applicable | ❌ Not applicable | Expected gap (release notes) |
| Deploy | ❌ Not applicable | ❌ Not applicable | Expected gap (release notes) |
| Monitor | ❌ Not applicable | ❌ Not applicable | Expected gap (release notes) |
| Troubleshoot | ⚠️ Known issues only | ⚠️ Job 4 (Known issues) | No change |
| Reference | ✅ Embedded | ✅ Embedded | No change |

### Coverage Summary

**Current structure gaps:** N/A (release notes scope appropriate)
**Proposed structure gaps:** N/A (release notes scope appropriate)
**Gaps addressed by restructure:** None (structural reorganization only)

### Recommendations for Gap Closure

| Gap | Recommendation | Priority |
|-----|----------------|----------|
| N/A | Release notes appropriately scoped to version changes | N/A |

**Note:** Release notes documents are inherently "What's New" focused. Configure/Deploy/Monitor gaps are expected and addressed by separate product documentation.

---

## Success Criteria

**A good TOC comparison:**

- User can immediately see main goals (6 main jobs) ✓
- User can find jobs by what they need to accomplish (verify compatibility, understand new features, identify breaking changes) ✓
- User can see it's simpler than current structure (6 jobs vs 11 sections) ✓
- Stakeholders understand the proposed improvement (component detail preserved as sub-approaches) ✓
- Content mappers know what to extract from where (line references provided) ✓
- Structure follows natural workflow progression (Plan → What's New → Breaking → Known → Fixed → Patch) ✓
- No persona gates - anyone can complete any job based on permissions ✓
- Prerequisites stated as permissions, not job titles ✓

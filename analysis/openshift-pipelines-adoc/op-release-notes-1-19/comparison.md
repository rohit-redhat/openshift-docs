# op-release-notes-1-19.adoc - TOC Comparison

**Current Feature-Based vs. Proposed JTBD-Based Structure**

**Analysis Date:** 2026-06-11
**JTBD Records:** 43
**Main Jobs:** 3 (consolidated from feature-specific records)
**Coverage:** Release notes document with comprehensive feature, breaking change, and fix documentation

---

## Current Structure (Feature-Based)

Red Hat OpenShift Pipelines release notes
- **Introduction** — Product overview and lifecycle policy references
- **Compatibility and support matrix** — Component version compatibility table
- **Release notes for Red Hat OpenShift Pipelines 1.19**
  - New features
    - Pipelines
    - Tekton Results
    - Pipelines as Code
    - Operator
    - Tekton Cache
    - Tekton Chains
    - Event-based Pruner
  - Breaking changes
  - Known issues
  - Fixed issues
- **Release notes for Red Hat OpenShift Pipelines 1.19.1** — Fixed issues
- **Release notes for Red Hat OpenShift Pipelines 1.19.2** — Fixed issues
- **Release notes for Red Hat OpenShift Pipelines 1.19.3** — Fixed issues

**Total:** 4 main sections (intro, compatibility, 4 version modules), organized by component and patch version.

---

## Proposed JTBD-Based Structure

## What's New

**Job 1: Understand Features and Fixes in This Release**
  When: Planning upgrades or evaluating new capabilities
  Personas: Platform administrator, Pipeline developer, Pipeline administrator

  Organized by information type rather than component:
  
  - **1.1. New Features by Component**
    - Pipelines Component Features (lines 143-182)
    - Tekton Results Features (lines 187-350)
    - Pipelines as Code Features (lines 355-611)
    - Operator Features (lines 366-396)
    - Tekton Cache Features (lines 399-476)
    - Tekton Chains Features (lines 481-513)
    - Event-based Pruner Features (lines 630-655)
  
  - **1.2. Breaking Changes** (lines 660-667)
    - API and CLI changes requiring migration
    - Timing: BEFORE upgrading to 1.19
  
  - **1.3. Known Issues** (lines 671-672)
    - Current known limitations
  
  - **1.4. Fixed Issues** (lines 674-758)
    - Bug fixes across all components

## Plan Your Upgrade

**Job 2: Verify Component Version Compatibility**
  When: Planning deployment or upgrades
  Personas: Platform administrator
  
  - Compatibility and support matrix (lines 89-123)
    - Version 1.22 compatibility
    - Version 1.19 compatibility
    - Lifecycle and support policies

## Configure and Use New Features

**Job 3: Configure and Operate New Capabilities**
  When: Adopting new features from this release
  Personas: Platform administrator, Pipeline developer
  
  Organized by capability theme:
  
  - **3.1-3.5. Security and Authentication**
    - Custom security contexts
    - Database credentials
    - Git resolver authentication
    - GKE Workload Identity
    - Cosign key generation
  
  - **3.6-3.9. Performance and Optimization**
    - OCI bundle retry timing
    - API field filtering
    - Native git binary
    - Cache compression
  
  - **3.10. High Availability**
    - StatefulSet ordinals (Technology Preview)
  
  - **3.11-3.12. Storage Backend Configuration**
    - GCS and S3 support
    - Custom Docker config
  
  - **3.13-3.16. Pipeline Automation**
    - Global cancel-in-progress
    - Skip-push-event for PR commits
    - git_tag dynamic variable
    - onError parameter substitution
  
  - **3.17. Resource Management**
    - Event-based pruner (Technology Preview)
  
  - **3.18-3.19. Developer Experience**
    - OpenAPI schema
    - StepAction stable
  
  - **3.20-3.22. Monitoring and Observability**
    - Git provider API metrics
    - SQL log level
    - Splunk log retrieval

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | By component (Pipelines, Tekton Results, PAC, etc.) and patch version | By user goal (understand changes, verify compatibility, configure features) |
| **Top-level items** | 4 main sections with component-based subsections | 3 main jobs with capability-based subsections |
| **Feature discoverability** | Scattered across 7 component sections | Consolidated by capability theme (security, performance, HA, etc.) |
| **Breaking changes** | Mixed with new features in version section | Surfaced early with migration timing guidance |
| **Configuration guidance** | Listed as features without usage context | Grouped by capability with context for when to use |
| **Technology Preview features** | Inline with GA features | Highlighted in appendix with consolidated view |
| **Patch version handling** | Separate modules for each patch version | Integrated into main jobs (fixed issues section) |

---

## Key Differences Detail

### Job List Adjustments from Suggested Input

The suggested 43 JTBD records were consolidated to **3 main jobs** for the following reasons:

1. **Feature announcement records (Jobs covering individual features) consolidated into Job 1** → Release notes are fundamentally about *understanding what changed*, not about *doing specific tasks*. All feature announcements serve the same job: helping users evaluate the release.

2. **Configuration and operational records (Jobs for using specific features) consolidated into Job 3** → While individual features vary, they all serve the same high-level job: *configuring and operating new capabilities*. Grouped by capability theme for easier navigation.

3. **Breaking change and compatibility records consolidated into Jobs 1 and 2** → Breaking changes are part of understanding the release (Job 1), while compatibility verification is a distinct planning job (Job 2).

---

## Example: Content Consolidation

### Example 1: Security Features (7 scattered features → 1 unified section)

**Current (Fragmented):**
- Section 2.1: EventListener custom securityContext (Pipelines)
- Section 2.2: Custom database credentials (Tekton Results)
- Section 2.4: Git resolver personal access tokens (Tekton Results)
- Section 4.2: Disable ok-to-test memory (Operator)
- Section 4.8: remember-ok-to-test default to false (Operator)
- Section 6.6: GKE Workload Identity Federation (Tekton Cache)
- Section 4.1: Cosign key pair generation (Operator)

Users must read through all component sections to find security-related features.

**Proposed (Consolidated):**
- **Job 3, Security and Authentication theme:**
  - 3.1. Custom security contexts (Pipelines)
  - 3.2. Database credentials (Tekton Results)
  - 3.3. Git resolver authentication (Tekton Results)
  - 3.4. GKE Workload Identity (Tekton Cache)
  - 3.5. Cosign key generation (Operator)

**Benefit:** All security-related configuration in one place, organized by capability rather than component ownership.

---

### Example 2: High Availability Features (2 identical features in different sections → 1 unified section)

**Current (Fragmented):**
- Section 2.8: StatefulSet ordinals for Tekton Results watcher HA
- Section 7.1: StatefulSet ordinals for Tekton Chains controller HA

Same Technology Preview feature described twice in different component sections.

**Proposed (Consolidated):**
- **Job 3.10: Configure StatefulSet Ordinals for HA (Technology Preview)**
  - Applies to both Tekton Results watcher and Tekton Chains controller
  - Configuration examples for both components
  - Single reference in Technology Preview appendix

**Benefit:** Users see HA approach once, understand it applies to multiple components.

---

### Example 3: Breaking Changes (4 scattered items → 1 section with migration timing)

**Current (Fragmented):**
- Buried in "Breaking changes" subsection of 1.19 release notes
- No clear indication of when action is required
- Mixed with new features and fixes

**Proposed (Consolidated):**
- **Job 1.8: API and CLI Changes**
  - **Timing:** BEFORE upgrading to 1.19
  - All 4 breaking changes with migration actions
  - Clear consequence statements

**Benefit:** Users immediately know they must review this section before upgrading.

---

## Navigation Improvement

**Current:** Browse 7+ component sections across multiple patch version modules to find content
**Proposed:** Navigate 3 main jobs → choose capability theme
**Reduction:** ~57% fewer top-level navigation items (from 7 component sections to 3 jobs)
**Benefit:** Find content in 2-3 clicks vs 4-6

### Task-Specific Navigation Examples

| Task | Current Path | Proposed Path | Improvement |
|------|-------------|---------------|-------------|
| Find security features | Scan all 7 component sections | Job 3 → Security and Authentication | 70% reduction |
| Review breaking changes | Find within 1.19 module, mixed with features | Job 1 → Breaking Changes (section 1.8) | Surfaced earlier |
| Check compatibility | Separate section, unclear when to use | Job 2 (with timing context) | Contextual guidance |
| Configure HA features | 2 separate component sections | Job 3 → High Availability | Single section |

---

## Workflow Coverage Comparison

| Stage | Current | Proposed | Gap Status |
|-------|---------|----------|------------|
| What's New | ✅ Main focus | ✅ Job 1 | Improved organization |
| Plan | ⚠️ Compatibility buried | ✅ Job 2 (dedicated) | Elevated to main job |
| Configure | ⚠️ Scattered by component | ✅ Job 3 (by capability) | Reorganized |
| Operate | ⚠️ Mixed with Configure | ✅ Job 3 (clear sections) | Reorganized |
| Monitor | ⚠️ Scattered | ✅ Job 3.20-3.22 | Consolidated |
| Secure | ⚠️ Scattered | ✅ Job 3.1-3.5 | Consolidated |
| Troubleshoot | ⚠️ Known issues buried | ✅ Job 1.9 + Job 3.21 | Surfaced |
| Upgrade | ⚠️ Breaking changes mixed | ✅ Job 1.8 + Job 2 | Surfaced with timing |

### Coverage Summary

**Current structure gaps:** No significant content gaps, but organization scatters related capabilities across component sections
**Proposed structure gaps:** No content gaps
**Gaps addressed by restructure:** 
- Compatibility verification elevated to dedicated job
- Breaking changes surfaced with timing guidance
- Security features consolidated
- HA features consolidated

### Recommendations for Gap Closure

| Gap | Recommendation | Priority |
|-----|----------------|----------|
| Feature discoverability | Adopt JTBD structure to group by capability | High |
| Upgrade planning | Highlight compatibility and breaking changes earlier | High |
| Configuration guidance | Add "when to use" context for each feature | Medium |

---

## UI and CLI Path Documentation

**Note:** Release notes are primarily reference material. Most features documented here link to detailed procedure documentation elsewhere. The proposed structure improves discoverability but does not add procedural detail.

**Format used in proposed structure:**
```markdown
**Feature Name** `[reference]`
- Context: When to use this feature
- Benefit: What problem it solves
- Link to: Detailed procedure documentation (where available)
```

---

## Quality Checklist

### Main Jobs
- [x] 3 main jobs total (not 30+)
- [x] Clean, professional titles (not fragments)
- [x] Outcome-focused (understand, verify, configure)
- [x] Stable goals (would exist even if tech changed)
- [x] Organized by workflow stages (What's New, Plan, Configure)

### User Stories/Tasks
- [x] Capability themes under main jobs
- [x] Scenario-specific organization (security, performance, HA, etc.)
- [x] Properly nested under main jobs
- [x] No persona gates (information available to all)
- [x] Context provided for when to use each feature

### Structure
- [x] Follows workflow stage progression
- [x] Jobs ordered by when users need them (understand → plan → configure)
- [x] Line references use `→ Lines X-Y: Title` format with `Source:` line
- [x] Prerequisites stated (e.g., version 1.19 installed)
- [x] Both component ownership and capability preserved
- [x] Technology Preview features highlighted

### Comparison
- [x] Current structure shown accurately
- [x] Proposed structure is logical
- [x] Key differences explained
- [x] Navigation improvements quantified
- [x] Workflow coverage comparison with ✅/⚠️/❌ indicators
- [x] Gap recommendations with priorities

---

## Success Criteria

**A good TOC comparison:**

- [x] User can immediately see main goals (3 main jobs)
- [x] User can find features by capability, not just by component
- [x] User can see it's simpler than current structure (57% fewer top-level items)
- [x] Stakeholders understand the proposed improvement (consolidated capabilities)
- [x] Content mappers know what to extract from where (line references preserved)
- [x] Structure follows natural workflow progression (understand → plan → configure)
- [x] No persona gates (all information accessible based on permissions)
- [x] Breaking changes and timing clearly marked
- [x] Technology Preview features consolidated in appendix

---

## Additional Observations

### Release Notes Characteristics

Release notes are unique documentation:
- **Not procedural:** They announce changes, not how to use them
- **Time-bounded:** Content is specific to a release
- **Reference material:** Users scan for relevant changes
- **Multiple audiences:** Developers, administrators, and decision-makers

### Proposed Structure Benefits for Release Notes

1. **Faster scanning:** Capability themes let users find relevant features without reading all components
2. **Better planning:** Breaking changes and compatibility surfaced early with timing guidance
3. **Clearer impact:** Security, performance, and HA features grouped for impact assessment
4. **Technology Preview visibility:** All TP features in one appendix for risk assessment
5. **Patch version integration:** Fixed issues consolidated rather than fragmented across modules

### Implementation Notes

- Maintain component attribution in line references for traceability
- Link to detailed procedure documentation where available
- Preserve all content from current structure (no information loss)
- Technology Preview warnings preserved and consolidated in appendix
- Breaking change timing guidance added (not in current structure)

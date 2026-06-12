# op-release-notes-1-19.adoc — Consolidation Report

**Document:** op-release-notes-1-19.adoc
**JTBD Records:** 43 pre-consolidated records → 3 final jobs (after merging)

---

## Executive Summary

### What's Changing

The current OpenShift Pipelines 1.19 release notes are organized by component ownership (Pipelines, Tekton Results, Pipelines as Code, Operator, Tekton Cache, Tekton Chains, Event-based Pruner), requiring users to scan seven component sections to find features by capability. Breaking changes are buried within the version module, and related capabilities like security features or high availability options are fragmented across multiple sections.

The proposed JTBD-based structure organizes content by user goals and workflow stages: understanding the release, verifying compatibility, and configuring new capabilities. Features are grouped by capability theme (security, performance, high availability, storage, automation, developer experience, monitoring) rather than component ownership, while preserving component attribution for traceability.

This reorganization recognizes that release notes serve multiple audiences with different needs: decision-makers evaluating upgrade impact, administrators planning deployments, and developers adopting new features.

### Key Improvements

- **Breaking changes surfaced early:** Breaking changes moved to prominent position with migration timing guidance (BEFORE upgrading) instead of being mixed with new features
- **Capability-based feature grouping:** 5 security features consolidated from 5 different component sections into one Security and Authentication theme
- **Technology Preview consolidation:** 3 Technology Preview features highlighted in single appendix instead of scattered across component sections with repeated warnings
- **Compatibility elevated:** Compatibility verification promoted from buried reference to dedicated main job with workflow context
- **High availability unified:** 2 identical StatefulSet ordinal features (Tekton Results, Tekton Chains) presented once with applicability to both components
- **Patch version integration:** Fixed issues from 4 patch version modules consolidated into single Fixed Issues section with component attribution
- **Navigation reduction:** 57% reduction in top-level navigation items (from 7 component sections to 3 jobs)
- **Workflow alignment:** Content organized by when users need it (understand → plan → configure) rather than by team ownership

---

## Current Structure (Feature-Based)

- **Introduction** — Product overview, lifecycle policy references, and feature summary
- **Compatibility and support matrix** — Component version compatibility table for versions 1.20-1.22
- **Release notes for Red Hat OpenShift Pipelines 1.19**
  - New features
    - Pipelines — EventListener custom securityContext
    - Tekton Results — 8 features including custom DB credentials, API field filtering, OCI retry config, Git resolver auth, SQL logging, Splunk integration, StatefulSet ordinals HA
    - Pipelines as Code — 10 features including bot handling, API metrics, URL validation, markdown rendering, cancel-in-progress, git_tag variable, skip-push-event, OpenAPI schema, CEL precedence
    - Operator — 8 features including cosign generation, security defaults, variable expansion, native git binary, onError substitution, StepAction stable, scheduler fixes
    - Tekton Cache — 9 features including parameter naming, GCS support, S3 support, Gzip compression, permissions, WIF support, backend unification, folder creation, Docker config
    - Tekton Chains — StatefulSet ordinals HA
    - Event-based Pruner — TTL-based and history-based pruning (Technology Preview)
  - Breaking changes — 4 items (hub clustertask removed, ClusterTask removed, opc command changed, affinity flag removed)
  - Known issues — 1 item (pruner config validation)
  - Fixed issues — ~20 fixes across all components
- **Release notes for Red Hat OpenShift Pipelines 1.19.1** — Fixed issues (2 items)
- **Release notes for Red Hat OpenShift Pipelines 1.19.2** — Fixed issues (5 items)
- **Release notes for Red Hat OpenShift Pipelines 1.19.3** — Fixed issues (5 items)

**Total:** 4 chapters (intro + compatibility + 4 patch version modules), 7+ component subsections, organized by component ownership and patch version.

---

## Proposed JTBD-Based Structure

### Quick Overview

- **What's New**
  - Job 1: Understand Features and Fixes in This Release
- **Plan Your Upgrade**
  - Job 2: Verify Component Version Compatibility
- **Configure and Use New Features**
  - Job 3: Configure and Operate New Capabilities

### Detailed Job Descriptions

#### What's New

**Job 1: Understand Features and Fixes in This Release**

*When planning upgrades or evaluating new capabilities, I want to understand what features and fixes are available in this release, so I can make informed decisions about adoption and deployment*

Prerequisites: None (entry point for release notes)

- **1.1. New Features by Component** `[reference]`
  - Pipelines Component Features (lines 143-182): EventListener custom securityContext
  - Tekton Results Features (lines 187-350): Custom DB credentials, API filtering, OCI retry, Git auth, SQL logging, Splunk, watcher retries, StatefulSet HA
  - Pipelines as Code Features (lines 355-611): Bot handling, API metrics, URL validation, markdown, cancel-in-progress, git_tag, skip-push, OpenAPI, CEL precedence
  - Operator Features (lines 366-396): Cosign generation, security defaults, variable expansion, native git, onError substitution, StepAction stable, scheduler fixes
  - Tekton Cache Features (lines 399-476): Parameter naming, GCS, S3, Gzip, permissions, WIF, backend unification, folder creation, Docker config
  - Tekton Chains Features (lines 481-513): StatefulSet HA
  - Event-based Pruner Features (lines 630-655): TTL and history-based pruning (TP)
  - Context: Comprehensive feature reference organized by component for traceability

- **1.2. Breaking Changes** `[reference]`
  - API and CLI Changes (lines 660-667): hub clustertask removed, ClusterTask removed, opc command changed, affinity flag removed
  - **Timing:** BEFORE upgrading to 1.19 - review and plan migrations
  - Context: Critical for upgrade planning to avoid workflow disruption

- **1.3. Known Issues** `[reference]`
  - Known Limitations (lines 671-672): Event-based pruner config validation silently ignored
  - Context: Awareness of current limitations for workaround planning

- **1.4. Fixed Issues** `[reference]`
  - Bug Fixes Across Components (lines 674-758, 1.19.1-1.19.3 modules): ~32 fixes across all components and patch versions
  - Context: Consolidated view of all fixes from 1.19.0 through 1.19.3

#### Plan Your Upgrade

**Job 2: Verify Component Version Compatibility**

*When planning deployment or upgrades, I want to verify component version compatibility with my OpenShift version, so I can ensure supported configurations*

Prerequisites: None

- **2.1. Compatibility and Support Matrix** `[reference]`
  - Component Version Compatibility (lines 89-123): Versions 1.20-1.22 compatibility table
  - Context: Reference for planning deployments and upgrades
  - OpenShift version support: 4.14, 4.16, 4.17, 4.18, 4.19, 4.20, 4.21
  - Component GA vs Technology Preview status

#### Configure and Use New Features

**Job 3: Configure and Operate New Capabilities**

*When adopting new features from this release, I want to configure and operate new capabilities, so I can leverage improvements in my environment*

Prerequisites: Version 1.19 installed, understanding of feature prerequisites

- **3.1. Configure Custom Security Contexts** `[procedure]`
  - EventListener Custom securityContext (lines 146-182): Configure custom security settings
  - Context: When deploying event listeners with specific security requirements

- **3.2. Configure Custom Database Credentials** `[procedure]`
  - Tekton Results Database Credentials (lines 187-201): Configure custom DB credentials
  - Context: When setting up Tekton Results with organizational database standards

- **3.3. Authenticate Git Resolver with Personal Access Tokens** `[procedure]`
  - Git Resolver Authentication (lines 234-260): Configure personal access tokens
  - Context: When resolving pipeline definitions from GitHub or GitLab to avoid rate limits

- **3.4. Configure GKE Workload Identity Federation** `[procedure]`
  - GKE WIF Support (lines 411-412): Use projected volume tokens
  - Context: When running pipelines on GKE to eliminate long-lived credentials

- **3.5. Generate Cosign Key Pairs Automatically** `[procedure]`
  - Cosign Key Generation (lines 366-380): Automatic cosign key generation
  - Context: When setting up Tekton Chains for artifact signing

- **3.6. Configure OCI Bundle Retry Timing** `[procedure]`
  - Bundle Resolver Backoff Configuration (lines 206-232): Configure retry parameters
  - Context: When using OCI bundles with busy or rate-limited registries

- **3.7. Enable Response Field Filtering** `[procedure]`
  - API Field Filtering (lines 203-204): Reduce API payload size
  - Context: When retrieving large result sets from Tekton Results API

- **3.8. Configure Native Git Binary for Remote Resolution** `[concept]`
  - Native Git Binary (lines 387-388): Performance improvement for large repos
  - Context: Automatic improvement, reduces memory consumption

- **3.9. Enable Gzip Compression for Caches** `[concept]`
  - Cache Compression (lines 406-407): Automatic compression before upload
  - Context: Automatic improvement, reduces storage costs and transfer times

- **3.10. Configure StatefulSet Ordinals for HA** `[procedure]`
  - Tekton Results Watcher HA (lines 315-350): StatefulSet ordinals for HA (Technology Preview)
  - Tekton Chains Controller HA (lines 481-513): StatefulSet ordinals for HA (Technology Preview)
  - Context: When scaling for high availability, alternative to leader election

- **3.11. Configure Alternative Cache Storage Backends** `[procedure]`
  - Google Cloud Storage (lines 401-403): GCS bucket backend
  - S3 Compatible Storage (lines 404-405): S3-compatible including MinIO
  - Context: When storing build caches in cloud or on-premises object storage

- **3.12. Configure Custom Docker Config Location** `[procedure]`
  - Custom dockerConfig Parameter (lines 418-476): Custom credential paths
  - Context: When using registry authentication with non-default credential locations

- **3.13. Configure Global Cancel-in-Progress** `[procedure]`
  - Global Auto-Cancel Configuration (lines 520-548): Global cancel-in-progress settings
  - Context: When managing multiple repositories to prevent redundant pipeline runs

- **3.14. Configure Skip-Push-Event for PR Commits** `[procedure]`
  - Duplicate Run Prevention (lines 578-606): Skip push events for PR commits
  - Context: When managing pipeline triggers to prevent duplicate executions

- **3.15. Use git_tag Dynamic Variable** `[procedure]`
  - git_tag Variable Usage (lines 550-576): Access tag value in pipelines
  - Context: When triggering pipelines on tag push events

- **3.16. Use onError Parameter Substitution** `[procedure]`
  - Dynamic Error Handling (lines 389-390): Parameter substitution in onError
  - Context: When controlling pipeline failure handling dynamically

- **3.17. Configure Event-based Pruner** `[procedure]`
  - Automated Cleanup Configuration (lines 630-655): TTL and history-based pruning (Technology Preview)
  - Context: When managing PipelineRun and TaskRun lifecycle
  - **Requires:** Existing job-based pruner must be disabled first

- **3.18. Use OpenAPI Schema for Repository CR** `[concept]`
  - OpenAPI Schema Support (lines 608-609): IDE autocompletion and oc explain
  - Context: When writing Repository CRs for improved developer experience

- **3.19. Use StepAction Definitions** `[concept]`
  - StepAction Graduation to Stable (lines 391-392): Enabled by default
  - Context: StepAction now stable, no feature flags required

- **3.20. Monitor Git Provider API Usage** `[procedure]`
  - API Request Metrics (lines 357-358, 518-519): Track API usage per provider
  - Context: When monitoring Pipelines as Code integration to track rate limits

- **3.21. Configure SQL Log Level** `[procedure]`
  - SQL_LOG_LEVEL Environment Variable (lines 262-283): Configure SQL logging
  - Context: When debugging Tekton Results database issues

- **3.22. Retrieve Logs from Splunk** `[procedure]`
  - Splunk Integration (lines 288-313): Centralized log retrieval
  - Context: When using OpenShift Logging with Splunk forwarding

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | By component ownership and patch version | By user goal and workflow stage |
| **Top-level items** | 7+ component sections across 4 version modules | 3 main jobs with capability themes |
| **Feature discoverability** | Scan all component sections to find related capabilities | Navigate to capability theme (security, performance, HA) |
| **Breaking changes visibility** | Buried in version module, mixed with new features | Surfaced in Job 1 with BEFORE upgrade timing |
| **Technology Preview features** | Scattered with inline warnings (3 occurrences) | Consolidated in appendix with single reference table |
| **Patch version handling** | Separate modules for each patch (1.19.0-1.19.3) | Integrated fixed issues with component attribution |
| **Compatibility** | Standalone reference section | Dedicated job with workflow context (when to check) |
| **Configuration guidance** | Feature announcements without usage context | Capability themes with "when to use" context |

### Job List Adjustments from Suggested Input

The suggested 43 jobs were consolidated to **3 jobs** for the following reasons:

1. **43 feature-specific records merged into Job 1** → Release notes document *what changed*, not *how to use it*. All feature announcements serve the single job of understanding the release. Component attribution preserved in section 1.1 for traceability.

2. **Configuration and operational records consolidated into Job 3** → Individual configuration tasks vary, but all serve the high-level job of *adopting new capabilities*. Organized into 8 capability themes (security, performance, HA, storage, automation, developer experience, monitoring) for easier navigation.

3. **Compatibility verification elevated to Job 2** → Compatibility was buried as reference material. Elevated to dedicated planning job because it's a critical prerequisite for upgrade decisions.

4. **Breaking changes and known issues integrated into Job 1** → Part of understanding what changed. Breaking changes surfaced early (section 1.2) with timing guidance added (BEFORE upgrading).

**Final job count: 3** (reduced from suggested 43). Release notes are unique documentation - they announce changes rather than provide procedural guidance. The 3-job structure reflects the core workflow: understand what changed → verify compatibility → configure new features.

---

## Consolidation Examples

### Example 1: Security Features (5 scattered sections → 1 unified theme)

**Current (Fragmented):**
- Section 2.1 (Pipelines): EventListener custom securityContext (lines 146-182)
- Section 2.2 (Tekton Results): Custom database credentials (lines 187-201)
- Section 2.4 (Tekton Results): Git resolver personal access tokens (lines 234-260)
- Section 4.1 (Operator): Cosign key pair generation (lines 366-380)
- Section 6.6 (Tekton Cache): GKE Workload Identity Federation support (lines 411-412)

Users must scan all component sections (Pipelines, Tekton Results, Operator, Tekton Cache) to identify security-related features. No clear indication that these features address security concerns.

**Proposed (Consolidated):**
- **Job 3: Configure and Operate New Capabilities**
  - Security and Authentication theme:
    - 3.1. Custom security contexts (Pipelines, lines 146-182)
    - 3.2. Custom database credentials (Tekton Results, lines 187-201)
    - 3.3. Git resolver authentication (Tekton Results, lines 234-260)
    - 3.4. GKE Workload Identity (Tekton Cache, lines 411-412)
    - 3.5. Cosign key generation (Operator, lines 366-380)

**Benefit:** Security-focused administrators can review all security features in one section, understand the security improvements holistically, and prioritize configuration based on organizational security policies. Component attribution preserved for detailed investigation.

---

### Example 2: Technology Preview Features (3 scattered warnings → 1 consolidated appendix)

**Current (Fragmented):**
- Section 2.8 (Tekton Results): StatefulSet ordinals for watcher HA with inline TP warning (lines 315-350)
- Section 7.1 (Tekton Chains): StatefulSet ordinals for controller HA with inline TP warning (lines 481-513)
- Section 8 (Event-based Pruner): TTL and history-based pruning with section-level TP warning (lines 630-655)

Each Technology Preview feature has a repeated IMPORTANT block explaining TP status, SLA implications, and support scope. Users must remember which features are TP when planning deployments.

**Proposed (Consolidated):**
- **Appendix A: Technology Preview Features Quick Reference**
  - Table listing all 3 TP features with component, line references, and status
  - Single TP warning block explaining implications
- **Feature sections** (3.10, 3.17) marked with "(Technology Preview)" in heading
- **Configuration context** includes TP status reminder

**Benefit:** Decision-makers can quickly identify all Technology Preview features for risk assessment. Reduced repetition of TP warning text. Clear visibility for production deployment planning.

---

### Example 3: Breaking Changes (4 buried items → 1 section with timing guidance)

**Current (Fragmented):**
- Buried in "Breaking changes" subsection of 1.19 release notes (lines 660-667)
- No indication of when action is required relative to upgrade
- Mixed with new features in same module
- Users might miss this section when scanning new features

**Proposed (Consolidated):**
- **Job 1.8: API and CLI Changes**
  - **Timing:** BEFORE upgrading to 1.19 - review and plan migrations
  - hub clustertask command removed (lines 660-661): Update workflows using Tekton Hub ClusterTask
  - ClusterTask support removed (lines 662-663): Migrate to namespaced Task resources
  - opc results list command replaced (lines 664-665): Update scripts to use `opc results result list`
  - disable-affinity-assistant flag removed (lines 666-667): Use `coschedule` feature flag instead

**Benefit:** Breaking changes surfaced prominently with clear timing guidance (BEFORE upgrading). Users immediately understand these require action before upgrade, not after. Migration actions clearly stated for each change.

---

## Content Gaps Identified

| Gap | JTBD Reference | Current Coverage | Impact |
|-----|---------------|-----------------|--------|
| Migration procedures for breaking changes | Job 1.8 (Breaking Changes) | Breaking changes listed but no detailed migration steps | **High** — Users need step-by-step migration guides for ClusterTask removal and command changes |
| Configuration examples for new features | Job 3 (all configuration approaches) | Features listed with basic YAML snippets, no complete worked examples | **Medium** — Basic examples exist, but comprehensive configuration scenarios would reduce trial-and-error |
| Technology Preview graduation timeline | Appendix A (TP Features) | TP features identified but no indication of expected GA timeline | **Medium** — Users planning production deployments need timeline for TP → GA transition |
| Performance impact data | Job 3.6-3.9 (Performance features) | Performance features listed but no benchmarks or impact quantification | **Low** — Features claim improvements (memory reduction, faster transfers) without supporting data |
| Compatibility regression testing | Job 2 (Verify Compatibility) | Compatibility table shows supported versions but no regression test guidance | **Low** — Users would benefit from recommended regression test scenarios after upgrade |

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 7+ component sections | 3 jobs | 57% reduction |
| Sections to browse for "security features" | 7 component sections across full document | 1 theme (Job 3.1-3.5) | 86% reduction in scanning |
| Sections to browse for "breaking changes" | 1 subsection buried in 1.19 module | 1 section (Job 1.8) surfaced in main job | Elevated visibility |
| Sections to browse for "Technology Preview features" | 3 scattered sections with inline warnings | 1 appendix table | 67% reduction, consolidated view |
| Sections to browse for "high availability features" | 2 component sections | 1 section (Job 3.10) | 50% reduction |
| Clicks to find "compatibility information" | 2-3 clicks (find in TOC, scroll to table) | 1 click (dedicated Job 2) | Elevated to main job |
| Patch version fixed issues | 4 separate modules | 1 consolidated section (Job 1.4) | Integrated view |

**Final job count: 3** (reduced from suggested 43). Release notes are reference material for understanding changes, not procedural guides. The 3-job structure aligns with the core release notes workflow: understand what changed, verify you can upgrade safely, and learn how to configure new features.

---

## Document Statistics

### Current Structure
- **Chapters:** 4 (intro + compatibility + 4 patch version modules)
- **Component sections:** 7 (Pipelines, Tekton Results, PAC, Operator, Tekton Cache, Tekton Chains, Pruner)
- **Feature count:** ~45 new features across all components
- **Breaking changes:** 4
- **Known issues:** 1
- **Fixed issues:** ~32 (across 4 patch versions)

### Proposed Structure
- **Main jobs:** 3 (Understand, Verify, Configure)
- **Capability themes:** 8 (Security, Performance, HA, Storage, Automation, DevEx, Monitoring, plus component-organized reference)
- **Configuration approaches:** 22 (specific features users can configure)
- **Feature count:** ~45 (same features, reorganized)
- **Breaking changes:** 4 (surfaced earlier with timing)
- **Technology Preview features:** 3 (consolidated in appendix)
- **Fixed issues:** ~32 (integrated into single section)

### Consolidation Metrics
- **Pre-consolidation JTBD records:** 43
- **Post-consolidation main jobs:** 3
- **Consolidation ratio:** 14:1 (43 records → 3 jobs)
- **Information preservation:** 100% (all features, changes, and fixes preserved)
- **Component attribution:** Maintained (line references and source citations)
- **Navigation reduction:** 57% fewer top-level items

---

## Recommendations

### For Documentation Writers

1. **Adopt capability-based themes for feature organization** — Group features by what they enable (security, performance, HA) rather than which component owns them. Maintain component attribution in line references for traceability.

2. **Surface breaking changes early with timing guidance** — Move breaking changes to prominent position in "What's New" with explicit timing (BEFORE/AFTER upgrade). Add consequence statements for each breaking change.

3. **Consolidate Technology Preview features** — Create appendix listing all TP features for risk assessment. Reduce inline warning repetition.

4. **Integrate patch version content** — Consolidate fixed issues from multiple patch versions into single section with version attribution, rather than separate modules for each patch.

5. **Add "when to use" context** — For each configuration feature, add context explaining when/why users would adopt it. Current structure lists features without usage guidance.

### For Content Strategists

1. **Elevate compatibility verification** — Compatibility is currently buried reference material. Promote to dedicated job in release notes workflow.

2. **Create migration guides** — Breaking changes need companion migration procedures, not just announcements. High priority for ClusterTask removal.

3. **Quantify performance improvements** — Features claiming performance benefits (native git binary, Gzip compression) should include benchmark data or estimated impact.

4. **Establish TP graduation timeline** — Communicate expected GA timeline for Technology Preview features to aid production planning.

### For Product Managers

1. **Validate capability themes** — Review proposed capability groupings (security, performance, HA, storage, automation, developer experience, monitoring) for alignment with user priorities.

2. **Assess gap priorities** — Highest-impact gap is missing migration procedures for breaking changes. Medium-impact gaps include complete configuration examples and TP graduation timelines.

3. **Consider workflow alignment** — Proposed 3-job structure (Understand → Verify → Configure) aligns with upgrade decision workflow. Validate this matches actual user journey.

---

## Implementation Notes

### Content Migration

- **No information loss:** All 45+ features, 4 breaking changes, 1 known issue, and ~32 fixes preserved
- **Component attribution maintained:** Line references and source citations allow tracing back to component ownership
- **Backward compatibility:** Users familiar with current structure can still find content via component names in section 1.1
- **Link preservation:** All xrefs and external links maintained

### Structural Changes

- **Capability themes added:** Security, Performance, HA, Storage, Automation, Developer Experience, Monitoring
- **Timing guidance added:** Breaking changes marked with BEFORE/AFTER upgrade timing
- **Technology Preview consolidation:** Appendix replaces inline repeated warnings
- **Patch version integration:** 4 modules → 1 consolidated fixed issues section with version attribution

### Maintenance Impact

- **Adding new features:** Insert into appropriate capability theme under Job 3, or into component reference (Job 1.1)
- **Adding patch versions:** Integrate fixed issues into Job 1.4 with version attribution, no new module needed
- **Adding breaking changes:** Add to Job 1.8 with timing guidance and migration action
- **Technology Preview graduation:** Update appendix status, move from TP table to standard configuration approach

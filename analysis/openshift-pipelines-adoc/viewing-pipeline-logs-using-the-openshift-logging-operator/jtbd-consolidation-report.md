# Viewing pipeline logs by using the OpenShift Logging Operator — Consolidation Report

**Document:** viewing-pipeline-logs-using-the-openshift-logging-operator.adoc
**JTBD Records:** 2 pre-consolidated main jobs → 1 final job (after merging)

---

## Executive Summary

### What's Changing

The current documentation is organized around the Kibana tool and presents a linear procedure for viewing pipeline logs. While functional, this tool-centric approach obscures the underlying user goal: accessing pipeline logs after pods have been deleted.

The pain this causes includes:
- **Hidden prerequisites**: Users must read into the procedure to discover they need OpenShift Logging and Elasticsearch Operators installed first
- **Unclear motivation**: The procedure title doesn't explain WHY users would use Kibana instead of other log viewing methods
- **Missing context**: No guidance on when to use this approach versus alternatives (e.g., `oc logs` for live pods)
- **Embedded reference material**: Filter query examples are scattered within procedural steps instead of being available as quick reference

The proposed structure reorganizes the content by user goal and workflow stage (Observe), making the job outcome explicit and surfacing prerequisites and context at the job level.

### Key Improvements

- **Prerequisites surfaced early:** OpenShift Logging/Elasticsearch Operator requirements visible at job level instead of buried in procedure section
- **Explicit goal statement:** "Access Pipeline Logs Independently of Pod Lifecycle" makes the outcome clear before users read implementation details
- **Timing guidance added:** Clarifies this job happens AFTER operator installation and explains consequences of missing prerequisites
- **Reference material extracted:** Filter query examples moved to dedicated appendix for quick lookup
- **Task grouping introduced:** 7 sequential steps reorganized into 5 thematic task groups (access, pattern, filter, select, validate)
- **Gaps identified and prioritized:** Missing Get Started and Troubleshoot content flagged with High priority recommendations

---

## Current Structure (Feature-Based)

- **Viewing pipeline logs by using the OpenShift Logging Operator** — Assembly explaining pod log storage and Kibana solution
  - Abstract — Problem statement (ephemeral pods) and solution (OpenShift Logging Operator + Kibana)
  - **Viewing pipeline logs in Kibana** — Procedure module
    - Prerequisites section — Lists operator installations and cluster admin requirement
    - Procedure (7 steps)
      - Step 1: Log in to OpenShift web console
      - Step 2: Navigate to Kibana (grid icon → Observability → Logging)
      - Step 3: Create index pattern (2-step wizard with wildcard and @timestamp)
      - Step 4: Add filters (4 DSL query examples + graphical approach example)
        - Filter Tekton-managed containers
        - Exclude place-tools container
        - Filter pipelineRun labels
        - Filter pipeline labels
      - Step 5: Select fields (kubernetes.flat_labels and message)
      - Step 6-7: View filtered messages
  - Additional resources — 3 external links to OpenShift Logging documentation

**Total:** 1 assembly, 1 procedure module, organized by tool (Kibana).

---

## Proposed JTBD-Based Structure

### Quick Overview

- **Observe System State**
  - Job 1: Access Pipeline Logs Independently of Pod Lifecycle

### Detailed Job Descriptions

#### Observe System State

**Job 1: Access Pipeline Logs Independently of Pod Lifecycle**

*When pipeline runs, task runs, and event listeners complete and their pods are deleted, I want to access pipeline logs independently of pod lifecycle, so I can review logs even after pods are deleted for troubleshooting and audit requirements*

Prerequisites: OpenShift Elasticsearch Operator installed, OpenShift Logging Operator installed, cluster administrator permissions

- **1.1. Configure Kibana for Pipeline Log Access (The "Complete Setup")** `[procedure]`
  - Lines 97-182 (modules/op-viewing-pipeline-logs-in-kibana.adoc): Complete Kibana configuration including web console access, index pattern creation with wildcard and @timestamp configuration, filter setup using DSL queries for Tekton-managed containers (excluding place-tools, highlighting pipelineRun and pipeline labels), field selection (kubernetes.flat_labels and message), and log message verification
  - Context: UI-based method for cluster administrators requiring no CLI expertise; only documented approach in this guide for persistent log access

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | By tool (Kibana) and linear procedure steps | By user goal (access logs after pod deletion) and workflow stage (Observe) |
| **Top-level items** | 1 assembly with 1 procedure (7 steps) | 1 main job with 1 configuration approach (5 task groups) |
| **Entry point** | "Viewing pipeline logs in Kibana" (tool name) | "Access Pipeline Logs Independently of Pod Lifecycle" (user outcome) |
| **Prerequisites** | Buried in procedure section after title | Surfaced at job level with timing guidance (AFTER operators installed) |
| **Motivation** | Implicit (inferred from assembly abstract) | Explicit ("When X, I want Y, so I can Z" format) |
| **Task organization** | Sequential steps (1-7) | Thematic groups (access console, create pattern, configure filters, select fields, validate) |
| **Reference material** | Embedded in step 4 (filter examples) | Dedicated Appendix A (Filter Query Reference table) |
| **Context guidance** | Not provided | Explains when/why to use Kibana approach |
| **Gap visibility** | Not addressed | Gaps identified with High/Medium/Low priority recommendations |

### Job List Adjustments from Suggested Input

The suggested 2 jobs were consolidated to **1 job** for the following reasons:

1. **Jobs 1 and 2 ("Access pipeline logs independently of pod lifecycle" main job + "Configure Kibana" user story) merged** → The JTBD analysis initially separated the goal (Job 1) from the implementation (Job 2). However, since this guide documents only ONE approach to achieving the goal (Kibana configuration), treating Kibana configuration as a standalone job would be misleading. Instead, Kibana configuration becomes the sole user story/approach under the main job. This consolidation accurately reflects that configuration is the METHOD, not a separate GOAL. If future content added alternative methods (e.g., CLI-based log export, third-party observability tools), those would become additional user stories under Job 1.

---

## Consolidation Examples

### Example 1: Linear Procedure → Hierarchical Task Structure (7 steps → 5 task groups)

**Current (Fragmented):**
- Step 1: Log in to OpenShift web console
- Step 2: Navigate to Kibana
- Step 3: Create index pattern (substep a-d)
- Step 4: Add filters (substep a-b with 4 filter examples)
- Step 5: Select fields from Available fields list
- Step 6: Ensure fields appear under Selected fields
- Step 7: View logs in message field

Users follow a flat list of 7 steps with substeps, making it unclear which steps are logically related or serve the same purpose.

**Proposed (Consolidated):**
- **Job 1: Access Pipeline Logs Independently of Pod Lifecycle**
  - 1.1. Configure Kibana for Pipeline Log Access
    - Task: Access Kibana web console (Steps 1-2 combined)
    - Task: Create index pattern for pipeline logs (Step 3)
    - Task: Configure filters for Tekton pipeline containers (Step 4 with 4 filter types)
    - Task: Select relevant log fields for display (Steps 5-6 combined)
    - Validation: View filtered pipeline log messages (Step 7)

**Benefit:** Logically grouped tasks with clear purpose statements; validation separated from configuration; 5 task groups instead of 7 sequential steps reduce cognitive load and improve scannability.

---

### Example 2: Embedded Filter Examples → Dedicated Reference Appendix (Scattered examples → Reference table)

**Current (Fragmented):**
- Line 117-132: Example query to filter pipelines containers (JSON DSL)
- Line 134-137: Example of filtering using drop-down fields (graphical approach with screenshot)
- Line 139-154: Example query to filter pipelineRun in labels (JSON DSL)
- Line 156-171: Example query to filter pipeline in labels (JSON DSL)

Users must scroll through procedural text to find filter syntax, and there's no quick way to compare filter patterns or understand when to use each approach.

**Proposed (Consolidated):**
- **Appendix A: Kibana Filter Query Reference**
  - Table with columns: Filter Purpose, Query Type, Example
  - Row 1: Tekton-managed containers | DSL match query | `app_kubernetes_io/managed-by=tekton-pipelines`
  - Row 2: Exclude place-tools | Graphical drop-down | Field negation filter
  - Row 3: PipelineRun highlighting | DSL match query | `tekton_dev/pipelineRun=`
  - Row 4: Pipeline highlighting | DSL match query | `tekton_dev/pipeline=`

**Benefit:** Quick reference lookup without reading procedure; tabular format enables scanning; clear distinction between DSL and graphical methods; users can bookmark appendix for repeated use.

---

## Content Gaps Identified

| Gap | JTBD Reference | Current Coverage | Impact |
|-----|---------------|-----------------|--------|
| No operator installation guidance | Job 1 prerequisites | Mentioned as prerequisite but not documented | **High** — Users cannot complete the job without operators installed; likely causes confusion and support tickets |
| No troubleshooting for missing logs | Job 1 validation step | Not addressed | **High** — If logs don't appear after configuration, users have no guidance on root cause (permissions, operator status, log collection failures) |
| No troubleshooting for failed filters | Job 1 filter configuration task | Not addressed | **High** — Complex DSL queries prone to syntax errors; no debugging guidance provided |
| No log retention policy configuration | Job 1 (overall job) | Not mentioned | **Medium** — Users may exhaust storage or lose audit logs without retention guidance; operational concern |
| No guidance on alternative log viewing methods | Job 1 context | Not addressed | **Medium** — Users don't know when to use Kibana vs `oc logs` vs external tools; missing decision criteria |
| No CLI alternative documented | Job 1 configuration approach | UI-only method | **Medium** — Automation and CI/CD workflows require scriptable log access; UI method doesn't scale |
| No filter query reference for task runs or event listeners | Appendix A | Only pipelineRun and pipeline filters shown | **Low** — Users can adapt existing patterns but would benefit from explicit examples |
| No storage requirements or cost considerations | Job 1 prerequisites | Not addressed | **Low** — Elasticsearch storage costs can be significant; users may benefit from planning guidance |

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 1 procedure | 1 job | Clarity: "Access Pipeline Logs" vs "Viewing pipeline logs in Kibana" makes outcome explicit |
| Clicks to understand prerequisites | 2 (click procedure → scroll to prerequisites section) | 1 (prerequisites visible at job level) | ~50% reduction in navigation |
| Sections to browse for filter syntax | 1 procedure (scroll through step 4) | 1 appendix table (scan 4 rows) | ~75% time reduction for lookup tasks |
| Steps to validate configuration | 7 (read all steps to reach validation) | 5 task groups with validation step explicit | Validation purpose clear from structure |
| Clicks to find troubleshooting guidance | N/A (not documented) | N/A (gap identified) | No improvement yet; gap flagged for High priority |

**Final job count: 1** (reduced from suggested 2). Kibana configuration is the only documented method for achieving persistent log access, so it becomes a user story under the main job rather than a separate job. This consolidation accurately reflects that configuration is the implementation approach, not a distinct goal.

---

## Document Statistics

**Workflow Coverage:**
- Get Started: ❌ Gap (no operator installation)
- Configure: ✅ 1 job (Kibana setup)
- Observe: ✅ 1 job (log viewing)
- Troubleshoot: ❌ Gap (no debugging guidance)
- Reference: ⚠️ Limited (filter examples only)

**Main Jobs:** 1
**User Stories/Paths:** 1 (Kibana configuration approach)
**Source Sections:** 1 procedure module
**Platform/Tool Variations:** 1 (Kibana web console; no CLI documented)
**Gaps Identified:** 8 (3 High, 3 Medium, 2 Low priority)

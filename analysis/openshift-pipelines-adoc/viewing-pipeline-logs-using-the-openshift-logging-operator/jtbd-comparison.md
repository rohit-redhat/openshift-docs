# Viewing pipeline logs by using the OpenShift Logging Operator - TOC Comparison

**Current Feature-Based vs. Proposed JTBD-Based Structure**

**Analysis Date:** 2026-06-11
**JTBD Records:** 2
**Main Jobs:** 1 (rolled up from records)
**Coverage:** Basic schema (no research extensions)

---

## Current Structure (Feature-Based)

Viewing pipeline logs by using the OpenShift Logging Operator
- Abstract: Explains the problem (pods store logs but are ephemeral) and solution (OpenShift Logging Operator + Kibana)
- Viewing pipeline logs in Kibana (Procedure)
  - Prerequisites
  - Procedure (7 numbered steps)
    - Log in to web console
    - Navigate to Kibana
    - Create index pattern (2-step wizard)
    - Add filters (4 example filters with DSL queries)
    - Select fields
    - View logs
- Additional resources (3 external links)

**Total:** 1 assembly with 1 included procedure module, organized by tool/feature (Kibana).

---

## Proposed JTBD-Based Structure

## Observe System State

**Job 1: Access Pipeline Logs Independently of Pod Lifecycle**

*When pipeline runs, task runs, and event listeners complete and their pods are deleted, I want to access pipeline logs independently of pod lifecycle, so I can review logs even after pods are deleted for troubleshooting and audit requirements*

Personas: Cluster administrator
Prerequisites: OpenShift Elasticsearch Operator installed, OpenShift Logging Operator installed, cluster administrator permissions

- **1.1. Configure Kibana for Pipeline Log Access (The "Complete Setup")** `[procedure]`
  → Lines 97-182: Viewing pipeline logs in Kibana (Procedure module): Complete setup including web console access, index pattern creation, filter configuration with DSL queries, field selection, and verification
  Source: modules/op-viewing-pipeline-logs-in-kibana.adoc
  - Context: UI-based method for cluster administrators; no CLI alternative documented
  - Tasks:
    - Access Kibana web console (Lines 97-99)
    - Create index pattern for pipeline logs (Lines 101-106)
    - Configure filters for Tekton pipeline containers (Lines 107-172)
    - Select relevant log fields for display (Lines 173-178)
    - Validate filtered log messages (Lines 179-182)

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | By tool (Kibana) and procedure steps | By user goal (accessing logs independently of pod lifecycle) and workflow stage (Observe) |
| **Top-level items** | 1 assembly with 1 procedure | 1 main job with 1 user story (configuration approach) |
| **Entry point** | "Viewing pipeline logs in Kibana" (tool-centric) | "Access Pipeline Logs Independently of Pod Lifecycle" (outcome-centric) |
| **Navigation** | Linear procedure with 7 steps | Hierarchical: Job → User Story → Tasks with clear goal statements |
| **Prerequisites visibility** | Buried in procedure prerequisites section | Surfaced at job level with timing guidance |
| **Context** | Implicit (must read procedure to understand when to use) | Explicit "When" statement and context explanation |
| **Troubleshooting** | Not addressed | Gap identified with recommendations |

### Job List Adjustments from Suggested Input

The suggested 2 jobs were consolidated to **1 job** for the following reasons:

1. **Jobs 1 and 2 ("Access pipeline logs independently of pod lifecycle" main job + "Configure Kibana" user story) merged** → The "Viewing pipeline logs in Kibana" procedure is the only documented approach to achieving the main goal. Rather than treating configuration as a separate job, it becomes the sole user story under the main job. This reflects the reality that Kibana configuration IS the method for accessing logs in this guide.

---

## Consolidation Examples

### Example 1: Kibana Configuration (1 procedure → 1 job with structured tasks)

**Current (Linear Procedure):**
- Procedure: Viewing pipeline logs in Kibana
  - 7 numbered steps (lines 97-182)
  - Prerequisites section
  - Flat step list

Users must read through all 7 steps sequentially to understand the workflow. Prerequisites are separated from the procedure context.

**Proposed (Goal-Oriented with Structured Tasks):**
- **Job 1: Access Pipeline Logs Independently of Pod Lifecycle**
  - 1.1. Configure Kibana for Pipeline Log Access
    - Task: Access Kibana web console
    - Task: Create index pattern
    - Task: Configure filters (4 filter types)
    - Task: Select fields
    - Validation: View filtered messages

**Benefit:** Clear goal hierarchy with prerequisites surfaced at job level; tasks grouped by purpose (access, pattern, filter, select, validate) instead of sequential steps.

---

### Example 2: Filter Configuration (Embedded examples → Reference appendix)

**Current (Embedded in Procedure):**
- 4 filter examples scattered within step 4 (lines 107-172)
- Mix of DSL queries and graphical approach
- No summary table or quick reference

Users must scroll through the procedure to find filter syntax examples.

**Proposed (Consolidated Reference):**
- **Appendix A: Kibana Filter Query Reference**
  - Table with filter purpose, query type, and example
  - 4 filter patterns (Tekton-managed, exclude place-tools, pipelineRun, pipeline)
  - Clear distinction between DSL and graphical methods

**Benefit:** Quick lookup for filter syntax without navigating through procedure steps; reference material separated from instructional content.

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 1 procedure | 1 job | Clarity improvement (outcome vs tool) |
| Steps to find filter syntax | Read through step 4, scroll to example | Navigate to Appendix A, scan table | ~50% time reduction for lookup |
| Prerequisites visibility | Buried in procedure section | Surfaced at job level | Immediate visibility |
| Goal clarity | Implicit (inferred from procedure title) | Explicit ("When X, I want Y, so I can Z") | Clear user intent |
| Task grouping | Sequential steps (1-7) | Thematic groups (access, pattern, filter, select, validate) | Conceptual clarity |

**Final job count: 1** (reduced from suggested 2). The "Viewing pipeline logs in Kibana" procedure is the sole method for achieving the main goal, so configuration becomes a user story under the main job rather than a separate job.

---

## Workflow Coverage Comparison

| Stage | Current | Proposed | Gap Status |
|-------|---------|----------|------------|
| Get Started | ❌ Missing | ❌ Missing | Gap remains - No onboarding or operator installation guidance |
| Configure | ⚠️ Scattered | ✅ Job 1 | Improved - Kibana configuration consolidated under main job |
| Observe | ⚠️ Embedded in procedure | ✅ Job 1 | Improved - Log viewing made explicit as observation workflow |
| Troubleshoot | ❌ Missing | ❌ Missing | Gap remains - No troubleshooting for failed queries or missing logs |
| Reference | ⚠️ Embedded examples | ✅ Appendix A | Improved - Filter query reference table added |

### Coverage Summary

**Current structure gaps:** Get Started, Troubleshoot, Reference (embedded only)
**Proposed structure gaps:** Get Started, Troubleshoot
**Gaps addressed by restructure:** Reference (now dedicated appendix), Observe (made explicit)

### Recommendations for Gap Closure

| Gap | Recommendation | Priority |
|-----|----------------|----------|
| Get Started | Add prerequisite installation section or link to operator installation guides | High - Users cannot complete the procedure without prerequisites |
| Troubleshoot | Add troubleshooting section for common issues (missing logs, failed filters, permission errors) | High - Critical for user success |
| Configure | Add guidance on log retention policy configuration for pipeline logs | Medium - Important for operational management |
| Reference | Expand filter query reference with additional patterns for task runs, event listeners | Low - Current patterns cover primary use cases |

---

## Success Criteria Met

✅ User can immediately see main goal (access logs independently of pods)
✅ User can find the job by what they need to accomplish (observe pipeline logs)
✅ Structure follows natural workflow progression (configure → observe → validate)
✅ Prerequisites stated as permissions and operator installations (not job titles)
✅ Gaps clearly marked with recommendations and priorities
✅ Both the main goal and implementation approach are clearly separated

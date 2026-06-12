# JTBD Workflow Analysis: Viewing Pipeline Logs Using the OpenShift Logging Operator

**Document:** viewing-pipeline-logs-using-the-openshift-logging-operator.adoc
**Variant:** self-managed
**Analysis Date:** 2026-06-11

---

## Workflow Outputs

This directory contains the complete JTBD workflow analysis for the "Viewing pipeline logs using the OpenShift Logging Operator" document. All 5 steps have been completed:

### 1. JTBD Analysis (`jtbd-analysis.jsonl`)
- **2 JTBD records** extracted from the source document
- **1 main job:** Access Pipeline Logs Independently of Pod Lifecycle
- **1 user story:** Configure Kibana for Pipeline Log Access
- Format: JSONL (one JSON object per line)
- Schema: Compliant with `/Users/roparmar/.claude/plugins/cache/ccs-ai-agentic-workflow/jtbd-tools/1.3.0/reference/schema.md`

### 2. Include Graph (`include-graph.json`)
- Parsed structure of the original assembly
- **1 included module:** `modules/op-viewing-pipeline-logs-in-kibana.adoc`
- Module type: `procedure`
- Additional resources: 3 external OpenShift Logging documentation links
- Format: JSON

### 3. JTBD-Oriented TOC (`jtbd-toc.md`)
- Table of Contents organized by user goals and workflow stages
- **1 main job** in the Observe System State stage
- Quick Navigation section for common tasks
- Appendices:
  - A. Kibana Filter Query Reference (4 filter patterns)
  - B. Workflow Coverage Analysis (identifies gaps in Get Started, Troubleshoot, Reference stages)
- Navigation Guide with user journey examples
- Format: Markdown

### 4. Comparison Document (`jtbd-comparison.md`)
- Side-by-side comparison of current vs. proposed structure
- **Key finding:** 2 suggested jobs consolidated to 1 final job (Kibana configuration merged as user story)
- Navigation improvement metrics: ~50% reduction in clicks to find prerequisites, ~50% time reduction for filter syntax lookup
- Workflow coverage comparison with gap recommendations (3 High, 1 Medium priority)
- Format: Markdown

### 5. Consolidation Report (`jtbd-consolidation-report.md`)
- Stakeholder-facing report explaining restructuring rationale
- **2 consolidation examples:**
  1. Linear procedure → Hierarchical task structure (7 steps → 5 task groups)
  2. Embedded filter examples → Dedicated reference appendix
- **8 content gaps identified** (3 High, 3 Medium, 2 Low priority)
- Executive summary explaining organizing principle shift (tool-centric → goal-centric)
- Format: Markdown

---

## Key Findings

### Main Job Identified

**Job 1: Access Pipeline Logs Independently of Pod Lifecycle**
- **Persona:** Cluster administrator
- **Workflow Stage:** Observe System State
- **Prerequisites:** OpenShift Elasticsearch Operator, OpenShift Logging Operator, cluster admin permissions
- **Desired Outcomes:**
  - Minimize time required to locate relevant pipeline logs
  - Reduce resource consumption from retaining unnecessary pods
  - Ensure logs remain accessible for audit requirements
  - Eliminate dependency on pod availability for log access

### Structural Improvements

1. **Prerequisites surfaced early** — Moved from buried procedure section to job level
2. **Explicit goal statement** — "When X, I want Y, so I can Z" format clarifies user intent
3. **Task grouping** — 7 sequential steps reorganized into 5 thematic groups (access, pattern, filter, select, validate)
4. **Reference material extraction** — Filter query examples moved to dedicated appendix
5. **Gap identification** — Missing Get Started and Troubleshoot content flagged with priorities

### High-Priority Content Gaps

1. **No operator installation guidance** — Users cannot complete the job without prerequisites
2. **No troubleshooting for missing logs** — If logs don't appear, no root cause guidance
3. **No troubleshooting for failed filters** — Complex DSL queries prone to syntax errors

---

## Navigation Guide

### For Documentation Writers
1. Start with `jtbd-consolidation-report.md` for executive summary and consolidation examples
2. Review `jtbd-comparison.md` for detailed before/after structure comparison
3. Use `jtbd-analysis.jsonl` for raw JTBD records and evidence citations
4. Reference `include-graph.json` for current assembly structure

### For Content Strategists
1. Review `jtbd-consolidation-report.md` Executive Summary for organizing principle shift
2. Check Content Gaps Identified section for prioritized recommendations
3. Review Navigation Improvement Summary for quantified metrics

### For Stakeholders
1. Read `jtbd-consolidation-report.md` for complete picture
2. Focus on Key Differences table and Consolidation Examples
3. Review Gap recommendations for action items

---

## Methodology References

This analysis followed the JTBD methodology defined in:
- `/Users/roparmar/.claude/plugins/cache/ccs-ai-agentic-workflow/jtbd-tools/1.3.0/reference/methodology.md`
- `/Users/roparmar/.claude/plugins/cache/ccs-ai-agentic-workflow/jtbd-tools/1.3.0/reference/schema.md`
- `/Users/roparmar/.claude/plugins/cache/ccs-ai-agentic-workflow/jtbd-tools/1.3.0/reference/toc-guidelines.md`
- `/Users/roparmar/.claude/plugins/cache/ccs-ai-agentic-workflow/jtbd-tools/1.3.0/reference/comparison-guide.md`
- `/Users/roparmar/.claude/plugins/cache/ccs-ai-agentic-workflow/jtbd-tools/1.3.0/reference/consolidation-guide.md`

---

## File Sizes

```
1.5K  include-graph.json
2.6K  jtbd-analysis.jsonl
8.4K  jtbd-comparison.md
12K   jtbd-consolidation-report.md
5.4K  jtbd-toc.md
6.6K  viewing-pipeline-logs-using-the-openshift-logging-operator-self-managed-reduced.adoc
```

**Total analysis output:** ~36KB across 5 deliverable files

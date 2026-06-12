# JTBD Consolidation Report
## Viewing pipeline logs by using the OpenShift Logging Operator

**Document:** viewing-pipeline-logs-using-the-openshift-logging-operator  
**Analysis Date:** June 12, 2026  
**Variant:** self-managed  
**Analyst:** JTBD Workflow Agent

---

## Executive Summary

This document provides guidance on viewing OpenShift Pipelines logs using the Kibana web console after pipeline execution pods are deleted. The current structure presents the content as a single large procedure with an abstract. The JTBD analysis reveals **2 main jobs** that users are trying to accomplish, which can be better served by reorganizing the content into **2 concept modules** and **4 focused procedures**.

**Key Finding:** The content is solid but would benefit from clearer separation between conceptual understanding (the problem and solution) and procedural guidance (how to use Kibana). This reorganization will improve user comprehension and task completion rates.

---

## Jobs-to-be-Done Analysis

### Main Jobs Identified

Through analysis of the content and application of the "Why?" ladder test, the following main jobs were identified:

#### Job 1: View pipeline logs for troubleshooting and audits
**User Context:** "When I need to review and analyze pipeline activity"  
**Desired Outcome:** "So I can troubleshoot issues and conduct audits without depending on pod retention"

**Why this is a main job:**
- It represents the fundamental user need that drives all related tasks
- It encompasses the core problem (pod dependency) and constraint (resource efficiency)
- Users arrive at this document specifically to solve this problem

**Supporting Content:**
- Understanding the pipeline log storage problem
- Learning about the Kibana-based solution
- Recognizing the benefits of persistent logging

#### Job 2: Access and analyze pipeline logs in Kibana
**User Context:** "When I need to use Kibana to view pipeline logs"  
**Desired Outcome:** "So I can successfully set up, filter, and read pipeline execution logs"

**Why this is a main job:**
- It represents a distinct user goal separate from understanding the problem
- It requires specific technical knowledge and procedural steps
- It passes the "Why?" ladder test (the answer goes back to Job 1, not a more specific task)

**Supporting Tasks:**
- Creating an index pattern in Kibana
- Filtering pipeline-related logs
- Viewing log messages

---

## Content Inventory

### Current Structure
- **Total modules:** 2 (1 assembly, 1 procedure)
- **Content types:** Mixed (abstract with concept, one large procedure)
- **Approaches:** 1 monolithic procedure with multiple embedded tasks

### Extracted JTBD Records
- **Total records extracted:** 7
- **Main jobs:** 2 (after consolidation)
- **Supporting tasks:** 5

### Record Consolidation

**Original Records 1, 2, 3 → Main Job 1:**
- Record 1: "View pipeline logs for troubleshooting and audits"
- Record 2: "Avoid resource waste from indefinite pod retention"
- Record 3: "View pipeline logs using Elasticsearch Kibana stack"

**Consolidation Rationale:** These three records all describe the same fundamental job from different angles - understanding the problem, the constraint, and the solution. When you ask "why?" for records 2 and 3, the answer is record 1.

**Original Records 4, 5, 6, 7 → Main Job 2:**
- Record 4: "Access pipeline logs in Kibana web console"
- Record 5: "Create an index pattern in Kibana"
- Record 6: "Filter pipeline-related logs in Kibana"
- Record 7: "Display and read pipeline log messages"

**Consolidation Rationale:** These are all tasks supporting the goal of using Kibana to access logs. Record 4 is the overarching task, while 5, 6, and 7 are sequential steps. They fail the "Why?" test as standalone jobs.

---

## Proposed Reorganization

### Recommended Structure

```
Main Job 1: View pipeline logs for troubleshooting and audits
├── Understanding pipeline log storage and the pod dependency problem [concept]
└── Viewing pipeline logs using the Elasticsearch Kibana stack [concept]

Main Job 2: Access and analyze pipeline logs in Kibana
├── Viewing pipeline logs in the Kibana web console [procedure - parent]
├── Creating an index pattern in Kibana [procedure]
├── Filtering pipeline-related logs [procedure]
└── Viewing log messages [procedure]
```

### Content Type Distribution

| Content Type | Current | Proposed | Change |
|-------------|---------|----------|--------|
| Concept | 0 (embedded in abstract) | 2 | +2 |
| Procedure | 1 (monolithic) | 4 (focused) | +3 |
| Reference | 0 | 0 | 0 |
| **Total Modules** | **1** | **6** | **+5** |

---

## Benefits of Reorganization

### 1. Clearer User Journey
**Current:** Users jump directly from a brief abstract into a complex procedure  
**Proposed:** Users progress from understanding → planning → doing

**Impact:** Improved task completion rates, reduced support requests

### 2. Better Content Discoverability
**Current:** All guidance buried in one procedure  
**Proposed:** Focused procedures with descriptive, job-oriented titles

**Impact:** Users can quickly locate the specific task they need help with

### 3. Improved Reusability
**Current:** Monolithic module difficult to reuse in other contexts  
**Proposed:** Modular procedures can be referenced independently

**Impact:** Content can be reused in troubleshooting guides, admin documentation

### 4. Enhanced Comprehension
**Current:** Conceptual information mixed with procedural steps  
**Proposed:** Clear separation between "why/what" and "how"

**Impact:** Users better understand when and why to use this approach

### 5. Reduced Cognitive Load
**Current:** Large procedure with multiple embedded examples and filtering options  
**Proposed:** Focused procedures with clear, single outcomes

**Impact:** Easier to follow, less overwhelming for new users

---

## Implementation Recommendations

### Priority 1: Split Conceptual and Procedural Content
**Action:** Create two concept modules from the current abstract
- **Module 1:** Pipeline log storage challenges (problem statement)
- **Module 2:** Kibana-based logging solution (solution overview)

**Effort:** Low - content exists, needs reorganization  
**Impact:** High - establishes clear foundation before procedures

### Priority 2: Break Down the Monolithic Procedure
**Action:** Split the current procedure into 4 focused procedures
- **Procedure 1:** Viewing pipeline logs in Kibana (parent/overview)
- **Procedure 2:** Creating an index pattern
- **Procedure 3:** Filtering pipeline logs
- **Procedure 4:** Viewing log messages

**Effort:** Medium - requires careful step redistribution  
**Impact:** High - dramatically improves usability

### Priority 3: Enhance Prerequisites
**Action:** Reorganize prerequisites into categorized format
- Access requirements (cluster admin)
- Data requirements (available logs)
- Platform requirements (installed operators)

**Effort:** Low - content exists, needs restructuring  
**Impact:** Medium - clearer preparation checklist

### Priority 4: Add Context to Filtering
**Action:** Add brief explanations for each filter type
- Why filter by managed-by label
- Purpose of excluding place-tools
- Using pipelinerun and pipeline labels for highlighting

**Effort:** Low - 1-2 sentences per filter  
**Impact:** Medium - better understanding of filtering options

### Priority 5: Add Job-Level Headings
**Action:** Restructure assembly to use job statements as headings
- Makes user goals explicit
- Improves scannability
- Enables job-based navigation

**Effort:** Low - heading restructure  
**Impact:** High - aligns with JTBD methodology

---

## Migration Considerations

### Content Creation Required
**None** - All content exists; only reorganization needed

### Module Count Impact
- **Current:** 1 procedure module
- **Proposed:** 2 concept modules, 4 procedure modules
- **Net change:** +5 modules

### Dependency Impact
**Low** - This document is self-contained; reorganization won't affect other assemblies

### File Naming Recommendations
Using Red Hat modular docs conventions:

**Concepts:**
- `con_pipeline-log-storage-challenges.adoc`
- `con_kibana-based-pipeline-logging-solution.adoc`

**Procedures:**
- `proc_viewing-pipeline-logs-in-kibana.adoc` (parent)
- `proc_creating-index-pattern-kibana.adoc`
- `proc_filtering-pipeline-logs-kibana.adoc`
- `proc_viewing-pipeline-log-messages.adoc`

**Assembly:**
- `assembly_viewing-pipeline-logs-using-openshift-logging-operator.adoc` (updated)

---

## Validation Criteria

To ensure the reorganization successfully addresses user needs, validate against these criteria:

### Conceptual Understanding
- [ ] Users can explain why pipeline logs need persistent storage
- [ ] Users understand the role of Kibana in the logging solution
- [ ] Users recognize when this approach is appropriate

### Task Completion
- [ ] Users can successfully create an index pattern
- [ ] Users can apply appropriate filters to narrow log scope
- [ ] Users can locate and read relevant log messages

### Navigation Efficiency
- [ ] Users can quickly locate the task they need help with
- [ ] Job-oriented headings clearly communicate user goals
- [ ] Prerequisites are easy to find and verify

### Content Reusability
- [ ] Individual procedures can be referenced independently
- [ ] Concept modules can be used in other logging contexts
- [ ] Procedures work as standalone modules

---

## Effort and Impact Assessment

### Reorganization Effort: **Low to Medium**
- **Time estimate:** 2-4 hours
- **Complexity:** Primarily structural reorganization
- **Risk:** Low - no new content creation, minimal rewording needed

### User Impact: **High**
- **Comprehension:** Significant improvement through concept/procedure separation
- **Task success:** Improved through focused, single-purpose procedures
- **Discoverability:** Enhanced through job-oriented structure
- **Reusability:** Better module independence

### Maintenance Impact: **Neutral to Positive**
- More modules to maintain, but each is simpler and more focused
- Updates to filtering logic only affect one module
- Concept updates don't require touching procedures

---

## Next Steps

1. **Review and validate** the proposed structure with stakeholders
2. **Create concept modules** by splitting and expanding the current abstract
3. **Refactor procedure module** into 4 focused procedures
4. **Update assembly** to use job-oriented headings and new includes
5. **Validate prerequisites** section formatting and categorization
6. **Add context** to filtering steps (brief explanations)
7. **Test navigation** to ensure users can easily find relevant content
8. **Update references** in other documents if needed

---

## Appendix: JTBD Methodology Application

### "Why?" Ladder Test Results

**Record 2 → Record 1:**
- Q: "Why avoid resource waste from pod retention?"
- A: "To view pipeline logs sustainably" (Record 1)

**Record 3 → Record 1:**
- Q: "Why use Elasticsearch Kibana stack?"
- A: "To view pipeline logs without pod dependency" (Record 1)

**Record 5 → Record 4:**
- Q: "Why create an index pattern?"
- A: "To access pipeline logs in Kibana" (Record 4)

**Record 6 → Record 4:**
- Q: "Why filter pipeline logs?"
- A: "To access relevant pipeline logs in Kibana" (Record 4)

**Record 7 → Record 4:**
- Q: "Why display log messages?"
- A: "To access and read pipeline logs in Kibana" (Record 4)

**Record 4 → Record 1:**
- Q: "Why access pipeline logs in Kibana?"
- A: "To view logs for troubleshooting and audits" (Record 1)

### Signal Types Found
- **Problem statements:** Pod dependency, resource waste
- **Solution statements:** Kibana stack, logging operators
- **Procedural goals:** View logs in web console
- **Procedural steps:** Index pattern, filtering, field selection

### Content Type Mapping
- Lines 64-69: **Concept** - problem and solution overview
- Lines 79-182: **Procedure** - complete Kibana setup and usage workflow
- Lines 85-93: **Prerequisites** - required conditions
- Lines 95-182: **Procedural steps** - setup, filtering, viewing

---

## Document Metadata

**Source files analyzed:**
- `/Users/roparmar/git/openshift-docs/records/viewing-pipeline-logs-using-the-openshift-logging-operator.adoc`
- `/Users/roparmar/git/openshift-docs/modules/op-viewing-pipeline-logs-in-kibana.adoc`

**Analysis outputs:**
- JTBD records: `jtbd-records.json`
- Source map: `source-map.json`
- TOC proposal: `jtbd-toc.md`
- Structure comparison: `comparison.md`
- This report: `consolidation-report.md`

**Reduced document:**
- `reduced.adoc` (195 lines)

---

*This report was generated using the JTBD workflow for AsciiDoc documents, applying the "Why?" ladder test to consolidate user jobs and the Red Hat modular documentation framework for content type classification.*

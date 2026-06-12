# JTBD Analysis Output Summary

## Document 19: Understanding the Tekton Results retention policy

**Analysis Date:** 2026-06-12  
**Variant:** self-managed  
**Workflow:** Complete 4-step JTBD analysis

---

## Analysis Overview

This directory contains the complete Jobs-to-be-Done (JTBD) analysis for the "Understanding the Tekton Results retention policy" documentation.

### Document Information
- **Source file:** `/Users/roparmar/git/openshift-docs/records/understanding-the-tekton-results-retention-policy.adoc`
- **Document type:** Assembly
- **Current modules:** 2 (1 assembly + 1 concept module)
- **Product:** Red Hat OpenShift Pipelines
- **Component:** Tekton Results

---

## Key Findings

### Jobs Identified: 5

1. **Understand how Tekton Results retention works** (Learn)
2. **Configure basic retention settings** (Do)
3. **Understand fine-grained retention policies** (Learn)
4. **Create namespace-based retention policies** (Do)
5. **Create status and label-based retention policies** (Do)

### Main Jobs (After Consolidation): 5

All identified jobs validated as main jobs using the "Why?" ladder test. No consolidation needed - each job represents a distinct user goal.

### Critical Gaps Identified

1. **No procedural guidance** (Severity: High)
   - Zero procedure modules in current structure
   - Users have reference material but no step-by-step instructions
   - Affects Jobs 2, 4, and 5

2. **Weak basic retention coverage** (Severity: Medium)
   - Retention fundamentals only in 2-paragraph abstract
   - Affects Job 1

3. **Poor task discoverability** (Severity: Medium)
   - Users must read entire doc to find specific use cases
   - Reference tables embedded in narrative

---

## Output Files

### 1. source-map.json
**Purpose:** Document structure and include graph  
**Contents:**
- Assembly metadata
- Include directive mapping
- Module relationships
- Line range tracking

### 2. jtbd-records.json
**Purpose:** Extracted JTBD jobs with line references  
**Contents:**
- 5 JTBD job records
- Current approaches for each job
- Gap analysis per job
- Why? ladder validation
- Source module attribution

### 3. reduced.adoc
**Purpose:** Flattened document for analysis  
**Contents:**
- Complete document with all includes resolved
- Self-managed variant attributes applied
- Used for line reference extraction

### 4. jtbd-toc.md
**Purpose:** Proposed JTBD-oriented table of contents  
**Contents:**
- Job-based structure (5 jobs + 2 references)
- Content type distribution (2 concepts, 3 procedures, 2 references)
- TOC design rationale
- Cross-reference recommendations

### 5. comparison.md
**Purpose:** Side-by-side structure comparison  
**Contents:**
- Current vs. proposed structure diagrams
- Module count comparison
- Content mapping analysis
- Impact assessment
- Implementation recommendation

### 6. consolidation-report.md
**Purpose:** Stakeholder-facing consolidation report  
**Contents:**
- Executive summary
- Detailed job analysis
- Current state assessment (strengths/weaknesses)
- Proposed structure with module breakdown
- Content mapping (current → proposed)
- Gap analysis with priorities
- Benefits analysis
- Implementation recommendations with timeline
- Success metrics

---

## Proposed Structure Summary

### Module Breakdown

| Module Type | Current | Proposed | Change |
|-------------|---------|----------|--------|
| Assembly | 1 | 1 | No change |
| Concept | 1 | 2 | +1 |
| Procedure | 0 | 3 | +3 ⭐ |
| Reference | 0 (embedded) | 2 | +2 |
| **Total** | **2** | **8** | **+6** |

⭐ = Critical gap fill

### New Modules Required

1. **Job 1 Concept:** Understanding retention (expand from abstract)
2. **Job 2 Procedure:** Configure basic retention ⭐ NEW
3. **Reference:** Retention config fields (extract from assembly)
4. **Reference:** Policy selector fields (extract from concept)
5. **Job 4 Procedure:** Create namespace policies ⭐ NEW
6. **Job 5 Procedure:** Create status/label policies ⭐ NEW

**Estimated new content:** ~150-190 lines

---

## Implementation Priority

### Priority 1: Procedures (High Impact)
- Job 2: Configure basic retention settings
- Job 4: Create namespace-based retention policies
- Job 5: Create status and label-based retention policies

### Priority 2: Structure (Medium Impact)
- Extract reference modules
- Expand Job 1 concept
- Refocus Job 3 concept

### Priority 3: Enhancement (Low Priority)
- Add troubleshooting sections
- Add verification examples
- Create quick-start guide

**Estimated effort:** 4-5 weeks with 1 technical writer

---

## Key Recommendations

1. **Implement all 3 new procedure modules** - fills critical "how-to" gaps
2. **Extract reference modules** - improves maintainability
3. **Expand conceptual foundation** - better user preparation
4. **Maintain example quality** - preserve strong YAML examples
5. **Add verification steps** - help users confirm success

---

## Usage

This analysis supports:
- **Documentation planning:** Use consolidation-report.md for roadmap planning
- **Content creation:** Use jtbd-records.json and jtbd-toc.md for module writing
- **Gap prioritization:** Use comparison.md for priority setting
- **Stakeholder review:** Use consolidation-report.md executive summary

---

## Files in This Directory

```
understanding-the-tekton-results-retention-policy/
├── README.md (this file)
├── source-map.json
├── jtbd-records.json
├── reduced.adoc
├── jtbd-toc.md
├── comparison.md
└── consolidation-report.md
```

---

**Generated by:** JTBD Workflow for AsciiDoc Documents  
**Workflow version:** 4-step complete analysis  
**Date:** 2026-06-12

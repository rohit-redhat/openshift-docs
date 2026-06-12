# JTBD Consolidation Report

## Document: Understanding the Tekton Results retention policy

**Product:** Red Hat OpenShift Pipelines  
**Component:** Tekton Results  
**Analysis Date:** 2026-06-12  
**Variant:** self-managed

---

## Executive Summary

This report presents a Jobs-to-be-Done (JTBD) analysis of the "Understanding the Tekton Results retention policy" documentation. The analysis identifies **5 distinct user jobs** and proposes a restructured approach that addresses critical gaps in procedural guidance while maintaining strong conceptual and reference content.

**Key Findings:**
- **Current state:** 2 modules (1 assembly + 1 concept) with strong reference material but no procedures
- **Proposed state:** 8 modules addressing 5 user jobs with 3 new procedure modules
- **Primary gap:** Lack of step-by-step instructions for configuring retention policies
- **Recommendation:** Implement proposed structure to fill procedural gaps and improve task discoverability

---

## Jobs-to-be-Done Analysis

### Identified Jobs

| # | Job Statement | Job Type | Current Coverage | Gap Severity |
|---|---------------|----------|------------------|--------------|
| 1 | Understand how Tekton Results retention works | Learn | Partial (assembly abstract) | Medium |
| 2 | Configure basic retention settings | Do | Poor (example only) | High |
| 3 | Understand fine-grained retention policies | Learn | Good (dedicated concept) | Low |
| 4 | Create namespace-based retention policies | Do | Poor (example only) | High |
| 5 | Create status and label-based retention policies | Do | Poor (example only) | High |

### Job Validation (Why? Ladder Test)

Each job was tested using the "Why?" ladder to ensure it represents a genuine user goal:

- **Job 1:** "Why understand retention?" → To make informed configuration decisions → VALID (foundation)
- **Job 2:** "Why configure basic settings?" → To manage Results retention → VALID (core task)
- **Job 3:** "Why understand fine-grained policies?" → To create targeted rules → VALID (foundation for Jobs 4-5)
- **Job 4:** "Why create namespace policies?" → To configure fine-grained retention → VALID (specific implementation)
- **Job 5:** "Why create status/label policies?" → To configure fine-grained retention → VALID (specific implementation)

All 5 jobs are validated as main jobs, not sub-tasks.

---

## Current State Assessment

### Strengths

1. **Strong conceptual foundation**
   - Fine-grained retention policies concept is well-written
   - Policy evaluation order is clearly explained
   - AND logic for selectors is well-documented

2. **Comprehensive reference material**
   - Complete field reference tables for configuration and policy selectors
   - Rich YAML examples showing complex policy configurations

3. **Good examples**
   - Multiple policy scenarios (production, CI, debug, failed runs)
   - Concrete application examples with expected behavior

### Weaknesses

1. **No procedural guidance** (Critical Gap)
   - Users have reference material but no step-by-step instructions
   - Configuration examples lack context on how to apply them
   - No prerequisites, verification steps, or troubleshooting guidance

2. **Weak basic retention coverage**
   - Retention fundamentals only covered in 2-paragraph abstract
   - Config map location and structure not prominently explained
   - Duration format options mentioned but not explained

3. **Poor task discoverability**
   - Users seeking namespace-specific retention must read entire doc
   - No clear entry point for common tasks like "retain failed runs longer"
   - Reference tables embedded in narrative flow

4. **Limited separation of concerns**
   - Reference content mixed with concepts
   - Single concept module covers multiple policy selector types

---

## Proposed Structure

### Overview

The proposed structure reorganizes content into **8 modular components** addressing **5 user jobs**:

```
Managing Tekton Results retention [ASSEMBLY]
├── Job 1: Understand how retention works [CONCEPT]
├── Job 2: Configure basic retention [PROCEDURE] ⭐ NEW
├── Job 3: Understand fine-grained policies [CONCEPT]
├── Retention policy configuration fields [REFERENCE]
├── Fine-grained policy selector fields [REFERENCE]
├── Job 4: Create namespace-based policies [PROCEDURE] ⭐ NEW
└── Job 5: Create status/label-based policies [PROCEDURE] ⭐ NEW
```

⭐ = New content to be created

### Module Breakdown

#### Job 1: Understand how Tekton Results retention works [CONCEPT]
**Source:** Assembly abstract + new content  
**Lines:** 63-67 (current assembly)

**Proposed Content:**
- Overview of Retention Policy Agent and its role
- How retention policies determine deletion timing
- Config map location and purpose (tekton-results-config-results-retention-policy)
- Global defaults vs. fine-grained rules
- Retention period formats (days, duration strings like 30d, 24h)
- When Results and Records are pruned

**Rationale:** Current abstract provides minimal context. Expanded concept module gives users solid foundation before configuration tasks.

---

#### Job 2: Configure basic retention settings [PROCEDURE] ⭐ NEW
**Source:** New content + reference to lines 68-135  
**Gap Addressed:** No step-by-step guidance for basic configuration

**Proposed Content:**
- Prerequisites (cluster admin access, namespace access)
- Steps:
  1. Access the tekton-results-config-results-retention-policy config map
  2. Set the defaultRetention value (with format examples)
  3. Configure the runAt cron schedule
  4. Apply the configuration
  5. Verify the retention policy is active
- Verification section (checking retention policy logs/status)
- Additional resources (cron format reference, troubleshooting)

**Rationale:** Fills critical procedural gap. Users currently must reverse-engineer from YAML example.

---

#### Job 3: Understand fine-grained retention policies [CONCEPT]
**Source:** modules/op-fine-grained-retention-policies.adoc (lines 147-176)  
**Lines:** Current concept module abstract + field descriptions

**Proposed Content:**
- What fine-grained policies are and when to use them
- How policy evaluation works (order of precedence, first match wins)
- Policy structure overview (name, selector, retention)
- Selector types: namespace, label, annotation, status
- AND logic explanation (all conditions must match)
- Relationship between policies and defaultRetention
- When fine-grained policies override default retention

**Rationale:** Maintains strong conceptual foundation from current module, with clearer focus on understanding vs. doing.

---

#### Reference: Retention policy configuration fields [REFERENCE]
**Source:** Assembly reference table (lines 114-135)

**Proposed Content:**
- runAt field (cron schedule, default value, examples)
- defaultRetention field (fallback period, format options, default value)
- maxRetention field (deprecated notice, backward compatibility)
- policies field (list structure, precedence)

**Rationale:** Separates reference material from narrative for easier updates and cross-referencing.

---

#### Reference: Fine-grained policy selector fields [REFERENCE]
**Source:** Fine-grained concept table (lines 150-176)

**Proposed Content:**
- name field (descriptive policy identifier)
- selector field (matching criteria container)
- matchNamespaces (namespace list, any-of logic)
- matchLabels (key-value map, all-of logic for keys)
- matchAnnotations (key-value map, similar to matchLabels)
- matchStatuses (final status list: Succeeded, Failed, etc.)
- retention field (policy-specific retention period)

**Rationale:** Dedicated reference for policy configuration, supporting Jobs 4-5 procedures.

---

#### Job 4: Create namespace-based retention policies [PROCEDURE] ⭐ NEW
**Source:** New content + examples from lines 178-217  
**Gap Addressed:** No guidance for implementing namespace-specific retention

**Proposed Content:**
- Prerequisites (understanding of fine-grained policies, namespace access)
- Steps:
  1. Identify target namespaces (production, CI, dev, etc.)
  2. Determine desired retention period for each namespace group
  3. Create policy entries in the policies field
  4. Define matchNamespaces selector
  5. Set retention value
  6. Order policies by specificity (most specific first)
  7. Apply configuration
- Example: Different retention for production vs. CI namespaces
  - Production: 60d retention
  - CI: 7d retention
- Verification: Checking which policy matches specific Results
- Additional resources: Kubernetes namespace best practices

**Rationale:** Common use case (environment-specific retention) needs dedicated procedure.

---

#### Job 5: Create status and label-based retention policies [PROCEDURE] ⭐ NEW
**Source:** New content + examples from lines 191-225  
**Gap Addressed:** No guidance for implementing advanced policy selectors

**Proposed Content:**
- Prerequisites (understanding of fine-grained policies, label/annotation strategy)
- Steps for label-based policies:
  1. Identify label keys and values to match
  2. Create policy with matchLabels selector
  3. Set retention period
- Steps for status-based policies:
  1. Identify target statuses (Failed, Succeeded, etc.)
  2. Create policy with matchStatuses selector
  3. Set retention period
- Combining multiple selectors:
  1. Determine all matching criteria (namespace + status + labels)
  2. Add all selector types to single policy
  3. Understand AND logic (all must match)
- Common use cases with examples:
  - **Retain failed runs longer:** matchStatuses: Failed, retention: 90d
  - **Debug annotation retention:** matchAnnotations: debug/retain: true, retention: 14d
  - **Critical workload retention:** Combine matchNamespaces (production) + matchLabels (criticality: high) + matchStatuses (Failed), retention: 180d
- Understanding policy precedence and ordering
- Verification: Testing policy matching for different Result scenarios
- Additional resources: Tekton Results label best practices

**Rationale:** Advanced selectors enable powerful retention strategies but require clear procedural guidance. Multiple use cases address diverse user needs.

---

## Content Mapping

### From Current to Proposed

| Current Content | Current Location | Proposed Location | Action |
|----------------|------------------|-------------------|--------|
| Assembly abstract | Lines 63-67 | Job 1 concept | Expand + split |
| Sample YAML config | Lines 68-112 | Job 2 procedure | Reference in steps |
| Config fields table | Lines 114-135 | Retention config fields reference | Extract to dedicated module |
| Fine-grained concept | Module lines 147-176 | Job 3 concept | Refocus on understanding |
| Policy fields table | Module lines 150-176 | Policy selector fields reference | Extract to dedicated module |
| Policy examples (YAML) | Module lines 178-217 | Jobs 4-5 procedures | Distribute as examples |
| Application examples | Module lines 219-225 | Jobs 4-5 procedures | Use in verification sections |

### New Content Required

1. **Job 2 procedure:** ~30-40 lines (prerequisites, 5-7 steps, verification)
2. **Job 4 procedure:** ~40-50 lines (prerequisites, 7-8 steps, namespace example, verification)
3. **Job 5 procedure:** ~60-70 lines (prerequisites, multiple step groups, 3 use case examples, verification)
4. **Expanded Job 1 concept:** ~20-30 additional lines beyond current abstract

**Total new content:** ~150-190 lines across 4 modules

---

## Gap Analysis

### High-Priority Gaps (Addressed by Proposal)

1. **No basic configuration procedure** → Job 2 procedure
   - **Impact:** Users struggle to apply configuration despite having reference material
   - **Evidence:** Assembly provides YAML example but no steps to apply it

2. **No namespace policy procedure** → Job 4 procedure
   - **Impact:** Common use case (env-specific retention) requires guesswork
   - **Evidence:** Example exists (lines 178-217) but no guidance on implementation

3. **No advanced policy procedure** → Job 5 procedure
   - **Impact:** Users can't leverage powerful selector combinations
   - **Evidence:** Complex examples exist but no procedural guidance

### Medium-Priority Gaps (Addressed by Proposal)

4. **Weak retention fundamentals** → Expanded Job 1 concept
   - **Impact:** Users lack foundation before configuration tasks
   - **Evidence:** Only 2 paragraphs in abstract explain retention basics

5. **Poor reference separation** → Dedicated reference modules
   - **Impact:** Reference material harder to maintain and cross-reference
   - **Evidence:** Tables embedded in assembly and concept narrative

### Low-Priority Gaps (Not Addressed)

- Troubleshooting guidance (could be future addition to procedures)
- Integration with monitoring/alerting (out of scope for retention doc)
- Performance implications of aggressive retention (could be added to Job 1 concept)

---

## Benefits of Proposed Structure

### For Users

1. **Task discoverability:** Direct navigation to specific jobs (Job 4 for namespace policies)
2. **Clear procedures:** Step-by-step guidance for all configuration tasks
3. **Better learning path:** Concepts before procedures, basic before advanced
4. **Quick reference:** Dedicated reference modules for field lookups

### For Documentation Team

1. **Modularity:** Independent module updates without full assembly revision
2. **Reusability:** Reference modules can be linked from other retention docs
3. **Clear ownership:** Each module has single purpose and topic type
4. **Easier maintenance:** Procedural updates don't require concept/reference changes

### For Product

1. **Feature adoption:** Clear procedures reduce barrier to using fine-grained policies
2. **Support reduction:** Better guidance = fewer support tickets on configuration
3. **User satisfaction:** Task-oriented docs improve user experience

---

## Implementation Recommendations

### Priority 1: Create Procedure Modules (High Impact)

1. **Job 2: Configure basic retention settings**
   - Addresses most common user need
   - Fills biggest procedural gap
   - Foundation for Jobs 4-5

2. **Job 4: Create namespace-based retention policies**
   - Common environment-specific use case
   - Relatively straightforward procedure
   - High user value

3. **Job 5: Create status and label-based retention policies**
   - Enables advanced retention strategies
   - Addresses multiple use cases
   - Demonstrates selector combination

### Priority 2: Refactor Existing Content (Medium Impact)

4. **Extract reference modules**
   - Retention policy configuration fields
   - Fine-grained policy selector fields
   - Improves maintainability

5. **Expand Job 1 concept**
   - Strengthen foundational understanding
   - Prepare users for configuration tasks

6. **Refocus Job 3 concept**
   - Clarify fine-grained policy concepts
   - Support Jobs 4-5 procedures

### Priority 3: Enhancement (Low Priority)

7. **Add troubleshooting sections** to procedures
8. **Add verification steps** with log examples
9. **Create quick-start guide** for common scenarios

---

## Migration Path

### Phase 1: New Procedures (Weeks 1-2)
- Write Job 2 procedure module
- Write Job 4 procedure module
- Write Job 5 procedure module
- Review with SMEs

### Phase 2: Reference Extraction (Week 3)
- Extract retention config fields reference
- Extract policy selector fields reference
- Update cross-references in existing modules

### Phase 3: Concept Enhancement (Week 4)
- Expand Job 1 concept content
- Refocus Job 3 concept (fine-grained policies)
- Update assembly to new structure

### Phase 4: Review & Publish (Week 5)
- Peer review of all new/updated modules
- User testing with draft docs
- Final edits and publication

**Estimated effort:** 4-5 weeks with 1 technical writer

---

## Success Metrics

### Quantitative
- **Module count:** Increase from 2 to 8 modules (better granularity)
- **Procedure coverage:** Increase from 0 to 3 procedures (100% gap fill)
- **Content completeness:** Add ~150-190 lines of new procedural content

### Qualitative
- **User feedback:** Survey users on task completion confidence
- **Support ticket trends:** Monitor reduction in retention configuration questions
- **SME validation:** Confirm technical accuracy of new procedures

---

## Conclusion

The proposed JTBD-oriented structure transforms the "Understanding the Tekton Results retention policy" documentation from a reference-heavy overview into a comprehensive task-oriented guide. By adding **3 critical procedure modules** and **improving conceptual foundation**, the restructure addresses all high-priority gaps while maintaining the quality of existing reference material.

**Recommendation: Proceed with implementation** following the phased migration path, prioritizing the high-impact procedure modules.

---

## Appendix: Job-to-Module Mapping

| Job # | Job Statement | Module Type | Module File Name (Proposed) | Current Source |
|-------|---------------|-------------|-----------------------------|----------------|
| 1 | Understand how Tekton Results retention works | Concept | `con-tekton-results-retention-overview.adoc` | Assembly lines 63-67 |
| 2 | Configure basic retention settings | Procedure | `proc-configuring-basic-retention-settings.adoc` | ⭐ NEW |
| 3 | Understand fine-grained retention policies | Concept | `con-fine-grained-retention-policies.adoc` | `modules/op-fine-grained-retention-policies.adoc` |
| - | Retention config fields | Reference | `ref-retention-policy-config-fields.adoc` | Assembly lines 114-135 |
| - | Policy selector fields | Reference | `ref-policy-selector-fields.adoc` | Module lines 150-176 |
| 4 | Create namespace-based retention policies | Procedure | `proc-creating-namespace-based-retention-policies.adoc` | ⭐ NEW |
| 5 | Create status and label-based retention policies | Procedure | `proc-creating-status-label-retention-policies.adoc` | ⭐ NEW |

**Assembly file:** `understanding-the-tekton-results-retention-policy.adoc` (updated structure)

---

**Document prepared by:** JTBD Analysis Workflow  
**Contact:** Documentation team lead  
**Next review date:** Post-implementation review (Week 6)

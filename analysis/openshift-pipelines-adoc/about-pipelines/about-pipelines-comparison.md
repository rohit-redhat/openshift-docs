# Documentation Structure Comparison
## About Red Hat OpenShift Pipelines

**Document:** about-pipelines  
**Variant:** self-managed  
**Analysis Date:** 2026-06-11  
**Total Sections:** 1  
**JTBD Records Extracted:** 1

---

## Current Structure (Feature-Based)

### Document Title (Level 1)
= About {pipelines-title}

**Content:**
- Product description (cloud-native CI/CD solution)
- Tekton overview
- Documentation links (versioned docs, Customer Portal)
- Lifecycle policy references

**Type:** Landing page / Orientation

---

## Proposed JTBD-Based Structure

### Get Started (1 Job)

**Job 1: Locate correct documentation version for OpenShift installation**
- **When:** I need to understand what OpenShift Pipelines is and where to find its documentation
- **So I can:** Access relevant implementation guidance for CI/CD pipelines
- **Personas:** Platform administrator
- **Source:** Lines 1-80 (entire document)

---

## Key Differences

| Aspect | Current (Feature-Based) | Proposed (JTBD-Based) |
|--------|------------------------|----------------------|
| **Organization** | Single overview page with embedded links | Single navigational job (minimal change) |
| **Primary Focus** | Product description + documentation pointers | User goal: finding correct versioned docs |
| **Structure** | Flat (no hierarchy beyond title) | Flat (single main job, no user stories) |
| **Content Gaps** | N/A - intentionally minimal | N/A - document serves its purpose |

---

## Hierarchy Levels

### Current Structure
```
Level 1 (=):  Document title only
Level 2 (==): None
Level 3 (===): None
```

**Total depth:** 1 level

### Proposed Structure
```
Main Jobs: 1
User Stories: 0
```

**Total depth:** 1 level (main job only)

---

## Example Consolidation

### N/A - Single Section Document

This document has only one section (the title and abstract) and cannot be consolidated further. It serves as a landing/orientation page with links to external documentation.

---

## Navigation Improvement Metrics

| Metric | Current | Proposed | Change |
|--------|---------|----------|--------|
| **Sections to scan** | 1 | 1 | 0% |
| **Clicks to relevant content** | 1 (external link) | 1 (external link) | 0% |
| **Workflow stages covered** | 1 (Get Started) | 1 (Get Started) | 0% |

**Note:** This document is already optimized for its purpose (orientation and navigation). No structural changes are needed.

---

## Workflow Coverage Comparison

### Current Coverage
| Stage | Present? | Sections |
|-------|----------|----------|
| Get Started | ✅ | 1 (Entire document) |
| All other stages | ❌ | N/A |

### Proposed Coverage
| Stage | Jobs | Completeness |
|-------|------|--------------|
| Get Started | 1 | ✅ Adequate for landing page |
| All other stages | 0 | ⚠️ By design - external docs |

**Gap Recommendations:**
- No gaps - this is a landing page by design
- All implementation content is in linked documentation sets
- This structure is appropriate for the document's purpose

---

## Alignment Notes

This document is a minimal landing page that intentionally provides only:
1. Product overview
2. Links to versioned documentation
3. Lifecycle policy references

The JTBD structure aligns perfectly with the current structure because the document already serves a single, focused navigational job. No restructuring is needed or recommended.

---

## Summary

**Recommendation:** Keep current structure  
**Rationale:** Document already serves its intended purpose efficiently (orientation and navigation to versioned docs)  
**Impact:** No changes needed

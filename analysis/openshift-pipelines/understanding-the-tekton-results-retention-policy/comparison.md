# Structure Comparison: Current vs. Proposed

## Document: Understanding the Tekton Results retention policy

**Analysis Date:** 2026-06-12  
**Variant:** self-managed

---

## Side-by-Side Comparison

### Current Structure

```
Understanding the Tekton Results retention policy [ASSEMBLY]
├── Abstract (overview of retention policy)
├── Sample YAML configuration example
├── Configuration fields reference table
│   ├── runAt
│   ├── defaultRetention
│   ├── maxRetention (deprecated)
│   └── policies
└── Fine-grained retention policies [CONCEPT]
    ├── Abstract (policies field explanation)
    ├── Policy fields reference table
    │   ├── name
    │   ├── selector
    │   ├── matchNamespaces
    │   ├── matchLabels
    │   ├── matchAnnotations
    │   ├── matchStatuses
    │   └── retention
    ├── Complete policy examples (config map)
    └── Policy application examples (bullet list)
```

**Content Type Count:**
- Assemblies: 1
- Concepts: 1 (embedded in assembly)
- Procedures: 0
- References: 2 (tables embedded in concept/assembly)

**Total Modules:** 2 files (1 assembly + 1 concept module)

---

### Proposed Structure

```
Managing Tekton Results retention [ASSEMBLY]
├── Job 1: Understand how Tekton Results retention works [CONCEPT]
│   ├── Overview of Retention Policy Agent
│   ├── How retention policies work
│   ├── Configuration overview
│   ├── Config map structure and location
│   └── Retention period formats
│
├── Job 2: Configure basic retention settings [PROCEDURE]
│   ├── Prerequisites
│   ├── Steps to configure config map
│   ├── Setting defaultRetention
│   ├── Configuring runAt schedule
│   ├── Verifying configuration
│   └── Additional resources
│
├── Job 3: Understand fine-grained retention policies [CONCEPT]
│   ├── What are fine-grained policies
│   ├── Policy evaluation order
│   ├── Policy structure overview
│   ├── Selector types and AND logic
│   └── When to use fine-grained vs. default
│
├── Reference: Retention policy configuration fields [REFERENCE]
│   ├── runAt field
│   ├── defaultRetention field
│   ├── maxRetention field (deprecated)
│   └── policies field
│
├── Reference: Fine-grained policy selector fields [REFERENCE]
│   ├── name
│   ├── selector
│   ├── matchNamespaces
│   ├── matchLabels
│   ├── matchAnnotations
│   ├── matchStatuses
│   └── retention
│
├── Job 4: Create namespace-based retention policies [PROCEDURE]
│   ├── Prerequisites
│   ├── Steps to create namespace policy
│   ├── Defining matchNamespaces selectors
│   ├── Setting namespace retention periods
│   ├── Handling multiple namespaces
│   ├── Verifying policy application
│   └── Example: Production vs. CI retention
│
└── Job 5: Create status and label-based retention policies [PROCEDURE]
    ├── Prerequisites
    ├── Steps for label-based policies
    ├── Steps for status-based policies
    ├── Combining multiple selectors
    ├── Common use cases
    │   ├── Retaining failed runs longer
    │   ├── Debug annotation retention
    │   └── Critical workload retention
    ├── Understanding selector AND logic
    ├── Policy precedence and ordering
    └── Verifying advanced policy application
```

**Content Type Count:**
- Assemblies: 1
- Concepts: 2
- Procedures: 3
- References: 2

**Total Modules:** 8 files (1 assembly + 2 concepts + 3 procedures + 2 references)

---

## Key Differences

### Structural Changes

| Aspect | Current | Proposed | Impact |
|--------|---------|----------|--------|
| **Organization** | Topic-based (retention overview → fine-grained policies) | Job-based (5 distinct user jobs) | Improved task discoverability |
| **Module count** | 2 modules | 8 modules | Better granularity and reusability |
| **Procedures** | 0 | 3 | Fills critical "how-to" gaps |
| **References** | Embedded tables | 2 dedicated reference modules | Cleaner separation, easier maintenance |
| **Concepts** | 1 (fine-grained only) | 2 (basic + fine-grained) | Better conceptual foundation |

### Content Mapping

#### What Stays the Same
- **Concept: Fine-grained retention policies** → Retained as Job 3 concept module
- **Reference tables** → Extracted into dedicated reference modules
- **Policy examples** → Distributed across procedure modules as practical examples

#### What Gets Split
- **Assembly intro content** → Split into:
  - Job 1: Concept module (understanding retention)
  - Job 2: Procedure module (configuring basic settings)
  
- **Fine-grained policies module** → Split into:
  - Job 3: Concept module (understanding fine-grained policies)
  - Job 4: Procedure module (namespace policies)
  - Job 5: Procedure module (status/label policies)
  - Reference module (policy selector fields)

#### What Gets Created (New Content)
- **Job 2 procedure:** Step-by-step instructions for configuring basic retention
- **Job 4 procedure:** Step-by-step instructions for namespace-based policies
- **Job 5 procedure:** Step-by-step instructions for label/status-based policies
- **Prerequisites sections** in all procedures
- **Verification steps** in all procedures
- **Common use case examples** in Job 5

### User Journey Improvements

| User Need | Current Approach | Proposed Approach | Benefit |
|-----------|------------------|-------------------|---------|
| Learn retention basics | Read abstract + config table | Job 1 concept module | Dedicated learning resource |
| Set up retention | Infer from YAML example | Job 2 procedure with steps | Clear actionable guidance |
| Understand policy options | Read nested concept + table | Job 3 concept + 2 references | Better separation of concerns |
| Create namespace policy | Reverse-engineer from example | Job 4 procedure | Task-focused guidance |
| Retain failed runs longer | Find example in bullet list | Job 5 procedure with use cases | Direct path to solution |

---

## Impact Assessment

### Strengths of Current Structure
1. **Concise:** All content in 2 files, easy to read linearly
2. **Good examples:** YAML examples are comprehensive
3. **Clear concept:** Fine-grained policies concept is well-written

### Weaknesses Addressed by Proposed Structure
1. **No procedures:** Current doc is reference-heavy with no actionable steps
2. **Embedded references:** Tables mixed with narrative make updates harder
3. **Weak basic coverage:** Retention fundamentals are only in the abstract
4. **Task discovery:** Users must read entire doc to find their specific use case

### Trade-offs
- **More modules:** Increases file count from 2 to 8
  - *Mitigation:* Better reusability, clearer ownership
- **More cross-references:** Procedures will reference concept and reference modules
  - *Mitigation:* Standard modular docs practice, improves maintainability
- **Initial migration effort:** Requires splitting existing content and writing new procedures
  - *Mitigation:* One-time cost for long-term user experience gain

---

## Recommendation

**Proceed with proposed structure** for the following reasons:

1. **Fills critical gaps:** Adds 3 procedure modules for common configuration tasks
2. **Improves discoverability:** Users can navigate directly to their job (Job 4 for namespace policies)
3. **Better modularity:** Reference tables can be updated independently of concepts/procedures
4. **Aligns with JTBD:** Each module addresses a specific user goal
5. **Maintains quality:** Preserves all existing content while adding procedural guidance

**Migration Priority:**
1. **High:** Jobs 2, 4, 5 (procedures) - fill the biggest gaps
2. **Medium:** Jobs 1, 3 (concepts) - improve existing conceptual coverage
3. **Low:** References - extract existing tables into separate modules

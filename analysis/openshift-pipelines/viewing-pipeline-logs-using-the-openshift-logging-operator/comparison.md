# Structure Comparison: Current vs. JTBD-Oriented
## Document: viewing-pipeline-logs-using-the-openshift-logging-operator

---

## Current Structure

```
Viewing pipeline logs by using the OpenShift Logging Operator
├── Abstract (problem statement and solution overview)
├── Viewing pipeline logs in Kibana [PROCEDURE]
│   ├── Prerequisites
│   ├── Procedure
│   │   ├── Log in to OpenShift web console
│   │   ├── Open Kibana
│   │   ├── Create an index pattern (4 sub-steps)
│   │   └── Add a filter (multiple sub-steps with examples)
│   │       ├── Filter pipelines containers
│   │       ├── Filter out place-tools container
│   │       ├── Filter pipelinerun labels
│   │       ├── Filter pipeline labels
│   │       └── Select fields to display
└── Additional resources (3 links)
```

**Current Document Metrics:**
- Total sections: 1 assembly + 1 procedure module
- Heading levels: 2 (assembly title, procedure title)
- Content types: 1 concept (abstract), 1 procedure
- Total approaches: Mixed in single procedure

---

## Proposed JTBD-Oriented Structure

```
Viewing pipeline logs for troubleshooting and audits

├── Main Job 1: View pipeline logs for troubleshooting and audits
│   ├── Understanding pipeline log storage and the pod dependency problem [concept]
│   │   ├── How pipeline components store logs in pods
│   │   ├── The resource cost of indefinite pod retention
│   │   └── Removing pod dependency with logging operators
│   └── Viewing pipeline logs using the Elasticsearch Kibana stack [concept]
│       ├── Overview of the OpenShift Logging solution
│       └── Benefits of persistent log storage
│
└── Main Job 2: Access and analyze pipeline logs in Kibana
    └── Viewing pipeline logs in the Kibana web console [procedure]
        ├── Prerequisites
        │   ├── Cluster administrator access
        │   ├── Available pipeline run and task run logs
        │   └── Installed OpenShift Elasticsearch and Logging Operators
        ├── Creating an index pattern in Kibana [procedure]
        │   ├── Access Kibana through OpenShift web console
        │   ├── Define the index pattern
        │   └── Configure time filter settings
        ├── Filtering pipeline-related logs [procedure]
        │   ├── Filter containers managed by Tekton
        │   ├── Exclude non-pipeline containers
        │   ├── Filter by pipelinerun labels
        │   └── Filter by pipeline labels
        └── Viewing log messages [procedure]
            ├── Select relevant fields
            └── Read the message field content

Additional resources (3 links)
```

**Proposed Document Metrics:**
- Main jobs: 2
- Total approaches: 6 (2 concepts, 4 procedures)
- Heading levels: 4 (job groups, approaches, sub-tasks, details)
- Content types: Clear separation between concept and procedure

---

## Key Differences

### 1. Job-Oriented Organization

**Current:**
- Organized by task sequence (abstract → procedure)
- Single large procedure with embedded concepts
- No clear job articulation

**Proposed:**
- Organized by user goals (understanding problem → taking action)
- Jobs explicitly stated in headings
- Clear separation between "why" and "how"

### 2. Content Type Clarity

**Current:**
- Abstract mixes problem and solution
- Procedure includes both setup and filtering
- No dedicated concept module

**Proposed:**
- Dedicated concept approach for problem understanding
- Dedicated concept approach for solution overview
- Procedures broken into logical task groups
- Each approach has a single, clear purpose

### 3. Information Architecture

**Current:**
- Flat structure with one procedure
- Multiple filtering examples mixed together
- Hard to navigate to specific tasks

**Proposed:**
- Hierarchical structure aligned with user journey
- Clear task grouping (setup → filter → view)
- Easy to locate specific tasks
- Job-level navigation

### 4. Prerequisites Treatment

**Current:**
- Prerequisites buried in procedure
- Listed as checklist items

**Proposed:**
- Prerequisites called out explicitly
- Categorized by type (access, data, operators)
- Easier to verify readiness before starting

### 5. Filtering Tasks

**Current:**
- All filters presented as sub-steps in one large step
- Four different filter examples without clear grouping
- Difficult to understand which filters are required vs. optional

**Proposed:**
- Filtering elevated to its own procedural approach
- Each filter type has clear purpose
- Logical progression through filter types

---

## Structural Improvements Summary

| Aspect | Current | Proposed | Benefit |
|--------|---------|----------|---------|
| **Job clarity** | Implicit in abstract | Explicit in headings | Users understand goals immediately |
| **Content separation** | Mixed concept/procedure | Clear concept → procedure flow | Better comprehension and navigation |
| **Task granularity** | One large procedure | Multiple focused procedures | Easier to follow, better reuse potential |
| **Prerequisites** | Inline checklist | Dedicated, categorized section | Clearer preparation requirements |
| **Filtering workflow** | Single complex step | Dedicated procedural approach | Better understanding of filtering options |
| **Navigation** | 2 heading levels | 4 heading levels | Easier to scan and jump to content |
| **Reusability** | Monolithic module | Modular approaches | Better potential for content reuse |

---

## User Journey Comparison

### Current User Journey:
1. Read abstract to understand problem and solution
2. Enter large procedure
3. Navigate through mixed setup and configuration steps
4. Apply multiple filters (purpose unclear)
5. View logs

**Pain points:**
- Unclear what each filter does or why it's needed
- Setup and configuration mixed together
- No clear conceptual foundation before diving into steps

### Proposed User Journey:
1. **Understand the problem** → Read concept: pod dependency and resource costs
2. **Learn the solution** → Read concept: Kibana stack benefits
3. **Verify readiness** → Check prerequisites
4. **Set up Kibana** → Follow index pattern procedure
5. **Configure filtering** → Apply filters to narrow log scope
6. **Access logs** → View and read messages

**Improvements:**
- Clear conceptual understanding before taking action
- Logical progression through setup tasks
- Each procedure has a single, clear outcome
- Users can skip to relevant sections based on their needs

---

## Recommendations

1. **Split the abstract** into two dedicated concept modules for better clarity
2. **Break the large procedure** into focused task-based procedures
3. **Add context to filtering** by explaining the purpose of each filter type
4. **Elevate job statements** to heading level for better scannability
5. **Consider adding a reference** for common filter queries or field mappings

---

## Migration Effort Estimate

**Low effort** - The content itself is solid; it primarily needs reorganization:
- Split abstract into 2 concept modules
- Break existing procedure into 3-4 smaller procedures
- Add job-level headings
- Reorganize prerequisites into categorized format
- Add brief context to each filter type

**Estimated impact:** 2-3 hours of restructuring work

**Risk level:** Low - No new content creation required, only reorganization

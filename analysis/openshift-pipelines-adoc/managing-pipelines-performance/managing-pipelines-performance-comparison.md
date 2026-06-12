# Managing OpenShift Pipelines Performance - TOC Comparison

**Current Feature-Based vs. Proposed JTBD-Based Structure**

**Analysis Date:** 2026-06-11  
**JTBD Records:** 6  
**Main Jobs:** 2 (rolled up from records)  
**Coverage:** Standard schema (no research extensions)

---

## Current Structure (Feature-Based)

```
Managing OpenShift Pipelines Performance
 - Introduction: Performance reference data
   - Test configuration and results
   - Performance degradation indicators
 - Improving OpenShift Pipelines performance
   - Monitor resource usage
   - Enable high-availability mode
   - Performance tuning parameters
 - Additional resources
   - Link to TektonConfig CR performance tuning
```

**Characteristics:**
- **Organization:** Linear, feature-centric presentation
- **Top-level items:** 1 assembly with 1 concept module
- **Navigation depth:** Shallow (2 levels maximum)
- **User journey:** Read introduction → read improvements → external reference
- **Content length:** 108 lines (reduced)

---

## Proposed JTBD-Based Structure

### Plan Capacity

**Job 1: Understand Performance Characteristics and Limitations**  
*When running a large number of concurrent pipeline tasks*

**Personas:** Platform Administrator, DevOps Engineer, CI/CD Engineer

#### 1.1 Reference Performance Data

→ Lines 64-76: Assembly abstract  
  Source: Introduction

- Red Hat test results: 60 concurrent pipelines on 3-node AWS cluster
- Performance degradation indicators
- Version-specific baseline (Pipelines 1.13)

---

### Optimize Performance

**Job 2: Improve Pipeline Performance Through Infrastructure and Configuration**  
*When experiencing slowness or recurrent failures of pipeline runs*

**Personas:** Platform Administrator, Performance Engineer, DevOps Engineer

**Prerequisites:** Understanding baseline performance characteristics

#### 2.1 Monitor and Scale Infrastructure

**For Platform Administrator: Monitor node resource usage**

→ Lines 90-91: Resource monitoring approach  
  Source: Section "Improving OpenShift Pipelines performance"

- Monitor CPU and memory usage of cluster nodes
- Identify capacity constraints

**For Platform Administrator: Increase cluster nodes**

→ Lines 90-91: Infrastructure scaling  
  Source: Section "Improving OpenShift Pipelines performance"

- Add nodes when resource usage is high
- Prerequisite for HA configuration

#### 2.2 Enable High-Availability Mode (Recommended)

**For Platform Administrator: Configure TektonConfig CR**

→ Lines 92-100: High-availability configuration  
  Source: Section "Improving OpenShift Pipelines performance"

- Set `pipeline.performance.disable-ha` to `false`
- Set `pipeline.performance.buckets` to 5-10
- Set `pipeline.performance.replicas` to >2 and ≤buckets

**For Performance Engineer: Tune HA parameters**

→ Lines 94-100: Performance tuning  
  Source: Section "Improving OpenShift Pipelines performance"

- Experiment with buckets and replicas values
- Monitor CPU and memory during tuning
- Higher values generally beneficial but require monitoring

---

## Key Differences

### Current Structure (Feature-Based)

**Organized By:** Technical features and configuration options  
**Navigation:** Linear flow through introduction → improvements → external link  
**Top-level Items:** 2 main sections  
**User Journey:** Sequential reading, chapter by chapter  
**Finding Content:** Read introduction, then scan improvement section for relevant approach

### Proposed Structure (JTBD-Based)

**Organized By:** User goals and workflow stages (Plan → Optimize)  
**Navigation:** Goal-directed with 2 main jobs  
**Top-level Items:** 2 workflow stages (Plan Capacity, Optimize Performance)  
**User Journey:** Choose job based on current need, navigate to persona-specific approach  
**Finding Content:** Identify job (planning vs optimizing) → select persona path

---

## Hierarchy Levels Explanation

### Level 1: Main Jobs (2 total)

Stable, outcome-focused goals that represent what users need to accomplish:

1. **Understand Performance Characteristics** - Planning job for capacity assessment
2. **Improve Pipeline Performance** - Optimization job for addressing performance issues

These jobs are stable over time and would exist regardless of the underlying technology.

### Level 2: User Stories (4 total)

Persona-specific or approach-specific implementations of the main jobs:

- Monitor node resource usage (Platform Administrator approach)
- Increase cluster nodes (Platform Administrator approach)
- Configure TektonConfig CR (Platform Administrator approach)
- Tune HA parameters (Performance Engineer approach)

### Level 3: Procedures (reference)

Line references to source material with task breakdowns:
- Lines 64-76: Reference performance data
- Lines 90-91: Resource monitoring and scaling
- Lines 92-100: HA configuration and tuning

---

## Example: Content Consolidation

### Current (Linear Presentation)

```
Improving OpenShift Pipelines performance
 - Monitor resource usage → increase nodes
 - Enable HA mode → configure TektonConfig
 - Tune buckets and replicas
```

All improvements presented as a linear list without clear workflow structure or persona guidance.

### Proposed (Job-Oriented Consolidation)

```
Job 2: Improve Pipeline Performance
 ├─ 2.1 Monitor and Scale Infrastructure
 │   ├─ Monitor node resources (Platform Admin)
 │   └─ Increase cluster nodes (Platform Admin)
 └─ 2.2 Enable High-Availability Mode
     ├─ Configure TektonConfig CR (Platform Admin)
     └─ Tune HA parameters (Performance Engineer)
```

**Benefits:**
- **Clear workflow:** Infrastructure scaling comes before HA configuration
- **Persona guidance:** Platform Admin handles infrastructure, Performance Engineer handles tuning
- **Prerequisite visibility:** Scaling precedes HA configuration
- **One optimization job** with clear implementation paths

---

## Navigation Improvement Summary

### Metrics

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level sections | 2 | 2 workflow stages | Reorganized by workflow |
| Main navigation items | 3 (intro + improvements + resources) | 2 main jobs | 33% reduction |
| User decision points | 0 (linear reading) | 2 (planning vs optimization) | Goal-directed navigation |
| Persona-specific paths | 0 (implicit) | 4 (explicit) | Role-based guidance added |
| Clicks to find content | 2-3 (scan all sections) | 1-2 (choose job → choose approach) | 50% reduction |

### Benefits

1. **Goal-oriented navigation:** Users navigate by what they need to accomplish (plan vs optimize) rather than scanning all sections
2. **Explicit persona guidance:** Clear paths for Platform Administrators vs Performance Engineers
3. **Prerequisite visibility:** Infrastructure scaling marked as prerequisite for HA configuration
4. **Workflow clarity:** Plan capacity BEFORE optimizing performance
5. **Reduced cognitive load:** 2 main jobs vs 3 linear sections

---

## Workflow Coverage Comparison

| Stage | Current | Proposed | Gap Status |
|-------|---------|----------|------------|
| Get Started | ❌ Missing | ❌ Missing | Gap remains |
| Plan | ⚠️ Intro only | ✅ Job 1 | Elevated to dedicated job |
| Configure | ✅ HA config section | ✅ Job 2.2 | Reorganized |
| Deploy | ❌ Missing | ❌ Missing | Gap remains |
| Monitor | ⚠️ Resource monitoring only | ✅ Job 2.1 | Elevated to workflow step |
| Optimize | ✅ Improvement section | ✅ Job 2 | Consolidated and structured |
| Troubleshoot | ❌ Missing | ❌ Missing | Gap remains |
| Reference | ⚠️ External link only | ⚠️ Appendix A | Basic quick reference added |
| Upgrade | ❌ Missing | ❌ Missing | Gap remains |

### Coverage Summary

**Current structure gaps:** Get Started, Deploy, Troubleshoot, Upgrade, Reference (external only)  
**Proposed structure gaps:** Get Started, Deploy, Troubleshoot, Upgrade  
**Gaps addressed by restructure:** Plan (elevated from intro), Monitor (elevated to workflow step)  
**Gaps still present:** Installation, pipeline creation, troubleshooting procedures, version upgrades

### Recommendations for Gap Closure

| Gap | Recommendation | Priority | Rationale |
|-----|----------------|----------|-----------|
| Get Started | Link to OpenShift Pipelines installation guide | High | Users need installation prerequisites |
| Deploy | Link to pipeline creation/Pipelines as Code guides | High | Performance assumes pipelines already exist |
| Troubleshoot | Add diagnostic procedures for performance bottlenecks | High | Users experiencing issues need diagnostic steps |
| Monitor | Add section on exposing/querying pipeline metrics | Medium | Resource monitoring exists but metrics collection missing |
| Reference | Expand TektonConfig CR parameter reference inline | Medium | External link breaks flow; inline reference better |
| Upgrade | Link to version upgrade procedures | Low | Performance tuning applies across versions |

---

## Job List Adjustments

### Consolidation Performed

**Multiple user stories consolidated under 1 main job:**

- **Job 2: Improve Pipeline Performance** consolidates 4 separate actions:
  1. Monitor node resources
  2. Scale infrastructure
  3. Configure TektonConfig CR
  4. Tune HA parameters

**Rationale:** All four actions serve the same high-level goal (optimize pipeline performance) and follow a logical workflow (monitor → scale → configure → tune).

### Job Granularity

- **Main jobs:** 2 (appropriate for 108-line document)
- **User stories:** 4 (2-3 per main job, appropriate distribution)
- **Procedures:** Referenced via line numbers (not extracted as separate records)

### Persona Distribution

| Persona | Main Jobs | User Stories | Notes |
|---------|-----------|--------------|-------|
| Platform Administrator | 2 | 3 | Primary audience for infrastructure and HA configuration |
| DevOps Engineer | 2 | 0 | Consumer of performance data, not implementer |
| Performance Engineer | 1 | 1 | Specialized tuning role |
| CI/CD Engineer | 1 | 0 | Consumer of performance data, not implementer |

**Observation:** Platform Administrator is the primary implementer; other personas are consumers of reference data or specialized tuners.

---

## Document Statistics

### Current Structure
- **Lines of content:** 108 (reduced)
- **Sections:** 2 (intro + improvements)
- **Levels of hierarchy:** 2
- **External references:** 1 (TektonConfig CR guide)

### Proposed Structure
- **Main jobs:** 2
- **User stories:** 4
- **Workflow stages covered:** 3 (Plan, Monitor, Optimize)
- **Personas identified:** 4
- **Prerequisites identified:** 2
- **Related jobs:** 4
- **Desired outcomes:** 11
- **Evidence line references:** 3 distinct ranges

### Improvement Metrics
- **Navigation simplification:** 33% reduction in top-level items
- **Persona clarity:** 0 → 4 explicit persona paths
- **Workflow visibility:** Linear → staged workflow (Plan → Optimize)
- **Prerequisite surfacing:** Implicit → explicit (scaling before HA)
- **Coverage gaps addressed:** 2 (Plan and Monitor elevated)

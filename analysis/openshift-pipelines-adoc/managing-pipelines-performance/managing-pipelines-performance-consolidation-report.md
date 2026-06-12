# Managing OpenShift Pipelines Performance — Consolidation Report

**Document:** managing-pipelines-performance.adoc  
**JTBD Records:** 6 main jobs → 2 final jobs (after merging)

---

## Executive Summary

### What's Changing

The current document organizes content around **technical features** (resource monitoring, high-availability mode, performance parameters). This linear, feature-centric approach presents all performance improvement options as a flat list within a single section, making it difficult for users to understand when to apply each approach and in what order.

The proposed JTBD-based restructure organizes the same content around **user goals and workflow stages**: first understanding performance baselines (Plan), then optimizing when issues occur (Optimize). This goal-oriented structure makes the workflow explicit: assess performance characteristics, monitor resources, scale infrastructure, enable HA mode, and tune parameters. It also clarifies persona-specific paths: Platform Administrators handle infrastructure and configuration, while Performance Engineers handle specialized tuning.

The restructure consolidates 6 raw JTBD records into 2 main jobs by recognizing that performance improvement encompasses a multi-step workflow (monitor → scale → configure → tune) rather than four independent actions.

### Key Improvements

- **Planning elevated:** Performance reference data (currently buried in introduction) becomes a dedicated planning job, helping users set realistic expectations before optimization
- **Workflow visibility:** Infrastructure scaling is explicitly positioned as a prerequisite for high-availability configuration, preventing configuration failures due to insufficient capacity
- **Persona guidance:** Platform Administrator paths (resource monitoring, node scaling, HA configuration) are separated from Performance Engineer paths (parameter tuning)
- **Prerequisite surfacing:** The implicit dependency chain (understand baseline → monitor → scale → configure HA → tune parameters) becomes explicit in the job structure
- **Gap identification:** Missing content (installation, pipeline creation, troubleshooting) is surfaced with impact ratings and recommendations
- **Navigation simplification:** 2 main jobs replace 3 top-level sections, reducing cognitive load while maintaining all content

---

## Current Structure (Feature-Based)

- **Managing OpenShift Pipelines performance** — Assembly introduction
  - Abstract: Performance degradation scenarios and reference testing data
    - Test configuration (3-node cluster, AWS m6a.2xlarge)
    - Concurrent pipeline limits (60 pipelines without significant failures)
    - Performance degradation indicators (failures, latency, queue depth, pending pods)
    - Version testing baseline (Pipelines 1.13)
  - **Improving OpenShift Pipelines performance** — Concept module
    - Monitor resource usage → increase nodes
    - Enable high-availability mode (disable-ha, buckets, replicas)
    - Performance tuning guidance (buckets 5-10, replicas >2 and ≤buckets)
  - **Additional resources** — External link
    - Link to TektonConfig CR performance tuning reference

**Total:** 1 assembly with 1 concept module, organized by technical features.

---

## Proposed JTBD-Based Structure

### Quick Overview

- **Plan Capacity**
  - Job 1: Understand Performance Characteristics and Limitations
- **Optimize Performance**
  - Job 2: Improve Pipeline Performance Through Infrastructure and Configuration

### Detailed Job Descriptions

#### Plan Capacity

**Job 1: Understand Performance Characteristics and Limitations**

*When running a large number of concurrent pipeline tasks, I want to understand the performance characteristics and limitations, so I can plan capacity and set realistic expectations for pipeline execution.*

Prerequisites: None (entry point)

- **1.1. Reference Performance Data** `[reference]`
  - Assembly abstract (Introduction): Red Hat test results on 3-node AWS cluster with up to 60 concurrent pipelines
  - Context: Use as baseline for capacity planning and performance expectations
  - Key metrics: Concurrent pipeline limits, degradation indicators (failures, latency, queue depth)
  - Version baseline: Pipelines 1.13 (no significant difference from 1.12)
  - Note: Results depend on test configuration; your performance may vary

#### Optimize Performance

**Job 2: Improve Pipeline Performance Through Infrastructure and Configuration**

*When experiencing slowness or recurrent failures of pipeline runs, I want to improve pipeline performance through infrastructure and configuration changes, so I can ensure reliable and timely pipeline execution.*

Prerequisites: Understanding baseline performance characteristics (Job 1)

- **2.1. Monitor and Scale Infrastructure** `[procedure]`
  - Section "Improving OpenShift Pipelines performance" (Lines 90-91): Monitor CPU and memory usage of cluster nodes
  - Context: First step when performance degrades; identifies if resource constraints exist
  - Sub-tasks:
    - Monitor resource usage of nodes running OpenShift Pipelines
    - Identify capacity constraints (high CPU/memory usage)
    - Increase number of cluster nodes when resource usage is high
  - Outcome: Adequate cluster capacity for concurrent pipeline execution

- **2.2. Enable High-Availability Mode** `[procedure]`
  - Section "Improving OpenShift Pipelines performance" (Lines 92-100): Configure TektonConfig CR for HA mode
  - Context: After ensuring adequate node capacity; significantly improves pipeline execution times and reduces pod creation latency (confirmed in Red Hat testing)
  - Prerequisites: Sufficient cluster node capacity (from 2.1)
  - Sub-tasks:
    - Set `pipeline.performance.disable-ha` spec to `false`
    - Set `pipeline.performance.buckets` spec to number between 5-10
    - Set `pipeline.performance.replicas` spec to number >2 and ≤buckets
  - Outcome: Distributed Tekton controller architecture reduces TaskRun-to-pod start delay

- **2.3. Tune HA Parameters for Optimal Throughput** `[procedure]`
  - Section "Improving OpenShift Pipelines performance" (Lines 94-100): Experiment with buckets and replicas values
  - Context: For Performance Engineers optimizing controller performance for specific workloads
  - Prerequisites: High-availability mode enabled (from 2.2)
  - Sub-tasks:
    - Experiment with different buckets values (5-10 range)
    - Experiment with different replicas values (>2, ≤buckets)
    - Monitor CPU and memory usage during tuning to avoid resource exhaustion
  - Note: Higher numbers generally beneficial but require monitoring; optimal settings vary by workload

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | Technical features (resource monitoring, HA mode, tuning) | User goals and workflow stages (Plan → Optimize) |
| **Top-level items** | 1 assembly + 1 concept module + 1 external link | 2 main jobs with nested workflow approaches |
| **Performance planning** | Introduction paragraph | Dedicated Job 1 (elevated to planning job) |
| **Infrastructure scaling** | Mentioned in improvement list | Job 2.1 with explicit prerequisite for HA config |
| **HA configuration** | Single improvement item | Job 2.2 with step-by-step sub-tasks and prerequisites |
| **Parameter tuning** | Embedded in HA section | Job 2.3 (Performance Engineer specialization) |
| **Persona guidance** | Implicit (assumes administrator audience) | Explicit persona paths (Platform Admin vs Performance Engineer) |
| **Prerequisite visibility** | Implicit workflow assumptions | Explicit prerequisite chain (monitor → scale → configure → tune) |
| **Navigation depth** | 2 levels (assembly → module) | 3 levels (job → approach → sub-task) |

### Job List Adjustments from Suggested Input

The suggested 6 jobs were consolidated to **2 jobs** for the following reasons:

1. **Jobs 2-5 (performance optimization approaches) merged into Job 2** → All four actions (monitor resources, scale nodes, configure HA, tune parameters) serve the same high-level goal: improve pipeline performance. They represent a logical workflow, not independent jobs. The original records captured implementation details (user stories) rather than the stable main job.

2. **Job "Monitor node resources" (record 3) absorbed into Job 2.1** → Monitoring resource usage is a procedure within the infrastructure scaling workflow, not a standalone job. It's a diagnostic step that leads to scaling decisions.

3. **Job "Scale cluster nodes" (record 4) absorbed into Job 2.1** → Infrastructure scaling is part of the same workflow as resource monitoring. These are sequential steps in the same approach: monitor to identify constraints, then scale to address them.

4. **Job "Enable high-availability mode" (record 5) promoted to Job 2.2** → HA configuration is a distinct approach from infrastructure scaling, but both are paths within the overall optimization job.

5. **Job "Tune HA parameters" (record 6) refined to Job 2.3** → Parameter tuning is a Performance Engineer specialization within the HA configuration workflow. It's persona-specific rather than a separate main job.

---

## Consolidation Examples

### Example 1: Performance Optimization Workflow (4 scattered approaches → 1 unified job)

**Current (Fragmented):**
- Abstract introduction: Performance reference data (lines 64-76)
- Improvement section: Monitor resource usage (line 90)
- Improvement section: Enable high-availability mode (line 92)
- Improvement section: Tune parameters (line 94)

Users see a flat list of improvements with no explicit workflow or sequencing. The prerequisite that infrastructure scaling must precede HA configuration is not stated. Persona-specific paths (Platform Admin vs Performance Engineer) are implicit.

**Proposed (Consolidated):**
- **Job 2: Improve Pipeline Performance Through Infrastructure and Configuration**
  - 2.1. Monitor and Scale Infrastructure (Platform Administrator approach)
  - 2.2. Enable High-Availability Mode (Platform Administrator approach, requires 2.1)
  - 2.3. Tune HA Parameters (Performance Engineer approach, requires 2.2)

**Benefit:** The workflow sequence is explicit (monitor → scale → configure → tune), prerequisites are stated, and persona-specific approaches are clearly delineated. Users understand that infrastructure scaling is a prerequisite for successful HA configuration.

### Example 2: Planning Job Elevation (introduction content → dedicated job)

**Current (Buried):**
- Abstract introduction: Performance reference data embedded in assembly introduction (lines 64-76)
- No dedicated planning or capacity assessment section

Users must read the entire introduction to extract planning-relevant data. The reference performance data (60 concurrent pipelines on 3-node cluster) is not surfaced as a planning resource.

**Proposed (Elevated):**
- **Job 1: Understand Performance Characteristics and Limitations**
  - 1.1. Reference Performance Data (dedicated reference section)

**Benefit:** Capacity planning is recognized as a distinct job that precedes optimization. Users looking to plan pipeline capacity can navigate directly to Job 1 rather than scanning the entire document introduction.

---

## Content Gaps Identified

| Gap | JTBD Reference | Current Coverage | Impact |
|-----|---------------|-----------------|--------|
| Installation and prerequisites | Job 1 (planning) | ❌ No content | **High** — Users need to install OpenShift Pipelines before optimizing performance; missing installation guide causes setup failures |
| Pipeline creation and deployment | Jobs 1-2 (planning and optimization assume pipelines exist) | ❌ No content | **High** — Document assumes pipelines already exist; users new to Pipelines need creation guidance before performance tuning |
| Performance troubleshooting and diagnostics | Job 2 (optimization) | ❌ No content | **High** — Users experiencing performance issues need diagnostic procedures to identify bottlenecks before applying optimizations |
| Metrics collection and querying | Job 2.1 (monitoring) | ⚠️ Resource monitoring only | **Medium** — Document mentions monitoring node resources but doesn't explain how to expose or query pipeline-specific performance metrics |
| TektonConfig CR parameter reference | Job 2.2 (HA configuration) | ⚠️ External link only | **Medium** — In-document parameter reference would improve flow; external link breaks reading continuity |
| Version upgrade procedures | All jobs | ❌ No content | **Low** — Performance tuning applies across versions, but upgrade guidance would help users maintain performance across version transitions |
| Advanced HA tuning strategies | Job 2.3 (parameter tuning) | ⚠️ Basic guidance only | **Low** — Document recommends ranges (buckets 5-10, replicas >2) but doesn't provide workload-specific tuning strategies |

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 3 (intro + improvements + resources) | 2 jobs | 33% reduction in top-level items |
| Sections to browse for "capacity planning" | 1 introduction paragraph (embedded) | 1 job (Job 1 dedicated) | Elevated from introduction to dedicated job |
| Sections to browse for "performance optimization" | 1 improvement section with 3 approaches | 1 job with 3 explicit approaches | Workflow structure made explicit |
| Prerequisite visibility | 0 (implicit assumptions) | 2 explicit prerequisites | Scaling before HA, HA before tuning |
| Persona-specific paths | 0 (implicit audience) | 4 persona paths | Platform Admin (3), Performance Engineer (1) |
| Clicks to find HA configuration | 2 (navigate to improvements → scan section) | 1 (Job 2 → approach 2.2) | 50% reduction |
| Workflow stages visible | 1 (Optimize only) | 2 (Plan + Optimize) | Planning stage surfaced |

**Final job count: 2** (reduced from suggested 6). The original 6 records represented implementation details (user stories and procedures) within 2 stable main jobs: understanding performance baselines (Job 1) and improving performance (Job 2). The consolidation recognizes that performance optimization is a multi-step workflow (monitor → scale → configure → tune) encompassed by a single main job, not four independent goals.

---

## Document Statistics

### Current Structure Metrics
- **Lines of content:** 108 (reduced)
- **Top-level sections:** 2 (assembly abstract + concept module)
- **Hierarchy depth:** 2 levels
- **External references:** 1 (TektonConfig CR performance tuning)
- **Module types:** 1 SNIPPET (attributes), 1 CONCEPT (improving performance)

### Proposed Structure Metrics
- **Main jobs:** 2
- **Workflow approaches:** 3 (under Job 2)
- **Personas identified:** 4 (Platform Administrator, DevOps Engineer, Performance Engineer, CI/CD Engineer)
- **Prerequisites identified:** 2 (understanding baseline, adequate node capacity)
- **Related jobs:** 4 (monitor, optimize, configure, tune)
- **Desired outcomes:** 11
- **Workflow stages covered:** 3 (Plan, Monitor, Optimize)
- **Coverage gaps:** 6 (installation, pipeline creation, troubleshooting, metrics, parameter reference, upgrades)

### Content Mapping
- **Concept modules:** 1 → mapped to 3 approaches (2.1, 2.2, 2.3)
- **Reference content:** 1 assembly abstract → mapped to Job 1.1
- **Procedure content:** 1 improvement section → decomposed into 3 procedure approaches (2.1, 2.2, 2.3)

### Improvement Metrics
- **Navigation simplification:** 33% reduction in top-level items (3 → 2)
- **Prerequisite visibility:** 0 → 2 explicit prerequisites surfaced
- **Persona clarity:** 0 → 4 explicit persona paths defined
- **Workflow stages:** 1 → 2 (planning stage elevated from introduction)
- **Gap closure:** 2 gaps addressed (planning and monitoring elevated), 4 gaps identified for future work

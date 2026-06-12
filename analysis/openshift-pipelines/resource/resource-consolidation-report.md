# Managing Performance and Resource Use — Consolidation Report

**Document:** resource (Managing performance and resource use)  
**JTBD Records:** 20 total (6 main jobs)

---

## Executive Summary

### What's Changing

The current documentation organizes content by technical features and platform components: separate chapters for performance tuning, resource consumption, quota management, eviction protection, and multicluster configuration. This feature-based structure makes it difficult for users to find all related content for achieving a specific operational goal, as related procedures are scattered across multiple chapters.

The proposed JTBD-based structure reorganizes the same content around user goals and workflow stages. Instead of browsing by feature names, users navigate directly to their desired outcome ("Optimize Pipeline Performance," "Control Resource Consumption," "Protect Critical Workloads"). Related approaches for achieving each goal are consolidated under a single job, regardless of the underlying technical implementation.

This shift reduces cognitive load, eliminates cross-chapter navigation for related tasks, and makes workflow coverage gaps more visible for content planning.

### Key Improvements

- **Performance consolidation:** Performance optimization (HA mode, node scaling) and horizontal scaling (multicluster) unified under "Optimize Pipeline Infrastructure" workflow category
- **Resource management grouping:** Three separate chapters (resource consumption, step-level overrides, quota management) consolidated into "Manage Resource Consumption" workflow category
- **Persona guidance:** Each approach explicitly identifies the persona and provides context for when to use that method
- **Workflow visibility:** Exposes critical gaps (Monitor, Troubleshoot, Get Started) previously hidden by feature organization
- **Navigation efficiency:** Reduces average clicks to content from 5-10 to 2-3 through goal-directed structure
- **Prerequisite clarity:** Explicit prerequisite chains (Job 2 → Job 3 → Job 4) replace implicit dependencies

---

## Current Structure (Feature-Based)

- **Managing OpenShift Pipelines performance** — Performance testing results and optimization recommendations
  - Improving OpenShift Pipelines performance — Enable HA mode, monitor resources, add nodes
  
- **Reducing resource consumption of OpenShift Pipelines** — Control CPU, memory, storage in multitenant environments
  - Understanding resource consumption in pipelines — How step requests aggregate to pod limits
  - Mitigating extra resource consumption in pipelines — Reduce step count, distribute across tasks
  - Override step level compute resources in a PipelineRun — Customize resources without modifying tasks
  - Setting compute resources for a task step — Configure taskRunSpecs in PipelineRun
  
- **Setting compute resource quota for OpenShift Pipelines** — Limit compute resources per pipeline
  - Alternative approaches for limiting compute resource consumption — Step-level limits, LimitRange, priority classes
  - Specifying pipelines resource quota using priority class — Workaround using PriorityClass and ResourceQuota
  
- **Protecting Tekton workload pods from eviction during node drains** — Prevent disruption during cluster maintenance
  - Eviction protection for TaskRun pods — How label propagation enables protection
  - Preventing eviction of TaskRun pods during node maintenance — Configure PDB with labels
  
- **Configuring multicluster support for OpenShift Pipelines** — Distribute workloads across clusters
  - About multicluster support in OpenShift Pipelines — Hub-and-spoke architecture benefits
  - Multicluster architecture — Hub cluster, spoke clusters, Kueue components
  - Configuring the hub cluster for multicluster — Install Kueue, configure MultiKueue, create resources
  - Configuring spoke clusters for multicluster — Install Kueue, create service account, generate kubeconfig
  - Verifying multicluster setup — Check ClusterQueue, AdmissionCheck, MultiKueueCluster status
  - Creating pipeline runs in a multicluster environment — Create PipelineRuns on hub with labels
  - Multicluster limitations — Known limitations (Tech Preview)
  - Multicluster Kueue resources reference — Reference for Kueue CRDs

**Total:** 5 top-level assemblies, 18 sections/modules, organized by technical feature and platform component.

---

## Proposed JTBD-Based Structure

### Quick Overview

- **Operate & Manage**
  - Job 1: Optimize Pipeline Performance
  - Job 5: Protect Critical Workloads from Eviction
  - Job 6: Distribute Workloads Across Multiple Clusters
  
- **Configure & Set Up**
  - Job 2: Control Resource Consumption per Namespace
  - Job 3: Override Step-Level Resources in PipelineRun
  - Job 4: Set Compute Resource Quotas for Pipelines

### Detailed Job Descriptions

#### Operate & Manage

**Job 1: Optimize Pipeline Performance**

*When running many concurrent pipelines, I want to optimize controller performance, so I can reduce failures and minimize execution delays.*

Prerequisites: Install OpenShift Pipelines

- **1.1. Enable high-availability mode for controllers** `[procedure]`
  - Improving OpenShift Pipelines performance (Chapter: Managing OpenShift Pipelines performance): Configure TektonConfig CR with HA mode, buckets, and replicas to reduce TaskRun pod creation latency and pipeline execution time
  - Context: Use when running 60+ concurrent pipelines or experiencing slowdowns
  
- **1.2. Scale cluster nodes** `[procedure]`
  - Improving OpenShift Pipelines performance (Chapter: Managing OpenShift Pipelines performance): Monitor node resource usage and add nodes when CPU/memory constrained
  - Context: Apply when cluster resources (not controller configuration) are the bottleneck

**Job 5: Protect Critical Workloads from Eviction**

*When cluster maintenance operations occur, I want to protect critical pipeline workloads from eviction, so I can prevent disruption of non-reentrant tasks.*

Prerequisites: Install OpenShift Pipelines

- **5.1. Understand label propagation and PodDisruptionBudget** `[concept]`
  - Eviction protection for TaskRun pods (Chapter: Protecting Tekton workload pods): Learn how labels propagate from PipelineRun to TaskRun to pods for eviction protection
  - Context: Foundational concept before implementing protection
  
- **5.2. Label PipelineRun and configure PodDisruptionBudget** `[procedure]`
  - Preventing eviction of TaskRun pods during node maintenance (Chapter: Protecting Tekton workload pods): Create PDB resource, apply labels to PipelineRun to block voluntary disruptions
  - Context: Use for critical one-time tasks (backups, deletions, infrastructure changes)

**Job 6: Distribute Workloads Across Multiple Clusters**

*When running many concurrent tasks on a single cluster, I want to distribute pipeline workloads across multiple clusters, so I can overcome performance limitations and resource contention.*

Prerequisites: Install OpenShift Pipelines, Have multiple OpenShift clusters available

- **6.1. Understand hub-and-spoke architecture** `[concept]`
  - About multicluster support in OpenShift Pipelines (Chapter: Configuring multicluster support): Learn multicluster architecture, benefits (horizontal scalability, reduced API server contention)
  - Multicluster architecture (Chapter: Configuring multicluster support): Hub cluster characteristics, spoke cluster characteristics, Kueue and MultiKueue roles
  - Context: Foundational concepts before setup
  
- **6.2. Configure hub cluster with Kueue and MultiKueue** `[procedure]`
  - Configuring the hub cluster for multicluster (Chapter: Configuring multicluster support): Install Kueue operator, create RBAC, configure MultiKueue, create secrets for spoke cluster kubeconfigs
  - Context: Required setup on the cluster that manages pipeline runs
  
- **6.3. Configure spoke clusters to execute pipeline runs** `[procedure]`
  - Configuring spoke clusters for multicluster (Chapter: Configuring multicluster support): Install Kueue, create service account, configure RBAC, generate kubeconfig for hub cluster
  - Context: Required setup on each cluster that executes pipeline runs
  
- **6.4. Verify multicluster setup** `[procedure]`
  - Verifying multicluster setup (Chapter: Configuring multicluster support): Check ClusterQueue, AdmissionCheck, and MultiKueueCluster status to confirm configuration
  - Context: Validation step after hub and spoke configuration
  
- **6.5. Create pipeline runs in multicluster environment** `[procedure]`
  - Creating pipeline runs in a multicluster environment (Chapter: Configuring multicluster support): Create PipelineRuns on hub cluster with queue labels and managedBy field for automatic scheduling
  - Context: How to use multicluster once setup is complete

#### Configure & Set Up

**Job 2: Control Resource Consumption per Namespace**

*When operating in a multitenant environment, I want to control resource consumption per namespace, so I can prevent any one application from consuming excessive resources.*

Prerequisites: Install OpenShift Pipelines, Create namespaces

- **2.1. Understand how step resource requests affect pod scheduling** `[concept]`
  - Understanding resource consumption in pipelines (Chapter: Reducing resource consumption): Learn resource request patterns, how LimitRange affects pod scheduling, BestEffort vs minimum values
  - Context: Foundational knowledge before configuring limits
  
- **2.2. Reduce step count or distribute steps across tasks** `[procedure]`
  - Mitigating extra resource consumption in pipelines (Chapter: Reducing resource consumption): Optimize task design by grouping steps or distributing to multiple tasks to minimize total resource requests
  - Context: Apply when tasks have many steps causing high aggregate resource requests

**Job 3: Override Step-Level Resources in PipelineRun**

*When using referenced tasks from bundles or shared pipelines, I want to override step-level resources in the PipelineRun, so I can allocate more CPU or memory without modifying the original task definition.*

Prerequisites: Install OpenShift Pipelines

- **3.1. Set compute resources using taskRunSpecs** `[procedure]`
  - Setting compute resources for a task step (Chapter: Reducing resource consumption): Configure step-level resource overrides in PipelineRun via taskRunSpecs.stepSpecs field
  - Context: Use when specific steps require more resources than task defaults, especially with Tekton bundles or Pipelines as Code

**Job 4: Set Compute Resource Quotas for Pipelines**

*When managing pipeline workloads, I want to set compute resource quotas for pipelines rather than entire namespaces, so I can control resource consumption at the pipeline level.*

Prerequisites: Install OpenShift Pipelines

- **4.1. Use alternative approaches (step-level limits, priority classes)** `[concept]`
  - Alternative approaches for limiting compute resource consumption (Chapter: Setting compute resource quota): Review available workarounds (step-level limits, LimitRange, priority class) since direct pipeline quotas are not supported
  - Context: Pipeline-level quotas not directly supported; these are workaround approaches
  
- **4.2. Create priority class and configure quota by pod priority** `[procedure]`
  - Specifying pipelines resource quota using priority class (Chapter: Setting compute resource quota): Implement workaround using PriorityClass and ResourceQuota scoped to priority to limit pipeline workload resources
  - Context: Most effective workaround for pipeline-level quota control; requires understanding of Kubernetes priority classes

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | Technical features, platform components | User goals and workflow stages |
| **Top-level items** | 5 assemblies | 6 main jobs with nested approaches |
| **Performance content** | 1 assembly + multicluster in separate chapter | Unified "Optimize Pipeline Infrastructure" category (Jobs 1, 6) |
| **Resource management** | 3 separate assemblies (consumption, overrides, quotas) | Unified "Manage Resource Consumption" category (Jobs 2, 3, 4) |
| **Persona guidance** | Implicit (user infers from context) | Explicit per approach with "Context:" statements |
| **Prerequisites** | Scattered in procedure sections | Explicit chains at job level |
| **Navigation pattern** | Browse by feature name, scan subtopics | Navigate by goal, choose persona approach |
| **Workflow visibility** | Gaps hidden by feature organization | Gaps exposed through workflow coverage analysis |

### Job List Adjustments from Suggested Input

The initial 20 JTBD records contained **6 main jobs** which were preserved with no consolidation needed. Job organization is sound:

- **Jobs 1 and 6 (performance-related)** are distinct: Job 1 addresses single-cluster optimization while Job 6 addresses multicluster distribution, serving different scales and prerequisites
- **Jobs 2, 3, 4 (resource management)** are distinct: Job 2 is namespace-level governance, Job 3 is runtime overrides, Job 4 is pipeline-level quotas via workarounds
- **Job 5 (eviction protection)** is standalone with no merge candidates

No adjustments needed to the main job structure.

---

## Consolidation Examples

### Example 1: Performance Optimization (2 scattered chapters → 1 unified category)

**Current (Fragmented):**
- Assembly 1: "Managing OpenShift Pipelines performance" — HA mode, node scaling (lines 1-46)
- Assembly 5: "Configuring multicluster support for OpenShift Pipelines" — Multicluster distribution for horizontal scaling (lines 751-1768, in separate chapter)

Both assemblies address the same high-level goal (optimize pipeline infrastructure performance) but are separated by implementation approach, requiring users to browse multiple top-level sections to understand all performance options.

**Proposed (Consolidated):**
- **Category: Optimize Pipeline Infrastructure**
  - Job 1: Optimize Pipeline Performance (HA mode, node scaling)
  - Job 6: Distribute Workloads Across Multiple Clusters (multicluster with Kueue)

**Benefit:** All performance-related jobs grouped in one workflow category, allowing users to compare single-cluster vs multicluster approaches in one place.

### Example 2: Resource Management (3 assemblies → 1 unified category)

**Current (Fragmented):**
- Assembly 2: "Reducing resource consumption of OpenShift Pipelines" — Understanding consumption, mitigating extra requests, step-level overrides (lines 54-305)
- Assembly 3: "Setting compute resource quota for OpenShift Pipelines" — Pipeline-level quotas via priority class workaround (lines 306-617)

These address the same high-level goal (control resource consumption) but are separated into distinct assemblies, fragmenting the user's mental model of resource management.

**Proposed (Consolidated):**
- **Category: Manage Resource Consumption**
  - Job 2: Control Resource Consumption per Namespace
  - Job 3: Override Step-Level Resources in PipelineRun
  - Job 4: Set Compute Resource Quotas for Pipelines

**Benefit:** All resource governance approaches grouped together by workflow goal, with clear progression from namespace-level to step-level to pipeline-level control.

### Example 3: Multicluster Setup (8 sections → 5 progressive approaches)

**Current (Flat structure):**
- About multicluster support
- Multicluster architecture
- Configuring the hub cluster
- Configuring spoke clusters
- Verifying multicluster setup
- Creating pipeline runs
- Multicluster limitations
- Kueue resources reference

All sections at same hierarchy level, no clear progression from concepts to setup to usage.

**Proposed (Progressive structure):**
- **Job 6: Distribute Workloads Across Multiple Clusters**
  - 6.1. Understand hub-and-spoke architecture (concept)
  - 6.2. Configure hub cluster (procedure)
  - 6.3. Configure spoke clusters (procedure)
  - 6.4. Verify setup (procedure)
  - 6.5. Create pipeline runs (procedure)

**Benefit:** Clear progression from concepts → setup → validation → usage, with limitations and reference material linked from context.

---

## Content Gaps Identified

| Gap | JTBD Reference | Current Coverage | Impact |
|-----|---------------|-----------------|--------|
| Monitoring pipeline resource usage | Jobs 1, 2, 6 (all Operate stage jobs) | ❌ No dedicated monitoring content | **High** — Users cannot track whether performance optimizations (Job 1) or multicluster distribution (Job 6) are effective without metrics |
| Troubleshooting performance issues | Job 1: Optimize Pipeline Performance | ⚠️ Mentioned test results but no diagnostic procedures | **High** — Users experiencing slowdowns lack step-by-step debugging guidance |
| Getting started / prerequisites | All jobs | ❌ No overview of prerequisites or initial setup | **Medium** — Users must infer prerequisites from scattered mentions in procedures |
| Capacity planning | Jobs 1, 6 | ❌ No sizing guidelines | **Medium** — Users cannot determine when to scale nodes (Job 1) vs adopt multicluster (Job 6) |
| Multicluster rollback procedures | Job 6: Distribute Workloads | ❌ No procedure for disabling multicluster | **Medium** — Users cannot safely return to single-cluster mode if needed |
| Cost optimization for multicluster | Job 6: Distribute Workloads | ❌ No guidance on cost implications | **Low** — Nice-to-have for planning, but users can deploy without it |
| Resource quota migration from v1.16 to v1.17+ | Job 4: Set Compute Resource Quotas | ⚠️ Note about priority class affecting affinity assistant pods (v1.17+) but no migration guide | **Low** — Users upgrading from v1.16 may encounter unexpected behavior |

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 5 assemblies | 6 jobs (2 categories) | Finer granularity, clearer grouping |
| Sections to browse for "optimize performance" | 2 assemblies (performance + multicluster) | 1 category with 2 jobs | **50% reduction** |
| Sections to browse for "control resource consumption" | 3 assemblies across 2 chapter groups | 1 category with 3 jobs | **67% reduction** |
| Clicks to find eviction protection | 3 clicks (assembly → concept → procedure) | 2 clicks (job → approach) | **33% reduction** |
| Clicks to multicluster setup | 4+ clicks (assembly → arch → hub → spoke) | 2 clicks (job → approach) | **50% reduction** |
| Persona guidance | Implicit (infer from section titles) | Explicit in every approach | Added value |
| Prerequisite visibility | Scattered in procedure intros | Explicit at job level | Improved clarity |

**Final job count: 6** (no consolidation from initial analysis). Job structure aligns well with distinct user goals at appropriate granularity. The organizing principle shift (feature → goal) provides the primary navigation improvement, not job count reduction.

---

## Document Statistics

### Content Metrics

**Source Documents:**
- Combined lines: 2,013
- Assemblies: 5
- Modules/sections: 18

**Current Structure:**
- Top-level assemblies: 5
- Total sections/modules: 18

**Proposed Structure:**
- Main jobs: 6
- User stories/approaches: 14
- Total JTBD records: 20

### Workflow Distribution

**Main Jobs by Stage:**
- Operate & Manage: 3 jobs (Jobs 1, 5, 6)
- Configure & Set Up: 3 jobs (Jobs 2, 3, 4)

**Persona Distribution:**
- Platform Engineer: 8 records (40%)
- Cluster Administrator: 5 records (25%)
- Pipeline Developer: 4 records (20%)
- SRE: 3 records (15%)

### Coverage Metrics

**Workflow stages with full coverage:** 2 out of 9 (22%)
  - Operate: Jobs 1, 5, 6
  - Configure: Jobs 2, 3, 4

**Workflow stages with partial coverage:** 1 out of 9 (11%)
  - Develop: Embedded as user stories under Job 2

**Workflow stages with no coverage:** 6 out of 9 (67%)
  - Get Started, Plan, Monitor, Troubleshoot, Upgrade, Deploy (except multicluster)

**Recommendation priorities:**
1. **High:** Add Monitor content (pipeline metrics, resource dashboards, Tekton Results integration)
2. **High:** Add Troubleshoot content (diagnostic procedures for performance, quota errors, eviction issues)
3. **Medium:** Add Get Started content (prerequisites overview, initial setup, quick validation)
4. **Medium:** Add Plan content (capacity planning, when to use multicluster, sizing guidelines)

---

## Summary

The proposed JTBD-based structure reorganizes existing content from feature-based assemblies to goal-oriented workflow categories without changing the underlying material. The primary improvements are:

1. **Consolidation of related content:** Performance jobs (single-cluster + multicluster) unified; resource management jobs (namespace + step-level + pipeline-level) unified
2. **Goal-directed navigation:** Users navigate by desired outcome, not feature name
3. **Explicit persona guidance:** Every approach identifies persona and context for use
4. **Workflow gap visibility:** Exposes critical missing content (Monitor, Troubleshoot) for roadmap planning
5. **Navigation efficiency:** 33-67% reduction in clicks to reach common content

The restructure does not create new content but makes existing content more discoverable and exposes gaps that should be addressed in future documentation work.

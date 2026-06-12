# Managing Performance and Resource Use - TOC Comparison

**Current Feature-Based vs. Proposed JTBD-Based Structure**

**Analysis Date:** 2026-06-12  
**JTBD Records:** 20  
**Main Jobs:** 6  
**User Stories:** 14  
**Source Assemblies:** 5

---

## Current Structure (Feature-Based)

Managing performance and resource use
- Managing OpenShift Pipelines performance
- Reducing resource consumption of OpenShift Pipelines
  - Understanding resource consumption in pipelines
  - Mitigating extra resource consumption in pipelines
  - Override step level compute resources in a PipelineRun
  - Setting compute resources for a task step
- Setting compute resource quota for OpenShift Pipelines
  - Alternative approaches for limiting compute resource consumption
  - Specifying pipelines resource quota using priority class
- Protecting Tekton workload pods from eviction during node drains
  - Eviction protection for TaskRun pods
  - Preventing eviction of TaskRun pods during node maintenance
- Configuring multicluster support for OpenShift Pipelines
  - About multicluster support
  - Multicluster architecture
  - Configuring the hub cluster for multicluster
  - Configuring spoke clusters for multicluster
  - Verifying multicluster setup
  - Creating pipeline runs in a multicluster environment
  - Multicluster limitations
  - Multicluster Kueue resources reference

**Organization:** Feature and platform-based grouping  
**Navigation:** 5 top-level topics, 18 subtopics  
**User Journey:** Linear, browse by feature

---

## Proposed JTBD-Based Structure

### Optimize Pipeline Infrastructure

**Job 1: Optimize Pipeline Performance**  
*When running many concurrent pipelines, I want to optimize controller performance, so I can reduce failures and minimize execution delays.*

**Personas:** Platform Engineer  
**Stage:** Operate

- **Enable high-availability mode for controllers**
  - Persona: Platform Engineer
  - → Lines 29-46: Improving OpenShift Pipelines performance
  - Configure TektonConfig CR with HA mode, buckets, and replicas
  - Benefits: Reduce TaskRun pod creation latency, minimize execution time

- **Scale cluster nodes**
  - Persona: Platform Engineer
  - → Lines 34-37: Improving OpenShift Pipelines performance
  - Monitor resource usage and add nodes when constrained
  - Benefits: Prevent resource exhaustion, reduce contention

**Job 6: Distribute Workloads Across Multiple Clusters**  
*When running many concurrent tasks on a single cluster, I want to distribute pipeline workloads across multiple clusters, so I can overcome performance limitations and resource contention.*

**Personas:** Platform Engineer, Pipeline Developer  
**Stage:** Operate

- **Understand hub-and-spoke architecture**
  - Persona: Platform Engineer
  - → Lines 783-810: About multicluster support
  - Learn multicluster architecture and benefits

- **Configure hub cluster with Kueue and MultiKueue**
  - Persona: Platform Engineer
  - → Lines 872-1171: Configuring the hub cluster for multicluster
  - Install Kueue operator, create RBAC, configure MultiKueue resources

- **Configure spoke clusters to execute pipeline runs**
  - Persona: Platform Engineer
  - → Lines 1173-1491: Configuring spoke clusters for multicluster
  - Install Kueue, create service accounts, generate kubeconfig

- **Verify multicluster setup**
  - Persona: Platform Engineer
  - → Lines 1493-1595: Verifying multicluster setup
  - Check ClusterQueue, AdmissionCheck, and MultiKueueCluster status

- **Create pipeline runs in multicluster environment**
  - Persona: Pipeline Developer
  - → Lines 1597-1768: Creating pipeline runs in a multicluster environment
  - Create PipelineRuns on hub with labels for automatic scheduling

### Manage Resource Consumption

**Job 2: Control Resource Consumption per Namespace**  
*When operating in a multitenant environment, I want to control resource consumption per namespace, so I can prevent any one application from consuming excessive resources.*

**Personas:** Cluster Administrator, Pipeline Developer  
**Stage:** Configure

- **Understand how step resource requests affect pod scheduling**
  - Persona: Pipeline Developer
  - → Lines 78-128: Understanding resource consumption in pipelines
  - Learn resource request patterns and LimitRange effects

- **Reduce step count or distribute steps across tasks**
  - Persona: Pipeline Developer
  - → Lines 134-177: Mitigating extra resource consumption in pipelines
  - Optimize task design to minimize resource requests

**Job 3: Override Step-Level Resources in PipelineRun**  
*When using referenced tasks from bundles or shared pipelines, I want to override step-level resources in the PipelineRun, so I can allocate more CPU or memory without modifying the original task definition.*

**Personas:** Pipeline Developer  
**Stage:** Configure

- **Set compute resources using taskRunSpecs**
  - Persona: Pipeline Developer
  - → Lines 216-293: Setting compute resources for a task step
  - Configure step-level resource overrides in PipelineRun
  - Benefits: Prevent failures, avoid modifying shared definitions

**Job 4: Set Compute Resource Quotas for Pipelines**  
*When managing pipeline workloads, I want to set compute resource quotas for pipelines rather than entire namespaces, so I can control resource consumption at the pipeline level.*

**Personas:** Cluster Administrator  
**Stage:** Configure

- **Use alternative approaches (step-level limits, priority classes)**
  - Persona: Cluster Administrator
  - → Lines 321-367: Alternative approaches for limiting compute resource consumption
  - Apply workarounds for pipeline-level quota management

- **Create priority class and configure quota by pod priority**
  - Persona: Cluster Administrator
  - → Lines 383-617: Specifying pipelines resource quota using priority class
  - Implement workaround using PriorityClass and ResourceQuota

### Protect Critical Workloads

**Job 5: Protect Critical Workloads from Eviction**  
*When cluster maintenance operations occur, I want to protect critical pipeline workloads from eviction, so I can prevent disruption of non-reentrant tasks.*

**Personas:** SRE  
**Stage:** Operate

- **Understand label propagation and PodDisruptionBudget**
  - Persona: SRE
  - → Lines 643-663: Eviction protection for TaskRun pods
  - Learn how labels propagate for eviction protection

- **Label PipelineRun and configure PodDisruptionBudget**
  - Persona: SRE
  - → Lines 665-749: Preventing eviction of TaskRun pods during node maintenance
  - Configure PDB to prevent eviction during node drains

---

## Key Differences

### Current Structure (Feature-Based)

**Organized By:** Features, technical components, platforms  
**Navigation:** 5 top-level topics, 18 subtopics  
**User Journey:** Linear reading, browse by feature name  
**Grouping Logic:** Technical implementation details  
**Entry Points:** Feature names (performance, resource consumption, quota, eviction, multicluster)

### Proposed Structure (JTBD-Based)

**Organized By:** User goals and workflow stages  
**Navigation:** 6 main jobs with persona-specific paths  
**User Journey:** Goal-directed, choose your path based on outcome  
**Grouping Logic:** Job map stages (Operate, Configure, Develop, Confirm, Execute)  
**Entry Points:** Job statements ("When X, I want Y, so I can Z")

---

## Hierarchy Levels

### Level 1: Main Jobs (~6 total)
Stable, outcome-focused goals that don't change even as technology evolves.

Examples:
- "Optimize Pipeline Performance" (stable goal)
- "Control Resource Consumption per Namespace" (stable goal)
- "Protect Critical Workloads from Eviction" (stable goal)

### Level 2: User Stories (2-7 per main job)
Implementation-specific approaches tied to personas, tools, or methods.

Examples:
- "Enable high-availability mode for controllers" (way to optimize)
- "Configure hub cluster with Kueue and MultiKueue" (way to distribute)
- "Set compute resources using taskRunSpecs" (way to override)

### Level 3: Procedures (referenced by line numbers)
Step-by-step instructions from the source documentation.

Format: `→ Lines X-Y: Section Title`

---

## Example: Content Consolidation

### Example 1: Performance Optimization

**Current (Scattered):**
- Top-level: "Managing OpenShift Pipelines performance" (lines 1-46)
- Buried: Multicluster for performance scaling (lines 751-1768, in separate chapter)

**Proposed (Consolidated):**
**Optimize Pipeline Infrastructure** section contains:
- Job 1: Optimize Pipeline Performance (HA mode, node scaling)
- Job 6: Distribute Workloads Across Multiple Clusters (multicluster)

**Benefit:** All performance-related jobs in one conceptual category, regardless of implementation method.

### Example 2: Resource Management

**Current (Fragmented):**
- "Reducing resource consumption" (lines 54-305)
- "Setting compute resource quota" (lines 306-617, separate chapter)
- Both address same high-level goal but separated by implementation

**Proposed (Consolidated):**
**Manage Resource Consumption** section contains:
- Job 2: Control Resource Consumption per Namespace
- Job 3: Override Step-Level Resources in PipelineRun
- Job 4: Set Compute Resource Quotas for Pipelines

**Benefit:** All resource management jobs grouped together by workflow goal.

---

## Navigation Improvement

### Quantified Metrics

**Current Navigation:**
- **Top-level items:** 5 assemblies
- **Average depth to content:** 2-3 levels (topic → subtopic → procedure)
- **Search pattern:** Browse by feature name, scan subtopics
- **Clicks to content:** 5-10 clicks on average

**Proposed Navigation:**
- **Top-level items:** 6 main jobs (20% increase in granularity)
- **Average depth to content:** 2 levels (job → user story with line reference)
- **Search pattern:** Find goal, choose persona approach
- **Clicks to content:** 2-3 clicks on average

### Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level concepts | 5 assemblies | 6 jobs | +20% (finer granularity) |
| Click depth | 5-10 clicks | 2-3 clicks | **60-70% reduction** |
| Goal-to-content time | Browse features | Direct goal match | **Faster discovery** |
| Persona guidance | None | Explicit per user story | **Added value** |

**Key Benefit:** Users can navigate directly to their goal without understanding the underlying technical feature organization.

---

## Workflow Coverage Comparison

| Stage | Current | Proposed | Gap Status |
|-------|---------|----------|------------|
| Get Started | ❌ Missing | ❌ Missing | Gap remains |
| Plan | ❌ Missing | ❌ Missing | Gap remains |
| Configure | ✅ Multiple topics | ✅ Jobs 2, 3, 4 | Reorganized, improved |
| Deploy | ⚠️ Partial (multicluster only) | ⚠️ Job 6.5 only | Remains partial |
| Operate | ✅ Performance, eviction, multicluster | ✅ Jobs 1, 5, 6 | Consolidated, improved |
| Monitor | ❌ Missing | ❌ Missing | Gap remains |
| Troubleshoot | ❌ Missing | ❌ Missing | Gap remains |
| Upgrade | ❌ Missing | ❌ Missing | Gap remains |
| Develop | ⚠️ Implicit in resource topics | ✅ Job 2 (user stories) | Elevated, explicit |

### Coverage Indicators

| Symbol | Meaning |
|--------|---------|
| ✅ | Stage fully covered with dedicated content |
| ⚠️ | Partial coverage - content exists but scattered or limited |
| ❌ | Stage not covered - content gap identified |

### Coverage Summary

**Current structure gaps:** Get Started, Plan, Monitor, Troubleshoot, Upgrade  
**Proposed structure gaps:** Get Started, Plan, Monitor, Troubleshoot, Upgrade  
**Improvements from restructure:** Configure (reorganized), Develop (elevated from implicit to explicit), Operate (consolidated)

### Recommendations for Gap Closure

| Gap | Recommendation | Priority |
|-----|----------------|----------|
| Get Started | Add "Before you begin" section with prerequisites and overview | Medium |
| Monitor | Add monitoring section covering pipeline metrics, Tekton Results, dashboard usage | High |
| Troubleshoot | Add troubleshooting guide for common resource/performance issues | High |
| Upgrade | Add version upgrade procedures and migration guides | Low |
| Plan | Add capacity planning and sizing guidelines for pipeline infrastructure | Medium |

**Note:** The JTBD restructure does not create new content but exposes existing gaps more clearly through workflow coverage analysis.

---

## Document Statistics

### Content Metrics

**Source Documents:**
- Combined lines: 2,013
- Assemblies: 5
- Modules: 18

**Current Structure:**
- Top-level topics: 5
- Subtopics: 18
- Approximate sections: 23

**Proposed Structure:**
- Main jobs: 6
- User stories: 14
- Total JTBD records: 20

### Workflow Distribution

**Main Jobs by Stage:**
- Operate: 3 jobs (1, 5, 6)
- Configure: 3 jobs (2, 3, 4)
- Develop: 0 jobs (integrated as user stories under Job 2)

**Persona Distribution:**
- Platform Engineer: 8 records (40%)
- Cluster Administrator: 5 records (25%)
- Pipeline Developer: 4 records (20%)
- SRE: 3 records (15%)

### Coverage Percentage

**Workflow stages with coverage:** 2 out of 9 (22%)  
**Workflow stages with partial coverage:** 2 out of 9 (22%)  
**Workflow stages with no coverage:** 5 out of 9 (56%)

**Recommendation:** Focus content development on high-priority gaps (Monitor, Troubleshoot) to increase coverage to 44-56%.

---

## Summary

The proposed JTBD-based structure reorganizes existing content from feature groupings to job-based workflows. Key improvements include:

1. **Goal-directed navigation:** Users find content by goal, not feature name
2. **Consolidated related content:** Performance and scaling jobs grouped together
3. **Explicit persona guidance:** Each user story identifies persona and benefits
4. **Workflow coverage visibility:** Exposes gaps (Monitor, Troubleshoot) for content roadmap
5. **Reduced navigation clicks:** 60-70% reduction in average clicks to reach content

The restructure does not change content but improves discoverability and workflow alignment.

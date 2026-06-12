# Managing OpenShift Pipelines Performance and Resource Use
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** Enable platform engineers, cluster administrators, and pipeline developers to optimize performance, control resource consumption, and protect critical workloads in OpenShift Pipelines environments.

**Personas:** Platform Engineer, Cluster Administrator, Pipeline Developer, SRE

**Main Jobs:** 6 core jobs across 5 workflow stages (Configure, Develop, Operate, Confirm, Execute)

---

## Quick Navigation

**I want to:**
- Optimize controller performance for high-volume pipeline environments -> Job 1 (Operate)
- Control resource usage in a multitenant cluster -> Job 2 (Configure)
- Override task resource requests without modifying shared definitions -> Job 3 (Configure)
- Set compute quotas for pipeline workloads -> Job 4 (Configure)
- Protect critical pipelines from eviction during maintenance -> Job 5 (Operate)
- Scale pipeline capacity across multiple clusters -> Job 6 (Operate)
- Enable high-availability mode for controllers -> Job 1.1 (Configure)
- Understand how step resources affect pod scheduling -> Job 2.1 (Develop)
- Use priority classes to control pipeline quotas -> Job 4.2 (Configure)
- Configure PodDisruptionBudget for critical workloads -> Job 5.2 (Configure)
- Set up multicluster hub-and-spoke architecture -> Job 6.2 (Configure)

---

# Table of Contents

## Operate & Manage

### Job 1: Optimize Pipeline Performance
*When running many concurrent pipelines, I want to optimize controller performance, so I can reduce failures and minimize execution delays*

**Personas:** Platform Engineer

**Timing:** Day 2 operation - monitor performance after installation to identify optimization needs

#### 1.1 Enable High-Availability Mode (The "HA" Setup)
**Goal:** Reduce TaskRun pod creation latency and minimize pipeline execution time.

- **Task:** Configure controller replicas in TektonConfig CR
  -> Lines 29-46: Improving OpenShift Pipelines performance
  - Set `spec.platforms.openshift.pipelinesAsCode.settings.ha.enabled: true`
  - Requires cluster-admin permissions

- **Validation:** Verify controller pods are running in HA mode
  ```bash
  oc get pods -n openshift-pipelines
  ```

#### 1.2 Scale Cluster Infrastructure (Horizontal Scaling)
**Goal:** Prevent resource exhaustion and pipeline failures on resource-constrained nodes.

- **Task:** Increase the number of cluster nodes
  -> Lines 34-37: Improving OpenShift Pipelines performance
  - Monitor cluster resource usage to identify contention
  - Add nodes to ensure adequate CPU and memory for pipeline workloads

---

## Set Up & Configure

### Job 2: Control Resource Consumption per Namespace
*When operating in a multitenant environment, I want to control resource consumption per namespace, so I can prevent any one application from consuming excessive resources*

**Personas:** Cluster Administrator

**Why:** Prevents resource exhaustion and ensures fair distribution across tenants in shared clusters

#### 2.1 Understand Resource Consumption Patterns (Knowledge Foundation)
**Goal:** Understand how step resource requests affect pod scheduling and quota enforcement.

- **For Pipeline Developers:** Learn resource aggregation behavior
  -> Lines 78-128: Understanding resource consumption in pipelines
  - Step requests are aggregated (not maxed) to determine pod request
  - LimitRange minimum CPU/memory affects every step
  - Formula: Pod request = sum(step requests) + init containers

- **Key Insight:** Tasks with many steps can exhaust quotas even if individual steps are small

#### 2.2 Optimize Task Design to Reduce Resource Requests (The "Efficient" Approach)
**Goal:** Minimize total resource requests through task restructuring.

- **Task:** Reduce step count in tasks
  -> Lines 134-177: Mitigating extra resource consumption in pipelines
  - Combine related commands into fewer steps
  - Distribute steps across multiple tasks to reduce per-pod aggregation

- **Task:** Configure explicit resource requests for steps
  - Set requests at minimum viable levels
  - Avoid relying on LimitRange defaults which multiply across steps

---

### Job 3: Override Step-Level Resources in PipelineRun
*When using referenced tasks from bundles or shared pipelines, I want to override step-level resources in the PipelineRun, so I can allocate more CPU or memory without modifying the original task definition*

**Personas:** Pipeline Developer

**Requires:**
- OpenShift Pipelines installed
- Permission to modify PipelineRun definitions
- Knowledge of which task steps need resource adjustment

#### 3.1 Set Compute Resources Using taskRunSpecs (Runtime Override)
**Goal:** Allocate adequate memory and CPU for specific steps experiencing failures.

- **Task:** Identify failing task step from execution logs
  -> Lines 216-293: Setting compute resources for a task step

- **Task:** Define taskRunSpecs in PipelineRun
  ```yaml
  spec:
    taskRunSpecs:
      - pipelineTaskName: <task-name>
        stepSpecs:
          - name: <step-name>
            computeResources:
              requests:
                memory: 2Gi
                cpu: 500m
              limits:
                memory: 4Gi
  ```

- **Validation:** Verify step completes successfully with increased resources

---

### Job 4: Set Compute Resource Quotas for Pipelines
*When managing pipeline workloads, I want to set compute resource quotas for pipelines rather than entire namespaces, so I can control resource consumption at the pipeline level*

**Personas:** Cluster Administrator

**Why:** Direct pipeline-level quotas are not currently supported - workarounds required

#### 4.1 Evaluate Alternative Approaches (Decision Point)
**Goal:** Choose the best workaround for pipeline-level quota control.

- **Context:** OpenShift Pipelines does not directly support pipeline-specific ResourceQuota
  -> Lines 306-318: Setting compute resource quota for OpenShift Pipelines

- **Decision:** Choose quota enforcement method

| Method | Best For | Complexity | Granularity |
|--------|----------|------------|-------------|
| Priority Class + ResourceQuota | Multiple pipeline tiers | Medium | Pipeline-level |
| Namespace-level ResourceQuota | Simple single-tenant | Low | Namespace-wide |
| LimitRange + step limits | Per-task control | Low | Task/step-level |

-> Lines 321-367: Alternative approaches for limiting compute resource consumption in OpenShift Pipelines

#### 4.2 Configure Priority Class for Pipeline-Level Quotas (The "Priority-Based" Approach)
**Goal:** Use PriorityClass and ResourceQuota together to achieve pipeline-level resource control.

- **Task:** Create PriorityClass for pipeline workloads
  -> Lines 383-617: Specifying pipelines resource quota using priority class
  ```yaml
  apiVersion: scheduling.k8s.io/v1
  kind: PriorityClass
  metadata:
    name: pipeline-priority
  value: 1000
  ```

- **Task:** Configure ResourceQuota scoped to priority
  ```yaml
  apiVersion: v1
  kind: ResourceQuota
  metadata:
    name: pipeline-quota
  spec:
    scopeSelector:
      matchExpressions:
        - operator: In
          scopeName: PriorityClass
          values: ["pipeline-priority"]
    hard:
      requests.cpu: "10"
      requests.memory: 20Gi
  ```

- **Task:** Set podTemplate.spec.priorityClassName in PipelineRun definitions

- **Validation:** Verify quota enforcement prevents over-allocation
  ```bash
  oc describe resourcequota pipeline-quota
  ```

---

## Operate & Manage

### Job 5: Protect Critical Workloads from Eviction
*When cluster maintenance operations occur, I want to protect critical pipeline workloads from eviction, so I can prevent disruption of non-reentrant tasks*

**Personas:** SRE

**Timing:** Configure BEFORE scheduling node drains or cluster upgrades

**Why:** Non-reentrant tasks like backups or deletions cannot safely restart mid-execution

#### 5.1 Understand Label Propagation Mechanism (Knowledge Foundation)
**Goal:** Understand how labels propagate from PipelineRun to TaskRun pods.

- **Concept:** Label propagation for eviction protection
  -> Lines 643-663: Eviction protection for TaskRun pods
  - Labels on PipelineRun propagate to TaskRun resources
  - TaskRun labels propagate to pod specs
  - PodDisruptionBudget can then target these pods via label selector

#### 5.2 Configure PodDisruptionBudget for Critical Tasks (The "Protected" Setup)
**Goal:** Block voluntary disruptions during execution of critical workloads.

- **Task:** Label PipelineRun with protection identifier
  -> Lines 665-749: Preventing eviction of TaskRun pods during node maintenance
  ```yaml
  metadata:
    labels:
      pipelines.openshift.io/pdb: protected
  ```

- **Task:** Create PodDisruptionBudget targeting labeled pods
  ```yaml
  apiVersion: policy/v1
  kind: PodDisruptionBudget
  metadata:
    name: protect-critical-pipelines
  spec:
    minAvailable: 1
    selector:
      matchLabels:
        pipelines.openshift.io/pdb: protected
  ```

- **Validation:** Verify PDB blocks node drain while protected tasks run
  ```bash
  oc get pdb protect-critical-pipelines
  ```

---

### Job 6: Distribute Workloads Across Multiple Clusters
*When running many concurrent tasks on a single cluster, I want to distribute pipeline workloads across multiple clusters, so I can overcome performance limitations and resource contention*

**Personas:** Platform Engineer

**Timing:** Technology Preview feature - evaluate stability requirements before production use

**Requires:**
- OpenShift Pipelines installed on all clusters
- Multiple OpenShift clusters available
- Kueue operator installed
- Cluster-admin permissions on hub and spoke clusters

**Why:** Single cluster Kubernetes API server can become a bottleneck at high pipeline volume

#### 6.1 Understand Multicluster Architecture (Knowledge Foundation)
**Goal:** Understand the hub-and-spoke architecture and benefits.

- **Concept:** Hub-and-spoke multicluster support
  -> Lines 783-810: About multicluster support in OpenShift Pipelines
  - Hub cluster: Manages pipeline definitions and scheduling
  - Spoke clusters: Execute pipeline runs
  - MultiKueue: Handles cross-cluster scheduling and status synchronization
  - Benefits: Horizontal scalability, reduced API server load, fault isolation

#### 6.2 Configure Hub Cluster for Multicluster (The "Hub" Setup)
**Goal:** Set up the hub cluster to manage and schedule pipeline runs centrally.

- **Task:** Install Kueue operator on hub cluster
  -> Lines 872-1171: Configuring the hub cluster for multicluster
  ```bash
  oc apply -f kueue-operator-subscription.yaml
  ```

- **Task:** Create RBAC resources for MultiKueue
  - Create ServiceAccount in `kueue-system` namespace
  - Create ClusterRole with cross-cluster permissions
  - Create ClusterRoleBinding

- **Task:** Create kubeconfig secrets for each spoke cluster
  ```bash
  oc create secret generic spoke-cluster-1-kubeconfig \
    --from-file=kubeconfig=./spoke1-kubeconfig \
    -n kueue-system
  ```

- **Task:** Configure MultiKueueCluster resources
  ```yaml
  apiVersion: kueue.x-k8s.io/v1alpha1
  kind: MultiKueueCluster
  metadata:
    name: spoke-cluster-1
  spec:
    kubeConfig:
      location: Secret
      secretRef:
        name: spoke-cluster-1-kubeconfig
        namespace: kueue-system
  ```

- **Task:** Create ClusterQueue and AdmissionCheck
  ```yaml
  apiVersion: kueue.x-k8s.io/v1beta1
  kind: ClusterQueue
  metadata:
    name: multicluster-queue
  spec:
    cohort: all-clusters
    queueingStrategy: BestEffortFIFO
    admissionChecks:
      - multicluster-check
  ```

#### 6.3 Configure Spoke Clusters for Execution (The "Spoke" Setup)
**Goal:** Enable spoke clusters to execute scheduled pipeline runs from the hub.

- **Task:** Install Kueue operator on each spoke cluster
  -> Lines 1173-1491: Configuring spoke clusters for multicluster

- **Task:** Create ServiceAccount and RBAC for hub access
  - Create ServiceAccount in `kueue-system` namespace
  - Create ClusterRole with resource management permissions
  - Create ClusterRoleBinding

- **Task:** Generate kubeconfig for hub cluster consumption
  ```bash
  oc --kubeconfig=./spoke-kubeconfig create token spoke-kueue-sa \
    --duration=8760h > spoke-token.txt
  ```

- **Task:** Create ResourceFlavor and ClusterQueue on spoke
  ```yaml
  apiVersion: kueue.x-k8s.io/v1beta1
  kind: ResourceFlavor
  metadata:
    name: default-flavor
  ---
  apiVersion: kueue.x-k8s.io/v1beta1
  kind: ClusterQueue
  metadata:
    name: cluster-queue
  spec:
    namespaceSelector: {}
    resourceGroups:
      - coveredResources: ["cpu", "memory"]
        flavors:
          - name: default-flavor
            resources:
              - name: cpu
                nominalQuota: 10
              - name: memory
                nominalQuota: 20Gi
  ```

#### 6.4 Verify Multicluster Setup (Confirmation Step)
**Goal:** Confirm the hub-to-spoke configuration is working correctly.

- **Task:** Check ClusterQueue status on hub
  -> Lines 1493-1595: Verifying multicluster setup
  ```bash
  oc get clusterqueue multicluster-queue -o yaml
  ```

- **Task:** Verify AdmissionCheck status
  ```bash
  oc get admissioncheck multicluster-check -o yaml
  ```

- **Task:** Check MultiKueueCluster connectivity
  ```bash
  oc get multikueuecluster -o yaml
  ```

- **Validation:** All resources show "Active" status, no connectivity errors

#### 6.5 Create Pipeline Runs in Multicluster Environment (Execution)
**Goal:** Create pipeline runs that are automatically scheduled across spoke clusters.

- **Task:** Create LocalQueue in namespace on hub cluster
  -> Lines 1597-1768: Creating pipeline runs in a multicluster environment
  ```yaml
  apiVersion: kueue.x-k8s.io/v1beta1
  kind: LocalQueue
  metadata:
    name: pipeline-queue
    namespace: pipelines-project
  spec:
    clusterQueue: multicluster-queue
  ```

- **Task:** Create PipelineRun with Kueue integration
  ```yaml
  apiVersion: tekton.dev/v1
  kind: PipelineRun
  metadata:
    name: example-pipeline-run
    namespace: pipelines-project
    labels:
      kueue.x-k8s.io/queue-name: pipeline-queue
  spec:
    pipelineRef:
      name: example-pipeline
    taskRunTemplate:
      podTemplate:
        metadata:
          labels:
            kueue.x-k8s.io/managed: "true"
  ```

- **Validation:** Pipeline run is scheduled to an available spoke cluster, status syncs to hub

---

## Appendices

### A. Resource Control Methods Comparison

| Method | Scope | Prerequisites | Best For |
|--------|-------|---------------|----------|
| High-availability mode | Controller performance | Cluster-admin access | High-volume environments |
| Namespace ResourceQuota | All pods in namespace | None | Simple quota enforcement |
| Priority Class + ResourceQuota | Pipeline workloads by priority | Kueue optional | Multi-tier pipeline environments |
| LimitRange | Per-container minimums | None | Basic resource floors |
| Step-level overrides | Individual task steps | None | Fixing resource failures |
| Multicluster distribution | Horizontal scaling | Multiple clusters, Kueue | Extreme scale, fault isolation |

### B. Eviction Protection Decision Guide

**When to use PodDisruptionBudget:**
- Non-reentrant tasks (backups, deletions, migrations)
- Long-running builds or deployments
- Tasks with external side effects

**When NOT to use PodDisruptionBudget:**
- Idempotent tasks that can safely restart
- Quick tasks (< 5 minutes)
- Development/test pipelines

### C. Workflow Coverage Analysis

| Stage | Coverage | Jobs | Notes |
|-------|----------|------|-------|
| Architecture | Partial | Job 6.1 | Multicluster architecture overview |
| Configure | ✅ | Jobs 2, 3, 4, 5.2, 6.2, 6.3 | Comprehensive configuration coverage |
| Develop | ✅ | Job 2.2 | Task design optimization |
| Operate | ✅ | Jobs 1, 5, 6 | Performance, protection, scaling |
| Confirm | ✅ | Job 6.4 | Multicluster setup verification |
| Execute | ✅ | Job 6.5 | Multicluster pipeline execution |

**Gaps Identified:**

| Stage | Gap | Recommendation |
|-------|-----|----------------|
| Monitor | No observability content | Add performance monitoring section |
| Troubleshoot | Limited troubleshooting | Add common failure scenarios and remediation |
| Upgrade | No upgrade procedures | Document impact of upgrades on running pipelines |

---

## Navigation Guide

### By User Journey

**Platform Engineer optimizing performance:**
1. Job 1: Optimize controller performance with HA mode
2. Job 6: Evaluate multicluster distribution for horizontal scaling
3. Job 6.2-6.5: Configure and verify multicluster setup

**Cluster Administrator managing multitenant resources:**
1. Job 2.1: Understand resource consumption patterns
2. Job 4: Set compute quotas using priority classes
3. Job 2.2: Guide developers on efficient task design

**Pipeline Developer fixing resource failures:**
1. Job 3: Override step-level resources in PipelineRun
2. Job 2.2: Optimize task structure to reduce aggregation

**SRE protecting critical workloads:**
1. Job 5.1: Understand label propagation mechanism
2. Job 5.2: Configure PodDisruptionBudget for protected tasks

**Platform Engineer scaling to multiple clusters:**
1. Job 6.1: Understand multicluster architecture
2. Job 6.2: Configure hub cluster with Kueue and MultiKueue
3. Job 6.3: Configure spoke clusters for execution
4. Job 6.4: Verify multicluster setup
5. Job 6.5: Create pipeline runs with multicluster scheduling

---

## Document Statistics

**Workflow Coverage:**
- Architecture: 1 job section
- Configure: 8 job sections
- Develop: 1 job section
- Operate: 4 job sections
- Confirm: 1 job section
- Execute: 1 job section

**Main Jobs:** 6
**User Stories/Paths:** 15 themed sections
**Source Sections:** 20 referenced
**Personas:** 4 (Platform Engineer, Cluster Administrator, Pipeline Developer, SRE)

**Technology Preview Features:** 1 (Multicluster support - Job 6)

---

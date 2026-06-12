# Multicluster Support for OpenShift Pipelines - TOC Comparison

**Current Feature-Based vs. Proposed JTBD-Based Structure**

**Analysis Date:** 2026-06-11  
**JTBD Records:** 32  
**Main Jobs:** 6 core jobs (rolled up from detailed user stories)  
**Workflow Coverage:** Plan → Onboard → Configure → Use → Troubleshoot (partial)

---

## Current Structure (Feature-Based)

```
Multicluster support for OpenShift Pipelines
├─ About multicluster support in OpenShift Pipelines (CONCEPT)
├─ Multicluster architecture (CONCEPT)
│  ├─ Hub cluster
│  ├─ Spoke clusters
│  └─ Kueue and MultiKueue
├─ Configuring the hub cluster for multicluster (PROCEDURE)
│  ├─ Install Red Hat Build of Kueue operator
│  ├─ Create RBAC resources
│  ├─ Create spoke cluster secrets
│  ├─ Create network policy
│  ├─ Create Kueue resources
│  ├─ Enable multicluster in TektonConfig
│  └─ Configure Tekton Results (optional)
├─ Configuring spoke clusters for multicluster (PROCEDURE)
│  ├─ Install Red Hat Build of Kueue operator
│  ├─ Create service account and RBAC
│  ├─ Create network policy
│  ├─ Create Kueue resources
│  ├─ Enable multicluster in TektonConfig
│  └─ Generate kubeconfig
├─ Verifying multicluster setup (PROCEDURE)
│  ├─ Check ClusterQueue status
│  ├─ Check AdmissionCheck status
│  ├─ Check MultiKueueCluster status
│  └─ Create test pipeline run (optional)
├─ Creating pipeline runs in a multicluster environment (PROCEDURE)
│  ├─ Basic pipeline run creation
│  ├─ Monitor pipeline run status
│  ├─ Using HTTP resolver
│  └─ Using Pipelines as Code
├─ Known limitations for multicluster pipeline runs (REFERENCE)
└─ Kueue resources for multicluster configuration (REFERENCE)
```

**Organization:** Feature/component-based (hub cluster, spoke cluster, resources)  
**Navigation:** 8 top-level sections (2 concepts, 4 procedures, 2 references)  
**User Journey:** Linear configuration flow (hub → spoke → verify → use)

---

## Proposed JTBD-Based Structure

### Plan Your Infrastructure

**Job 1: Scale Pipeline Infrastructure Horizontally**  
*When I experience resource contention from running many concurrent pipeline tasks*

**Personas:** Platform Administrator  
**Why:** Performance degrades due to API server and etcd bottlenecks on single cluster

**Evaluate Multicluster Approach**
- **Concept:** Understand horizontal scalability benefits
  → Lines 63-67: Abstract - Multicluster capability overview  
  Source: Assembly abstract describing distribution of workloads across clusters

**Desired Outcomes:**
- Minimize resource contention on API server and etcd
- Reduce impact of cluster failures
- Increase overall pipeline capacity

---

**Job 2: Understand How Multicluster Architecture Addresses Resource Bottlenecks**  
*When I plan to implement multicluster pipelines and need to decide if this approach fits my needs*

**Personas:** Platform Administrator, Cluster Administrator  
**Why:** Need to evaluate architectural options before committing to implementation

**Learn Core Concepts and Workflow**
- **Concept:** Multicluster benefits and operational workflow
  → Lines 90-116: About multicluster support in OpenShift Pipelines  
  Source: Concept module explaining key benefits and how pipeline runs flow through the system

**Desired Outcomes:**
- Minimize time to evaluate architectural options
- Reduce likelihood of choosing wrong scaling approach
- Ensure understanding of multicluster benefits and tradeoffs

**Understand Hub-and-Spoke Architecture Components**
- **Concept:** Hub cluster role and responsibilities
  → Lines 126-175: Multicluster architecture  
  Source: Concept module detailing hub cluster, spoke clusters, Kueue/MultiKueue components

  **Hub cluster:**
  - Central control plane for managing pipeline runs
  - Runs Kueue with MultiKueue enabled
  - Schedules pipeline runs based on resource availability
  - Does not execute workloads

- **Concept:** Spoke cluster role and responsibilities
  → Lines 126-175: Multicluster architecture  
  Source: Concept module - spoke cluster execution environment

  **Spoke cluster:**
  - Executes actual pipeline workloads
  - Reports status back to hub
  - Cleans up completed pipeline runs

- **Concept:** Kueue and MultiKueue scheduling mechanism
  → Lines 126-175: Multicluster architecture  
  Source: Concept module - workload scheduling explanation

**Desired Outcomes:**
- Minimize time to understand architectural roles
- Ensure correct component placement
- Reduce likelihood of misconfiguration

**Understand Current Limitations**
- **Reference:** Known limitations for multicluster pipeline runs
  → Lines 1083-1162: Known limitations for multicluster pipeline runs  
  Source: Reference module covering web console, API version, references, and tkn CLI limitations

**Key Limitations:**
- Cannot cancel pipeline runs from web console on hub (must use spoke cluster)
- Must use `tekton.dev/v1` API version (v1beta1 not supported)
- Cannot use Cluster resolver for pipelineRef or taskRef
- Limited tkn CLI functionality on hub cluster

**Desired Outcomes:**
- Minimize surprises during multicluster adoption
- Reduce time to plan workarounds for limitations
- Ensure awareness of unsupported use cases

---

### Set Up & Configure

**Job 3: Configure Hub Cluster to Manage and Schedule Pipeline Runs**  
*When I want to enable multicluster pipeline distribution and centralize orchestration*

**Personas:** Platform Administrator, Cluster Administrator

**Prerequisites:**
- OpenShift Pipelines Operator installed on hub cluster
- Cluster administrator permissions
- Kubeconfig files for spoke clusters (from Job 4.6)

**Timing:** BEFORE Job 4 - hub must be ready to accept spoke cluster registrations

**3.1 Install Red Hat Build of Kueue Operator**  
*Onboarding Step*

**Goal:** Enable workload scheduling capabilities on the hub cluster

- **Task:** Install RHBoK operator version 1.3 or later
  → Lines 198-238: Configuring the hub cluster for multicluster - Install RHBoK operator  
  Source: Procedure module step 1 - install cert-manager and Kueue operator

**Prerequisites:**
- Cluster administrator access to hub cluster

**Desired Outcomes:**
- Minimize installation time
- Ensure correct operator version installed
- Reduce likelihood of dependency issues

---

**3.2 Create RBAC Resources for Kueue**

**Goal:** Grant Kueue controller permissions to manage Tekton PipelineRuns

- **Task:** Create ClusterRole and ClusterRoleBinding for kueue-controller-manager
  → Lines 240-279: Configuring the hub cluster for multicluster - Create RBAC resources  
  Source: Procedure module step 2 - permissions for pipeline run management

**Prerequisites:**
- Red Hat Build of Kueue operator installed

**Desired Outcomes:**
- Ensure Kueue has minimal required permissions
- Reduce likelihood of permission denied errors
- Minimize time to troubleshoot RBAC issues

---

**3.3 Create Spoke Cluster Authentication Secrets**

**Goal:** Authenticate hub-to-spoke connections securely

- **Task:** Create secrets containing spoke cluster kubeconfig files in `openshift-kueue-operator` namespace
  → Lines 281-301: Configuring the hub cluster for multicluster - Create spoke cluster secrets  
  Source: Procedure module step 3 - creating secrets for each spoke cluster

**Prerequisites:**
- Obtain kubeconfig files from spoke cluster administrators (see Job 4.6)

**Desired Outcomes:**
- Minimize time to establish spoke connections
- Ensure secure credential storage
- Reduce likelihood of authentication failures

---

**3.4 Configure Hub Cluster Networking**

**Goal:** Enable cross-cluster communication from hub to spokes

- **Task:** Create NetworkPolicy allowing egress traffic from Kueue pods to spoke API servers
  → Lines 303-329: Configuring the hub cluster for multicluster - Create network policy  
  Source: Procedure module step 4 - network policy for external connectivity

**Prerequisites:**
- Red Hat Build of Kueue operator installed

**Desired Outcomes:**
- Ensure connectivity to all spoke clusters
- Minimize network-related scheduling failures
- Reduce time to diagnose connection issues

---

**3.5 Define Workload Scheduling Policies**

**Goal:** Control pipeline distribution policies through Kueue resource configuration

- **Task:** Create Kueue resources defining quotas and spoke cluster connections
  → Lines 331-425: Configuring the hub cluster for multicluster - Create Kueue resources  
  Source: Procedure module step 5 - ResourceFlavor, ClusterQueue, LocalQueue, AdmissionCheck, MultiKueueConfig, MultiKueueCluster

**Prerequisites:**
- Spoke cluster secrets created
- Red Hat Build of Kueue operator installed

**Key Resources:**
- **ResourceFlavor:** Defines available resource types (default-flavor)
- **ClusterQueue:** Manages quota allocation (CPU, memory, pipeline runs) and admission checks
- **LocalQueue:** Namespace-scoped queue for workload submission (pipelines-queue)
- **AdmissionCheck:** Enables MultiKueue scheduling (sample-multikueue)
- **MultiKueueConfig:** Lists spoke clusters available for scheduling
- **MultiKueueCluster:** Registers each spoke cluster with kubeconfig secret reference

**Reference:** Detailed Kueue resource schemas
  → Lines 1172-1309: Kueue resources for multicluster configuration  
  Source: Reference module with complete field descriptions for all Kueue custom resources

**Desired Outcomes:**
- Minimize configuration complexity for MultiKueue
- Ensure correct quota allocation across clusters
- Reduce likelihood of misconfigured cluster references

---

**3.6 Activate Multicluster Features in Tekton**

**Goal:** Enable pipeline scheduling across clusters

- **Task:** Patch TektonConfig to set hub cluster role
  → Lines 426-442: Configuring the hub cluster for multicluster - Enable multicluster in TektonConfig  
  Source: Procedure module step 6 - setting multi-cluster-role: Hub

**Configuration:**
```yaml
spec:
  scheduler:
    disabled: false
    multi-cluster-disabled: false
    multi-cluster-role: Hub
```

**Prerequisites:**
- OpenShift Pipelines Operator installed
- Kueue resources created

**Desired Outcomes:**
- Minimize time to enable multicluster mode
- Ensure scheduler correctly identifies hub role
- Reduce likelihood of role misconfiguration

---

**3.7 Configure Tekton Results for Multicluster (Optional)**

**Goal:** Prevent conflicts with spoke cluster pipeline executions when Tekton Results is enabled

- **Task:** Disable watcher and retention policy agent on hub cluster
  → Lines 444-471: Configuring the hub cluster for multicluster - Configure Tekton Results for multicluster  
  Source: Procedure module step 7 (optional) - disabling Results components

**When to use:** Only if Tekton Results is enabled on the hub cluster

**Desired Outcomes:**
- Eliminate pipeline run conflicts between hub and spoke
- Ensure correct result storage location
- Reduce likelihood of duplicate result entries

---

**Job 4: Configure Spoke Clusters to Receive and Run Pipeline Runs**  
*When I want to enable spoke clusters to execute workloads distributed from the hub*

**Personas:** Cluster Administrator

**Prerequisites:**
- OpenShift Pipelines Operator installed on spoke clusters
- Cluster administrator permissions on spoke clusters
- Hub cluster configured for multicluster (Job 3)

**4.1 Install Red Hat Build of Kueue Operator**  
*Onboarding Step*

**Goal:** Enable workload management capabilities on each spoke cluster

- **Task:** Install RHBoK operator version 1.3 or later on each spoke
  → Lines 500-540: Configuring spoke clusters - Install RHBoK operator  
  Source: Procedure module step 1 - install cert-manager and Kueue operator on spoke

**Prerequisites:**
- Cluster administrator access to spoke cluster

**Desired Outcomes:**
- Minimize installation time per spoke
- Ensure consistent operator version across spokes
- Reduce likelihood of version mismatch errors

---

**4.2 Implement Hub-to-Spoke Authentication**

**Goal:** Allow the hub to schedule workloads on this spoke securely

- **Task:** Create service account with pipeline execution permissions
  → Lines 542-643: Configuring spoke clusters - Create service account and RBAC  
  Source: Procedure module step 2 - creating multikueue-sa ServiceAccount and RBAC resources

**Prerequisites:**
- Red Hat Build of Kueue operator installed on spoke

**RBAC Resources Created:**
- **ServiceAccount:** multikueue-sa (hub uses this to authenticate)
- **ClusterRole:** Permissions for pipeline runs, task runs, pods, secrets, workloads
- **ClusterRoleBinding:** Binds role to service account

**Desired Outcomes:**
- Ensure minimal required permissions granted
- Reduce likelihood of permission denied errors
- Minimize security risk from excessive permissions

---

**4.3 Configure Spoke Cluster Networking**

**Goal:** Enable external communication for MultiKueue

- **Task:** Create NetworkPolicy allowing egress traffic from Kueue pods
  → Lines 645-671: Configuring spoke clusters - Create network policy  
  Source: Procedure module step 3 - network policy for egress

**Prerequisites:**
- Red Hat Build of Kueue operator installed on spoke

**Desired Outcomes:**
- Ensure Kueue can communicate with required external services
- Minimize network-related execution failures
- Reduce time to diagnose connectivity issues

---

**4.4 Define Spoke Resource Quotas**

**Goal:** Control pipeline execution capacity on this spoke

- **Task:** Create Kueue resources defining resource quotas for this spoke
  → Lines 673-715: Configuring spoke clusters - Create Kueue resources  
  Source: Procedure module step 4 - ResourceFlavor, ClusterQueue, LocalQueue for spoke

**Prerequisites:**
- Red Hat Build of Kueue operator installed on spoke

**Key Resources:**
- **ResourceFlavor:** default-flavor
- **ClusterQueue:** Defines CPU, memory, and pipeline run quotas for this spoke
- **LocalQueue:** pipelines-queue (referenced by hub when scheduling)

**Desired Outcomes:**
- Ensure spoke quota matches actual available resources
- Minimize resource overcommitment
- Reduce likelihood of OOM or resource exhaustion

---

**4.5 Activate Multicluster Features in Tekton**

**Goal:** Enable pipeline execution from hub

- **Task:** Patch TektonConfig to set spoke cluster role
  → Lines 717-733: Configuring spoke clusters - Enable multicluster in TektonConfig  
  Source: Procedure module step 5 - setting multi-cluster-role: Spoke

**Configuration:**
```yaml
spec:
  scheduler:
    disabled: false
    multi-cluster-disabled: false
    multi-cluster-role: Spoke
```

**Prerequisites:**
- OpenShift Pipelines Operator installed
- Kueue resources created on spoke

**Desired Outcomes:**
- Minimize time to enable multicluster mode on spoke
- Ensure scheduler correctly identifies spoke role
- Reduce likelihood of role misconfiguration

---

**4.6 Generate Kubeconfig for Hub Cluster Access**

**Goal:** Securely share spoke cluster access with hub administrators

- **Task:** Create token secret and generate kubeconfig file with service account credentials
  → Lines 735-791: Configuring spoke clusters - Generate kubeconfig  
  Source: Procedure module step 6 - creating long-lived token and generating kubeconfig

**Prerequisites:**
- Service account and RBAC resources created

**Output:** `spoke-cluster.kubeconfig` file to provide to hub administrator for Job 3.3

**Desired Outcomes:**
- Minimize time to generate kubeconfig
- Ensure long-lived token validity
- Reduce likelihood of credential expiration issues

---

### Deploy & Operate

**Job 5: Verify Hub and Spoke Connectivity and Readiness**  
*When I complete multicluster configuration and need to confirm the setup works correctly before production workloads*

**Personas:** Platform Administrator

**Prerequisites:**
- Hub cluster configured for multicluster (Job 3)
- Spoke clusters configured for multicluster (Job 4)

**Timing:** AFTER Jobs 3 and 4 - validates configuration before production use

**5.1 Check ClusterQueue Active Status**

**Goal:** Confirm workload admission is ready

- **Task:** Verify ClusterQueue status shows "Active: True"
  → Lines 819-830: Verifying multicluster setup - Check ClusterQueue status  
  Source: Procedure module step 1 - checking cluster-queue condition

**Command:**
```bash
oc get clusterqueues cluster-queue -o jsonpath="{range .status.conditions[?(@.type == 'Active')]}..."
```

**Expected Output:** `CQ - Active: True Reason: Ready Message: Can admit new workloads`

**Desired Outcomes:**
- Quickly identify if ClusterQueue is misconfigured
- Reduce time to troubleshoot admission issues
- Ensure workloads can be admitted

---

**5.2 Check AdmissionCheck Active Status**

**Goal:** Confirm the multicluster admission check is functioning

- **Task:** Verify AdmissionCheck status shows "Active: True"
  → Lines 832-843: Verifying multicluster setup - Check AdmissionCheck status  
  Source: Procedure module step 2 - checking sample-multikueue condition

**Command:**
```bash
oc get admissionchecks sample-multikueue -o jsonpath="{range .status.conditions[?(@.type == 'Active')]}..."
```

**Expected Output:** `AC - Active: True Reason: Active Message: The admission check is active`

**Desired Outcomes:**
- Quickly identify if AdmissionCheck is misconfigured
- Reduce time to troubleshoot scheduling issues
- Ensure MultiKueue admission is working

---

**5.3 Check Spoke Cluster Connectivity**

**Goal:** Confirm the hub can connect to all spokes

- **Task:** Verify MultiKueueCluster active status for each spoke
  → Lines 845-858: Verifying multicluster setup - Check MultiKueueCluster status  
  Source: Procedure module step 3 - checking each spoke cluster connection

**Prerequisites:**
- Hub cluster configured for multicluster
- Spoke clusters configured for multicluster
- Spoke cluster secrets created on hub

**Command:**
```bash
oc get multikueuecluster <spoke_cluster_name> -o jsonpath="{range .status.conditions[?(@.type == 'Active')]}..."
```

**Expected Output:** `MC - Active: True Reason: Active Message: Connected`

**Desired Outcomes:**
- Quickly identify spoke clusters with connection issues
- Reduce time to troubleshoot authentication failures
- Ensure all spokes are reachable from hub

---

**5.4 Validate End-to-End Functionality**  
*Confirmation Step*

**Goal:** Validate the complete multicluster workflow with a test pipeline run

- **Task:** Create test pipeline run that executes on a spoke cluster and monitor status
  → Lines 860-898: Verifying multicluster setup - Create test pipeline run  
  Source: Procedure module steps 4-5 - creating and monitoring test pipeline

**Prerequisites:**
- ClusterQueue status verified
- AdmissionCheck status verified
- MultiKueueCluster status verified

**Validation Steps:**
1. Create simple test pipeline run on hub with `kueue.x-k8s.io/queue-name` label
2. Monitor status with `oc get pipelineruns -w`
3. Verify transitions: Pending → Running → Succeeded

**Desired Outcomes:**
- Minimize time to confirm end-to-end functionality
- Reduce likelihood of discovering issues during production use
- Ensure pipeline runs transition through expected states

---

**Job 6: Create Pipeline Runs Automatically Scheduled to Spoke Clusters**  
*When I run pipelines in a multicluster setup and need to leverage distributed execution*

**Personas:** CI/CD Engineer

**Prerequisites:**
- Hub cluster configured for multicluster (Job 3)
- Spoke clusters configured for multicluster (Job 4)
- Multicluster setup verified (Job 5)

**6.1 Create Basic Multicluster Pipeline Runs**

**Goal:** Ensure MultiKueue schedules runs to appropriate spokes

- **Task:** Specify required labels and fields in PipelineRun manifest
  → Lines 922-974: Creating pipeline runs - Basic pipeline run creation  
  Source: Procedure module - basic example with embedded pipeline spec

**Required Configuration:**
- **Label:** `kueue.x-k8s.io/queue-name: pipelines-queue`
- **Field:** `spec.managedBy: kueue.x-k8s.io/multikueue` (added automatically by webhook if omitted)

**Prerequisites:**
- Namespace with LocalQueue resource exists
- Multicluster setup verified

**Desired Outcomes:**
- Minimize configuration errors in pipeline run manifests
- Ensure pipeline runs are recognized by MultiKueue
- Reduce likelihood of runs stuck in Pending state

---

**6.2 Monitor Pipeline Run Execution Status**

**Goal:** Observe state transitions and track execution progress

- **Task:** Monitor pipeline run status on the hub cluster
  → Lines 976-997: Creating pipeline runs - Monitor pipeline run status  
  Source: Procedure module - monitoring with oc get pipelineruns -w

**Command:**
```bash
oc get pipelineruns -w
```

**Expected States:**
1. **Pending:** Waiting for MultiKueue to schedule to spoke cluster
2. **Running:** Executing on spoke cluster
3. **Succeeded:** Completed successfully (or Failed)

**Note:** Web console shows multicluster icon next to pipeline run name

**Desired Outcomes:**
- Minimize time to identify stuck pipeline runs
- Ensure visibility into execution status
- Reduce need to check spoke clusters individually

---

**6.3 Use Remote Pipeline Definitions**

**Goal:** Centrally manage pipeline definitions and avoid duplication across clusters

- **Task:** Use HTTP resolver to reference pipelines from external locations
  → Lines 999-1022: Creating pipeline runs - Use HTTP resolver  
  Source: Procedure module - HTTP resolver example fetching from remote URL

**Context:** Cannot use Cluster resolver (pipelineRef/taskRef to cluster-stored resources). Must use embedded specs or remote resolvers (HTTP, Git, Bundle).

**Benefits:**
- Avoid cluster-stored pipeline references
- Centralize pipeline definition management
- Reduce maintenance overhead for updates

**Desired Outcomes:**
- Minimize duplication of pipeline definitions across clusters
- Ensure pipeline definitions are centrally managed
- Reduce maintenance overhead for pipeline updates

---

**6.4 Integrate Pipelines as Code with Multicluster**

**Goal:** Enable PAC-created pipeline runs to use multicluster scheduling

- **Task:** Ensure PAC pipeline runs include managedBy field
  → Lines 1024-1057: Creating pipeline runs - Use Pipelines as Code with multicluster  
  Source: Procedure module - PAC example with annotations and managedBy field

**Configuration:**
- PAC repository configuration must include `spec.managedBy: kueue.x-k8s.io/multikueue`

**Prerequisites:**
- Pipelines as Code configured on hub cluster
- Multicluster setup verified

**Note:** Secret synchronization handled automatically by syncer-service

**Desired Outcomes:**
- Minimize configuration changes to existing PAC setups
- Ensure PAC pipeline runs are scheduled to spoke clusters
- Reduce manual intervention for PAC workloads

---

**6.5 Cancel Multicluster Pipeline Runs**  
*Workaround for Hub Console Limitation*

**Goal:** Stop unwanted pipeline runs when hub console limitation prevents cancellation

- **Task:** Cancel pipeline run directly on the spoke cluster
  → Lines 1098-1121: Known limitations - Cancel multicluster pipeline runs  
  Source: Reference module - cancellation workaround procedure

**Why Needed:** Web console Stop and Cancel actions do not work for multicluster pipeline runs on hub

**Prerequisites:**
- Access to spoke cluster where pipeline is executing

**Procedure:**
1. Log in to the spoke cluster where pipeline run is executing
2. Patch pipeline run: `oc patch pipelinerun <name> -n <namespace> --type merge -p '{"spec":{"status":"Cancelled"}}'`
3. Cancellation status syncs back to hub cluster

**Note:** Cancelling from spoke cluster allows finally tasks to execute properly

**Desired Outcomes:**
- Minimize time to stop unwanted pipeline runs
- Ensure finally tasks execute properly
- Reduce wasted compute resources

---

## Key Differences

### Current Structure (Feature-Based)

**Organized By:** Technical components (hub cluster, spoke cluster, Kueue resources)  
**Navigation:** 8 top-level sections organized by implementation order  
**User Journey:** Linear configuration flow (concepts → hub → spoke → verify → use → reference)  
**Assumptions:** Users understand architectural distinctions before they start

### Proposed Structure (JTBD-Based)

**Organized By:** Job map stages (Plan → Onboard → Configure → Use)  
**Navigation:** 6 main jobs with nested user stories organized by workflow stage  
**User Journey:** Goal-directed with clear workflow phases (understand → set up → operate)  
**Focus:** User goals and outcomes at each stage

### Consolidation

**Current:** 8 separate top-level sections  
**Proposed:** 6 main jobs organized into 3 workflow phases  
**Reduction:** 25% fewer top-level items, with clearer progression through stages

---

## Hierarchy Levels Explanation

### Level 1: Main Jobs (6 total)

Stable, outcome-focused goals that remain constant regardless of implementation details:
- Job 1: Scale Pipeline Infrastructure Horizontally
- Job 2: Understand How Multicluster Architecture Addresses Resource Bottlenecks
- Job 3: Configure Hub Cluster to Manage and Schedule Pipeline Runs
- Job 4: Configure Spoke Clusters to Receive and Run Pipeline Runs
- Job 5: Verify Hub and Spoke Connectivity and Readiness
- Job 6: Create Pipeline Runs Automatically Scheduled to Spoke Clusters

### Level 2: User Stories (25 total)

Scenario-specific approaches and implementation paths nested under main jobs:
- Installation steps (3.1, 4.1)
- RBAC configuration (3.2, 4.2)
- Network configuration (3.4, 4.3)
- Resource quota setup (3.5, 4.4)
- Verification checks (5.1, 5.2, 5.3, 5.4)
- Pipeline run variations (6.1, 6.2, 6.3, 6.4, 6.5)

### Level 3: Procedures

Step-by-step instructions referenced with line numbers:
- Example: Lines 198-238 = Install RHBoK operator procedure
- Example: Lines 819-830 = Check ClusterQueue status command
- Example: Lines 922-974 = Create basic multicluster pipeline run

---

## Example: Content Consolidation

### Current (Component-Separated)

**Hub Cluster Configuration:**
- Section: Configuring the hub cluster for multicluster (lines 184-476)
  - 7 separate steps in single monolithic procedure

**Spoke Cluster Configuration:**
- Section: Configuring spoke clusters for multicluster (lines 486-796)
  - 6 separate steps in single monolithic procedure

**Connection between hub and spoke:**
- Hidden in step 3 of hub config (create secrets)
- Hidden in step 6 of spoke config (generate kubeconfig)

### Proposed (Goal-Consolidated)

**Job 3: Configure Hub Cluster** (lines 184-476)
- 7 discrete user stories (3.1 - 3.7)
- Clear prerequisite: "Obtain kubeconfig files from spoke cluster administrators (see Job 4.6)"
- Cross-reference to Job 4.6 for credential generation

**Job 4: Configure Spoke Clusters** (lines 486-796)
- 6 discrete user stories (4.1 - 4.6)
- Job 4.6 clearly produces output for Job 3.3

**Benefit:**
- **Current:** User must read entire procedure to find connection between hub and spoke
- **Proposed:** Cross-references make dependency explicit (Job 4.6 → Job 3.3)
- **Navigation:** Prerequisites clearly show workflow order (Job 4.6 BEFORE Job 3.3)

---

## Navigation Improvement Metrics

### Current Structure

**To find:** "How do I set up authentication between hub and spoke?"
1. Read hub cluster procedure
2. Find step 3 (create secrets)
3. Read note about obtaining kubeconfig
4. Navigate to spoke cluster procedure
5. Find step 6 (generate kubeconfig)
6. Connect the two manually

**Clicks to content:** 5-10 (scanning through procedures)

### Proposed Structure

**To find:** "How do I set up authentication between hub and spoke?"
1. Navigate to "Set Up & Configure"
2. See Job 3.3: "Create Spoke Cluster Authentication Secrets"
3. See prerequisite: "Obtain kubeconfig files (see Job 4.6)"
4. Click to Job 4.6: "Generate Kubeconfig for Hub Cluster Access"

**Clicks to content:** 2-3 (direct navigation with clear cross-reference)

### Metrics

**Current:** 8 top-level sections, monolithic procedures, manual connection of steps  
**Proposed:** 6 main jobs, 25 discrete user stories, explicit prerequisites  
**Reduction:** 25% fewer top-level items  
**Navigation Improvement:** 50-70% reduction in clicks to find related content  
**Cognitive Load:** Lower - clear workflow phases vs. component-based scanning

---

## Workflow Coverage Comparison

| Stage | Current | Proposed | Gap Status |
|-------|---------|----------|------------|
| **PLAN** | ⚠️ Scattered (2 concepts at top) | ✅ Jobs 1, 2 | **Improved** - Consolidated into dedicated "Plan Your Infrastructure" section |
| **ONBOARD** | ✅ Embedded in procedures | ✅ Jobs 3.1, 4.1 | **Reorganized** - Onboarding steps clearly marked as first steps in configuration jobs |
| **CONFIGURE** | ✅ Sections 3-4 (hub and spoke) | ✅ Jobs 3, 4 | **Reorganized** - Same content, better structure with discrete user stories |
| **USE** | ✅ Sections 5-6 (verify and create) | ✅ Jobs 5, 6 | **Consolidated** - Verification and execution clearly separated |
| **TROUBLESHOOT** | ⚠️ Partial (cancellation workaround only) | ⚠️ Job 6.5 (partial) | **Gap remains** - Only cancellation workaround, no comprehensive troubleshooting |

### Coverage Summary

**Current structure gaps:**
- PLAN: Concepts exist but not clearly marked as planning phase
- TROUBLESHOOT: Only cancellation workaround, no general troubleshooting

**Proposed structure gaps:**
- TROUBLESHOOT: Still limited to cancellation workaround

**Gaps addressed by restructure:**
- PLAN: Now clearly organized under "Plan Your Infrastructure" heading
- ONBOARD: Installation steps explicitly marked as onboarding
- CONFIGURE: Discrete user stories replace monolithic procedures

### Recommendations for Gap Closure

| Gap | Recommendation | Priority |
|-----|----------------|----------|
| **Comprehensive Troubleshooting** | Add troubleshooting section covering: authentication failures, quota exceeded errors, network connectivity issues, workload stuck in Pending, spoke cluster unreachable | High |
| **Monitoring & Observability** | Add monitoring section: ClusterQueue health metrics, spoke cluster capacity utilization, pipeline run distribution patterns, MultiKueue scheduling decisions | Medium |
| **Upgrade Procedures** | Add section for upgrading Kueue operators across hub and spokes while maintaining multicluster operation | Medium |
| **Migration Content** | Add section for migrating from single-cluster to multicluster setup | Low |
| **Disaster Recovery** | Add section for spoke cluster failure scenarios and recovery procedures | Low |

---

## Document Statistics

**Workflow Coverage:**
- PLAN: 2 jobs (Jobs 1, 2)
- ONBOARD: 2 operator installations (embedded in Jobs 3.1, 4.1)
- CONFIGURE: 2 jobs (Jobs 3, 4 for hub and spoke configuration)
- USE: 2 jobs (Jobs 5, 6 for verification and execution)
- TROUBLESHOOT: 1 partial user story (Job 6.5 - cancellation workaround only)

**Main Jobs:** 6 core jobs  
**User Stories:** 25 detailed user stories nested under main jobs  
**Source Sections Referenced:** 32 JTBD records mapping to original content  
**Hub/Spoke Configuration Paths:** Complete dual-path configuration clearly differentiated

**Content Mapping:**
- Planning content: Lines 63-175 (abstract, concepts, architecture, limitations)
- Hub configuration: Lines 184-476 (7 steps)
- Spoke configuration: Lines 486-796 (6 steps)
- Verification: Lines 806-899 (4 checks)
- Usage: Lines 909-1073 (4 usage patterns)
- Reference: Lines 1083-1309 (limitations and resource schemas)

---

## Success Criteria

✅ **User can immediately see main goals** - 6 clear main jobs organized by workflow phase  
✅ **User can find jobs by workflow stage** - Plan → Configure → Operate phases  
✅ **Simpler than current structure** - 25% reduction in top-level items  
✅ **Prerequisites clearly stated** - Permissions required, not persona gates  
✅ **Cross-references explicit** - Job 4.6 → Job 3.3 dependency visible  
✅ **Workflow coverage visible** - Gaps in TROUBLESHOOT clearly identified  
✅ **Natural progression** - Prerequisites order jobs correctly (Job 4.6 before Job 3.3)

---

## Appendix: Quick Reference Tables

### A. Main Jobs by Workflow Stage

| Workflow Stage | Main Jobs | User Stories |
|----------------|-----------|--------------|
| Plan Your Infrastructure | Jobs 1, 2 | 4 user stories (evaluate, understand concepts, understand architecture, understand limitations) |
| Set Up & Configure | Jobs 3, 4 | 13 user stories (hub config: 7, spoke config: 6) |
| Deploy & Operate | Jobs 5, 6 | 9 user stories (verification: 4, execution: 5) |

### B. Hub vs. Spoke Configuration Paths

| Configuration Aspect | Hub (Job 3) | Spoke (Job 4) |
|---------------------|-------------|---------------|
| Install Kueue | Job 3.1 (lines 198-238) | Job 4.1 (lines 500-540) |
| RBAC | Job 3.2 (lines 240-279) - permissions for Kueue controller | Job 4.2 (lines 542-643) - service account for hub authentication |
| Network Policy | Job 3.4 (lines 303-329) - egress to spoke API servers | Job 4.3 (lines 645-671) - egress for MultiKueue |
| Kueue Resources | Job 3.5 (lines 331-425) - includes MultiKueueConfig and MultiKueueCluster | Job 4.4 (lines 673-715) - local queues and quotas |
| TektonConfig Role | Job 3.6 (lines 426-442) - multi-cluster-role: Hub | Job 4.5 (lines 717-733) - multi-cluster-role: Spoke |
| Authentication | Job 3.3 (lines 281-301) - create secrets from kubeconfig | Job 4.6 (lines 735-791) - generate kubeconfig |

### C. Kueue Resources Quick Reference

| Resource | Scope | Hub | Spoke | Purpose |
|----------|-------|-----|-------|---------|
| ResourceFlavor | Cluster | ✅ | ✅ | Defines available resource types |
| ClusterQueue | Cluster | ✅ | ✅ | Manages quota allocation |
| LocalQueue | Namespace | ✅ | ✅ | Namespace-scoped queue for workload submission |
| AdmissionCheck | Cluster | ✅ | ❌ | Enables MultiKueue scheduling |
| MultiKueueConfig | Cluster | ✅ | ❌ | Lists spoke clusters |
| MultiKueueCluster | Cluster | ✅ | ❌ | Registers each spoke cluster |

Full reference: Lines 1172-1309

---

*End of Comparison*

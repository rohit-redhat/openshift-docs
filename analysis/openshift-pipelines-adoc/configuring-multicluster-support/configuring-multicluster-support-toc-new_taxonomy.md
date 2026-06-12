# Configuring Multicluster Support
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** Enable platform administrators and cluster administrators to distribute pipeline workloads across multiple OpenShift clusters to overcome resource contention and scale horizontally.

**Personas:** Platform Administrator, Cluster Administrator, CI/CD Engineer

**Main Jobs:** 6 core jobs across 4 workflow stages (Plan, Onboard, Configure, Use)

---

## Quick Navigation

**I want to:**
- Understand if multicluster is right for my needs -> Job 1 (Plan)
- Learn about hub-and-spoke architecture -> Job 2 (Plan)
- Configure the hub cluster -> Job 3 (Configure)
- Configure spoke clusters -> Job 4 (Configure)
- Verify my multicluster setup works -> Job 5 (Use)
- Create pipeline runs across clusters -> Job 6 (Use)
- Install Kueue operator on hub -> Job 3 (Onboard)
- Set up RBAC for multicluster -> Job 3.2 (Configure)
- Generate spoke kubeconfig files -> Job 4.6 (Configure)
- Check connectivity between hub and spokes -> Job 5.3 (Use)
- Cancel a multicluster pipeline run -> Job 6.5 (Use)
- Understand Kueue resource schemas -> Job 3 (Configure)

---

# Table of Contents

## Understand Your Options

### Job 1: Scale Pipeline Infrastructure Horizontally
*When I experience resource contention and need to handle increased capacity demands*

**Personas:** Platform Administrator

#### Evaluate Multicluster Approach

**Context:** Running many concurrent pipeline tasks can cause performance degradation due to API server and etcd bottlenecks. Multicluster architecture distributes workloads to overcome these limits.

**Benefits:**
- Minimize resource contention on API server and etcd
- Reduce impact of cluster failures
- Increase overall pipeline capacity

→ Lines 63-67: Abstract
  Source: Assembly abstract - multicluster capability overview

---

### Job 2: Understand How Multicluster Architecture Addresses Resource Bottlenecks
*When I plan to implement multicluster pipelines and need to evaluate if this approach fits my needs*

**Personas:** Platform Administrator, Cluster Administrator

**Why:** Understanding the architecture helps decide if multicluster is the right scaling approach for your environment.

#### Learn Core Concepts and Workflow

**Goal:** Understand benefits, tradeoffs, and operational workflow before committing to implementation.

- **Concept:** Multicluster benefits and workflow
  → Lines 90-116: About multicluster support in OpenShift Pipelines
    Source: Concept module explaining benefits and workflow

**Desired Outcomes:**
- Minimize time to evaluate architectural options
- Reduce likelihood of choosing wrong scaling approach
- Ensure understanding of multicluster benefits and tradeoffs

#### Understand Hub-and-Spoke Architecture Components

**Goal:** Properly design infrastructure by understanding component roles.

- **Concept:** Hub cluster role
  → Lines 126-175: Multicluster architecture
    Source: Concept module - hub cluster, spoke clusters, Kueue/MultiKueue components
  
  **Hub cluster responsibilities:**
  - Hosts Tekton Pipelines Operator and Kueue
  - Centralized pipeline definition storage
  - Schedules pipeline runs to spoke clusters
  
- **Concept:** Spoke cluster role
  → Lines 126-175: Multicluster architecture
    Source: Concept module - spoke cluster execution
  
  **Spoke cluster responsibilities:**
  - Execute pipeline runs
  - Report status back to hub
  - Manage local resource quotas

- **Concept:** Kueue and MultiKueue scheduling
  → Lines 126-175: Multicluster architecture
    Source: Concept module - workload scheduling

**Desired Outcomes:**
- Minimize time to understand architectural roles
- Ensure correct component placement
- Reduce likelihood of misconfiguration

#### Understand Current Limitations

**Goal:** Assess impact on workflows and plan workarounds before adoption.

- **Reference:** Known limitations for multicluster pipeline runs
  → Lines 1083-1162: Known limitations for multicluster pipeline runs
    Source: Reference module - web console, API version, references, tkn CLI limitations

**Key Limitations:**
- Cannot cancel pipeline runs from web console on hub (must use spoke cluster)
- Must use v1 API version for PipelineRuns
- Cannot use Cluster resolver for remote pipelines
- Limited tkn CLI operations on hub

**Desired Outcomes:**
- Minimize surprises during multicluster adoption
- Reduce time to plan workarounds for limitations
- Ensure awareness of unsupported use cases

---

## Set Up & Configure

### Job 3: Configure Hub Cluster to Manage and Schedule Pipeline Runs
*When I want to enable multicluster pipeline distribution and centralize orchestration*

**Personas:** Platform Administrator, Cluster Administrator

**Requires:**
- OpenShift Pipelines Operator installed on hub cluster
- Cluster-admin permissions
- Kubeconfig files for spoke clusters

**Timing:** BEFORE Job 4 (Configure Spoke Clusters) - hub must be ready to accept spoke registrations

#### 3.1 Install Red Hat Build of Kueue Operator (Onboarding Step)

**Goal:** Enable workload scheduling capabilities on the hub cluster.

- **Task:** Install RHBoK operator via OperatorHub or CLI
  → Lines 198-238: Configuring the hub cluster for multicluster - Install RHBoK operator
    Source: Procedure module step 1

**Prerequisites:**
- Cluster-admin access to hub cluster

**Desired Outcomes:**
- Minimize installation time
- Ensure correct operator version installed
- Reduce likelihood of dependency issues

#### 3.2 Create RBAC Resources for Kueue

**Goal:** Grant Kueue controller permissions to manage Tekton PipelineRuns.

- **Task:** Create ClusterRole and ClusterRoleBinding
  → Lines 240-279: Configuring the hub cluster for multicluster - Create RBAC resources
    Source: Procedure module step 2

**Prerequisites:**
- Red Hat Build of Kueue operator installed

**Desired Outcomes:**
- Ensure Kueue has minimal required permissions
- Reduce likelihood of permission denied errors
- Minimize time to troubleshoot RBAC issues

#### 3.3 Create Spoke Cluster Authentication Secrets

**Goal:** Authenticate hub-to-spoke connections securely.

- **Task:** Create secrets containing spoke kubeconfig files
  → Lines 281-301: Configuring the hub cluster for multicluster - Create spoke cluster secrets
    Source: Procedure module step 3

**Prerequisites:**
- Obtain kubeconfig files from spoke cluster administrators (see Job 4.6)

**Desired Outcomes:**
- Minimize time to establish spoke connections
- Ensure secure credential storage
- Reduce likelihood of authentication failures

#### 3.4 Configure Hub Cluster Networking

**Goal:** Enable cross-cluster communication from hub to spokes.

- **Task:** Create NetworkPolicy allowing egress traffic from Kueue pods to spoke API servers
  → Lines 303-329: Configuring the hub cluster for multicluster - Create network policy
    Source: Procedure module step 4

**Prerequisites:**
- Red Hat Build of Kueue operator installed

**Desired Outcomes:**
- Ensure connectivity to all spoke clusters
- Minimize network-related scheduling failures
- Reduce time to diagnose connection issues

#### 3.5 Define Workload Scheduling Policies

**Goal:** Control pipeline distribution policies through Kueue resource configuration.

- **Task:** Create Kueue resources (ResourceFlavor, ClusterQueue, LocalQueue, AdmissionCheck, MultiKueueConfig, MultiKueueCluster)
  → Lines 331-425: Configuring the hub cluster for multicluster - Create Kueue resources
    Source: Procedure module step 5

**Prerequisites:**
- Spoke cluster secrets created
- Red Hat Build of Kueue operator installed

**Key Resources:**
- **ResourceFlavor:** Defines available resource types
- **ClusterQueue:** Manages quota allocation across clusters
- **LocalQueue:** Namespace-scoped queue for workload submission
- **AdmissionCheck:** Enables MultiKueue scheduling
- **MultiKueueConfig:** Configures multicluster admission
- **MultiKueueCluster:** Registers each spoke cluster

**Reference:** Kueue resource schemas
  → Lines 1172-1309: Kueue resources for multicluster configuration
    Source: Reference module with field descriptions

**Desired Outcomes:**
- Minimize configuration complexity for MultiKueue
- Ensure correct quota allocation across clusters
- Reduce likelihood of misconfigured cluster references

#### 3.6 Activate Multicluster Features in Tekton

**Goal:** Enable pipeline scheduling across clusters.

- **Task:** Patch TektonConfig to set hub cluster role
  → Lines 426-442: Configuring the hub cluster for multicluster - Enable multicluster in TektonConfig
    Source: Procedure module step 6

**Configuration:**
```yaml
multi-cluster-role: Hub
```

**Prerequisites:**
- OpenShift Pipelines Operator installed
- Kueue resources created

**Desired Outcomes:**
- Minimize time to enable multicluster mode
- Ensure scheduler correctly identifies hub role
- Reduce likelihood of role misconfiguration

#### 3.7 Configure Tekton Results for Multicluster (Optional)

**Goal:** Prevent conflicts with spoke cluster pipeline executions when Tekton Results is enabled.

- **Task:** Disable watcher and retention agents on hub
  → Lines 444-471: Configuring the hub cluster for multicluster - Configure Tekton Results for multicluster
    Source: Procedure module step 7 (optional)

**When to use:** Only if Tekton Results is enabled on the hub cluster

**Desired Outcomes:**
- Eliminate pipeline run conflicts between hub and spoke
- Ensure correct result storage location
- Reduce likelihood of duplicate result entries

---

### Job 4: Configure Spoke Clusters to Receive and Run Pipeline Runs
*When I want to enable spoke clusters to execute workloads distributed from the hub*

**Personas:** Cluster Administrator

**Requires:**
- OpenShift Pipelines Operator installed on spoke clusters
- Cluster-admin permissions on spoke clusters
- Hub cluster configured for multicluster (Job 3)

#### 4.1 Install Red Hat Build of Kueue Operator (Onboarding Step)

**Goal:** Enable workload management capabilities on each spoke cluster.

- **Task:** Install RHBoK operator on each spoke via OperatorHub or CLI
  → Lines 500-540: Configuring spoke clusters - Install RHBoK operator
    Source: Procedure module step 1

**Prerequisites:**
- Cluster-admin access to spoke cluster

**Desired Outcomes:**
- Minimize installation time per spoke
- Ensure consistent operator version across spokes
- Reduce likelihood of version mismatch errors

#### 4.2 Implement Hub-to-Spoke Authentication

**Goal:** Allow the hub to schedule workloads on this spoke securely.

- **Task:** Create service account with pipeline execution permissions
  → Lines 542-643: Configuring spoke clusters - Create service account and RBAC
    Source: Procedure module step 2

**Prerequisites:**
- Red Hat Build of Kueue operator installed on spoke

**RBAC Resources Created:**
- ServiceAccount: `multikueue-sa`
- ClusterRole: Permissions for pipeline execution
- ClusterRoleBinding: Binds role to service account

**Desired Outcomes:**
- Ensure minimal required permissions granted
- Reduce likelihood of permission denied errors
- Minimize security risk from excessive permissions

#### 4.3 Configure Spoke Cluster Networking

**Goal:** Enable external communication for MultiKueue.

- **Task:** Create NetworkPolicy allowing egress traffic from Kueue pods
  → Lines 645-671: Configuring spoke clusters - Create network policy
    Source: Procedure module step 3

**Prerequisites:**
- Red Hat Build of Kueue operator installed on spoke

**Desired Outcomes:**
- Ensure Kueue can communicate with required external services
- Minimize network-related execution failures
- Reduce time to diagnose connectivity issues

#### 4.4 Define Spoke Resource Quotas

**Goal:** Control pipeline execution capacity on this spoke.

- **Task:** Create Kueue resources (ResourceFlavor, ClusterQueue, LocalQueue)
  → Lines 673-715: Configuring spoke clusters - Create Kueue resources
    Source: Procedure module step 4

**Prerequisites:**
- Red Hat Build of Kueue operator installed on spoke

**Desired Outcomes:**
- Ensure spoke quota matches actual available resources
- Minimize resource overcommitment
- Reduce likelihood of OOM or resource exhaustion

#### 4.5 Activate Multicluster Features in Tekton

**Goal:** Enable pipeline execution from hub.

- **Task:** Patch TektonConfig to set spoke cluster role
  → Lines 717-733: Configuring spoke clusters - Enable multicluster in TektonConfig
    Source: Procedure module step 5

**Configuration:**
```yaml
multi-cluster-role: Spoke
```

**Prerequisites:**
- OpenShift Pipelines Operator installed
- Kueue resources created on spoke

**Desired Outcomes:**
- Minimize time to enable multicluster mode on spoke
- Ensure scheduler correctly identifies spoke role
- Reduce likelihood of role misconfiguration

#### 4.6 Generate Kubeconfig for Hub Cluster Access

**Goal:** Securely share spoke cluster access with hub administrators.

- **Task:** Create token secret and generate kubeconfig file with service account credentials
  → Lines 735-791: Configuring spoke clusters - Generate kubeconfig
    Source: Procedure module step 6

**Prerequisites:**
- Service account and RBAC resources created

**Output:** Kubeconfig file to provide to hub administrator for Job 3.3

**Desired Outcomes:**
- Minimize time to generate kubeconfig
- Ensure long-lived token validity
- Reduce likelihood of credential expiration issues

---

## Deploy & Operate

### Job 5: Verify Hub and Spoke Connectivity and Readiness
*When I complete multicluster configuration and need to confirm the setup works correctly before production workloads*

**Personas:** Platform Administrator

**Requires:**
- Hub cluster configured for multicluster (Job 3)
- Spoke clusters configured for multicluster (Job 4)

**Timing:** AFTER Jobs 3 and 4 - validates configuration before production use

#### 5.1 Check ClusterQueue Active Status

**Goal:** Confirm workload admission is ready.

- **Task:** Verify ClusterQueue status
  → Lines 819-830: Verifying multicluster setup - Check ClusterQueue status
    Source: Procedure module step 1

**Command:**
```bash
oc get clusterqueue -n <namespace>
```

**Expected:** Status shows "Active"

**Desired Outcomes:**
- Quickly identify if ClusterQueue is misconfigured
- Reduce time to troubleshoot admission issues
- Ensure workloads can be admitted

#### 5.2 Check AdmissionCheck Active Status

**Goal:** Confirm the multicluster admission check is functioning.

- **Task:** Verify AdmissionCheck status
  → Lines 832-843: Verifying multicluster setup - Check AdmissionCheck status
    Source: Procedure module step 2

**Command:**
```bash
oc get admissioncheck -n <namespace>
```

**Expected:** Status shows "Active"

**Desired Outcomes:**
- Quickly identify if AdmissionCheck is misconfigured
- Reduce time to troubleshoot scheduling issues
- Ensure MultiKueue admission is working

#### 5.3 Check Spoke Cluster Connectivity

**Goal:** Confirm the hub can connect to all spokes.

- **Task:** Verify MultiKueueCluster active status for each spoke
  → Lines 845-858: Verifying multicluster setup - Check MultiKueueCluster status
    Source: Procedure module step 3

**Command:**
```bash
oc get multikueuecluster -n <namespace>
```

**Expected:** Each spoke shows "Active" status

**Prerequisites:**
- Hub cluster configured for multicluster
- Spoke clusters configured for multicluster
- Spoke cluster secrets created on hub

**Desired Outcomes:**
- Quickly identify spoke clusters with connection issues
- Reduce time to troubleshoot authentication failures
- Ensure all spokes are reachable from hub

#### 5.4 Validate End-to-End Functionality (Confirmation Step)

**Goal:** Validate the complete multicluster workflow with a test pipeline run.

- **Task:** Create test pipeline run that executes on a spoke cluster
  → Lines 860-898: Verifying multicluster setup - Create test pipeline run
    Source: Procedure module steps 4-5

**Prerequisites:**
- ClusterQueue status verified
- AdmissionCheck status verified
- MultiKueueCluster status verified

**Validation Steps:**
1. Create simple test pipeline run on hub
2. Monitor status transitions: Pending → Running → Succeeded
3. Verify execution occurred on spoke cluster

**Desired Outcomes:**
- Minimize time to confirm end-to-end functionality
- Reduce likelihood of discovering issues during production use
- Ensure pipeline runs transition through expected states

---

### Job 6: Create Pipeline Runs Automatically Scheduled to Spoke Clusters
*When I run pipelines in a multicluster setup and need to leverage distributed execution*

**Personas:** CI/CD Engineer

**Requires:**
- Hub cluster configured for multicluster (Job 3)
- Spoke clusters configured for multicluster (Job 4)
- Multicluster setup verified (Job 5)

#### 6.1 Create Basic Multicluster Pipeline Runs

**Goal:** Ensure MultiKueue schedules runs to appropriate spokes.

- **Task:** Specify required labels and fields in PipelineRun manifest
  → Lines 922-974: Creating pipeline runs - Basic pipeline run creation
    Source: Procedure module - basic example

**Required Configuration:**
- **Label:** `kueue.x-k8s.io/queue-name: <queue-name>`
- **Field:** `spec.managedBy: tekton-pipelines/multicluster`

**Prerequisites:**
- Namespace with LocalQueue resource
- Multicluster setup verified

**Desired Outcomes:**
- Minimize configuration errors in pipeline run manifests
- Ensure pipeline runs are recognized by MultiKueue
- Reduce likelihood of runs stuck in Pending state

#### 6.2 Monitor Pipeline Run Execution Status

**Goal:** Observe state transitions and track execution progress.

- **Task:** Monitor pipeline run status on the hub cluster
  → Lines 976-997: Creating pipeline runs - Monitor pipeline run status
    Source: Procedure module - monitoring

**Command:**
```bash
oc get pipelineruns -w
```

**Expected States:**
1. Pending (queued for scheduling)
2. Running (executing on spoke)
3. Succeeded (completed)

**Desired Outcomes:**
- Minimize time to identify stuck pipeline runs
- Ensure visibility into execution status
- Reduce need to check spoke clusters individually

#### 6.3 Use Remote Pipeline Definitions

**Goal:** Centrally manage pipeline definitions and avoid duplication across clusters.

- **Task:** Use HTTP resolver to reference pipelines from external locations
  → Lines 999-1022: Creating pipeline runs - Use HTTP resolver
    Source: Procedure module - HTTP resolver example

**Benefits:**
- Avoid cluster-stored pipeline references
- Centralize pipeline definition management
- Reduce maintenance overhead for updates

**Desired Outcomes:**
- Minimize duplication of pipeline definitions across clusters
- Ensure pipeline definitions are centrally managed
- Reduce maintenance overhead for pipeline updates

#### 6.4 Integrate Pipelines as Code with Multicluster

**Goal:** Enable PAC-created pipeline runs to use multicluster scheduling.

- **Task:** Ensure PAC pipeline runs include managedBy field
  → Lines 1024-1057: Creating pipeline runs - Use Pipelines as Code with multicluster
    Source: Procedure module - PAC example

**Configuration:**
- PAC must add `spec.managedBy: tekton-pipelines/multicluster` to generated PipelineRuns

**Prerequisites:**
- Pipelines as Code configured on hub cluster
- Multicluster setup verified

**Desired Outcomes:**
- Minimize configuration changes to existing PAC setups
- Ensure PAC pipeline runs are scheduled to spoke clusters
- Reduce manual intervention for PAC workloads

#### 6.5 Cancel Multicluster Pipeline Runs (Workaround)

**Goal:** Stop unwanted pipeline runs when hub console limitation prevents cancellation.

- **Task:** Cancel pipeline run directly on the spoke cluster
  → Lines 1098-1121: Known limitations - Cancel multicluster pipeline runs
    Source: Reference module - cancellation workaround

**Why needed:** Web console on hub does not support canceling multicluster pipeline runs

**Prerequisites:**
- Access to spoke cluster where pipeline is executing

**Desired Outcomes:**
- Minimize time to stop unwanted pipeline runs
- Ensure finally tasks execute properly
- Reduce wasted compute resources

---

## Appendices

### A. Kueue Resources Quick Reference

| Resource | Purpose | Scope |
|----------|---------|-------|
| ResourceFlavor | Defines available resource types | Cluster-wide |
| ClusterQueue | Manages quota allocation across clusters | Cluster-wide |
| LocalQueue | Namespace-scoped queue for workload submission | Namespace |
| AdmissionCheck | Enables MultiKueue scheduling | Cluster-wide |
| MultiKueueConfig | Configures multicluster admission | Cluster-wide |
| MultiKueueCluster | Registers each spoke cluster | Cluster-wide |

**Full Reference:**
→ Lines 1172-1309: Kueue resources for multicluster configuration
  Source: Reference module with detailed field descriptions

---

### B. Multicluster Setup Decision Guide

| Setup Type | Hub Cluster | Spoke Clusters | Best For |
|------------|-------------|----------------|----------|
| Development/Testing | Single hub, 1-2 spokes | Minimal resources | Evaluation, testing |
| Production Small | Single hub, 3-5 spokes | Standard production resources | Small-scale production |
| Production Large | Single hub, 6+ spokes | High-capacity clusters | Enterprise scale |
| High Availability | Hub with HA config, 10+ spokes | Distributed across regions | Mission-critical workloads |

**Choose based on:**
- **Development/Testing:** Learning multicluster, proof-of-concept
- **Production Small:** Standard production workloads with moderate scale
- **Production Large:** High-volume CI/CD pipelines across many teams
- **High Availability:** Geographic distribution, disaster recovery requirements

---

### C. Workflow Coverage Analysis

| Stage | Coverage | Jobs | Notes |
|-------|----------|------|-------|
| PLAN | ✅ | Jobs 1, 2 | Architecture understanding, limitations |
| ONBOARD | ✅ | Jobs 3.1, 4.1 | Operator installation on hub and spokes |
| CONFIGURE | ✅ | Jobs 3, 4 | Complete hub and spoke configuration |
| USE | ✅ | Jobs 5, 6 | Verification and pipeline run creation |
| TROUBLESHOOT | ⚠️ Limited | Job 6.5 (partial) | Only cancellation workaround, no comprehensive troubleshooting |

### Gaps Identified

| Stage | Gap | Recommendation |
|-------|-----|----------------|
| TROUBLESHOOT | No comprehensive troubleshooting | Add troubleshooting section for common errors (authentication failures, quota issues, network connectivity) |
| MONITOR | No observability guidance | Add monitoring section for cluster health, queue metrics, workload distribution |
| UPGRADE | No upgrade procedures | Add section for upgrading Kueue operators across hub and spokes |
| MIGRATE | No migration content | Consider adding section for migrating from single-cluster to multicluster |

---

## Navigation Guide

### By User Journey

**Platform Administrator deploying multicluster for the first time:**
1. Job 1: Understand if multicluster solves your scaling needs
2. Job 2: Learn hub-and-spoke architecture and limitations
3. Job 3: Configure hub cluster for multicluster
4. Job 4: Configure spoke clusters to receive workloads
5. Job 5: Verify connectivity and run test pipeline
6. Job 6: Create production pipeline runs

**Cluster Administrator adding new spoke to existing multicluster:**
1. Job 4: Configure new spoke cluster
2. Job 3.3: Create spoke cluster secret on hub
3. Job 3.5: Update MultiKueueCluster resource on hub
4. Job 5.3: Verify new spoke connectivity

**CI/CD Engineer using existing multicluster infrastructure:**
1. Job 6.1: Create pipeline runs with correct labels
2. Job 6.2: Monitor pipeline run status
3. Job 6.3: Use HTTP resolver for remote pipelines (optional)
4. Job 6.4: Integrate Pipelines as Code (optional)

---

## Document Statistics

**Workflow Coverage:**
- PLAN: 2 jobs
- ONBOARD: 2 operator installations (within Jobs 3, 4)
- CONFIGURE: 2 jobs (hub and spoke configuration)
- USE: 2 jobs (verification and execution)
- TROUBLESHOOT: 1 partial (cancellation workaround only)

**Main Jobs:** 6
**User Stories/Approaches:** 25 detailed user stories
**Source Sections:** 31 JTBD records referenced
**Spoke/Hub Variations:** Complete dual-path configuration

---

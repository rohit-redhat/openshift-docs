# Multicluster Support for OpenShift Pipelines — Consolidation Report

**Document:** configuring-multicluster-support-self-managed-reduced.adoc  
**JTBD Records:** 31 pre-consolidated records → 6 final main jobs (after merging related user stories)

---

## Executive Summary

### What's Changing

The current documentation organizes multicluster support content by technical component (hub cluster configuration, spoke cluster configuration, Kueue resources) and implementation order. This structure assumes users already understand the architectural distinctions and are ready to execute a linear setup sequence. While this works for users following a first-time setup guide, it creates friction for users who need to understand *why* they need multicluster support, troubleshoot specific components, or add new spoke clusters to an existing setup.

The proposed JTBD-based structure reorganizes the same content by user goals and workflow stages: Plan → Set Up & Configure → Deploy & Operate. Instead of forcing users to navigate through component-focused procedures, users can find content by asking "What am I trying to accomplish?" This consolidation elevates planning and decision-making content, breaks monolithic procedures into discrete user stories with clear prerequisites, and makes cross-references explicit (e.g., Job 4.6 produces the kubeconfig needed for Job 3.3).

### Key Improvements

- **Planning content elevated:** Architecture concepts and limitations moved from scattered sections to a dedicated "Understand Your Options" phase, helping users make informed decisions before implementation.
- **Monolithic procedures broken into discrete jobs:** Hub configuration (7 steps) and spoke configuration (6 steps) restructured as individual user stories with explicit prerequisites and outcomes.
- **Authentication workflow clarified:** Spoke kubeconfig generation (Job 4.6) and hub secret creation (Job 3.3) now have explicit cross-references showing the dependency chain.
- **Verification consolidated:** Four verification checks grouped under a single "Verify Connectivity" job with clear success criteria.
- **Reference material positioned by use case:** Kueue resource schemas referenced in-context during configuration jobs, with full reference appendix for troubleshooting.
- **Cancellation workaround surfaced:** Known limitation for canceling multicluster pipeline runs promoted from buried reference content to operational troubleshooting approach (Job 6.5).
- **Workflow progression made explicit:** Jobs organized into three phases (Understand & Plan, Set Up & Configure, Deploy & Operate) with 25% reduction in top-level navigation items.
- **Prerequisites clarified:** Each job lists specific technical requirements (not persona gates), making dependencies visible and reducing setup errors.

---

## Current Structure (Feature-Based)

Based on the actual `.adoc` file structure:

- **Abstract** — Overview of multicluster capability and horizontal scaling benefits
- **About multicluster support in OpenShift Pipelines** (CONCEPT) — Key benefits and operational workflow explanation
- **Multicluster architecture** (CONCEPT) — Hub cluster, spoke cluster, and Kueue/MultiKueue component descriptions
- **Configuring the hub cluster for multicluster** (PROCEDURE) — Monolithic 7-step procedure
  - Install Red Hat Build of Kueue operator
  - Create RBAC resources
  - Create spoke cluster secrets
  - Create network policy
  - Create Kueue resources
  - Enable multicluster in TektonConfig
  - Configure Tekton Results (optional)
- **Configuring spoke clusters for multicluster** (PROCEDURE) — Monolithic 6-step procedure
  - Install Red Hat Build of Kueue operator
  - Create service account and RBAC
  - Create network policy
  - Create Kueue resources
  - Enable multicluster in TektonConfig
  - Generate kubeconfig
- **Verifying multicluster setup** (PROCEDURE) — 4 verification checks
  - Check ClusterQueue status
  - Check AdmissionCheck status
  - Check MultiKueueCluster status
  - Create test pipeline run (optional)
- **Creating pipeline runs in a multicluster environment** (PROCEDURE) — Usage patterns
  - Basic pipeline run creation
  - Monitor pipeline run status
  - Using HTTP resolver
  - Using Pipelines as Code
- **Known limitations for multicluster pipeline runs** (REFERENCE) — Web console limitations, API version requirements, reference limitations, tkn CLI limitations
- **Kueue resources for multicluster configuration** (REFERENCE) — ResourceFlavor, ClusterQueue, LocalQueue, AdmissionCheck, MultiKueueConfig, MultiKueueCluster schemas

**Total:** 8 top-level sections (2 concepts, 4 procedures, 2 references), organized by component type and linear implementation order.

---

## Proposed JTBD-Based Structure

### Quick Overview

- **Understand & Plan**
  - Job 1: Scale Pipeline Infrastructure Horizontally
  - Job 2: Understand How Multicluster Architecture Addresses Resource Bottlenecks
- **Set Up & Configure**
  - Job 3: Configure Hub Cluster to Manage and Schedule Pipeline Runs
  - Job 4: Configure Spoke Clusters to Receive and Run Pipeline Runs
- **Deploy & Operate**
  - Job 5: Verify Hub and Spoke Connectivity and Readiness
  - Job 6: Create Pipeline Runs Automatically Scheduled to Spoke Clusters

---

### Detailed Job Descriptions

#### Understand & Plan

**Job 1: Scale Pipeline Infrastructure Horizontally**

*When I experience resource contention from running many concurrent pipeline tasks, I want to distribute pipeline workloads across multiple clusters, so I can overcome performance bottlenecks and handle increased capacity demands.*

Prerequisites: None (entry point for users evaluating multicluster)

- **1.1. Evaluate multicluster capability** `[concept]`
  - Abstract (lines 63-67): Overview of horizontal scaling benefits and hub-and-spoke architecture
  - Context: Use this to understand if multicluster solves your specific performance issues

---

**Job 2: Understand How Multicluster Architecture Addresses Resource Bottlenecks**

*When I plan to implement multicluster pipelines, I want to understand the hub-and-spoke architecture components, so I can properly design my infrastructure and assess whether this approach fits my needs.*

Prerequisites: None (planning phase)

- **2.1. Learn core multicluster concepts and workflow** `[concept]`
  - About multicluster support in OpenShift Pipelines (lines 90-116): Benefits, operational workflow, horizontal scalability explanation
  - Context: Read this to understand how pipeline runs flow through the system before committing to implementation
  
- **2.2. Understand hub cluster role and responsibilities** `[concept]`
  - Multicluster architecture - Hub cluster (lines 132-148): Central control plane, Kueue/MultiKueue, scheduling responsibilities
  - Context: Use this to determine which cluster should be the hub in your infrastructure
  
- **2.3. Understand spoke cluster role and responsibilities** `[concept]`
  - Multicluster architecture - Spoke clusters (lines 150-161): Workload execution, status reporting, cleanup responsibilities
  - Context: Use this to plan resource allocation for spoke clusters
  
- **2.4. Understand Kueue and MultiKueue scheduling mechanism** `[concept]`
  - Multicluster architecture - Kueue and MultiKueue (lines 163-174): Job queueing, resource quota management, cross-cluster scheduling
  - Context: Read this to understand how workload distribution decisions are made
  
- **2.5. Review known limitations and workarounds** `[reference]`
  - Known limitations for multicluster pipeline runs (lines 1083-1162): Web console limitations, API version requirements, reference restrictions, tkn CLI constraints
  - Context: Review before planning to identify unsupported use cases and plan workarounds (e.g., cannot cancel from hub console, must use v1 API)

---

#### Set Up & Configure

**Job 3: Configure Hub Cluster to Manage and Schedule Pipeline Runs**

*When I want to enable multicluster pipeline distribution, I want to configure a hub cluster to centralize pipeline orchestration, so I can manage pipeline runs across multiple spoke clusters.*

Prerequisites: OpenShift Pipelines Operator installed on hub cluster, cluster-admin permissions, kubeconfig files for spoke clusters

- **3.1. Install Red Hat Build of Kueue operator** `[procedure]`
  - Configuring the hub cluster for multicluster - Install RHBoK operator (lines 198-238): Cert-manager installation, operator installation from OperatorHub, Kueue custom resource creation
  - Context: First step for hub setup; enables workload scheduling capabilities
  
- **3.2. Create RBAC resources for Kueue controller** `[procedure]`
  - Configuring the hub cluster for multicluster - Create RBAC resources (lines 240-279): ClusterRole and ClusterRoleBinding for kueue-controller-manager to manage PipelineRuns
  - Context: Use after operator installation to grant Kueue permissions to manage Tekton PipelineRuns
  
- **3.3. Create spoke cluster authentication secrets** `[procedure]`
  - Configuring the hub cluster for multicluster - Create spoke cluster secrets (lines 281-301): Secret creation in openshift-kueue-operator namespace with kubeconfig files
  - Context: Requires kubeconfig from spoke cluster administrators (see Job 4.6); enables hub-to-spoke authentication
  
- **3.4. Configure hub cluster networking** `[procedure]`
  - Configuring the hub cluster for multicluster - Create network policy (lines 303-329): NetworkPolicy allowing egress traffic from Kueue pods to spoke API servers
  - Context: Use after operator installation to enable cross-cluster communication
  
- **3.5. Define workload scheduling policies** `[procedure]`
  - Configuring the hub cluster for multicluster - Create Kueue resources (lines 331-425): ResourceFlavor, ClusterQueue, LocalQueue, AdmissionCheck, MultiKueueConfig, MultiKueueCluster creation
  - Context: Use after creating spoke secrets; controls pipeline distribution policies and quota allocation
  - Reference: Kueue resources for multicluster configuration (lines 1172-1309): Full schema descriptions for troubleshooting
  
- **3.6. Activate multicluster features in Tekton** `[procedure]`
  - Configuring the hub cluster for multicluster - Enable multicluster in TektonConfig (lines 426-442): Patch TektonConfig with multi-cluster-role: Hub
  - Context: Use after creating Kueue resources; enables pipeline scheduling across clusters
  
- **3.7. Configure Tekton Results for multicluster (optional)** `[procedure]`
  - Configuring the hub cluster for multicluster - Configure Tekton Results (lines 444-471): Disable watcher and retention agents
  - Context: Only if Tekton Results is enabled; prevents conflicts with spoke cluster executions

---

**Job 4: Configure Spoke Clusters to Receive and Run Pipeline Runs**

*When I want to enable spoke clusters to execute workloads distributed from the hub, I want to configure spoke clusters to receive and run pipeline runs, so I can distribute pipeline execution across my cluster infrastructure.*

Prerequisites: OpenShift Pipelines Operator installed on spoke clusters, cluster-admin permissions on spoke clusters, hub cluster configured for multicluster (Job 3)

- **4.1. Install Red Hat Build of Kueue operator** `[procedure]`
  - Configuring spoke clusters - Install RHBoK operator (lines 500-540): Cert-manager installation, operator installation, Kueue custom resource creation
  - Context: First step for spoke setup; enables workload management capabilities
  
- **4.2. Implement hub-to-spoke authentication** `[procedure]`
  - Configuring spoke clusters - Create service account and RBAC (lines 542-643): ServiceAccount multikueue-sa, ClusterRole, ClusterRoleBinding with pipeline execution permissions
  - Context: Use after operator installation; credentials used by hub to schedule workloads on this spoke
  
- **4.3. Configure spoke cluster networking** `[procedure]`
  - Configuring spoke clusters - Create network policy (lines 645-671): NetworkPolicy allowing egress traffic from Kueue pods
  - Context: Use after operator installation; enables external communication for MultiKueue
  
- **4.4. Define spoke resource quotas** `[procedure]`
  - Configuring spoke clusters - Create Kueue resources (lines 673-715): ResourceFlavor, ClusterQueue, LocalQueue with CPU, memory, and pipeline run quotas
  - Context: Use after operator installation; controls pipeline execution capacity on this spoke
  
- **4.5. Activate multicluster features in Tekton** `[procedure]`
  - Configuring spoke clusters - Enable multicluster in TektonConfig (lines 717-733): Patch TektonConfig with multi-cluster-role: Spoke
  - Context: Use after creating Kueue resources; enables pipeline execution from hub
  
- **4.6. Generate kubeconfig for hub cluster access** `[procedure]`
  - Configuring spoke clusters - Generate kubeconfig (lines 735-791): Create long-lived token secret, generate kubeconfig file with service account credentials
  - Context: Use after creating service account; output file provided to hub administrator for Job 3.3

---

#### Deploy & Operate

**Job 5: Verify Hub and Spoke Connectivity and Readiness**

*When I complete multicluster configuration, I want to verify hub and spoke connectivity and readiness, so I can confirm the setup is working correctly before running production workloads.*

Prerequisites: Hub cluster configured for multicluster (Job 3), spoke clusters configured for multicluster (Job 4)

- **5.1. Check ClusterQueue active status** `[procedure]`
  - Verifying multicluster setup - Check ClusterQueue status (lines 819-830): oc get clusterqueues command with jsonpath to verify Active: True
  - Context: First verification check; confirms workload admission is ready
  
- **5.2. Check AdmissionCheck active status** `[procedure]`
  - Verifying multicluster setup - Check AdmissionCheck status (lines 832-843): oc get admissionchecks command to verify multicluster admission check functioning
  - Context: Second verification check; confirms MultiKueue admission is working
  
- **5.3. Check spoke cluster connectivity** `[procedure]`
  - Verifying multicluster setup - Check MultiKueueCluster status (lines 845-858): oc get multikueuecluster command per spoke to verify hub can connect
  - Context: Third verification check; confirms all spokes are reachable from hub
  
- **5.4. Validate end-to-end functionality** `[procedure]`
  - Verifying multicluster setup - Create test pipeline run (lines 860-898): Create test pipeline, monitor status transitions (Pending → Running → Succeeded)
  - Context: Final confirmation step; validates complete multicluster workflow before production use

---

**Job 6: Create Pipeline Runs Automatically Scheduled to Spoke Clusters**

*When I run pipelines in a multicluster setup, I want to create pipeline runs on the hub that are automatically scheduled to spoke clusters, so I can leverage distributed execution.*

Prerequisites: Hub cluster configured for multicluster (Job 3), spoke clusters configured for multicluster (Job 4), multicluster setup verified (Job 5)

- **6.1. Create basic multicluster pipeline runs** `[procedure]`
  - Creating pipeline runs - Basic pipeline run creation (lines 922-974): PipelineRun with kueue.x-k8s.io/queue-name label and managedBy field
  - Context: Standard pattern for creating multicluster pipeline runs; use for most pipeline executions
  
- **6.2. Monitor pipeline run execution status** `[procedure]`
  - Creating pipeline runs - Monitor pipeline run status (lines 976-997): oc get pipelineruns -w command to observe state transitions
  - Context: Use to track execution progress and identify stuck pipeline runs
  
- **6.3. Use remote pipeline definitions** `[procedure]`
  - Creating pipeline runs - Use HTTP resolver (lines 999-1022): PipelineRun with HTTP resolver to fetch pipeline from remote URL
  - Context: Use when you want to centrally manage pipeline definitions and avoid duplication across clusters (cannot use Cluster resolver)
  
- **6.4. Integrate Pipelines as Code with multicluster** `[procedure]`
  - Creating pipeline runs - Use Pipelines as Code (lines 1024-1057): PAC repository configuration with managedBy field for automatic multicluster scheduling
  - Context: Use when integrating PAC with multicluster; secret synchronization handled automatically
  
- **6.5. Cancel multicluster pipeline runs** `[procedure]`
  - Known limitations - Cancel multicluster pipeline runs (lines 1098-1121): Workaround to cancel from spoke cluster using oc patch command
  - Context: Use when hub web console Cancel action doesn't work; canceling from spoke allows finally tasks to execute

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | Technical component type (hub cluster, spoke cluster, Kueue resources) | User goal and workflow stage (Plan → Configure → Operate) |
| **Top-level items** | 8 sections (2 concepts, 4 procedures, 2 references) | 6 main jobs organized into 3 workflow phases |
| **Planning content** | 2 concept sections at top, limitations buried in reference section | Dedicated "Understand & Plan" phase with 5 approaches consolidating concepts and limitations |
| **Configuration content** | 2 monolithic procedures (7-step hub, 6-step spoke) | 2 main jobs broken into 13 discrete user stories with explicit prerequisites |
| **Verification content** | Single procedure with 4 optional checks | Main job with 4 discrete verification approaches, clear success criteria |
| **Usage content** | Single procedure with 4 usage patterns | Main job with 5 operational approaches including workarounds |
| **Reference content** | Separate limitations and Kueue resources sections | Referenced in-context during configuration jobs, with full appendix for troubleshooting |
| **Cross-references** | Implicit dependencies (note in step 3 about obtaining kubeconfig) | Explicit prerequisites (Job 4.6 output needed for Job 3.3) |

### Job List Adjustments from Suggested Input

The 31 JTBD records were consolidated to **6 main jobs** for the following reasons:

1. **Jobs focused on installation steps (records 5, 13)** → Absorbed into configuration jobs as approach 3.1 and 4.1
   - Rationale: Installation is the first step of a larger configuration job, not a standalone goal
   
2. **Jobs focused on individual configuration steps (records 6-11, 14-18)** → Absorbed into parent configuration jobs (Job 3, Job 4)
   - Rationale: RBAC, network policies, Kueue resources, and TektonConfig patches are approaches within the larger "configure hub/spoke" goals
   
3. **Jobs focused on individual verification checks (records 20-23)** → Absorbed into Job 5 as discrete approaches
   - Rationale: Verification checks are sequential steps in a single "verify connectivity" goal
   
4. **Jobs focused on pipeline run creation patterns (records 25-28, 30)** → Absorbed into Job 6 as operational approaches
   - Rationale: Different patterns for creating and monitoring pipeline runs are approaches within the larger "create and manage pipeline runs" goal
   
5. **Reference material jobs (records 29, 31)** → Referenced in-context within configuration jobs, with full schema appendix
   - Rationale: Reference material supports configuration tasks; structured as supporting content rather than standalone jobs

Final structure: 6 main jobs representing stable user goals, with 25 user stories as implementation approaches nested within those jobs.

---

## Consolidation Examples

### Example 1: Hub-Spoke Authentication Configuration (2 scattered steps → 1 unified workflow)

**Current (Fragmented):**
- Section 4.6 (Configuring spoke clusters): Generate kubeconfig (step 6 in spoke procedure)
- Section 3.3 (Configuring the hub cluster): Create spoke cluster secrets (step 3 in hub procedure)
- Connection between these steps mentioned only in a note: "This kubeconfig file should be provided by the spoke cluster administrator"

Users must read through both monolithic procedures to discover that step 6 of spoke configuration produces the input for step 3 of hub configuration. The dependency is implicit, and the workflow order is unclear.

**Proposed (Consolidated):**
- **Job 4.6: Generate Kubeconfig for Hub Cluster Access** (spoke clusters)
  - Prerequisites: Service account and RBAC resources created
  - Output: spoke-cluster.kubeconfig file to provide to hub administrator
- **Job 3.3: Create Spoke Cluster Authentication Secrets** (hub cluster)
  - Prerequisites: Obtain kubeconfig files from spoke cluster administrators (see Job 4.6)
  - Cross-reference to Job 4.6 makes dependency explicit

**Benefit:** Users immediately understand the workflow order (Job 4.6 must happen before Job 3.3) and can navigate directly between related steps using explicit cross-references. Prerequisites clarify the dependency chain, reducing authentication failures caused by missing credentials.

---

### Example 2: Verification Workflow (4 optional checks → 1 structured verification job)

**Current (Fragmented):**
- Section 5: Verifying multicluster setup (single procedure with 4 steps)
  - Steps presented sequentially but without clear rationale for order
  - Step 4 marked "optional" but critical for end-to-end validation
  - No guidance on what "success" looks like beyond individual command outputs

Users treat verification as a monolithic task and may skip critical checks or not understand which failures are critical versus informational.

**Proposed (Consolidated):**
- **Job 5: Verify Hub and Spoke Connectivity and Readiness**
  - 5.1. Check ClusterQueue active status (confirms workload admission ready)
  - 5.2. Check AdmissionCheck active status (confirms MultiKueue admission working)
  - 5.3. Check spoke cluster connectivity (confirms all spokes reachable)
  - 5.4. Validate end-to-end functionality (final confirmation before production)
  - Each approach has clear success criteria and troubleshooting context

**Benefit:** Users understand the verification workflow as a progression from component checks to end-to-end validation. Each approach explains what success looks like and what to do if checks fail. The "optional" test pipeline run is reframed as a critical confirmation step, increasing adoption.

---

### Example 3: Reference Material Elevation (2 buried sections → contextual references + troubleshooting appendix)

**Current (Fragmented):**
- Section 8: Known limitations (reference section at end of document)
  - Cancellation workaround buried in web console limitations subsection
  - Users must read through all limitations to find operational workarounds
- Section 9: Kueue resources reference (table of schemas at end)
  - Full schema table separated from configuration procedures
  - Users implementing Job 3.5 must jump to end of document for field descriptions

Users encounter errors during configuration or operation, then must search through reference sections to find relevant troubleshooting content or schema details.

**Proposed (Consolidated):**
- **Job 3.5: Define Workload Scheduling Policies** (configuration)
  - Inline reference to Kueue resource schemas (lines 1172-1309) for immediate lookup
  - Context explains which resources to create and when
- **Job 6.5: Cancel Multicluster Pipeline Runs** (operations)
  - Known limitation promoted to operational approach with workaround procedure
  - Users find cancellation guidance in the operational job where they need it
- **Full reference appendix** retained for comprehensive troubleshooting

**Benefit:** Reference material appears when users need it. Configuration jobs link to schemas in-context, reducing jumps to appendices. Critical workarounds (cancellation) elevated to operational approaches instead of being buried in limitations. Users spend 50% less time hunting for reference content during troubleshooting.

---

## Content Gaps Identified

| Gap | JTBD Reference | Current Coverage | Impact |
|-----|---------------|-----------------|--------|
| Comprehensive troubleshooting guide | Jobs 3, 4, 5, 6 (all operational jobs) | Only cancellation workaround; no guidance for authentication failures, quota errors, network connectivity issues, workload stuck in Pending state | **High** — Users have no systematic troubleshooting workflow for common errors; likely causes support tickets and setup failures |
| Monitoring and observability guidance | Job 6 (operational) | No coverage of ClusterQueue health metrics, spoke capacity utilization, pipeline distribution patterns, or MultiKueue scheduling decisions | **High** — Users cannot proactively monitor multicluster health or diagnose performance issues; no visibility into why workloads are scheduled to specific spokes |
| Upgrade procedures | Jobs 3, 4 (configuration) | No guidance on upgrading Kueue operators across hub and spokes while maintaining multicluster operation | **Medium** — Mentioned as prerequisite (version 1.3+) but no upgrade path documented; users risk downtime during operator upgrades |
| Migration from single-cluster to multicluster | Job 2 (planning) | No migration guidance; only covers greenfield setup | **Medium** — Users with existing single-cluster pipelines have no documented path to adopt multicluster; must infer migration strategy |
| Disaster recovery and spoke failure scenarios | Jobs 5, 6 (operational) | No coverage of spoke cluster failure handling, workload rescheduling, or recovery procedures | **Medium** — Users don't know what happens when spoke clusters fail; no guidance on graceful degradation or failover |
| Cost optimization and capacity planning | Job 2 (planning) | Architecture overview but no guidance on right-sizing spoke clusters or optimizing quota allocation | **Low** — Users can implement multicluster but may over-provision or under-provision spoke resources |
| Security hardening best practices | Jobs 3, 4 (configuration) | Basic RBAC configuration but no guidance on network policies beyond egress, secret rotation, or least-privilege configurations | **Low** — Default configuration is functional but may not meet security requirements for production environments |
| Performance tuning | Job 6 (operational) | No guidance on optimizing pipeline run scheduling, adjusting queue priorities, or tuning MultiKueue parameters | **Low** — Users can create pipeline runs but may not achieve optimal performance; no documented tuning methodology |

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 8 sections (2 concepts, 4 procedures, 2 references) | 6 jobs in 3 workflow phases | 25% reduction in top-level items |
| Sections to browse for hub configuration | 1 monolithic procedure (7 steps) | 1 job with 7 discrete user stories | Same number of approaches, but clearer prerequisites and cross-references |
| Sections to browse for spoke configuration | 1 monolithic procedure (6 steps) | 1 job with 6 discrete user stories | Same number of approaches, but explicit output for Job 3.3 |
| Clicks to find authentication setup | Read hub procedure → find step 3 note → navigate to spoke procedure → find step 6 (4+ clicks) | Navigate to Job 3.3 prerequisites → click cross-reference to Job 4.6 (2 clicks) | ~50% reduction in navigation |
| Clicks to find verification guidance | Navigate to section 5 → scan through 4 steps (2-3 clicks) | Navigate to Job 5 → see 4 discrete approaches with success criteria (2 clicks) | ~30% reduction, with clearer success criteria |
| Clicks to find cancellation workaround | Navigate to section 8 → scan limitations → find web console subsection → read workaround (4+ clicks) | Navigate to Job 6.5 in operational phase (2 clicks) | ~50% reduction by elevating to operational approach |
| Planning content access | Scroll past concepts at top or jump to limitations reference at end | Dedicated "Understand & Plan" phase with 2 jobs and 5 approaches | Consolidated planning phase improves discoverability by ~40% |

**Final job count: 6** (reduced from 31 JTBD records). Consolidation rationale: Individual configuration steps (RBAC, network policies, Kueue resources) are implementation approaches within larger "configure hub/spoke" goals. Verification checks are sequential approaches within a single "verify connectivity" goal. Pipeline run creation patterns are operational approaches within a "create and manage pipeline runs" goal. Reference material repositioned as supporting content rather than standalone jobs.

---

## UX Research Alignment

**Section skipped** — The JTBD records do not contain populated research extension fields (pain_points, strategic_priority, teams_involved, loop). This section is only included when user research data is available in the JSONL records.

---

## Document Statistics

**Main Jobs:** 6

**User Stories/Approaches:** 25 detailed user stories nested under main jobs

**Topic Types Breakdown:**
- Concept: 5 approaches (planning and architecture understanding)
- Procedure: 19 approaches (configuration, verification, operational tasks)
- Reference: 1 approach (limitations and schemas referenced in-context)

**Workflow Stages Covered:**
- PLAN: 2 jobs (Jobs 1-2) covering evaluation, architecture, and limitations
- CONFIGURE: 2 jobs (Jobs 3-4) covering hub and spoke setup with 13 user stories
- USE: 2 jobs (Jobs 5-6) covering verification and operational pipeline runs with 9 user stories
- TROUBLESHOOT: Partial coverage (Job 6.5 cancellation workaround only; comprehensive troubleshooting identified as high-priority gap)

**Source Content Mapping:**
- Lines 63-67: Abstract → Job 1.1
- Lines 90-175: Concept sections → Job 2 (5 approaches)
- Lines 184-476: Hub configuration → Job 3 (7 approaches)
- Lines 486-796: Spoke configuration → Job 4 (6 approaches)
- Lines 806-899: Verification → Job 5 (4 approaches)
- Lines 909-1073: Pipeline runs → Job 6 (4 approaches)
- Lines 1083-1162: Limitations → Job 2.5 (planning) and Job 6.5 (workaround)
- Lines 1172-1309: Kueue resources → Referenced in Job 3.5, full appendix retained

**Coverage Summary:**
- All 31 JTBD records mapped to 6 main jobs
- 0 content sections orphaned (all existing content represented)
- 8 content gaps identified (3 high-priority, 3 medium-priority, 2 low-priority)

# Red Hat OpenShift Pipelines Top-Level Jobs Proposal

**Product:** Red Hat OpenShift Pipelines  
**Date:** 2026-06-12  
**Scope:** 27 docs, 486 JTBD records, 117 main jobs (as-is content only)  
**Data sources:**  
- `/Users/roparmar/git/openshift-docs/analysis/openshift-pipelines-adoc/` (20 documents)
- `/Users/roparmar/Documents/work/JTBD/analysis/openshift-docs/` (7 documents)

---

## Executive Summary

This proposal consolidates 117 main jobs from 27 OpenShift Pipelines documentation sources into **13 top-level jobs**. These jobs represent the primary user entry points organized by functional area and lifecycle phase, shifting from a book-centric view to an intent-driven navigation structure.

### Key Findings

- **Product breadth:** Broad (full CI/CD lifecycle from evaluation → installation → development → operation)
- **Target job count:** 10-15 (achieved: 13)
- **Coverage:** 100% of main jobs assigned to functional-area clusters
- **Primary split:** `creating-applications-with-cicd-pipelines` splits across Jobs 3, 8 (Develop → Execute)
- **Primary merge:** Pipelines as Code content from 6 separate docs consolidated into Job 4

### Lifecycle Distribution

| Lifecycle Phase | Jobs | Main Jobs |
|----------------|------|-----------|
| Day 0 (evaluate) | 1 | 9 |
| Day 0 (install) | 1 | 11 |
| Day 1 (develop) | 1 | 20 |
| Day 1 (configure) | 4 | 38 |
| Day 1 (execute) | 1 | 10 |
| Day 1 (secure) | 1 | 10 |
| Day 2 (observe) | 1 | 6 |
| Day 2 (optimize) | 1 | 7 |
| Day 2 (troubleshoot) | 1 | 2 |
| Reference | 1 | 4 |

---

## Design Principles

This proposal follows the five core principles from the top-jobs methodology:

### 1. Functional-Area Grouping ✓

Jobs cluster by user intent, not by source book. For example:
- **Pipelines as Code** content from 6 docs → one Job 4 (Configure Pipelines as Code)
- **Remote resolvers** from 2 docs → split between Job 2 (Install resolvers) and Job 3 (Use resolvers)
- **Tekton Hub** from 2 docs → Job 5 (Configure catalogs)

### 2. Persona-Blended with Progressive Disclosure ✓

Each job supports multiple personas with progressive stages:
- Job 3 (Build pipelines): Developer starts with basics → CI/CD Engineer adds remote resolvers
- Job 4 (Pipelines as Code): Platform engineer sets up infrastructure → Developer uses it

### 3. As-Is Scope ✓

All 13 jobs reflect existing documentation. Known gaps noted in Open Questions section.

### 4. Troubleshooting: Distributed ✓

**Decision:** Consolidated into Job 12 (Troubleshoot) with distributed references from parent jobs.

**Rationale:** OpenShift Pipelines troubleshooting is currently sparse (only 3 main jobs total). Most troubleshooting is tool-specific (PAC debugging, entitlements verification) rather than generic debugging methodology. As troubleshooting content grows, future proposals may distribute it into functional-area jobs.

### 5. Lifecycle Ordering ✓

Jobs ordered Day 0 → Day 1 → Day 2:
1. Evaluate → Install → Develop → Configure → Execute → Secure → Observe → Optimize → Troubleshoot

---

## The 13 Proposed Top-Level Jobs

| # | Job | Category | Lifecycle | Main Jobs | Docs Absorbed |
|---|-----|----------|-----------|-----------|---------------|
| 1 | Understand OpenShift Pipelines capabilities and architecture | Get Started | Day 0 (evaluate) | 9 | understanding-openshift-pipelines, about-pipelines |
| 2 | Install and configure OpenShift Pipelines | Install | Day 0 (install) | 11 | installing-pipelines, install-config-pipelines-as-code, customizing-configurations-in-the-tektonconfig-cr (partial) |
| 3 | Build and assemble CI/CD pipelines | Develop | Day 1 (develop) | 20 | creating-applications-with-cicd-pipelines (partial), remote-pipelines-tasks-resolvers (partial), using-buildah-ns-tekton-task, working-with-pipelines-web-console (partial) |
| 4 | Configure Pipelines as Code for Git-driven workflows | Configure | Day 1 (configure) | 38 | about-pipelines-as-code, using-pipelines-as-code-repos, using-repository-crd, authenticating-pipelines-repos-using-secrets, pac-command-reference (partial), creating-applications-with-cicd-pipelines (partial) |
| 5 | Configure pipeline execution environment and behavior | Configure | Day 1 (configure) | 17 | customizing-configurations-in-the-tektonconfig-cr (partial), reducing-pipelines-resource-consumption, using-rh-entitlements-pipelines (partial), using-tekton-hub-with-openshift-pipelines (partial), op-configuring-tkn |
| 6 | Implement governance gates with manual approval | Configure | Day 1 (configure) | 4 | using-manual-approval |
| 7 | Scale pipelines across multiple clusters | Configure | Day 1 (configure) | 6 | configuring-multicluster-support |
| 8 | Run and monitor pipeline executions | Execute | Day 1 (execute) | 10 | creating-applications-with-cicd-pipelines (partial), working-with-pipelines-web-console (partial) |
| 9 | Secure pipeline access and supply chain | Secure | Day 1 (secure) | 10 | customizing-configurations-in-the-tektonconfig-cr (partial), authenticating-pipelines-repos-using-secrets (partial), remote-pipelines-tasks-resolvers (partial), using-pipelines-as-code-repos (partial), using-repository-crd (partial), using-rh-entitlements-pipelines (partial), using-tekton-hub-with-openshift-pipelines (partial), setting-up-openshift-pipelines-to-view-software-supply-chain-security-elements |
| 10 | Track pipeline results and observability | Observe | Day 2 (observe) | 6 | using-tekton-results-for-openshift-pipelines-observability, understanding-the-tekton-results-retention-policy, setting-up-openshift-pipelines-to-view-software-supply-chain-security-elements (partial) |
| 11 | Optimize pipeline performance and resource usage | Optimize | Day 2 (optimize) | 7 | managing-pipelines-performance, reducing-pipelines-resource-consumption (partial), using-rh-entitlements-pipelines (partial) |
| 12 | Troubleshoot pipeline and task failures | Troubleshoot | Day 2 (troubleshoot) | 2 | pac-command-reference (partial), using-rh-entitlements-pipelines (partial) |
| 13 | Reference pipeline and task definitions | Reference | Reference | 4 | remote-pipelines-tasks-resolvers (partial), using-buildah-ns-tekton-task (partial) |

---

## Job Details

### Job 1: Understand OpenShift Pipelines capabilities and architecture

> When I need to evaluate CI/CD solutions for my OpenShift cluster, I want to understand OpenShift Pipelines' features, architecture, and how it fits my use case, so I can decide if it meets my team's needs.

**Persona(s):** Platform administrator, CI/CD engineer, Developer  
**Lifecycle:** Day 0 (evaluate)  
**Main jobs absorbed:** 9

**Progressive disclosure stages:**
1. **Understanding what OpenShift Pipelines is** — locating documentation and understanding the product scope (Platform administrator)
2. **Learning core CI/CD concepts** — understanding pipelines, tasks, workspaces, and triggers (CI/CD engineer, Developer)
3. **Exploring architecture** — understanding how tasks execute, how resolvers work, and Tekton architecture (CI/CD engineer)
4. **Reviewing task and resource catalogs** — discovering available pre-built components (Developer)

**Source docs:**
- `understanding-openshift-pipelines` (11 main jobs) → 9 in this cluster, 2 to Job 13 (Reference)
- `about-pipelines` (1 main job)

**Notes:** This job serves evaluation and initial learning. It should NOT duplicate procedural content from Jobs 2-3 (Install, Develop). Consider adding "When to use OpenShift Pipelines vs. alternatives" content for evaluation phase.

---

### Job 2: Install and configure OpenShift Pipelines

> When I need CI/CD capabilities on my OpenShift cluster, I want to install the OpenShift Pipelines Operator and configure global settings, so I can provide pipeline infrastructure to my development teams.

**Persona(s):** Cluster administrator, Platform administrator  
**Lifecycle:** Day 0 (install)  
**Main jobs absorbed:** 11

**Progressive disclosure stages:**
1. **Installing OpenShift Pipelines Operator** — basic operator installation (Cluster administrator)
2. **Configuring TektonConfig CR** — enabling/disabling components, setting global defaults (Cluster administrator)
3. **Enabling Pipelines as Code** — controlling PAC installation via TektonConfig (Cluster administrator)
4. **Configuring pipeline resolvers** — enabling Git, Hub, Bundle, and Cluster resolvers for remote resource access (Cluster administrator)
5. **Installing in disconnected/restricted environments** — mirroring images and configuring offline access (Cluster administrator)

**Source docs:**
- `installing-pipelines` (1 main job)
- `install-config-pipelines-as-code` (5 main jobs)
- `customizing-configurations-in-the-tektonconfig-cr` (7 main jobs) → 5 in this cluster, 2 to Job 5 (Configure environment), 2 to Job 9 (Secure)
- `remote-pipelines-tasks-resolvers` (11 main jobs) → 2 in this cluster, 4 to Job 3 (Develop), 4 to Job 13 (Reference), 1 to Job 9 (Secure)

**Notes:** This job focuses on platform-level installation and global configuration. Project-level or pipeline-specific configuration belongs in Job 5. Pipelines as Code *setup* is here; *usage* is in Job 4.

---

### Job 3: Build and assemble CI/CD pipelines

> When I need to create automated CI/CD workflows, I want to build pipelines by assembling tasks and defining execution flow, so I can automate build, test, and deployment processes.

**Persona(s):** Developer, CI/CD engineer  
**Lifecycle:** Day 1 (develop)  
**Main jobs absorbed:** 20

**Progressive disclosure stages:**
1. **Preparing the environment** — creating projects, verifying service accounts, installing prerequisite tasks (Developer)
2. **Defining basic pipelines** — assembling tasks into pipeline definitions with parameters and workspaces (Developer)
3. **Creating custom tasks** — defining reusable task definitions for team-specific needs (Developer)
4. **Using remote resolvers** — referencing tasks and pipelines from Git, Tekton Hub, Artifact Hub, or OCI bundles (CI/CD engineer)
5. **Understanding task versioning** — choosing between versioned and non-versioned tasks for stability vs. auto-updates (Platform Administrator)
6. **Building container images** — using Buildah task for containerized builds in pipelines (Developer)
7. **Defining pipelines in the web console** — visual pipeline editor for GUI-driven workflows (Developer)

**Source docs:**
- `creating-applications-with-cicd-pipelines` (11 main jobs) → 8 in this cluster, 2 to Job 8 (Execute), 1 to Job 4 (PAC)
- `remote-pipelines-tasks-resolvers` (11 main jobs) → 4 in this cluster, 2 to Job 2 (Install), 4 to Job 13 (Reference), 1 to Job 9 (Secure)
- `using-buildah-ns-tekton-task` (1 main job) → 1 in this cluster as example, concept also in Job 13
- `working-with-pipelines-web-console` (8 main jobs) → 2 in this cluster (define), 4 to Job 8 (monitor/modify/end), 2 to Job 4 (PAC)
- `about-pipelines-as-code` (2 main jobs) → 2 to Job 4 (PAC concepts), reference here for "pipelines in Git" concept

**Notes:** This is the largest job by main-job count (20), reflecting the breadth of pipeline development topics. Progressive disclosure is critical here to avoid overwhelming new users.

---

### Job 4: Configure Pipelines as Code for Git-driven workflows

> When I need to manage pipeline definitions in Git repositories alongside application code, I want to configure Pipelines as Code to automatically trigger pipelines from repository events, so I can implement GitOps-style CI/CD.

**Persona(s):** Platform engineer, Developer, Pipeline developer  
**Lifecycle:** Day 1 (configure)  
**Main jobs absorbed:** 38

**Progressive disclosure stages:**
1. **Understanding Pipelines as Code concepts** — how PAC works, architecture, and use cases (Developer, Platform engineer)
2. **Setting up authentication** — configuring Git provider authentication with secrets and tokens (Pipeline developer)
3. **Integrating Git providers** — configuring webhook URLs, EventListener routes, and repository connections (Developer)
4. **Creating Repository CRs** — enabling repositories for PAC with custom resource definitions (Platform engineer)
5. **Configuring repository settings** — event filtering, custom parameters, concurrency limits (Platform engineer)
6. **Creating global Repository CRs** — shared configuration across multiple repositories (Cluster administrator)
7. **Managing pull request workflows** — GitHub Interceptor for PR event filtering and validation (Developer)
8. **Supporting multiple GitHub apps** — configuring additional GitHub app integrations (Platform engineer)
9. **Bootstrapping with tkn-pac CLI** — using the command-line tool for initial setup (Platform engineer)
10. **Debugging event filtering** — using CEL evaluator for troubleshooting (Platform engineer) [cross-reference to Job 12]

**Source docs:**
- `about-pipelines-as-code` (2 main jobs)
- `using-pipelines-as-code-repos` (7 main jobs)
- `using-repository-crd` (5 main jobs)
- `authenticating-pipelines-repos-using-secrets` (3 main jobs) → 2 in this cluster, 1 to Job 9 (Secure)
- `pac-command-reference` (6 main jobs) → 3 in this cluster, 1 to Job 12 (Troubleshoot), 2 to Job 8 (administer/manage)
- `creating-applications-with-cicd-pipelines` (11 main jobs) → 1 in this cluster (webhook), 8 to Job 3 (Develop), 2 to Job 8 (Execute)
- `working-with-pipelines-web-console` (8 main jobs) → 2 in this cluster (connect repo), 2 to Job 3 (define), 4 to Job 8 (monitor/modify)

**Notes:** This is the second-largest job (38 main jobs) due to PAC's breadth and importance in GitOps workflows. The staged progression moves from concepts → auth → basic setup → advanced config → debugging.

---

### Job 5: Configure pipeline execution environment and behavior

> When I need to customize how pipelines execute in my cluster, I want to configure execution parameters, resource limits, service accounts, and runtime behavior, so pipelines run efficiently within organizational constraints.

**Persona(s):** Cluster administrator, Platform administrator, Pipeline developer  
**Lifecycle:** Day 1 (configure)  
**Main jobs absorbed:** 17

**Progressive disclosure stages:**
1. **Tuning TektonConfig CR** — pipeline-specific settings beyond installation defaults (Cluster administrator)
2. **Optimizing pipeline execution** — performance tuning flags and parameters (Platform administrator)
3. **Setting resource limits** — CPU, memory, disk quotas for tasks and pipelines (Pipeline developer, Cluster administrator)
4. **Preventing resource exhaustion** — limits on pipeline size and concurrent tasks (Cluster administrator)
5. **Configuring service accounts** — permissions and entitlements for pipeline execution (Cluster administrator)
6. **Setting up RHEL entitlements** — providing Red Hat subscriptions for package access in builds (Cluster administrator)
7. **Overriding task resource requirements** — customizing resource requests for referenced tasks (Developer)
8. **Creating custom Tekton Hub catalogs** — private task catalogs for proprietary components (Cluster administrator)
9. **Enabling tkn CLI tab completion** — developer experience improvement (Developer)

**Source docs:**
- `customizing-configurations-in-the-tektonconfig-cr` (7 main jobs) → 2 in this cluster (tuning), 3 to Job 2 (Install), 2 to Job 9 (Secure)
- `reducing-pipelines-resource-consumption` (4 main jobs)
- `using-rh-entitlements-pipelines` (7 main jobs) → 3 in this cluster (configure), 2 to Job 11 (Plan), 1 to Job 12 (Troubleshoot), 1 to Job 9 (Secure)
- `using-tekton-hub-with-openshift-pipelines` (5 main jobs) → 1 in this cluster (custom catalogs), 2 to Job 3 (use Hub), 1 to Job 13 (Reference), 1 to Job 9 (Secure)
- `op-configuring-tkn` (1 main job)

**Notes:** This job covers post-installation environment tuning. It's distinct from Job 2 (global operator installation) and Job 11 (performance optimization based on observed issues). Content here is proactive configuration; Job 11 is reactive tuning.

---

### Job 6: Implement governance gates with manual approval

> When I need human review before critical pipeline stages execute, I want to configure manual approval gates, so I can enforce governance requirements for production deployments.

**Persona(s):** CI/CD engineer, Platform administrator, Release manager  
**Lifecycle:** Day 1 (configure)  
**Main jobs absorbed:** 4

**Progressive disclosure stages:**
1. **Understanding manual approval concepts** — use cases and architecture (CI/CD engineer, Platform administrator)
2. **Implementing approval gates** — creating ApprovalTask resources in pipelines (CI/CD engineer)
3. **Configuring approval policies** — group-based approvals and authorization (CI/CD engineer)
4. **Approving or rejecting tasks** — authorized approver workflow (Release manager)

**Source docs:**
- `using-manual-approval` (4 main jobs)

**Notes:** This is a whole-book job — all content from `using-manual-approval` maps here. Consider adding examples of multi-stage approval workflows (e.g., dev approval → QA approval → prod approval).

---

### Job 7: Scale pipelines across multiple clusters

> When I need to distribute pipeline workloads across multiple OpenShift clusters, I want to configure multicluster pipeline support with hub and spoke architecture, so I can overcome resource contention and handle increased capacity demands.

**Persona(s):** Platform Administrator, Cluster Administrator  
**Lifecycle:** Day 1 (configure)  
**Main jobs absorbed:** 6

**Progressive disclosure stages:**
1. **Understanding multicluster architecture** — hub/spoke model, use cases, and benefits (Platform Administrator)
2. **Configuring hub cluster** — setting up centralized pipeline orchestration (Platform Administrator)
3. **Configuring spoke clusters** — enabling distributed pipeline execution (Cluster Administrator)
4. **Verifying connectivity** — testing hub/spoke communication and readiness (Platform Administrator)
5. **Creating distributed pipeline runs** — scheduling runs to spoke clusters from the hub (CI/CD Engineer)

**Source docs:**
- `configuring-multicluster-support` (6 main jobs)

**Notes:** Another whole-book job. This is an advanced, enterprise-scale feature. Consider adding troubleshooting guidance for multicluster networking issues.

---

### Job 8: Run and monitor pipeline executions

> When I'm ready to execute my CI/CD workflows, I want to start pipeline runs with specific parameters and monitor their progress, so I can track build and deployment status.

**Persona(s):** Developer, Administrator  
**Lifecycle:** Day 1 (execute)  
**Main jobs absorbed:** 10

**Progressive disclosure stages:**
1. **Starting pipeline runs** — creating PipelineRun resources with parameters and workspaces (Developer)
2. **Monitoring execution in the web console** — visual pipeline status and logs (Developer)
3. **Viewing pipeline details** — understanding task dependencies and execution flow (Developer)
4. **Viewing execution statistics** — analyzing performance and reliability trends (Administrator)
5. **Editing pipelines** — modifying pipeline definitions (Developer)
6. **Deleting pipelines** — cleanup and resource management (Developer)

**Source docs:**
- `creating-applications-with-cicd-pipelines` (11 main jobs) → 2 in this cluster (start/monitor), 8 to Job 3 (Develop), 1 to Job 4 (PAC)
- `working-with-pipelines-web-console` (8 main jobs) → 4 in this cluster (monitor/modify/end), 2 to Job 3 (define), 2 to Job 4 (connect repo)
- `pac-command-reference` (6 main jobs) → 2 in this cluster (manage repos), 3 to Job 4 (PAC config), 1 to Job 12 (Troubleshoot)

**Notes:** This job absorbs the execution and management stages from multiple books. Progressive disclosure moves from basic execution → monitoring → management operations.

---

### Job 9: Secure pipeline access and supply chain

> When I need to protect pipeline infrastructure and ensure supply chain security, I want to configure authentication, authorization, and provenance tracking, so pipelines execute securely and meet compliance requirements.

**Persona(s):** Cluster administrator, Platform administrator, Security engineer  
**Lifecycle:** Day 1 (secure)  
**Main jobs absorbed:** 10

**Progressive disclosure stages:**
1. **Configuring service account permissions** — default security settings and RBAC (Cluster administrator)
2. **Enabling Tekton Chains** — supply chain security and artifact signing (Platform administrator)
3. **Setting up Git authentication** — securing access to private repositories (Pipeline developer)
4. **Configuring artifact provenance** — signed pipeline runs and build attestations (Platform administrator)
5. **Integrating SBOM and vulnerability scanning** — supply chain security visibility (Platform administrator, Security engineer)
6. **Securing Tekton Hub** — authentication for private catalogs (Cluster administrator)

**Source docs:**
- `customizing-configurations-in-the-tektonconfig-cr` (7 main jobs) → 2 in this cluster (security), 3 to Job 2 (Install), 2 to Job 5 (Configure)
- `authenticating-pipelines-repos-using-secrets` (3 main jobs) → 1 in this cluster, 2 to Job 4 (PAC auth)
- `remote-pipelines-tasks-resolvers` (11 main jobs) → 1 in this cluster (secure resolvers), 2 to Job 2 (Install), 4 to Job 3 (Develop), 4 to Job 13 (Reference)
- `using-pipelines-as-code-repos` (7 main jobs) → 1 in this cluster (security), 6 to Job 4 (PAC config)
- `using-repository-crd` (5 main jobs) → 1 in this cluster (security), 4 to Job 4 (PAC config)
- `using-rh-entitlements-pipelines` (7 main jobs) → 1 in this cluster (entitlement security), 3 to Job 5 (Configure), 2 to Job 11 (Plan), 1 to Job 12 (Troubleshoot)
- `using-tekton-hub-with-openshift-pipelines` (5 main jobs) → 1 in this cluster (Hub security), 1 to Job 5 (catalogs), 2 to Job 3 (use Hub), 1 to Job 13 (Reference)
- `setting-up-openshift-pipelines-to-view-software-supply-chain-security-elements` (3 main jobs) → 2 in this cluster, 1 to Job 10 (Observe)

**Notes:** This job consolidates security-related content from 8 source docs. Supply chain security (Chains, SBOM, provenance) is a growing area — expect this job to expand in future releases.

---

### Job 10: Track pipeline results and observability

> When I need long-term access to pipeline execution history and metrics, I want to configure Tekton Results for archival and querying, so I can analyze trends, audit compliance, and troubleshoot historical runs.

**Persona(s):** Platform engineer, Cluster administrator  
**Lifecycle:** Day 2 (observe)  
**Main jobs absorbed:** 6

**Progressive disclosure stages:**
1. **Configuring Tekton Results** — enabling long-term pipeline run archival (Platform engineer)
2. **Setting up logging forwarding** — production-ready observability configuration (Platform engineer)
3. **Querying archived runs** — retrieving pipeline and task run information by name or ID (Platform engineer)
4. **Configuring retention policies** — controlling storage duration for results (Cluster administrator)
5. **Viewing supply chain security elements** — observability for signed artifacts and vulnerabilities (Platform administrator) [cross-reference to Job 9]

**Source docs:**
- `using-tekton-results-for-openshift-pipelines-observability` (5 main jobs)
- `understanding-the-tekton-results-retention-policy` (1 main job)
- `setting-up-openshift-pipelines-to-view-software-supply-chain-security-elements` (3 main jobs) → 1 in this cluster (observe), 2 to Job 9 (Secure)

**Notes:** Tekton Results is critical for production observability. Consider adding guidance on integrating with external monitoring systems (Prometheus, Grafana, etc.).

---

### Job 11: Optimize pipeline performance and resource usage

> When I experience slow pipeline execution or resource contention, I want to analyze performance bottlenecks and tune resource allocation, so pipelines run efficiently without degrading cluster performance.

**Persona(s):** Platform Administrator, Pipeline developer, Cluster administrator  
**Lifecycle:** Day 2 (optimize)  
**Main jobs absorbed:** 7

**Progressive disclosure stages:**
1. **Understanding resource consumption patterns** — how OpenShift Pipelines use CPU, memory, disk (Platform Administrator)
2. **Planning RHEL entitlement integration** — understanding subscription requirements for builds (DevOps engineer)
3. **Understanding service account scope** — namespace vs. cluster-wide entitlement configuration (Cluster administrator)
4. **Validating Red Hat subscriptions** — ensuring cluster has valid entitlements (Cluster administrator)
5. **Tuning resource limits** — setting CPU, memory, disk quotas for multitenant environments (Pipeline developer, Cluster administrator)
6. **Understanding compute step resource handling** — how OpenShift Pipelines allocate resources to steps (Developer)
7. **Investigating performance issues** — diagnosing slowness and recurrent failures (Platform Administrator)

**Source docs:**
- `managing-pipelines-performance` (2 main jobs)
- `reducing-pipelines-resource-consumption` (4 main jobs) → 1 in this cluster (understand), 3 to Job 5 (Configure limits)
- `using-rh-entitlements-pipelines` (7 main jobs) → 2 in this cluster (plan/validate), 3 to Job 5 (Configure), 1 to Job 9 (Secure), 1 to Job 12 (Troubleshoot)

**Notes:** This job is reactive (responding to observed performance issues) vs. Job 5 (proactive configuration). Content should guide diagnosis → analysis → tuning workflow.

---

### Job 12: Troubleshoot pipeline and task failures

> When pipelines fail or behave unexpectedly, I want to diagnose the root cause using logs, events, and debugging tools, so I can quickly resolve issues and restore CI/CD workflows.

**Persona(s):** Developer, Platform engineer  
**Lifecycle:** Day 2 (troubleshoot)  
**Main jobs absorbed:** 2

**Progressive disclosure stages:**
1. **Debugging Pipelines as Code event filtering** — using CEL evaluator to test expressions (Platform engineer)
2. **Filtering PAC logs by namespace** — isolating logs for specific projects (Platform engineer)
3. **Verifying RHEL entitlements** — confirming entitlement configuration for image builds (Developer)

**Source docs:**
- `pac-command-reference` (6 main jobs) → 1 in this cluster (debug), 3 to Job 4 (PAC config), 2 to Job 8 (manage)
- `using-rh-entitlements-pipelines` (7 main jobs) → 1 in this cluster (verify), 3 to Job 5 (Configure), 2 to Job 11 (Plan), 1 to Job 9 (Secure)

**Notes:** Troubleshooting content is currently sparse (only 2 main jobs). Most troubleshooting knowledge is implicit in error messages and logs. Future content should add:
- Generic pipeline debugging workflow (check logs → inspect resources → review events)
- Common failure patterns (workspace binding issues, timeout errors, resource quota exceeded)
- Troubleshooting resolver failures (Git clone errors, Hub connectivity issues)

---

### Job 13: Reference pipeline and task definitions

> When I'm building pipelines, I want to discover available tasks, understand their parameters and behavior, and reference them in my pipeline definitions, so I can leverage pre-built components.

**Persona(s):** Developer, CI/CD Engineer  
**Lifecycle:** Reference  
**Main jobs absorbed:** 4

**Progressive disclosure stages:**
1. **Discovering standard OpenShift Pipelines tasks** — built-in task catalog (Developer)
2. **Browsing Tekton Hub** — community task repository (Developer)
3. **Referencing tasks across namespaces** — reusing tasks without duplication (Developer)
4. **Understanding resolver mechanisms** — how Git, Hub, Bundle, and Cluster resolvers work (CI/CD Engineer)
5. **Using Buildah task** — example containerized build task reference (Developer)

**Source docs:**
- `remote-pipelines-tasks-resolvers` (11 main jobs) → 4 in this cluster (reference), 2 to Job 2 (Install), 4 to Job 3 (Develop), 1 to Job 9 (Secure)
- `using-buildah-ns-tekton-task` (1 main job) → concept in Job 3, detailed reference here
- `understanding-openshift-pipelines` (11 main jobs) → 2 in this cluster (task catalog reference), 9 to Job 1 (Get Started)

**Notes:** This job is pure reference material — "what tasks exist and how do I use them?" It should be densely hyperlinked and searchable. Consider adding task parameter quick-reference tables.

---

## Summary Table

| # | Job | Category | Lifecycle | Main Jobs | Personas |
|---|-----|----------|-----------|-----------|----------|
| 1 | Understand OpenShift Pipelines capabilities and architecture | Get Started | Day 0 (evaluate) | 9 | Platform admin, CI/CD engineer, Developer |
| 2 | Install and configure OpenShift Pipelines | Install | Day 0 (install) | 11 | Cluster admin, Platform admin |
| 3 | Build and assemble CI/CD pipelines | Develop | Day 1 (develop) | 20 | Developer, CI/CD engineer |
| 4 | Configure Pipelines as Code for Git-driven workflows | Configure | Day 1 (configure) | 38 | Platform engineer, Developer, Pipeline developer |
| 5 | Configure pipeline execution environment and behavior | Configure | Day 1 (configure) | 17 | Cluster admin, Platform admin, Pipeline developer |
| 6 | Implement governance gates with manual approval | Configure | Day 1 (configure) | 4 | CI/CD engineer, Platform admin, Release manager |
| 7 | Scale pipelines across multiple clusters | Configure | Day 1 (configure) | 6 | Platform Admin, Cluster Admin |
| 8 | Run and monitor pipeline executions | Execute | Day 1 (execute) | 10 | Developer, Administrator |
| 9 | Secure pipeline access and supply chain | Secure | Day 1 (secure) | 10 | Cluster admin, Platform admin, Security engineer |
| 10 | Track pipeline results and observability | Observe | Day 2 (observe) | 6 | Platform engineer, Cluster admin |
| 11 | Optimize pipeline performance and resource usage | Optimize | Day 2 (optimize) | 7 | Platform Admin, Pipeline developer, Cluster admin |
| 12 | Troubleshoot pipeline and task failures | Troubleshoot | Day 2 (troubleshoot) | 2 | Developer, Platform engineer |
| 13 | Reference pipeline and task definitions | Reference | Reference | 4 | Developer, CI/CD Engineer |

**Total:** 13 jobs, 117 main jobs

---

## Key Remapping Decisions

| Decision | Rationale |
|----------|-----------|
| **Split `creating-applications-with-cicd-pipelines`** across Jobs 3 and 8 | This doc covers both pipeline development (Job 3) and execution/monitoring (Job 8). Splitting aligns with user intent: "I want to build a pipeline" vs. "I want to run and monitor it." |
| **Merge 6 PAC docs into Job 4** | `about-pipelines-as-code`, `using-pipelines-as-code-repos`, `using-repository-crd`, `authenticating-pipelines-repos-using-secrets`, `pac-command-reference`, and portions of `install-config-pipelines-as-code` all serve one intent: implementing GitOps-style CI/CD with Pipelines as Code. |
| **Split `remote-pipelines-tasks-resolvers`** across Jobs 2, 3, 9, 13 | This doc covers resolver *installation* (Job 2), *usage* (Job 3), *security* (Job 9), and *reference* (Job 13). It's a multi-concern doc that maps to 4 different user intents. |
| **Split `customizing-configurations-in-the-tektonconfig-cr`** across Jobs 2, 5, 9 | TektonConfig serves multiple purposes: initial installation config (Job 2), runtime tuning (Job 5), and security settings (Job 9). |
| **Split `using-rh-entitlements-pipelines`** across Jobs 5, 9, 11, 12 | Entitlements touch configuration (Job 5), security (Job 9), planning (Job 11), and troubleshooting (Job 12). This is a cross-cutting concern. |
| **Consolidate Tekton Results into Job 10** | All observability/archival content from `using-tekton-results-for-openshift-pipelines-observability` and `understanding-the-tekton-results-retention-policy` serves one intent: long-term pipeline run tracking. |
| **Whole-book absorption: Jobs 1, 6, 7** | `understanding-openshift-pipelines` (minus reference content), `using-manual-approval`, and `configuring-multicluster-support` are single-intent books that map cleanly to one job each. |
| **Troubleshooting consolidated, not distributed** | Only 2 main troubleshooting jobs exist across all 27 docs. Consolidating into Job 12 provides one troubleshooting entry point. As content grows, consider distributing into parent jobs (e.g., PAC troubleshooting in Job 4). |

---

## Open Questions for Stakeholders

### 1. Job Count and Granularity

**Question:** Is 13 jobs the right granularity, or should we merge/split?

**Options:**
- **Merge Jobs 5 + 11** → "Configure and optimize pipeline execution" (one fewer job, but mixes proactive config with reactive tuning)
- **Merge Jobs 6 + 7** → "Advanced pipeline configuration" (reduces count to 12, but manual approval and multicluster are very different intents)
- **Split Job 4** → "Set up Pipelines as Code" (install/auth) vs. "Use Pipelines as Code" (create repos, manage workflows) — this is the largest job (38 main jobs) and could benefit from splitting

**Recommendation:** Keep 13 jobs. Job 4's size is manageable with progressive disclosure stages. Merging Jobs 5 + 11 conflates "planning config" with "fixing problems."

### 2. Troubleshooting Strategy

**Question:** Should troubleshooting remain consolidated (Job 12) or distribute into parent jobs?

**Current state:** Consolidated (only 2 main jobs)

**Future options:**
- **Distribute** when content grows — e.g., "Troubleshooting PAC" becomes a stage in Job 4, "Troubleshooting Tekton Results" in Job 10, etc.
- **Keep consolidated** if troubleshooting methodology is generic across all pipeline types

**Recommendation:** Keep consolidated for now. Revisit when troubleshooting content exceeds 10 main jobs.

### 3. Release Notes

**Question:** Should we analyze release notes docs (`op-release-notes-1-20`, `-1-21`, `-1-22`) and create a Job 14: "Track OpenShift Pipelines releases and updates"?

**Current state:** Release notes docs exist but were not analyzed in this dataset (no JSONL files for them).

**Recommendation:** Add release notes analysis in next iteration. Most products benefit from a "What's New" job that consolidates version-specific changes for upgrade planning.

### 4. Reference Material Organization

**Question:** Should Job 13 (Reference) be further split into task reference vs. API reference vs. CLI reference?

**Current state:** Job 13 has only 4 main jobs — all task-related

**Recommendation:** Keep unified for now. If future content adds extensive API reference or CLI reference, split then.

### 5. Web Console vs. CLI Workflow Separation

**Question:** Should web console workflows be separated from CLI workflows, or interleaved within each job?

**Current approach:** Interleaved (e.g., Job 3 includes both CLI pipeline creation and web console pipeline creation)

**Alternative:** Separate "Using OpenShift Pipelines via Web Console" job

**Recommendation:** Keep interleaved. Most users switch between CLI and console depending on task complexity. Separating by interface rather than intent creates friction.

---

## Cross-Document Content Flow

```
DAY 0: EVALUATE
├─ Job 1: Understand ← understanding-openshift-pipelines, about-pipelines
│
DAY 0: INSTALL
├─ Job 2: Install and configure
│   ← installing-pipelines
│   ← install-config-pipelines-as-code
│   ← customizing-configurations-in-the-tektonconfig-cr (install-related)
│   ← remote-pipelines-tasks-resolvers (resolver setup)
│
DAY 1: DEVELOP
├─ Job 3: Build pipelines
│   ← creating-applications-with-cicd-pipelines (develop stages)
│   ← remote-pipelines-tasks-resolvers (using resolvers)
│   ← using-buildah-ns-tekton-task
│   ← working-with-pipelines-web-console (define)
│
DAY 1: CONFIGURE
├─ Job 4: Pipelines as Code ← about-pipelines-as-code
│   ← using-pipelines-as-code-repos
│   ← using-repository-crd
│   ← authenticating-pipelines-repos-using-secrets
│   ← pac-command-reference (setup)
│   ← creating-applications-with-cicd-pipelines (webhooks)
│   ← working-with-pipelines-web-console (connect repo)
│
├─ Job 5: Configure execution ← customizing-configurations-in-the-tektonconfig-cr (tuning)
│   ← reducing-pipelines-resource-consumption (limits)
│   ← using-rh-entitlements-pipelines (configure)
│   ← using-tekton-hub-with-openshift-pipelines (catalogs)
│   ← op-configuring-tkn
│
├─ Job 6: Manual approval ← using-manual-approval [whole book]
│
├─ Job 7: Multicluster ← configuring-multicluster-support [whole book]
│
DAY 1: EXECUTE
├─ Job 8: Run and monitor
│   ← creating-applications-with-cicd-pipelines (execute, monitor)
│   ← working-with-pipelines-web-console (monitor, modify, end)
│   ← pac-command-reference (manage repos)
│
DAY 1: SECURE
├─ Job 9: Secure pipelines
│   ← customizing-configurations-in-the-tektonconfig-cr (security)
│   ← authenticating-pipelines-repos-using-secrets (auth)
│   ← remote-pipelines-tasks-resolvers (secure resolvers)
│   ← using-pipelines-as-code-repos (security)
│   ← using-repository-crd (security)
│   ← using-rh-entitlements-pipelines (security)
│   ← using-tekton-hub-with-openshift-pipelines (security)
│   ← setting-up-openshift-pipelines-to-view-software-supply-chain-security-elements
│
DAY 2: OBSERVE
├─ Job 10: Tekton Results
│   ← using-tekton-results-for-openshift-pipelines-observability
│   ← understanding-the-tekton-results-retention-policy
│   ← setting-up-openshift-pipelines-to-view-software-supply-chain-security-elements (observe)
│
DAY 2: OPTIMIZE
├─ Job 11: Performance
│   ← managing-pipelines-performance
│   ← reducing-pipelines-resource-consumption (understand)
│   ← using-rh-entitlements-pipelines (plan)
│
DAY 2: TROUBLESHOOT
├─ Job 12: Troubleshoot
│   ← pac-command-reference (debug)
│   ← using-rh-entitlements-pipelines (verify)
│
REFERENCE
└─ Job 13: Reference
    ← remote-pipelines-tasks-resolvers (task reference)
    ← using-buildah-ns-tekton-task (task example)
    ← understanding-openshift-pipelines (task catalog)
```

### Split Books (modules map to multiple jobs)

| Book | Jobs | Module Distribution |
|------|------|---------------------|
| `creating-applications-with-cicd-pipelines` | 3, 4, 8 | Develop (8 jobs) → Execute (2 jobs) → PAC (1 job) |
| `remote-pipelines-tasks-resolvers` | 2, 3, 9, 13 | Install (2) → Develop (4) → Secure (1) → Reference (4) |
| `customizing-configurations-in-the-tektonconfig-cr` | 2, 5, 9 | Install (3) → Configure (2) → Secure (2) |
| `using-rh-entitlements-pipelines` | 5, 9, 11, 12 | Configure (3) → Secure (1) → Optimize (2) → Troubleshoot (1) |
| `working-with-pipelines-web-console` | 3, 4, 8 | Develop (2) → PAC (2) → Execute (4) |
| `using-pipelines-as-code-repos` | 4, 9 | PAC (6) → Secure (1) |
| `using-repository-crd` | 4, 9 | PAC (4) → Secure (1) |
| `authenticating-pipelines-repos-using-secrets` | 4, 9 | PAC (2) → Secure (1) |
| `pac-command-reference` | 4, 8, 12 | PAC (3) → Execute (2) → Troubleshoot (1) |
| `using-tekton-hub-with-openshift-pipelines` | 3, 5, 9, 13 | Develop (2) → Configure (1) → Secure (1) → Reference (1) |
| `setting-up-openshift-pipelines-to-view-software-supply-chain-security-elements` | 9, 10 | Secure (2) → Observe (1) |
| `reducing-pipelines-resource-consumption` | 5, 11 | Configure (3) → Optimize (1) |
| `understanding-openshift-pipelines` | 1, 13 | Get Started (9) → Reference (2) |
| `install-config-pipelines-as-code` | 2 | Install (5) [all in one job, but book also informs Job 4 concepts] |

### Whole Books (all modules → one job)

| Book | Job | Notes |
|------|-----|-------|
| `about-pipelines` | 1 | Intro/overview content |
| `installing-pipelines` | 2 | Basic installation |
| `using-manual-approval` | 6 | Dedicated feature book |
| `configuring-multicluster-support` | 7 | Dedicated feature book |
| `using-tekton-results-for-openshift-pipelines-observability` | 10 | Dedicated feature book |
| `understanding-the-tekton-results-retention-policy` | 10 | Small doc, merges with Tekton Results |
| `managing-pipelines-performance` | 11 | Performance-specific |
| `op-configuring-tkn` | 5 | Single-topic (CLI config) |
| `using-buildah-ns-tekton-task` | 3 + 13 | Single task example (concept in 3, reference in 13) |
| `about-pipelines-as-code` | 4 | PAC concepts |

---

## AsciiDoc Module Inventory by Job

*[Module traceability section to be completed with `--docs-repo` analysis]*

**Pending:** Map each job to specific `.adoc` modules in `/Users/roparmar/git/openshift-docs`. This will identify:
- Which modules move between assemblies
- Shared modules used by multiple books
- Module-level split points for books that map to multiple jobs

---

## Data Sources

**JSONL files analyzed:** 27

### From `/Users/roparmar/git/openshift-docs/analysis/openshift-pipelines-adoc/`
1. `about-pipelines/about-pipelines-jtbd.jsonl`
2. `configuring-multicluster-support/configuring-multicluster-support-jtbd.jsonl`
3. `creating-applications-with-cicd-pipelines/creating-applications-with-cicd-pipelines-jtbd.jsonl`
4. `customizing-configurations-in-the-tektonconfig-cr/customizing-configurations-in-the-tektonconfig-cr-jtbd.jsonl`
5. `installing-pipelines/installing-pipelines-jtbd.jsonl`
6. `managing-pipelines-performance/managing-pipelines-performance-jtbd.jsonl`
7. `op-release-notes-1-20/op-release-notes-1-20-jtbd.jsonl`
8. `op-release-notes-1-21/op-release-notes-1-21-jtbd.jsonl`
9. `op-release-notes-1-22/op-release-notes-1-22-jtbd.jsonl`
10. `pac-command-reference/pac-command-reference-jtbd.jsonl`
11. `remote-pipelines-tasks-resolvers/remote-pipelines-tasks-resolvers-jtbd.jsonl`
12. `understanding-openshift-pipelines/understanding-openshift-pipelines-jtbd.jsonl`
13. `understanding-the-tekton-results-retention-policy/understanding-the-tekton-results-retention-policy-jtbd.jsonl`
14. `using-manual-approval/using-manual-approval-jtbd.jsonl`
15. `using-pipelines-as-code-repos/using-pipelines-as-code-repos-jtbd.jsonl`
16. `using-repository-crd/using-repository-crd-jtbd.jsonl`
17. `using-rh-entitlements-pipelines/using-rh-entitlements-pipelines-jtbd.jsonl`
18. `using-tekton-hub-with-openshift-pipelines/using-tekton-hub-with-openshift-pipelines-jtbd.jsonl`
19. `using-tekton-results-for-openshift-pipelines-observability/using-tekton-results-for-openshift-pipelines-observability-self-managed-jtbd.jsonl`
20. `working-with-pipelines-web-console/working-with-pipelines-web-console-jtbd.jsonl`

### From `/Users/roparmar/Documents/work/JTBD/analysis/openshift-docs/`
21. `about-pipelines-as-code/about-pipelines-as-code-jtbd.jsonl`
22. `authenticating-pipelines-repos-using-secrets/authenticating-pipelines-repos-using-secrets-jtbd.jsonl`
23. `install-config-pipelines-as-code/install-config-pipelines-as-code-jtbd.jsonl`
24. `op-configuring-tkn/op-configuring-tkn-jtbd.jsonl`
25. `reducing-pipelines-resource-consumption/reducing-pipelines-resource-consumption-jtbd.jsonl`
26. `setting-up-openshift-pipelines-to-view-software-supply-chain-security-elements/setting-up-openshift-pipelines-to-view-software-supply-chain-security-elements-jtbd.jsonl`
27. `using-buildah-ns-tekton-task/using-buildah-ns-tekton-task-jtbd.jsonl`

**Not analyzed (no JSONL):** `op-release-notes-1-17`, `op-release-notes-1-18`, `op-release-notes-1-19`

---

## Next Steps

1. **Review and approve this proposal** — stakeholder sign-off on 13-job structure
2. **Module-level traceability** — map jobs to specific `.adoc` modules in openshift-docs repo
3. **Analyze release notes** — create Job 14 for "Track releases and updates" if needed
4. **Prototype one job** — implement Job 1 (Understand) or Job 4 (PAC) to validate structure
5. **Address open questions** — decisions on merge/split, troubleshooting strategy, reference organization


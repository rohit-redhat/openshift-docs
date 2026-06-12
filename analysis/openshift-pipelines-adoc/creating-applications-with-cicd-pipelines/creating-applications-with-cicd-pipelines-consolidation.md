# Creating CI/CD Solutions for Applications Using OpenShift Pipelines — Consolidation Report

**Document:** creating-applications-with-cicd-pipelines.adoc
**JTBD Records:** 14 records → 11 main jobs (after consolidation)

---

## Executive Summary

### What's Changing

The current documentation organizes content **sequentially by implementation steps**, presenting 13 flat sections that users must read in order to understand the CI/CD pipeline workflow. This linear structure obscures the logical relationships between concepts, buries optional configuration (like air-gapped deployment) mid-document, and separates related concerns (trigger setup, webhook configuration, and validation) into independent sections.

The proposed structure organizes content **by user goals and workflow stages**: Prepare Your Environment → Set Up & Configure → Deploy & Execute → Automate & Integrate → Track & Monitor → Filter & Secure. This approach groups related tasks under outcome-focused jobs, surfaces optional vs required steps through clear prerequisites, and reduces navigation overhead by consolidating scattered procedures into cohesive jobs.

The transformation reduces 13 sections to 11 main jobs with 35+ nested approaches, cutting top-level navigation items by 15% while improving discoverability through workflow-based organization.

### Key Improvements

- **Trigger automation consolidated:** 3 scattered sections (Adding triggers, Creating webhooks, Triggering pipeline run) → 3 focused jobs (Job 7: Configure, Job 8: Connect, Job 9: Validate) that show clear workflow progression
- **Air-gapped deployment surfaced:** Mirroring section buried mid-document → Job 5 in Configure stage with explicit timing guidance (BEFORE pipeline execution)
- **Security made explicit:** PR filtering/validation embedded in subsections → Job 11 with dedicated "Filter & Secure" stage
- **Monitoring elevated:** Single section at end → Job 10 in dedicated "Track & Monitor" stage
- **Prerequisites clarified:** Prerequisites scattered → Consolidated in Job 1 with clear dependency chains
- **Workflow stages visible:** Linear sections → 6 distinct stages (Prepare, Configure, Execute, Automate, Monitor, Secure) guide user journey

---

## Current Structure (Feature-Based)

- **Prerequisites** — Cluster access, Operator installation, CLI tools, forked Git repositories
- **Creating a project and checking your pipeline service account** — Namespace setup and service account verification
- **Creating pipeline tasks** — Installing apply-manifests and update-deployment tasks from pipelines-tutorial repository
- **Assembling a pipeline** — Defining build-and-deploy pipeline with 4 tasks (fetch-repository, build-image, apply-manifests, update-deployment)
- **Mirroring images to run pipelines in a restricted environment** — Mirroring Python, Golang, and CLI builder images for air-gapped clusters
  - 1. Mirror front-end Python builder image
  - 2. Mirror back-end Golang builder image
  - 3. Mirror CLI image
- **Running a pipeline** — Starting PipelineRun for back-end and front-end applications, tracking progress, verifying success
- **Adding triggers to a pipeline** — Creating TriggerBinding, TriggerTemplate, Trigger, and EventListener resources with HTTPS or HTTP routes
- **Configuring event listeners to serve many namespaces** — Multitenant EventListener setup with ClusterRole and ClusterRoleBinding
- **Creating webhooks** — Configuring webhook URLs in GitHub repositories pointing to EventListener service routes
- **Triggering a pipeline run** — Pushing empty commit to validate webhook and trigger automation
- **Enabling monitoring of event listeners for Triggers for user-defined projects** — Creating ServiceMonitor to collect EventListener metrics
- **Configuring pull request capabilities in GitHub Interceptor** — Overview of filtering and validation capabilities
  - **Filtering pull requests using GitHub Interceptor** — Using CEL Interceptor with changed_files property
  - **Validating pull requests using GitHub Interceptors** — Using OWNERS file with githubOwners parameter

**Total:** 13 sections (11 main + 2 nested), organized by implementation sequence.

---

## Proposed JTBD-Based Structure

### Quick Overview

- **Prepare Your Environment**
  - Job 1: Verify Prerequisites
  - Job 2: Create Project and Verify Service Accounts
  - Job 3: Install Reusable Pipeline Tasks
- **Set Up & Configure**
  - Job 4: Assemble a Pipeline
  - Job 5: Mirror Images for Restricted Environments
- **Deploy & Execute**
  - Job 6: Run a Pipeline
- **Automate & Integrate**
  - Job 7: Configure Pipeline Triggers
  - Job 8: Connect Git Repository Webhooks
  - Job 9: Validate Pipeline Automation
- **Track & Monitor**
  - Job 10: Monitor Event Listener Performance
- **Filter & Secure**
  - Job 11: Optimize and Secure Pull Request Triggers

---

### Detailed Job Descriptions

#### Prepare Your Environment

**Job 1: Verify Prerequisites**

*When starting a CI/CD pipeline project, I want to ensure my OpenShift cluster has the necessary components installed, so I can build pipelines without encountering environment issues.*

Prerequisites: Cluster access

- **1.1. Check Operator installation** `[procedure]`
  - Lines 81-87 (Prerequisites): Verify OpenShift Pipelines Operator installed via OperatorHub
  - Context: Operator must be cluster-wide before project creation

- **1.2. Verify CLI installation** `[procedure]`
  - Lines 81-87 (Prerequisites): Confirm tkn CLI available for command-line management

- **1.3. Prepare Git repositories** `[procedure]`
  - Lines 81-87 (Prerequisites): Fork pipelines-vote-ui and pipelines-vote-api with admin access

**Job 2: Create Project and Verify Service Accounts**

*When preparing to run pipelines, I want to create a dedicated project and verify the pipeline service account exists, so I can ensure proper isolation and permissions for my CI/CD workflows.*

Prerequisites: Cluster access, Pipelines Operator installed

- **2.1. Log in and create project** `[procedure]`
  - Lines 96-127 (Creating a project): oc login and oc new-project commands
  - Context: Namespace isolation for pipeline resources

- **2.2. Verify pipeline service account** `[procedure]`
  - Lines 96-127 (Creating a project): oc get serviceaccount pipeline
  - Context: Automatically created by Pipelines Operator with build/push permissions

**Job 3: Install Reusable Pipeline Tasks**

*When building a CI/CD pipeline, I want to install reusable tasks from existing repositories, so I can avoid reinventing the wheel and leverage proven pipeline components.*

Prerequisites: Project created

- **3.1. Install task resources** `[procedure]`
  - Lines 136-168 (Creating pipeline tasks): oc create from pipelines-tutorial repository
  - Tasks: apply-manifests, update-deployment

- **3.2. Verify task installation** `[procedure]`
  - Lines 136-168 (Creating pipeline tasks): tkn task list to confirm

---

#### Set Up & Configure

**Job 4: Assemble a Pipeline**

*When creating a CI/CD workflow, I want to assemble pipeline tasks into an executable flow with defined dependencies and workspaces, so I can automate the build and deployment process for my application.*

Prerequisites: Reusable tasks installed

- **4.1. Understand pipeline structure** `[concept]`
  - Lines 177-309 (Assembling a pipeline): Pipeline design, task interaction, workspaces, parameters
  - Context: Generic and reusable across applications

- **4.2. Define pipeline YAML** `[procedure]`
  - Lines 177-309 (Assembling a pipeline): build-and-deploy pipeline with 4 tasks
  - Task dependencies: fetch-repository → build-image → apply-manifests → update-deployment
  - Parameters: deployment-name, git-url, git-revision, IMAGE

- **4.3. Create pipeline resource** `[procedure]`
  - Lines 177-309 (Assembling a pipeline): oc create from local file or GitHub URL
  - Verification: tkn pipeline list

**Job 5: Mirror Images for Restricted Environments**

*When deploying pipelines in a disconnected or restricted cluster, I want to mirror required builder images to a private registry, so I can run pipelines without external internet access.*

Prerequisites: Pipeline assembled, mirror registry access

**Timing:** BEFORE Job 6 (pipeline execution) — images must be available before running pipelines

- **5.1. Mirror Python builder image** `[procedure]`
  - Lines 319-394 (Mirroring images): Mirror ubi9/python-39 for front-end (pipelines-vote-ui)
  - Steps: Verify tag not imported → Mirror to private registry → Import with --scheduled → Verify

- **5.2. Mirror Golang builder image** `[procedure]`
  - Lines 395-459 (Mirroring images): Mirror ubi9/go-toolset for back-end (pipelines-vote-api)
  - Same process as Python image

- **5.3. Mirror CLI image** `[procedure]`
  - Lines 460-521 (Mirroring images): Mirror ocp-v4.0-art-dev for CLI tools
  - Required for pipeline task execution

---

#### Deploy & Execute

**Job 6: Run a Pipeline**

*When ready to build and deploy my application, I want to start a pipeline run with specific parameters and track its progress, so I can see my code move from source to deployed application.*

Prerequisites: Pipeline assembled

- **6.1. Start back-end pipeline** `[procedure]`
  - Lines 546-558 (Running a pipeline): tkn pipeline start build-and-deploy
  - Parameters: deployment-name=pipelines-vote-api, git-url, IMAGE
  - Workspace: volumeClaimTemplateFile for persistent storage

- **6.2. Track pipeline progress** `[procedure]`
  - Lines 560-568 (Running a pipeline): tkn pipelinerun logs <pipelinerun_id> -f
  - Context: Real-time log following

- **6.3. Start front-end pipeline** `[procedure]`
  - Lines 569-579 (Running a pipeline): Same process with deployment-name=pipelines-vote-ui

- **6.4. Verify pipeline success** `[procedure]`
  - Lines 590-613 (Running a pipeline): tkn pipelinerun list, check Succeeded status, get application route
  - Validation: Access deployed application via route URL

- **6.5. Rerun last pipeline** `[procedure]`
  - Lines 615-620 (Running a pipeline): tkn pipeline start build-and-deploy --last
  - Context: Reuses resources and service account from previous run

---

#### Automate & Integrate

**Job 7: Configure Pipeline Triggers**

*When automating CI/CD workflows, I want to configure triggers that respond to GitHub events, so I can automatically build and deploy my application when code changes occur.*

Prerequisites: Pipeline successfully run

- **7.1. Create TriggerBinding** `[procedure]`
  - Lines 643-673 (Adding triggers): Extract parameters from webhook payload
  - Extracts: git-repo-url, git-repo-name, git-revision

- **7.2. Create TriggerTemplate** `[procedure]`
  - Lines 675-737 (Adding triggers): Define PipelineRun template with volumeClaimTemplate
  - Context: volumeClaimTemplate eliminates need for pre-created PVC

- **7.3. Create Trigger resource** `[procedure]`
  - Lines 739-767 (Adding triggers): Link TriggerBinding and TriggerTemplate

- **7.4. Create EventListener with secure HTTPS** `[procedure]`
  - Lines 801-860 (Adding triggers): Label namespace → Create EventListener → Create re-encrypt TLS route
  - Context: Recommended for production environments

- **7.5. Create EventListener with HTTP (alternative)** `[procedure]`
  - Lines 862-870 (Adding triggers): Create EventListener → Expose service
  - Context: Simpler but insecure, acceptable for development

- **7.6. Configure multitenant EventListener (optional)** `[procedure]`
  - Lines 880-1027 (Configuring event listeners): ClusterRole, ClusterRoleBinding, ServiceAccount, namespaceSelector
  - Context: For organizations managing pipelines across multiple namespaces

**Job 8: Connect Git Repository Webhooks**

*When connecting Git repositories to pipelines, I want to configure webhook URLs pointing to EventListener routes, so I can receive notifications when repository events occur.*

Prerequisites: EventListener created, Git repository admin access

- **8.1. Get webhook URL** `[procedure]`
  - Lines 1054-1068 (Creating webhooks): oc get route el-vote-app for HTTPS or HTTP URL

- **8.2. Configure front-end webhook** `[procedure]`
  - Lines 1070-1082 (Creating webhooks): GitHub Settings → Webhooks → Add Webhook
  - Configuration: Payload URL, Content type (application/json), Secret, Event (push), Active

- **8.3. Configure back-end webhook** `[procedure]`
  - Line 1083 (Creating webhooks): Repeat for pipelines-vote-api repository

**Job 9: Validate Pipeline Automation**

*When validating my CI/CD automation, I want to push a code change and verify it triggers a pipeline run, so I can confirm my webhooks and triggers are working correctly.*

Prerequisites: Webhooks configured

- **9.1. Clone forked repository** `[procedure]`
  - Lines 1105-1110 (Triggering a pipeline run): git clone with branch specification

- **9.2. Push empty commit** `[procedure]`
  - Lines 1111-1116 (Triggering a pipeline run): git commit --allow-empty && git push
  - Context: Tests webhook without actual code changes

- **9.3. Verify pipeline triggered** `[procedure]`
  - Lines 1117-1123 (Triggering a pipeline run): tkn pipelinerun list shows new run
  - Validation: Confirm event initiated pipeline

---

#### Track & Monitor

**Job 10: Monitor Event Listener Performance**

*When operating CI/CD pipelines in production, I want to monitor event listener metrics and performance, so I can track webhook delivery, event processing, and resource creation.*

Prerequisites: EventListener deployed, monitoring enabled for user-defined projects

- **10.1. Create ServiceMonitor** `[procedure]`
  - Lines 1149-1177 (Enabling monitoring): ServiceMonitor YAML with labels and endpoints
  - Metrics collected: eventlistener_http_duration_seconds, eventlistener_event_count, eventlistener_triggered_resources

- **10.2. Test metrics collection** `[procedure]`
  - Lines 1179-1186 (Enabling monitoring): Push commit → Navigate to Administrator → Observe → Metrics
  - Search: eventlistener_http_resources keyword

---

#### Filter & Secure

**Job 11: Optimize and Secure Pull Request Triggers**

*When managing pull request workflows, I want to filter events based on changed files and validate based on repository ownership, so I can minimize unnecessary pipeline runs and prevent unauthorized execution.*

Prerequisites: Triggers configured

- **11.1. Understand GitHub Interceptor capabilities** `[concept]`
  - Lines 1200-1212 (Configuring pull request capabilities): Overview of filtering and validation
  - Capabilities: Filter by changed files, Validate by repository ownership

- **11.2. Filter by changed files (public repository)** `[procedure]`
  - Lines 1234-1267 (Filtering pull requests): Set addChangedFiles.enabled=true, use CEL Interceptor
  - Example: extensions.changed_files.matches('controllers/')
  - Context: Run pipelines only when relevant files change

- **11.3. Filter by changed files (private repository)** `[procedure]`
  - Lines 1269-1306 (Filtering pull requests): Same as public with personalAccessToken secret
  - Additional: secretName and secretKey for authentication

- **11.4. Validate by ownership (public repository)** `[procedure]`
  - Lines 1334-1368 (Validating pull requests): Create OWNERS file → Enable githubOwners parameter → Set checkType
  - checkType options: none, orgMembers, repoMembers, all
  - Context: Prevents unauthorized pipeline execution from external contributors

- **11.5. Validate by ownership (private repository)** `[procedure]`
  - Lines 1370-1407 (Validating pull requests): Same as public with personalAccessToken
  - Requires: /ok-to-test comment from repository owner for external PRs

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | Sequential implementation steps | User goals and workflow stages |
| **Top-level items** | 13 flat sections | 11 main jobs with 35+ nested approaches |
| **Trigger setup** | Single "Adding triggers" section with all resources | Job 7 (6 approaches) for trigger configuration |
| **Webhook configuration** | Separate "Creating webhooks" section | Job 8 (3 approaches) under Automate & Integrate stage |
| **Validation** | "Triggering a pipeline run" isolated at end | Job 9 (3 approaches) completing Automate workflow |
| **Monitoring** | Single section at end | Dedicated "Track & Monitor" stage with Job 10 |
| **Security** | Nested subsections under PR configuration | Explicit "Filter & Secure" stage with Job 11 |
| **Air-gapped deployment** | Buried mid-document (section 4 of 13) | Job 5 with clear timing (BEFORE execution) |
| **Multitenant setup** | Embedded in triggers section | Optional approach 7.6 under Job 7 |
| **Navigation** | Linear reading required | Goal-directed, jump to specific job |

### Job List Adjustments from Suggested Input

The suggested 14 records were consolidated to **11 jobs** for the following reasons:

1. **Record "Configuring pull request capabilities in GitHub Interceptor" (concept)** merged into Job 11 as approach 11.1 → Concept introduction becomes first step of optimization/security job
2. **Records "Filtering pull requests using GitHub Interceptor" and "Validating pull requests using GitHub Interceptors"** absorbed into Job 11 as approaches 11.2-11.5 → Related capabilities presented as unified job for managing PR triggers
3. **Record "Configuring event listeners to serve many namespaces"** dissolved as standalone job → Reassigned as optional approach 7.6 under Job 7 (Configure Pipeline Triggers) because multitenant setup is configuration variant, not separate goal

---

## Consolidation Examples

### Example 1: Trigger Automation (3 sections → 3 coordinated jobs)

**Current (Fragmented):**
- Section 7: "Adding triggers to a pipeline" (TriggerBinding, TriggerTemplate, Trigger, EventListener)
- Section 9: "Creating webhooks" (Git repository configuration)
- Section 10: "Triggering a pipeline run" (Validation with empty commit)

Users must read three independent sections to understand the complete automation workflow. Relationship between trigger resources, webhooks, and validation is implicit.

**Proposed (Consolidated):**
- **Job 7: Configure Pipeline Triggers**
  - 7.1-7.6: TriggerBinding, TriggerTemplate, Trigger, EventListener (all trigger resources)
- **Job 8: Connect Git Repository Webhooks**
  - 8.1-8.3: Webhook URL extraction and GitHub configuration
- **Job 9: Validate Pipeline Automation**
  - 9.1-9.3: Clone, push, verify (end-to-end testing)

Grouped under **Automate & Integrate** stage, showing clear progression: Configure triggers → Connect webhooks → Validate automation.

**Benefit:** Users see the logical workflow from trigger setup through validation. Each job has clear prerequisites and builds on the previous job.

---

### Example 2: Air-Gapped Deployment (1 buried section → Positioned job with timing)

**Current (Buried):**
- Section 4 of 13: "Mirroring images to run pipelines in a restricted environment"
- Located after pipeline assembly, before pipeline execution
- No explicit timing guidance on when mirroring is required

Users scanning the document may skip this section if title doesn't match their environment. Air-gapped users discover requirement too late.

**Proposed (Contextualized):**
- **Job 5: Mirror Images for Restricted Environments**
  - Positioned in **Set Up & Configure** stage after Job 4 (Assemble Pipeline)
  - **Timing:** BEFORE Job 6 (Run a Pipeline) — images must be available before execution
  - **Prerequisites:** Pipeline assembled, mirror registry access
  - Clear signal: Optional for connected environments, required for air-gapped

**Benefit:** Air-gapped users immediately see timing and prerequisites. Connected-environment users can skip without reading detailed procedures.

---

### Example 3: Security (2 nested subsections → Integrated security job)

**Current (Fragmented):**
- Section 12: "Configuring pull request capabilities in GitHub Interceptor" (concept overview)
  - Subsection 12.1: "Filtering pull requests using GitHub Interceptor" (optimization)
  - Subsection 12.2: "Validating pull requests using GitHub Interceptors" (security)

Filtering (optimization) and validation (security) presented as independent capabilities. No connection to broader security concerns.

**Proposed (Integrated):**
- **Job 11: Optimize and Secure Pull Request Triggers**
  - 11.1: Understand capabilities (concept)
  - 11.2-11.3: Filter by changed files (optimization reduces compute costs)
  - 11.4-11.5: Validate by ownership (security prevents unauthorized execution)
  - Placed in dedicated **Filter & Secure** stage

**Benefit:** Users see filtering and validation as complementary capabilities under unified security/optimization goal. Security concerns elevated to stage level.

---

## Content Gaps Identified

| Gap | JTBD Reference | Current Coverage | Impact |
|-----|---------------|-----------------|--------|
| Troubleshooting failed pipelines | Jobs 6, 7, 9 | None | **High** — Users have no guidance for debugging task failures, webhook delivery issues, or trigger problems |
| Debugging webhook delivery | Job 8 | None | **High** — No procedures for checking webhook delivery status, examining payloads, or troubleshooting GitHub connectivity |
| Pipeline upgrade procedures | Jobs 4, 6 | None | **Medium** — No guidance for upgrading pipelines to new Tekton versions or migrating task definitions |
| Decision guidance for HTTPS vs HTTP | Job 7 (approach 7.4 vs 7.5) | Brief context only | **Medium** — No detailed comparison of security, certificate management, or performance trade-offs |
| Multitenant vs single-tenant decision matrix | Job 7 (approach 7.6) | Brief note only | **Medium** — No guidance on when to use multitenant EventListeners vs dedicated per-namespace |
| Performance tuning for pipelines | Job 6 | None | **Low** — No guidance on workspace sizing, parallel task execution, or resource optimization |
| Cost optimization strategies | Jobs 5, 6, 11 | None | **Low** — No discussion of compute costs for pipelines, storage costs for workspaces, or filtering to reduce runs |
| Rollback procedures | Job 6 | None | **Medium** — No guidance for rolling back deployments after failed pipeline runs |

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 13 sections | 11 jobs | 15% reduction |
| Sections to browse for "automate triggers" | 3 sections (7, 9, 10) across document | 3 jobs (7, 8, 9) in Automate stage | Grouped under stage, ~50% faster discovery |
| Sections to browse for "securing pipelines" | 2 nested sections (12.1, 12.2) | 1 job (11) in Filter & Secure stage | Direct access to security content |
| Clicks to find "air-gapped deployment" | Scan 13 sections, find at position 4 | Navigate to Set Up & Configure → Job 5 | ~60% faster |
| Clicks to find "monitoring" | Scroll to section 11 of 13 | Navigate to Track & Monitor → Job 10 | Direct stage access |
| Clicks to find "prerequisites" | Read section 1, extract from subsequent sections | Navigate to Prepare → Job 1 | Consolidated in single job |

**Final job count: 11** (reduced from 14 records, 13 sections). Consolidation rationale: Concept records merged into parent jobs, optional configuration variants nested as approaches rather than standalone jobs, related capabilities grouped under unified goals.

---

## Document Statistics

**Workflow Coverage:**
- Prepare: 3 jobs (Prerequisites, Project, Tasks)
- Configure: 5 jobs (Pipeline, Mirroring, Triggers, Webhooks, PR filtering/validation)
- Execute: 2 jobs (Running, Validation)
- Monitor: 1 job (Event listener metrics)
- Secure: 1 job (shared with Filter in Job 11)
- Troubleshoot: **Gap identified** (no content)
- Upgrade: **Gap identified** (no content)

**Main Jobs:** 11
**User Stories/Paths:** 35+ (nested approaches)
**Source Sections:** 13 modules included in assembly
**Platform/Tool Variations:** Air-gapped vs connected, HTTPS vs HTTP, public vs private repositories, multitenant vs single-tenant

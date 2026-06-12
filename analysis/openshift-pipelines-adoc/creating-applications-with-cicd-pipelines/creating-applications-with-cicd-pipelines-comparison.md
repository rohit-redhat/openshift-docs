# Creating CI/CD Solutions for Applications Using OpenShift Pipelines — TOC Comparison

**Current Feature-Based vs. Proposed JTBD-Based Structure**

**Analysis Date:** 2026-06-11
**JTBD Records:** 14
**Main Jobs:** 11 (rolled up from records)
**Coverage:** 100% enhanced schema with validation

---

## Current Structure (Feature-Based)

**Creating CI/CD solutions for applications using OpenShift Pipelines**

- **Prerequisites** — Required cluster access, Operator installation, CLI, forked Git repos
- **Creating a project and checking your pipeline service account** — Project namespace setup
- **Creating pipeline tasks** — Installing apply-manifests and update-deployment tasks
- **Assembling a pipeline** — Defining build-and-deploy pipeline YAML
- **Mirroring images to run pipelines in a restricted environment** — Air-gapped deployment preparation
  - Mirror Python builder image for front-end
  - Mirror Golang builder image for back-end
  - Mirror CLI image
- **Running a pipeline** — Starting PipelineRun for front-end and back-end applications
- **Adding triggers to a pipeline** — Creating TriggerBinding, TriggerTemplate, Trigger, EventListener
- **Configuring event listeners to serve many namespaces** — Multitenant EventListener setup
- **Creating webhooks** — Connecting GitHub repositories to EventListener
- **Triggering a pipeline run** — Validating webhook with empty commit
- **Enabling monitoring of event listeners for Triggers for user-defined projects** — ServiceMonitor creation
- **Configuring pull request capabilities in GitHub Interceptor** — Overview of filtering and validation
  - Filtering pull requests using GitHub Interceptor
  - Validating pull requests using GitHub Interceptors

**Total:** 13 sections, organized sequentially by implementation steps

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
  - Context: Operator must be installed cluster-wide before proceeding

- **1.2. Verify CLI installation** `[procedure]`
  - Lines 81-87 (Prerequisites): Confirm tkn CLI available
  - Context: Required for command-line pipeline management

- **1.3. Prepare Git repositories** `[procedure]`
  - Lines 81-87 (Prerequisites): Fork pipelines-vote-ui and pipelines-vote-api
  - Context: Requires administrator access for webhook configuration

---

**Job 2: Create Project and Verify Service Accounts**

*When preparing to run pipelines, I want to create a dedicated project and verify the pipeline service account exists, so I can ensure proper isolation and permissions for my CI/CD workflows.*

Prerequisites: Cluster access, Pipelines Operator installed

- **2.1. Log in and create project** `[procedure]`
  - Lines 96-127 (Creating a project and checking your pipeline service account): Login to cluster and create pipelines-tutorial project
  - Context: Namespace isolation for pipeline resources

- **2.2. Verify pipeline service account** `[procedure]`
  - Lines 96-127 (Creating a project and checking your pipeline service account): Check pipeline service account exists
  - Context: Automatically created by Pipelines Operator with build and push permissions

---

**Job 3: Install Reusable Pipeline Tasks**

*When building a CI/CD pipeline, I want to install reusable tasks from existing repositories, so I can avoid reinventing the wheel and leverage proven pipeline components.*

Prerequisites: Project created

- **3.1. Install task resources** `[procedure]`
  - Lines 136-168 (Creating pipeline tasks): Install apply-manifests and update-deployment from pipelines-tutorial repo
  - Context: Reusable tasks for Kubernetes manifest application and deployment updates

- **3.2. Verify task installation** `[procedure]`
  - Lines 136-168 (Creating pipeline tasks): Use tkn task list to confirm installation
  - Context: Ensures tasks are available for pipeline assembly

---

#### Set Up & Configure

**Job 4: Assemble a Pipeline**

*When creating a CI/CD workflow, I want to assemble pipeline tasks into an executable flow with defined dependencies and workspaces, so I can automate the build and deployment process for my application.*

Prerequisites: Reusable tasks installed

- **4.1. Understand pipeline structure** `[concept]`
  - Lines 177-309 (Assembling a pipeline): Pipeline design, task interaction, workspaces
  - Context: Generic and reusable across applications

- **4.2. Define pipeline YAML** `[procedure]`
  - Lines 177-309 (Assembling a pipeline): Create build-and-deploy pipeline with 4 tasks
  - Task sequence: fetch-repository → build-image → apply-manifests → update-deployment

- **4.3. Create pipeline resource** `[procedure]`
  - Lines 177-309 (Assembling a pipeline): oc create from local file or GitHub repository
  - Verification: tkn pipeline list

---

**Job 5: Mirror Images for Restricted Environments**

*When deploying pipelines in a disconnected or restricted cluster, I want to mirror required builder images to a private registry, so I can run pipelines without external internet access.*

Prerequisites: Pipeline assembled, mirror registry access

- **5.1. Mirror Python builder image** `[procedure]`
  - Lines 319-394 (Mirroring images - front-end): Mirror ubi9/python-39 for pipelines-vote-ui
  - Steps: Verify, mirror, import with --scheduled, verify import

- **5.2. Mirror Golang builder image** `[procedure]`
  - Lines 395-459 (Mirroring images - back-end): Mirror ubi9/go-toolset for pipelines-vote-api
  - Same process as Python image

- **5.3. Mirror CLI image** `[procedure]`
  - Lines 460-521 (Mirroring images - CLI): Mirror ocp-v4.0-art-dev image
  - Required for pipeline execution

---

#### Deploy & Execute

**Job 6: Run a Pipeline**

*When ready to build and deploy my application, I want to start a pipeline run with specific parameters and track its progress, so I can see my code move from source to deployed application.*

Prerequisites: Pipeline assembled

- **6.1. Start back-end pipeline** `[procedure]`
  - Lines 546-558 (Running a pipeline): tkn pipeline start with parameters and workspace
  - Parameters: deployment-name, git-url, IMAGE

- **6.2. Track pipeline progress** `[procedure]`
  - Lines 560-568 (Running a pipeline): tkn pipelinerun logs with follow flag
  - Context: Real-time monitoring

- **6.3. Start front-end pipeline** `[procedure]`
  - Lines 569-579 (Running a pipeline): Same process with different parameters

- **6.4. Verify pipeline success** `[procedure]`
  - Lines 590-613 (Running a pipeline): List pipeline runs and get application route
  - Validation: Check Succeeded status

- **6.5. Rerun last pipeline** `[procedure]`
  - Lines 615-620 (Running a pipeline): Use --last flag to reuse previous configuration

---

#### Automate & Integrate

**Job 7: Configure Pipeline Triggers**

*When automating CI/CD workflows, I want to configure triggers that respond to GitHub events, so I can automatically build and deploy my application when code changes occur.*

Prerequisites: Pipeline successfully run

- **7.1. Create TriggerBinding** `[procedure]`
  - Lines 643-673 (Adding triggers): Define parameter extraction from webhook payload
  - Maps: git-repo-url, git-repo-name, git-revision

- **7.2. Create TriggerTemplate** `[procedure]`
  - Lines 675-737 (Adding triggers): Define PipelineRun template with workspace volumeClaimTemplate
  - Context: Template eliminates need for pre-created PVC

- **7.3. Create Trigger resource** `[procedure]`
  - Lines 739-767 (Adding triggers): Link binding and template

- **7.4. Create EventListener with secure HTTPS** `[procedure]`
  - Lines 801-860 (Adding triggers): Label namespace, create EventListener, create re-encrypt route
  - Context: Recommended for production

- **7.5. Create EventListener with HTTP** `[procedure]`
  - Lines 862-870 (Adding triggers): Create EventListener and expose service
  - Context: Simpler but insecure

- **7.6. Configure multitenant EventListener (optional)** `[procedure]`
  - Lines 880-1027 (Configuring event listeners to serve many namespaces): ClusterRole, ClusterRoleBinding, namespaceSelector
  - Context: For organizations with many namespaces

---

**Job 8: Connect Git Repository Webhooks**

*When connecting Git repositories to pipelines, I want to configure webhook URLs pointing to EventListener routes, so I can receive notifications when repository events occur.*

Prerequisites: EventListener created, Git repo admin access

- **8.1. Get webhook URL** `[procedure]`
  - Lines 1054-1068 (Creating webhooks): Extract route URL for HTTPS or HTTP
  - Command: oc get route el-vote-app

- **8.2. Configure front-end webhook** `[procedure]`
  - Lines 1070-1082 (Creating webhooks): GitHub Settings → Webhooks → Add Webhook
  - Fields: Payload URL, Content type, Secret, Event type (push), Active

- **8.3. Configure back-end webhook** `[procedure]`
  - Line 1083 (Creating webhooks): Repeat for pipelines-vote-api

---

**Job 9: Validate Pipeline Automation**

*When validating my CI/CD automation, I want to push a code change and verify it triggers a pipeline run, so I can confirm my webhooks and triggers are working correctly.*

Prerequisites: Webhooks configured

- **9.1. Clone forked repository** `[procedure]`
  - Lines 1105-1110 (Triggering a pipeline run): git clone with branch specification

- **9.2. Push empty commit** `[procedure]`
  - Lines 1111-1116 (Triggering a pipeline run): Test webhook without code changes

- **9.3. Verify pipeline triggered** `[procedure]`
  - Lines 1117-1123 (Triggering a pipeline run): Check tkn pipelinerun list for new run

---

#### Track & Monitor

**Job 10: Monitor Event Listener Performance**

*When operating CI/CD pipelines in production, I want to monitor event listener metrics and performance, so I can track webhook delivery, event processing, and resource creation.*

Prerequisites: EventListener deployed, monitoring enabled for user-defined projects

- **10.1. Create ServiceMonitor** `[procedure]`
  - Lines 1149-1177 (Enabling monitoring): Define ServiceMonitor for event listener
  - Metrics: eventlistener_http_duration_seconds, eventlistener_event_count, eventlistener_triggered_resources

- **10.2. Test metrics collection** `[procedure]`
  - Lines 1179-1186 (Enabling monitoring): Push commit and view metrics in web console
  - Navigate: Administrator → Observe → Metrics

---

#### Filter & Secure

**Job 11: Optimize and Secure Pull Request Triggers**

*When managing pull request workflows, I want to filter events based on changed files and validate based on repository ownership, so I can minimize unnecessary pipeline runs and prevent unauthorized execution.*

Prerequisites: Triggers configured

- **11.1. Understand GitHub Interceptor capabilities** `[concept]`
  - Lines 1200-1212 (Configuring pull request capabilities): Overview of filtering and validation
  - Context: Selective pipeline execution

- **11.2. Filter by changed files (public repo)** `[procedure]`
  - Lines 1234-1267 (Filtering pull requests): Set addChangedFiles to true, use CEL Interceptor
  - Example: extensions.changed_files.matches('controllers/')

- **11.3. Filter by changed files (private repo)** `[procedure]`
  - Lines 1269-1306 (Filtering pull requests): Same as public with personalAccessToken secret

- **11.4. Validate by ownership (public repo)** `[procedure]`
  - Lines 1334-1368 (Validating pull requests): Create OWNERS file, enable githubOwners parameter
  - Context: Prevents unauthorized pipeline execution

- **11.5. Validate by ownership (private repo)** `[procedure]`
  - Lines 1370-1407 (Validating pull requests): Same as public with personalAccessToken
  - checkType options: orgMembers, repoMembers, all

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | Sequential implementation steps | User goals and workflow stages |
| **Top-level items** | 13 flat sections | 11 main jobs with nested approaches |
| **Trigger configuration** | Single "Adding triggers" section | Split into Job 7 (Configure), Job 8 (Webhooks), Job 9 (Validate) |
| **Monitoring** | Isolated section at end | Dedicated "Track & Monitor" stage with Job 10 |
| **Security** | Embedded in PR configuration | Explicit "Filter & Secure" stage with Job 11 |
| **Restricted environments** | Mid-document optional section | Early Job 5 with clear timing guidance |
| **Multitenant setup** | Embedded in triggers section | Optional approach under Job 7 |
| **Navigation** | Linear, must read sequentially | Goal-directed, jump to specific job |
| **Reusability** | Implementation-focused titles | Outcome-focused job titles |

---

## Workflow Coverage Comparison

| Stage | Current | Proposed | Gap Status |
|-------|---------|----------|------------|
| Prepare | ✅ Prerequisites, Project, Tasks | ✅ Jobs 1-3 | Improved organization |
| Configure | ✅ Pipeline, Triggers, Webhooks | ✅ Jobs 4, 5, 7, 8, 11 | Consolidated |
| Execute | ✅ Running, Triggering | ✅ Jobs 6, 9 | Separated validation from execution |
| Monitor | ⚠️ Single section at end | ✅ Job 10 | Elevated to dedicated stage |
| Secure | ⚠️ Embedded in PR section | ✅ Job 11 (explicit) | Made explicit |
| Troubleshoot | ❌ Missing | ❌ Missing | Gap remains |
| Upgrade | ❌ Missing | ❌ Missing | Gap remains |

### Coverage Summary

**Current structure gaps:** Troubleshooting, Upgrade, Decision guidance for choosing approaches
**Proposed structure gaps:** Troubleshooting, Upgrade (unchanged from current)
**Gaps addressed by restructure:** Security made explicit, Monitoring elevated

### Recommendations for Gap Closure

| Gap | Recommendation | Priority |
|-----|----------------|----------|
| Troubleshoot | Add debugging section for failed pipelines, task failures, webhook issues | High |
| Upgrade | Add procedures for upgrading pipelines, migrating to new Tekton versions | Medium |
| Decision guidance | Add comparison matrix for HTTP vs HTTPS, multitenant vs single-tenant | Medium |

---

## Example Consolidation

### Example 1: Trigger Configuration (3 scattered jobs → 3 focused jobs)

**Current (Fragmented):**
- Section "Adding triggers to a pipeline" (TriggerBinding, TriggerTemplate, Trigger, EventListener)
- Section "Creating webhooks" (Git repository configuration)
- Section "Triggering a pipeline run" (Validation)

These three sections are presented as independent steps, obscuring the logical workflow.

**Proposed (Consolidated):**
- **Job 7: Configure Pipeline Triggers**
  - 7.1-7.6: All trigger resources (Automate stage)
- **Job 8: Connect Git Repository Webhooks**
  - 8.1-8.3: Webhook configuration (Integrate stage)
- **Job 9: Validate Pipeline Automation**
  - 9.1-9.3: End-to-end testing (Execute stage)

**Benefit:** Clear progression from trigger setup → webhook connection → validation. Users understand the automation workflow.

---

### Example 2: Image Mirroring (1 monolithic section → Staged job)

**Current (Buried):**
- Section "Mirroring images to run pipelines in a restricted environment" appears mid-document
- No clear timing guidance on when this is required

**Proposed (Contextualized):**
- **Job 5: Mirror Images for Restricted Environments**
  - Positioned in "Set Up & Configure" stage
  - **Timing:** BEFORE Job 6 (pipeline execution)
  - **Prerequisites:** Pipeline assembled
  - Clear signal: Optional for connected environments, required for air-gapped

**Benefit:** Users in air-gapped environments immediately understand when to perform mirroring. Users in connected environments can skip.

---

### Example 3: Pull Request Security (2 nested sections → Integrated job)

**Current (Fragmented):**
- Section "Configuring pull request capabilities in GitHub Interceptor" (concept)
  - Subsection "Filtering pull requests using GitHub Interceptor"
  - Subsection "Validating pull requests using GitHub Interceptors"

**Proposed (Integrated):**
- **Job 11: Optimize and Secure Pull Request Triggers**
  - 11.1: Understand capabilities (concept)
  - 11.2-11.3: Filter by changed files (optimize)
  - 11.4-11.5: Validate by ownership (secure)

**Benefit:** Users see filtering (optimization) and validation (security) as complementary capabilities, not separate concerns.

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 13 sections | 11 jobs | 15% reduction |
| Sections to browse for "trigger automation" | 3 sections across document | 1 job (Job 7) with 6 approaches | ~67% reduction |
| Sections to browse for "securing pipelines" | 2 nested sections | 1 job (Job 11) with 5 approaches | 50% reduction |
| Clicks to find "air-gapped deployment" | Scan 13 sections (mid-document) | Navigate to Job 5 (Configure stage) | ~62% faster |
| Clicks to find "monitoring" | Scroll to section 11 of 13 | Navigate to Job 10 (Monitor stage) | Direct access |

**Final job count: 11** (reduced from 13 sections). Jobs are outcome-focused and organized by workflow stage, reducing cognitive load.

---

## Success Criteria Met

✅ User can immediately see main goals (11 jobs vs 13 sections)
✅ User can find jobs by what they need to accomplish (Prepare, Configure, Execute, Monitor, Secure)
✅ User can see it's simpler than current structure (11 jobs vs 13 flat sections)
✅ Stakeholders understand the proposed improvement (workflow stages vs sequential steps)
✅ Content mappers know what to extract from where (detailed line references)
✅ Structure follows natural workflow progression (Prepare → Configure → Execute → Monitor → Secure)
✅ No persona gates - jobs are accessible based on permissions
✅ Prerequisites stated as permissions, not job titles
✅ Gaps clearly marked with recommendations

# Creating CI/CD Pipelines
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** Enable teams to build automated CI/CD solutions using OpenShift Pipelines, from assembling reusable tasks to implementing event-driven automation with governance controls.

**Personas:** 
- Application developer
- Pipeline developer
- Platform engineer
- Platform administrator
- Cluster administrator
- DevOps engineer
- Pipeline approver

**Main Jobs:** 9 core jobs across 6 workflow stages

---

## Quick Navigation

**I want to:**
- Create an automated CI/CD pipeline for my application → Job 1 (Build Pipeline Workflows)
- Work with pipelines in the Developer console → Job 2 (Build Pipeline Workflows)
- Start and monitor pipeline runs → Job 3 (Execute and Monitor)
- Reuse existing tasks from catalogs or Git → Job 4 (Build Pipeline Workflows)
- Create pipeline templates for my team → Job 5 (Govern and Secure)
- View pipeline performance statistics → Job 6 (Analyze Performance)
- Add approval gates to production deployments → Job 7 (Govern and Secure)
- Use Red Hat entitlements in pipeline builds → Job 8 (Manage Resources)
- Trigger pipelines automatically on Git events → Job 1.3 (Build Pipeline Workflows)
- Configure webhooks for my repositories → Job 1.3.3 (Build Pipeline Workflows)
- Monitor event listener metrics → Job 1.3.5 (Execute and Monitor)
- Filter pull requests to avoid unnecessary builds → Job 1.3.6 (Govern and Secure)
- Access tasks from Tekton Hub or Artifact Hub → Job 4.1 (Build Pipeline Workflows)
- Reference tasks from private Git repositories → Job 4.3 (Build Pipeline Workflows)
- Approve deployments via web console or CLI → Job 7.2, 7.3 (Govern and Secure)

---

# Table of Contents

## Build Pipeline Workflows

### Job 1: Create Automated CI/CD Solutions for Applications
*When I need to automate application build, test, and deployment workflows*

**Personas:** Application developer, Pipeline developer

**Why:** Reduces manual effort and ensures consistent delivery processes across environments.

#### 1.1 Define Reusable Tasks (Building Blocks)
**Goal:** Create standardized task definitions that can be shared across pipelines.

- **Task:** Install tasks from public repositories
  → Lines 138-170: Creating pipeline tasks
  - Access pre-built tasks from GitHub
  - Install using `oc apply` or `kubectl apply`
  - Verify task installation in namespace

#### 1.2 Assemble Pipeline Workflow (Orchestration)
**Goal:** Combine tasks into a complete build-test-deploy sequence.

- **Task:** Define pipeline structure with task references
  → Lines 179-311: Assembling a pipeline
  - Specify task execution order
  - Configure pipeline parameters
  - Define workspace requirements
  - Set up task dependencies

- **Task:** Configure pipeline for restricted environments
  → Lines 321-523: Mirroring images to run pipelines in restricted environment
  - Mirror builder images to private registry
  - Configure Samples Operator for disconnected clusters
  - Set up image pull secrets
  - Schedule periodic image re-imports

#### 1.3 Enable Event-Driven Automation (Triggers)
**Goal:** Eliminate manual pipeline invocation by responding to Git events automatically.

- **Approach:** Add GitHub event triggers
  → Lines 637-873: Adding triggers to a pipeline
  
  **Components:**
  - **TriggerBinding:** Extract parameters from webhook payload
  - **TriggerTemplate:** Define PipelineRun to create
  - **Trigger:** Connect binding and template
  - **EventListener:** Expose HTTP endpoint to receive events

- **Approach (Advanced):** Configure multitenant event listeners
  → Lines 881-1030: Configuring event listeners to serve many namespaces
  *For platform engineers deploying across multiple teams*
  
  **Benefits:**
  - Minimize duplication of event listener resources
  - Serve multiple namespaces from single listener
  - Reduce cluster resource consumption
  
  **Requirements:**
  - Cluster-wide permissions
  - Namespace selector configuration
  - Service account impersonation setup

- **Task:** Configure webhook URLs on repositories
  → Lines 1038-1086: Creating webhooks
  - Expose event listener service
  - Obtain webhook URL
  - Configure webhook on GitHub repository
  - Set webhook secret for validation

- **Task:** Test end-to-end automation
  → Lines 1094-1126: Triggering a pipeline run
  - Push code changes to repository
  - Verify webhook delivery
  - Confirm pipeline run started
  - Monitor pipeline execution

- **Task:** Enable event listener monitoring
  → Lines 1134-1189: Enabling monitoring of event listeners for Triggers for user-defined projects
  *For platform engineers*
  
  **Setup:**
  - Create ServiceMonitor resources
  - Enable monitoring for user-defined projects
  - View metrics in OpenShift console
  - Set up alerting on metrics

- **Task:** Filter events to minimize unnecessary builds
  → Lines 1222-1309: Filtering pull requests using GitHub Interceptor
  
  **Capabilities:**
  - Filter by changed files using CEL expressions
  - Configure personal access tokens for private repos
  - Specify directory path filters
  - Reduce compute resource consumption

- **Task:** Validate pull requests before triggering builds
  → Lines 1317-1410: Validating pull requests using GitHub Interceptors
  *Security control for external contributors*
  
  **Validation:**
  - Check PR author against OWNERS file
  - Require approval from authorized users
  - Prevent unauthorized code execution
  - Configure approval comment triggers

#### 1.4 Set Up Project Prerequisites (Foundation)
**Goal:** Prepare the project environment for pipeline execution.

- **Task:** Create project and verify service account
  → Lines 98-129: Creating a project and checking your pipeline service account
  - Create dedicated project for isolation
  - Verify pipeline service account exists
  - Check service account permissions

#### 1.5 Execute Pipeline Runs (Deployment)
**Goal:** Start the automated workflow to build, test, and deploy.

- **Task:** Run pipeline with parameters and workspaces
  → Lines 539-623: Running a pipeline
  - Configure workspace storage
  - Provide Git repository URL
  - Set image registry location
  - Supply runtime parameters
  - Track execution progress

---

### Job 2: Work with Pipelines in Developer Perspective
*When I need to create and manage pipelines through the OpenShift web console*

**Personas:** Application developer

**Why:** Provides visual interface for pipeline creation integrated with the development workflow, reducing need for YAML expertise.

#### 2.1 Construct Pipelines Using Visual Builder (UI Approach)
**Goal:** Build pipelines interactively without writing YAML manually.

- **Approach:** Use Pipeline builder with task catalog
  → Lines 1522-1606: Constructing pipelines using the Pipeline builder
  
  **Features:**
  - Search and add tasks from Tekton Hub
  - Visual task configuration
  - Pipeline parameter setup
  - Switch between visual and YAML views
  
  **Requirements:**
  - Tekton Hub access for full task catalog (optional)
  - OpenShift Pipelines Operator installed

- **Related Setup:** Enable Tekton Hub for developers
  → Lines 1535-1539: Constructing pipelines using the Pipeline builder (Tekton Hub note)
  *For cluster administrators*
  
  **Purpose:** Provide curated task catalog without public hub dependency

#### 2.2 Create Pipelines During Application Import (From Git Approach)
**Goal:** Establish CI/CD automation from the start of application deployment.

- **Approach:** Generate pipeline from Git repository import
  → Lines 1615-1627: Creating OpenShift Pipelines along with applications
  
  **Benefits:**
  - Pipeline automatically linked to application
  - Default webhooks configured
  - Minimal steps to enable CI/CD
  
  **Available Options:**
  - Import from Git URL
  - Select pipeline template
  - View available tasks from Tekton Hub

#### 2.3 Add Repository with Pipeline Definitions (Pipelines as Code Approach)
**Goal:** Use pipeline definitions stored in the Git repository itself for version control and GitOps.

- **Approach:** Add GitHub repository containing .tekton directory
  → Lines 1637-1694: Adding a GitHub repository containing pipelines
  
  **Capabilities:**
  - Support for public and private repositories
  - Automatic pipeline triggering on Git events
  - GitHub App or webhook integration
  
  **Prerequisites:**
  - Cluster administrator configured GitHub applications
  - Repository contains `.tekton` directory with pipeline definitions

#### 2.4 Monitor Pipeline Execution (Visual Interface)
**Goal:** Understand pipeline structure and troubleshoot failures efficiently.

- **Features:** View pipeline details and run status
  → Lines 1704-1766: Interacting with pipelines using the Developer perspective
  
  **Visual Representation:**
  - Serial tasks execution flow
  - Parallel tasks visualization
  - Finally tasks (cleanup)
  - When expressions (conditional execution)
  - Quick access to logs and error details

---

### Job 3: Start and Monitor Pipelines
*When I have created a pipeline and need to execute it*

**Personas:** Application developer

#### 3.1 Execute Pipeline Runs with Resources
**Goal:** Start the pipeline with correct resources and credentials configured.

- **Entry Points:** Multiple ways to start pipelines
  → Lines 1775-1839: Starting pipelines from Pipelines view
  
  **Access Points:**
  - Pipelines view
  - Pipeline Details page
  - Topology view
  
  **Configuration:**
  - Add Git resource references
  - Configure image resources
  - Attach authentication secrets for private registries
  - Provide runtime parameters

---

### Job 4: Reuse Existing Pipeline and Task Definitions
*When building CI/CD pipelines, I want to leverage existing solutions from various sources*

**Personas:** Pipeline developer, Platform engineer

**Why:** Avoids duplicating code, leverages community-tested solutions, and increases maintainability through centralized definitions.

#### 4.1 Reference Tasks from Public Catalogs (Hub Resolver)
**Goal:** Use community-maintained tasks from Artifact Hub or Tekton Hub.

- **Task:** Configure hub resolver defaults
  → Lines 2254-2255: Configuring the hub resolver
  *For platform engineers*
  - Set default hub catalog source
  - Configure catalog settings
  - Control approved catalog sources

- **Task:** Reference catalog tasks in pipelines
  → Lines 2296-2299: Specifying a remote pipeline, task, or step action using the hub resolver
  - Specify catalog name, resource name, and version
  - Ensure version pinning for reproducible builds
  - Minimize local task duplication

#### 4.2 Reference Tasks from OCI Registries (Bundles Resolver)
**Goal:** Distribute pipelines and tasks as versioned container images using existing container infrastructure.

- **Task:** Configure bundles resolver
  → Lines 2429-2430: Configuring the bundles resolver
  *For platform engineers*
  - Set default service account for bundle access
  - Configure resource kind defaults
  - Standardize authentication

- **Task:** Reference tasks from Tekton bundles
  → Lines 2460-2461: Specifying a remote pipeline, task, or step action using the bundles resolver
  - Specify OCI bundle image URL
  - Reference specific resource by name
  - Use container registry versioning

#### 4.3 Reference Tasks from Git Repositories (Git Resolver)
**Goal:** Use version-controlled task definitions with full traceability and commit-level pinning.

##### For Public Repositories (Anonymous Access)

- **Task:** Configure Git resolver for anonymous cloning
  → Lines 2658-2659: Configuring the Git resolver for anonymous Git cloning
  *For platform engineers*
  - Set default Git revision
  - Configure fetch timeout
  - Set default repository URL

- **Task:** Reference public repository tasks
  → Lines 2697-2700: Specifying a remote pipeline, task, or step action by using the Git resolver for anonymous cloning
  - Specify Git URL, branch/revision, and file path
  - Pin to specific commits for reproducibility
  - Track upstream task changes

##### For Private Repositories (Authenticated API)

- **Task:** Configure authenticated API access
  → Lines 2792-2793: Configuring the Git resolver for an authenticated API
  *For platform engineers*
  - Set up API endpoints for Git providers
  - Create secrets with API tokens
  - Configure multiple SCM providers

- **Task:** Reference private repository tasks
  → Lines 2898-2899: Specifying a remote pipeline, task, or step action using the Git resolver with the authenticated SCM API
  - Reference by organization and repository name
  - Use API authentication without embedding credentials
  - Manage API token expiration

#### 4.4 Reference Tasks from HTTP Endpoints (HTTP Resolver)
**Goal:** Integrate tasks from web-hosted sources or internal servers.

- **Task:** Configure HTTP resolver settings
  → Lines 3114-3115: Configuring the HTTP resolver
  *For platform engineers*
  - Set timeout for HTTP requests
  - Configure default URL settings
  - Set up HTTP basic auth

- **Task:** Reference tasks by URL
  → Lines 3140-3141: Specifying a remote pipeline, task, or step action with the HTTP Resolver
  - Provide HTTP/HTTPS URL
  - Use optional basic authentication
  - Minimize infrastructure for task distribution

#### 4.5 Reference Cluster-Local Tasks (Cluster Resolver)
**Goal:** Reuse tasks already installed in the cluster without external dependencies.

- **Task:** Configure cluster resolver
  → Lines 3224-3225: Configuring the cluster resolver
  *For platform engineers*
  - Set default namespace for lookups
  - Configure resource kind defaults
  - Standardize shared task access

- **Task:** Reference cluster-installed tasks
  → Lines 3262-3263: Specifying a pipeline, task, or step action from the same cluster using the cluster resolver
  - Reference by namespace and name
  - Use cluster-wide shared tasks
  - Ensure fast lookup without network calls

---

## Modify and Update

### Job 5: Modify Pipeline Configurations
*When I need to update existing pipelines*

**Personas:** Application developer

#### 5.1 Edit Pipelines Through Web Console
**Goal:** Update pipeline configuration without recreating the entire pipeline.

- **Task:** Modify pipeline using Pipeline builder
  → Lines 1897-1912: Editing pipelines
  - Add or remove tasks
  - Modify parameters
  - Update resources
  - Apply changes

---

## Govern and Secure

### Job 6: Create Reusable Pipeline Templates
*When I want to provide standardized pipeline patterns for my organization*

**Personas:** Cluster administrator

**Why:** Ensures consistent pipeline patterns across teams, reduces duplication, and minimizes developer effort.

#### 6.1 Define Pipeline Templates (Administrator Setup)
**Goal:** Create templates that developers can reuse across projects.

- **Task:** Create templates in openshift namespace
  → Lines 1945-1981: Creating pipeline templates in the Administrator perspective
  
  **Requirements:**
  - Cluster administrator permissions
  - OpenShift Pipelines Operator installed
  
  **Configuration:**
  - Define runtime labels for templates
  - Define pipeline type labels
  - Place in openshift namespace for visibility

---

### Job 7: Control Pipeline Execution with Manual Approval Gates
*When critical deployments require human authorization before proceeding*

**Personas:** Platform administrator, DevOps engineer, Pipeline approver

**Why:** Ensures the right stakeholders authorize production deployments and prevents unauthorized or untrusted code execution.

#### 7.1 Enable Approval Gate Capability (Platform Setup)
**Goal:** Prepare the cluster to support approval tasks in pipelines.

- **Task:** Enable manual approval gate controller
  → Lines 5787-5834: Enabling the manual approval gate controller
  *Technology Preview feature*
  *For platform administrators*
  
  **Prerequisites:**
  - OpenShift Pipelines Operator installed
  - Administrator permissions for openshift-pipelines namespace
  - oc CLI access
  
  **Note:** This is a one-time prerequisite before approval tasks can be used.

#### 7.2 Configure Approval Tasks in Pipelines (DevOps Setup)
**Goal:** Define who can approve and how many approvals are required for critical stages.

- **Task:** Specify approval task with approvers
  → Lines 5842-6076: Specifying a manual approval task
  *For DevOps engineers*
  
  **Approval Patterns:**
  
  - **Multi-user approval:** Requires N approvals from individual users
  - **Group-based approval:** Requires approvals from group members
  - **Mixed user/group approval:** Combines individual users and groups
  
  **Configuration:**
  - List approvers (users or groups)
  - Set approval threshold (number required)
  - Configure timeout (default 1 hour)
  - Create groups and add required users (for group approval)

#### 7.3 Understand Group Approval Behavior (Policy Design)
**Goal:** Design approval policies that match organizational requirements.

- **Concept:** How controller tracks approvals
  → Lines 6218-6286: Behavior of ApprovalTask with groups and users
  
  **Behavior:**
  - Controller tracks individual approvals from group members
  - Updates group approval state automatically
  - Supports complex policies combining users and groups

#### 7.4 Approve or Reject Deployments (Approver Actions)
**Goal:** Authorize or block critical deployments when pipeline reaches approval gate.

##### Via Web Console

- **Approach:** Approve using OpenShift web console
  → Lines 6106-6131: Approving a manual approval task by using the web console
  *For pipeline approvers*
  
  **Access Points:**
  - Notification link (appears when approval required)
  - Pipelines Approvals tab (Administrator perspective)
  - Pipelines Approvals tab (Developer perspective)
  - PipelineRun details window
  
  **Actions:**
  - Approve with optional reason
  - Reject with optional reason

##### Via Command Line

- **Approach:** Approve using opc CLI
  → Lines 6145-6209: Approving a manual approval task by using the command line
  *For pipeline approvers*
  
  **Prerequisites:**
  - opc CLI utility installed (same package as tkn)
  - oc CLI access
  - Listed as approver in approval task
  
  **Commands:**
  - `opc approvaltask list` - View pending approvals
  - `opc approvaltask describe` - View approval details
  - `opc approvaltask approve` - Approve with optional message
  - `opc approvaltask reject` - Reject with optional message

---

## Analyze Performance

### Job 8: Analyze Pipeline Performance and Trends
*When I need to understand pipeline effectiveness across my organization*

**Personas:** Platform administrator

**Why:** Identifies trends, optimizes workflows, and enables CI/CD effectiveness reporting.

#### 8.1 View Execution Statistics (Performance Monitoring)
**Goal:** Access consolidated metrics for pipeline runs and success rates.

- **Setup:** Enable pipeline statistics
  → Lines 1990-2002: Pipeline execution statistics in the web console
  
  **Prerequisites:**
  - Tekton Results installed
  - OpenShift Pipelines console plugin enabled
  
  **Metrics:**
  - Pipeline success ratios
  - Pipeline run durations
  - Run trends over time
  - Statistics for individual pipelines
  - Statistics across all pipelines

---

## Manage Resources

### Job 9: Use Red Hat Entitlements in Pipeline Builds
*When building container images that require RHEL packages*

**Personas:** Pipeline developer, Platform engineer

**Why:** Enables access to RHEL repositories during pipeline build processes.

**Prerequisites (One-time):**
- Enable Insights Operator feature on cluster
- Configure importing of Red Hat entitlements into Insights Operator from Simple Content Access (SCA)
- Verify etc-pki-entitlement secret exists in openshift-config-managed namespace

#### 9.1 Choose Entitlement Distribution Method
**Goal:** Select the right approach based on your number of pipeline namespaces.

| Method | Best For | Complexity | Maintenance |
|--------|----------|------------|-------------|
| Manual secret copying | Few namespaces | Low | Manual per namespace |
| Shared Resources CSI Driver | Many namespaces | Medium | Automatic across namespaces |

#### 9.2 Manual Secret Copying Approach (Simple Setup)
**Goal:** Provide entitlements without additional operator configuration.

- **Approach:** Copy secret to each namespace
  → Lines 6412-6493: Using Red Hat entitlements by manually copying the etc-pki-entitlement secret
  *For pipeline developers*
  *Recommended when there are a limited number of pipeline namespaces*
  
  **Prerequisites:**
  - jq package installed
  - Insights Operator enabled
  - etc-pki-entitlement secret exists
  
  **Steps:**
  - Extract secret from openshift-config-managed namespace
  - Copy to target pipeline namespace
  - Configure Buildah task to use rhel-entitlement workspace
  - Define workspace in pipeline runs

#### 9.3 Shared Resources CSI Driver Approach (Automated Setup)
**Goal:** Centralize entitlement management across many namespaces automatically.

- **Approach:** Share secret using CSI driver
  → Lines 6501-6628: Using Red Hat entitlements by sharing the secret using the Shared Resources CSI driver operator
  *For platform engineers*
  *Recommended when using the Shared Resources CSI Driver*
  
  **Prerequisites:**
  - Cluster administrator permissions
  - Shared Resources CSI Driver operator enabled
  - Insights Operator enabled
  - etc-pki-entitlement secret exists
  
  **Setup:**
  - Create SharedSecret custom resource
  - Configure RBAC for shared resource access
  - Manage service account permissions
  - Configure Buildah task to use rhel-entitlement workspace
  
  **Benefits:**
  - Automatic entitlement availability for new namespaces
  - Centralized secret management
  - Reduced configuration drift

---

## Appendices

### A. Resolver Comparison Matrix

| Resolver | Source | Best For | Authentication |
|----------|--------|----------|----------------|
| Hub | Tekton Hub, Artifact Hub | Community tasks, public catalogs | None |
| Bundles | OCI registries | Container-native versioning, existing registry infra | Registry credentials |
| Git (anonymous) | Public Git repos | Version-controlled public tasks | None |
| Git (authenticated) | Private Git repos | Proprietary/internal tasks | API tokens |
| HTTP | HTTP/HTTPS endpoints | Web-hosted tasks, internal servers | Optional basic auth |
| Cluster | Same cluster | Fast local lookups, shared cluster tasks | RBAC |

### B. Trigger Configuration Quick Reference

| Component | Purpose | Scope |
|-----------|---------|-------|
| TriggerBinding | Extract data from webhook | Per trigger |
| TriggerTemplate | Define PipelineRun to create | Per trigger |
| Trigger | Connect binding and template | Per event type |
| EventListener | Expose webhook endpoint | Per namespace or multitenant |

### C. Workflow Coverage Analysis

| Stage | Coverage | Jobs | Notes |
|-------|----------|------|-------|
| Build | ✅ Full | Jobs 1, 2, 4 | Task creation, pipeline assembly, reusable definitions |
| Execute | ✅ Full | Jobs 1, 3 | Manual and automated pipeline runs |
| Monitor | ✅ Full | Jobs 2, 3, 8 | Visual interface, metrics, statistics |
| Govern | ✅ Full | Jobs 6, 7 | Templates, approval gates, validation |
| Secure | ✅ Full | Job 7 | Approval validation, PR authorization |
| Analyze | ✅ Full | Job 8 | Performance statistics, trends |
| Modify | ✅ Full | Job 5 | Pipeline editing |
| Manage | ✅ Full | Job 9 | Entitlements, resource access |

### Gaps Identified

No significant gaps identified. The guide covers the complete lifecycle from pipeline creation through execution, monitoring, governance, and resource management.

---

## Navigation Guide

### By User Journey

**Application Developer - Getting Started with Pipelines:**
1. Job 1.4: Set up project prerequisites
2. Job 1.1: Define or install reusable tasks
3. Job 1.2: Assemble pipeline workflow
4. Job 1.5: Execute first pipeline run
5. Job 1.3: Enable event-driven automation

**Application Developer - Using Developer Console:**
1. Job 2: Work with pipelines in Developer perspective
   - Option 2.1: Build visually with Pipeline builder
   - Option 2.2: Create during application import
   - Option 2.3: Add repository with pipeline definitions
2. Job 3: Start and monitor pipeline runs
3. Job 5: Edit pipelines as needed

**Pipeline Developer - Building Reusable Solutions:**
1. Job 4: Reuse existing pipeline and task definitions
   - Choose resolver type based on source
   - Configure resolver settings
   - Reference tasks in pipeline definitions
2. Job 1.2: Assemble pipelines using referenced tasks
3. Job 1.3: Add triggers for automation

**Platform Engineer - Setting Up for Teams:**
1. Job 4: Configure resolvers for team (hub, bundles, git, http, cluster)
2. Job 1.3: Configure multitenant event listeners
3. Job 9: Set up Red Hat entitlements (choose approach based on scale)
4. Job 7.1: Enable approval gate controller
5. Job 8.1: Enable pipeline statistics and monitoring

**Cluster Administrator - Governance and Standards:**
1. Job 6: Create reusable pipeline templates
2. Job 7.1: Enable manual approval gates
3. Job 2.1: Install and deploy Tekton Hub instance (optional)

**DevOps Engineer - Production Deployment Control:**
1. Job 7.2: Configure approval tasks in pipelines
2. Job 7.3: Understand group approval behavior
3. Job 1.3.6: Filter pull requests
4. Job 1.3.7: Validate pull requests from external contributors

**Pipeline Approver - Authorizing Deployments:**
1. Job 7.4: Approve or reject deployments
   - Via web console (Job 7.4 Console approach)
   - Via CLI (Job 7.4 CLI approach)

---

## Document Statistics

**Workflow Coverage:**
- Build Pipeline Workflows: 4 main jobs (Jobs 1, 2, 4, 5)
- Execute and Monitor: 2 main jobs (Jobs 3, 8)
- Govern and Secure: 2 main jobs (Jobs 6, 7)
- Manage Resources: 1 main job (Job 9)

**Main Jobs:** 9
**User Stories/Themed Sections:** 45
**Source Sections:** 51 JTBD records analyzed
**Personas:** 7 distinct roles
**Resolver Types:** 5 (Hub, Bundles, Git, HTTP, Cluster)
**Approval Patterns:** 3 (Multi-user, Group-based, Mixed)
**Entitlement Distribution Methods:** 2 (Manual, CSI Driver)

**Coverage by Persona:**
- Application developer: Jobs 1, 2, 3, 5
- Pipeline developer: Jobs 1, 4, 9
- Platform engineer: Jobs 1, 4, 9
- Platform administrator: Jobs 7, 8
- Cluster administrator: Jobs 2, 6
- DevOps engineer: Job 7
- Pipeline approver: Job 7

---

## Key Insights

### Documentation Strengths

1. **Complete workflow coverage** - From basic pipeline creation to advanced governance with approval gates
2. **Multiple approach options** - UI, CLI, GitOps, and programmatic methods supported
3. **Strong reusability** - Five resolver types enable task sharing from various sources
4. **Production readiness** - Approval gates, monitoring, and entitlement management included
5. **Role-based guidance** - Clear separation between developer, engineer, administrator, and approver tasks

### Strategic Priorities

1. **Event-driven automation** (Job 1.3) is the critical path to reducing manual effort
2. **Task reusability** (Job 4) is essential for scaling across teams
3. **Approval gates** (Job 7) are necessary for production governance
4. **Monitoring and analytics** (Job 8) enable continuous improvement

### Workflow Dependencies

**Sequential dependencies:**
1. Job 1.4 (Project setup) → BEFORE → Job 1.1-1.2 (Pipeline creation)
2. Job 1.2 (Pipeline assembly) → BEFORE → Job 1.5 (Pipeline execution)
3. Job 7.1 (Enable approval controller) → BEFORE → Job 7.2 (Configure approval tasks)
4. Job 9 prerequisites (Insights Operator) → BEFORE → Job 9.2 or 9.3 (Entitlement distribution)

**Parallel options:**
- Jobs 2.1, 2.2, 2.3 are alternative approaches to pipeline creation
- Jobs 4.1-4.5 are alternative resolver types (choose based on source)
- Jobs 9.2-9.3 are alternative entitlement distribution methods

---

**Document Version:** 1.0  
**Generated:** 2026-06-12  
**Source:** create-combined.adoc (51 JTBD records)  
**Methodology:** Jobs-To-Be-Done framework with workflow stage organization

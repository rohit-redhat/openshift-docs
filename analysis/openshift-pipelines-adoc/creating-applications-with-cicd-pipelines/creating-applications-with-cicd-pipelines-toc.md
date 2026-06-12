# Creating CI/CD Solutions for Applications Using OpenShift Pipelines
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** Enable developers and administrators to create automated CI/CD pipelines that build, test, and deploy applications on OpenShift using Tekton Pipelines.

**Personas:** Developer, Platform Administrator, Cluster Administrator

**Main Jobs:** 11 core jobs across 6 workflow stages (Prepare, Configure, Execute, Monitor, Secure)

---

## Quick Navigation

**I want to:**
- Set up my environment for pipelines → Job 1 (Prepare)
- Create a project for my pipeline → Job 2 (Prepare)
- Build reusable pipeline components → Job 3 (Prepare)
- Define my CI/CD workflow → Job 4 (Configure)
- Run pipelines in air-gapped environments → Job 5 (Configure)
- Execute my pipeline → Job 6 (Execute)
- Automate pipeline triggers → Job 7 (Configure)
- Connect Git webhooks → Job 8 (Configure)
- Validate automation works → Job 9 (Execute)
- Monitor pipeline performance → Job 10 (Monitor)
- Filter and secure pull requests → Job 11 (Configure/Secure)

---

# Table of Contents

## Prepare Your Environment

### Job 1: Verify Prerequisites
*When starting a CI/CD pipeline project, I want to ensure my OpenShift cluster has the necessary components installed*

**Personas:** Developer

**Prerequisites:** Cluster access

→ Lines 81-87: Prerequisites
  Source: Assembly root, Prerequisites section
  - OpenShift Pipelines Operator installed
  - Pipelines CLI (tkn) installed
  - Forked Git repositories with admin access
  - Optional: Cloned pipelines-tutorial repository

---

### Job 2: Create Project and Verify Service Accounts
*When preparing to run pipelines, I want to create a dedicated project and verify the pipeline service account exists*

**Personas:** Developer

**Prerequisites:** Cluster access and Pipelines Operator installed

→ Lines 96-127: Creating a project and checking your pipeline service account
  Source: Module op-creating-project-and-checking-pipeline-service-account

**2.1. Log in to cluster and create project** `[procedure]`
  - Context: Creates namespace isolation for pipeline resources
  - Example: `oc new-project pipelines-tutorial`
  - Note: Pipeline service account automatically configured by Operator

**2.2. Verify pipeline service account** `[procedure]`
  - Context: Ensures service account has permissions to build and push images
  - Command: `oc get serviceaccount pipeline`

---

### Job 3: Install Reusable Pipeline Tasks
*When building a CI/CD pipeline, I want to install reusable tasks from existing repositories*

**Personas:** Developer

**Prerequisites:** Project created

→ Lines 136-168: Creating pipeline tasks
  Source: Module op-creating-pipeline-tasks

**3.1. Install task resources from repository** `[procedure]`
  - apply-manifests task: Applies Kubernetes manifests
  - update-deployment task: Updates deployment with new image
  - Source: pipelines-tutorial GitHub repository

**3.2. Verify task installation** `[procedure]`
  - Command: `tkn task list`
  - Expected output: apply-manifests and update-deployment tasks listed

---

## Set Up & Configure

### Job 4: Assemble a Pipeline
*When creating a CI/CD workflow, I want to assemble pipeline tasks into an executable flow with defined dependencies and workspaces*

**Personas:** Developer

**Prerequisites:** Reusable tasks installed

**Timing:** BEFORE Job 5 (image mirroring) or Job 6 (pipeline execution)

→ Lines 177-309: Assembling a pipeline
  Source: Module op-assembling-a-pipeline

**4.1. Understand pipeline structure** `[concept]`
  - Context: Pipeline defines task interaction and execution order
  - Uses workspaces for shared storage across tasks
  - Parameters: git-url, git-revision, deployment-name, IMAGE

**4.2. Define pipeline YAML** `[procedure]`
  - Task 1: fetch-repository (git-clone)
  - Task 2: build-image (buildah) - runAfter fetch-repository
  - Task 3: apply-manifests - runAfter build-image
  - Task 4: update-deployment - runAfter apply-manifests

**4.3. Create the pipeline resource** `[procedure]`
  - Option A: Create from local YAML file
  - Option B: Create directly from GitHub repository
  - Verification: `tkn pipeline list`

---

### Job 5: Mirror Images for Restricted Environments
*When deploying pipelines in a disconnected or restricted cluster, I want to mirror required builder images to a private registry*

**Personas:** Platform Administrator

**Prerequisites:** Pipeline assembled, access to mirror registry

**Why:** Air-gapped environments cannot pull images from public registries

→ Lines 319-521: Mirroring images to run pipelines in a restricted environment
  Source: Module op-mirroring-images-to-run-pipelines-in-restricted-environment

**5.1. Mirror front-end builder image (Python)** `[procedure]`
  - Verify image tag not imported
  - Mirror from registry.redhat.io to private registry
  - Import image with --scheduled flag for auto-reimport
  - Verify import: `oc describe imagestream python`

**5.2. Mirror back-end builder image (Golang)** `[procedure]`
  - Mirror go-toolset image
  - Configure scheduled reimport
  - Verification steps

**5.3. Mirror CLI image** `[procedure]`
  - Mirror ocp-v4.0-art-dev image
  - Tag and schedule reimport

---

## Deploy & Execute

### Job 6: Run a Pipeline
*When ready to build and deploy my application, I want to start a pipeline run with specific parameters and track its progress*

**Personas:** Developer

**Prerequisites:** Pipeline assembled

→ Lines 538-621: Running a pipeline
  Source: Module op-running-a-pipeline

**6.1. Start pipeline for back-end application** `[procedure]`
  - Command: `tkn pipeline start build-and-deploy`
  - Parameters: deployment-name, git-url, IMAGE
  - Workspace: volumeClaimTemplateFile for persistent storage
  - Context: Creates PipelineRun object

**6.2. Track pipeline progress** `[procedure]`
  - Command: `tkn pipelinerun logs <pipelinerun_id> -f`
  - Follow log output in real-time

**6.3. Start pipeline for front-end application** `[procedure]`
  - Same process with different parameters
  - Different git-url and deployment-name

**6.4. Verify pipeline success** `[procedure]`
  - Command: `tkn pipelinerun list`
  - Check STATUS column shows "Succeeded"
  - Get application route: `oc get route pipelines-vote-ui`

**6.5. Rerun previous pipeline** `[procedure]`
  - Command: `tkn pipeline start build-and-deploy --last`
  - Context: Reuses resources and service account from last run

---

## Automate & Integrate

### Job 7: Configure Pipeline Triggers
*When automating CI/CD workflows, I want to configure triggers that respond to GitHub events*

**Personas:** Developer

**Prerequisites:** Pipeline created and successfully run

→ Lines 636-871: Adding triggers to a pipeline
  Source: Module op-adding-triggers

**7.1. Create TriggerBinding** `[procedure]`
  - Extracts parameters from GitHub webhook payload
  - Maps: git-repo-url, git-repo-name, git-revision

**7.2. Create TriggerTemplate** `[procedure]`
  - Defines PipelineRun template
  - Uses parameters from TriggerBinding
  - Includes volumeClaimTemplate for workspace storage

**7.3. Create Trigger resource** `[procedure]`
  - Links TriggerBinding and TriggerTemplate
  - Specifies service account

**7.4. Create EventListener** `[procedure]`
  - Option A: Secure HTTPS connection (recommended)
    - Enable annotation: `oc label namespace <ns_name> operator.tekton.dev/enable-annotation=enabled`
    - Create EventListener
    - Create route with re-encrypt TLS termination
  - Option B: Insecure HTTP connection
    - Create EventListener
    - Expose service: `oc expose svc el-vote-app`

**7.5. Configure multitenant event listeners (optional)** `[procedure]`
  → Lines 880-1027: Configuring event listeners to serve many namespaces
  - Context: For deployments spanning multiple namespaces
  - Configure cluster-wide fetch permissions
  - Set ClusterRole, ClusterRoleBinding, ServiceAccount
  - Configure namespaceSelector in EventListener spec

---

### Job 8: Connect Git Repository Webhooks
*When connecting Git repositories to pipelines, I want to configure webhook URLs pointing to EventListener routes*

**Personas:** Developer

**Prerequisites:** EventListener created, administrative access to Git repositories

→ Lines 1037-1085: Creating webhooks
  Source: Module op-creating-webhooks

**8.1. Get webhook URL** `[procedure]`
  - HTTPS: `echo "URL: $(oc get route el-vote-app --template='https://{{.spec.host}}')"`
  - HTTP: `echo "URL: $(oc get route el-vote-app --template='http://{{.spec.host}}')"`

**8.2. Configure webhook on front-end repository** `[procedure]`
  - Navigate to GitHub repository → Settings → Webhooks → Add Webhook
  - Enter webhook URL in Payload URL
  - Select application/json content type
  - Specify secret
  - Select "Just the push event"
  - Activate webhook

**8.3. Configure webhook on back-end repository** `[procedure]`
  - Repeat configuration for pipelines-vote-api repository

---

### Job 9: Validate Pipeline Automation
*When validating my CI/CD automation, I want to push a code change and verify it triggers a pipeline run*

**Personas:** Developer

**Prerequisites:** Webhooks configured

→ Lines 1093-1125: Triggering a pipeline run
  Source: Module op-triggering-a-pipelinerun

**9.1. Clone forked repository** `[procedure]`
  - Command: `git clone git@github.com:<your GitHub ID>/pipelines-vote-ui.git`

**9.2. Push empty commit to trigger pipeline** `[procedure]`
  - Command: `git commit -m "empty-commit" --allow-empty && git push origin pipelines-1.22`
  - Context: Tests webhook without actual code changes

**9.3. Verify pipeline run triggered** `[procedure]`
  - Command: `tkn pipelinerun list`
  - Confirm new PipelineRun created with correct timestamp

---

## Track & Monitor

### Job 10: Monitor Event Listener Performance
*When operating CI/CD pipelines in production, I want to monitor event listener metrics and performance*

**Personas:** Cluster Administrator

**Prerequisites:** EventListener deployed, monitoring enabled for user-defined projects

→ Lines 1133-1187: Enabling monitoring of event listeners for Triggers for user-defined projects
  Source: Module op-enabling-monitoring-of-event-listeners-for-triggers-for-user-defined-projects

**10.1. Create ServiceMonitor for event listener** `[procedure]`
  - Configure labels matching EventListener
  - Set endpoint interval (e.g., 10s)
  - Specify namespace selector

**10.2. Test metrics collection** `[procedure]`
  - Send request to event listener (push commit)
  - Navigate to Administrator → Observe → Metrics
  - Search for metrics: eventlistener_http_duration_seconds, eventlistener_event_count, eventlistener_triggered_resources

---

## Filter & Secure

### Job 11: Optimize and Secure Pull Request Triggers
*When managing pull request workflows, I want to filter events based on changed files and validate based on repository ownership*

**Personas:** Developer

**Prerequisites:** Triggers configured

→ Lines 1200-1212: Configuring pull request capabilities in GitHub Interceptor
  Source: Module op-configuring-pull-request-capabilities-in-GitHub-interceptor

**11.1. Understand GitHub Interceptor capabilities** `[concept]`
  - Filter pull requests based on changed files
  - Validate pull requests based on repository owners

**11.2. Filter pull requests by changed files** `[procedure]`
  → Lines 1220-1308: Filtering pull requests using GitHub Interceptor
  - Option A: Public repository
    - Set addChangedFiles parameter to true
    - Use CEL Interceptor to match file patterns
    - Example: `extensions.changed_files.matches('controllers/')`
  - Option B: Private repository
    - Include personalAccessToken secret reference
    - Configure same filtering logic

**11.3. Validate pull requests by ownership** `[procedure]`
  → Lines 1316-1409: Validating pull requests using GitHub Interceptors
  - Create OWNERS file in repository root
  - Configure githubOwners parameter
  - Option A: Public repository with checkType setting
  - Option B: Private repository with personalAccessToken
  - Context: Requires /ok-to-test comment from owner for external contributors

---

## Additional Resources

### External Documentation
- Pipelines as Code integration
- Working with Pipelines in web console
- Security Context Constraints (SCCs)
- Tekton Hub for reusable tasks
- Configuring Samples Operator for restricted clusters
- Disconnected installation mirroring

---

## Document Statistics

**Workflow Coverage:**
- Prepare: 3 jobs (Prerequisites, Project setup, Task installation)
- Configure: 5 jobs (Pipeline assembly, Image mirroring, Triggers, Webhooks, PR filtering)
- Execute: 2 jobs (Running pipeline, Validating automation)
- Monitor: 1 job (Event listener metrics)
- Secure: Part of Job 11 (PR validation)

**Main Jobs:** 11
**User Stories/Paths:** 35+ (nested approaches)
**Source Sections:** 13 modules
**Platform Variations:** Disconnected/connected, public/private repositories, HTTP/HTTPS

**Gap identified:** No troubleshooting content for failed pipelines or debugging guidance

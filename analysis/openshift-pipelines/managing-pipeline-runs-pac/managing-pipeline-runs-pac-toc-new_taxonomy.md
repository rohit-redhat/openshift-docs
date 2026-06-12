# Managing Pipeline Runs using Pipelines as Code
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** Enable DevOps engineers and platform engineers to verify, execute, monitor, and manage pipeline runs using Pipelines as Code automation and GitOps workflows.

**Personas:** Pipeline Developer, DevOps Engineer, Platform Engineer

**Main Jobs:** 9 core jobs across 5 workflow stages (Configure, Deploy, Operate, Monitor)

---

## Quick Navigation

**I want to:**
- Verify pipeline definitions before deployment → Job 1 (Configure)
- Trigger pipelines automatically on Git events → Job 2 (Deploy)
- View pipeline execution logs → Job 2 (Deploy)
- Trigger pipelines on Git tags → Job 3 (Deploy)
- Use GitOps commands on tagged commits → Job 4 (Deploy)
- Restart failed pipeline runs → Job 5 (Operate)
- Cancel running pipeline runs → Job 5 (Operate)
- Monitor pipeline status and errors → Job 6 (Monitor)
- View error annotations on pull requests → Job 6 (Monitor)
- Check pipeline run history → Job 6 (Monitor)
- Configure automatic cleanup of old pipeline runs → Job 7 (Operate)
- Trigger pipelines from external systems → Job 8 (Deploy)
- Use incoming webhooks with custom automation → Job 8 (Deploy)

---

# Table of Contents

## Validate Pipeline Configurations

### Job 1: Verify Pipeline Run Definitions
*When I create a pipeline run definition, I want to validate that all referenced resources are resolvable before triggering in production*

**Personas:** Pipeline Developer

**Why:** Catch errors before pipeline execution to minimize time identifying definition errors and reduce likelihood of runtime failures

**Requires:** 
- tkn CLI utility installed
- OpenShift cluster login credentials
- Git repository cloned locally

#### 1.1 Validate Using CLI Resolver
**Goal:** Use tkn pac resolve command to see the fully resolved PipelineRun with all referenced resources.

→ Lines 72-95: Verifying a pipeline run

- **Task:** Run tkn pac resolve command from repository root
  ```bash
  tkn pac resolve .tekton/pipeline-run-definition.yaml
  ```

- **Validation:** 
  - Resolver displays complete PipelineRun CR if successful
  - Error messages identify missing resources if validation fails
  - Complete validation in under 1 minute

---

## Deploy & Execute Pipelines

### Job 2: Execute Pipeline Runs Automatically on Git Events
*When a Git event occurs on my repository, I want pipeline runs to execute automatically based on configured event triggers*

**Personas:** DevOps Engineer

**Timing:** AFTER Job 1 (Verify pipeline definitions) - ensures pipeline definitions are valid before automatic execution

**Requires:**
- Repository CRD configured
- Pipeline run definitions in .tekton/ directory
- Authentication for repository set up

→ Lines 104-142: Running a pipeline run using Pipelines as Code

#### 2.1 Understand Automatic Execution Behavior
**Goal:** Know when and how pipelines execute based on Git events and user permissions.

- **Context:** Pipelines as Code runs any pipeline in `.tekton/` directory when events (pull request, push) occur on default branch

- **Authorization Rules:**
  - Pull request author must be repository owner, collaborator, or public member
  - OWNERS file can list authors in approvers/reviewers sections
  - Other authorized users can comment `/ok-to-test` to approve execution

- **Execution Context:**
  - Pipeline runs execute in namespace of Repository CRD
  - Pipelines from non-default branches run only if author meets authorization requirements

#### 2.2 Monitor Pipeline Execution via CLI
**Goal:** Follow pipeline progress and troubleshoot issues in real-time using command line.

- **Task:** Follow last pipeline run execution
  ```bash
  tkn pac logs -n <namespace> -L
  ```

- **Task:** Select and follow specific pipeline run interactively
  ```bash
  tkn pac logs -n <namespace>
  ```

- **Alternative:** View execution in GitHub App Checks tab (if configured)

---

### Job 3: Trigger Pipeline Runs on Git Tags
*When I create or reference a Git tag representing a specific release version, I want to trigger pipeline runs that test or deploy that tagged version*

**Personas:** DevOps Engineer

**Why:** Support release-based workflows and version control practices, enabling consistent validation and deployment of tagged versions

**Requires:**
- PipelineRun configured with tag event annotations
- Supported Git provider (GitHub App, GitHub Webhook, or GitLab)

→ Lines 151-197: Triggering a PipelineRun on Git tags

#### 3.1 Understand Tag-Based Triggering
**Goal:** Know how Pipelines as Code processes tag events and GitOps commands.

- **Context:** Tag creation triggers PipelineRun when configured with:
  - Annotation: `pipelinesascode.tekton.dev/on-target-branch: "[refs/tags/*]"`
  - Annotation: `pipelinesascode.tekton.dev/on-event: "[push]"`

- **Behavior:** 
  - Pipelines as Code resolves Git tag to commit SHA
  - Runs PipelineRun defined for that commit
  - Treats tag creation as push event

#### 3.2 Configure PipelineRun for Tag Events
**Goal:** Author PipelineRun manifest that responds to tag events.

- **Task:** Add tag event annotations to PipelineRun
  ```yaml
  apiVersion: tekton.dev/v1
  kind: PipelineRun
  metadata:
    name: pipelinerun-on-tag
    annotations:
      pipelinesascode.tekton.dev/on-target-branch: "[refs/tags/*]"
      pipelinesascode.tekton.dev/on-event: "[push]"
  ```

- **Use Case:** Continuous delivery scenarios where tags represent specific versions or releases

---

### Job 4: Trigger Pipeline Runs Using GitOps Commands on Tags
*When I need to manage pipeline runs for tagged commits, I want to use GitOps commands via Git provider UI*

**Personas:** DevOps Engineer

**Requires:**
- Git tag exists in repository
- GitHub UI access (or GitLab for GitLab provider)
- Required repository permissions (owner, collaborator, public member, or OWNERS file)

→ Lines 206-220: Triggering PipelineRuns for GitOps commands using tagged commits

#### 4.1 Supported GitOps Commands for Tags
**Goal:** Know which commands can trigger, restart, or cancel tag-based pipeline runs.

**Available Commands:**
- `/test tag:<tag>` - Retrigger all matching PipelineRuns for tag commit
- `/test <pipelinerun_name> tag:<tag>` - Retrigger specific PipelineRun
- `/retest tag:<tag>` - Retrigger all matching PipelineRuns
- `/retest <pipelinerun_name> tag:<tag>` - Retrigger specific PipelineRun
- `/cancel tag:<tag>` - Cancel all running PipelineRuns
- `/cancel <pipelinerun_name> tag:<tag>` - Cancel specific PipelineRun

#### 4.2 Execute GitOps Commands via GitHub UI
**Goal:** Trigger or manage tag-based pipeline runs without CLI tools.

- **Task:** Navigate to tag in GitHub repository
  1. Open GitHub repository
  2. Navigate to Tags view or Releases section
  3. Select required tag (e.g., `v1.0.0`)
  4. Click commit SHA for selected tag

- **Task:** Enter GitOps command in commit comment field
  - Example: `/test tag:v1.0.0`
  - Example: `/cancel tag:v1.0.0`

- **Validation:** Pipelines as Code processes comment and triggers/updates corresponding PipelineRun within 30 seconds

---

## Operate & Manage Pipelines

### Job 5: Restart or Cancel Pipeline Runs
*When I need to restart a failed pipeline or cancel a running pipeline, I want to manage pipeline lifecycle without triggering new Git events*

**Personas:** DevOps Engineer

**Requires:** User has required repository permissions (owner, collaborator, public member, or OWNERS file listing)

→ Lines 229-317: Restarting or canceling a pipeline run using Pipelines as Code

#### 5.1 Restart All Pipeline Runs (GitHub App Method)
**Goal:** Retry all failed pipelines with one click using GitHub UI.

- **Task:** Use GitHub App Re-run all checks feature
  1. Navigate to pull request
  2. Go to Checks tab
  3. Click "Re-run all checks"

- **Benefits:**
  - Restart all pipelines in under 10 seconds
  - Avoid restarting pipelines individually
  - View results in GitHub Checks tab

**Note:** Technology Preview when starting pipelines not matching original events

#### 5.2 Restart or Cancel Specific Pipelines (GitOps Commands)
**Goal:** Control individual pipelines using comments on pull requests or commits.

**For Pull/Merge Requests:**

- **Commands:**
  - `/test` or `/retest` - Restart all pipeline runs
  - `/test <pipeline_run_name>` or `/retest <pipeline_run_name>` - Restart specific pipeline
  - `/cancel` - Cancel all pipeline runs
  - `/cancel <pipeline_run_name>` - Cancel specific pipeline

- **Example Usage:**
  ```
  This is a comment inside a pull request.
  /cancel
  ```

**For Push Requests (GitHub and GitLab only):**

- **Task:** Add command in commit message comments
  1. Navigate to repository Commits section (GitHub) or History section (GitLab)
  2. Click target commit
  3. Click line number to add comment
  4. Enter command, e.g., `/retest example_pipeline_run`

**Important:** 
- If commit exists in multiple branches, Pipelines as Code uses branch with latest commit
- Commands without branch specification default to main branch
- Include branch specification for specific branch: `/test branch:user-branch`

---

## Track Performance & Status

### Job 6: Monitor Pipeline Run Status and Errors
*When pipeline runs execute, I want to monitor their status, view error details, and track execution progress across different interfaces*

**Personas:** DevOps Engineer, Platform Engineer

→ Lines 326-409: Monitoring pipeline run status using Pipelines as Code

#### 6.1 View Pipeline Status in GitHub App
**Goal:** See high-level pipeline results and task execution times without accessing cluster.

- **Task:** Check GitHub App Checks tab after pipeline completion
  
- **Information Available:**
  - Task duration for each pipeline step
  - Output of `tkn pipelinerun describe` command
  - Error snippets (last 3 lines) from first failed task

**Security Note:** Pipelines as Code masks secrets automatically but cannot hide secrets from workspaces and envFrom sources

#### 6.2 Enable Advanced Error Detection (Platform Engineer)
**Goal:** See detailed error annotations directly on pull requests where failures occurred.

→ Lines 343-373: Annotations for log error snippets

**Technology Preview Feature**

- **Task:** Enable error detection in TektonConfig CR
  ```yaml
  pipelinesAsCode.settings:
    error-detection-from-container-logs: true
  ```

- **Behavior:**
  - Pipelines as Code detects errors from container logs
  - Adds error annotations on pull request at exact location
  - Supports makefile/grep format: `<filename>:<line>:<column>: <error message>`

- **Customization:**
  - Customize regex pattern with `error-detection-simple-regexp` parameter
  - Adjust scan depth with `error-detection-max-number-of-lines` (default: 50 lines)
  - Set `-1` for unlimited lines (increases memory usage)

#### 6.3 Check Pipeline Run History via CLI
**Goal:** View recent pipeline run status and metadata without GitHub UI access.

→ Lines 390-406: Status associated with Repository CRD

- **Task:** Query Repository CRD for recent run status
  ```bash
  oc get repo -n <namespace>
  ```

- **Output Columns:**
  - SUCCEEDED - Success/failure status
  - REASON - Execution result reason
  - STARTTIME - Pipeline start timestamp
  - COMPLETIONTIME - Pipeline completion timestamp

- **Task:** Extract detailed run metadata
  ```bash
  tkn pac describe
  ```

**Context:** Pipelines as Code stores last 5 status messages in Repository custom resource

#### 6.4 View Status for Webhook-Based Pipelines
**Goal:** Monitor pipeline runs triggered via webhooks.

→ Lines 375-376: Status for webhook

- **Behavior:** For webhook-triggered pull requests, Pipelines as Code adds status as comment on pull/merge request

#### 6.5 Monitor Validation Errors and Failures
**Goal:** Identify YAML parsing errors and validation issues.

→ Lines 378-389: Failures and YAML parsing error messages

**YAML Error Reporting:**
- Pipelines as Code detects YAML errors in PipelineRun definitions within `.tekton` directory
- Creates comment on PR describing error when invalid PipelineRun YAML found
- Halts execution of other correctly formatted pipeline runs
- Updates existing error comment if new errors detected
- Logs validation issues in namespace events log and controller log

**Namespace Events:**
- Check Kubernetes events in namespace for failure log messages when Repository CRD matches namespace

**Note:** Validation issues do not halt execution of valid pipeline runs

---

### Job 7: Clean Up Old Pipeline Runs
*When many pipeline runs accumulate in my namespace, I want to automatically retain only a limited number of recent runs*

**Personas:** Platform Engineer

**Why:** Manage resource usage, keep namespace clean, avoid hitting resource limits while retaining sufficient history for troubleshooting

→ Lines 427-447: Cleaning up pipeline runs using Pipelines as Code

#### 7.1 Configure Automatic Cleanup via Annotation
**Goal:** Set retention policy per pipeline to control resource consumption.

- **Task:** Add max-keep-runs annotation to PipelineRun definition
  ```yaml
  metadata:
    annotations:
      pipelinesascode.tekton.dev/max-keep-runs: "<max_number>"
  ```

- **Behavior:**
  - Pipelines as Code cleans up after successful execution
  - Retains only maximum number of pipeline runs configured
  - Skips running pipelines (cleans unknown status)
  - Skips failed pull requests (preserves for debugging)

- **Benefits:**
  - Configure cleanup in under 5 minutes
  - Set different retention policies per pipeline type
  - Ensure failed runs preserved for debugging

---

## Integrate with External Systems

### Job 8: Trigger Pipeline Runs via Incoming Webhooks
*When I need to trigger pipeline runs from external systems or custom automation, I want to use incoming webhook URLs with shared secrets*

**Personas:** DevOps Engineer

**Requires:**
- Repository CRD configured with incoming webhook settings
- Secret created with webhook shared secret
- Git provider type specified (github, gitlab, bitbucket-cloud)
- User token configured

→ Lines 457-519: Using incoming webhook with Pipelines as Code

#### 8.1 Configure Repository for Incoming Webhooks
**Goal:** Set up Repository CRD with incoming webhook configuration.

→ Lines 474-494: Repository CRD with incoming webhook

- **Task:** Define incoming webhook in Repository spec
  ```yaml
  apiVersion: "pipelinesascode.tekton.dev/v1alpha1"
  kind: Repository
  metadata:
    name: repo
    namespace: ns
  spec:
    url: "https://github.com/owner/repo"
    git_provider:
      type: github
      secret:
        name: "owner-token"
    incoming:
      - targets:
        - main
        secret:
          name: repo-incoming-secret
        type: webhook-url
  ```

- **Task:** Create webhook secret
  → Lines 496-507: Secret for incoming webhook
  ```yaml
  apiVersion: v1
  kind: Secret
  metadata:
    name: repo-incoming-secret
    namespace: ns
  type: Opaque
  stringData:
    secret: <very_secure_shared_secret>
  ```

**Note:** When using incoming webhook URLs with GitHub App, token must be specified

#### 8.2 Trigger Pipeline Run via Webhook URL
**Goal:** Execute pipelines from external automation workflows.

→ Lines 509-519: Triggering via incoming webhook

- **Task:** POST to webhook URL with parameters
  ```bash
  curl -X POST 'https://control.pac.url/incoming?secret=very-secure-shared-secret&repository=repo&branch=main&pipelinerun=target_pipelinerun'
  ```

- **Parameters:**
  - `secret` - Shared secret from webhook configuration
  - `repository` - Repository name
  - `branch` - Target branch
  - `pipelinerun` - Specific pipeline run name in `.tekton` directory

- **Behavior:**
  - Pipelines as Code matches incoming URL and treats as push event
  - Pipeline executes in under 5 seconds
  - No status reporting by default

**Important:** To get status reports or notifications:
- Add notifications via `finally` tasks in pipeline
- Inspect Repository CRD with `tkn pac` CLI tool

---

## Appendices

### A. GitOps Commands Quick Reference

| Command | Scope | Use Case |
|---------|-------|----------|
| `/test` | All pipelines | Restart all pipeline runs |
| `/test <name>` | Specific pipeline | Restart named pipeline run |
| `/retest` | All pipelines | Restart all pipeline runs |
| `/retest <name>` | Specific pipeline | Restart named pipeline run |
| `/cancel` | All pipelines | Cancel all running pipelines |
| `/cancel <name>` | Specific pipeline | Cancel named pipeline run |
| `/test tag:<tag>` | All (tag-based) | Trigger all pipelines for tag |
| `/test <name> tag:<tag>` | Specific (tag-based) | Trigger specific pipeline for tag |
| `/ok-to-test` | Authorization | Approve pipeline run from non-authorized PR author |

### B. Authorization Requirements Matrix

| User Type | Pull Request From Default | Pull Request From Other Branch | GitOps Commands |
|-----------|---------------------------|--------------------------------|-----------------|
| Repository owner | ✅ Always allowed | ✅ Always allowed | ✅ All commands |
| Collaborator | ✅ Always allowed | ✅ Always allowed | ✅ All commands |
| Public org member | ✅ Always allowed | ✅ Always allowed | ✅ All commands |
| Listed in OWNERS (approvers/reviewers) | ✅ Always allowed | ✅ Always allowed | ✅ All commands |
| Other users | ⚠️ Requires `/ok-to-test` | ⚠️ Requires `/ok-to-test` | ❌ Not authorized |

### C. Monitoring Options Decision Guide

| Interface | Best For | Access Required | Information Depth | Real-time |
|-----------|----------|-----------------|-------------------|-----------|
| GitHub App Checks tab | Quick status review | GitHub UI access | Medium | No |
| tkn pac logs | Real-time troubleshooting | CLI + cluster access | High | Yes |
| Repository CRD | Recent run history | CLI + cluster access | Medium | No |
| Webhook comments | Webhook-triggered PRs | GitHub/GitLab UI | Low | No |
| Error annotations (Tech Preview) | Detailed error location | Configured in TektonConfig | High | No |

### D. Workflow Coverage Analysis

| Stage | Coverage | Jobs | Notes |
|-------|----------|------|-------|
| Configure | ✅ | Job 1 | Pipeline definition validation |
| Deploy | ✅ | Jobs 2, 3, 4, 8 | Automatic execution, tag-based triggering, webhooks |
| Operate | ✅ | Jobs 5, 7 | Restart/cancel, cleanup |
| Monitor | ✅ | Job 6 | Status monitoring, error detection, run history |
| Troubleshoot | ⚠️ Limited | Job 6 (partial) | Error detection and logging, no dedicated troubleshooting guide |
| Upgrade | ❌ | - | No upgrade or migration content |
| Reference | ⚠️ Limited | - | Some CLI reference embedded, no comprehensive reference |

### E. Gaps Identified

| Stage | Gap | Recommendation |
|-------|-----|----------------|
| Troubleshoot | No dedicated troubleshooting procedures | Add common failure scenarios and resolution steps |
| Upgrade | No upgrade procedures for Pipelines as Code | Add version upgrade section |
| Reference | No comprehensive CLI reference | Add complete `tkn pac` command reference |
| Configure | No pipeline definition best practices | Add section on annotation patterns and configuration guidelines |
| Secure | No security hardening guidance | Add RBAC configuration and secret management best practices |

---

## Navigation Guide

### By User Journey

**Pipeline Developer setting up new pipeline:**
1. Job 1: Verify pipeline run definitions
2. Job 2: Execute pipeline runs automatically on Git events
3. Job 6: Monitor pipeline run status and errors

**DevOps Engineer managing release pipeline:**
1. Job 3: Trigger pipeline runs on Git tags
2. Job 4: Trigger pipeline runs using GitOps commands on tags
3. Job 6: Monitor pipeline run status and errors
4. Job 5: Restart or cancel pipeline runs (if needed)

**Platform Engineer implementing automation:**
1. Job 8: Trigger pipeline runs via incoming webhooks
2. Job 6.2: Enable advanced error detection
3. Job 7: Clean up old pipeline runs

**DevOps Engineer troubleshooting failed pipeline:**
1. Job 6: Monitor pipeline run status and errors
2. Job 5: Restart or cancel pipeline runs
3. Job 2.2: Monitor pipeline execution via CLI

---

## Document Statistics

**Workflow Coverage:**
- Configure: 1 job
- Deploy: 4 jobs
- Operate: 2 jobs
- Monitor: 1 job
- Troubleshoot: Limited (embedded in monitoring)
- Upgrade: Gap identified
- Reference: Limited (embedded content)

**Main Jobs:** 8
**User Stories/Sub-tasks:** 18 themed sections
**Source Sections:** 10 major sections referenced
**Supported Git Providers:** GitHub App, GitHub Webhook, GitLab (tag support); Bitbucket Cloud (webhook support)

**Technology Preview Features:**
- Using comments to start pipelines not matching events
- Error detection from container logs with annotations

---

## Additional Resources

**Example Implementations:**
- `.tekton/` directory in Pipelines as Code repository
- Slack notification task for success/failure
- Pipeline run with finally tasks on push events
- git-clone task for private repositories

**Related Documentation:**
- Creating applications using Developer perspective (OpenShift)
- Kubernetes OWNERS file specification
- GitHub Checks API documentation

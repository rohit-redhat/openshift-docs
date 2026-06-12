# OpenShift Pipelines 1.22 Release Notes
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** Help users understand new features, improvements, bug fixes, and breaking changes in OpenShift Pipelines 1.22 to plan upgrades and adopt new capabilities.

**Personas:** Platform Administrator, Security Engineer, CI/CD Engineer, DevOps Engineer, Developer

**Main Jobs:** 59 core jobs across 9 workflow stages

---

## Quick Navigation

**I want to:**
- Check compatibility with my OpenShift version → Job 1 (EVALUATE)
- Understand breaking changes before upgrading → Jobs 24, 58, 59 (MIGRATE)
- Improve pipeline security → Jobs 2, 3, 16 (USE)
- Optimize pipeline performance → Jobs 4, 8, 11, 12, 18, 30, 37 (OPTIMIZE)
- Use array values in conditional logic → Job 5 (USE)
- Add display names to steps → Job 6 (USE)
- Execute embedded pipelines → Job 7 (USE)
- Handle PVC quota limits → Job 9 (USE)
- Override task timeouts → Job 10 (USE)
- Configure multi-cluster mode → Jobs 20, 21, 22, 23 (EVALUATE/OPTIMIZE/USE)
- Use CEL expressions in PAC → Job 17 (USE)
- Troubleshoot buildah-ns task failures → Job 25 (TROUBLESHOOT)
- Fix issues with resolved content → Jobs 26-57 (TROUBLESHOOT)

---

# Table of Contents

## Evaluate Platform Readiness

### Job 1: Verify Platform Compatibility for OpenShift Pipelines 1.22
*When planning to deploy or upgrade to OpenShift Pipelines 1.22*

**Personas:** Platform Administrator

**Goal:** Confirm that OpenShift Pipelines 1.22 is compatible with my OpenShift Container Platform version and understand component support status.

→ Lines 89-124: Compatibility matrix
  Source: Compatibility and support matrix section

**What you'll verify:**
- OpenShift version is listed in compatibility matrix (4.14 through 4.21)
- Component versions are known and supported
- Technology Preview vs GA status is clear for each component

**Key components:**
- Pipelines Operator 1.22
- Tekton Pipelines 1.9.x
- Tekton Triggers 0.35.x
- Tekton CLI 0.44.x
- Tekton Chains 0.26.x (GA)
- Tekton Hub 1.23.x (Technology Preview)
- Pipelines as Code 0.42.x (GA)
- Tekton Results 0.18.x (GA)
- Manual Approval Gate 0.8.x (Technology Preview)
- Tekton Pruner 0.3.x (GA)
- Tekton Cache 0.3.x (GA)

---

### Job 20: Configure Multi-Cluster Mode in TektonConfig (Technology Preview)
*When planning multi-cluster Pipelines deployment*

**Personas:** Platform Administrator

**Goal:** Enable and configure multi-cluster setup with Hub or Spoke role.

→ Lines 320-337: Multi-cluster configuration
  Source: New features - Multi-cluster section

**Configuration options:**
- Set `multi-cluster-disabled: false` to enable multi-cluster mode
- Configure `multi-cluster-role` as `Hub` or `Spoke`
- Integrate with Tekton Scheduler for resource management

**Key capabilities:**
- Centralized Results API on Hub
- Distributed execution on Spoke clusters
- Multi-cluster pipeline management

**Note:** Technology Preview feature - not for production use

---

## Enhance Pipeline Security

### Job 2: Isolate User Namespaces for TaskRuns and PipelineRuns on OpenShift 4.20+
*When securing pipeline workloads with Kubernetes-native user namespace isolation*

**Personas:** Security Engineer

**Goal:** Configure hostUsers in podTemplate to control host user namespace sharing without legacy CRI-O annotations.

→ Lines 148-151: hostUsers support in podTemplate
  Source: New features - Pipelines section

**What's enabled:**
- `hostUsers` setting works in podTemplate
- User namespace isolation effective on OpenShift 4.20+
- No need for legacy CRI-O annotations (removed in OpenShift 4.20)

**Implementation:**
- Set `hostUsers: false` in TaskRun or PipelineRun podTemplate
- Kubernetes-native approach replaces `io.kubernetes.cri-o.userns-mode` annotation

---

### Job 3: Verify HTTP Resolver Content Integrity with Hash Parameter
*When fetching pipeline resources from HTTP sources*

**Personas:** DevOps Engineer

**Goal:** Ensure fetched content matches expected hash to prevent tampering or corruption.

→ Lines 153-156: HTTP resolver hash parameter
  Source: New features - Pipelines section

**Security features:**
- `hash` parameter supports SHA-256 and SHA-512
- Content verification works after fetch
- Improved security for HTTP resources similar to git resolver

---

### Job 16: Enforce Webhook Signature Validation for Forgejo and Gitea Providers
*When using Pipelines as Code with Forgejo or Gitea VCS providers*

**Personas:** Security Engineer

**Goal:** Ensure incoming webhook requests are validated and authenticated from trusted sources.

→ Lines 281-284: Webhook signature validation
  Source: New features - Pipelines as Code section

**Security improvements:**
- Webhook signature validation enabled for Forgejo
- Webhook signature validation enabled for Gitea
- Unauthenticated requests rejected
- Spoofed requests prevented

---

## Configure Pipeline Behavior

### Job 4: Reduce Remote Resource Fetches and Avoid API Rate Limits with Resolver Caching
*When running pipelines that repeatedly fetch the same remote resources*

**Personas:** CI/CD Engineer

**Goal:** Enable resolver caching to minimize redundant fetches and prevent API rate limit errors.

→ Lines 158-167: Resolver caching
  Source: New features - Pipelines section

**Configuration modes:**
- **auto** - Cache enabled automatically (default recommended)
- **always** - Cache always used
- **never** - Cache disabled

**Supported resolvers:**
- Bundle resolver
- Git resolver
- Cluster resolver

**Benefits:**
- Reduced external API calls
- API rate limit errors prevented
- Improved pipeline performance

---

### Job 5: Use Array Values in When Expression Inputs for Conditional Logic
*When building pipelines with conditional task execution based on array parameters or results*

**Personas:** CI/CD Engineer

**Goal:** Evaluate array values in when expression inputs to enable flexible conditional logic.

→ Lines 169-172: Array values in when expressions
  Source: New features - Pipelines section

**What's supported:**
- Array values work in when expression `input` attribute
- Array-based conditions function correctly
- Improved conditional pipeline logic with array parameters

---

### Job 6: Add Display Names to Pipeline Steps for Better Readability
*When creating or maintaining Task definitions for CI/CD pipelines*

**Personas:** Developer

**Goal:** Add human-readable display names to steps that improve pipeline monitoring and readability.

→ Lines 174-177: displayName field for Step objects
  Source: New features - Pipelines section

**Features:**
- `displayName` field available on Step objects
- Display names appear in UI and monitoring
- Steps easier to identify in console

---

### Job 7: Execute Embedded Pipelines Within Pipelines
*When building complex pipeline workflows that require nested pipeline execution*

**Personas:** CI/CD Engineer

**Goal:** Use PipelineSpec field under tasks to execute embedded pipelines directly.

→ Lines 179-182: Embedded pipelines via PipelineSpec
  Source: New features - Pipelines section

**Capabilities:**
- `PipelineSpec` field available under tasks
- Embedded pipelines execute correctly
- Pipelines-in-pipelines functionality for complex workflows

---

### Job 10: Override Individual Task Timeouts at PipelineRun Level
*When managing pipeline executions where different tasks need different timeout values*

**Personas:** CI/CD Engineer

**Goal:** Set specific timeout values for individual tasks using spec.taskRunSpecs[].timeout field.

→ Lines 194-197: Per-task timeout override
  Source: New features - Pipelines section

**Configuration:**
- Use `spec.taskRunSpecs[].timeout` field in PipelineRun
- Individual task timeouts honored
- Overall PipelineRun timeout remains separate

**Benefit:** Tasks with varying execution times can have appropriate timeout limits

---

## Optimize Pipeline Performance

### Job 8: Reduce TaskRun Startup Time with Concurrent StepAction Resolution
*When running TaskRuns that use multiple remote StepActions*

**Personas:** DevOps Engineer

**Goal:** Benefit from concurrent StepAction resolution to minimize startup delays.

→ Lines 184-187: Concurrent StepAction resolution
  Source: New features - Pipelines section

**Performance improvements:**
- StepActions resolved concurrently not sequentially
- Reduced TaskRun startup time
- Improved pipeline performance with multiple remote StepActions

---

### Job 9: Handle PVC Quota Limits Gracefully Without Immediate PipelineRun Failure
*When operating in environments with PVC quota limits*

**Personas:** Platform Administrator

**Goal:** Allow PipelineRuns to requeue and retry when PVC quota is hit instead of failing immediately.

→ Lines 189-192: PVC quota limit handling
  Source: New features - Pipelines section

**Resilience features:**
- PipelineRun requeued when PVC creation hits quota
- Runs succeed when quota becomes available
- Runs timeout only after configured timeout period
- No immediate failures on temporary quota issues

---

### Job 11: Enable Automatic Metrics Discovery for Tekton Results and Pipelines Webhook
*When setting up monitoring and alerting for Pipelines components*

**Personas:** Platform Administrator

**Goal:** Use automatically created ServiceMonitor resources for Prometheus Operator integration.

→ Lines 202-205: Automatic ServiceMonitor creation
  Source: New features - Pipelines section

**What's automated:**
- ServiceMonitor created for tekton-results
- ServiceMonitor created for tekton-pipelines-webhook
- Prometheus automatically discovers metrics endpoints
- No manual ServiceMonitor creation required

---

### Job 12: Reduce VCS API Load with Pipelines as Code File Caching
*When using PAC with path-based filtering that makes many API calls*

**Personas:** CI/CD Engineer

**Goal:** Enable caching of changed files per event to minimize VCS API calls and avoid rate limits.

→ Lines 210-213: PAC file caching
  Source: New features - Pipelines as Code section

**Caching behavior:**
- Changed files cached per event
- `path.pathChanged()` evaluations use cache
- `on-path-change` annotations use cache
- Reduced API rate limit risk

---

### Job 18: Improve Pipelines as Code Performance with Batched GitHub GraphQL API Calls
*When using PAC with GitHub or GitHub Enterprise with many .tekton files*

**Personas:** DevOps Engineer

**Goal:** Benefit from batched GraphQL API calls that reduce GitHub API call count.

→ Lines 299-302: GitHub GraphQL batching
  Source: New features - Pipelines as Code section

**Performance improvements:**
- Multiple .tekton files fetched in single request
- Reduced GitHub API call count
- Improved performance with many pipeline files
- Reduced API rate limit risk

---

### Job 21: Optimize Hub Cluster Resources with Automatic Results Scaling in Multi-Cluster Mode (Technology Preview)
*When operating multi-cluster Hub with centralized Results API*

**Personas:** Platform Administrator

**Goal:** Reduce Hub cluster resource usage by automatically scaling down watcher and retention-policy-agent to zero replicas.

→ Lines 339-342: Automatic Results scaling on Hub
  Source: New features - Multi-cluster section

**Resource optimization:**
- `watcher` replicas set to 0 on Hub
- `retention-policy-agent` replicas set to 0 on Hub
- Resource usage reduced (components only needed on Spoke)
- Results API remains operational

**Note:** Technology Preview feature

---

### Job 30: Reduce Controller Reconciliation Load for Runs Without Timeouts
*When operating pipelines controller with many running TaskRuns and PipelineRuns*

**Personas:** Platform Administrator

**Goal:** Ensure runs without timeout configurations do not cause excessive reconciliation loops.

→ Lines 416-419: Reconciliation optimization
  Source: Resolved issues section

**Improvements:**
- Reconciliation only on actual changes
- Reduced CPU usage on controller
- Improved cluster performance and scalability
- Fixed excessive reconciliation for runs without timeouts

---

### Job 37: Reduce API Server Load from PipelineRun Status Updates
*When operating large-scale pipelines with many status updates*

**Personas:** Platform Administrator

**Goal:** Ensure consistent array ordering in PipelineRun status to reduce invalid status updates.

→ Lines 451-454: Status update optimization
  Source: Resolved issues section

**Fixes:**
- Array ordering consistent in status
- Reduced invalid status updates
- Improved API server performance
- Better cluster stability

---

## Use Pipelines Features

### Job 13: Reduce Comment Noise with Update Comment Strategy for GitLab and GitHub
*When managing Pipelines as Code with GitLab or GitHub webhooks*

**Personas:** CI/CD Engineer

**Goal:** Maintain single status comment per PipelineRun that updates instead of creating multiple comments.

→ Lines 216-219: Update comment strategy
  Source: New features - Pipelines as Code section

**Features:**
- `update` comment strategy available
- Single comment updated with new status
- Comment includes current commit SHA
- Reduced repository comment clutter

---

### Job 14: Skip Pipeline Execution for Work-in-Progress Commits with Commit Message Tags
*When pushing work-in-progress or minor commits that should not trigger pipelines*

**Personas:** Developer

**Goal:** Use commit message tags to skip pipeline execution and save resources.

→ Lines 221-240: Commit skip tags
  Source: New features - Pipelines as Code section

**Supported tags (case-insensitive):**
- `[skip ci]`
- `[ci skip]`
- `[skip tkn]`
- `[tkn skip]`

**Behavior:**
- Pipeline execution skipped for tagged commits
- Works on all supported VCS providers
- Resource savings for WIP commits

**GitLab note:** May generate extra list entry due to API response format

---

### Job 15: Use Glob Patterns for GitHub App Token Scoping in Pipelines as Code
*When managing many private Git submodules with GitHub App*

**Personas:** CI/CD Engineer

**Goal:** Grant token access to multiple repositories using wildcard patterns in single configuration.

→ Lines 243-278: Glob patterns for GitHub App scoping
  Source: New features - Pipelines as Code section

**Pattern support:**
- Glob patterns supported in `secret-github-app-scope-extra-repos`
- Patterns like `owner/*` work
- Works in global config maps and Repository CR

**Configuration locations:**
- Repository CR: `github_app_token_scope_repos` field
- Global ConfigMap: `secret-github-app-scope-extra-repos` field

**Benefit:** Simplified management of many private submodules

---

### Job 17: Use CEL Expressions in Pipelines as Code Pipeline Templates
*When creating dynamic pipeline templates in Pipelines as Code*

**Personas:** CI/CD Engineer

**Goal:** Use `cel:` prefix to evaluate Common Expression Language expressions inline in templates.

→ Lines 287-297: CEL expressions in templates
  Source: New features - Pipelines as Code section

**CEL capabilities:**
- Use `cel:` prefix in templates
- Perform ternary operations
- Perform presence checks
- Compose complex strings
- Access to `body`, `headers`, `files`, `pac` namespaces

**Example use cases:**
- Conditional pipeline parameters
- Dynamic resource generation
- Complex template logic

---

### Job 19: View ANSI Color Codes in OpenShift Console Log Viewer
*When viewing TaskRun and PipelineRun logs in OpenShift console*

**Personas:** Developer

**Goal:** See colored logs with ANSI color code support for better readability.

→ Lines 307-310: ANSI color code support
  Source: New features - OpenShift Pipelines console section

**Features:**
- ANSI color codes rendered in console
- Logs more readable
- Better visual distinction in output
- Improved log level visibility

---

### Job 22: Install and Manage Tekton Scheduler with Pipelines Operator (Technology Preview)
*When setting up resource allocation and queuing for pipelines*

**Personas:** Platform Administrator

**Goal:** Deploy Tekton Scheduler (Tekton-Kueue) using Pipelines Operator for pipeline resource management.

→ Lines 344-351: Tekton Scheduler management
  Source: New features - Multi-cluster section

**Configuration:**
- `scheduler` section available in TektonConfig CR
- Scheduler installation managed by operator
- Default queue name configurable
- Multi-cluster support available

**Prerequisite:** Upstream Kueue must be installed separately

**Note:** Technology Preview feature

---

### Job 23: Differentiate Federated PipelineRuns in Multi-Cluster UI (Technology Preview)
*When viewing PipelineRuns in multi-cluster UI*

**Personas:** DevOps Engineer

**Goal:** Visually distinguish between local Hub PipelineRuns and federated PipelineRuns using icon indicator.

→ Lines 353-356: Federated PipelineRun visual indicator
  Source: New features - Multi-cluster section

**Features:**
- Icon differentiates local vs federated PipelineRuns
- `managedBy` field evaluated
- Clear visual distinction in UI
- Improved multi-cluster visibility

**Note:** Technology Preview feature

---

## Troubleshoot Issues

### Job 24: Enable Console Plugin Explicitly After Upgrading to Pipelines 1.22
*When upgrading to OpenShift Pipelines 1.22 with console plugin changes*

**Personas:** Platform Administrator
**Timing:** DURING upgrade to 1.22 - console plugin requires explicit enablement

**Goal:** Understand that console plugin must be explicitly enabled for Pipelines section to appear.

→ Lines 363-368: Console plugin explicit enablement
  Source: Breaking changes section

**What changed:**
- Console plugin requires explicit enablement
- Legacy static console plugin deprecated
- Pipelines navigation not visible by default after upgrade

**Action required:** Enable console plugin in TektonConfig

---

### Job 25: Work Around buildah-ns Task Failure on OpenShift 4.20+
*When using buildah-ns task on OpenShift 4.20 or later*

**Personas:** CI/CD Engineer

**Goal:** Use standard buildah task with `hostUsers: false` in PodTemplate to enable user namespaces.

→ Lines 373-378: buildah-ns task workaround
  Source: Known issues section

**Workaround:**
- Use standard `buildah` task instead of `buildah-ns`
- Set `hostUsers: false` in PodTemplate
- User namespace support via Kubernetes-native mechanism
- No dependency on removed CRI-O annotations

**Root cause:** CRI-O annotation `io.kubernetes.cri-o.userns-mode` removed in OpenShift 4.20

---

### Job 26: Understand tkn CLI Limitations in Multicluster Environments
*When operating tkn CLI tool in multicluster Hub and Spoke setup*

**Personas:** DevOps Engineer

**Goal:** Recognize which tkn commands do not work correctly in multicluster and use alternatives.

→ Lines 380-392: tkn CLI multicluster limitations
  Source: Known issues section

**Commands that fail on Hub:**
- `tkn taskrun list` - fails on Hub
- `tkn pipelinerun describe` - fails
- `tkn pipelinerun logs` - fails
- `tkn pipelinerun cancel` - fails

**Spoke limitations:**
- `pipelinerun list` and `taskrun list` only work during run execution

**Workaround:** Use OpenShift console or oc commands for multicluster management

---

### Job 27: Work Around opc results logs get Command Line Limit
*When retrieving logs from Tekton Results with more than 300 lines*

**Personas:** DevOps Engineer

**Goal:** Use `opc results pipelinerun logs` or `opc results taskrun logs` commands for complete output.

→ Lines 394-399: opc results logs workaround
  Source: Known issues section

**Issue:**
- `opc results logs get` limited to 300 lines
- Cannot view complete logs

**Workaround:**
- Use `opc results pipelinerun logs` for complete PipelineRun logs
- Use `opc results taskrun logs` for complete TaskRun logs

**Note:** `logs get` command deprecated

---

### Job 28: Ensure Affinity Assistant Pods Inherit Correct Service Account
*When using affinity assistant to co-schedule tasks with shared workspaces*

**Personas:** Platform Administrator

**Goal:** Verify Affinity Assistant pods use PipelineRun service account instead of default service account.

→ Lines 406-409: Affinity Assistant service account fix
  Source: Resolved issues section

**Fix applied:**
- Affinity Assistant inherits PipelineRun service account
- Correct SCC permissions applied
- PipelineRuns with workspaces start successfully

---

### Job 29: Identify TaskRun Pod Configuration Errors Early with Clear Error Messages
*When TaskRuns failing to start due to missing config maps or secrets*

**Personas:** DevOps Engineer

**Goal:** Receive immediate clear error messages identifying specific configuration issues.

→ Lines 411-414: Early TaskRun pod configuration errors
  Source: Resolved issues section

**Improvements:**
- TaskRun fails immediately with clear error
- Specific missing resource identified (config map or secret)
- No timeout waiting for generic error
- Faster troubleshooting

---

### Job 31: Use Parameter References in Pipeline Parameter Defaults
*When defining pipeline parameters with fallback patterns*

**Personas:** CI/CD Engineer

**Goal:** Reference other parameters in default values to enable flexible fallback patterns.

→ Lines 421-424: Parameter references in defaults
  Source: Resolved issues section

**What's fixed:**
- Parameter defaults support references to other parameters
- Arbitrary dependency chains work
- Circular dependencies detected with clear errors
- All parameter types supported (string, array, object)

**Previous issue:** Literal strings used instead of resolved values, causing task pod creation failures

---

### Job 32: Improve PipelineRun Resilience to Retryable TaskRef Errors
*When running PipelineRuns that reference remote tasks*

**Personas:** DevOps Engineer

**Goal:** Ensure PipelineRuns retry on retryable TaskRef reconciliation errors instead of failing.

→ Lines 426-429: TaskRef error resilience
  Source: Resolved issues section

**Improvements:**
- PipelineRuns retry on retryable errors
- Only explicit validation errors cause failure
- Improved resilience to transient issues

---

### Job 33: Use Kubernetes-Native Sidecars with Proper Signal Handling
*When running TaskRuns with Kubernetes-native sidecars*

**Personas:** DevOps Engineer

**Goal:** Ensure sidecars handle signals correctly and operate reliably.

→ Lines 431-434: Sidecar signal handling fix
  Source: Resolved issues section

**Fixes:**
- Signal handling added to SidecarLog results
- No repeated init container restarts
- Sidecars operate reliably

---

### Job 34: Inspect Timed-Out TaskRun Pods When keep-pod-on-cancel Enabled
*When debugging timed-out TaskRuns with keep-pod-on-cancel feature flag*

**Personas:** DevOps Engineer

**Goal:** Ensure pods are retained for timed-out TaskRuns for debugging purposes.

→ Lines 436-439: Pod retention on timeout fix
  Source: Resolved issues section

**Fix:**
- `keep-pod-on-cancel` feature flag honored
- Pods retained on timeout
- Can inspect pod state for debugging

---

### Job 35: View StepAction Status in Correct Chronological Order
*When reviewing task execution timeline using StepAction*

**Personas:** DevOps Engineer

**Goal:** See status steps displayed in correct sequential order for accurate interpretation.

→ Lines 441-444: StepAction chronological ordering
  Source: Resolved issues section

**Fix:**
- Status steps in correct order
- Chronological flow clear
- Accurate execution timeline

---

### Job 36: Run TaskRuns Successfully on arm64 Clusters
*When operating TaskRuns on arm64 Kubernetes clusters*

**Personas:** DevOps Engineer

**Goal:** Ensure TaskRuns execute reliably on arm64 architecture without platform variant issues.

→ Lines 446-449: arm64 platform support fix
  Source: Resolved issues section

**Fix:**
- TaskRuns succeed on arm64 clusters
- Entrypoint handles Linux platform variants
- No architecture-specific failures

---

### Job 38: Ensure Operator Webhooks Are Cleaned Up When Namespace Is Deleted
*When uninstalling Pipelines Operator by deleting openshift-pipelines namespace*

**Personas:** Platform Administrator

**Goal:** Verify all operator webhooks are removed with proper owner references.

→ Lines 459-462: Webhook cleanup on namespace deletion
  Source: Resolved issues section

**Fix:**
- Owner references added to all webhooks
- Webhooks cleaned up on namespace deletion
- No orphaned webhooks remain on cluster

**Webhooks affected:**
- `proxy.operator.tekton.dev`
- `validation.pipelinesascode.tekton.dev`
- `namespace.operator.tekton.dev`

---

### Job 39: Fix Prometheus Metrics Collection When Operator Installed in Custom Namespace
*When Pipelines Operator installed in non-default namespace like openshift-pipelines*

**Personas:** Platform Administrator

**Goal:** Ensure ServiceMonitor targets correct namespace for metrics scraping.

→ Lines 464-467: ServiceMonitor namespace fix
  Source: Resolved issues section

**Fix:**
- ServiceMonitor auto-targets operator namespace
- No hardcoded `openshift-operators` namespace reference
- Prometheus metrics collection works
- No `PrometheusKubernetesListWatchFailures` alerts

---

### Job 40: Use Custom Parameters in Pipelines as Code CEL Expressions
*When defining repository-specific parameters for event filtering in PAC*

**Personas:** CI/CD Engineer

**Goal:** Reference custom parameters from Repository CR in `on-cel-expression` annotations.

→ Lines 473-508: Custom parameters in CEL
  Source: Resolved issues - Pipelines as Code section

**Fix:**
- Custom parameters exposed as CEL variables
- Parameters usable in CEL expressions
- Standard variables take precedence on conflicts

**Configuration:** Define parameters in Repository CR `params` field

---

### Job 41: Skip CI Execution for Commits with [skip ci] Tag in GitLab Merge Requests
*When using GitLab with Pipelines as Code for MR automation*

**Personas:** CI/CD Engineer

**Goal:** Ensure `[skip ci]` commit messages are honored and PipelineRuns are not created.

→ Lines 511-514: GitLab skip ci tag support
  Source: Resolved issues - Pipelines as Code section

**Fix:**
- `[skip ci]` tag recognized in commit messages
- Pipeline execution skipped
- Unnecessary runs prevented

---

### Job 42: Resolve Tasks from Custom Hub Catalogs with Version Specifiers
*When using custom hub catalogs with versioned task references*

**Personas:** CI/CD Engineer

**Goal:** Use versioned catalog references like `foo://resource:1.2` without invalid port errors.

→ Lines 516-519: Custom catalog version resolution fix
  Source: Resolved issues - Pipelines as Code section

**Fix:**
- Non-HTTP(S) schemes supported
- Version specifiers parsed correctly
- Custom catalog resolution works
- No invalid port errors

---

### Job 43: Use tkn pac cel Command with Required Flags and Clear Errors
*When testing CEL expressions with tkn pac cel command*

**Personas:** DevOps Engineer

**Goal:** Receive clear error messages when required flags are missing.

→ Lines 521-524: tkn pac cel error messaging
  Source: Resolved issues - Pipelines as Code section

**Improvements:**
- Body (`-b`) and header (`-H`) flags mandatory
- Clear error messages for missing arguments
- No misleading auto-detection failed errors
- No unexpected end of JSON input errors

---

### Job 44: Reliably Populate pull_request_number Variable for Push Events
*When push events associated with pull request merges*

**Personas:** CI/CD Engineer

**Goal:** Ensure `pull_request_number` variable is populated even with GitHub API indexing delays.

→ Lines 526-529: pull_request_number reliability fix
  Source: Resolved issues - Pipelines as Code section

**Fix:**
- Exponential backoff retry mechanism in place
- `pull_request_number` populated reliably
- Works with merge commit strategy
- Handles GitHub API indexing delays

---

### Job 45: Evaluate All Modified Files in GitLab Push Events for Trigger Filtering
*When using file-based filtering in Pipelines as Code with GitLab*

**Personas:** CI/CD Engineer

**Goal:** Ensure all modified files are evaluated not just first 20 due to API pagination.

→ Lines 531-534: GitLab file pagination fix
  Source: Resolved issues - Pipelines as Code section

**Fix:**
- API pagination implemented
- All modified files retrieved
- `files` CEL variable complete
- `pathChanged()` method accurate

---

### Job 46: View Accurate GitLab Commit Statuses Throughout Pipeline Lifecycle
*When using Pipelines as Code with GitLab forked merge requests*

**Personas:** CI/CD Engineer

**Goal:** See correct pending and running statuses in GitLab for `/ok-to-test` approval workflow.

→ Lines 536-539: GitLab status mapping fix
  Source: Resolved issues - Pipelines as Code section

**Fix:**
- Pending state displayed before approval
- Running state after pipeline starts
- Parent status entry updated
- Accurate status throughout lifecycle

---

### Job 47: Reduce GitLab Merge Request Comment Noise with Permission-Based Fallback
*When using Pipelines as Code with GitLab with restricted permissions*

**Personas:** CI/CD Engineer

**Goal:** Only post fallback comments when commit status update fails due to permissions.

→ Lines 541-544: GitLab comment fallback fix
  Source: Resolved issues - Pipelines as Code section

**Fix:**
- Fallback comments only on permission failures
- No misleading "pipeline run started" comments
- Reduced comment noise

---

### Job 48: Handle Invalid GitLab Input in tkn pac cel Command Safely
*When testing CEL expressions with GitLab provider*

**Personas:** DevOps Engineer

**Goal:** Receive descriptive errors instead of nil pointer dereference panic.

→ Lines 546-549: tkn pac cel GitLab error handling
  Source: Resolved issues - Pipelines as Code section

**Fix:**
- Input validation before processing
- Descriptive error messages
- No panic on malformed input
- Can handle malformed payloads or headers

---

### Job 49: Re-Evaluate /ok-to-test Approvals Per Commit When remember-ok-to-test Is False
*When reviewing pull requests from unauthorized users with security controls*

**Personas:** Security Engineer

**Goal:** Ensure each new commit requires fresh `/ok-to-test` approval when `remember-ok-to-test=false`.

→ Lines 551-554: ok-to-test re-evaluation fix
  Source: Resolved issues - Pipelines as Code section

**Fix:**
- Permissions re-evaluated per commit
- Single approval not retained
- CI blocked until new approval
- Security policy enforced correctly

---

### Job 50: View Correct Logging for Intentionally Skipped Push Events
*When operating Pipelines as Code with push events associated with open PRs*

**Personas:** DevOps Engineer

**Goal:** See info-level logging for skipped events instead of error-level.

→ Lines 557-560: Skipped event logging level fix
  Source: Resolved issues - Pipelines as Code section

**Fix:**
- Skipped push events logged at info level
- No confusing error logs
- Expected behavior clearly logged

---

### Job 51: View Individual Status for Each PipelineRun in Bitbucket Cloud Pull Requests
*When running multiple pipelines per pull request in Bitbucket Cloud*

**Personas:** CI/CD Engineer

**Goal:** See individual commit status for each PipelineRun instead of single overwritten status.

→ Lines 562-565: Bitbucket Cloud unique status keys
  Source: Resolved issues - Pipelines as Code section

**Fix:**
- Unique commit status key per PipelineRun
- Format: `ApplicationName / PipelineRunName`
- All pipeline results visible
- No status overwriting

---

### Job 52: Trigger Pipelines Based on Label Conditions Using CEL Expressions
*When building event-driven pipelines that respond to pull request labeling*

**Personas:** CI/CD Engineer

**Goal:** Ensure `on-cel-expression` annotations are evaluated during PR labeling events.

→ Lines 568-571: CEL label evaluation fix
  Source: Resolved issues - Pipelines as Code section

**Fix:**
- CEL expressions evaluated on label events
- AST inspection detects label references
- Pipelines trigger on label conditions
- No need for `on-label` annotation workaround

---

### Job 53: Update Git Provider Status When PipelineRuns Are Deleted or Canceled
*When managing PipelineRuns that are deleted while running or queued*

**Personas:** DevOps Engineer

**Goal:** Ensure Git provider commit status shows canceled instead of stuck in pending.

→ Lines 573-576: PipelineRun deletion status update
  Source: Resolved issues - Pipelines as Code section

**Fix:**
- Finalizer reports canceled status to Git provider
- Commit status updated on deletion
- No indefinite pending status
- Works for Running and Queued states

---

### Job 54: View Pipeline Logs with Preserved Whitespace and Horizontal Scrolling
*When viewing structured log output and tabular data in OpenShift console*

**Personas:** DevOps Engineer

**Goal:** See logs with preserved whitespace and horizontal scrolling for long lines.

→ Lines 582-585: Log whitespace preservation
  Source: Resolved issues - OpenShift Pipelines console section

**Fix:**
- Whitespace preserved in logs
- Horizontal scrolling available
- Structured output aligned correctly
- Tabular data readable

---

### Job 55: Access TaskSidebar Correctly in Pipeline Builder
*When using Pipeline Builder in OpenShift console*

**Personas:** Developer

**Goal:** View TaskSidebar overlay with correct styling and accessibility.

→ Lines 587-590: TaskSidebar rendering fix
  Source: Resolved issues - OpenShift Pipelines console section

**Fix:**
- TaskSidebar renders above other elements
- Required styling applied
- Sidebar accessible
- Header and content visible

---

## Plan Migration & Deprecation

### Job 56: Plan Migration from openshift-pipelines-client RPM
*When using openshift-pipelines-client RPM for tkn CLI*

**Personas:** Platform Administrator
**Timing:** BEFORE Pipelines 1.23 - RPM will be removed

**Goal:** Identify alternative distribution method before RPM is removed in 1.23.

→ Lines 598-600: RPM deprecation notice
  Source: Deprecation notices section

**What's changing:**
- `openshift-pipelines-client` RPM deprecated
- Will be removed in Pipelines 1.23
- Need alternative tkn CLI distribution

**Action required:** Plan migration to alternative tkn CLI installation method

---

### Job 57: Stop Using pipelinerun_status Field in Repository CR
*When using Pipelines as Code Repository custom resources*

**Personas:** CI/CD Engineer
**Timing:** BEFORE Pipelines 1.23 - field will be removed

**Goal:** Update configurations to avoid `pipelinerun_status` field before removal in 1.23.

→ Lines 602-605: pipelinerun_status deprecation
  Source: Deprecation notices - Pipelines as Code section

**What's changing:**
- `pipelinerun_status` field deprecated in Repository CR
- Will be removed in Pipelines 1.23
- Need to update integrations

**Action required:** Identify alternative approach and update configurations

---

### Job 58: Migrate from disable-affinity-assistant to coschedule Feature Flag
*When upgrading to Pipelines 1.22 with affinity assistant configuration*

**Personas:** Platform Administrator
**Timing:** DURING upgrade to 1.22 - breaking change in configuration

**Goal:** Update TektonConfig to use `coschedule` feature flag instead of removed `disable-affinity-assistant` field.

→ Lines 610-613: disable-affinity-assistant removal
  Source: Breaking changes section

**What changed:**
- `disable-affinity-assistant` field removed from TektonConfig
- Replaced with `coschedule` feature flag
- Breaking change in configuration format

**Migration steps:**
1. Remove `disable-affinity-assistant` from TektonConfig
2. Configure `coschedule` feature flag instead
3. Verify affinity assistant behavior

---

### Job 59: Migrate from Public Tekton Hub to Custom Self-Hosted Hub or Alternative Catalogs
*When using public Tekton Hub (hub.tekton.dev) for pipeline resources*

**Personas:** CI/CD Engineer
**Timing:** BEFORE relying on hub.tekton.dev - public hub removed

**Goal:** Migrate to custom self-hosted Tekton Hub instances or other task catalogs.

→ Lines 615-618: Tekton Hub removal
  Source: Breaking changes section

**What changed:**
- Public Tekton Hub (hub.tekton.dev) removed
- No default built-in catalog
- Need to self-host or find alternative

**Migration options:**
- Deploy custom self-hosted Tekton Hub instance
- Use alternative task catalogs (Artifact Hub)
- Host task catalog internally

---

# Appendices

## A. Multi-Cluster Deployment Decision Guide

**When to use multi-cluster mode:**

| Scenario | Recommendation | Key Benefits |
|----------|---------------|-------------|
| Centralized pipeline management across multiple OpenShift clusters | Multi-cluster Hub/Spoke | Centralized Results API, unified visibility |
| Single cluster pipeline deployment | Standard mode | Simpler configuration, no multi-cluster overhead |
| Resource sharing across clusters | Multi-cluster with Tekton Scheduler | Queue-based resource allocation, better utilization |
| Development/test vs production isolation | Multi-cluster Spoke clusters | Workload isolation, independent failure domains |

**Note:** Multi-cluster features are Technology Preview in 1.22

---

## B. Resolver Caching Mode Selection

**Choose resolver cache mode based on your workflow:**

| Mode | Best For | Behavior | Use When |
|------|----------|----------|----------|
| `auto` | Most users (default) | Cache enabled automatically | You want automatic optimization without configuration |
| `always` | High-repeatability environments | Cache always used | You fetch same resources repeatedly and want guaranteed caching |
| `never` | Dynamic development | Cache disabled | You're actively developing remote resources and need fresh fetches |

**Applies to:** Bundle resolver, Git resolver, Cluster resolver

---

## C. Workflow Coverage Analysis

| Stage | Coverage | Jobs | Notes |
|-------|----------|------|-------|
| EVALUATE | ✅ | Jobs 1, 20 | Platform compatibility, multi-cluster assessment |
| USE | ✅ | Jobs 2, 3, 5-7, 10, 13-17, 19, 22-23 | Security, configuration, features, multi-cluster UI |
| OPTIMIZE | ✅ | Jobs 4, 8-9, 11-12, 18, 21, 30, 37 | Performance, resource optimization, API efficiency |
| TROUBLESHOOT | ✅ | Jobs 24-55 | Breaking changes, known issues, resolved issues, console fixes |
| PLAN | ✅ | Jobs 56-57 | Deprecation notices, migration planning |
| MIGRATE | ✅ | Jobs 58-59 | Breaking changes, required migrations |

### Gaps Identified

| Stage | Gap | Recommendation |
|-------|-----|----------------|
| DEVELOP | No development workflow content | Release notes focus on platform features, not development workflows |
| MONITOR | No dedicated monitoring section | Monitoring covered via ServiceMonitor automation (Job 11) |
| GOVERN | Limited governance content | Consider adding retention policy and pruner configuration |

---

## Navigation Guide

### By User Journey

**Platform Administrator upgrading to 1.22:**
1. Job 1: Verify Platform Compatibility
2. Job 24: Enable Console Plugin Explicitly
3. Job 58: Migrate from disable-affinity-assistant to coschedule
4. Job 59: Migrate from Public Tekton Hub
5. Job 56: Plan RPM migration (if applicable)

**Security Engineer hardening pipelines:**
1. Job 2: Isolate User Namespaces on OpenShift 4.20+
2. Job 3: Verify HTTP Resolver Content Integrity
3. Job 16: Enforce Webhook Signature Validation
4. Job 49: Re-Evaluate /ok-to-test Approvals

**CI/CD Engineer optimizing performance:**
1. Job 4: Reduce Remote Resource Fetches with Resolver Caching
2. Job 8: Reduce TaskRun Startup Time
3. Job 12: Reduce VCS API Load with PAC File Caching
4. Job 18: Improve PAC Performance with GitHub GraphQL

**DevOps Engineer adopting new features:**
1. Job 5: Use Array Values in When Expressions
2. Job 6: Add Display Names to Steps
3. Job 7: Execute Embedded Pipelines
4. Job 17: Use CEL Expressions in PAC Templates

**Platform Administrator deploying multi-cluster (Technology Preview):**
1. Job 20: Configure Multi-Cluster Mode
2. Job 21: Optimize Hub Resources with Automatic Scaling
3. Job 22: Install Tekton Scheduler
4. Job 23: Differentiate Federated PipelineRuns in UI
5. Job 26: Understand tkn CLI Limitations

---

## Document Statistics

**Workflow Coverage:**
- EVALUATE: 2 jobs
- USE: 18 jobs
- OPTIMIZE: 10 jobs
- TROUBLESHOOT: 32 jobs
- PLAN: 2 jobs
- MIGRATE: 2 jobs

**Main Jobs:** 59
**Platform/Tool Variations:** Multi-cluster (Hub/Spoke), GitLab, GitHub, Bitbucket Cloud, Forgejo, Gitea
**Source Sections:** Compatibility matrix, New features (Pipelines, PAC, Console, Multi-cluster), Known issues, Resolved issues, Breaking changes, Deprecation notices

**Technology Preview Features:** Multi-cluster mode (Jobs 20-23), Tekton Scheduler (Job 22), Manual Approval Gate (compatibility)
**General Availability Features:** Tekton Chains, Pipelines as Code, Tekton Results, Tekton Pruner, Tekton Cache

---

**Generated:** 2026-06-11
**Source Document:** op-release-notes-1-22-self-managed-reduced.adoc (Lines 1-618)
**JTBD Analysis Records:** 59 jobs

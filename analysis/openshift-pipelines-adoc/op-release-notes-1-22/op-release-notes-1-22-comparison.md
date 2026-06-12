# op-release-notes-1-22 - TOC Comparison

**Current Feature-Based vs. Proposed JTBD-Based Structure**

**Analysis Date:** 2026-06-11  
**JTBD Records:** 59  
**Main Jobs:** 59 (from JTBD analysis)  
**Coverage:** 100% enhanced schema

---

## Current Structure (Feature-Based)

**Release notes for Red Hat OpenShift Pipelines 1.22**

- Compatibility and support matrix (lines 89-124)
- Release notes for {pipelines-title} 1.22 (lines 127-618)
  - New features and enhancements (lines 141-359)
    - Pipelines (lines 146-205)
    - Pipelines as Code (lines 208-304)
    - OpenShift Pipelines console (lines 307-312)
    - Multi-cluster features (Technology Preview) (lines 315-359)
  - Breaking changes (lines 362-370)
    - OpenShift Pipelines console (lines 365-370)
  - Known issues (lines 372-401)
    - Pipelines (lines 375-380)
    - CLI (lines 382-401)
  - Resolved issues (lines 404-592)
    - Pipelines (lines 407-456)
    - Operator (lines 459-469)
    - Pipelines as Code (lines 472-578)
    - OpenShift Pipelines console (lines 581-592)
  - Deprecation notices (lines 595-607)
    - OpenShift Pipelines (lines 598-601)
    - Pipelines as Code (lines 603-607)
  - Breaking changes (lines 609-620)

---

## Proposed JTBD-Based Structure

### Getting Started

**Job 1: Verify platform compatibility for OpenShift Pipelines 1.22**  
When: Planning to deploy or upgrade to OpenShift Pipelines 1.22  
Personas: Platform Administrator

- Check compatibility matrix and component versions
  Persona: Platform Administrator  
  → Lines 89-124: Compatibility and support matrix  
  Source: Section: Compatibility and support matrix  
  - Confirm OpenShift version support (4.14-4.21)
  - Verify component versions: Pipelines 1.9.x, Triggers 0.35.x, CLI 0.44.x
  - Verify component GA/TP status: Chains 0.26.x (GA), Hub 1.23.x (TP), PAC 0.42.x (GA), Results 0.18.x (GA), Manual Approval Gate 0.8.x (TP), Pruner 0.3.x (GA), Cache 0.3.x (GA)

**Job 20: Configure multi-cluster mode in TektonConfig (Technology Preview)**  
When: Planning multi-cluster Pipelines deployment  
Personas: Platform Administrator

- Enable and configure multi-cluster setup with Hub or Spoke role
  Persona: Platform Administrator  
  → Lines 320-337: Multi-cluster configuration options  
  Source: Section: Multi-cluster features, New features and enhancements  
  - Set multi-cluster-disabled to false
  - Configure multi-cluster-role as Hub or Spoke
  - Integrate with Tekton Scheduler for resource management
  - Note: Technology Preview feature

---

### Set Up & Configure - Security

**Job 2: Isolate user namespaces for TaskRuns and PipelineRuns on OpenShift 4.20+**  
When: Securing pipeline workloads with Kubernetes-native user namespace isolation  
Personas: Security Engineer

- Configure hostUsers in podTemplate for user namespace isolation
  Persona: Security Engineer  
  → Lines 148-151: hostUsers support in podTemplate  
  Source: Section: Pipelines, New features and enhancements  
  - Set hostUsers: false in TaskRun or PipelineRun podTemplate
  - Control host user namespace sharing without legacy CRI-O annotations
  - Kubernetes-native approach for OpenShift 4.20+

**Job 3: Verify HTTP resolver content integrity with hash parameter**  
When: Fetching pipeline resources from HTTP sources  
Personas: DevOps Engineer

- Use hash parameter for content verification
  Persona: DevOps Engineer  
  → Lines 153-156: HTTP resolver hash parameter support  
  Source: Section: Pipelines, New features and enhancements  
  - hash parameter supports SHA-256 and SHA-512
  - Ensure fetched content matches expected hash
  - Improved security for HTTP resources

**Job 16: Enforce webhook signature validation for Forgejo and Gitea providers**  
When: Using Pipelines as Code with Forgejo or Gitea VCS providers  
Personas: Security Engineer

- Enable webhook signature validation
  Persona: Security Engineer  
  → Lines 281-284: Webhook signature validation for Forgejo and Gitea  
  Source: Section: Pipelines as Code, New features and enhancements  
  - Webhook signature validation enabled
  - Unauthenticated requests rejected
  - Spoofed requests prevented

---

### Set Up & Configure - Performance

**Job 4: Reduce remote resource fetches and avoid API rate limits with resolver caching**  
When: Running pipelines that repeatedly fetch the same remote resources  
Personas: CI/CD Engineer

- Configure resolver caching for bundle, git, and cluster resolvers
  Persona: CI/CD Engineer  
  → Lines 158-167: Resolver caching configuration  
  Source: Section: Pipelines, New features and enhancements  
  - Cache mode: auto (default), always, or never
  - Supported resolvers: bundle, git, cluster
  - Reduce external API calls and prevent rate limits

**Job 8: Reduce TaskRun startup time with concurrent StepAction resolution**  
When: Running TaskRuns that use multiple remote StepActions  
Personas: DevOps Engineer

- Benefit from concurrent StepAction resolution
  Persona: DevOps Engineer  
  → Lines 184-187: Concurrent StepAction resolution  
  Source: Section: Pipelines, New features and enhancements  
  - StepActions resolved concurrently not sequentially
  - Reduced TaskRun startup time
  - Improved pipeline performance

**Job 11: Enable automatic metrics discovery for Tekton Results and Pipelines webhook**  
When: Setting up monitoring and alerting for Pipelines components  
Personas: Platform Administrator

- Use automatically created ServiceMonitor resources
  Persona: Platform Administrator  
  → Lines 202-205: Automatic ServiceMonitor creation  
  Source: Section: Pipelines, New features and enhancements  
  - ServiceMonitor for tekton-results and tekton-pipelines-webhook
  - Prometheus Operator integration enabled
  - No manual ServiceMonitor creation required

**Job 12: Reduce VCS API load with Pipelines as Code file caching**  
When: Using PAC with path-based filtering that makes many API calls  
Personas: CI/CD Engineer

- Enable caching of changed files per event
  Persona: CI/CD Engineer  
  → Lines 210-213: PAC file caching for path-based filtering  
  Source: Section: Pipelines as Code, New features and enhancements  
  - Changed files cached per event
  - path.pathChanged() and on-path-change annotations use cache
  - Reduced API rate limit risk

**Job 18: Improve Pipelines as Code performance with batched GitHub GraphQL API calls**  
When: Using PAC with GitHub or GitHub Enterprise with many .tekton files  
Personas: DevOps Engineer

- Benefit from batched GraphQL API calls
  Persona: DevOps Engineer  
  → Lines 299-302: GitHub GraphQL batching for .tekton files  
  Source: Section: Pipelines as Code, New features and enhancements  
  - Multiple .tekton files fetched in single request
  - Reduced GitHub API call count
  - Improved performance

**Job 21: Optimize Hub cluster resources with automatic Results scaling in multi-cluster mode (Technology Preview)**  
When: Operating multi-cluster Hub with centralized Results API  
Personas: Platform Administrator

- Automatically scale down watcher and retention-policy-agent to zero replicas
  Persona: Platform Administrator  
  → Lines 339-342: Automatic Results scaling on Hub  
  Source: Section: Multi-cluster features, New features and enhancements  
  - watcher and retention-policy-agent replicas set to 0 on Hub
  - Reduce Hub cluster resource usage
  - Components only needed on Spoke
  - Note: Technology Preview feature

**Job 30: Reduce controller reconciliation load for runs without timeouts**  
When: Operating pipelines controller with many running TaskRuns and PipelineRuns  
Personas: Platform Administrator

- Ensure runs without timeout configurations do not cause excessive reconciliation
  Persona: Platform Administrator  
  → Lines 416-419: Reconciliation optimization for runs without timeouts  
  Source: Section: Resolved issues - Pipelines  
  - Reconciliation only on actual changes
  - Reduced CPU usage on controller
  - Improved cluster performance and scalability

**Job 37: Reduce API server load from PipelineRun status updates**  
When: Operating large-scale pipelines with many status updates  
Personas: Platform Administrator

- Ensure consistent array ordering in PipelineRun status
  Persona: Platform Administrator  
  → Lines 451-454: Status update optimization via consistent array ordering  
  Source: Section: Resolved issues - Pipelines  
  - Array ordering consistent in status
  - Reduced invalid status updates
  - Improved API server performance and cluster stability

---

### Set Up & Configure - Pipeline Behavior

**Job 5: Use array values in when expression inputs for conditional logic**  
When: Building pipelines with conditional task execution based on array parameters or results  
Personas: CI/CD Engineer

- Evaluate array values in when expression inputs
  Persona: CI/CD Engineer  
  → Lines 169-172: Array values in when expressions  
  Source: Section: Pipelines, New features and enhancements  
  - Array values work in when expression input attribute
  - Improved conditional pipeline logic

**Job 6: Add display names to pipeline steps for better readability**  
When: Creating or maintaining Task definitions for CI/CD pipelines  
Personas: Developer

- Add human-readable display names to steps
  Persona: Developer  
  → Lines 174-177: displayName field for Step objects  
  Source: Section: Pipelines, New features and enhancements  
  - displayName field available on Step objects
  - Display names appear in UI and monitoring

**Job 7: Execute embedded pipelines within pipelines**  
When: Building complex pipeline workflows that require nested pipeline execution  
Personas: CI/CD Engineer

- Use PipelineSpec field under tasks
  Persona: CI/CD Engineer  
  → Lines 179-182: Embedded pipelines via PipelineSpec  
  Source: Section: Pipelines, New features and enhancements  
  - PipelineSpec field available under tasks
  - Pipelines-in-pipelines functionality

**Job 9: Handle PVC quota limits gracefully without immediate PipelineRun failure**  
When: Operating in environments with PVC quota limits  
Personas: Platform Administrator

- Allow PipelineRuns to requeue and retry when PVC quota is hit
  Persona: Platform Administrator  
  → Lines 189-192: PVC quota limit handling  
  Source: Section: Pipelines, New features and enhancements  
  - PipelineRun requeued when PVC creation hits quota
  - Runs succeed when quota becomes available
  - No immediate failures on temporary quota issues

**Job 10: Override individual task timeouts at PipelineRun level**  
When: Managing pipeline executions where different tasks need different timeout values  
Personas: CI/CD Engineer

- Set specific timeout values for individual tasks
  Persona: CI/CD Engineer  
  → Lines 194-197: Per-task timeout override  
  Source: Section: Pipelines, New features and enhancements  
  - Use spec.taskRunSpecs[].timeout field in PipelineRun
  - Individual task timeouts honored

---

### Use Pipelines Features

**Job 13: Reduce comment noise with update comment strategy for GitLab and GitHub**  
When: Managing Pipelines as Code with GitLab or GitHub webhooks  
Personas: CI/CD Engineer

- Maintain single status comment per PipelineRun that updates
  Persona: CI/CD Engineer  
  → Lines 216-219: Update comment strategy  
  Source: Section: Pipelines as Code, New features and enhancements  
  - update comment strategy available
  - Single comment updated with new status
  - Reduced repository comment clutter

**Job 14: Skip pipeline execution for work-in-progress commits with commit message tags**  
When: Pushing work-in-progress or minor commits that should not trigger pipelines  
Personas: Developer

- Use commit message tags to skip pipeline execution
  Persona: Developer  
  → Lines 221-240: Commit skip tags ([skip ci], [ci skip], [skip tkn], [tkn skip])  
  Source: Section: Pipelines as Code, New features and enhancements  
  - Case-insensitive tags to skip pipeline execution
  - Save resources for WIP commits
  - GitLab note: may generate extra list entry

**Job 15: Use glob patterns for GitHub App token scoping in Pipelines as Code**  
When: Managing many private Git submodules with GitHub App  
Personas: CI/CD Engineer

- Grant token access to multiple repositories using wildcard patterns
  Persona: CI/CD Engineer  
  → Lines 243-278: Glob patterns for GitHub App token scoping  
  Source: Section: Pipelines as Code, New features and enhancements  
  - Glob patterns supported in secret-github-app-scope-extra-repos
  - Patterns like owner/* work
  - Works in global config maps and Repository CR

**Job 17: Use CEL expressions in Pipelines as Code pipeline templates**  
When: Creating dynamic pipeline templates in Pipelines as Code  
Personas: CI/CD Engineer

- Use cel: prefix to evaluate Common Expression Language expressions
  Persona: CI/CD Engineer  
  → Lines 287-297: CEL expressions in templates  
  Source: Section: Pipelines as Code, New features and enhancements  
  - cel: prefix supported in templates
  - Perform ternary operations, presence checks, compose complex strings
  - Access to body, headers, files, pac namespaces

**Job 19: View ANSI color codes in OpenShift console log viewer**  
When: Viewing TaskRun and PipelineRun logs in OpenShift console  
Personas: Developer

- See colored logs with ANSI color code support
  Persona: Developer  
  → Lines 307-310: ANSI color code support in console  
  Source: Section: OpenShift Pipelines console, New features and enhancements  
  - ANSI color codes rendered in console
  - Improved log readability

**Job 22: Install and manage Tekton Scheduler with Pipelines Operator (Technology Preview)**  
When: Setting up resource allocation and queuing for pipelines  
Personas: Platform Administrator

- Deploy Tekton Scheduler (Tekton-Kueue) using Pipelines Operator
  Persona: Platform Administrator  
  → Lines 344-351: Tekton Scheduler management via operator  
  Source: Section: Multi-cluster features, New features and enhancements  
  - scheduler section available in TektonConfig CR
  - Default queue name configurable
  - Multi-cluster support available
  - Note: Technology Preview feature, requires upstream Kueue

**Job 23: Differentiate federated PipelineRuns in multi-cluster UI (Technology Preview)**  
When: Viewing PipelineRuns in multi-cluster UI  
Personas: DevOps Engineer

- Visually distinguish between local Hub and federated PipelineRuns
  Persona: DevOps Engineer  
  → Lines 353-356: Federated PipelineRun visual indicator  
  Source: Section: Multi-cluster features, New features and enhancements  
  - Icon differentiates local vs federated PipelineRuns
  - managedBy field evaluated
  - Note: Technology Preview feature

---

### Troubleshoot Breaking Changes

**Job 24: Enable console plugin explicitly after upgrading to Pipelines 1.22**  
When: Upgrading to OpenShift Pipelines 1.22 with console plugin changes  
Personas: Platform Administrator  
Timing: DURING upgrade to 1.22 - console plugin requires explicit enablement

- Understand console plugin explicit enablement requirement
  Persona: Platform Administrator  
  → Lines 363-368: Console plugin explicit enablement  
  Source: Section: Breaking changes  
  - Console plugin requires explicit enablement
  - Legacy static console plugin deprecated
  - Pipelines navigation not visible by default after upgrade

**Job 58: Migrate from disable-affinity-assistant to coschedule feature flag**  
When: Upgrading to Pipelines 1.22 with affinity assistant configuration  
Personas: Platform Administrator  
Timing: DURING upgrade to 1.22 - breaking change in configuration

- Update TektonConfig to use coschedule feature flag
  Persona: Platform Administrator  
  → Lines 610-613: disable-affinity-assistant removal  
  Source: Section: Breaking changes  
  - disable-affinity-assistant field removed from TektonConfig
  - Replaced with coschedule feature flag
  - Breaking change in configuration format

**Job 59: Migrate from public Tekton Hub to custom self-hosted Hub or alternative catalogs**  
When: Using public Tekton Hub (hub.tekton.dev) for pipeline resources  
Personas: CI/CD Engineer  
Timing: BEFORE relying on hub.tekton.dev - public hub removed

- Migrate to custom self-hosted Tekton Hub instances or other task catalogs
  Persona: CI/CD Engineer  
  → Lines 615-618: Tekton Hub removal  
  Source: Section: Breaking changes  
  - Public Tekton Hub (hub.tekton.dev) removed
  - No default built-in catalog
  - Need to self-host or find alternative (Artifact Hub)

---

### Troubleshoot Known Issues

**Job 25: Work around buildah-ns task failure on OpenShift 4.20+**  
When: Using buildah-ns task on OpenShift 4.20 or later  
Personas: CI/CD Engineer

- Use standard buildah task with hostUsers: false in PodTemplate
  Persona: CI/CD Engineer  
  → Lines 373-378: buildah-ns task workaround  
  Source: Section: Known issues - Pipelines  
  - Use buildah task with hostUsers: false
  - CRI-O annotation io.kubernetes.cri-o.userns-mode removed in OpenShift 4.20

**Job 26: Understand tkn CLI limitations in multicluster environments**  
When: Operating tkn CLI tool in multicluster Hub and Spoke setup  
Personas: DevOps Engineer

- Recognize which tkn commands do not work correctly in multicluster
  Persona: DevOps Engineer  
  → Lines 380-392: tkn CLI multicluster limitations  
  Source: Section: Known issues - CLI  
  - tkn taskrun list, pipelinerun describe, pipelinerun logs, pipelinerun cancel fail on Hub
  - pipelinerun/taskrun list only work during run on Spoke
  - Workaround: Use OpenShift console or oc commands

**Job 27: Work around opc results logs get command line limit**  
When: Retrieving logs from Tekton Results with more than 300 lines  
Personas: DevOps Engineer

- Use opc results pipelinerun logs or opc results taskrun logs for complete output
  Persona: DevOps Engineer  
  → Lines 394-399: opc results logs workaround  
  Source: Section: Known issues - CLI  
  - opc results logs get limited to 300 lines
  - Use opc results pipelinerun logs or opc results taskrun logs instead
  - logs get command deprecated

---

### Troubleshoot Resolved Issues

**Job 28: Ensure Affinity Assistant pods inherit correct service account**  
When: Using affinity assistant to co-schedule tasks with shared workspaces  
Personas: Platform Administrator

- Verify Affinity Assistant pods use PipelineRun service account
  Persona: Platform Administrator  
  → Lines 406-409: Affinity Assistant service account fix  
  Source: Section: Resolved issues - Pipelines  
  - Affinity Assistant inherits PipelineRun service account
  - Correct SCC permissions applied

**Job 29: Identify TaskRun pod configuration errors early with clear error messages**  
When: TaskRuns failing to start due to missing config maps or secrets  
Personas: DevOps Engineer

- Receive immediate clear error messages identifying specific configuration issues
  Persona: DevOps Engineer  
  → Lines 411-414: Early TaskRun pod configuration errors  
  Source: Section: Resolved issues - Pipelines  
  - TaskRun fails immediately with clear error
  - Specific missing resource identified
  - No timeout waiting for generic error

**Job 31: Use parameter references in pipeline parameter defaults**  
When: Defining pipeline parameters with fallback patterns  
Personas: CI/CD Engineer

- Reference other parameters in default values to enable flexible fallback patterns
  Persona: CI/CD Engineer  
  → Lines 421-424: Parameter references in defaults fix  
  Source: Section: Resolved issues - Pipelines  
  - Parameter defaults support references to other parameters
  - Arbitrary dependency chains work
  - Circular dependencies detected with clear errors

**Job 32: Improve PipelineRun resilience to retryable TaskRef errors**  
When: Running PipelineRuns that reference remote tasks  
Personas: DevOps Engineer

- Ensure PipelineRuns retry on retryable TaskRef reconciliation errors
  Persona: DevOps Engineer  
  → Lines 426-429: TaskRef error resilience fix  
  Source: Section: Resolved issues - Pipelines  
  - PipelineRuns retry on retryable errors
  - Only explicit validation errors cause failure

**Job 33: Use Kubernetes-native sidecars with proper signal handling**  
When: Running TaskRuns with Kubernetes-native sidecars  
Personas: DevOps Engineer

- Ensure sidecars handle signals correctly and operate reliably
  Persona: DevOps Engineer  
  → Lines 431-434: Sidecar signal handling fix  
  Source: Section: Resolved issues - Pipelines  
  - Signal handling added to SidecarLog results
  - No repeated init container restarts

**Job 34: Inspect timed-out TaskRun pods when keep-pod-on-cancel enabled**  
When: Debugging timed-out TaskRuns with keep-pod-on-cancel feature flag  
Personas: DevOps Engineer

- Ensure pods are retained for timed-out TaskRuns
  Persona: DevOps Engineer  
  → Lines 436-439: Pod retention on timeout fix  
  Source: Section: Resolved issues - Pipelines  
  - keep-pod-on-cancel feature flag honored
  - Pods retained on timeout for debugging

**Job 35: View StepAction status in correct chronological order**  
When: Reviewing task execution timeline using StepAction  
Personas: DevOps Engineer

- See status steps displayed in correct sequential order
  Persona: DevOps Engineer  
  → Lines 441-444: StepAction chronological ordering fix  
  Source: Section: Resolved issues - Pipelines  
  - Status steps in correct order
  - Accurate execution timeline

**Job 36: Run TaskRuns successfully on arm64 clusters**  
When: Operating TaskRuns on arm64 Kubernetes clusters  
Personas: DevOps Engineer

- Ensure TaskRuns execute reliably on arm64 architecture
  Persona: DevOps Engineer  
  → Lines 446-449: arm64 platform support fix  
  Source: Section: Resolved issues - Pipelines  
  - TaskRuns succeed on arm64 clusters
  - Entrypoint handles Linux platform variants

**Job 38: Ensure operator webhooks are cleaned up when namespace is deleted**  
When: Uninstalling Pipelines Operator by deleting openshift-pipelines namespace  
Personas: Platform Administrator

- Verify all operator webhooks are removed with proper owner references
  Persona: Platform Administrator  
  → Lines 459-462: Webhook cleanup on namespace deletion  
  Source: Section: Resolved issues - Operator  
  - Owner references added to all webhooks
  - Webhooks cleaned up on namespace deletion

**Job 39: Fix Prometheus metrics collection when Operator installed in custom namespace**  
When: Pipelines Operator installed in non-default namespace like openshift-pipelines  
Personas: Platform Administrator

- Ensure ServiceMonitor targets correct namespace for metrics scraping
  Persona: Platform Administrator  
  → Lines 464-467: ServiceMonitor namespace fix  
  Source: Section: Resolved issues - Operator  
  - ServiceMonitor auto-targets operator namespace
  - No hardcoded openshift-operators namespace reference

**Job 40: Use custom parameters in Pipelines as Code CEL expressions**  
When: Defining repository-specific parameters for event filtering in PAC  
Personas: CI/CD Engineer

- Reference custom parameters from Repository CR in on-cel-expression annotations
  Persona: CI/CD Engineer  
  → Lines 473-508: Custom parameters in CEL fix  
  Source: Section: Resolved issues - Pipelines as Code  
  - Custom parameters exposed as CEL variables
  - Parameters usable in CEL expressions

**Job 41: Skip CI execution for commits with [skip ci] tag in GitLab merge requests**  
When: Using GitLab with Pipelines as Code for MR automation  
Personas: CI/CD Engineer

- Ensure [skip ci] commit messages are honored
  Persona: CI/CD Engineer  
  → Lines 511-514: GitLab skip ci tag support fix  
  Source: Section: Resolved issues - Pipelines as Code  
  - [skip ci] tag recognized in commit messages
  - Pipeline execution skipped

**Job 42: Resolve tasks from custom hub catalogs with version specifiers**  
When: Using custom hub catalogs with versioned task references  
Personas: CI/CD Engineer

- Use versioned catalog references like foo://resource:1.2 without errors
  Persona: CI/CD Engineer  
  → Lines 516-519: Custom catalog version resolution fix  
  Source: Section: Resolved issues - Pipelines as Code  
  - Non-HTTP(S) schemes supported
  - Version specifiers parsed correctly

**Job 43: Use tkn pac cel command with required flags and clear errors**  
When: Testing CEL expressions with tkn pac cel command  
Personas: DevOps Engineer

- Receive clear error messages when required flags are missing
  Persona: DevOps Engineer  
  → Lines 521-524: tkn pac cel error messaging fix  
  Source: Section: Resolved issues - Pipelines as Code  
  - Body (-b) and header (-H) flags mandatory
  - Clear error messages for missing arguments

**Job 44: Reliably populate pull_request_number variable for push events**  
When: Push events associated with pull request merges  
Personas: CI/CD Engineer

- Ensure pull_request_number variable is populated with GitHub API delays
  Persona: CI/CD Engineer  
  → Lines 526-529: pull_request_number reliability fix  
  Source: Section: Resolved issues - Pipelines as Code  
  - Exponential backoff retry mechanism in place
  - pull_request_number populated reliably

**Job 45: Evaluate all modified files in GitLab push events for trigger filtering**  
When: Using file-based filtering in Pipelines as Code with GitLab  
Personas: CI/CD Engineer

- Ensure all modified files are evaluated not just first 20
  Persona: CI/CD Engineer  
  → Lines 531-534: GitLab file pagination fix  
  Source: Section: Resolved issues - Pipelines as Code  
  - API pagination implemented
  - All modified files retrieved

**Job 46: View accurate GitLab commit statuses throughout pipeline lifecycle**  
When: Using Pipelines as Code with GitLab forked merge requests  
Personas: CI/CD Engineer

- See correct pending and running statuses in GitLab
  Persona: CI/CD Engineer  
  → Lines 536-539: GitLab status mapping fix  
  Source: Section: Resolved issues - Pipelines as Code  
  - Pending state displayed before approval
  - Running state after pipeline starts

**Job 47: Reduce GitLab merge request comment noise with permission-based fallback**  
When: Using Pipelines as Code with GitLab with restricted permissions  
Personas: CI/CD Engineer

- Only post fallback comments when commit status update fails due to permissions
  Persona: CI/CD Engineer  
  → Lines 541-544: GitLab comment fallback fix  
  Source: Section: Resolved issues - Pipelines as Code  
  - Fallback comments only on permission failures
  - Reduced comment noise

**Job 48: Handle invalid GitLab input in tkn pac cel command safely**  
When: Testing CEL expressions with GitLab provider  
Personas: DevOps Engineer

- Receive descriptive errors instead of nil pointer dereference panic
  Persona: DevOps Engineer  
  → Lines 546-549: tkn pac cel GitLab error handling fix  
  Source: Section: Resolved issues - Pipelines as Code  
  - Input validation before processing
  - No panic on malformed input

**Job 49: Re-evaluate /ok-to-test approvals per commit when remember-ok-to-test is false**  
When: Reviewing pull requests from unauthorized users with security controls  
Personas: Security Engineer

- Ensure each new commit requires fresh /ok-to-test approval
  Persona: Security Engineer  
  → Lines 551-554: ok-to-test re-evaluation fix  
  Source: Section: Resolved issues - Pipelines as Code  
  - Permissions re-evaluated per commit
  - Single approval not retained
  - Security policy enforced correctly

**Job 50: View correct logging for intentionally skipped push events**  
When: Operating Pipelines as Code with push events associated with open PRs  
Personas: DevOps Engineer

- See info-level logging for skipped events instead of error-level
  Persona: DevOps Engineer  
  → Lines 557-560: Skipped event logging level fix  
  Source: Section: Resolved issues - Pipelines as Code  
  - Skipped push events logged at info level
  - No confusing error logs

**Job 51: View individual status for each PipelineRun in Bitbucket Cloud pull requests**  
When: Running multiple pipelines per pull request in Bitbucket Cloud  
Personas: CI/CD Engineer

- See individual commit status for each PipelineRun
  Persona: CI/CD Engineer  
  → Lines 562-565: Bitbucket Cloud unique status keys  
  Source: Section: Resolved issues - Pipelines as Code  
  - Unique commit status key per PipelineRun
  - Format: ApplicationName / PipelineRunName

**Job 52: Trigger pipelines based on label conditions using CEL expressions**  
When: Building event-driven pipelines that respond to pull request labeling  
Personas: CI/CD Engineer

- Ensure on-cel-expression annotations are evaluated during PR labeling events
  Persona: CI/CD Engineer  
  → Lines 568-571: CEL label evaluation fix  
  Source: Section: Resolved issues - Pipelines as Code  
  - CEL expressions evaluated on label events
  - AST inspection detects label references

**Job 53: Update Git provider status when PipelineRuns are deleted or canceled**  
When: Managing PipelineRuns that are deleted while running or queued  
Personas: DevOps Engineer

- Ensure Git provider commit status shows canceled instead of stuck in pending
  Persona: DevOps Engineer  
  → Lines 573-576: PipelineRun deletion status update  
  Source: Section: Resolved issues - Pipelines as Code  
  - Finalizer reports canceled status to Git provider
  - Commit status updated on deletion

**Job 54: View pipeline logs with preserved whitespace and horizontal scrolling**  
When: Viewing structured log output and tabular data in OpenShift console  
Personas: DevOps Engineer

- See logs with preserved whitespace and horizontal scrolling
  Persona: DevOps Engineer  
  → Lines 582-585: Log whitespace preservation  
  Source: Section: Resolved issues - OpenShift Pipelines console  
  - Whitespace preserved in logs
  - Horizontal scrolling available

**Job 55: Access TaskSidebar correctly in Pipeline Builder**  
When: Using Pipeline Builder in OpenShift console  
Personas: Developer

- View TaskSidebar overlay with correct styling and accessibility
  Persona: Developer  
  → Lines 587-590: TaskSidebar rendering fix  
  Source: Section: Resolved issues - OpenShift Pipelines console  
  - TaskSidebar renders above other elements
  - Required styling applied

---

### Plan Migration & Deprecation

**Job 56: Plan migration from openshift-pipelines-client RPM**  
When: Using openshift-pipelines-client RPM for tkn CLI  
Personas: Platform Administrator  
Timing: BEFORE Pipelines 1.23 - RPM will be removed

- Identify alternative distribution method before RPM is removed in 1.23
  Persona: Platform Administrator  
  → Lines 598-600: RPM deprecation notice  
  Source: Section: Deprecation notices - OpenShift Pipelines  
  - openshift-pipelines-client RPM deprecated
  - Will be removed in Pipelines 1.23

**Job 57: Stop using pipelinerun_status field in Repository CR**  
When: Using Pipelines as Code Repository custom resources  
Personas: CI/CD Engineer  
Timing: BEFORE Pipelines 1.23 - field will be removed

- Update configurations to avoid pipelinerun_status field before removal in 1.23
  Persona: CI/CD Engineer  
  → Lines 602-605: pipelinerun_status deprecation  
  Source: Section: Deprecation notices - Pipelines as Code  
  - pipelinerun_status field deprecated in Repository CR
  - Will be removed in Pipelines 1.23

---

## Key Differences

### Current Structure (Feature-Based)
**Organized By:** Technical components and features  
**Navigation:** 6 major sections (Compatibility, New features, Breaking changes, Known issues, Resolved issues, Deprecation notices)  
**User Journey:** Linear reading by feature category  
**Structure:** Component-centric (Pipelines, PAC, Console, Multi-cluster separate sections)

### Proposed Structure (JTBD-Based)
**Organized By:** Job map stages and user goals  
**Navigation:** 59 jobs organized by workflow stage  
**User Journey:** Goal-directed, find by what you need to accomplish  
**Structure:** Workflow-centric (Getting Started, Security, Performance, Features, Troubleshooting, Migration)

---

## Example: Content Consolidation

**Current (Fragmented):**
- Section: Pipelines (lines 146-205) - Security features mixed with performance and functional features
- Section: Pipelines as Code (lines 208-304) - PAC features separate from general pipeline features
- Section: Resolved issues - Pipelines (lines 407-456) - Fixes scattered across component sections

**Proposed (Consolidated):**
- **Job 2-3, 16:** All security features consolidated under "Set Up & Configure - Security"
- **Job 4, 8, 11-12, 18, 21, 30, 37:** All performance optimizations consolidated under "Set Up & Configure - Performance"
- **Job 28-55:** All resolved issues organized by functional area under "Troubleshoot Resolved Issues"

**Benefit:** Find all security features in one place! Find all performance optimizations together! Find troubleshooting fixes organized by problem domain!

---

## Hierarchy Levels Explanation

### Level 1: Main Jobs (59 total)
**Stable, outcome-focused goals** - Would exist even if technology changes
- Examples: "Verify platform compatibility", "Isolate user namespaces", "Reduce remote resource fetches"

### Level 2: Implementation Approaches
**Persona-specific or option-based paths** - How to accomplish the job
- Format: "Configure X for Y" or "Use X approach"
- Examples: "Configure hostUsers in podTemplate", "Use hash parameter for content verification"

### Level 3: Procedures
**Step-by-step implementation** - Line references to source content
- Format: "→ Lines X-Y: Section Title"
- Includes source references and key details

---

## Navigation Improvement

**Current:** Browse 6 major sections with 10+ subsections each to find content  
**Proposed:** Navigate 59 jobs organized into 8 workflow stages  
**Reduction:** From ~60+ scattered subsections to 59 organized jobs  
**Benefit:** Find content in 2-3 clicks instead of scanning multiple component sections

**Example user journeys:**

**Security Engineer hardening pipelines:**
- Current: Search through Pipelines section, PAC section, and Resolved issues
- Proposed: Go directly to "Set Up & Configure - Security" (Jobs 2, 3, 16, 49)

**Platform Administrator optimizing performance:**
- Current: Search through Pipelines, PAC, and Resolved issues for performance content
- Proposed: Go directly to "Set Up & Configure - Performance" (Jobs 4, 8, 11-12, 18, 21, 30, 37)

**CI/CD Engineer troubleshooting PAC:**
- Current: Search through Known issues, Resolved issues - Pipelines as Code
- Proposed: Go directly to "Troubleshoot Resolved Issues" PAC jobs (Jobs 40-53)

---

## Workflow Coverage Comparison

| Stage | Current | Proposed | Gap Status |
|-------|---------|----------|------------|
| EVALUATE | ✅ Compatibility matrix | ✅ Jobs 1, 20 | Reorganized |
| USE | ⚠️ Scattered in New features | ✅ Jobs 2-3, 5-7, 9-10, 13-17, 19, 22-23 | Consolidated |
| OPTIMIZE | ⚠️ Mixed with features | ✅ Jobs 4, 8, 11-12, 18, 21, 30, 37 | Elevated |
| TROUBLESHOOT | ⚠️ Split across Known/Resolved | ✅ Jobs 24-55 | Unified |
| PLAN | ⚠️ In Deprecation | ✅ Jobs 56-57 | Reorganized |
| MIGRATE | ⚠️ In Breaking changes | ✅ Jobs 58-59 | Reorganized |
| MONITOR | ❌ Missing | ⚠️ Limited (Job 11 ServiceMonitor only) | Gap remains |
| GOVERN | ❌ Missing | ❌ Missing | Gap identified |

### Coverage Summary

**Current structure characteristics:**
- Feature-centric organization
- Component-based sections
- Issues separated from features
- Security, performance, and features mixed within component sections

**Proposed structure improvements:**
- Workflow-stage organization
- Security features consolidated (Jobs 2, 3, 16, 49)
- Performance features consolidated (Jobs 4, 8, 11-12, 18, 21, 30, 37)
- Troubleshooting unified (Jobs 24-55)
- Migration and deprecation elevated (Jobs 56-59)

**Gaps remaining in both structures:**
- MONITOR: Limited to automatic ServiceMonitor creation (Job 11)
- GOVERN: No dedicated governance or retention policy content (PAC retention in other docs)

### Recommendations for Gap Closure

| Gap | Recommendation | Priority |
|-----|----------------|----------|
| MONITOR | Link to Tekton Results monitoring guide or add basic observability checks | Medium |
| GOVERN | Add retention policy configuration for Pipelines resources (if available) | Low |
| DEVELOP | Release notes focus on features, not development workflows - appropriate for doc type | N/A |

---

## Document Statistics

**Current Structure:**
- Top-level sections: 6
- Component subsections: ~10
- Total line references: 618 lines
- Organization: Component-based

**Proposed Structure:**
- Main jobs: 59
- Workflow stages: 8 (Getting Started, Security, Performance, Pipeline Behavior, Features, Troubleshoot Breaking Changes, Troubleshoot Known Issues, Troubleshoot Resolved Issues, Migration & Deprecation)
- Line coverage: 618 lines (100% of source)
- Organization: Workflow-based

**Key Metrics:**
- Jobs addressing security: 4 (Jobs 2, 3, 16, 49)
- Jobs addressing performance: 8 (Jobs 4, 8, 11-12, 18, 21, 30, 37)
- Jobs addressing troubleshooting: 32 (Jobs 24-55)
- Jobs addressing migration/deprecation: 4 (Jobs 56-59)
- Technology Preview features: 4 (Jobs 20-23)

---

**Generated:** 2026-06-11  
**Source Document:** op-release-notes-1-22-self-managed-reduced.adoc (Lines 1-618)  
**JTBD Analysis:** 59 records

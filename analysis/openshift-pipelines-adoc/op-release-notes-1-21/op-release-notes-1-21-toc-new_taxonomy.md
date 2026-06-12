# OpenShift Pipelines 1.21 Release Notes
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** Help users understand new features, improvements, bug fixes, and breaking changes in OpenShift Pipelines 1.21 to plan upgrades and adopt new capabilities.

**Personas:** Platform Administrator, Security Engineer, CI/CD Engineer, DevOps Engineer, Developer

**Main Jobs:** 38 core jobs across 8 workflow stages

---

## Quick Navigation

**I want to:**
- Check compatibility with my OpenShift version → Job 1 (EVALUATE)
- Understand breaking changes before upgrading → Jobs 37-39 (PLAN)
- Improve pipeline security → Jobs 2, 7, 14, 26, 28 (USE)
- Optimize pipeline performance → Jobs 4, 11, 17, 20, 30-33, 46, 71, 84 (OPTIMIZE)
- Configure timeout controls → Job 3 (USE)
- Enable resolver caching → Job 4 (OPTIMIZE)
- Use array values in conditional logic → Job 5 (USE)
- Set up Tekton Results external access → Job 8 (ONBOARD)
- Configure group-based approvals → Jobs 9, 36 (USE)
- Set retention policies for Results → Job 17 (OPTIMIZE)
- Troubleshoot missing pipeline runs → Jobs 19, 40-88 (TROUBLESHOOT)
- Migrate PostgreSQL databases → Jobs 22, 27 (MIGRATE)
- Use Tekton Cache in production → Job 23 (EVALUATE)
- Configure event-driven pruner → Jobs 30-34 (USE/GOVERN/OPTIMIZE)
- Debug CEL expressions → Job 35 (TROUBLESHOOT)

---

# Table of Contents

## Evaluate Platform Readiness

### Job 1: Verify Platform Compatibility for OpenShift Pipelines 1.21
*When planning to deploy or upgrade to OpenShift Pipelines 1.21*

**Personas:** Platform Administrator

**Goal:** Confirm that OpenShift Pipelines 1.21 is compatible with my OpenShift Container Platform version and understand component support status.

→ Lines 84-125: Compatibility matrix
  Source: Compatibility and support matrix section

**What you'll verify:**
- OpenShift version is listed in compatibility matrix (4.14 through 4.21)
- Component versions are known and supported
- Technology Preview vs GA status is clear for each component

**Key components:**
- Pipelines Operator 1.21.0
- Tekton Pipelines 0.65.3
- Tekton Triggers 0.29.1
- Tekton Results 0.13.0
- Pipelines as Code 0.29.0
- Tekton Chains 0.23.1
- Tekton Hub 1.18.1
- Tekton Cache 0.2.2 (GA)
- Manual Approval Gate 0.2.1 (Technology Preview)

---

### Job 23: Assess Tekton Cache General Availability for Production Use
*When evaluating features for production pipeline deployments*

**Personas:** Platform Administrator

**Goal:** Confirm Tekton Cache is GA and supported for production workloads.

→ Lines 590-591: Tekton Cache GA announcement
  Source: New features section

**What changed:**
- Tekton Cache promoted to General Availability
- Fully supported for production use
- No longer Technology Preview

---

### Job 18: Verify PostgreSQL 17.5 Support for Tekton Results
*When planning database infrastructure for Tekton Results*

**Personas:** Platform Administrator

**Goal:** Confirm that PostgreSQL version 17.5 is supported for Tekton Results deployment.

→ Lines 536-538: PostgreSQL 17.5 support
  Source: New features - Tekton Results section

**Key information:**
- PostgreSQL 17.5 officially supported
- Database compatibility verified
- Safe to deploy with version 17.5

---

## Enhance Pipeline Security

### Job 2: Enforce Read-Only Root Filesystems for Container Security
*When securing Pipelines deployments following Kubernetes security best practices*

**Personas:** Security Engineer

**Goal:** Ensure all Pipelines containers run with read-only root filesystems to prevent unauthorized modifications.

→ Lines 150-151: readOnlyRootFilesystem security enhancement
  Source: New features - OpenShift Pipelines section

**What's enabled:**
- All Pipelines controllers have `readOnlyRootFilesystem=true`
- All webhooks have `readOnlyRootFilesystem=true`
- Security posture improved against unauthorized modifications

---

### Job 7: Control Pipeline Service Account Permissions Using legacyPipelineRbac Parameter
*When managing RBAC for pipeline service accounts across namespaces*

**Personas:** Platform Administrator

**Goal:** Prevent pipeline service accounts from automatically receiving edit ClusterRole to enforce stricter permissions.

→ Lines 335-357: legacyPipelineRbac parameter
  Source: New features - OpenShift Pipelines section

**Configuration options:**
- Set `legacyPipelineRbac: false` to disable automatic edit ClusterRole
- Pipeline service accounts no longer receive edit ClusterRole by default
- Enforces principle of least privilege

**Important:** Manual cleanup of existing RoleBindings required for namespaces created before this change.

---

### Job 14: Enforce Commit SHA Validation for /ok-to-test Commands to Prevent TOCTOU Attacks
*When reviewing pull requests from untrusted contributors in GitHub*

**Personas:** Security Engineer

**Goal:** Prevent race condition vulnerability by requiring exact commit SHA in /ok-to-test approvals.

→ Lines 445-449: require-ok-to-test-sha setting
  Source: New features - Pipelines as Code section

**Security improvement:**
- Enable `require-ok-to-test-sha` setting
- Users must specify exact SHA: `/ok-to-test <sha>`
- Pipeline tied to specific commit, preventing force-push exploits
- Prevents TOCTOU (time-of-check-time-of-use) race conditions

---

### Job 26: Enforce SHA-256 Signature Validation for GitHub Webhooks
*When securing Tekton Triggers webhook validation*

**Personas:** Security Engineer

**Goal:** Ensure GitHub interceptor only accepts SHA-256 signatures, rejecting SHA-1.

**Why:** SHA-1 is cryptographically weak and no longer secure for HMAC validation.

→ Lines 604-607: SHA-256 signature enforcement
  Source: New features - Tekton Triggers section

**What changed:**
- Only `X-Hub-Signature-256` accepted
- SHA-1 support (`X-Hub-Signature`) dropped
- Custom webhook implementations must update to SHA-256

---

### Job 28: Disable OCI Image Signing While Maintaining Provenance and Attestation
*When managing security artifacts in CI/CD pipelines with external image signing*

**Personas:** Security Engineer

**Goal:** Configure Tekton Chains to skip OCI image signing but still generate provenance and sign attestations.

→ Lines 619-627: artifacts.oci.disable-signing option
  Source: New features - Tekton Chains section

**Use case:**
- When using external image signing workflow
- Still need provenance generation
- Still need attestation signing

**Configuration:**
- Set `artifacts.oci.disable-signing` option
- Image signing disabled
- Provenance generation continues
- Attestation signing continues with cosign

---

### Job 68: Re-Evaluate Permissions on Each GitLab MR Commit When remember-ok-to-test is False
*When reviewing merge requests from unauthorized users with remember-ok-to-test=false*

**Personas:** Security Engineer

**Goal:** Ensure /ok-to-test approval is required for each new commit, not remembered.

→ Lines 922-925: remember-ok-to-test fix
  Source: Bug fixes - Pipelines as Code section

**What's fixed:**
- Permissions re-evaluated on every commit
- /ok-to-test not remembered for later commits
- CI halted for each new commit when setting is false

---

## Configure Pipeline Execution

### Job 3: Override Individual TaskRun Timeouts Within a PipelineRun
*When managing pipeline executions where different tasks require different timeout values*

**Personas:** CI/CD Engineer

**Goal:** Set specific timeout values for individual tasks without affecting the overall PipelineRun timeout.

→ Lines 154-175: TaskRun timeout override
  Source: New features - OpenShift Pipelines section

**How to use:**
- Override timeout using `spec.taskRunSpecs[].timeout`
- Individual task timeouts are honored
- Overall PipelineRun timeout remains separate

**Example:**
```yaml
spec:
  taskRunSpecs:
    - pipelineTaskName: build
      timeout: 10m
    - pipelineTaskName: test
      timeout: 30m
```

---

### Job 5: Use Array Values in When Expressions for Conditional Task Execution
*When building pipelines with conditional logic based on array parameters or results*

**Personas:** CI/CD Engineer

**Goal:** Evaluate array values in when expression inputs to control task execution based on array membership.

→ Lines 229-290: Array values in when expressions
  Source: New features - OpenShift Pipelines section

**What you can do:**
- Array parameters can be used in when expressions
- Array results from tasks can be consumed by when expressions
- Use `input` attribute with `operator: in` for membership checks

**Example:**
```yaml
when:
  - input: "$(params.environment)"
    operator: in
    values: ["$(params.allowed-envs[*])"]
```

---

### Job 6: Add Display Names to Pipeline Steps for Better Readability
*When creating or maintaining Task definitions for CI/CD pipelines*

**Personas:** Developer

**Goal:** Add human-readable display names to steps that support parameter substitution.

→ Lines 295-327: Step displayName field
  Source: New features - OpenShift Pipelines section

**What's available:**
- `displayName` field available on Step objects
- Display names support parameter substitution
- Steps more readable in UI and logs

**Example:**
```yaml
steps:
  - name: build
    displayName: "Build the application"
  - name: test
    displayName: "Run unit tests for $(params.component)"
```

---

### Job 9: Configure Group Approvers for Approval Tasks
*When setting up approval workflows where teams rather than individuals approve pipeline tasks*

**Personas:** CI/CD Engineer

**Goal:** Enable group-based approvals where any member can approve or reject tasks.

→ Lines 368-369: Group approvers for Approval Tasks
  Source: New features - Tekton Triggers section

**How to configure:**
- Specify group approvers using `group:<groupName>` syntax
- Any group member can approve or reject
- Single rejection fails the task immediately

---

### Job 13: Trigger and Cancel PipelineRuns for Git Tags Using Comments
*When managing version-specific CI/CD workflows triggered by Git tags*

**Personas:** CI/CD Engineer

**Goal:** Trigger or cancel PipelineRuns by commenting on tagged commits for specific versions.

→ Lines 426-443: Git tag commands
  Source: New features - Pipelines as Code section

**Commands available:**
- Trigger: `/test <pipeline> tag:<tag>`
- Cancel: `/cancel <pipeline> tag:<tag>`
- Supported for GitHub and GitLab

**Use case:** Version-specific pipeline control for releases

---

### Job 15: Use Glob Patterns for Incoming Webhook Targets in Pipelines as Code
*When managing webhook configurations for repositories with many branches*

**Personas:** CI/CD Engineer

**Goal:** Match multiple branch names with single glob pattern rules to simplify configuration.

→ Lines 451-464: Glob patterns in targets field
  Source: New features - Pipelines as Code section

**Pattern support:**
- Shell prompt-style patterns in Repository CR `targets` field
- Examples: `feature/*`, `v[0-9]*`, `release-*`
- First matching webhook is used

**Benefits:**
- Reduce configuration management overhead
- Simplify branch matching rules

---

### Job 16: Route Incoming Webhook Requests to Specific Namespace Using Namespace Parameter
*When managing Pipelines as Code repositories with duplicate names across namespaces*

**Personas:** CI/CD Engineer

**Goal:** Uniquely identify target Repository CR when multiple repositories share the same name.

→ Lines 466-469: Namespace parameter for webhooks
  Source: New features - Pipelines as Code section

**How to use:**
- Add `namespace` parameter to webhook requests
- Correct routing even with duplicate repository names
- 400 status returned when namespace needed but omitted

---

### Job 36: Configure Group Approvers for Manual Approval Gate Tasks (Technology Preview)
*When setting up approval workflows for Manual Approval Gate*

**Personas:** CI/CD Engineer

**Goal:** Enable group-based approvals where any group member can approve or reject.

**Timing:** Technology Preview feature - evaluate before production use

→ Lines 703-708: Group approvers for Manual Approval Gate
  Source: Technology Preview - Manual Approval Gate section

**How it works:**
- Specify group approvers with `group:<groupName>`
- Any member can approve or reject
- Approval by one member counts as single approval
- Rejection by one member fails task
- Messages from all members preserved in `status.approverResponse`

---

## Optimize Pipeline Performance

### Job 4: Reduce External API Calls and Improve Pipeline Execution Reliability with Resolver Caching
*When running pipelines that fetch resources from external services like GitHub or OCI registries*

**Personas:** DevOps Engineer

**Goal:** Enable caching for bundle, Git, and cluster resolvers to minimize redundant fetches and API rate limit issues.

→ Lines 178-227: Resolver caching configuration
  Source: New features - OpenShift Pipelines section

**What you can configure:**
- Resolver cache with appropriate TTL and max-size
- Cache modes: `auto` (default), `always`, `never`
- Support for bundle resolver, Git resolver, cluster resolver

**Benefits:**
- Cache hits reduce external API calls
- Pipeline execution more reliable during service issues
- Avoid API rate limits

**Configuration fields:**
- `bundles-resolver-ttl` and `bundles-resolver-max-size`
- `git-resolver-ttl` and `git-resolver-max-size`
- `cluster-resolver-ttl` and `cluster-resolver-max-size`

---

### Job 11: Improve GitLab Project Access Control Performance with Caching
*When running Pipelines as Code with GitLab repositories*

**Personas:** CI/CD Engineer

**Goal:** Reduce repeated API calls to GitLab for permission checks by caching ACL membership queries.

→ Lines 385-386: GitLab ACL caching
  Source: New features - Pipelines as Code section

**Performance improvement:**
- GitLab ACL (Project Access Control List) membership queries cached
- Performance improved for permission checks
- Reduced API call volume to GitLab
- Helps avoid GitLab API throttling

---

### Job 20: Monitor Run Storage Latency with New Metrics
*When operating Tekton Results and optimizing database performance*

**Personas:** Platform Administrator

**Goal:** Measure time between run completion and database storage to identify performance issues.

→ Lines 556-569: run_storage_latency_seconds metric
  Source: New features - Tekton Results section

**Metric details:**
- `run_storage_latency_seconds` available in watcher container
- Latency measured per kind (PipelineRun/TaskRun) and namespace
- Helps identify performance bottlenecks
- Enables storage timing analysis

---

### Job 30: Assess Event-Driven Pruner General Availability for Production Use
*When evaluating pruning mechanisms for OpenShift Pipelines*

**Personas:** Platform Administrator

**Goal:** Confirm event-driven tektonpruner is GA and adopt it for centralized pruning configuration.

→ Lines 644-647: Event-driven pruner GA
  Source: New features - OpenShift Pipelines section

**What's available:**
- `tektonpruner` is now General Availability (not Technology Preview)
- Fully supported for production
- Better performance than job-based pruner
- Centralized configuration with hierarchical overrides

---

### Job 31: Configure Namespace-Level Pruner Policies to Override Global Defaults
*When managing pruning behavior for different namespaces with varying requirements*

**Personas:** Platform Administrator

**Goal:** Define custom TTL and history limits per namespace using tekton-pruner-namespace-spec config map.

→ Lines 651-652: Namespace-level pruner configuration
  Source: New features - OpenShift Pipelines section

**How to configure:**
- Create `tekton-pruner-namespace-spec` config map in namespace
- Set custom TTL and history limits
- Namespace-level config overrides global defaults
- Policies work independently per namespace

**Use case:** Different retention for production vs development namespaces

---

### Job 32: Configure Selector-Based Pruning with matchLabels and matchAnnotations
*When implementing fine-grained pruning policies based on resource characteristics*

**Personas:** Platform Administrator

**Goal:** Create pruning rules that match resources by labels and annotations in namespace-level config maps.

→ Lines 652-653: Selector-based pruning
  Source: New features - OpenShift Pipelines section

**Selector options:**
- `matchLabels` - Match resources by labels
- `matchAnnotations` - Match resources by annotations
- AND logic applied when both specified
- Name matching has absolute precedence over selectors

**Benefits:**
- Granular control over retention
- Prune based on resource metadata
- Different policies for different resource types

---

### Job 46: Improve Proxy Webhook Performance Under High Concurrency
*When experiencing webhook timeouts under heavy workload*

**Personas:** Platform Administrator

**Goal:** Ensure webhook uses optional config map volumes to prevent blocking on CA bundle checks.

→ Lines 785-788: Proxy webhook performance fix
  Source: Bug fixes - OpenShift Pipelines Operator section

**What's fixed:**
- Webhook no longer performs synchronous API calls during admission
- Pod creation not blocked by config map checks
- `SSL_CERT_DIR` always set
- Improved performance under load
- Prevents etcd performance issues affecting webhooks

---

### Job 71: Optimize GitHub App Installation ID Retrieval Performance
*When using GitHub App for Pipelines as Code*

**Personas:** Platform Administrator

**Goal:** Reduce API calls by directly fetching installation by repository URL with organization fallback.

→ Lines 938-941: GitHub App optimization
  Source: Bug fixes - Pipelines as Code section

**Performance improvement:**
- Direct installation fetch by repository URL
- Organization fallback when needed
- No unnecessary API listings
- Reduced API calls
- Improved performance

---

### Job 84: Improve Tekton Chains Controller Pod Distribution with Anti-Affinity Rule
*When managing Tekton Chains controller pod scheduling*

**Personas:** Platform Administrator

**Goal:** Ensure pods distributed evenly across nodes to prevent resource contention.

→ Lines 1025-1028: Anti-affinity rule for Chains controller
  Source: Bug fixes - Tekton Chains section

**What's improved:**
- Anti-affinity rule added to tekton-chains-controller
- Pods evenly distributed across nodes
- Better resource distribution
- No resource contention from co-located pods

---

## Set Up and Onboard

### Job 8: Access Tekton Results API Endpoint Externally via Automatically Created Route
*When setting up Tekton Results component for the first time*

**Personas:** Platform Administrator

**Goal:** Enable external access to Tekton Results API without manual Route configuration.

→ Lines 359-363: Automatic Route creation for Results API
  Source: New features - Tekton Results section

**What's automatic:**
- OpenShift Route automatically created for Results API
- API endpoint accessible externally
- Custom host and path can be configured if needed

**Benefits:**
- No manual Route creation required
- External access available by default
- Reduced configuration steps

---

## Monitor and Track Performance

### Job 10: Persist Pipeline Overview Page Filter Selections Across Navigation
*When monitoring pipelines across different namespaces and time ranges*

**Personas:** DevOps Engineer

**Goal:** Maintain namespace, time range, and refresh interval selections when navigating away and returning.

→ Lines 371-373: Filter persistence
  Source: New features - Tekton Triggers section

**What persists:**
- Filter selections stored in application state and URL
- Selections persist across page refreshes
- Namespace filter
- Time Range filter
- Refresh Interval

**Note:** Filters reset when switching namespaces

---

### Job 19: Monitor Runs Not Stored in Database with New Metrics
*When operating Tekton Results and investigating missing pipeline run data*

**Personas:** Platform Administrator

**Goal:** Track PipelineRun and TaskRun instances deleted before database persistence.

→ Lines 542-553: runs_not_stored_count metric
  Source: New features - Tekton Results section

**Metric details:**
- `runs_not_stored_count` available in watcher container
- Tracks kind (PipelineRun/TaskRun) and namespace
- Can identify data loss patterns
- Helps diagnose deletion issues

**Use case:** Runs disappearing before storage, need visibility into missing data

---

## Govern and Configure Retention

### Job 17: Configure Fine-Grained Retention Policies for Tekton Results
*When managing storage and retention of PipelineRun and TaskRun results across namespaces*

**Personas:** Platform Administrator

**Goal:** Set different retention periods based on namespace, labels, annotations, and status.

→ Lines 481-533: Retention policies configuration
  Source: New features - Tekton Results section

**Configuration location:** `tekton-results-config-results-retention-policy` config map

**Selector options:**
- `matchNamespaces` - Target specific namespaces
- `matchLabels` - Match resources by labels
- `matchAnnotations` - Match resources by annotations
- `matchStatuses` - Match by completion status
- `defaultRetention` - Fallback retention period

**Policy evaluation:**
- First matching policy is applied
- Different retention for production vs CI namespaces
- Can retain critical failures longer

---

### Job 33: Enforce Cluster-Wide Maximum Limits for Event-Driven Pruner Configuration
*When preventing resource overuse from namespace-level pruner settings*

**Personas:** Platform Administrator

**Goal:** Ensure namespace-specific pruner settings do not exceed cluster-wide maximum values.

→ Lines 653-654: Cluster-wide maximum limits
  Source: New features - OpenShift Pipelines section

**Maximum limits:**
- Maximum TTL: 2592000 seconds (30 days)
- Maximum history limit: 100
- Global limits take precedence when set
- Validation prevents excessive values

**Purpose:** Prevent storage exhaustion, bound resource usage

---

### Job 34: Validate Pruner Config Maps at Apply-Time Using Admission Webhook
*When creating or updating pruner configuration*

**Personas:** Platform Administrator

**Goal:** Catch invalid pruner configurations immediately with clear error messages.

→ Lines 654-661: Config map validation
  Source: New features - OpenShift Pipelines section

**Validation features:**
- Admission webhook validates config maps at apply-time
- Invalid configurations rejected immediately
- Clear error messages provided
- Config maps must have correct labels:
  - `app.kubernetes.io/part-of: tekton-pruner`
  - `pruner.tekton.dev/config-type: namespace`

**Benefits:**
- No silent failures
- Immediate feedback on errors
- Easier debugging

---

## Use CLI and Management Tools

### Job 12: Configure Error Log Snippet Length in Pipelines as Code
*When managing error reporting in Pipelines as Code with GitHub integration*

**Personas:** CI/CD Engineer

**Goal:** Control the number of lines displayed in error log snippets to fit GitHub API limits.

→ Lines 389-408: error-log-snippet-number-of-lines setting
  Source: New features - Pipelines as Code section

**Configuration:**
- `error-log-snippet-number-of-lines` setting is configurable
- Log snippets truncated to 65000 characters
- Prevents GitHub API failures

**Why:** GitHub API has message length limits; long error logs cause check-run update failures

---

### Job 21: Use Tekton Results CLI Across Namespace Switches Without Re-Authentication
*When working with Tekton Results across multiple namespaces*

**Personas:** DevOps Engineer

**Goal:** Maintain API configuration when switching between namespaces.

→ Lines 571-574: Configuration persistence
  Source: New features - Tekton Results section

**What's improved:**
- Configuration persists across namespace switches
- No need to run `opc results config set` repeatedly
- Authentication maintained

**Benefits:**
- Reduced repetitive setup steps
- Better user experience

---

### Job 24: Download Tekton Cache Binaries for Custom StepAction Configurations
*When building custom StepActions that require Tekton Cache binaries*

**Personas:** DevOps Engineer

**Goal:** Access Red Hat Tekton Cache binaries without authentication.

→ Lines 594-595: Public binary downloads
  Source: New features - Tekton Cache section

**What's available:**
- Binaries available for public download
- No authentication required
- Can use in custom StepActions

---

### Job 25: Use Docker Credentials Without config.json Key for Tekton Cache
*When configuring Tekton Cache with private registry authentication*

**Personas:** DevOps Engineer

**Goal:** Support Docker secrets that contain .dockerconfigjson instead of config.json.

→ Lines 598-600: Docker credential flexibility
  Source: New features - Tekton Cache section

**What's supported:**
- Docker secrets work without `config.json` key
- `DOCKER_CONFIG` can point to `.dockerconfigjson`
- Private registry authentication works with either format

**Benefits:**
- More flexible credential configuration
- Support for standard Kubernetes Docker secrets

---

### Job 29: Rerun Resolver-Based PipelineRuns with tkn CLI Using --resolvertype Flag
*When re-executing previous PipelineRuns that used resolvers*

**Personas:** DevOps Engineer

**Goal:** Specify resolver type when rerunning PipelineRuns that used git, http, hub, cluster, bundle, or remote resolvers.

→ Lines 633-638: --resolvertype flag
  Source: New features - tkn CLI section

**How to use:**
- `tkn p start` with `--resolvertype` flag
- Can reference existing PipelineRun name
- Resolver type correctly applied to rerun

**Supported resolver types:**
- git
- http
- hub
- cluster
- bundle
- remote

---

### Job 35: Evaluate CEL Expressions Interactively Against Webhook Payloads Using tkn pac cel (Technology Preview)
*When debugging Pipelines as Code CEL expressions in Repository configurations*

**Personas:** CI/CD Engineer

**Goal:** Test and debug CEL expressions against real webhook data with tab completion.

**Timing:** Technology Preview feature - evaluate before production use

→ Lines 676-697: tkn pac cel command
  Source: Technology Preview - Pipelines as Code section

**Features:**
- `tkn pac cel` command available
- Can load webhook payload and headers
- Interactive prompt with tab completion
- Variable access to body, headers, pac parameters

**Use case:**
- Debug CEL expressions before deployment
- Test against real webhook data
- Avoid trial and error with live webhooks

---

## Migrate and Upgrade

### Job 22: Upgrade Default PostgreSQL Database from Version 13 to 15 for Tekton Results
*When maintaining Tekton Results deployment before PostgreSQL 13 EOL*

**Personas:** Platform Administrator

**Goal:** Complete automated migration from PostgreSQL 13 to 15 without data loss.

**Why:** PostgreSQL 13 approaching end-of-life

→ Lines 576-584: PostgreSQL migration
  Source: New features - Tekton Results section

**Migration process:**
- Automated migration from PostgreSQL 13 to 15
- Backup completed before upgrade
- Requires PVC with >50% free space
- Migration completes successfully when space requirements met

**Important:** Ensure adequate storage space before upgrade

---

### Job 27: Upgrade Tekton Hub Default Database from PostgreSQL 13 to 15
*When maintaining Tekton Hub deployment before PostgreSQL 13 EOL*

**Personas:** Platform Administrator

**Goal:** Complete automated migration to PostgreSQL 15 for continued stability and support.

**Why:** PostgreSQL 13 EOL approaching

→ Lines 612-615: Tekton Hub PostgreSQL migration
  Source: New features - Tekton Hub section

**What happens:**
- Automated migration from version 13 to 15
- Tekton Hub remains operational
- Deployment stability maintained

---

### Job 39: Migrate Private OIDC Provider from HS256 to RS256 Tokens for Tekton Chains
*When using keyless signing with Tekton Chains and private OIDC provider*

**Personas:** Security Engineer

**Timing:** BEFORE upgrading to Pipelines 1.21 - breaking change

**Goal:** Update OIDC provider to use RS256 tokens before upgrading to Pipelines 1.21.

**Why:** Cosign 2.6.0 breaking change - HS256 tokens no longer accepted

→ Lines 730-731: HS256 to RS256 migration
  Source: Breaking changes section

**Migration steps:**
- Update OIDC provider to use RS256 tokens
- HS256 tokens no longer accepted by Cosign 2.6.0
- Keyless signing will continue to work after update

---

### Job 86: Retain Event-Based Pruner Config Values After Upgrade
*When upgrading OpenShift Pipelines with event-based pruner enabled*

**Personas:** Platform Administrator

**Goal:** Ensure pruner config values are retained after upgrade, not reverted to defaults.

→ Lines 1042-1045: Pruner config retention fix
  Source: Bug fixes - OpenShift Pipelines section

**What's fixed:**
- Pruner config values retained during upgrade
- No revert to defaults after upgrade
- Configuration preserved

---

## Plan for Breaking Changes and Deprecations

### Job 37: Plan for Console Plugin Enablement After Pipelines Operator Installation
*When upgrading to OpenShift Pipelines 1.21 with UI changes*

**Personas:** Platform Administrator

**Timing:** BEFORE upgrading to 1.21 - breaking change

**Goal:** Understand that static console plugin is deprecated and explicit enablement is required.

→ Lines 716-719: Console plugin breaking change
  Source: Breaking changes section

**What changed:**
- Static console plugin deprecated
- Console plugin must be explicitly enabled
- Pipelines navigation only visible when plugin active
- No fallback limited Pipelines entry

**Action required:** Enable console plugin after upgrade to see Pipelines UI

---

### Job 38: Plan for Deprecation of pipelinerun_status Field in Repository CR
*When using Pipelines as Code Repository custom resources*

**Personas:** CI/CD Engineer

**Goal:** Update integrations and automation to stop using pipelinerun_status field before removal.

→ Lines 724-725: pipelinerun_status deprecation
  Source: Deprecated features section

**What's deprecated:**
- `pipelinerun_status` field in Repository CR
- Will be removed in future release
- Deprecation timeline uncertain

**Action required:**
- Identify alternative approach
- Update integrations
- Update automation that references this field

---

### Job 87: Plan for Future Migration from OpenCensus to OpenTelemetry
*When using OpenCensus for observability and tracing in Pipelines*

**Personas:** CI/CD Engineer

**Goal:** Understand that OpenCensus is deprecated and prepare for OpenTelemetry migration.

→ Lines 1056-1059: OpenCensus deprecation
  Source: Deprecated features section

**What's deprecated:**
- OpenCensus observability and tracing
- Will be replaced with OpenTelemetry

**Action required:**
- Prepare for migration timeline
- Plan to update PromQL queries
- Prepare migration effort for observability tooling

---

## Troubleshoot Issues

### Job 40: Resolve Duplicate Pipelines Navigation Entries in OpenShift Console
*When experiencing UI issue after Pipelines Operator installation or upgrade*

**Personas:** Platform Administrator

**Goal:** Apply updates to OpenShift Console and Pipelines Operator to eliminate duplicate menu entries.

→ Lines 739-744: Duplicate navigation entries
  Source: Known issues section

**Issue:** Two Pipelines entries in console menu during migration from static to dynamic plugin

**Resolution:**
- Apply updates to OpenShift Console
- Apply updates to Pipelines Operator
- Migration from static to dynamic plugin completes
- Pipeline execution not affected

**Issue ID:** SRVKP-10006

---

### Job 41: Diagnose PipelineRun Failures with Clear Errors on Invalid apiVersion
*When PipelineRun execution failing without clear error messages*

**Personas:** CI/CD Engineer

**Goal:** Identify that spec.tasks[].taskRef.apiVersion is invalid and correct it.

→ Lines 752-755: Clear error for invalid apiVersion
  Source: Known issues section

**What's improved:**
- Clear error message displayed for invalid apiVersion
- Invalid `spec.tasks[].taskRef.apiVersion` identified
- PipelineRun no longer fails silently

**Issue ID:** SRVKP-8514

---

### Job 42: Troubleshoot TaskRef Reconciliation Errors Without PipelineRun Failure
*When PipelineRun failing on temporary TaskRef resolution issues*

**Personas:** DevOps Engineer

**Goal:** Understand that PipelineRuns now only fail on explicit validation errors, not retryable errors.

→ Lines 757-760: TaskRef reconciliation reliability
  Source: Known issues section

**What's improved:**
- PipelineRuns continue on retryable errors
- Only explicit validation errors cause failure
- Improved pipeline reliability for external task resolution

**Issue ID:** SRVKP-9135

---

### Job 43: Debug Timed-Out TaskRuns with Retained Pods When keep-pod-on-cancel is Enabled
*When TaskRuns timing out and need to debug pod state*

**Personas:** DevOps Engineer

**Goal:** Confirm that pods are retained for timed-out TaskRuns when feature flag is enabled.

→ Lines 767-770: Pod retention on timeout
  Source: Known issues section

**What's fixed:**
- `keep-pod-on-cancel` flag enabled
- Pods retained on TaskRun timeout
- Can debug timed-out tasks

**Issue IDs:** SRVKP-9135, SRVKP-9176

---

### Job 44: Interpret StepAction Status Steps in Correct Chronological Order
*When reviewing StepAction execution timeline*

**Personas:** CI/CD Engineer

**Goal:** View status steps in correct sequential order for accurate interpretation.

→ Lines 772-775: StepAction status order fix
  Source: Known issues section

**What's fixed:**
- Status steps display in correct order
- Chronological flow is clear
- Timeline is accurate

**Issue ID:** SRVKP-9135

---

### Job 45: Run TaskRuns Successfully on arm64 Clusters
*When TaskRuns failing on arm64 Kubernetes clusters*

**Personas:** DevOps Engineer

**Goal:** Ensure TaskRuns execute reliably on arm64 architecture after platform variant mismatch fix.

→ Lines 777-780: arm64 compatibility fix
  Source: Known issues section

**What's fixed:**
- TaskRuns succeed on arm64 clusters
- Entrypoint logic handles platform variants
- No architecture-specific failures

**Issue ID:** SRVKP-9135

---

### Job 47: Prevent prioritySemaphore Deadlocks and Race Conditions
*When experiencing deadlocks or panics in pipeline execution*

**Personas:** Platform Administrator

**Goal:** Ensure prioritySemaphore locking is corrected with proper synchronization.

→ Lines 790-793: Semaphore synchronization fix
  Source: Known issues section

**What's fixed:**
- No deadlocks occur
- No race conditions
- No panics from unsynchronized data
- Stable concurrent operation

**Issue ID:** SRVKP-8198

---

### Job 48: Verify Default Catalog Name is Correct After Upgrade from 1.19.x to 1.20.0
*When upgrading from OpenShift Pipelines 1.19.x*

**Personas:** Platform Administrator

**Goal:** Ensure hub-catalog-name points to Artifact Hub catalog, not deprecated Tekton Hub catalog.

→ Lines 805-808: Catalog name upgrade fix
  Source: Known issues section

**What to verify:**
- `hub-catalog-name` set to correct value
- Points to Artifact Hub, not deprecated Tekton Hub
- No unexpected task resolution behavior

**Issue ID:** SRVKP-8930

---

### Job 49: Ensure nodeSelector and Tolerations Apply to Tekton Results Pods
*When Results pods not scheduled according to configured preferences*

**Personas:** Platform Administrator

**Goal:** Verify nodeSelector and tolerations from TektonConfig propagate to Results pods.

→ Lines 810-813: Scheduling configuration fix
  Source: Known issues section

**What's fixed:**
- nodeSelector applied to Results pods
- tolerations applied to Results pods
- Pods scheduled according to TektonConfig configuration

**Issue ID:** SRVKP-8922

---

### Job 50: Prevent Webhook Validation Issues in Control-Plane Namespaces
*When experiencing webhook certificate issues affecting system components*

**Personas:** Platform Administrator

**Goal:** Ensure tekton-operator-proxy-webhook excludes kube-* and openshift-* namespaces.

→ Lines 815-818: Webhook namespace exclusion
  Source: Known issues section

**What's fixed:**
- Webhook does not validate control-plane namespaces (kube-*, openshift-*)
- No certificate issues in system namespaces
- Better isolation between components

**Issue ID:** SRVKP-8891

---

### Job 51: Preserve Custom Hub Catalog Configuration During Conversion
*When custom hub catalog type lost after operator conversion*

**Personas:** Platform Administrator

**Goal:** Verify catalog-{INDEX}-type field is preserved in config map.

→ Lines 820-823: Catalog type preservation fix
  Source: Known issues section

**What's fixed:**
- `catalog-{INDEX}-type` field preserved
- Custom catalog types not lost after conversion
- Configuration maintained after conversion

**Issue ID:** SRVKP-9472

---

### Job 52: Verify PipelineRun Status Reflects Completed TaskRuns in OpenShift Console
*When PipelineRun showing as canceling even after TaskRuns complete*

**Personas:** DevOps Engineer

**Goal:** Confirm PipelineRun status accurately reflects completion state.

→ Lines 827-830: PipelineRun status consistency fix
  Source: Bug fixes - OpenShift Pipelines section

**What's fixed:**
- PipelineRun status correct after TaskRun completion
- No lingering canceling state
- Console displays accurate status

**Issue ID:** SRVKP-6960

---

### Job 53: Save Buildah Tasks in Pipeline Builder UI Without Validation Errors
*When creating pipelines with Buildah tasks in OpenShift Console*

**Personas:** CI/CD Engineer

**Goal:** Successfully save Buildah tasks with default BUILD_ARGS parameter.

→ Lines 832-835: Buildah task validation fix
  Source: Bug fixes - OpenShift Pipelines section

**What's fixed:**
- Buildah tasks save without validation error
- BUILD_ARGS parameter accepted
- Pipeline builder works correctly

**Issue ID:** SRVKP-8571

---

### Job 54: Sort PipelineRuns by Actual Duration in OpenShift Console
*When viewing and analyzing PipelineRun performance*

**Personas:** DevOps Engineer

**Goal:** See PipelineRuns sorted correctly by duration in seconds, not string sort.

→ Lines 837-840: Duration sorting fix
  Source: Bug fixes - OpenShift Pipelines section

**What's fixed:**
- Duration sorting uses actual duration values
- PipelineRuns ordered correctly by elapsed time
- No misleading sort results

**Issue ID:** SRVKP-6211

---

### Job 55: Sort TaskRuns by Elapsed Duration in OpenShift Console
*When reviewing TaskRun performance and execution times*

**Personas:** DevOps Engineer

**Goal:** View TaskRuns sorted by actual elapsed time, not completion time.

→ Lines 842-845: TaskRun duration sorting fix
  Source: Bug fixes - OpenShift Pipelines section

**What's fixed:**
- TaskRuns sorted by duration correctly
- Chronological order accurate
- Duration calculation correct

**Issue ID:** SRVKP-8835

---

### Job 56: Navigate to Tasks with Similar Names Using Strict URL Matching
*When accessing tasks via URLs when multiple tasks have similar names*

**Personas:** CI/CD Engineer

**Goal:** Ensure URL navigation matches exact task names, avoiding partial matches.

→ Lines 847-850: Strict task name matching
  Source: Bug fixes - OpenShift Pipelines section

**What's fixed:**
- Task names matched with strict equality
- No partial string matches
- Correct task displayed from URL

**Issue ID:** SRVKP-8976

---

### Job 57: View Empty State Instead of Error When Results Data Unavailable
*When Results API or database pods restarting*

**Personas:** DevOps Engineer

**Goal:** See graceful empty state on Overview page instead of error message.

→ Lines 852-855: Graceful empty state
  Source: Bug fixes - OpenShift Pipelines section

**What's improved:**
- Empty state displayed when data unavailable
- No error message shown during pod restarts
- Smooth user experience

**Issue ID:** SRVKP-8076

---

### Job 58: See Immediate YAML Editor Updates Using useEffect Hook
*When editing YAML in OpenShift Console*

**Personas:** Developer

**Goal:** View YAML changes immediately without component remount.

→ Lines 857-860: YAML editor reactivity fix
  Source: Bug fixes - OpenShift Pipelines section

**What's improved:**
- Changes reflected immediately
- useEffect hook applied
- No wait for component remount

**Issue ID:** SRVKP-8205

---

### Job 59: Paginate Through Archived PipelineRun Results Correctly
*When viewing archived PipelineRun data with data_source=archived filter*

**Personas:** DevOps Engineer

**Goal:** Load additional results when scrolling using correct next_page_token field.

→ Lines 862-875: Pagination fix for archived results
  Source: Bug fixes - OpenShift Pipelines section

**What's fixed:**
- Pagination works for archived results
- `next_page_token` field handled correctly (was `nextPageToken`)
- All pages of results load

**Issue ID:** SRVKP-9397

---

### Job 60: View Correct Task Parameters in Pipeline Builder for Tasks Across Namespaces
*When building pipelines with tasks from different namespaces*

**Personas:** CI/CD Engineer

**Goal:** See correct task parameter data from selected namespace, not stale data.

→ Lines 867-870: Task parameter namespace fix
  Source: Bug fixes - OpenShift Pipelines section

**What's fixed:**
- Task parameters match selected namespace
- No stale or incorrect data from different namespace
- Unique task names generated for duplicates
- Validation detects name conflicts

**Issue ID:** SRVKP-8998

---

### Job 61: Monitor Pipeline Overview Page with Reliable Data Loading
*When monitoring pipelines on clusters with slow backend responses*

**Personas:** DevOps Engineer

**Goal:** View complete and current data without stale or partial information.

→ Lines 883-886: Data loading reliability fix
  Source: Bug fixes - OpenShift Pipelines section

**What's improved:**
- No stale data displayed
- Complete data loads reliably
- Increased API timeouts improve reliability
- Safeguards prevent incomplete data

**Issue ID:** SRVKP-9427

---

### Job 62: Understand Time Range Filter with Corrected Last Week Label
*When filtering PipelineRuns by time range*

**Personas:** DevOps Engineer

**Goal:** Select correct time range with clear label and consistent API behavior.

→ Lines 888-891: Time range filter label fix
  Source: Bug fixes - OpenShift Pipelines section

**What's fixed:**
- Label reads "Last week" not "Last weeks"
- API payload aligned with label
- Time range behavior consistent

**Issue ID:** SRVKP-9428

---

### Job 63: Track Data Loading Status on Pipeline Overview Cards with Loading Indicators
*When monitoring Pipeline Overview page while data loads*

**Personas:** DevOps Engineer

**Goal:** See loading spinners on each card during data retrieval for clear feedback.

→ Lines 893-896: Loading indicators
  Source: Bug fixes - OpenShift Pipelines section

**What's improved:**
- Loading spinners displayed on cards
- Clear visual feedback during fetch
- Better user experience

**Issue ID:** SRVKP-9436

---

### Job 64: Use GitOps Commands in GitLab Merge Request Discussion Replies
*When collaborating on GitLab merge requests with Pipelines as Code*

**Personas:** CI/CD Engineer

**Goal:** Post commands like /ok-to-test in discussion thread replies and have them recognized.

→ Lines 902-905: GitLab reply command support
  Source: Bug fixes - Pipelines as Code section

**What's fixed:**
- Commands in replies are recognized
- Not limited to top-level comments
- Improved workflow reliability

**Issue ID:** SRVKP-8324

---

### Job 65: View Correct Pending CI Status for Unauthorized Bitbucket PRs
*When pull request opened by unauthorized user on Bitbucket Data Center*

**Personas:** CI/CD Engineer

**Goal:** See Pending status while awaiting approval, not incorrect Running status.

→ Lines 907-910: Bitbucket status fix
  Source: Bug fixes - Pipelines as Code section

**What's fixed:**
- CI status shows Pending correctly
- Not incorrectly Running
- Awaiting administrator approval state clear

**Issue ID:** SRVKP-8269

---

### Job 66: View Repository Information with opc pac install info Command
*When checking Pipelines as Code repository configuration*

**Personas:** DevOps Engineer

**Goal:** Use install info command to display repositories for single CR correctly.

→ Lines 912-915: install info command fix
  Source: Bug fixes - Pipelines as Code section

**What's fixed:**
- `install info` shows repositories correctly
- `--namespace/-n` binds correctly
- Not incorrectly bound to kubeconfig

**Issue ID:** SRVKP-7152

---

### Job 67: Trigger Pipelines on Git Tag Push Events Regardless of skip-push-event-for-pr-commits Setting
*When using tag pushes to trigger pipelines*

**Personas:** CI/CD Engineer

**Goal:** Ensure tag push events proceed regardless of skip-push-event-for-pr-commits setting.

→ Lines 917-920: Tag push event fix
  Source: Bug fixes - Pipelines as Code section

**What's fixed:**
- Tag push events not skipped
- `skip-push-event-for-pr-commits` does not affect tags
- Tag-based workflows work correctly

**Issue ID:** SRVKP-9111

---

### Job 69: Prevent GitLab Merge Requests from Auto-Merging When PipelineRuns are Canceled
*When PipelineRuns canceled but GitLab MRs still merging*

**Personas:** CI/CD Engineer

**Goal:** Ensure canceled PipelineRuns reported correctly to GitLab API to keep MRs open.

→ Lines 927-930: GitLab cancellation status fix
  Source: Bug fixes - Pipelines as Code section

**What's fixed:**
- Canceled status mapped to "canceled" for GitLab (spelling compatibility)
- MRs remain open when PipelineRun canceled
- Auto-merge prevented correctly

**Issue ID:** SRVKP-9050

---

### Job 70: Evaluate Placeholder Variables When Some Data Sources are Missing
*When using placeholder variables in Pipelines as Code*

**Personas:** CI/CD Engineer

**Goal:** Process body.*, headers.*, and files.* placeholders independently without failure.

→ Lines 932-935: Placeholder evaluation fix
  Source: Bug fixes - Pipelines as Code section

**What's fixed:**
- Placeholders work if corresponding data present
- Missing payload or headers does not fail all placeholders
- Independent evaluation of each type (body.*, headers.*, files.*)

**Issue ID:** SRVKP-8984

---

### Job 72: Get Correct Commit IDs for Bitbucket Merge Commits
*When Bitbucket merge commits showing wrong revision variable*

**Personas:** CI/CD Engineer

**Goal:** Verify revision variable fetches correct commit IDs after revert of problematic change.

→ Lines 944-947: Bitbucket revision variable fix
  Source: Bug fixes - Pipelines as Code section

**What's fixed:**
- Correct commit IDs for merge commits
- `revision` variable accurate
- Expected behavior restored

**Issue ID:** SRVKP-9141

---

### Job 73: Cancel Only PR-Triggered PipelineRuns, Not Push-Triggered Ones
*When pull request closed and cancel-in-progress triggered*

**Personas:** CI/CD Engineer

**Goal:** Ensure only PipelineRuns from the PR are canceled, not unrelated push pipelines.

→ Lines 950-953: Cancellation scope fix
  Source: Bug fixes - Pipelines as Code section

**What's fixed:**
- Cancellation scoped to PR PipelineRuns only
- Push-triggered PipelineRuns not canceled
- Correct targeting of cancellation

**Issue ID:** SRVKP-9141

---

### Job 74: Post GitLab Merge Request Comments Correctly from Forks
*When working with GitLab forks and merge requests*

**Personas:** CI/CD Engineer

**Goal:** Ensure comments post successfully using TargetProjectID instead of wrong Project ID.

→ Lines 956-959: GitLab fork comment fix
  Source: Bug fixes - Pipelines as Code section

**What's fixed:**
- Comments posted correctly from forks
- TargetProjectID used (not Project ID)
- Fork workflow no longer broken

**Issue ID:** SRVKP-9141

---

### Job 75: Handle Duplicate Secret Creation Gracefully Without Failures
*When secret creation encountering existing secret*

**Personas:** Platform Administrator

**Goal:** Reuse existing secret instead of failing on duplicate error.

→ Lines 962-965: Duplicate secret handling
  Source: Bug fixes - Pipelines as Code section

**What's fixed:**
- Existing secret reused
- No failure on duplicate
- Graceful handling

**Issue ID:** SRVKP-9141

---

### Job 76: Create GitHub Check Runs with Correct Status and Output Fields
*When Pipelines as Code creating check runs on GitHub*

**Personas:** CI/CD Engineer

**Goal:** Ensure check runs use proper status/conclusion and include Title, Summary, and Text output.

→ Lines 968-971: GitHub check run fix
  Source: Bug fixes - Pipelines as Code section

**What's fixed:**
- Check runs use statusOpts not hardcoded `in_progress`
- Title, Summary, Text fields included
- No patch attempts on invalid PipelineRun names

**Issue ID:** SRVKP-9141

---

### Job 77: Update GitLab Commit Status Correctly After Fixing Validation Errors
*When PipelineRun failed validation, errors fixed, but MR still shows failed*

**Personas:** CI/CD Engineer

**Goal:** Ensure commit status updates after validation fix to reflect correct status.

→ Lines 974-982: GitLab status update fix
  Source: Bug fixes - Pipelines as Code section

**What's fixed:**
- Commit status updated after validation fix
- Merge request shows correct status
- Auto-merge enabled after fix

**Issue IDs:** SRVKP-9141, SRVKP-9044

---

### Job 78: Copy Multiple Images Using skopeo-copy Task with url.txt File
*When copying many container images with skopeo-copy task*

**Personas:** DevOps Engineer

**Goal:** Use url.txt file for bulk image copying regardless of source and destination URL parameters.

→ Lines 987-990: skopeo-copy task fix
  Source: Bug fixes - Tasks section

**What's fixed:**
- skopeo-copy task parameters are optional
- url.txt file method works
- Multiple images copied successfully

**Issue ID:** SRVKP-6491

---

### Job 79: Verify PipelineRun Deletion Metric has Correct Description
*When monitoring Tekton Results metrics*

**Personas:** Platform Administrator

**Goal:** Understand prDeleteDuration metric measures time between completion and deletion.

→ Lines 995-998: Metric description fix
  Source: Bug fixes - Tekton Results section

**What's fixed:**
- Metric description accurate
- Time between completion and deletion measured
- No confusion in metrics reporting

**Issue ID:** SRVKP-9138

---

### Job 80: Prevent Database Constraint Violations from Race Conditions in Results Watcher
*When experiencing PostgreSQL unique-constraint violations in Tekton Results*

**Personas:** Platform Administrator

**Goal:** Ensure proper handling of duplicate key errors by refetching existing records.

→ Lines 1000-1003: Race condition fix
  Source: Bug fixes - Tekton Results section

**What's fixed:**
- Race condition fixed for concurrent Result record creation
- Duplicate key errors handled correctly
- PostgreSQL error translator added
- No ambiguous Unknown errors (now proper gRPC codes)

**Issue ID:** SRVKP-9138

---

### Job 81: Ensure Reliable Annotation Updates with Server-Side Apply
*When Tekton Results managing annotations on Kubernetes objects*

**Personas:** Platform Administrator

**Goal:** Use SSA for reliable, conflict-aware annotation updates instead of merge patches.

→ Lines 1005-1008: Server-Side Apply for annotations
  Source: Bug fixes - Tekton Results section

**What's improved:**
- Server-Side Apply used for annotations
- Single Patch operation (not Get-Update-Patch)
- Reliable updates
- Conflict-aware

**Issue ID:** SRVKP-9138

---

### Job 82: Ensure defaultRetention Takes Precedence Over Deprecated maxRetention Field
*When upgrading Tekton Results with deprecated maxRetention field in config*

**Personas:** Platform Administrator

**Goal:** Verify defaultRetention field correctly takes precedence during upgrade.

→ Lines 1010-1013: Retention field precedence fix
  Source: Bug fixes - Tekton Results section

**What's fixed:**
- `defaultRetention` takes precedence over deprecated `maxRetention`
- Behavior consistent with TektonConfig CR
- Backward compatibility maintained

**Issue ID:** SRVKP-9425

---

### Job 83: Download Latest git-clone Task Version 0.10 Instead of Outdated 0.9
*When installing git-clone task from Tekton Hub*

**Personas:** DevOps Engineer

**Goal:** Ensure latest version 0.10 is downloaded, not outdated 0.9.0.

→ Lines 1017-1020: git-clone task version fix
  Source: Bug fixes - Tekton Hub section

**What's fixed:**
- git-clone task version 0.10 downloaded
- Latest improvements available
- No version inconsistencies

**Issue ID:** SRVKP-8568

---

### Job 85: Ensure TaskRun Finalizers are Removed for Proper Cleanup
*When TaskRun resources not cleaning up properly*

**Personas:** Platform Administrator

**Goal:** Verify old TaskRun finalizer is removed so resources clean up as expected.

→ Lines 1030-1033: TaskRun finalizer removal
  Source: Bug fixes - Tekton Chains section

**What's fixed:**
- Old finalizer removed from TaskRun resources
- TaskRun resources cleaned up properly
- No lingering resources

**Issue ID:** SRVKP-9137

---

### Job 88: Troubleshoot Additional Issues
*When encountering other issues in OpenShift Pipelines 1.21*

**Personas:** Platform Administrator, CI/CD Engineer, DevOps Engineer

**Additional bug fixes not covered above:**

All additional bug fixes are documented in the release notes with SRVKP issue IDs for reference and support escalation.

---

## Appendices

### A. Workflow Coverage Analysis

| Stage | Coverage | Jobs | Notes |
|-------|----------|------|-------|
| EVALUATE | ✅ | Jobs 1, 18, 23 | Platform compatibility, feature status |
| ONBOARD | ✅ | Job 8 | Tekton Results setup |
| USE | ✅ | Jobs 2-7, 9-16, 24-26, 28-29, 36, 53, 56, 58, 64-70, 73-78, 83 | Core feature usage, configuration |
| OPTIMIZE | ✅ | Jobs 4, 11, 17, 20, 30-34, 46, 71, 84 | Performance, caching, pruning, retention |
| GOVERN | ✅ | Jobs 7, 33 | RBAC, limits enforcement |
| MIGRATE | ✅ | Jobs 22, 27, 39, 86 | Database upgrades, breaking changes |
| PLAN | ✅ | Jobs 37-38, 87 | Breaking changes, deprecations |
| TROUBLESHOOT | ✅ | Jobs 19, 35, 40-88 | Bug fixes, known issues |

**Gaps Identified:** None - comprehensive coverage across all workflow stages

---

### B. Breaking Changes Quick Reference

| Change | Impact | Action Required | Job |
|--------|--------|----------------|------|
| Console plugin must be enabled | No Pipelines UI by default | Enable console plugin | Job 37 |
| HS256 tokens not supported | Keyless signing fails | Migrate OIDC to RS256 | Job 39 |

---

### C. Deprecation Timeline

| Feature | Status | Timeline | Action | Job |
|---------|--------|----------|--------|------|
| pipelinerun_status field | Deprecated | Future removal (TBD) | Update integrations | Job 38 |
| OpenCensus | Deprecated | Future removal (TBD) | Prepare OpenTelemetry migration | Job 87 |
| Static console plugin | Deprecated | 1.21 | Enable dynamic plugin | Job 37 |
| PostgreSQL 13 | EOL approaching | Upgrade to 15 | Complete migration | Jobs 22, 27 |

---

### D. Component Version Quick Reference

| Component | Version | Status |
|-----------|---------|--------|
| Pipelines Operator | 1.21.0 | GA |
| Tekton Pipelines | 0.65.3 | GA |
| Tekton Triggers | 0.29.1 | GA |
| Tekton Results | 0.13.0 | GA |
| Pipelines as Code | 0.29.0 | GA |
| Tekton Chains | 0.23.1 | GA |
| Tekton Hub | 1.18.1 | GA |
| Tekton Cache | 0.2.2 | GA (new) |
| Manual Approval Gate | 0.2.1 | Technology Preview |

---

## Navigation Guide

### By User Journey

**Platform Administrator evaluating and installing:**
1. Job 1: Verify platform compatibility
2. Job 23: Assess Tekton Cache GA status
3. Job 8: Set up Tekton Results external access
4. Job 37: Plan for console plugin enablement

**Security Engineer hardening deployment:**
1. Job 2: Enforce read-only root filesystems
2. Job 7: Control service account permissions
3. Job 14: Enforce commit SHA validation
4. Job 26: Enforce SHA-256 webhooks
5. Job 28: Configure selective signing in Chains

**CI/CD Engineer building pipelines:**
1. Job 3: Override task timeouts
2. Job 5: Use arrays in when expressions
3. Job 6: Add display names to steps
4. Job 9: Configure group approvers
5. Job 13: Trigger pipelines on tags
6. Job 15: Use glob patterns for webhooks

**DevOps Engineer optimizing performance:**
1. Job 4: Enable resolver caching
2. Job 11: Enable GitLab ACL caching
3. Job 30: Adopt event-driven pruner
4. Job 31: Configure namespace pruning
5. Job 17: Set retention policies

**Platform Administrator upgrading from 1.20:**
1. Job 37: Plan console plugin enablement
2. Job 39: Migrate OIDC to RS256 (if using Chains)
3. Job 22: Complete PostgreSQL migration (Results)
4. Job 27: Complete PostgreSQL migration (Hub)
5. Job 86: Verify pruner config retained

---

## Document Statistics

**Workflow Coverage:**
- EVALUATE: 3 jobs
- ONBOARD: 1 job
- USE: 35 jobs
- OPTIMIZE: 11 jobs
- GOVERN: 2 jobs
- MIGRATE: 4 jobs
- PLAN: 3 jobs
- TROUBLESHOOT: 49 jobs

**Main Jobs:** 88
**Technology Preview Features:** 2 (Manual Approval Gate, tkn pac cel)
**Breaking Changes:** 2
**Deprecated Features:** 3
**Source Lines:** 1059 (complete release notes document)
**Supported OpenShift Versions:** 8 (4.14 through 4.21)

---

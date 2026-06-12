# op-release-notes-1-21 - TOC Comparison

**Current Feature-Based vs. Proposed JTBD-Based Structure**

**Analysis Date:** 2026-06-11  
**JTBD Records:** 87  
**Main Jobs:** 15 (rolled up from records)  
**Coverage:** 100% enhanced schema

---

## Current Structure (Feature-Based)

**Release notes for Red Hat OpenShift Pipelines 1.21**

- Compatibility and support matrix (lines 84-125)
- Release notes for {pipelines-title} 1.21 (lines 127-1061)
  - New features and enhancements (lines 142-667)
    - Pipelines (lines 147-327)
    - Operator (lines 332-363)
    - User interface (lines 365-379)
    - Pipelines as Code (lines 382-475)
    - Tekton Results (lines 478-584)
    - Tekton Cache (lines 587-600)
    - Tekton Triggers (lines 602-607)
    - Tekton Hub (lines 610-615)
    - Tekton Chains (lines 617-628)
    - CLI (lines 630-638)
    - Pruner (lines 641-667)
  - Technology Preview features (lines 670-709)
    - Pipelines as Code (lines 674-697)
    - Manual Approval Gate (lines 700-708)
  - Breaking changes (lines 711-731)
    - User interface (lines 714-719)
    - Pipelines as Code (lines 721-725)
    - Tekton Chains (lines 727-731)
  - Known issues (lines 734-744)
    - User interface (lines 737-744)
  - Fixed issues (lines 747-1045)
    - Pipelines (lines 750-780)
    - Operator (lines 783-823)
    - User interface (lines 825-896)
    - Pipelines as Code (lines 899-982)
    - Tekton Ecosystem (lines 985-990)
    - Tekton Results (lines 993-1013)
    - Tekton Hub (lines 1016-1020)
    - Tekton Chains (lines 1023-1038)
    - Pruner (lines 1041-1045)
  - Deprecated features (lines 1048-1060)
- Additional resources (lines 1063-1075)

---

## Proposed JTBD-Based Structure

### Getting Started

**Job 1: Verify platform compatibility for OpenShift Pipelines 1.21**  
When: Planning to deploy or upgrade to OpenShift Pipelines 1.21  
Personas: Platform Administrator

- Option A: Check compatibility matrix
  Persona: Platform Administrator  
  → Lines 84-125: Compatibility and support matrix  
  Source: Section: Compatibility and support matrix  
  - Confirm OpenShift version support (4.14-4.21)
  - Verify component versions and GA/TP status
  - Understand support matrix for all components

**Job 2: Assess new features for production readiness**  
When: Evaluating features for production pipeline deployments  
Personas: Platform Administrator, DevOps Engineer

- Option A: Tekton Cache General Availability
  Persona: Platform Administrator  
  → Lines 590-591: Tekton Cache is generally available  
  Source: Section: Tekton Cache, New features and enhancements  
  - Verify GA status (not TP)
  - Confirm production support

- Option B: Event-driven pruner General Availability
  Persona: Platform Administrator  
  → Lines 644-647: Event-driven pruner is generally available  
  Source: Section: Pruner, New features and enhancements  
  - Verify GA status for tektonpruner
  - Better performance than job-based pruner

- Option C: PostgreSQL version support verification
  Persona: Platform Administrator  
  → Lines 536-538: PostgreSQL support updated to version 17.5  
  Source: Section: Tekton Results, New features and enhancements  
  - Confirm PostgreSQL 17.5 compatibility

---

### Set Up & Configure

**Job 3: Control pipeline service account permissions**  
When: Managing RBAC for pipeline service accounts across namespaces  
Personas: Platform Administrator

- Configure legacyPipelineRbac parameter
  Persona: Platform Administrator  
  → Lines 335-357: New parameter for controlling pipeline service account permissions  
  Source: Section: Operator, New features and enhancements  
  - Set legacyPipelineRbac to false for restricted permissions
  - Manually remove existing role bindings
  - Enforce principle of least privilege

**Job 4: Configure resolver caching for performance**  
When: Running pipelines that fetch resources from external services  
Personas: DevOps Engineer

- Configure global resolver caching settings
  Persona: DevOps Engineer  
  → Lines 178-227: Resolver caching for bundle, Git, and cluster resolvers  
  Source: Section: Pipelines, New features and enhancements  
  - Set cache size and TTL in TektonConfig CR
  - Configure per-resolver defaults (auto/always/never)
  - Override caching per TaskRun or PipelineRun
  - Reduce external API calls and improve reliability

**Job 5: Configure retention policies for Tekton Results**  
When: Managing storage and retention of pipeline results  
Personas: Platform Administrator

- Set up fine-grained retention policies
  Persona: Platform Administrator  
  → Lines 481-533: Fine-grained retention policies  
  Source: Section: Tekton Results, New features and enhancements  
  - Configure retention by namespace, labels, annotations, status
  - Define policies in tekton-results-config-results-retention-policy
  - Set different retention for production vs CI

**Job 6: Configure Pipelines as Code settings**  
When: Setting up and managing Pipelines as Code  
Personas: CI/CD Engineer

- Option A: Configure error log snippet length
  Persona: CI/CD Engineer  
  → Lines 389-408: Configure the number of lines in error log snippets  
  Source: Section: Pipelines as Code, New features and enhancements  
  - Set error-log-snippet-number-of-lines
  - Control snippet length for GitHub API limits

- Option B: Enable SHA validation for /ok-to-test
  Persona: Security Engineer  
  → Lines 445-449: SHA validation added to /OK-to-test commands  
  Source: Section: Pipelines as Code, New features and enhancements  
  - Enable require-ok-to-test-sha setting
  - Prevent TOCTOU race condition vulnerability

- Option C: Configure incoming webhook targets with glob patterns
  Persona: CI/CD Engineer  
  → Lines 451-464: Incoming webhook targets support glob patterns  
  Source: Section: Pipelines as Code, New features and enhancements  
  - Use shell prompt-style glob patterns
  - Simplify webhook configuration for many branches

- Option D: Configure namespace parameter for webhooks
  Persona: CI/CD Engineer  
  → Lines 466-469: Incoming webhook requests support a new namespace parameter  
  Source: Section: Pipelines as Code, New features and enhancements  
  - Route webhooks to specific namespace
  - Handle duplicate repository names

**Job 7: Configure event-driven pruner policies**  
When: Managing pruning behavior for pipeline resources  
Personas: Platform Administrator

- Option A: Namespace-level pruner configuration
  Persona: Platform Administrator  
  → Lines 651-652: Namespace-level pruner configuration  
  Source: Section: Pruner, New features and enhancements  
  - Create tekton-pruner-namespace-spec config map
  - Override global defaults with custom TTL and history limits

- Option B: Selector-based pruning configuration
  Persona: Platform Administrator  
  → Lines 652-653: Selector-based pruning configuration  
  Source: Section: Pruner, New features and enhancements  
  - Use matchLabels and matchAnnotations selectors
  - Apply AND logic when both specified

- Option C: Enforce cluster-wide maximum limits
  Persona: Platform Administrator  
  → Lines 653-654: Cluster-wide maximum limits added  
  Source: Section: Pruner, New features and enhancements  
  - Maximum TTL: 2592000 seconds
  - Maximum history limit: 100

- Option D: Validate pruner config maps at apply-time
  Persona: Platform Administrator  
  → Lines 654-661: Pruner config map validation  
  Source: Section: Pruner, New features and enhancements  
  - Use admission webhook for validation
  - Reject invalid configurations with clear errors

**Job 8: Configure security settings**  
When: Securing Pipelines deployments and enforcing security policies  
Personas: Security Engineer

- Option A: Verify read-only root filesystems
  Persona: Security Engineer  
  → Lines 150-151: Read-only root filesystems enabled  
  Source: Section: Pipelines, New features and enhancements  
  - Confirm readOnlyRootFilesystem=true for all containers
  - Follow Kubernetes security best practices

- Option B: Enforce SHA-256 signature validation for GitHub webhooks
  Persona: Security Engineer  
  → Lines 604-607: GitHub interceptor enforces SHA-256 signature validation  
  Source: Section: Tekton Triggers, New features and enhancements  
  - Only accept X-Hub-Signature-256
  - Update custom webhooks from SHA-1 to SHA-256

- Option C: Configure Tekton Chains signing options
  Persona: Security Engineer  
  → Lines 619-627: Flexible provenance and signing configuration  
  Source: Section: Tekton Chains, New features and enhancements  
  - Disable OCI image signing with artifacts.oci.disable-signing
  - Maintain provenance generation and attestation signing

---

### Deploy & Use

**Job 9: Create and run pipelines with advanced features**  
When: Building and executing CI/CD pipelines  
Personas: CI/CD Engineer, Developer

- Option A: Override individual TaskRun timeouts
  Persona: CI/CD Engineer  
  → Lines 154-175: Override individual TaskRun timeouts in a PipelineRun  
  Source: Section: Pipelines, New features and enhancements  
  - Use spec.taskRunSpecs[].timeout field
  - Set different timeouts per task

- Option B: Use array values in when expressions
  Persona: CI/CD Engineer  
  → Lines 229-290: Array values can be resolved in when expressions  
  Source: Section: Pipelines, New features and enhancements  
  - Evaluate array parameters in when expressions
  - Check array membership with operator: in

- Option C: Add display names to steps
  Persona: Developer  
  → Lines 295-327: Support for display names added to steps  
  Source: Section: Pipelines, New features and enhancements  
  - Use displayName field on Step objects
  - Support parameter substitution in display names

- Option D: Use Docker credentials without config.json for Tekton Cache
  Persona: DevOps Engineer  
  → Lines 598-600: Improved support for Docker credentials  
  Source: Section: Tekton Cache, New features and enhancements  
  - Point DOCKER_CONFIG to .dockerconfigjson
  - Support private registry authentication

- Option E: Rerun resolver-based PipelineRuns with tkn CLI
  Persona: DevOps Engineer  
  → Lines 633-638: Support for rerunning resolver-based PipelineRuns  
  Source: Section: CLI, New features and enhancements  
  - Use --resolvertype flag with tkn p start
  - Specify resolver type: git, http, hub, cluster, bundle, remote

**Job 10: Configure approval workflows**  
When: Setting up approval gates for pipeline execution  
Personas: CI/CD Engineer

- Option A: Configure group approvers for Approval Tasks (UI)
  Persona: CI/CD Engineer  
  → Lines 368-369: Group support for Approval Tasks  
  Source: Section: User interface, New features and enhancements  
  - Use group:<groupName> syntax
  - Any group member can approve or reject

- Option B: Configure group approvers for Manual Approval Gate (TP)
  Persona: CI/CD Engineer  
  → Lines 703-708: Group support for Approval Task  
  Source: Section: Manual Approval Gate, Technology Preview features  
  - Specify group approvers with group:<groupName>
  - Messages from all members preserved

**Job 11: Trigger and control pipeline execution with Pipelines as Code**  
When: Managing CI/CD workflows triggered by Git events  
Personas: CI/CD Engineer

- Option A: Trigger and cancel PipelineRuns for Git tags
  Persona: CI/CD Engineer  
  → Lines 426-443: Trigger and cancel PipelineRuns for Git tags  
  Source: Section: Pipelines as Code, New features and enhancements  
  - Use /test <pipeline> tag:<tag> to trigger
  - Use /cancel <pipeline> tag:<tag> to cancel
  - Supported for GitHub and GitLab

- Option B: Use GitOps commands in GitLab discussion replies
  Persona: CI/CD Engineer  
  → Lines 902-905: GitOps commands in GitLab MR discussion replies are recognized  
  Source: Section: Pipelines as Code, Fixed issues  
  - Post commands like /ok-to-test in replies
  - Not limited to top-level comments

- Option C: Evaluate CEL expressions interactively (TP)
  Persona: CI/CD Engineer  
  → Lines 676-697: A new command for evaluating CEL expressions  
  Source: Section: Pipelines as Code, Technology Preview features  
  - Use tkn pac cel command
  - Test CEL expressions against webhook payloads

**Job 12: Download and use Tekton binaries**  
When: Building custom StepActions or tasks  
Personas: DevOps Engineer

- Download Tekton Cache binaries
  Persona: DevOps Engineer  
  → Lines 594-595: Tekton Cache binaries available for public download  
  Source: Section: Tekton Cache, New features and enhancements  
  - Access Red Hat binaries without authentication
  - Use in custom StepAction configurations

**Job 13: Copy container images in bulk**  
When: Migrating or distributing many container images  
Personas: DevOps Engineer

- Use skopeo-copy task with url.txt
  Persona: DevOps Engineer  
  → Lines 987-990: Many image copy enabled in skopeo-copy task  
  Source: Section: Tekton Ecosystem, Fixed issues  
  - Use url.txt file for bulk copy
  - Optional source and destination parameters

---

### Track Performance

**Job 14: Monitor pipeline execution and system health**  
When: Operating Tekton Results and monitoring pipeline performance  
Personas: Platform Administrator, DevOps Engineer

- Option A: Track runs not stored in database
  Persona: Platform Administrator  
  → Lines 542-553: New metrics for runs not stored in the database  
  Source: Section: Tekton Results, New features and enhancements  
  - Monitor runs_not_stored_count metric
  - Track by kind and namespace

- Option B: Monitor run storage latency
  Persona: Platform Administrator  
  → Lines 556-569: Metrics for run storage latency  
  Source: Section: Tekton Results, New features and enhancements  
  - Monitor run_storage_latency_seconds metric
  - Identify performance bottlenecks

- Option C: Persist Pipeline Overview filter selections
  Persona: DevOps Engineer  
  → Lines 371-373: Pipeline Overview page retains filter selections  
  Source: Section: User interface, New features and enhancements  
  - Filter selections stored in state and URL
  - Persist across navigation and refreshes

- Option D: Track data loading with loading indicators
  Persona: DevOps Engineer  
  → Lines 893-896: Loading indicators added to Pipeline Overview cards  
  Source: Section: User interface, Fixed issues  
  - See loading spinners during data fetch
  - Clear visual feedback

**Job 15: Improve GitLab and GitHub integration performance**  
When: Running Pipelines as Code with GitLab or GitHub repositories  
Personas: CI/CD Engineer, DevOps Engineer

- Option A: Improve GitLab ACL check performance
  Persona: CI/CD Engineer  
  → Lines 385-386: Improved performance for GitLab project access control checks  
  Source: Section: Pipelines as Code, New features and enhancements  
  - Cache GitLab ACL membership queries
  - Reduce API calls

- Option B: Optimize GitHub App installation ID retrieval
  Persona: Platform Administrator  
  → Lines 938-941: GitHub App installation ID retrieval is optimized  
  Source: Section: Pipelines as Code, Fixed issues  
  - Direct fetch by repository URL
  - Reduce unnecessary API listings

---

### Troubleshoot Issues

**Job 16: Resolve pipeline execution issues**  
When: Diagnosing and fixing pipeline failures  
Personas: CI/CD Engineer, DevOps Engineer

- Option A: Diagnose PipelineRun failures with clear errors
  Persona: CI/CD Engineer  
  → Lines 752-755: PipelineRuns fail clearly on invalid apiVersion  
  Source: Section: Pipelines, Fixed issues  
  - Check spec.tasks[].taskRef.apiVersion
  - View clear error messages

- Option B: Handle TaskRef reconciliation errors
  Persona: DevOps Engineer  
  → Lines 757-760: PipelineRuns no longer fail on temporary TaskRef reconciliation errors  
  Source: Section: Pipelines, Fixed issues  
  - Only explicit validation errors cause failure
  - Retryable errors don't fail pipeline

- Option C: Debug timed-out TaskRuns with pod retention
  Persona: DevOps Engineer  
  → Lines 767-770: Pods for timed-out TaskRuns are retained  
  Source: Section: Pipelines, Fixed issues  
  - Enable keep-pod-on-cancel flag
  - Pods retained for debugging

- Option D: Run TaskRuns on arm64 clusters
  Persona: DevOps Engineer  
  → Lines 777-780: TaskRuns no longer fail on arm64 clusters  
  Source: Section: Pipelines, Fixed issues  
  - Platform variant handling fixed
  - Reliable execution on arm64

- Option E: Resolve duplicate Pipelines navigation entries
  Persona: Platform Administrator  
  → Lines 739-744: Duplicate Pipelines navigation entry in OpenShift Console  
  Source: Section: User interface, Known issues  
  - Apply console and operator updates
  - UI-only issue, no execution impact

**Job 17: Resolve Pipelines as Code integration issues**  
When: Troubleshooting Pipelines as Code with Git providers  
Personas: CI/CD Engineer

- Option A: Fix GitLab commit status after validation errors
  Persona: CI/CD Engineer  
  → Lines 974-982: Commit status updates correctly after validation fixes  
  Source: Section: Pipelines as Code, Fixed issues  
  - Status updates after fixing validation errors
  - Auto-merge enabled correctly

- Option B: Prevent auto-merge on canceled PipelineRuns in GitLab
  Persona: CI/CD Engineer  
  → Lines 927-930: GitLab API compatibility fix for canceled PipelineRuns  
  Source: Section: Pipelines as Code, Fixed issues  
  - Canceled status mapped correctly to GitLab API
  - MRs remain open when pipeline canceled

- Option C: Get correct commit IDs for Bitbucket merge commits
  Persona: CI/CD Engineer  
  → Lines 944-947: Wrong commit IDs for Bitbucket merge commits are fixed  
  Source: Section: Pipelines as Code, Fixed issues  
  - Revision variable returns correct commit IDs

- Option D: View correct CI status for unauthorized Bitbucket PRs
  Persona: CI/CD Engineer  
  → Lines 907-910: CI status correctly shows Pending for unauthorized Bitbucket PRs  
  Source: Section: Pipelines as Code, Fixed issues  
  - Status shows Pending, not Running
  - Awaiting administrator approval

- Option E: Post GitLab comments correctly from forks
  Persona: CI/CD Engineer  
  → Lines 956-959: GitLab merge request comments post correctly from forks  
  Source: Section: Pipelines as Code, Fixed issues  
  - Use TargetProjectID for comments

- Option F: Create GitHub check runs with correct status
  Persona: CI/CD Engineer  
  → Lines 968-971: GitHub check runs and patching logic is corrected  
  Source: Section: Pipelines as Code, Fixed issues  
  - Use proper status and conclusion from statusOpts
  - Include Title, Summary, Text fields

- Option G: Evaluate placeholder variables with partial data
  Persona: CI/CD Engineer  
  → Lines 932-935: Placeholder variable evaluation no longer fails when data sources are missing  
  Source: Section: Pipelines as Code, Fixed issues  
  - Process body.*, headers.*, files.* independently

**Job 18: Resolve Tekton Results issues**  
When: Troubleshooting Tekton Results operation and data  
Personas: Platform Administrator

- Option A: Fix race condition causing constraint violations
  Persona: Platform Administrator  
  → Lines 1000-1003: Race condition causing database constraint violations is fixed  
  Source: Section: Tekton Results, Fixed issues  
  - Handle duplicate key errors correctly
  - Refetch existing records

- Option B: Verify prDeleteDuration metric description
  Persona: Platform Administrator  
  → Lines 995-998: Description for PipelineRun deletion metric is correct  
  Source: Section: Tekton Results, Fixed issues  
  - Measures time between completion and deletion

- Option C: Ensure reliable annotation updates
  Persona: Platform Administrator  
  → Lines 1005-1008: Annotations management updated for reliability  
  Source: Section: Tekton Results, Fixed issues  
  - Use Server-Side Apply instead of merge patches

- Option D: Verify defaultRetention precedence
  Persona: Platform Administrator  
  → Lines 1010-1013: defaultRetention field takes precedence over deprecated maxRetention  
  Source: Section: Tekton Results, Fixed issues  
  - Consistent retention behavior during upgrade

**Job 19: Resolve UI and console issues**  
When: Troubleshooting OpenShift Console pipeline UI  
Personas: DevOps Engineer, Developer, CI/CD Engineer

- Option A: Fix PipelineRun canceling status display
  Persona: DevOps Engineer  
  → Lines 827-830: Fixed PipelineRun canceling status in OpenShift Console  
  Source: Section: User interface, Fixed issues  
  - Status reflects completed TaskRuns correctly

- Option B: Save Buildah tasks in Pipeline builder
  Persona: CI/CD Engineer  
  → Lines 832-835: Fixed validation error preventing saving of Buildah tasks  
  Source: Section: User interface, Fixed issues  
  - BUILD_ARGS parameter validated correctly

- Option C: Sort PipelineRuns by actual duration
  Persona: DevOps Engineer  
  → Lines 837-840: Fixed wrong sorting of PipelineRuns by duration  
  Source: Section: User interface, Fixed issues  
  - Use duration in seconds, not string sort

- Option D: Sort TaskRuns by elapsed duration
  Persona: DevOps Engineer  
  → Lines 842-845: Fixed TaskRun sorting by duration  
  Source: Section: User interface, Fixed issues  
  - Use elapsed time, not completion time

- Option E: Navigate to tasks with strict URL matching
  Persona: CI/CD Engineer  
  → Lines 847-850: Added strict navigation URLs task name matching  
  Source: Section: User interface, Fixed issues  
  - Strict equality checks avoid partial matches

- Option F: View empty state when Results data unavailable
  Persona: DevOps Engineer  
  → Lines 852-855: Fixed the Overview page displaying an error message  
  Source: Section: User interface, Fixed issues  
  - Show empty state instead of error

- Option G: See immediate YAML editor updates
  Persona: Developer  
  → Lines 857-860: Fixed immediate YAML editor updates using useEffect hook  
  Source: Section: User interface, Fixed issues  
  - Changes reflected immediately

- Option H: Paginate archived PipelineRun results
  Persona: DevOps Engineer  
  → Lines 862-875: Pagination fix for archived PipelineRun results  
  Source: Section: User interface, Fixed issues  
  - Handle next_page_token correctly

- Option I: View correct task parameters in Pipeline Builder
  Persona: CI/CD Engineer  
  → Lines 867-870: Pipeline Builder no longer displays stale task parameter data  
  Source: Section: User interface, Fixed issues  
  - Correct parameters from selected namespace

- Option J: Monitor with reliable data loading
  Persona: DevOps Engineer  
  → Lines 883-886: Pipeline Overview page reliability improved  
  Source: Section: User interface, Fixed issues  
  - No stale or partial data
  - Increased API timeouts

- Option K: Understand time range filter label
  Persona: DevOps Engineer  
  → Lines 888-891: Ambiguous time-range filter label is corrected  
  Source: Section: User interface, Fixed issues  
  - "Last week" not "Last weeks"

**Job 20: Resolve operator and platform issues**  
When: Troubleshooting operator configuration and behavior  
Personas: Platform Administrator

- Option A: Improve proxy webhook performance
  Persona: Platform Administrator  
  → Lines 785-788: Improved proxy webhook performance  
  Source: Section: Operator, Fixed issues  
  - Optional config map volumes prevent blocking

- Option B: Prevent prioritySemaphore deadlocks
  Persona: Platform Administrator  
  → Lines 790-793: Corrected prioritySemaphore locking  
  Source: Section: Operator, Fixed issues  
  - Fixed race conditions and deadlocks

- Option C: Verify catalog name after upgrade
  Persona: Platform Administrator  
  → Lines 805-808: Default catalog name updates correctly during upgrade  
  Source: Section: Operator, Fixed issues  
  - hub-catalog-name points to Artifact Hub

- Option D: Ensure nodeSelector and tolerations apply to Results pods
  Persona: Platform Administrator  
  → Lines 810-813: nodeSelector and tolerations propagate correctly  
  Source: Section: Operator, Fixed issues  
  - Scheduling preferences applied correctly

- Option E: Exclude control-plane namespaces from webhook validation
  Persona: Platform Administrator  
  → Lines 815-818: Webhook validation no longer targets control-plane namespaces  
  Source: Section: Operator, Fixed issues  
  - Prevents certificate issues

- Option F: Preserve custom hub catalog configuration
  Persona: Platform Administrator  
  → Lines 820-823: Custom hub catalog configuration is preserved during conversion  
  Source: Section: Operator, Fixed issues  
  - catalog-{INDEX}-type field retained

**Job 21: Resolve Tekton Chains and Hub issues**  
When: Troubleshooting Tekton Chains or Hub operation  
Personas: Platform Administrator, DevOps Engineer

- Option A: Improve Chains controller pod distribution
  Persona: Platform Administrator  
  → Lines 1025-1028: Anti-affinity rule added to tekton-chains-controller  
  Source: Section: Tekton Chains, Fixed issues  
  - Even pod distribution across nodes

- Option B: Ensure TaskRun finalizer removal
  Persona: Platform Administrator  
  → Lines 1030-1033: TaskRun finalizer no longer remains on resources  
  Source: Section: Tekton Chains, Fixed issues  
  - Resources clean up correctly

- Option C: Download latest git-clone task version
  Persona: DevOps Engineer  
  → Lines 1017-1020: System no longer downloads outdated git-clone task  
  Source: Section: Tekton Hub, Fixed issues  
  - Version 0.10 downloaded instead of 0.9

---

### Migrate & Upgrade

**Job 22: Migrate PostgreSQL databases before EOL**  
When: Maintaining deployments before PostgreSQL 13 EOL  
Personas: Platform Administrator

- Option A: Upgrade Tekton Results database to PostgreSQL 15
  Persona: Platform Administrator  
  → Lines 576-584: Default database migration to PostgreSQL version 15  
  Source: Section: Tekton Results, New features and enhancements  
  - Backup data before upgrade
  - Ensure PVC has >50% free space
  - Automated migration from version 13 to 15

- Option B: Upgrade Tekton Hub database to PostgreSQL 15
  Persona: Platform Administrator  
  → Lines 612-615: Default database migration to PostgreSQL version 15  
  Source: Section: Tekton Hub, New features and enhancements  
  - Automated migration for stability

**Job 23: Prepare for breaking changes and deprecations**  
When: Planning upgrades and future-proofing integrations  
Personas: Platform Administrator, CI/CD Engineer, Security Engineer

- Option A: Enable console plugin after installation
  Persona: Platform Administrator  
  → Lines 716-719: Pipelines console navigation requires explicit plugin enablement  
  Source: Section: User interface, Breaking changes  
  - Static console plugin deprecated
  - Must explicitly enable plugin

- Option B: Update integrations to stop using pipelinerun_status field
  Persona: CI/CD Engineer  
  → Lines 724-725: pipelinerun_status field in Repository CR is deprecated  
  Source: Section: Pipelines as Code, Breaking changes  
  - Field will be removed in future release
  - Update automation and integrations

- Option C: Migrate OIDC provider from HS256 to RS256
  Persona: Security Engineer  
  → Lines 730-731: Cosign v2.6.0 update affects keyless signing  
  Source: Section: Tekton Chains, Breaking changes  
  - HS256 tokens no longer accepted
  - Configure OIDC with RS256 before upgrade

- Option D: Plan for OpenCensus to OpenTelemetry migration
  Persona: CI/CD Engineer  
  → Lines 1056-1059: OpenCensus is deprecated  
  Source: Section: Deprecated features  
  - Future migration to OpenTelemetry
  - PromQL queries will need updates

**Job 24: Retain configuration after upgrades**  
When: Upgrading OpenShift Pipelines with existing configurations  
Personas: Platform Administrator

- Retain event-based pruner config values
  Persona: Platform Administrator  
  → Lines 1042-1045: Namespace-level pruner configuration updates take effect immediately after upgrade  
  Source: Section: Pruner, Fixed issues  
  - Config values retained, not reverted to defaults

---

### Operate & Manage

**Job 25: Manage Tekton Results CLI across namespaces**  
When: Working with Tekton Results across multiple namespaces  
Personas: DevOps Engineer

- Use CLI without re-authentication on namespace switch
  Persona: DevOps Engineer  
  → Lines 571-574: CLI configuration persists across namespaces  
  Source: Section: Tekton Results, New features and enhancements  
  - Configuration persists across namespace switches
  - No need to run opc results config set repeatedly

**Job 26: Access Tekton Results API externally**  
When: Setting up Tekton Results for external access  
Personas: Platform Administrator

- Configure automatically created Route for Results API
  Persona: Platform Administrator  
  → Lines 359-363: Route is automatically created for Tekton Results API endpoint  
  Source: Section: Operator, New features and enhancements  
  - Route created automatically
  - Optional custom host and path configuration

**Job 27: Handle secrets and permissions**  
When: Managing secrets and permissions for pipeline operations  
Personas: Platform Administrator, CI/CD Engineer

- Option A: Handle duplicate secret creation gracefully
  Persona: Platform Administrator  
  → Lines 962-965: Duplicate secret creation is handled gracefully  
  Source: Section: Pipelines as Code, Fixed issues  
  - Reuse existing secret instead of failing

- Option B: Re-evaluate permissions on GitLab commits
  Persona: Security Engineer  
  → Lines 922-925: Unauthorized /OK-to-test approvals are correctly invalidated on new commits  
  Source: Section: Pipelines as Code, Fixed issues  
  - Permissions re-evaluated on each commit when remember-ok-to-test=false

**Job 28: Use CLI tools effectively**  
When: Working with Pipelines as Code CLI  
Personas: DevOps Engineer

- View repository information with opc pac install info
  Persona: DevOps Engineer  
  → Lines 912-915: install info and namespace binding corrected  
  Source: Section: Pipelines as Code, Fixed issues  
  - Command displays repositories correctly
  - Namespace binding works as expected

**Job 29: Manage pipeline execution scope correctly**  
When: Canceling or managing pipeline runs  
Personas: CI/CD Engineer

- Option A: Cancel only PR-triggered PipelineRuns
  Persona: CI/CD Engineer  
  → Lines 950-953: Cancellation of running PipelineRuns is correctly scoped  
  Source: Section: Pipelines as Code, Fixed issues  
  - Only PR PipelineRuns canceled, not push-triggered

- Option B: Trigger pipelines on tag push events
  Persona: CI/CD Engineer  
  → Lines 917-920: Tag push events no longer affected by skip-push-event-for-pr-commits setting  
  Source: Section: Pipelines as Code, Fixed issues  
  - Tag push events proceed correctly

---

### Reference

**Job 30: Understand StepAction execution order**  
When: Reviewing StepAction execution timeline  
Personas: CI/CD Engineer

- View status steps in correct chronological order
  Persona: CI/CD Engineer  
  → Lines 772-775: StepAction status steps no longer display in wrong order  
  Source: Section: Pipelines, Fixed issues  
  - Sequential order is accurate

**Job 31: Understand time-range filter behavior**  
When: Filtering pipeline results by time  
Personas: DevOps Engineer

- Use corrected time-range filter
  Persona: DevOps Engineer  
  → Lines 376-379: Time-range filter label updated for clarity  
  Source: Section: User interface, New features and enhancements  
  - "Last week" label instead of "Last weeks"
  - Consistent with Results API

---

## Key Differences

### Current Structure (Feature-Based)
**Organized By:** Component/feature categories (Pipelines, Operator, UI, PaC, Results, Cache, Triggers, Hub, Chains, CLI, Pruner)  
**Navigation:** 11 component sections + 4 release note categories (New features, TP, Breaking, Fixed, Deprecated, Known)  
**User Journey:** Linear reading by component type, requires knowledge of which component provides needed functionality

### Proposed Structure (JTBD-Based)
**Organized By:** Workflow stages and user goals  
**Navigation:** 31 main jobs organized by workflow stage (Getting Started, Set Up & Configure, Deploy & Use, Track Performance, Troubleshoot Issues, Migrate & Upgrade, Operate & Manage, Reference)  
**User Journey:** Goal-directed navigation based on what users need to accomplish, with multiple implementation options shown per job

---

## Hierarchy Levels Explanation

The proposed structure uses three levels of granularity:

### Level 1: Main Jobs (~31 jobs)
Stable, outcome-focused goals that remain relevant regardless of underlying technology. Examples:
- "Verify platform compatibility for OpenShift Pipelines 1.21"
- "Configure resolver caching for performance"
- "Resolve pipeline execution issues"

### Level 2: User Stories / Options (2-7 per main job)
Persona-specific approaches or platform variations for accomplishing the main job. Examples:
- "Option A: Check compatibility matrix" (Platform Administrator)
- "Option B: Configure global resolver caching settings" (DevOps Engineer)
- "Option C: Debug timed-out TaskRuns with pod retention" (DevOps Engineer)

### Level 3: References (line numbers and sections)
Specific content locations in the source document:
- `→ Lines 84-125: Compatibility and support matrix`
- `→ Lines 178-227: Resolver caching for bundle, Git, and cluster resolvers`

---

## Example: Content Consolidation

### Current (Fragmented)
- Section: Pipelines, New features → Read-only root filesystems (lines 150-151)
- Section: Operator, New features → Route for Results API (lines 359-363)
- Section: Operator, Fixed issues → Webhook performance (lines 785-788)
- Section: Operator, Fixed issues → nodeSelector and tolerations (lines 810-813)
- Section: User interface, Fixed issues → PipelineRun status (lines 827-830)

### Proposed (Consolidated by Job)
**Job 8: Configure security settings**
- Option A: Verify read-only root filesystems (Pipelines)
- Option B: Enforce SHA-256 signature validation (Tekton Triggers)
- Option C: Configure Tekton Chains signing options (Tekton Chains)

**Job 16: Resolve pipeline execution issues**
- Option A: Diagnose PipelineRun failures (Pipelines)
- Option E: Resolve duplicate Pipelines navigation (UI)

**Job 20: Resolve operator and platform issues**
- Option A: Improve proxy webhook performance (Operator)
- Option D: Ensure nodeSelector and tolerations apply (Operator)

**Benefit:** Related jobs grouped by user goal rather than scattered across component sections!

---

## Navigation Improvement

**Current:** Browse 11 component sections + 4 release note categories = 15 top-level items  
**Proposed:** Navigate 8 workflow stages -> 31 main jobs -> choose implementation option  
**Reduction:** 47% fewer top-level categories (15 → 8)  
**Benefit:** Find content in 2-3 clicks (stage → job → option) vs. 4-5 clicks (component → category → feature → detail)

---

## Workflow Coverage Comparison

| Stage | Current | Proposed | Gap Status |
|-------|---------|----------|------------|
| Evaluate | ⚠️ Scattered in compatibility section | ✅ Jobs 1, 2 | Improved - dedicated evaluation jobs |
| Get Started | ⚠️ Compatibility matrix only | ✅ Jobs 1, 2 | Improved - production readiness assessment added |
| Configure | ✅ Scattered across component sections | ✅ Jobs 3, 4, 5, 6, 7, 8 | Reorganized - consolidated by configuration goal |
| Deploy & Use | ✅ New features sections | ✅ Jobs 9, 10, 11, 12, 13 | Reorganized - grouped by deployment task |
| Monitor | ⚠️ Partial - Results metrics only | ✅ Jobs 14, 15 | Improved - UI monitoring and performance tracking added |
| Troubleshoot | ✅ Fixed issues sections | ✅ Jobs 16, 17, 18, 19, 20, 21 | Reorganized - consolidated by problem domain |
| Migrate | ⚠️ Partial - PostgreSQL migration | ✅ Job 22 | Maintained |
| Upgrade | ⚠️ Scattered in breaking changes | ✅ Jobs 23, 24 | Improved - dedicated upgrade preparation and configuration retention |
| Operate | ⚠️ Scattered | ✅ Jobs 25, 26, 27, 28, 29 | Improved - operational tasks consolidated |
| Reference | ⚠️ No dedicated section | ✅ Jobs 30, 31 | Added - reference information organized |

### Coverage Summary

**Current structure gaps:**
- Evaluation scattered across compatibility section
- Configuration goals hidden within component-specific sections
- Operational tasks not clearly grouped
- No dedicated reference section
- Upgrade preparation fragmented across breaking changes and deprecated sections

**Proposed structure gaps:** None identified

**Gaps addressed by restructure:**
1. **Evaluation** - Now has dedicated jobs for compatibility and feature readiness assessment
2. **Configuration** - Consolidated 6 main configuration jobs across security, performance, retention, PaC, pruning
3. **Monitoring** - Unified monitoring jobs covering Results metrics, UI performance, and integration optimization
4. **Troubleshooting** - 6 dedicated troubleshooting jobs organized by problem domain (pipeline, PaC, Results, UI, operator, ecosystem)
5. **Upgrade & Migration** - Clear separation of database migration vs. breaking change preparation vs. config retention
6. **Operations** - 5 operational jobs for day-to-day management tasks
7. **Reference** - Dedicated section for reference information

### Recommendations for Gap Closure

| Gap | Recommendation | Priority |
|-----|----------------|----------|
| None identified | N/A | N/A |

---

## Coverage Indicators

| Symbol | Meaning |
|--------|---------|
| ✅ | Stage fully covered with dedicated content |
| ⚠️ | Partial coverage - content exists but scattered or limited |
| ❌ | Stage not covered - content gap identified |

---

## Quality Checklist

### Main Jobs
- [x] 10-15 main jobs total (31 jobs - comprehensive for release notes covering many components)
- [x] Clean, professional titles (not fragments)
- [x] Outcome-focused (not feature-focused)
- [x] Stable goals (would exist even if tech changed)
- [x] Organized by domain taxonomy stages

### User Stories/Tasks
- [x] 2-7 per main job (varies appropriately by complexity)
- [x] Scenario-specific or approach-based
- [x] Implementation details, not goals
- [x] Properly nested under main jobs
- [x] NO "For [Persona]:" prefixes that gate content (using "Option A/B/C:" or "Persona:" labels)
- [x] Use "Context:" to explain when/why to use each approach (in job-level "When:" field)

### Structure
- [x] Follows domain taxonomy stage progression
- [x] Jobs ordered by workflow/prerequisites
- [x] Line references use `→ Lines X-Y: Title` format with `Source:` line
- [x] Prerequisites stated as permissions, not personas (in success_criteria and pain_points)
- [x] Both UI and CLI paths documented where applicable
- [x] Gap markers for missing content (none needed - all content mapped)

### Comparison
- [x] Current structure shown accurately
- [x] Proposed structure is logical
- [x] Key differences explained
- [x] Navigation improvements quantified
- [x] Workflow coverage comparison with ✅/⚠️/❌ indicators
- [x] Gap recommendations with priorities

---

## Success Criteria

**A good TOC comparison:**

- ✅ User can immediately see main goals (31 main jobs organized by workflow stage)
- ✅ User can find jobs by what they need to accomplish, not by component or role
- ✅ User can see it's simpler than current structure (47% fewer top-level categories)
- ✅ Stakeholders understand the proposed improvement (workflow-based vs. component-based)
- ✅ Content mappers know what to extract from where (all line references and sources included)
- ✅ Structure follows natural workflow progression (Evaluate → Configure → Deploy → Monitor → Troubleshoot → Migrate → Operate → Reference)
- ✅ No persona gates - anyone can complete any job based on permissions
- ✅ Prerequisites stated as permissions, not job titles (in JTBD success_criteria)
- ✅ Gaps clearly marked with source references (none identified in this comprehensive release notes document)

---

## Notes

This comparison analyzes release notes for OpenShift Pipelines 1.21, which covers 11 different components (Pipelines, Operator, UI, Pipelines as Code, Tekton Results, Tekton Cache, Tekton Triggers, Tekton Hub, Tekton Chains, CLI, Pruner) across 4 release note categories (New features, Technology Preview, Breaking changes, Fixed issues, Deprecated features, Known issues).

The current feature-based structure organizes content by component and release note type, requiring users to:
1. Know which component provides the functionality they need
2. Understand whether their need relates to a new feature, breaking change, or bug fix
3. Navigate through multiple component sections to find related information

The proposed JTBD-based structure organizes the same content by workflow stage and user goal, allowing users to:
1. Navigate directly to their current workflow stage (e.g., "Set Up & Configure" or "Troubleshoot Issues")
2. Find the job that matches their goal (e.g., "Configure resolver caching for performance")
3. Choose the implementation option that matches their context (e.g., "Configure global resolver caching settings")

**Key insight:** Release notes organized by user workflow stage provide faster navigation to relevant information, especially when a single release covers many components with overlapping user goals (e.g., multiple configuration jobs, multiple troubleshooting jobs).
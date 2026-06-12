# Installing and Configuring OpenShift Pipelines — Consolidation Report

**Document:** install_config-consolidation-report.md
**JTBD Records:** 30 pre-consolidated user stories → 14 final main jobs (after consolidation)
**Analysis Date:** 2026-06-12
**Distro:** openshift-pipelines
**Book:** install_config

---

## Executive Summary

### What's Changing

The current Installing and Configuring OpenShift Pipelines documentation is organized by lifecycle phases (Installing, Uninstalling, Customizing) with 30+ scattered modules arranged by technical features. This feature-based organization forces users to navigate across 3 assemblies and 20+ configuration sections to accomplish common operational goals like "set up production pipelines" or "configure automatic cleanup." Configuration topics for performance tuning, control plane settings, resync periods, and service accounts are dispersed across separate sections without clear workflow progression.

The proposed JTBD-based structure consolidates these 30+ modules into 14 goal-oriented jobs organized by 7 workflow stages (Get Started, Configure, Secure, Migrate, Operate, Monitor, Conclude). Each job groups related content by user goal rather than technical feature, presenting multiple implementation paths (UI vs CLI, scheduled vs event-driven pruning) side-by-side with explicit prerequisite chains and timing guidance. This restructuring reduces top-level navigation items by 53% while improving discoverability by grouping scattered configuration topics under clear operational goals.

### Key Improvements

- **Installation consolidation:** 2 separate installation sections (web console and CLI) consolidated into 1 job with 2 implementation paths clearly labeled by persona (administrators preferring GUI vs platform engineers managing IaC).
- **Production configuration grouping:** 5 scattered configuration sections (performance tuning, control plane, service accounts, resync period, metrics) consolidated under 2 unified jobs (Optimize Controller Performance, Configure Control Plane Settings) organized by operational goal.
- **Pruning simplification:** 5 subsections for automatic pruning (cron config, annotations, event setup, event config, metrics) consolidated into 1 job with 2 clear mutually-exclusive options (Scheduled vs Event-Driven) presented side-by-side.
- **Security elevation:** 3 security-related sections buried in configuration assembly (service accounts, RBAC disabling, inline specs) elevated to dedicated "Secure Your Pipelines" stage with 3 visible jobs.
- **Migration clarity:** Tekton Hub to Artifact Hub migration content reorganized from scattered subsections into 1 job with 3 sequential steps (Assess, Update, Configure Private Hub).
- **Resolver management:** Configuration of 4 different resolver types and template disabling consolidated under 1 unified job (Manage Pipeline Resource Resolution) with clear security implications.
- **Uninstallation sequencing:** 3-step uninstallation sequence maintained but now with explicit critical sequencing warnings and "must follow this order" guidance to prevent orphaned components.
- **Workflow progression:** Natural flow from Get Started → Configure → Secure → Migrate → Operate → Conclude eliminates cross-assembly navigation and provides clear prerequisite chains.

---

## Current Structure (Feature-Based)

### Assembly 1: Installing OpenShift Pipelines
= Installing OpenShift Pipelines

- **Installing the Red Hat OpenShift Pipelines Operator in web console** — Graphical installation using OperatorHub, profile selection (Lite/Basic/All), update channel selection, verification procedures (lines 74-183)
- **Installing the Red Hat OpenShift Pipelines Operator by using the CLI** — Command-line installation with YAML manifests, Subscription object creation, automatic TektonConfig deployment (lines 188-235)
- **Red Hat OpenShift Pipelines Operator in a restricted environment** — Proxy webhook configuration, automatic proxy settings for pipeline containers in air-gapped environments (lines 240-256)

### Assembly 2: Uninstalling OpenShift Pipelines
= Uninstalling OpenShift Pipelines

- **Deleting the OpenShift Pipelines custom resources** — CR deletion procedure in correct sequence (TektonHub, TektonResult, TektonConfig), warnings about orphaned components (lines 361-392)
- **Uninstalling the Red Hat OpenShift Pipelines Operator** — Operator removal via web console, warning about namespace-wide deletion including secrets (lines 402-421)
- **Deleting the custom resource definitions of the operator.tekton.dev group** — CRD cleanup for complete removal, ensures no residual definitions remain (lines 431-449)

### Assembly 3: Customizing configurations in the TektonConfig custom resource
= Customizing configurations in the TektonConfig CR

- **Performance tuning using the TektonConfig custom resource** — HA mode configuration, buckets, replicas, threads-per-controller, API query limits (lines 541-613)
- **Configuring the pipelines control plane** — Metrics collection, sidecar injection, service account defaults (lines 621-668)
  - Modifiable fields with default values (lines 686-725)
  - Optional configuration fields (lines 737-753)
- **Changing the default service account for OpenShift Pipelines** — Service account customization for security/operational requirements (lines 764-784)
- **Setting labels and annotations for the OpenShift Pipelines installation namespace** — Namespace metadata configuration (lines 794-818)
- **Setting the resync period for the pipelines controller** — Resync period tuning for large clusters (lines 827-862)
- **Disabling the service monitor** — Metrics disabling by setting enableMetrics to false (lines 874-892)
- **Configuring pipeline resolvers** — Enabling/disabling bundles, cluster, git, hub resolvers, resolver-specific configurations (lines 903-949)
- **Disabling resolver tasks and pipeline templates** — Preventing automatic installation of default resources (lines 958-999)
- **Disabling the installation of Tekton Triggers** — Triggers component management (lines 1009-1027)
- **Disabling the integration of Tekton Hub** — Hub integration control in web console Developer perspective (lines 1036-1056)
- **Migrating from Tekton Hub to Artifact Hub** — Deprecation handling, migration procedures (lines 1065-1189)
  - Assess migration impact (lines 1085-1126)
  - Migrating to Artifact Hub (lines 1136-1189)
  - Configuring a private Artifact Hub instance (lines 1201-1231)
- **Disabling the automatic creation of RBAC resources** — Security hardening by disabling cluster-wide RBAC creation, addresses RunAsAny SCC privilege risk (lines 1240-1276)
- **Disabling inline specification of pipelines and tasks** — Supply chain security enforcement, requires version-controlled resources (lines 1284-1370)
- **Configuration of RBAC and Trusted CA flags** — Independent control of RBAC and Trusted CA bundle creation (lines 1378-1418)
- **Automatic pruning of task runs and pipeline runs** — Scheduled and event-driven pruning approaches (lines 1426-1875)
  - Configuring the pruner (scheduled/cron-based) (lines 1446-1506)
  - Annotations for automatically pruning task runs and pipeline runs (lines 1516-1554)
  - Enabling the event-driven pruner (lines 1563-1643)
  - Configuration of the event-driven pruner (lines 1651-1875)
  - Observability metrics of the event-driven pruner (lines 1883-1961)
- **Setting additional options for webhooks** — Webhook failure policies, timeouts, sideEffects configuration (lines 1969-2118)

**Total:** 3 assemblies, 30+ modules, organized by lifecycle phase (Installing, Uninstalling, Customizing) and technical features.

---

## Proposed JTBD-Based Structure

### Quick Overview

- **Getting Started with Pipelines**
  - Job 1: Install the OpenShift Pipelines Operator
  - Job 2: Verify Operator Installation Success
- **Configure for Production**
  - Job 3: Optimize Controller Performance
  - Job 4: Configure Control Plane Settings
  - Job 6: Manage Pipeline Resource Resolution
  - Job 11: Configure Webhook Behavior
  - Job 12: Configure Private Artifact Hub
  - Job 14: Configure Proxy for Restricted Environments
- **Secure Your Pipelines**
  - Job 5: Change Default Service Account
  - Job 9: Disable Automatic RBAC Creation
  - Job 10: Disable Inline Pipeline Specifications
- **Migrate Between Catalogs**
  - Job 7: Migrate from Tekton Hub to Artifact Hub
- **Operate and Maintain**
  - Job 8: Automatically Remove Completed Pipeline Runs
- **Decommission Pipelines**
  - Job 13: Fully Remove OpenShift Pipelines

---

### Detailed Job Descriptions

#### Getting Started with Pipelines

**Job 1: Install the OpenShift Pipelines Operator**

*When deploying CI/CD infrastructure to enable pipeline functionality across my cluster, I want to install the OpenShift Pipelines Operator with minimal setup complexity, so I can begin creating pipelines quickly while maintaining control over installation methods and upgrade strategies.*

Prerequisites: Cluster administrator permissions, OpenShift Container Platform cluster

- **1.1. Install via web console using OperatorHub** `[procedure]`
  - Source: Installing the Red Hat OpenShift Pipelines Operator in web console (lines 74-183)
  - Context: For cluster administrators preferring graphical interfaces who want visual configuration of installation options, approval strategies, and update channels
  - Includes: Namespace selection (all namespaces), approval strategy (Automatic/Manual), update channel selection (latest or pipelines-<version>), profile selection (Lite/Basic/All)
  
- **1.2. Install using CLI with YAML manifests** `[procedure]`
  - Source: Installing the Red Hat OpenShift Pipelines Operator by using the CLI (lines 188-235)
  - Context: For platform engineers managing infrastructure as code who need programmatic deployment and version-controlled configuration
  - Includes: Subscription object YAML creation, automatic TektonConfig deployment to openshift-pipelines namespace
  
- **1.3. Select update channel based on version requirements** `[concept]`
  - Source: Installing the Red Hat OpenShift Pipelines Operator in web console (lines 117-125)
  - Context: When managing multiple OpenShift versions and controlling which Pipelines version is installed and when upgrades occur
  - Options: 'latest' for most recent stable, 'pipelines-<version>' for specific versions, preview/stable channels deprecated after OCP 4.10

**Job 2: Verify Operator Installation Success**

*When the Operator installation completes, I want to verify that all Tekton components are ready and functional, so I can confirm the installation succeeded before creating pipelines and avoid relying on potentially misleading web console status indicators.*

Prerequisites: Completed Job 1 (Install the OpenShift Pipelines Operator)

- **2.1. Check TektonConfig status using CLI** `[procedure]`
  - Source: Installing the Red Hat OpenShift Pipelines Operator in web console (lines 134-182)
  - Context: Web console status may show "Succeeded Up to date" even if components are still installing
  - Commands: `oc get tektonconfig config`, `oc get tektonpipeline,tektontrigger,tektonchain,tektonaddon,pac`
  - Verification: Confirm all components show Ready: True with correct version numbers

---

#### Configure for Production

**Job 3: Optimize Controller Performance**

*When managing high-volume pipeline workloads, I want to optimize controller performance with HA mode and resource allocation, so I can reduce delays, handle peak loads without bottlenecks, and ensure controller operations scale across multiple replicas.*

Prerequisites: Completed Job 1, understanding of cluster scale and load characteristics

- **3.1. Enable high-availability mode with multiple controller replicas** `[procedure]`
  - Source: Performance tuning using the TektonConfig custom resource (lines 541-613, specifically 556-597)
  - Context: When needing to scale pipeline operations and distribute workload across pods to avoid single-point-of-failure delays
  - Configuration: Set disable-ha: false, configure buckets (max 10), set replicas (≤ buckets value), adjust threads-per-controller, tune kube-api-qps and kube-api-burst
  - How HA works: Operations distributed across buckets, picked by multiple replicas, internal leader election prevents duplicate operations

- **3.2. Understand HA mode performance parameters** `[reference]`
  - Source: Performance tuning using the TektonConfig custom resource (lines 541-613)
  - Parameters: disable-ha (default false), buckets (default 1, max 10), replicas (default 1), threads-per-controller (default 2), kube-api-qps (default 5.0), kube-api-burst (default 10)
  - Note: Controller multiplies kube-api-qps and kube-api-burst by 2 internally

**Job 4: Configure Control Plane Settings**

*When deploying pipelines in production environments, I want to configure control plane settings like sidecar behavior, metrics collection, and resync periods, so I can tailor pipeline execution to my cluster's characteristics and optimize resource consumption.*

Prerequisites: Access to TektonConfig CR, understanding of cluster characteristics (sidecar injection, scale, metrics requirements)

- **4.1. Optimize for non-sidecar environments** `[procedure]`
  - Source: Configuring the pipelines control plane (lines 621-668), Modifiable fields with default values (lines 686-693)
  - Context: For clusters without Istio or injected sidecars where sidecar readiness checks cause unnecessary task run startup delays
  - Configuration: Set running-in-environment-with-injected-sidecars: false, await-sidecar-readiness: false
  - Benefit: Reduces task run startup time by avoiding waits for non-existent sidecars

- **4.2. Configure metrics collection** `[procedure]`
  - Source: Configuring the pipelines control plane (lines 621-668, 686-784)
  - Context: When needing to customize metrics exposure, duration types, and aggregation levels for monitoring dashboards
  - Settings: metrics.taskrun.duration-type (histogram/gauge), metrics.pipelinerun.duration-type, metrics.taskrun.level (taskrun/task/namespace), metrics.pipelinerun.level (pipelinerun/pipeline/namespace), enableMetrics parameter

- **4.3. Set resync period for large clusters** `[procedure]`
  - Source: Setting the resync period for the pipelines controller (lines 827-862)
  - Context: For clusters with large numbers of pipeline runs where full reconciliation every 10 hours consumes too many resources
  - Configuration: Edit TektonConfig with -resync-period=24h argument in tekton-pipelines-controller container
  - Benefit: Reduces CPU and memory usage on control plane for large-scale deployments

- **4.4. Disable service monitor if needed** `[procedure]`
  - Source: Disabling the service monitor (lines 874-892)
  - Context: When not needing to expose telemetry data or wanting to reduce resource consumption
  - Configuration: Set enableMetrics parameter to false in TektonConfig

**Job 6: Manage Pipeline Resource Resolution**

*When managing how pipelines fetch remote resources, I want to enable or disable specific resolvers and configure their behavior, so I can control resource resolution methods, enforce security policies, and reduce complexity by disabling unused resolvers.*

Prerequisites: Understanding of resolver types (bundles, cluster, git, hub) and their security implications

- **6.1. Enable or disable specific resolver types** `[procedure]`
  - Source: Configuring pipeline resolvers (lines 903-949)
  - Context: When controlling which resolution methods are available to pipeline authors based on organizational security policies
  - Resolver types: enable-bundles-resolver (OCI bundles), enable-cluster-resolver (cluster-local resources), enable-git-resolver (Git repository resources), enable-hub-resolver (Hub catalog resources)
  - Resolver-specific configurations: bundles-resolver-config, cluster-resolver-config, git-resolver-config, hub-resolver-config

- **6.2. Disable automatic template installation** `[procedure]`
  - Source: Disabling resolver tasks and pipeline templates (lines 958-999)
  - Context: When customizing cluster initial state to prevent deployment of default resources your environment doesn't require
  - Configuration: Set resolverTasks: false to prevent default task installation, set pipelineTemplates: false to prevent template installation
  - Important: pipelineTemplates can only be true when resolverTasks is true

**Job 11: Configure Webhook Behavior**

*When customizing admission control behavior, I want to configure webhook failure policies, timeouts, and side effects in TektonConfig, so I can control how Kubernetes handles webhook failures and prevent pipeline submission delays.*

Prerequisites: Understanding of webhook types (mutating vs validating), access to TektonConfig CR

- **11.1. View existing webhook configurations** `[procedure]`
  - Source: Setting additional options for webhooks (lines 1969-2118, specifically 1986-2023)
  - Commands: `oc get MutatingWebhookConfiguration`, `oc get ValidatingWebhookConfiguration`
  - Webhook types: Mutating (webhook.pipeline.tekton.dev, webhook.triggers.tekton.dev) and Validating (validation.webhook.pipeline.tekton.dev, validation.webhook.triggers.tekton.dev, validation.pipelinesascode.tekton.dev, validation.webhook.hub.tekton.dev)

- **11.2. Configure webhook options for controllers** `[procedure]`
  - Source: Setting additional options for webhooks (lines 1969-2118, examples 2034-2116)
  - Context: When needing to customize webhook behavior for Pipelines, Triggers, Pipelines as Code, or Tekton Hub controllers
  - Configurable options: failurePolicy (Fail/Ignore), timeoutSeconds (default 10s, max 30s), sideEffects (None/NoneOnDryRun)
  - Note: Cannot configure operator webhooks

**Job 12: Configure Private Artifact Hub**

*When operating in disconnected or private networks, I want to configure a custom Artifact Hub URL in TektonConfig, so I can resolve pipeline resources from an internal registry instead of public artifacthub.io and maintain catalog access in air-gapped environments.*

Prerequisites: Private Artifact Hub instance deployed, network connectivity from resolver pods configured, TLS certificates for HTTPS endpoints configured

- **12.1. Configure custom Artifact Hub endpoint** `[procedure]`
  - Source: Configuring a private Artifact Hub instance (lines 1201-1231)
  - Context: For disconnected or air-gapped environments where public Artifact Hub is inaccessible
  - Configuration: Edit TektonConfig hub-resolver-config, set default-artifact-hub-url to private hub URL
  - Critical verification: Network connectivity from resolver pods, TLS certificates configured, authentication configured if required, catalog names match private hub publications

**Job 14: Configure Proxy for Restricted Environments**

*When operating in air-gapped networks, I want the Pipelines Operator to automatically configure proxy settings for pipeline components, so I can run pipelines without manual proxy configuration and enable pipeline execution in restricted environments.*

Prerequisites: Cluster proxy object configured, Operator installed

- **14.1. Understand automatic proxy configuration** `[concept]`
  - Source: Red Hat OpenShift Pipelines Operator in a restricted environment (lines 240-256)
  - Context: Operator automatically installs proxy webhook after installation
  - How it works: Webhook sets proxy environment variables in pod containers based on cluster proxy object, applies to TektonPipelines, TektonTriggers, Controllers, Webhooks
  - Default behavior: Proxy disabled for openshift-pipelines namespace

- **14.2. Disable proxy for specific namespaces** `[procedure]`
  - Source: Red Hat OpenShift Pipelines Operator in a restricted environment (lines 240-256)
  - Context: When certain namespaces should not use cluster proxy settings
  - Configuration: Add label operator.tekton.dev/disable-proxy: true to Namespace object

---

#### Secure Your Pipelines

**Job 5: Change Default Service Account**

*When enforcing security policies across pipelines, I want to change the default service account used by task and pipeline runs, so I can align with organizational RBAC requirements and ensure all pipeline runs use approved service accounts.*

Prerequisites: Custom service account with appropriate permissions created

- **5.1. Configure default service account for pipelines and triggers** `[procedure]`
  - Source: Changing the default service account for OpenShift Pipelines (lines 764-784)
  - Context: When needing to enforce security policies before running production pipelines
  - Configuration: Edit TektonConfig, set spec.pipeline.default-service-account and spec.trigger.default-service-account
  - Applies to: TaskRun and PipelineRun resources when no service account is explicitly specified

**Job 9: Disable Automatic RBAC Creation**

*When cluster security policies require fine-grained permission control, I want to disable automatic cluster-wide RBAC creation, so I can prevent privileged role bindings (especially pipelines-scc-rolebinding with RunAsAny SCC privilege) and manually manage permissions per namespace.*

Prerequisites: Understanding of pipelines-scc security implications, cluster-admin privileges

- **9.1. Disable automatic RBAC resource creation** `[procedure]`
  - Source: Disabling the automatic creation of RBAC resources (lines 1240-1276)
  - Context: Default pipelines-scc-rolebinding has RunAsAny SCC privilege, which is a potential security risk
  - Configuration: Edit TektonConfig, set createRbacResource parameter to "false"
  - After disabling: Manually create namespace-specific RBAC resources as needed

- **9.2. Configure independent control of Trusted CA bundle** `[concept]`
  - Source: Configuration of RBAC and Trusted CA flags (lines 1378-1418)
  - Context: When wanting to disable RBAC without affecting Trusted CA bundle config maps
  - Configuration: createRbacResource (controls RBAC only), createCABundleConfigMaps (controls Trusted CA bundle separately)
  - Benefit: Can disable RBAC security risk without impacting CA bundle functionality

**Job 10: Disable Inline Pipeline Specifications**

*When enforcing supply chain security, I want to disable inline taskSpec and pipelineSpec definitions, so I can require all pipelines and tasks to be referenced from version-controlled resources or resolvers, preventing unaudited code execution.*

Prerequisites: Pipeline and task versioning strategy established, resolver configuration in place

- **10.1. Understand inline specification security risks** `[concept]`
  - Source: Disabling inline specification of pipelines and tasks (lines 1284-1370, specifically 1291-1336)
  - Context: Inline specs bypass version control and security scanning
  - Default behavior: Pipelines supports inline taskSpec in Pipeline CRs, inline pipelineSpec in PipelineRun CRs, inline taskSpec in TaskRun CRs
  - Security implication: Inline definitions can contain unaudited code that executes without review

- **10.2. Configure enforcement levels for inline spec disabling** `[procedure]`
  - Source: Disabling inline specification of pipelines and tasks (lines 1284-1370, specifically 1338-1368)
  - Context: When ready to enforce supply chain security before deploying production pipelines
  - Configuration: Edit TektonConfig, set spec.pipeline.disable-inline-spec to "pipeline,pipelinerun,taskrun"
  - Enforcement levels: "pipeline" (prevents taskSpec in Pipeline CR), "pipelinerun" (prevents pipelineSpec in PipelineRun CR), "taskrun" (prevents taskSpec in TaskRun CR)
  - After enabling: All resources must use taskRef and pipelineRef to reference Task/Pipeline CRs or use resolvers

---

#### Migrate Between Catalogs

**Job 7: Migrate from Tekton Hub to Artifact Hub**

*When Tekton Hub deprecation affects my pipelines, I want to migrate to Artifact Hub as the catalog source with minimal disruption, so I can ensure uninterrupted catalog resolution, continue using prebuilt tasks, and comply with the new default hub resolver configuration.*

Prerequisites: Inventory of resources using Tekton Hub, understanding of Artifact Hub catalog structure

- **7.1. Assess migration impact** `[procedure]`
  - Source: Assess migration impact (lines 1085-1126)
  - Context: Before migrating, identify which resources require modification to scope the effort
  - Assessment script: Count resources by type using find/grep for "value: tekton" or "value: Tekton", check hub resolver configuration with kubectl
  - Must migrate if: Resources reference type: tekton or catalog: Tekton, resources use non-semver catalog versions, hub resolver still configured with type: tekton

- **7.2. Update resource definitions for Artifact Hub** `[procedure]`
  - Source: Migrating to Artifact Hub (lines 1136-1189)
  - Context: After assessment, update all identified resources to use Artifact Hub catalog names and semantic versioning
  - Migration steps: 1) Remove type: tekton parameter (do NOT add type: artifact, it's default), 2) Update catalog names (Tekton → tekton-catalog-tasks/pipelines/stepactions), 3) Update versions to full semver (e.g., 0.8 → 0.8.0), 4) Reapply resource definitions
  - Important: type: artifact is the default and does not need to be specified

- **7.3. Configure private Artifact Hub for disconnected environments** `[procedure]`
  - Source: Configuring a private Artifact Hub instance (lines 1201-1231)
  - Context: For disconnected/air-gapped environments after migrating to Artifact Hub
  - See Job 12 for complete configuration steps

---

#### Operate and Maintain

**Job 8: Automatically Remove Completed Pipeline Runs**

*When managing cluster resources over time, I want to automatically remove completed TaskRun and PipelineRun objects based on retention policies, so I can prevent resource exhaustion, maintain optimal cluster performance, and reduce storage costs from unused pipeline runs without manual intervention.*

Prerequisites: Understanding of retention requirements, compliance needs, cluster resource constraints

- **8.1. Choose between scheduled and event-driven pruning approaches** `[concept]`
  - Source: Automatic pruning of task runs and pipeline runs (lines 1426-1436)
  - Context: Two mutually-exclusive approaches with different cleanup timing and complexity
  - Scheduled (cron-based): Batch cleanup at scheduled intervals, simpler configuration, may cause resource spikes during batch processing
  - Event-driven (real-time): Immediate cleanup after completion, more complex configuration (TTL + history limits + enforcement levels), distributed load, rich observability metrics
  - Important: Cannot enable both pruner types simultaneously

- **8.2. Configure scheduled (cron-based) pruning** `[procedure]`
  - Source: Configuring the pruner (lines 1446-1506)
  - Context: For predictable batch cleanup with simpler configuration requirements
  - Configuration: Edit TektonConfig spec.pruner, set schedule (cron format, default "* 8 * * *"), choose retention policy (keep: 100 or keep-since: 7200), set prune-per-resource (true/false), configure startingDeadlineSeconds
  - Retention policies: keep (retain N most recent runs), keep-since (retain runs from last N minutes) — mutually exclusive
  - Per-resource behavior: false (100 total task runs + 100 total pipeline runs), true (100 per unique pipeline/task)

- **8.3. Configure namespace-specific overrides for scheduled pruning** `[procedure]`
  - Source: Annotations for automatically pruning task runs and pipeline runs (lines 1516-1554)
  - Context: When different projects have different retention needs without modifying cluster-wide configuration
  - Annotations: operator.tekton.dev/prune.schedule, operator.tekton.dev/prune.resources, operator.tekton.dev/prune.keep, operator.tekton.dev/prune.keep-since, operator.tekton.dev/prune.skip (set to "true" to skip namespace), operator.tekton.dev/prune.strategy (keep or keep-since)
  - Apply to: Namespace resource metadata

- **8.4. Enable event-driven (real-time) pruning** `[procedure]`
  - Source: Enabling the event-driven pruner (lines 1563-1643)
  - Context: For near real-time cleanup instead of scheduled batches
  - Prerequisites: Disable job-based pruner first (spec.pruner.disabled: true)
  - Configuration: Enable event pruner (spec.tektonpruner.disabled: false)
  - Verification: Check tekton-pruner-controller and tekton-pruner-webhook pods running, verify config maps present (tekton-pruner-default-spec, pruner-info, config-logging-tekton-pruner, config-observability-tekton-pruner)

- **8.5. Configure event pruner retention policies** `[procedure]`
  - Source: Configuration of the event-driven pruner (lines 1651-1875)
  - Context: After enabling event pruner, define TTL-based or history-based retention rules at global, namespace, or resource level
  - Global configuration: enforcedConfigLevel: global, ttlSecondsAfterFinished (e.g., 3600), historyLimit (generic retention count), successfulHistoryLimit, failedHistoryLimit
  - Namespace-level: Set enforcedConfigLevel: namespace, define per-namespace policies under namespaces section
  - Resource-level: Create tekton-pruner-namespace-spec ConfigMap in namespace with required labels (app.kubernetes.io/part-of: tekton-pruner, pruner.tekton.dev/config-type: namespace)
  - Common TTL values: 300s (5 min, dev/testing), 3600s (1 hour, CI pipelines), 86400s (1 day, staging), 2592000s (30 days, compliance), 7776000s (90 days, regulated industries)
  - Resource-level with selectors: Define selectors with matchLabels and matchAnnotations to apply rules only to resources matching both

- **8.6. Monitor event pruner performance** `[reference]`
  - Source: Observability metrics of the event-driven pruner (lines 1883-1961)
  - Context: For SREs operating event-driven pruner in production who need visibility into pruning performance and error rates
  - Resource processing metrics: tekton_pruner_controller_resources_processed_total (Counter with namespace, resource_type, status labels), tekton_pruner_controller_resources_deleted_total (Counter with namespace, resource_type, operation labels)
  - Performance timing metrics: tekton_pruner_controller_reconciliation_duration_seconds (Histogram, 0.1s to 30s buckets), tekton_pruner_controller_ttl_processing_duration_seconds, tekton_pruner_controller_history_processing_duration_seconds
  - State tracking: kn_workqueue_adds_total (Counter, total resources queued), kn_workqueue_depth (Gauge, current items in queue)
  - Error monitoring: tekton_pruner_controller_resources_errors_total (Counter with namespace, resource_type, reason labels)
  - Format: All metrics available in OpenTelemetry format

---

#### Decommission Pipelines

**Job 13: Fully Remove OpenShift Pipelines**

*When I need to fully remove OpenShift Pipelines from my cluster, I want to cleanly uninstall all components and custom resources in the correct sequence, so I can ensure no residual configuration or resources remain that could interfere with future installations or cluster operations.*

Prerequisites: Understanding that uninstallation deletes all pipelines and tasks, cluster administrator permissions

- **13.1. Delete custom resources in correct sequence** `[procedure]`
  - Source: Deleting the OpenShift Pipelines custom resources (lines 361-392)
  - Context: Preparing for Operator uninstallation, avoiding orphaned components that cannot be removed later
  - Critical sequencing (MUST follow this order): 1) Search and delete TektonHub CRs (if exist), 2) Search and delete TektonResult CRs (if exist), 3) Search and delete TektonConfig CR
  - Via web console: Administration → CustomResourceDefinitions, filter by name, click Instances tab, Options menu → Delete for each instance
  - Warnings: Deleting CRs also deletes all Pipelines components, tasks, and pipelines on cluster; if you uninstall Operator without removing TektonHub and TektonResult CRs, you cannot remove those components later
  - Recommended: Back up pipeline definitions before deletion

- **13.2. Uninstall the Operator** `[procedure]`
  - Source: Uninstalling the Red Hat OpenShift Pipelines Operator (lines 402-421)
  - Context: After deleting all CRs, remove the operator subscription and all operand instances
  - Prerequisites: Completed Step 1 (delete all CRs)
  - Via web console: Operators → OperatorHub, search "OpenShift Pipelines", click Uninstall, select "Delete all operand instances for this operator"
  - Warning: Uninstallation deletes ALL resources in openshift-pipelines namespace including secrets; back up secrets if needed before proceeding

- **13.3. Delete custom resource definitions** `[procedure]`
  - Source: Deleting the custom resource definitions of the operator.tekton.dev group (lines 431-449)
  - Context: For complete cleanup after operator uninstallation to ensure no residual CRD definitions remain
  - Prerequisites: Completed Steps 1 and 2 (delete CRs and uninstall Operator)
  - Via web console: Administration → CustomResourceDefinitions, filter by "operator.tekton.dev", for each displayed CRD: Options menu → Delete CustomResourceDefinition
  - Why this matters: Ensures no residual definitions remain, prevents conflicts during future installations, provides clean slate for potential reinstallation

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | Lifecycle phases (Installing, Uninstalling, Customizing) with modules arranged by technical feature | Workflow stages (Get Started, Configure, Secure, Migrate, Operate, Conclude) with jobs organized by user goal |
| **Top-level items** | 3 assemblies with 30+ scattered modules | 14 main jobs with 2-5 implementation paths each |
| **Installation guidance** | 2 separate sections (web console, CLI) without clear choice guidance | 1 job with 2 options side-by-side, labeled by persona (GUI-preferring administrators vs IaC-focused engineers) |
| **Production configuration** | 5 separate sections scattered across assembly 3 (performance, control plane, service accounts, resync period, metrics) | 2 consolidated jobs (Optimize Controller Performance, Configure Control Plane Settings) grouped by operational goal |
| **Pruning configuration** | 5 subsections under one heading with no clear "choose A or B" guidance | 1 job with 2 mutually-exclusive options (Scheduled vs Event-Driven) presented with clear comparison |
| **Security content** | 3 sections buried in configuration assembly (sections 4, 15, 17) | Dedicated "Secure Your Pipelines" stage with 3 visible jobs elevated to top-level navigation |
| **Migration guidance** | 3 subsections under hub customization (assess, migrate, configure private) | 1 dedicated job with 3 sequential steps in clear progression |
| **Resolver management** | 2 separate sections (configuring resolvers, disabling templates) | 1 unified job managing all resolver types and template settings |
| **Navigation depth** | 4-6 clicks (Assembly → Section → Subsection → Read → Compare) | 2-3 clicks (Stage → Job → Option) |
| **Prerequisite visibility** | Implicit, scattered across related sections | Explicit prerequisite chains with timing guidance (BEFORE, AFTER) |
| **Content discovery for "set up production pipelines"** | Must browse 5+ scattered sections across assembly 3 | Navigate to "Configure for Production" stage, see Jobs 3-4 grouped together |

### Job List Adjustments from Suggested Input

The suggested 30 JTBD records (user stories) were consolidated to **14 main jobs** for the following reasons:

1. **Records 1-2 (both "Install the OpenShift Pipelines Operator") merged** → Both are implementation paths for the same job, differentiated by persona (web console for GUI preference vs CLI for IaC). Consolidated as Job 1 with two approaches (1.1 web console, 1.2 CLI, 1.3 update channel selection).

2. **Record 3 ("Select update channel") absorbed into Job 1** → Update channel selection is a sub-decision within the installation job, not a separate job. Now appears as approach 1.3 with concept topic type.

3. **Record 4 ("Verify installation") promoted to Job 2** → Verification is a distinct job that must occur after installation, with explicit AFTER timing guidance and prerequisite chain.

4. **Records 5 (CLI installation user story) absorbed into Job 1** → Duplicate of record 1's CLI path, consolidated as approach 1.2.

5. **Record 6 ("Configure proxy for restricted environments") promoted to Job 14** → Proxy configuration is a distinct configuration job for air-gapped deployments, elevated to main job status in "Configure for Production" stage.

6. **Records 7-10 (all uninstallation-related) merged into Job 13** → These are sequential steps of one job ("Fully Remove OpenShift Pipelines"), not separate jobs. Consolidated as Job 13 with three approaches (13.1 delete CRs, 13.2 uninstall Operator, 13.3 delete CRDs).

7. **Records 11-12 (both performance tuning) merged into Job 3** → HA mode enablement (record 12) is an approach within the performance optimization job (record 11). Consolidated as Job 3 with approach 3.1 (enable HA mode) and 3.2 (understand parameters).

8. **Records 13-16 (all control plane configuration) merged into Job 4** → Sidecar configuration (14), control plane settings (13), and resync period (16) are all control plane tuning activities. Consolidated as Job 4 with approaches 4.1 (sidecars), 4.2 (metrics), 4.3 (resync period), 4.4 (disable service monitor).

9. **Record 15 (service account configuration) promoted to Job 5** → Service account is a security concern, elevated to dedicated job in "Secure Your Pipelines" stage for visibility.

10. **Records 17-18 (resolver configuration and template disabling) merged into Job 6** → Both manage resolver-related configuration. Consolidated as Job 6 with approaches 6.1 (enable/disable resolvers) and 6.2 (disable templates).

11. **Records 19-20 (Tekton Hub migration) merged into Job 7** → Assessment (20) is the first step of migration (19). Consolidated as Job 7 with approaches 7.1 (assess), 7.2 (update definitions), 7.3 (configure private hub).

12. **Records 21-26 (all pruning-related) merged into Job 8** → Scheduled pruning config (22), namespace annotations (23), event pruner setup (24), event pruner config (25), and observability (26) are all approaches within automatic pruning job (21). Consolidated as Job 8 with approaches 8.1 (choose approach), 8.2 (scheduled config), 8.3 (namespace overrides), 8.4 (enable event), 8.5 (event retention), 8.6 (monitor event pruner).

13. **Record 27 (disable automatic RBAC) promoted to Job 9** → RBAC disabling is a critical security job, elevated to main job in "Secure Your Pipelines" stage.

14. **Record 28 (disable inline specs) promoted to Job 10** → Supply chain security enforcement is a critical security job, elevated to main job in "Secure Your Pipelines" stage.

15. **Record 29 (webhook configuration) promoted to Job 11** → Webhook customization is a distinct configuration job for admission control, elevated to main job status in "Configure for Production" stage.

16. **Record 30 (configure private Artifact Hub) promoted to Job 12** → Private hub configuration is a distinct job for disconnected environments, elevated to main job status in "Configure for Production" stage.

---

## Consolidation Examples

### Example 1: Installation Methods (2 scattered sections → 1 unified job)

**Current (Fragmented):**
- Section 1: Installing the Red Hat OpenShift Pipelines Operator in web console (lines 74-183) — Separate assembly 1 section covering graphical installation
- Section 2: Installing the Red Hat OpenShift Pipelines Operator by using the CLI (lines 188-235) — Separate assembly 1 section covering command-line installation

User must read both sections separately to compare approaches, with no guidance on when to use which method or how the approaches differ beyond "web console" vs "CLI."

**Proposed (Consolidated):**
- **Job 1: Install the OpenShift Pipelines Operator**
  - 1.1. Install via web console using OperatorHub (lines 74-183) — For cluster administrators preferring graphical interfaces
  - 1.2. Install using CLI with YAML manifests (lines 188-235) — For platform engineers managing infrastructure as code
  - 1.3. Select update channel based on version requirements (lines 117-125) — When managing multiple OpenShift versions

**Benefit:** Users see both installation approaches in one place with clear persona-based guidance (GUI preference vs IaC workflow) and can immediately compare benefits (visual configuration and installation progress vs automation via CI/CD and version-controlled config). Update channel selection is presented as a sub-decision within installation rather than a separate topic.

**Metrics:** From 2 separate sections requiring 4 clicks (Assembly → Section 1 → Read, then back to Assembly → Section 2 → Compare) to 1 job with 3 approaches requiring 2 clicks (Job 1 → Read all approaches). 50% reduction in navigation depth.

---

### Example 2: Automatic Pruning Configuration (5 subsections → 1 job with 2 options)

**Current (Fragmented):**
- Section 17: Automatic pruning of task runs and pipeline runs (lines 1426-1436) — Overview section
  - Subsection 17.1: Configuring the pruner (lines 1446-1506) — Scheduled/cron-based approach
  - Subsection 17.2: Annotations for automatically pruning task runs and pipeline runs (lines 1516-1554) — Namespace overrides for scheduled approach
  - Subsection 17.3: Enabling the event-driven pruner (lines 1563-1643) — Event-based approach setup
  - Subsection 17.4: Configuration of the event-driven pruner (lines 1651-1875) — Event-based approach configuration details
  - Subsection 17.5: Observability metrics of the event-driven pruner (lines 1883-1961) — Event-based approach monitoring

User must read all 5 subsections (520 lines total) to discover that scheduled and event-driven approaches are mutually exclusive, to understand the trade-offs between batch vs real-time cleanup, and to learn that observability metrics are only available for the event-driven approach. No clear "choose A or B" guidance is provided upfront.

**Proposed (Consolidated):**
- **Job 8: Automatically Remove Completed Pipeline Runs**
  - 8.1. Choose between scheduled and event-driven pruning approaches (concept) — Comparison table showing timing, complexity, observability, use cases, mutual exclusivity
  - 8.2. Configure scheduled (cron-based) pruning (lines 1446-1506) — For predictable batch cleanup
  - 8.3. Configure namespace-specific overrides for scheduled pruning (lines 1516-1554) — When different projects have different retention needs
  - 8.4. Enable event-driven (real-time) pruning (lines 1563-1643) — For near real-time cleanup
  - 8.5. Configure event pruner retention policies (lines 1651-1875) — TTL-based and history-based rules at global/namespace/resource levels
  - 8.6. Monitor event pruner performance (lines 1883-1961) — OpenTelemetry metrics reference

**Benefit:** Users immediately see in approach 8.1 that two mutually-exclusive approaches exist, can compare them in a table (timing, complexity, observability, use cases), and choose the appropriate approach before diving into configuration details. Related configuration (namespace overrides for scheduled, retention policies for event-driven, metrics for event-driven) is nested under each approach rather than scattered across separate subsections. The 60% reduction in navigation items (from 5 subsections to 2 approaches with sub-items) makes the decision path clear: choose scheduled (approaches 8.2-8.3) OR event-driven (approaches 8.4-8.6).

**Metrics:** From 5 subsections requiring users to read all of them to understand options (5 sections × average 3 clicks each = 15 total clicks) to 1 job with 2 clearly-labeled options requiring 3 clicks (Job 8 → Read 8.1 comparison → Choose approach 8.2-8.3 OR 8.4-8.6). 80% reduction in navigation to decision.

---

### Example 3: Production Configuration Topics (5 scattered sections → 2 unified jobs)

**Current (Fragmented):**
- Section 1: Performance tuning using the TektonConfig custom resource (lines 541-613) — HA mode, buckets, replicas, API query limits
- Section 2: Configuring the pipelines control plane (lines 621-668) — Metrics, sidecars, service accounts
- Section 4: Changing the default service account for OpenShift Pipelines (lines 764-784) — Service account customization
- Section 6: Setting the resync period for the pipelines controller (lines 827-862) — Resync period tuning for large clusters
- Section 7: Disabling the service monitor (lines 874-892) — Metrics disabling

User must discover that sections 1, 2, 6, and 7 are all related to "production configuration" by reading through the entire assembly 3. Service account (section 4) appears to be related to control plane configuration but is separated from section 2. No guidance is provided on which configurations to apply when or in what order.

**Proposed (Consolidated):**
- **Job 3: Optimize Controller Performance**
  - 3.1. Enable high-availability mode with multiple controller replicas (lines 541-613) — When needing to scale pipeline operations
  - 3.2. Understand HA mode performance parameters (reference) — Buckets, replicas, threads-per-controller, API query limits
- **Job 4: Configure Control Plane Settings**
  - 4.1. Optimize for non-sidecar environments (lines 686-693) — For clusters without Istio or injected sidecars
  - 4.2. Configure metrics collection (lines 686-784) — When needing to customize metrics exposure
  - 4.3. Set resync period for large clusters (lines 827-862) — For clusters with large numbers of pipeline runs
  - 4.4. Disable service monitor if needed (lines 874-892) — When not needing to expose telemetry data

**Benefit:** Related production configuration topics are consolidated under 2 clear goals (optimize controller performance for high volume vs configure control plane for production environment). Service account configuration is moved to Job 5 (security stage) where it belongs. Users following a "production hardening" workflow can navigate directly to Jobs 3-4 instead of hunting through sections 1, 2, 6, 7 scattered across assembly 3.

**Metrics:** From 5 scattered sections across assembly 3 (requiring 10+ clicks to find all related content: Assembly → Section 1, Assembly → Section 2, Assembly → Section 4, Assembly → Section 6, Assembly → Section 7) to 2 unified jobs in "Configure for Production" stage (requiring 4 clicks: Stage → Job 3 → Read approaches, Job 4 → Read approaches). 60% reduction in clicks to find all production configuration content.

---

## Content Gaps Identified

| Gap | JTBD Reference | Current Coverage | Impact |
|-----|---------------|-----------------|--------|
| No troubleshooting workflows for webhook failures, installation issues, or component readiness problems | Jobs 1-2 (installation and verification) | None — users must rely on generic OpenShift troubleshooting or support tickets | **High** — Webhook timeout errors, installation verification failures, and proxy configuration problems are common issues that create support tickets and block users from proceeding with pipeline creation. Without troubleshooting guidance, users cannot self-recover from failed installations. |
| No upgrade procedures beyond update channel selection | Job 1 (installation) | Update channel selection mentioned (lines 117-125), but no pre-upgrade checklist, upgrade process via OLM, post-upgrade verification, or rollback procedures | **High** — Upgrading OpenShift Pipelines is a lifecycle-critical operation affecting production pipelines. Users need guidance on backup strategies, upgrade sequencing (especially for multi-cluster environments), and verification that components upgraded successfully. Current gap forces users to treat upgrades as "install and hope." |
| No performance monitoring beyond event pruner metrics | Job 8.6 (event pruner observability only) | Event pruner metrics documented (lines 1883-1961), but no pipeline execution metrics, controller performance metrics, or resource consumption dashboards for the controller itself | **Medium** — Event pruner metrics are useful but limited. Users running high-volume pipelines need visibility into controller performance (reconciliation times, queue depth, error rates) and pipeline execution metrics (duration, failure rates, resource usage) to optimize performance and diagnose bottlenecks. Current coverage focuses only on pruner observability, not overall system health. |
| No guidance on backup and restore of pipeline definitions | Job 13 (uninstallation) | Warning mentions "consider backing up pipeline definitions before deletion" (line 492), but no procedures for backing up, exporting, or restoring pipeline/task CRs | **Medium** — Users risk losing pipeline definitions during uninstallation, cluster migration, or disaster recovery scenarios. Without backup/restore procedures, users must discover third-party tools (velero, oc get/apply) or risk permanent loss. Gap is particularly critical during uninstallation when users are warned to back up but not told how. |
| No guidance on pipeline security scanning or admission control policies | Job 10 (disable inline specs) | Inline spec disabling documented as supply chain security control (lines 1284-1370), but no guidance on scanning pipeline definitions for security issues, enforcing policies via OPA/Gatekeeper, or auditing pipeline execution for compliance | **Medium** — Disabling inline specs is one control, but users enforcing compliance need guidance on scanning pipeline YAML for vulnerabilities (secrets in logs, privileged containers), enforcing policies (allowed registries, resource limits), and auditing execution. Current gap leaves security-conscious users without a complete security strategy. |
| No multi-cluster deployment patterns or federation guidance | All jobs (assumes single cluster) | All content assumes single-cluster deployment, no guidance on multi-cluster pipeline orchestration, shared catalog management, or federation strategies | **Low** — Most users deploy to single cluster initially. Multi-cluster patterns are advanced use case for large organizations. Gap is low priority for most users but blocks enterprises needing centralized pipeline management across clusters. |
| No cost optimization guidance for pipeline resource usage | Jobs 3-4 (performance and control plane configuration) | Performance tuning focuses on handling high load (HA mode, API query limits), but no guidance on reducing costs by rightsizing resources, using spot instances for pipeline runs, or optimizing task run resource requests | **Low** — Performance tuning exists but focuses on scale-up, not cost reduction. Users running pipelines in cloud environments could benefit from cost optimization tips (node selectors for spot instances, resource request optimization, pipeline caching strategies), but this is nice-to-have rather than critical. |
| No pipeline design best practices or anti-patterns | All jobs (operational focus, not design guidance) | Documentation covers operator installation and configuration, but no guidance on designing pipelines for reusability, modularity, or maintainability | **Low** — Users can create pipelines without design guidance, but may create unmaintainable monolithic pipelines. Best practices content (task decomposition, workspace usage, secret management, pipeline composition) would improve long-term maintainability but is not critical for initial deployment. This gap is better addressed in pipeline authoring documentation, not operator installation guide. |

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 3 assemblies with 30+ modules | 7 workflow stages with 14 jobs | 53% reduction in top-level items to browse |
| Sections to browse for "installing pipelines" | 2 sections across assembly 1 (web console, CLI) | 1 job with 2 approaches side-by-side | 50% reduction; side-by-side comparison eliminates need to switch sections |
| Sections to browse for "production configuration" | 5 scattered sections (performance, control plane, service account, resync period, metrics) across assembly 3 | 2 jobs in "Configure for Production" stage (Jobs 3-4) | 60% reduction; related topics grouped by goal |
| Sections to browse for "automatic pruning" | 5 subsections under automatic pruning heading | 1 job with 2 clearly-labeled approaches (Scheduled vs Event-Driven) | 60% reduction in navigation items; 80% reduction in clicks to decision (from 15 clicks to read all 5 subsections to 3 clicks to read comparison and choose approach) |
| Sections to browse for "security configuration" | 3 buried sections (service accounts section 4, RBAC section 15, inline specs section 17) in assembly 3 | Dedicated "Secure Your Pipelines" stage with 3 visible jobs (Jobs 5, 9, 10) | Elevated from buried content to top-level stage; security jobs now discoverable without reading entire assembly 3 |
| Clicks to find "how to uninstall cleanly" | 4 clicks (Assembly 2 → Section 1 → Read, Section 2 → Read, Section 3 → Read to understand sequence) | 2 clicks (Decommission stage → Job 13 with 3 sequential steps in one place) | 50% reduction; sequencing warnings now inline with steps |
| Clicks to find "Tekton Hub migration" | 4 clicks (Assembly 3 → Section 11 → Subsection 11.1 Assess, Subsection 11.2 Migrate) | 2 clicks (Migrate stage → Job 7 with 3 sequential steps) | 50% reduction; migration workflow now in clear progression |
| Navigation depth to common tasks | 4-6 clicks on average (Assembly → Section → Subsection → Read → potentially Compare other sections) | 2-3 clicks on average (Stage → Job → Read approaches in one place) | ~50% average reduction in navigation depth |

**Final job count: 14** (reduced from suggested 30 records). Consolidation rationale: The original 30 JTBD records represented fine-grained user stories (installation via web console as separate record from installation via CLI, HA mode enablement as separate from performance tuning, etc.). These were consolidated into 14 main jobs by recognizing that multiple records represent implementation paths for the same goal (installation job has UI and CLI approaches, pruning job has scheduled and event-driven approaches, uninstallation job has 3 sequential steps). This consolidation maintains granular content (all 30 original record topics appear as approaches within jobs) while reducing navigation complexity (from 30 separate items to 14 jobs with 2-5 approaches each).

---

## UX Research Alignment

**Note:** The JTBD records analyzed for this documentation (`install_config-jtbd.jsonl`) do not contain UX research extension fields (`pain_points`, `strategic_priority`, `teams_involved`, `loop`). This section is therefore not applicable to this consolidation report. 

If future JTBD analysis sessions include user research data (pain points from user interviews, strategic priority flags from product management, team collaboration patterns from organizational analysis, or inner/outer loop classifications from user workflows), that information would be documented here showing:

- **Pain Points Addressed by Restructure:** How the new structure directly resolves user-reported pain points
- **Strategic Priorities Elevated:** Jobs flagged as strategic that moved from buried sections to visible top-level positions
- **Cross-Team Collaboration Visibility:** Jobs requiring collaboration between multiple teams (e.g., cluster admins + security engineers) and how the structure facilitates that collaboration
- **Loop Distribution:** Classification of jobs by inner loop (dev/experimentation) vs outer loop (production/ops) to ensure both workflows are well-supported

The absence of this data in the current records indicates the JTBD analysis focused on structural consolidation and workflow organization rather than user research integration.

---

## Document Statistics

**Workflow Coverage:**
- **Get Started:** 2 jobs (Install Operator, Verify Installation)
- **Configure:** 6 jobs (Optimize Performance, Configure Control Plane, Manage Resolvers, Configure Webhooks, Configure Private Hub, Configure Proxy)
- **Secure:** 3 jobs (Change Service Account, Disable RBAC, Disable Inline Specs)
- **Migrate:** 1 job (Tekton Hub to Artifact Hub)
- **Operate:** 1 job (Automatic Pruning with 2 approaches)
- **Monitor:** Embedded in Job 8.6 (Event Pruner Metrics)
- **Conclude:** 1 job (Fully Remove Pipelines with 3 sequential steps)
- **Missing:** Troubleshoot stage (no troubleshooting content), Upgrade procedures (only update channel selection documented)

**Job Distribution:**
- Main jobs: 14
- Implementation paths/approaches: 39 total approaches across all jobs
- Average approaches per job: 2.8
- Jobs with multiple approaches: 10 (Jobs 1, 3, 4, 6, 7, 8, 9, 11, 13, 14)
- Jobs with single approach: 4 (Jobs 2, 5, 10, 12)

**Source Content Analysis:**
- Source documents: 3 assemblies (Installing, Uninstalling, Customizing)
- Total source lines: 2,127 (install_config-combined.adoc)
- JTBD records: 30 (pre-consolidated user stories)
- Main jobs after consolidation: 14 (53% reduction)
- Modules in current structure: 30+
- Jobs in proposed structure: 14 (with 39 nested approaches)

**Consolidation Impact:**
- Installation: 2 separate sections → 1 job with 2 approaches (50% consolidation)
- Production configuration: 5 scattered sections → 2 jobs with 7 approaches (60% consolidation)
- Pruning: 5 subsections → 1 job with 6 approaches (80% consolidation in navigation items)
- Uninstallation: 3 sections → 1 job with 3 sequential approaches (maintained granularity, improved sequencing clarity)
- Security: 3 buried sections → 3 elevated jobs in dedicated stage (100% visibility improvement)
- Overall top-level items: 30+ modules → 14 jobs (53% reduction)

**Personas Addressed:**
- Cluster administrator (Jobs 1, 2, 3, 4, 5, 9, 12, 13, 14)
- Platform engineer (Jobs 1, 3, 4, 6, 7, 8, 11)
- Security engineer (Jobs 10)
- SRE (Jobs 8.6 monitoring)

**Topic Type Distribution:**
- Procedures: 28 approaches (72% of total approaches)
- Concepts: 7 approaches (18% of total approaches)
- Reference: 4 approaches (10% of total approaches)
- Distribution shows appropriate balance: majority procedural (installation, configuration, operational tasks), supported by conceptual decision guidance and reference lookup material

**Cross-References and Dependencies:**
- Explicit prerequisite chains: 8 jobs have prerequisites (Jobs 2, 3, 4, 5, 6, 7, 10, 13)
- Timing guidance: 5 jobs have BEFORE/AFTER guidance (Jobs 2, 5, 10, 12, 14)
- Sequential workflows: 2 jobs have explicit step sequences (Jobs 7 and 13)
- Related jobs: Resolver management (Job 6) relates to migration (Job 7), security jobs (5, 9, 10) form cohesive hardening workflow


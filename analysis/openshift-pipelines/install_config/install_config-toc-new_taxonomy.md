# Installing and Configuring OpenShift Pipelines
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** This guide helps cluster administrators and platform engineers deploy, configure, and manage the Red Hat OpenShift Pipelines Operator and its components across cluster lifecycles.

**Personas:** Cluster administrator, Platform engineer, Security engineer, SRE

**Main Jobs:** 14 core jobs across 7 workflow stages

---

## Quick Navigation

**I want to:**
- Install the Pipelines Operator → Job 1 (Get Started)
- Verify installation succeeded → Job 2 (Get Started)
- Configure HA mode for performance → Job 3 (Configure)
- Tune control plane settings → Job 4 (Configure)
- Change service accounts → Job 5 (Secure)
- Manage resource resolution → Job 6 (Configure)
- Migrate from Tekton Hub → Job 7 (Migrate)
- Set up automatic cleanup → Job 8 (Operate)
- Disable automatic RBAC → Job 9 (Secure)
- Disable inline specs → Job 10 (Secure)
- Configure webhooks → Job 11 (Configure)
- Set up private Artifact Hub → Job 12 (Configure)
- Uninstall cleanly → Job 13 (Conclude)
- Handle proxy settings → Job 14 (Configure)

---

# Table of Contents

## Getting Started with Pipelines

### Job 1: Install the OpenShift Pipelines Operator
*When deploying CI/CD infrastructure to enable pipeline functionality*

**Personas:** Cluster administrator, Platform engineer

#### Installation Methods

**For administrators preferring graphical interfaces:**
- Install via web console using OperatorHub
  -> Lines 74-183: Web console installation procedure
  - Navigate to Operators → OperatorHub
  - Search for "OpenShift Pipelines"
  - Select installation mode (all namespaces)
  - Choose approval strategy (Automatic/Manual)
  - Select update channel (latest or pipelines-<version>)
  - Wait for installation to complete

**For platform engineers managing infrastructure as code:**
- Install using CLI with YAML manifests
  -> Lines 188-235: CLI-based installation
  - Create Subscription object YAML
  - Apply with `oc apply -f sub.yaml`
  - Operator auto-installs TektonConfig

**Update channel considerations:**
- Select update channel based on version requirements
  -> Lines 117-125: Channel selection
  - `latest` for most recent stable version
  - `pipelines-<version>` for specific version control
  - Note: preview/stable channels deprecated after OCP 4.10

### Job 2: Verify Operator Installation Success
*When installation completes, to confirm all components are ready*

**Personas:** Cluster administrator

**Timing:** AFTER Job 1 - Components may appear ready in UI while still installing

**Why:** Web console status may show "Succeeded Up to date" even if installation in progress

-> Lines 134-182: Verification procedures
1. Check TektonConfig status: `oc get tektonconfig config`
2. Verify READY condition is True
3. Check component versions:
   `oc get tektonpipeline,tektontrigger,tektonchain,tektonaddon,pac`
4. Confirm all components show Ready: True

---

## Configure for Production

### Job 3: Optimize Controller Performance
*When managing high-volume pipeline workloads to reduce delays*

**Personas:** Cluster administrator, Platform engineer

**Requires:** Understanding of cluster scale and load characteristics

-> Lines 541-613: Performance tuning reference

#### Enable High-Availability Mode

**For scaling pipeline operations:**
- Configure HA mode with multiple controller replicas
  -> Lines 556-597: HA mode configuration
  - Set `disable-ha: false`
  - Configure `buckets` (max 10)
  - Set `replicas` (≤ buckets value)
  - Adjust `threads-per-controller` (default 2)
  - Tune `kube-api-qps` and `kube-api-burst`

**Performance tuning parameters:**
| Parameter | Purpose | Default |
|-----------|---------|---------|
| disable-ha | Enable/disable HA mode | false |
| buckets | Operation partitioning | 1 |
| replicas | Controller pod count | 1 |
| threads-per-controller | Workers per controller | 2 |
| kube-api-qps | Max queries per second | 5.0 |
| kube-api-burst | Throttle burst limit | 10 |

### Job 4: Configure Control Plane Settings
*When deploying pipelines in production to tailor execution environment*

**Personas:** Cluster administrator, Platform engineer

-> Lines 621-668: Control plane configuration

#### Optimize for Non-Sidecar Environments

**For clusters without Istio or injected sidecars:**
- Disable sidecar readiness checks
  -> Lines 686-693: Sidecar configuration
  - Set `running-in-environment-with-injected-sidecars: false`
  - Reduces task run startup time
  - Set `await-sidecar-readiness: false` for environments without downwardAPI

**For large-scale deployments:**
- Configure longer resync period
  -> Lines 827-862: Resync period tuning
  - Default: 10 hours
  - For large clusters: increase to 24h
  - Edit TektonConfig with `-resync-period=24h`

#### Customize Metrics and Service Accounts

**Metrics configuration:**
-> Lines 621-668, 686-784: Configurable settings
- Set `metrics.taskrun.duration-type` (histogram/gauge)
- Set `metrics.pipelinerun.duration-type`
- Configure `metrics.taskrun.level` (taskrun/task/namespace)
- Configure `metrics.pipelinerun.level` (pipelinerun/pipeline/namespace)
- Enable/disable with `enableMetrics` parameter

### Job 6: Manage Pipeline Resource Resolution
*When controlling how pipelines fetch remote resources*

**Personas:** Cluster administrator

**Requires:** Understanding of resolver types and security implications

-> Lines 903-949: Resolver configuration

#### Enable or Disable Specific Resolvers

**Available resolver types:**
- `enable-bundles-resolver` - OCI bundle support
- `enable-cluster-resolver` - Cluster-local resources
- `enable-git-resolver` - Git repository resources
- `enable-hub-resolver` - Hub catalog resources

**Resolver-specific configuration:**
-> Lines 903-949: Per-resolver settings
- `bundles-resolver-config`: `default-service-account`
- `cluster-resolver-config`: `default-namespace`
- `git-resolver-config`: `server-url`
- `hub-resolver-config`: `default-tekton-hub-catalog`, `default-artifact-hub-url`

**For customizing default resources:**
- Disable automatic template installation
  -> Lines 958-999: Disabling resolver tasks and templates
  - Set `resolverTasks: false` to prevent default task installation
  - Set `pipelineTemplates: false` to prevent template installation
  - Note: pipelineTemplates requires resolverTasks to be true

### Job 12: Configure Private Artifact Hub
*When operating in disconnected networks to resolve from internal registry*

**Personas:** Cluster administrator

**Requires:** Private Artifact Hub instance, network connectivity, TLS certificates

**Timing:** BEFORE using hub resolver in air-gapped environments

-> Lines 1201-1231: Private Artifact Hub configuration

**Prerequisites:**
- Deploy private Artifact Hub instance
- Configure network connectivity from resolver pods
- Configure TLS certificates for HTTPS endpoints
- Configure authentication if required
- Ensure catalog names match private hub publications

**Configuration:**
- Edit TektonConfig hub-resolver-config
- Set `default-artifact-hub-url: "https://your-private-hub"`

### Job 14: Configure Proxy for Restricted Environments
*When operating in air-gapped networks to enable pipeline execution*

**Personas:** Cluster administrator

**Requires:** Cluster proxy object configured

**Timing:** AFTER Job 1 - Operator auto-configures proxy webhook

-> Lines 240-256: Restricted environment support

**How it works:**
- Operator installs proxy webhook automatically
- Webhook sets proxy environment variables in pod containers
- Based on cluster proxy object configuration
- Sets variables in TektonPipelines, TektonTriggers, Controllers, Webhooks

**To disable proxy for specific namespaces:**
- Add label: `operator.tekton.dev/disable-proxy: true`
- Default: disabled for openshift-pipelines namespace

### Job 11: Configure Webhook Behavior
*When customizing admission control to prevent submission delays*

**Personas:** Platform engineer

**Requires:** Understanding of webhook types (mutating vs validating)

-> Lines 1969-2118: Webhook configuration

**Configurable options:**
- `failurePolicy`: How Kubernetes handles webhook failures (Fail/Ignore)
- `timeoutSeconds`: Webhook timeout (default 10s, max 30s)
- `sideEffects`: Whether webhook has side effects (None/NoneOnDryRun)

**Applies to controllers:**
- Pipeline: `validation.webhook.pipeline.tekton.dev`, `webhook.pipeline.tekton.dev`
- Triggers: `validation.webhook.triggers.tekton.dev`, `webhook.triggers.tekton.dev`
- Pipelines as Code: `validation.pipelinesascode.tekton.dev`
- Tekton Hub: `validation.webhook.hub.tekton.dev`, `webhook.hub.tekton.dev`

**Note:** Cannot configure operator webhooks

---

## Secure Your Pipelines

### Job 5: Change Default Service Account
*When enforcing security policies to align with RBAC requirements*

**Personas:** Cluster administrator

**Requires:** Custom service account with appropriate permissions

**Timing:** BEFORE running production pipelines

-> Lines 764-784: Service account configuration

**Configuration:**
- Edit TektonConfig CR
- Set `spec.pipeline.default-service-account: <account-name>`
- Set `spec.trigger.default-service-account: <account-name>`
- Applies to TaskRun and PipelineRun resources

### Job 9: Disable Automatic RBAC Creation
*When requiring fine-grained permission control to prevent privileged bindings*

**Personas:** Cluster administrator

**Requires:** Understanding of pipelines-scc security implications

**Why:** Default `pipelines-scc-rolebinding` has RunAsAny SCC privilege, which is a potential security risk

-> Lines 1240-1276: RBAC disabling procedure

**Configuration:**
- Edit TektonConfig CR
- Set `spec.params[name=createRbacResource].value: "false"`
- Manually create namespace-specific RBAC resources as needed
- Can separately control Trusted CA bundle with `createCABundleConfigMaps`

### Job 10: Disable Inline Pipeline Specifications
*When enforcing supply chain security to require version-controlled resources*

**Personas:** Security engineer

**Requires:** Pipeline and task versioning strategy, resolver configuration

**Timing:** BEFORE deploying production pipelines

**Why:** Inline specs bypass version control and security scanning

-> Lines 1284-1370: Inline spec disabling

**Configuration:**
- Edit TektonConfig CR
- Set `spec.pipeline.disable-inline-spec: "pipeline,pipelinerun,taskrun"`
- Forces use of `taskRef:` and `pipelineRef:` instead of inline `taskSpec:` and `pipelineSpec:`

**Enforcement levels:**
- `pipeline` - Prevents taskSpec in Pipeline CR
- `pipelinerun` - Prevents pipelineSpec in PipelineRun CR
- `taskrun` - Prevents taskSpec in TaskRun CR

---

## Migrate Between Catalogs

### Job 7: Migrate from Tekton Hub to Artifact Hub
*When Tekton Hub deprecation affects pipelines to ensure uninterrupted catalog resolution*

**Personas:** Platform engineer

**Requires:** Inventory of resources using Tekton Hub, Artifact Hub catalog structure knowledge

**Why:** Tekton Hub is deprecated; hub resolver now defaults to Artifact Hub

-> Lines 1065-1189: Migration guide

#### Assess Migration Impact

**Before migrating:**
- Identify resources using Tekton Hub
  -> Lines 1085-1126: Assessment scripts
  - Search for `type: tekton` or `catalog: Tekton` in YAML files
  - Check hub resolver configuration with kubectl
  - Count affected resources by type (Pipeline, TaskRun, etc.)

**Migration checklist:**
- Resources reference `type: tekton` or `catalog: Tekton`
- Resources use non-semver catalog versions
- Hub resolver still configured with `type: tekton`

#### Update Resource Definitions

**Migration steps:**
1. Remove `type: tekton` parameter (do NOT add `type: artifact` - it's the default)
2. Update catalog names:
   - Tasks: `Tekton` → `tekton-catalog-tasks`
   - Pipelines: `Tekton` → `tekton-catalog-pipelines`
   - StepActions: `Tekton` → `tekton-catalog-stepactions`
3. Update versions to full semantic versioning (e.g., `0.8` → `0.8.0`)
4. Reapply resource definitions

**For private/disconnected environments:**
-> Lines 1201-1231: Private Artifact Hub setup
- Configure custom Artifact Hub endpoint (see Job 12)
- Ensure catalog names match private hub publications

---

## Operate and Maintain

### Job 8: Automatically Remove Completed Pipeline Runs
*When managing cluster resources over time to prevent exhaustion*

**Personas:** Cluster administrator, Platform engineer, SRE

**Requires:** Understanding of retention requirements and compliance needs

**Why:** Stale TaskRun and PipelineRun objects consume cluster resources and degrade performance

-> Lines 1426-1436: Pruning overview

#### Choose Pruning Approach

**Option A: Scheduled (Cron-Based) Pruning**
-> Lines 1446-1506: Scheduled pruner configuration

**For predictable batch cleanup:**
- Configure in TektonConfig `spec.pruner` section
- Set schedule (cron format, default `* 8 * * *`)
- Choose retention policy:
  - `keep: 100` - retain 100 most recent runs of each type
  - `keep-since: 7200` - retain runs from last 7200 minutes (5 days)
  - Note: `keep` and `keep-since` are mutually exclusive
- Set `prune-per-resource: false` (global count) or `true` (per pipeline/task)
- Configure `startingDeadlineSeconds` for missed schedules

**For namespace-specific overrides:**
-> Lines 1516-1554: Namespace annotations
- Add annotations to Namespace resource:
  - `operator.tekton.dev/prune.schedule`
  - `operator.tekton.dev/prune.resources: "taskrun, pipelinerun"`
  - `operator.tekton.dev/prune.keep: "100"`
  - `operator.tekton.dev/prune.keep-since: "7200"`
  - `operator.tekton.dev/prune.skip: "true"` (to skip namespace)

**Option B: Event-Driven (Real-Time) Pruning**
-> Lines 1563-1643: Event pruner setup

**For near real-time cleanup:**
- Disable job-based pruner: `spec.pruner.disabled: true`
- Enable event pruner: `spec.tektonpruner.disabled: false`
- Verify tekton-pruner-controller and tekton-pruner-webhook pods running
- Cannot enable both pruner types simultaneously

**Event pruner configuration:**
-> Lines 1651-1875: TTL and history limits
- `ttlSecondsAfterFinished`: Delete after N seconds (e.g., 300s for dev, 86400s for staging, 2592000s for compliance)
- `historyLimit`: Generic retention count when status-specific limits not defined
- `successfulHistoryLimit`: Retain N successful runs
- `failedHistoryLimit`: Retain N failed runs
- `enforcedConfigLevel`: `global` or `namespace`

**Namespace-level event pruner:**
- Set `enforcedConfigLevel: namespace`
- Define per-namespace policies in `namespaces` section
- Example: different TTL for dev-project (60s) vs staging (300s)

**Resource-level event pruner:**
- Create `tekton-pruner-namespace-spec` ConfigMap in namespace
- Add labels: `app.kubernetes.io/part-of: tekton-pruner`, `pruner.tekton.dev/config-type: namespace`
- Define TTL and history limits per resource type
- Use selectors to match specific labels/annotations

**Common TTL values:**
| Environment | TTL (seconds) | Use Case |
|-------------|---------------|----------|
| 5 minutes | 300 | Dev/testing rapid iteration |
| 30 minutes | 1800 | Short-lived experiments |
| 1 hour | 3600 | CI pipelines |
| 6 hours | 21600 | Daily builds |
| 1 day | 86400 | Staging environments |
| 7 days | 604800 | Production short retention |
| 30 days | 2592000 | Compliance/auditing |
| 90 days | 7776000 | Regulated industries |

#### Monitor Event Pruner Performance

**For SREs operating event-driven pruner:**
-> Lines 1883-1961: Observability metrics

**Available metrics (OpenTelemetry format):**
- `tekton_pruner_controller_resources_processed_total` (Counter)
  - Labels: namespace, resource_type, status
- `tekton_pruner_controller_resources_deleted_total` (Counter)
  - Labels: namespace, resource_type, operation
- `tekton_pruner_controller_reconciliation_duration_seconds` (Histogram)
  - Labels: namespace, resource_type
  - Buckets: 0.1s to 30s
- `tekton_pruner_controller_ttl_processing_duration_seconds` (Histogram)
- `tekton_pruner_controller_history_processing_duration_seconds` (Histogram)
- `tekton_pruner_controller_resources_errors_total` (Counter)
  - Labels: namespace, resource_type, reason
- `kn_workqueue_adds_total` (Counter)
- `kn_workqueue_depth` (Gauge)

---

## Decommission Pipelines

### Job 13: Fully Remove OpenShift Pipelines
*When needing to cleanly uninstall to avoid residual resources*

**Personas:** Cluster administrator

**Requires:** Understanding that uninstallation deletes all pipelines and tasks

**Why:** Skipping steps causes orphaned components that cannot be removed later

**Timing:** Follow 3-step sequence to avoid conflicts

-> Lines 335-393: Uninstallation overview

#### Step 1: Delete Custom Resources

**For preparing operator uninstallation:**
-> Lines 361-392: CR deletion procedure

**Critical sequencing (must follow this order):**
1. Search for and delete TektonHub CRs (if exist)
2. Search for and delete TektonResult CRs (if exist)
3. Search for and delete TektonConfig CR

**Via web console:**
- Navigate to Administration → CustomResourceDefinitions
- Filter by name for each CRD
- Click Options menu → Delete for each instance

**Warnings:**
- Deleting CRs also deletes all Pipelines components, tasks, and pipelines on cluster
- If you uninstall Operator without removing TektonHub and TektonResult CRs, you cannot remove those components later
- Consider backing up pipeline definitions before deletion

#### Step 2: Uninstall the Operator

**After deleting all CRs:**
-> Lines 402-421: Operator uninstallation

**Via web console:**
1. Navigate to Operators → OperatorHub
2. Search for "OpenShift Pipelines"
3. Click Uninstall
4. Select "Delete all operand instances for this operator"
5. Confirm uninstallation

**Warning:**
- Uninstallation deletes ALL resources in openshift-pipelines namespace, including secrets
- Back up secrets if needed before proceeding

#### Step 3: Delete Custom Resource Definitions

**For complete cleanup:**
-> Lines 431-449: CRD deletion

**Via web console:**
1. Navigate to Administration → CustomResourceDefinitions
2. Filter by `operator.tekton.dev`
3. For each displayed CRD:
   - Click Options menu → Delete CustomResourceDefinition
   - Confirm deletion

**Why this step matters:**
- Ensures no residual CRD definitions remain
- Prevents conflicts during future installations
- Provides clean slate for potential reinstallation

---

## Appendices

### A. Installation Method Comparison

| Method | Best For | Pros | Cons | Job Reference |
|--------|----------|------|------|---------------|
| Web Console | Administrators preferring GUI | Visual configuration, installation progress visibility | Requires web console access, less automation-friendly | Job 1 (User Story 1) |
| CLI (YAML) | Platform engineers, IaC workflows | Automation via CI/CD, version-controlled config, reproducible | Requires CLI expertise, less visibility into progress | Job 1 (User Story 2) |

### B. Pruning Approach Selection Guide

| Factor | Scheduled (Cron) | Event-Driven (Real-Time) |
|--------|------------------|--------------------------|
| Cleanup timing | Batch at scheduled intervals | Immediate after completion |
| Configuration complexity | Simpler (cron schedule + retention) | More complex (TTL + history limits + levels) |
| Resource spikes | May cause spikes during batch processing | Distributed load |
| Observability | Limited (cron job status) | Rich metrics via OpenTelemetry |
| Use cases | Predictable cleanup cycles, simpler requirements | Compliance with tight retention, resource-constrained clusters |
| Namespace customization | Annotations only | Annotations + ConfigMaps + selectors |
| Mutually exclusive | Cannot coexist with event-driven | Cannot coexist with scheduled |

### C. Workflow Coverage Analysis

**Coverage by Stage:**
- ✅ Get Started: 2 jobs (Install Operator, Verify Installation)
- ✅ Configure: 8 jobs (Performance, Control Plane, Resolvers, Webhooks, Proxy, Private Hub, Resync Period, Pruning Config)
- ✅ Secure: 3 jobs (Service Account, RBAC, Inline Specs)
- ✅ Migrate: 1 job (Tekton Hub to Artifact Hub)
- ✅ Operate: 1 job (Automatic Pruning)
- ✅ Monitor: 1 job (Event Pruner Metrics) - embedded in Job 8
- ✅ Conclude: 1 job (Uninstall)

**Coverage gaps identified:**
- ❌ Troubleshoot: No dedicated troubleshooting workflows (webhook failures, installation issues)
- ❌ Upgrade: No upgrade procedures (covered implicitly via update channel selection)
- ❌ Deploy: N/A for operator installation guide (pipelines themselves are created separately)

### D. Persona Journey Paths

**Cluster Administrator - New Installation:**
1. Job 1: Install Operator (Web Console method)
2. Job 2: Verify Installation
3. Job 5: Change Default Service Account
4. Job 9: Disable Automatic RBAC
5. Job 8: Configure Scheduled Pruning

**Platform Engineer - Production Hardening:**
1. Job 1: Install Operator (CLI method)
2. Job 3: Optimize Controller Performance (HA mode)
3. Job 4: Configure Control Plane (metrics, sidecars)
4. Job 6: Configure Resolvers
5. Job 11: Configure Webhooks
6. Job 8: Configure Event-Driven Pruning

**Security Engineer - Compliance Setup:**
1. Job 5: Change Default Service Account
2. Job 9: Disable Automatic RBAC
3. Job 10: Disable Inline Specs
4. Job 8: Configure Event-Driven Pruning (TTL for compliance)

**SRE - Disconnected Environment:**
1. Job 14: Configure Proxy Settings (automatically via cluster proxy)
2. Job 12: Configure Private Artifact Hub
3. Job 7: Migrate to Artifact Hub (private instance)
4. Job 8: Configure Event-Driven Pruning with monitoring (Job 8 metrics)

---

## Document Statistics

**Workflow Coverage:**
- Get Started: 2 jobs
- Configure: 8 jobs
- Secure: 3 jobs
- Migrate: 1 job
- Operate: 1 job
- Monitor: 1 job (embedded)
- Conclude: 1 job
- **Missing:** Troubleshoot, Upgrade (implicit)

**Main Jobs:** 14
**User Stories/Paths:** 16 (multiple implementation paths per job)
**Source Sections:** 30 JTBD records analyzed
**Platform/Tool Variations:** 2 pruning approaches, 2 installation methods, 4 resolver types

**Source Documentation:**
- Book: install_config
- Distro: openshift-pipelines
- Assemblies: Installing, Uninstalling, Customizing configurations
- Total lines: 2,126 (combined reduced content)

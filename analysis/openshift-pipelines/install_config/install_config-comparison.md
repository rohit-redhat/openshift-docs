# Installing and Configuring OpenShift Pipelines - TOC Comparison

**Current Feature-Based vs. Proposed JTBD-Based Structure**

**Analysis Date:** 2026-06-12  
**Distro:** openshift-pipelines  
**Book:** install_config  
**JTBD Records:** 30  
**Main Jobs:** 14 (consolidated from 30 records)  
**Workflow Stages Covered:** 7 of 8 (Get Started, Configure, Secure, Migrate, Operate, Monitor, Conclude)  
**Personas:** Cluster administrator, Platform engineer, Security engineer, SRE

---

## Executive Summary

**Current State:**
- 3 assemblies organized by lifecycle phase (Installing, Uninstalling, Customizing)
- 30+ modules covering features and configuration options
- Linear chapter-by-chapter navigation
- Scattered configuration topics across multiple sections

**Proposed State:**
- 14 main jobs organized by workflow stages
- Consolidated configuration topics under goal-oriented headings
- Multiple implementation paths (UI vs CLI, scheduled vs event-driven)
- Clear prerequisite chains and timing guidance

**Key Improvement:**
Reduction from 3 top-level assemblies with 30+ scattered topics → 14 goal-oriented jobs with clear implementation paths.

---

## Current Structure (Feature-Based)

**Extracted from AsciiDoc headings using `=` (book), `==` (chapter), `===` (section) hierarchy:**

### Assembly 1: Installing OpenShift Pipelines
= Installing OpenShift Pipelines

==== Installing the {pipelines-title} Operator in web console
- Lines 74-183: Procedure for web console installation
- Profile selection (Lite, Basic, All)
- Update channel selection
- Verification steps

==== Installing the {pipelines-title} Operator by using the CLI
- Lines 188-235: CLI-based installation
- Subscription object creation
- Automatic TektonConfig deployment

==== {pipelines-title} Operator in a restricted environment
- Lines 240-256: Proxy webhook configuration
- Automatic proxy settings for pipeline containers

---

### Assembly 2: Uninstalling OpenShift Pipelines
= Uninstalling OpenShift Pipelines

==== Deleting the {pipelines-shortname} custom resources
- Lines 361-392: CR deletion procedure
- TektonHub, TektonResult, TektonConfig sequencing

==== Uninstalling the {pipelines-title} Operator
- Lines 402-421: Operator removal via web console

==== Deleting the custom resource definitions of the `operator.tekton.dev` group
- Lines 431-449: CRD cleanup for complete removal

---

### Assembly 3: Customizing configurations in the TektonConfig custom resource
= Customizing configurations in the TektonConfig CR

==== Performance tuning using the TektonConfig custom resource
- Lines 541-613: HA mode, buckets, replicas, API query limits

==== Configuring the {pipelines-title} control plane
- Lines 621-668: Metrics, sidecars, service accounts

===== Modifiable fields with default values
- Lines 686-725: Detailed field reference

===== Optional configuration fields
- Lines 737-753: Non-default fields

==== Changing the default service account for {pipelines-shortname}
- Lines 764-784: Service account customization

==== Setting labels and annotations for the {pipelines-shortname} installation namespace
- Lines 794-818: Namespace metadata

==== Setting the resync period for the pipelines controller
- Lines 827-862: Resync period tuning

==== Disabling the service monitor
- Lines 874-892: Metrics disabling

==== Configuring pipeline resolvers
- Lines 903-949: Resolver types and configurations

==== Disabling resolver tasks and pipeline templates
- Lines 958-999: Template disabling

==== Disabling the installation of {tekton-triggers}
- Lines 1009-1027: Triggers disabling

==== Disabling the integration of {tekton-hub}
- Lines 1036-1056: Hub integration disabling

==== Migrating from {tekton-hub} to Artifact Hub
- Lines 1065-1189: Migration procedures
- Assessment scripts
- Resource definition updates
- Private Artifact Hub configuration

==== Disabling the automatic creation of RBAC resources
- Lines 1240-1276: RBAC creation control

==== Disabling inline specification of pipelines and tasks
- Lines 1284-1370: Inline spec enforcement

==== Configuration of RBAC and Trusted CA flags
- Lines 1378-1418: Independent RBAC and CA bundle control

==== Automatic pruning of task runs and pipeline runs
- Lines 1426-1875: Two pruning approaches

===== Configuring the pruner (scheduled/cron-based)
- Lines 1446-1506: Cron schedule, retention policies

===== Annotations for automatically pruning task runs and pipeline runs
- Lines 1516-1554: Namespace-level overrides

===== Enabling the event-driven pruner
- Lines 1563-1643: Event-based pruner setup

===== Configuration of the event-driven pruner
- Lines 1651-1875: TTL, history limits, global/namespace/resource levels

===== Observability metrics of the event-driven pruner
- Lines 1883-1961: OpenTelemetry metrics

==== Setting additional options for webhooks
- Lines 1969-2118: Webhook failure policies, timeouts

---

## Proposed JTBD-Based Structure

**Organized by workflow stages with clean, goal-oriented headings:**

---

## Getting Started with Pipelines

### Job 1: Install the OpenShift Pipelines Operator
**When deploying CI/CD infrastructure to enable pipeline functionality**

**Personas:** Cluster administrator, Platform engineer  
**Prerequisites:** Cluster administrator permissions

**Implementation paths:**

#### Option A: Web Console Installation (for visual configuration)
**Persona:** Cluster administrator preferring GUI  
→ Lines 74-183: Installing the Operator in web console  
Source: Assembly 1, Section 1

**Steps:**
1. Navigate to Operators → OperatorHub
2. Search for "OpenShift Pipelines"
3. Select installation mode (all namespaces)
4. Choose approval strategy (Automatic/Manual)
5. Select update channel (latest or pipelines-\<version\>)

**Benefits:**
- Visual installation progress
- No CLI expertise required
- Immediate feedback on configuration errors

#### Option B: CLI Installation (for infrastructure as code)
**Persona:** Platform engineer managing programmatic deployments  
→ Lines 188-235: Installing the Operator using CLI  
Source: Assembly 1, Section 2

**Steps:**
1. Create Subscription object YAML
2. Apply with `oc apply -f sub.yaml`
3. Operator auto-installs TektonConfig to openshift-pipelines

**Benefits:**
- Version-controlled configuration
- Automation via CI/CD
- Reproducible across clusters

#### Update Channel Selection
→ Lines 117-125: Channel selection guidance  
Source: Assembly 1, Section 1

- `latest` for most recent stable version
- `pipelines-<version>` for specific version control
- Note: preview/stable channels deprecated after OCP 4.10

---

### Job 2: Verify Operator Installation Success
**When installation completes, to confirm all components are ready**

**Personas:** Cluster administrator  
**Prerequisites:** Completed Job 1  
**Timing:** AFTER Job 1 - Web console may show "Succeeded" while components still installing

→ Lines 134-182: Verification procedures  
Source: Assembly 1, Section 1

**Why this matters:** Web console status can show "Succeeded Up to date" even if installation in progress.

**Verification steps:**
1. Check TektonConfig status: `oc get tektonconfig config`
2. Verify READY condition is True
3. Check component versions: `oc get tektonpipeline,tektontrigger,tektonchain,tektonaddon,pac`
4. Confirm all components show Ready: True

**Expected output:**
```
NAME     VERSION   READY   REASON
config   1.22.0    True
```

---

## Set Up & Configure

### Job 3: Optimize Controller Performance
**When managing high-volume pipeline workloads to reduce delays**

**Personas:** Cluster administrator, Platform engineer  
**Prerequisites:** Completed Job 1, understanding of cluster scale

→ Lines 541-613: Performance tuning reference  
Source: Assembly 3, Section 1

#### Enable High-Availability Mode
**For scaling pipeline operations across multiple replicas**

**Configuration via TektonConfig CR:**
```yaml
spec:
  pipeline:
    performance:
      disable-ha: false
      buckets: 7
      replicas: 5
      threads-per-controller: 2
      kube-api-qps: 5.0
      kube-api-burst: 10
```

**Tuning parameters:**
| Parameter | Purpose | Default | Max |
|-----------|---------|---------|-----|
| disable-ha | Enable/disable HA mode | false | - |
| buckets | Operation partitioning | 1 | 10 |
| replicas | Controller pod count | 1 | ≤ buckets |
| threads-per-controller | Workers per controller | 2 | - |
| kube-api-qps | Max queries per second | 5.0 | - |
| kube-api-burst | Throttle burst limit | 10 | - |

**How HA mode works:**
- Without HA: Single pod creates all task/pipeline run pods (delays under high load)
- With HA: Operations distributed across buckets, picked by multiple replicas
- Internal leader election prevents duplicate operations

**Note:** Controller multiplies kube-api-qps and kube-api-burst by 2 internally.

---

### Job 4: Configure Control Plane Settings
**When deploying pipelines in production to tailor execution environment**

**Personas:** Cluster administrator, Platform engineer  
**Prerequisites:** Access to TektonConfig CR

→ Lines 621-668: Control plane configuration  
Source: Assembly 3, Section 2

#### Optimize for Non-Sidecar Environments
**For clusters without Istio or injected sidecars**

→ Lines 686-693: Sidecar configuration

**Configuration:**
```yaml
spec:
  pipeline:
    running-in-environment-with-injected-sidecars: false
    await-sidecar-readiness: false
```

**Benefits:**
- Reduces task run startup time
- Avoids waiting for non-existent sidecars
- Enables pipelines in environments without downwardAPI

**Warning:** Setting to false in clusters WITH injected sidecars causes unexpected behavior.

#### Configure Metrics Collection
→ Lines 686-784: Metrics configuration

**Available settings:**
```yaml
spec:
  pipeline:
    metrics.taskrun.duration-type: histogram  # or gauge
    metrics.pipelinerun.duration-type: histogram
    metrics.taskrun.level: task  # or taskrun, namespace
    metrics.pipelinerun.level: pipeline  # or pipelinerun, namespace
    params:
      - name: enableMetrics
        value: 'true'
```

#### Set Resync Period for Large Clusters
**For clusters with large numbers of pipeline/task runs**

→ Lines 827-862: Resync period tuning  
Source: Assembly 3, Section 6

**Default:** 10 hours  
**Recommended for large clusters:** 24 hours

**Configuration:**
```yaml
spec:
  pipeline:
    options:
      deployments:
        tekton-pipelines-controller:
          spec:
            template:
              spec:
                containers:
                - name: tekton-pipelines-controller
                  args:
                    - "-resync-period=24h"
```

**Why:** Full reconciliation every 10 hours may consume too many resources in large clusters.

---

### Job 6: Manage Pipeline Resource Resolution
**When controlling how pipelines fetch remote resources**

**Personas:** Cluster administrator  
**Prerequisites:** Understanding of resolver types and security implications

→ Lines 903-949: Resolver configuration  
Source: Assembly 3, Section 8

#### Enable or Disable Specific Resolvers

**Available resolver types:**
- `enable-bundles-resolver` - OCI bundle support (Tekton OCI bundles)
- `enable-cluster-resolver` - Cluster-local resources
- `enable-git-resolver` - Git repository resources
- `enable-hub-resolver` - Hub catalog resources

**Configuration:**
```yaml
spec:
  pipeline:
    enable-bundles-resolver: true
    enable-cluster-resolver: true
    enable-git-resolver: true
    enable-hub-resolver: true
```

#### Configure Resolver-Specific Settings

→ Lines 903-949: Per-resolver configurations

**Example:**
```yaml
spec:
  pipeline:
    bundles-resolver-config:
      default-service-account: pipelines
    cluster-resolver-config:
      default-namespace: test
    git-resolver-config:
      server-url: localhost.com
    hub-resolver-config:
      default-tekton-hub-catalog: tekton
      default-artifact-hub-url: "https://artifacthub.io"
```

#### Disable Automatic Template Installation
**For customizing cluster initial state**

→ Lines 958-999: Disabling resolver tasks and templates  
Source: Assembly 3, Section 9

**Configuration:**
```yaml
spec:
  addon:
    params:
      - name: resolverTasks
        value: 'false'
      - name: pipelineTemplates
        value: 'false'
```

**Important:** pipelineTemplates can only be true when resolverTasks is true.

---

### Job 12: Configure Private Artifact Hub
**When operating in disconnected networks to resolve from internal registry**

**Personas:** Cluster administrator  
**Prerequisites:**
- Private Artifact Hub instance deployed
- Network connectivity from resolver pods configured
- TLS certificates for HTTPS endpoints configured
- Authentication configured (if required)
- Catalog names match private hub publications

**Timing:** BEFORE using hub resolver in air-gapped environments

→ Lines 1201-1231: Private Artifact Hub configuration  
Source: Assembly 3, Section 12.3

**Configuration:**
```yaml
spec:
  pipeline:
    hub-resolver-config:
      default-artifact-hub-url: "https://your-private-hub.example.com"
```

**Critical verification steps:**
- Verify network connectivity from resolver pods
- Confirm TLS certificates valid for HTTPS
- Test authentication if required
- Ensure catalog names match private hub

---

### Job 14: Configure Proxy for Restricted Environments
**When operating in air-gapped networks to enable pipeline execution**

**Personas:** Cluster administrator  
**Prerequisites:** Cluster proxy object configured  
**Timing:** AFTER Job 1 - Operator auto-configures proxy webhook

→ Lines 240-256: Restricted environment support  
Source: Assembly 1, Section 3

**How it works:**
1. Operator installs proxy webhook automatically
2. Webhook sets proxy environment variables in pod containers
3. Based on cluster proxy object configuration
4. Sets variables in TektonPipelines, TektonTriggers, Controllers, Webhooks

**To disable proxy for specific namespaces:**
Add label to Namespace object:
```yaml
metadata:
  labels:
    operator.tekton.dev/disable-proxy: "true"
```

**Default:** Proxy disabled for openshift-pipelines namespace.

---

### Job 11: Configure Webhook Behavior
**When customizing admission control to prevent submission delays**

**Personas:** Platform engineer  
**Prerequisites:** Understanding of webhook types (mutating vs validating)

→ Lines 1969-2118: Webhook configuration  
Source: Assembly 3, Section 19

#### View Existing Webhooks

**Mutating webhooks:**
```bash
oc get MutatingWebhookConfiguration
```

**Validating webhooks:**
```bash
oc get ValidatingWebhookConfiguration
```

#### Configure Webhook Options

**Available options:**
- `failurePolicy`: How Kubernetes handles webhook failures (Fail/Ignore)
- `timeoutSeconds`: Webhook timeout (default 10s, max 30s)
- `sideEffects`: Whether webhook has side effects (None/NoneOnDryRun)

**Example for Pipelines controller:**
```yaml
spec:
  pipeline:
    options:
      webhookConfigurationOptions:
        validation.webhook.pipeline.tekton.dev:
          failurePolicy: Fail
          timeoutSeconds: 20
          sideEffects: None
        webhook.pipeline.tekton.dev:
          failurePolicy: Fail
          timeoutSeconds: 20
          sideEffects: None
```

**Also applies to:** Triggers, Pipelines as Code, Tekton Hub controllers

**Note:** Cannot configure operator webhooks.

---

## Secure Your Pipelines

### Job 5: Change Default Service Account
**When enforcing security policies to align with RBAC requirements**

**Personas:** Cluster administrator  
**Prerequisites:** Custom service account with appropriate permissions created  
**Timing:** BEFORE running production pipelines

→ Lines 764-784: Service account configuration  
Source: Assembly 3, Section 4

**Configuration:**
```yaml
spec:
  pipeline:
    default-service-account: pipeline
  trigger:
    default-service-account: pipeline
```

**Applies to:** TaskRun and PipelineRun resources when no service account specified.

---

### Job 9: Disable Automatic RBAC Creation
**When requiring fine-grained permission control to prevent privileged bindings**

**Personas:** Cluster administrator  
**Prerequisites:** Understanding of pipelines-scc security implications

**Why this matters:** Default `pipelines-scc-rolebinding` has RunAsAny SCC privilege, which is a potential security risk.

→ Lines 1240-1276: RBAC disabling procedure  
Source: Assembly 3, Section 15

**Configuration:**
```yaml
spec:
  params:
    - name: createRbacResource
      value: "false"
```

**After disabling:** Manually create namespace-specific RBAC resources as needed.

#### Independent Control of Trusted CA Bundle

→ Lines 1378-1418: RBAC and CA flags  
Source: Assembly 3, Section 16

**Configuration:**
```yaml
spec:
  params:
    - name: createRbacResource
      value: "true"  # Controls RBAC only
    - name: createCABundleConfigMaps
      value: "true"  # Controls Trusted CA bundle separately
```

**Benefits:** Can disable RBAC without affecting Trusted CA bundle config maps.

---

### Job 10: Disable Inline Pipeline Specifications
**When enforcing supply chain security to require version-controlled resources**

**Personas:** Security engineer  
**Prerequisites:** Pipeline and task versioning strategy, resolver configuration  
**Timing:** BEFORE deploying production pipelines

**Why:** Inline specs bypass version control and security scanning.

→ Lines 1284-1370: Inline spec disabling  
Source: Assembly 3, Section 17

**Configuration:**
```yaml
spec:
  pipeline:
    disable-inline-spec: "pipeline,pipelinerun,taskrun"
```

**Enforcement levels:**
| Value | Effect |
|-------|--------|
| `pipeline` | Prevents taskSpec in Pipeline CR, requires taskRef |
| `pipelinerun` | Prevents pipelineSpec in PipelineRun CR, requires pipelineRef |
| `taskrun` | Prevents taskSpec in TaskRun CR, requires taskRef |

**After enabling:** All resources must use `taskRef:` and `pipelineRef:` to reference tasks/pipelines from Task/Pipeline CRs or resolvers.

---

## Migrate Between Catalogs

### Job 7: Migrate from Tekton Hub to Artifact Hub
**When Tekton Hub deprecation affects pipelines to ensure uninterrupted catalog resolution**

**Personas:** Platform engineer  
**Prerequisites:** Inventory of resources using Tekton Hub, Artifact Hub catalog structure knowledge

**Why:** Tekton Hub is deprecated; hub resolver now defaults to Artifact Hub.

→ Lines 1065-1189: Migration guide  
Source: Assembly 3, Sections 11-12

#### Step 1: Assess Migration Impact

→ Lines 1085-1126: Assessment scripts  
Source: Assembly 3, Section 11.1

**Identify resources needing migration:**
```bash
# Count resources by type
echo -e "\nResources needing migration:"
find . -type f \( -name "*.yaml" -o -name "*.yml" \) \
  -exec grep -l "value: tekton\|value: Tekton" {} \; \
  | xargs grep "^kind:" | awk '{print $2}' | sort | uniq -c

# Check cluster hub resolver configuration
echo -e "\nHub resolver configuration:"
kubectl get configmap hubresolver-config -n openshift-pipelines \
  -o jsonpath='{.data.default-type}'
```

**You must migrate if:**
- Resources reference `type: tekton` or `catalog: Tekton`
- Resources use non-semver catalog versions (e.g., "0.8" instead of "0.8.0")
- Hub resolver still configured with `type: tekton`

#### Step 2: Update Resource Definitions

→ Lines 1136-1189: Migration steps  
Source: Assembly 3, Section 11.2

**Migration steps:**
1. **Remove** `type: tekton` parameter (do NOT add `type: artifact` - it's the default)
2. **Update catalog names:**
   - Tasks: `Tekton` → `tekton-catalog-tasks`
   - Pipelines: `Tekton` → `tekton-catalog-pipelines`
   - StepActions: `Tekton` → `tekton-catalog-stepactions`
3. **Update versions** to full semantic versioning (e.g., `0.8` → `0.8.0`)
4. **Reapply** resource definitions

**Before:**
```yaml
params:
  - name: type
    value: tekton            # remove this
  - name: catalog
    value: Tekton            # change to tekton-catalog-tasks
  - name: name
    value: git-clone
  - name: version
    value: "0.8"             # change to 0.8.0
```

**After:**
```yaml
params:
  # type: artifact is the default, omit it
  - name: catalog
    value: tekton-catalog-tasks
  - name: name
    value: git-clone
  - name: version
    value: "0.8.0"
```

#### Step 3: Configure Private Hub (if applicable)

**For disconnected environments:** See Job 12 above.

---

## Operate and Maintain

### Job 8: Automatically Remove Completed Pipeline Runs
**When managing cluster resources over time to prevent exhaustion**

**Personas:** Cluster administrator, Platform engineer, SRE  
**Prerequisites:** Understanding of retention requirements and compliance needs

**Why:** Stale TaskRun and PipelineRun objects consume cluster resources and degrade performance.

→ Lines 1426-1436: Pruning overview  
Source: Assembly 3, Section 17

**Note:** You can configure pruner cluster-wide via TektonConfig, or override per-namespace via annotations. Cannot selectively auto-prune individual runs.

#### Choose Pruning Approach

**Option A: Scheduled (Cron-Based) Pruning**
**For predictable batch cleanup**

→ Lines 1446-1506: Scheduled pruner configuration  
Source: Assembly 3, Section 17.1

**Configuration:**
```yaml
spec:
  pruner:
    resources:
      - taskrun
      - pipelinerun
    keep: 100
    prune-per-resource: false
    schedule: "* 8 * * *"
    startingDeadlineSeconds: 60
```

**Retention policies (mutually exclusive):**
- `keep: 100` - Retain 100 most recent runs of each type
- `keep-since: 7200` - Retain runs from last 7200 minutes (5 days)

**Per-resource pruning:**
- `prune-per-resource: false` - 100 total task runs + 100 total pipeline runs
- `prune-per-resource: true` - 100 per unique pipeline/task (e.g., 100 for Pipeline1, 100 for Pipeline2)

**Namespace-level overrides via annotations:**

→ Lines 1516-1554: Namespace annotations  
Source: Assembly 3, Section 17.2

```yaml
kind: Namespace
metadata:
  annotations:
    operator.tekton.dev/prune.resources: "taskrun, pipelinerun"
    operator.tekton.dev/prune.keep-since: 7200
    operator.tekton.dev/prune.skip: "true"  # to skip namespace
```

**Available annotations:**
- `operator.tekton.dev/prune.schedule`
- `operator.tekton.dev/prune.resources`
- `operator.tekton.dev/prune.keep`
- `operator.tekton.dev/prune.prune-per-resource`
- `operator.tekton.dev/prune.keep-since`
- `operator.tekton.dev/prune.skip`
- `operator.tekton.dev/prune.strategy` (keep or keep-since)

---

**Option B: Event-Driven (Real-Time) Pruning**
**For near real-time cleanup**

→ Lines 1563-1643: Event pruner setup  
Source: Assembly 3, Section 17.3

**Important:** Cannot enable both pruner types simultaneously. Must disable job-based pruner first.

**Configuration:**
```yaml
spec:
  pruner:
    disabled: true
  tektonpruner:
    disabled: false
```

**Verification:**
1. Check tekton-pruner-controller and tekton-pruner-webhook pods running:
   ```bash
   oc get pods -n openshift-pipelines
   ```
2. Verify config maps exist:
   - `tekton-pruner-default-spec` (default pruning behavior)
   - `pruner-info` (runtime data)
   - `config-logging-tekton-pruner` (logging settings)
   - `config-observability-tekton-pruner` (metrics/tracing)

#### Configure Event Pruner Retention

→ Lines 1651-1875: TTL and history limits  
Source: Assembly 3, Section 17.4

**Global configuration:**
```yaml
spec:
  tektonpruner:
    disabled: false
    global-config:
      enforcedConfigLevel: global
      failedHistoryLimit: 5
      historyLimit: 10
      successfulHistoryLimit: 5
      ttlSecondsAfterFinished: 3600
```

**Parameters:**
- `ttlSecondsAfterFinished`: Delete after N seconds
- `historyLimit`: Generic retention count when status-specific limits not defined
- `successfulHistoryLimit`: Retain N successful runs
- `failedHistoryLimit`: Retain N failed runs

**Note:** TTL and history limits operate independently.

**Common TTL values:**
| Environment | TTL (seconds) | Use Case |
|-------------|---------------|----------|
| Dev/testing | 300 (5 min) | Rapid iteration |
| Experiments | 1800 (30 min) | Short-lived experiments |
| CI pipelines | 3600 (1 hour) | CI pipelines |
| Daily builds | 21600 (6 hours) | Daily builds |
| Staging | 86400 (1 day) | Staging environments |
| Production | 604800 (7 days) | Short retention |
| Compliance | 2592000 (30 days) | Auditing |
| Regulated | 7776000 (90 days) | Regulated industries |

**Namespace-level configuration:**
```yaml
spec:
  tektonpruner:
    disabled: false
    global-config:
      enforcedConfigLevel: namespace
      ttlSecondsAfterFinished: 300
      namespaces:
        dev-project:
          ttlSecondsAfterFinished: 60
        staging:
          ttlSecondsAfterFinished: 60
```

**Resource-level configuration via ConfigMap:**
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: tekton-pruner-namespace-spec
  namespace: user-specified-namespace
  labels:
    app.kubernetes.io/part-of: tekton-pruner
    pruner.tekton.dev/config-type: namespace
data:
  ns-config: |
    ttlSecondsAfterFinished: 300
    historyLimit: 5
```

**Required:** ConfigMap MUST be named `tekton-pruner-namespace-spec` with specified labels, or pruner controller ignores it.

**Resource-level with selectors:**
```yaml
data:
  ns-config: |
    ttlSecondsAfterFinished: 3600

    pipelineRuns:
      - selector:
        - matchLabels:
            priority: high
          matchAnnotations:
            compliance: required
        ttlSecondsAfterFinished: 7776000
        successfulHistoryLimit: 100
        failedHistoryLimit: 100
```

**How selectors work:** Rule applies only if resource has both matching labels AND annotations. Non-matching resources fall back to namespace default.

#### Monitor Event Pruner Performance

**For SREs operating event-driven pruner**

→ Lines 1883-1961: Observability metrics  
Source: Assembly 3, Section 17.5

**Available metrics (OpenTelemetry format):**

**Resource processing:**
- `tekton_pruner_controller_resources_processed_total` (Counter)
  - Labels: namespace, resource_type, status
- `tekton_pruner_controller_resources_deleted_total` (Counter)
  - Labels: namespace, resource_type, operation

**Performance timing (Histogram, buckets 0.1s to 30s):**
- `tekton_pruner_controller_reconciliation_duration_seconds`
  - Labels: namespace, resource_type
- `tekton_pruner_controller_ttl_processing_duration_seconds`
- `tekton_pruner_controller_history_processing_duration_seconds`

**State tracking:**
- `kn_workqueue_adds_total` (Counter) - Total resources queued
- `kn_workqueue_depth` (Gauge) - Current items in queue

**Error monitoring:**
- `tekton_pruner_controller_resources_errors_total` (Counter)
  - Labels: namespace, resource_type, reason

**Common labels:**
| Label | Description |
|-------|-------------|
| namespace | Kubernetes namespace of resource |
| resource_type | Tekton resource type |
| status | Outcome of processing |
| operation | Pruning method that deleted resource |
| reason | Specific cause for skip/error |

---

## Decommission Pipelines

### Job 13: Fully Remove OpenShift Pipelines
**When needing to cleanly uninstall to avoid residual resources**

**Personas:** Cluster administrator  
**Prerequisites:** Understanding that uninstallation deletes all pipelines and tasks  
**Timing:** Follow 3-step sequence to avoid conflicts

**Why sequential steps matter:** Skipping CR deletion causes orphaned components that cannot be removed later.

→ Lines 335-393: Uninstallation overview  
Source: Assembly 2

#### Step 1: Delete Custom Resources

**Critical sequencing (MUST follow this order):**

→ Lines 361-392: CR deletion procedure  
Source: Assembly 2, Section 1

1. **Delete TektonHub CRs** (if exist)
2. **Delete TektonResult CRs** (if exist)
3. **Delete TektonConfig CR**

**Via web console:**
1. Navigate to Administration → CustomResourceDefinitions
2. Filter by name: `TektonHub`
3. Click Instances tab
4. If instances exist: Options menu → Delete TektonHub
5. Repeat for `TektonResult`, then `TektonConfig`

**Warnings:**
- ⚠️ Deleting CRs also deletes all Pipelines components, tasks, and pipelines on cluster
- ⚠️ If you uninstall Operator without removing TektonHub and TektonResult CRs, you cannot remove those components later
- Consider backing up pipeline definitions before deletion

#### Step 2: Uninstall the Operator

**After completing Step 1:**

→ Lines 402-421: Operator uninstallation  
Source: Assembly 2, Section 2

**Via web console:**
1. Navigate to Operators → OperatorHub
2. Search for "OpenShift Pipelines"
3. Click Uninstall
4. Select "Delete all operand instances for this operator"
5. Confirm uninstallation

**Warning:** Uninstallation deletes ALL resources in openshift-pipelines namespace, including secrets. Back up secrets if needed.

#### Step 3: Delete Custom Resource Definitions

**For complete cleanup:**

→ Lines 431-449: CRD deletion  
Source: Assembly 2, Section 3

**Via web console:**
1. Navigate to Administration → CustomResourceDefinitions
2. Filter by `operator.tekton.dev`
3. For each displayed CRD:
   - Options menu → Delete CustomResourceDefinition
   - Confirm deletion

**Why this step matters:**
- Ensures no residual CRD definitions remain
- Prevents conflicts during future installations
- Provides clean slate for potential reinstallation

---

## Key Differences

### Current Structure (Feature-Based)

**Organized By:** Lifecycle phases (Installing, Uninstalling, Customizing) and technical features  
**Navigation:** 3 assemblies with 30+ scattered modules  
**User Journey:** Linear reading, chapter by chapter  
**Content Organization:**
- Installation methods in separate sections
- Configuration topics scattered across 20+ sections
- No clear workflow progression
- Pruning split across 5 subsections

**Example fragmentation:**
- Performance tuning: Section 1
- Control plane config: Section 2
- Resync period: Section 6
- Service account: Section 4
- All related to "configuring production environment" but scattered

### Proposed Structure (JTBD-Based)

**Organized By:** Workflow stages (Get Started, Configure, Secure, Migrate, Operate, Conclude) and user goals  
**Navigation:** 14 main jobs with clear implementation paths  
**User Journey:** Goal-directed, choose your approach  
**Content Organization:**
- Multiple paths per job (UI vs CLI, scheduled vs event-driven)
- Configuration topics consolidated under goal headings
- Clear prerequisite chains and timing guidance
- Related topics grouped by goal (e.g., all "production configuration" under Jobs 3-4)

**Example consolidation:**
- Job 4: Configure Control Plane Settings
  - Sidecar optimization
  - Metrics configuration
  - Resync period tuning
  - All in one goal-oriented section

---

## Hierarchy Levels Comparison

### Current Structure Depth

**3 levels:**
1. Assembly (= in AsciiDoc)
2. Section (==== in AsciiDoc)
3. Subsection (===== in AsciiDoc)

**Example:**
```
= Assembly: Customizing configurations in the TektonConfig CR
  ==== Section: Automatic pruning of task runs and pipeline runs
    ===== Subsection: Configuring the pruner
    ===== Subsection: Annotations for pruning
    ===== Subsection: Enabling event-driven pruner
    ===== Subsection: Configuration of event-driven pruner
    ===== Subsection: Observability metrics
```

**Issues:**
- 5 subsections for pruning scattered across hierarchy
- No clear guidance on "scheduled vs event-driven" choice
- User must read all 5 sections to understand options

### Proposed Structure Depth

**3 levels:**
1. Main Job (stable goal)
2. User Story/Option (implementation path)
3. Procedure reference (line numbers from source)

**Example:**
```
Job 8: Automatically Remove Completed Pipeline Runs
  Option A: Scheduled (Cron-Based) Pruning
    → Lines 1446-1506: Scheduled pruner configuration
    → Lines 1516-1554: Namespace annotations
  Option B: Event-Driven (Real-Time) Pruning
    → Lines 1563-1643: Event pruner setup
    → Lines 1651-1875: TTL and history limits
    → Lines 1883-1961: Observability metrics
```

**Benefits:**
- Clear choice between two approaches
- Related content grouped under option
- Prerequisites and timing guidance explicit
- User sees full picture in one job

---

## Example Consolidations

### Example 1: Installation Methods

**Current (Fragmented):**
```
= Assembly: Installing OpenShift Pipelines
  ==== Section: Installing the Operator in web console
    Lines 74-183: Web console procedure
  ==== Section: Installing the Operator using the CLI
    Lines 188-235: CLI procedure
```

**Issues:**
- Two separate sections for same job
- No guidance on when to use which method
- User must read both to compare

**Proposed (Consolidated):**
```
Job 1: Install the OpenShift Pipelines Operator
  Option A: Web Console Installation (for visual configuration)
    → Lines 74-183: Installing the Operator in web console
    Benefits: Visual progress, no CLI expertise required
  
  Option B: CLI Installation (for infrastructure as code)
    → Lines 188-235: Installing the Operator using CLI
    Benefits: Version control, automation, reproducible
```

**Benefit:** One place to learn installation with clear choice guidance!

---

### Example 2: Pruning Configuration

**Current (Fragmented):**
```
= Assembly: Customizing configurations
  ==== Section: Automatic pruning
    ===== Configuring the pruner (lines 1446-1506)
    ===== Annotations for pruning (lines 1516-1554)
    ===== Enabling event-driven pruner (lines 1563-1643)
    ===== Configuration of event-driven pruner (lines 1651-1875)
    ===== Observability metrics (lines 1883-1961)
```

**Issues:**
- 5 separate subsections for same goal
- No clear "choose A or B" guidance
- User must read all 5 to understand they're mutually exclusive
- Scheduled vs event-driven choice not explicit

**Proposed (Consolidated):**
```
Job 8: Automatically Remove Completed Pipeline Runs
  
  Choose Pruning Approach:
  
  Option A: Scheduled (Cron-Based) Pruning
    → Lines 1446-1506: Scheduled pruner configuration
    → Lines 1516-1554: Namespace annotations
    For: Predictable batch cleanup
  
  Option B: Event-Driven (Real-Time) Pruning
    → Lines 1563-1643: Event pruner setup
    → Lines 1651-1875: TTL and history limits
    → Lines 1883-1961: Observability metrics
    For: Near real-time cleanup
  
  Important: Cannot enable both simultaneously
```

**Benefit:** User immediately sees two approaches, when to use each, and that they're mutually exclusive!

---

### Example 3: Production Configuration

**Current (Scattered):**
```
= Assembly: Customizing configurations
  ==== Section 1: Performance tuning (lines 541-613)
  ==== Section 2: Configuring control plane (lines 621-668)
  ==== Section 4: Changing default service account (lines 764-784)
  ==== Section 6: Setting resync period (lines 827-862)
  ==== Section 7: Disabling service monitor (lines 874-892)
```

**Issues:**
- 5 separate sections for "configuring production environment"
- User doesn't know these are related
- No guidance on which to configure when
- Scattered across sections 1, 2, 4, 6, 7

**Proposed (Consolidated):**
```
Job 3: Optimize Controller Performance
  → Lines 541-613: HA mode, buckets, replicas

Job 4: Configure Control Plane Settings
  Optimize for Non-Sidecar Environments
    → Lines 686-693: Sidecar configuration
  
  Configure Metrics Collection
    → Lines 686-784: Metrics settings
  
  Set Resync Period for Large Clusters
    → Lines 827-862: Resync period tuning
  
  Disable Service Monitor (if needed)
    → Lines 874-892: Metrics disabling

Job 5: Change Default Service Account
  → Lines 764-784: Service account configuration
```

**Benefit:** Related production configuration topics grouped by goal with clear prerequisites!

---

## Navigation Improvement Metrics

### Quantified Improvements

**Top-Level Navigation:**
- **Current:** 3 assemblies → user must browse all to find content
- **Proposed:** 7 workflow stage sections → direct navigation to goal
- **Reduction:** 57% fewer mental categories to navigate

**Content Depth:**
- **Current:** 30+ modules across 3 assemblies
- **Proposed:** 14 main jobs with 2-5 options each
- **Reduction:** 53% fewer top-level items

**Pruning Example:**
- **Current:** 5 subsections to read to understand options
- **Proposed:** 1 job with 2 clear options
- **Reduction:** From 5 sections → 2 options (60% reduction in navigation)

**Installation Example:**
- **Current:** 2 separate sections (user must find and compare)
- **Proposed:** 1 job with 2 options side-by-side
- **Benefit:** Find content in 2 clicks (Job 1 → Option A/B) vs 4 clicks (Assembly → Section → Read → Compare)

**Migration Example:**
- **Current:** 4 subsections (Assess, Migrate, Configure Private Hub, scattered)
- **Proposed:** 1 job with 3 sequential steps
- **Benefit:** Clear 3-step workflow vs scattered 4-subsection reading

---

## Workflow Coverage Comparison

| Stage | Current Structure | Proposed Structure | Gap Status |
|-------|-------------------|-------------------|------------|
| **Get Started** | ⚠️ Scattered across Assembly 1 | ✅ Jobs 1-2 (Install, Verify) | **Improved** - Consolidated |
| **Configure** | ⚠️ Scattered across Assembly 3 (20+ sections) | ✅ Jobs 3, 4, 6, 11, 12, 14 | **Improved** - Organized by goal |
| **Secure** | ⚠️ Buried in Assembly 3 (sections 4, 15, 17) | ✅ Jobs 5, 9, 10 | **Improved** - Elevated visibility |
| **Migrate** | ⚠️ Subsection in Assembly 3 (section 11) | ✅ Job 7 (Tekton Hub → Artifact Hub) | **Improved** - Dedicated job |
| **Operate** | ⚠️ Scattered in Assembly 3 (section 17, 5 subsections) | ✅ Job 8 (Automatic Pruning) | **Improved** - Consolidated |
| **Monitor** | ⚠️ Buried in pruning subsection only | ✅ Job 8 (Event Pruner Metrics) | **Improved** - Part of operate job |
| **Conclude** | ✅ Assembly 2 (Uninstalling) | ✅ Job 13 (Fully Remove) | **Maintained** - Clear 3-step sequence |
| **Troubleshoot** | ❌ Missing | ❌ Missing | **Gap remains** |
| **Upgrade** | ⚠️ Update channel selection only | ⚠️ Update channel selection (Job 1) | **Gap remains** - No upgrade procedures |

### Coverage Indicators

| Symbol | Meaning |
|--------|---------|
| ✅ | Stage fully covered with dedicated content |
| ⚠️ | Partial coverage - content exists but scattered or limited |
| ❌ | Stage not covered - content gap identified |

### Coverage Summary

**Current structure gaps:**
- ❌ Troubleshoot: No troubleshooting workflows (webhook failures, installation issues)
- ⚠️ Upgrade: Only update channel selection, no upgrade procedures
- ⚠️ Configure: Scattered across 20+ sections
- ⚠️ Secure: Buried in configuration sections
- ⚠️ Operate: Fragmented across 5 pruning subsections

**Proposed structure improvements:**
- ✅ Get Started: Consolidated Jobs 1-2
- ✅ Configure: Organized into Jobs 3, 4, 6, 11, 12, 14
- ✅ Secure: Elevated to dedicated Jobs 5, 9, 10
- ✅ Migrate: Dedicated Job 7 with clear 3-step workflow
- ✅ Operate: Consolidated Job 8 with clear option choice
- ✅ Monitor: Embedded in Job 8 (event pruner metrics)
- ✅ Conclude: Clear 3-step sequence in Job 13

**Gaps addressed by restructure:**
- Configure: From 20+ scattered sections → 6 goal-oriented jobs
- Secure: From buried subsections → 3 visible jobs
- Operate: From 5 fragmented subsections → 1 consolidated job with 2 options

**Gaps remaining:**
- ❌ Troubleshoot: No troubleshooting content (not addressed by restructure)
- ⚠️ Upgrade: No upgrade procedures beyond channel selection (not addressed)

### Recommendations for Gap Closure

| Gap | Recommendation | Priority | Source |
|-----|----------------|----------|--------|
| **Troubleshoot** | Add troubleshooting job covering:<br>- Webhook timeout errors<br>- Installation verification failures<br>- Component readiness issues<br>- Proxy configuration problems | **High** | Common user questions |
| **Upgrade** | Add upgrade procedures job covering:<br>- Pre-upgrade checklist<br>- Upgrade process via OLM<br>- Post-upgrade verification<br>- Rollback procedures | **Medium** | Gap in lifecycle coverage |
| **Monitor** | Expand monitoring beyond pruner:<br>- Pipeline execution metrics<br>- Controller performance metrics<br>- Resource consumption dashboards | **Low** | Currently limited to pruner only |

---

## Document Statistics

### Source Content Analysis

**Source Documents:**
- Combined AsciiDoc: `install_config-combined.adoc` (2,126 lines)
- JTBD Records: `install_config-jtbd.jsonl` (30 records)
- Proposed TOC: `install_config-toc-new_taxonomy.md`

**Current Structure:**
- Assemblies: 3
- Modules: 30+
- Workflow stages covered: 5 (scattered)

**Proposed Structure:**
- Main Jobs: 14
- Workflow stages: 7 (organized)
- Implementation paths: 22 (multiple options per job)
- Personas: 4 (Cluster administrator, Platform engineer, Security engineer, SRE)

### Consolidation Metrics

**Installation (Job 1):**
- Current: 2 separate sections
- Proposed: 1 job with 2 options
- Consolidation: 2 → 1 (50% reduction)

**Configuration (Jobs 3-4, 6, 11, 12, 14):**
- Current: 20+ scattered sections
- Proposed: 6 goal-oriented jobs
- Consolidation: 20 → 6 (70% reduction)

**Pruning (Job 8):**
- Current: 5 subsections
- Proposed: 1 job with 2 options
- Consolidation: 5 → 2 (60% reduction in navigation)

**Security (Jobs 5, 9, 10):**
- Current: Buried in 3 different sections
- Proposed: 3 visible jobs under "Secure" stage
- Improvement: Elevated visibility, dedicated stage

**Uninstallation (Job 13):**
- Current: 3 sections
- Proposed: 1 job with 3 sequential steps
- Consolidation: 3 → 1 (maintained sequence clarity)

### Overall Reduction

**Total top-level items:**
- Current: 30+ modules across 3 assemblies
- Proposed: 14 main jobs across 7 stages
- **Reduction: 53%**

**Navigation depth to find content:**
- Current: 4-6 clicks (Assembly → Section → Subsection → Read → Compare)
- Proposed: 2-3 clicks (Stage → Job → Option)
- **Reduction: 50%**

---

## Appendices

### A. Installation Method Comparison

| Method | Best For | Pros | Cons | Job Reference |
|--------|----------|------|------|---------------|
| **Web Console** | Cluster administrators preferring GUI | Visual configuration, installation progress visibility, immediate error feedback | Requires web console access, less automation-friendly | Job 1, Option A |
| **CLI (YAML)** | Platform engineers, IaC workflows | Automation via CI/CD, version-controlled config, reproducible across clusters | Requires CLI expertise, less visibility into progress | Job 1, Option B |

### B. Pruning Approach Selection Guide

| Factor | Scheduled (Cron) | Event-Driven (Real-Time) |
|--------|------------------|--------------------------|
| **Cleanup timing** | Batch at scheduled intervals (e.g., daily at 8am) | Immediate after completion |
| **Configuration complexity** | Simpler (cron schedule + retention policy) | More complex (TTL + history limits + enforcement levels) |
| **Resource spikes** | May cause spikes during batch processing | Distributed load across completions |
| **Observability** | Limited (cron job status only) | Rich metrics via OpenTelemetry (reconciliation time, error rates, queue depth) |
| **Use cases** | Predictable cleanup cycles, simpler requirements | Compliance with tight retention, resource-constrained clusters |
| **Namespace customization** | Annotations only | Annotations + ConfigMaps + selectors (most flexible) |
| **Mutual exclusivity** | Cannot coexist with event-driven | Cannot coexist with scheduled |
| **Controllers** | Single pruner cron job | tekton-pruner-controller + tekton-pruner-webhook pods |
| **Config location** | TektonConfig spec.pruner | TektonConfig spec.tektonpruner + ConfigMaps |

### C. Workflow Coverage Analysis by Persona

#### Cluster Administrator Journey

**New installation path:**
1. Job 1: Install Operator (Web Console method)
2. Job 2: Verify Installation
3. Job 5: Change Default Service Account
4. Job 9: Disable Automatic RBAC (security hardening)
5. Job 8: Configure Scheduled Pruning (simpler approach)

**Coverage:** Get Started ✅, Configure ✅, Secure ✅, Operate ✅

#### Platform Engineer Journey

**Production hardening path:**
1. Job 1: Install Operator (CLI method for IaC)
2. Job 3: Optimize Controller Performance (HA mode)
3. Job 4: Configure Control Plane (metrics, sidecars, resync period)
4. Job 6: Configure Resolvers
5. Job 11: Configure Webhooks
6. Job 8: Configure Event-Driven Pruning (more control)

**Coverage:** Get Started ✅, Configure ✅, Operate ✅

#### Security Engineer Journey

**Compliance setup path:**
1. Job 5: Change Default Service Account
2. Job 9: Disable Automatic RBAC (prevent RunAsAny SCC)
3. Job 10: Disable Inline Specs (enforce version control)
4. Job 8: Configure Event-Driven Pruning with compliance TTL (90 days)

**Coverage:** Secure ✅, Operate ✅

#### SRE Journey (Disconnected Environment)

**Air-gapped deployment path:**
1. Job 14: Configure Proxy Settings (automatic via cluster proxy)
2. Job 12: Configure Private Artifact Hub
3. Job 7: Migrate to Artifact Hub (private instance)
4. Job 8: Configure Event-Driven Pruning with monitoring

**Coverage:** Configure ✅, Migrate ✅, Operate ✅, Monitor ✅

### D. Persona Journey Coverage Summary

| Persona | Stages Covered | Gaps |
|---------|---------------|------|
| **Cluster Administrator** | Get Started, Configure, Secure, Operate | Troubleshoot, Upgrade |
| **Platform Engineer** | Get Started, Configure, Operate | Troubleshoot, Upgrade |
| **Security Engineer** | Secure, Operate | Get Started (assumes installed), Troubleshoot |
| **SRE** | Configure, Migrate, Operate, Monitor | Get Started (assumes installed), Troubleshoot |

**Common gaps across all personas:** Troubleshoot, Upgrade

### E. Implementation Path Summary

**14 main jobs with 22 implementation paths:**

| Job | Implementation Paths | Path Type |
|-----|---------------------|-----------|
| 1 | Web Console, CLI | Persona-based (GUI vs IaC) |
| 2 | Single path (verification) | - |
| 3 | HA mode configuration | Single path |
| 4 | Sidecars, metrics, resync period | Multi-topic (3 configurations) |
| 5 | Single path (service account) | - |
| 6 | Enable/disable resolvers, templates | Multi-topic (2 configurations) |
| 7 | Assess, update definitions, private hub | Sequential (3 steps) |
| 8 | Scheduled, Event-driven | Approach-based (mutually exclusive) |
| 9 | Single path (RBAC disabling) | - |
| 10 | Single path (inline spec disabling) | - |
| 11 | Single path (webhook config) | - |
| 12 | Single path (private hub) | - |
| 13 | Delete CRs, uninstall operator, delete CRDs | Sequential (3 steps) |
| 14 | Single path (proxy config) | - |

**Path types:**
- Persona-based: 1 (Job 1: UI vs CLI)
- Approach-based: 1 (Job 8: Scheduled vs Event-driven)
- Multi-topic: 2 (Jobs 4, 6: Multiple related configurations)
- Sequential: 2 (Jobs 7, 13: Step-by-step workflows)
- Single path: 8 (Jobs 2, 3, 5, 9, 10, 11, 12, 14)

---

## Conclusion

The proposed JTBD-based structure consolidates 30+ scattered modules into 14 goal-oriented jobs, reducing top-level navigation by 53% and organizing content by workflow stages for improved findability.

**Key improvements:**
1. **Consolidation:** Related topics grouped by goal (e.g., all production configuration under Jobs 3-4)
2. **Clear choices:** Multiple implementation paths presented side-by-side (UI vs CLI, scheduled vs event-driven)
3. **Prerequisite chains:** Explicit timing and sequencing (Job 1 → Job 2 → Jobs 3-14)
4. **Workflow progression:** Natural flow from Get Started → Configure → Secure → Migrate → Operate → Conclude
5. **Elevated security:** Security jobs visible under dedicated "Secure" stage vs buried in configuration

**Remaining gaps:** Troubleshoot and Upgrade stages require new content (not addressed by restructure alone).

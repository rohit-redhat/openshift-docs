# Using Tekton Results for OpenShift Pipelines Observability
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** Enable platform engineers to archive pipeline run information and access complete manifests and logs after pruning resources.

**Personas:** Platform engineer

**Main Jobs:** 4 core jobs across 4 workflow stages

---

## Quick Navigation

**I want to:**
- Understand how Tekton Results works -> Job 1 (Get Started)
- Configure logging forwarding -> Job 2 (Configure)
- Set up external database -> Job 2 (Configure)
- Configure retention policy -> Job 2 (Configure)
- Query archived runs by UUID -> Job 3 (Observe)
- Query archived runs by name -> Job 4 (Observe)
- Monitor Tekton Results performance -> Job 5 (Monitor)

---

# Table of Contents

## Getting Started

### Job 1: Understand Tekton Results Architecture
*When I need to understand how pipeline runs and task runs are archived*

**Personas:** Platform engineer

#### Core Concepts

→ Lines 73-245: Tekton Results concepts
  Source: Main content, Conceptual section

- **Results and Records Data Model**
  - Results contain one or more records
  - Each pipeline run creates a result
  - Result includes records for PipelineRun and all TaskRuns
  - Standalone task runs create their own results
  
- **Naming Conventions**
  - Result name format: `<namespace>/results/<parent_run_uuid>`
  - Record name format: `<namespace>/results/<parent_run_uuid>/records/<run_uuid>`
  
- **YAML Manifest Preservation**
  - Records preserve complete YAML manifests after run completion
  - Manifests include specifications, annotations, and status information
  - Access retained after pruning original resources

---

## Set Up & Configure

### Job 2: Configure Tekton Results for Production Use
*When I need production-ready Tekton Results with logging and optional settings*

**Personas:** Platform engineer

**Timing:** BEFORE deploying production pipelines - log forwarding cannot be enabled retroactively for completed runs

#### 2.1 Configure LokiStack Forwarding for Logs

**Goal:** Enable long-term access to task run logs after resource deletion.

→ Lines 273-395: Configuring LokiStack forwarding for logging information
  Source: Configuration section

**Prerequisites:** LokiStack and OpenShift Logging installed

- **Task:** Install LokiStack and OpenShift Logging Operator
  - Cluster administrator access required
  
- **Task:** Create ClusterLogForwarder CR
  - Different manifests for OpenShift Logging v5 vs v6
  - Configure selector to match tekton-pipelines managed resources
  - Set up forwarding pipeline to default-lokistack output
  
- **Task:** Configure TektonConfig CR
  - Set `loki_stack_name` (typically `logging-loki`)
  - Set `loki_stack_namespace` (typically `openshift-logging`)

**Context:** Without LokiStack forwarding, Tekton Results does not store or provide log information via CLI or API.

#### 2.2 Configure External Database Server

**Goal:** Replace default internal PostgreSQL with production-grade database.

→ Lines 404-451: Configuring an external database server
  Source: Configuration section

**Why:** Default internal PostgreSQL lacks automated backups, performance tuning, and storage lifecycle management capabilities needed for production.

- **Task:** Create Secret with Database Credentials
  - Namespace: `openshift-pipelines`
  - Include `POSTGRES_USER` and `POSTGRES_PASSWORD`
  
- **Task:** Edit TektonConfig CR
  - Set `is_external_db: true`
  - Configure `db_host` (PostgreSQL server hostname)
  - Configure `db_port` (PostgreSQL server port)

#### 2.3 Configure Retention Policy

**Goal:** Prevent unnecessary storage use and database performance degradation.

→ Lines 461-497: Configuring the retention policy for Tekton Results
  Source: Configuration section

**Context:** Default retention is indefinite, leading to resource consumption over time.

- **Task:** Edit TektonConfig CR retention policy settings
  - `runAt` - Cron format schedule for pruning job (e.g., "3 5 * * 0" for Sunday at 5:03 AM)
  - `maxRetention` - Days to retain data (e.g., "30" for 30-day retention)

---

## Observe System State

### Job 3: Access Archived Pipeline and Task Run Information (UUID-Based Queries)
*When I need to retrieve archived information using universally unique identifiers*

**Personas:** Platform engineer

**Prerequisites:** opc utility installed, OpenShift cluster access, Tekton Results API token created

#### 3.1 Prepare opc Utility Environment

**Goal:** Configure authentication for Tekton Results API access.

→ Lines 628-680: Preparing the opc utility environment for querying Tekton Results
  Source: Querying section

- **Task:** Set RESULTS_API Environment Variable
  ```bash
  export RESULTS_API=$(oc get route tekton-results-api-service -n openshift-pipelines --no-headers -o custom-columns=":spec.host"):443
  ```
  
- **Task:** Create Authentication Token
  ```bash
  oc create token <service_account>
  ```
  Service account requires read access to pipeline namespaces.
  
- **Task:** Optional - Create ~/.config/tkn/results.yaml for Automatic Authentication
  - Configure `address`, `token`, `ssl.roots_file_path`, `ssl.server_name_override`, `service_account`

#### 3.2 Query Results and Records by Name

**Goal:** List and retrieve results using their names.

→ Lines 689-783: Querying for results and records by name
  Source: Querying section

**Prerequisites:** jq package installed, LokiStack configured (for log queries)

- **Task:** List All Results in Namespace
  ```bash
  opc results result list --addr ${RESULTS_API} <namespace_name>
  ```
  
- **Task:** List All Records in a Result
  ```bash
  opc results records list --addr ${RESULTS_API} <result_name>
  ```
  
- **Task:** Retrieve YAML Manifest from Record
  ```bash
  opc results records get --addr ${RESULTS_API} <record_name> | jq -r .data.value | base64 -d | xargs -0 python3 -c 'import sys, yaml, json; j=json.loads(sys.argv[1]); print(yaml.safe_dump(j))'
  ```
  
- **Task:** Retrieve Logs from Record
  ```bash
  opc results logs get --addr ${RESULTS_API} <log_record_name> | jq -r .data | base64 -d
  ```
  Replace `records` with `logs` in record name to get log record name.

#### 3.3 Search for Results Using CEL Queries

**Goal:** Find results by specific criteria using Common Expression Language queries.

→ Lines 792-824: Searching for results
  Source: Querying section

**Context:** Most relevant information is in record objects, not result objects. Use record searches for detailed queries.

- **Common Search Examples:**
  - Failed runs: `!(summary.status == SUCCESS)`
  - Runs with specific annotations: `summary.annotations.contains('ann1') && summary.annotations.contains('ann2') && summary.type=='PIPELINE_RUN'`

→ Lines 910-953: Reference information for searching results
  Source: Reference section

**Available CEL Fields:**
- `parent` - Namespace
- `uid` - Result unique identifier
- `annotations` - Annotations on PipelineRun/TaskRun CR
- `summary` - Result summary
- `create_time` - Result creation time
- `update_time` - Result last update time
- `summary.status` - Values: UNKNOWN, SUCCESS, FAILURE, TIMEOUT, CANCELLED

#### 3.4 Search for Records Using CEL Queries

**Goal:** Find pipeline runs or task runs by detailed criteria including YAML manifest data.

→ Lines 833-901: Searching for records
  Source: Querying section

**Context:** Records contain full YAML manifests allowing rich filtering by names, completion times, pipeline associations, and any YAML data element.

- **Common Search Examples:**
  - Failed runs: `!(data.status.conditions[0].status == 'True')`
  - TaskRun/PipelineRun named 'run1': `data.metadata.name == 'run1'`
  - Task runs for specific pipeline run: `data_type == 'TASK_RUN' && data.metadata.labels['tekton.dev/pipelineRun'] == 'run1'`
  - Runs associated with pipeline: `data.metadata.labels['tekton.dev/pipeline'] == 'pipeline1'`
  - Runs by duration: `data.status.completionTime - data.status.startTime > duration('5m') && data_type == 'PIPELINE_RUN'`
  - Runs by completion date: `data.status.completionTime.getDate() == 7 && data.status.completionTime.getMonth() == 10 && data.status.completionTime.getFullYear() == 2023`
  - Runs by task count: `size(data.status.pipelineSpec.tasks) >= 3 && data_type == 'PIPELINE_RUN'`
  - Runs with annotations: `data.metadata.annotations.contains('ann1') && data_type == 'PIPELINE_RUN'`

→ Lines 962-989: Reference information for searching records
  Source: Reference section

**Available CEL Fields:**
- `name` - Record name
- `data_type` - Values: `tekton.dev/v1.TaskRun` or `TASK_RUN`, `tekton.dev/v1.PipelineRun` or `PIPELINE_RUN`, `results.tekton.dev/v1alpha2.Log`
- `data` - Entire YAML manifest (can query any YAML element, e.g., `data.status.completionTime`)

---

### Job 4: Access Archived Information by Pipeline Run and Task Run Names (Technology Preview)
*When I need to query archived information using familiar run names instead of UUIDs*

**Personas:** Platform engineer

**Context:** Technology Preview feature requiring different opc configuration than UUID-based queries.

**Prerequisites:** opc utility installed, OpenShift cluster access

#### 4.1 Configure opc Utility for Name-Based Queries

**Goal:** Set up authentication configuration for name-based querying.

→ Lines 1035-1099: Configuring the opc utility for querying results by pipeline run and task run names
  Source: Name-based querying section

- **Task:** Create Authentication Token
  ```bash
  oc create token <service_account>
  ```
  
- **Task:** Configure opc Interactively
  ```bash
  opc results config set
  ```
  Reply to prompts, provide authentication token.
  
- **Task:** Configure opc from Command Line
  ```bash
  opc results config set --host="https://tekton-results.example.com" --token="<token>"
  ```
  
- **Verification:** View configuration
  ```bash
  opc results config view
  ```

#### 4.2 View List of Pipeline Run Names

**Goal:** Discover available pipeline runs for detailed queries.

→ Lines 1108-1156: Viewing a list of pipeline run names and identifiers
  Source: Name-based querying section

- **Task:** List All Pipeline Runs in Namespace
  ```bash
  opc results pipelinerun list -n <namespace_name>
  ```
  - Optional: `--limit=10` - Display specified number of lines
  - Optional: `--single-page=false` - Prompt to continue after limit
  - Optional: `--labels="key=value,key2=value2"` - Filter by labels/annotations
  
- **Task:** List Pipeline Runs for Named Pipeline
  ```bash
  opc results pipelinerun list <pipeline_name> -n <namespace_name>
  ```
  Shows runs for pipelines with names containing `<pipeline_name>`.

#### 4.3 View List of Task Run Names

**Goal:** Discover available task runs for detailed queries.

→ Lines 1165-1220: Viewing a list of task run names and identifiers
  Source: Name-based querying section

- **Task:** List All Task Runs in Namespace
  ```bash
  opc results taskrun list -n <namespace_name>
  ```
  - Optional: `--limit`, `--single-page=false`, `--labels` parameters
  
- **Task:** List Task Runs for Specific Pipeline Run
  ```bash
  opc results taskrun list --pipelinerun <pipelinerun_name> -n <namespace_name>
  ```

#### 4.4 View Pipeline Run Results

**Goal:** Retrieve detailed information about completed pipeline run.

→ Lines 1231-1328: Viewing result information for a pipeline run
  Source: Name-based querying section

- **Task:** Describe Pipeline Run (by name or UUID)
  ```bash
  opc results pipelinerun describe -n <namespace_name> <pipelinerun_name>
  ```
  or
  ```bash
  opc results pipelinerun describe -n <namespace_name> --uid <pipelinerun_uuid>
  ```
  Shows status, params, workspaces, task runs.
  
- **Task:** View Full YAML Manifest
  ```bash
  opc results pipelinerun describe -n <namespace_name> --output yaml <pipelinerun_name>
  ```
  
- **Task:** View Pipeline Run Logs
  ```bash
  opc results pipelinerun logs -n <namespace_name> <pipelinerun_name>
  ```
  
  **Context:** Pipeline run logs exclude task run logs. Query task runs separately using `opc results taskrun list --pipelinerun` to get names, then `opc results taskrun logs`.

#### 4.5 View Task Run Results

**Goal:** Retrieve detailed information about completed task run.

→ Lines 1337-1418: Viewing result information for a task run
  Source: Name-based querying section

**Prerequisites:** LokiStack configured for log retrieval

- **Task:** Describe Task Run (by name or UUID)
  ```bash
  opc results taskrun describe -n <namespace_name> <taskrun_name>
  ```
  or
  ```bash
  opc results taskrun describe -n <namespace_name> --uid <taskrun_uuid>
  ```
  Shows status and params.
  
- **Task:** View Full YAML Manifest
  ```bash
  opc results taskrun describe -n <namespace_name> --output yaml <taskrun_name>
  ```
  
- **Task:** View Task Run Logs
  ```bash
  opc results taskrun logs -n <namespace_name> <taskrun_name>
  ```

---

## Track Performance

### Job 5: Monitor Tekton Results Health and Performance
*When I need to monitor storage and deletion operations performance*

**Personas:** Platform engineer

**Prerequisites:** ServiceMonitor resources configured for Tekton Results, Prometheus Operator installed

→ Lines 506-600: Observability metrics for Tekton Results
  Source: Observability section

#### Metrics Exposure

**Endpoint:** tekton-results-watcher service, port 9090, /metrics path

**Available Metrics Categories:**
1. Storage performance
2. Storage failures
3. Deletion duration
4. Deletion count

#### Metric Labels

All metrics use labels for filtering:
- `kind` - Resource type: pipelinerun or taskrun
- `namespace` - Kubernetes namespace
- `pipeline` - Pipeline name (optional)
- `status` - Completion status
- `task` - Task name (optional, TaskRuns only)
- `taskrun` - TaskRun name (optional, TaskRuns only)

#### Storage Performance Metrics

**Metric:** `watcher_run_storage_latency_seconds` (Histogram)
- Description: Duration between run completion and successful storage
- Labels: kind, namespace
- Buckets: 0.1, 0.5, 1, 2, 5, 10, 30, 60, 120, 300, 600, 1800 seconds

**Context:** Tracks latency only when watcher stores run after completion. With `DisableStoringIncompleteRuns` set to false, watcher stores before completion but only records latency at final storage.

#### Storage Failure Metrics

**Metric:** `runs_not_stored_count` (Counter)
- Description: Total runs deleted without successful storage
- Labels: kind, namespace

**Context:** May show inflated values in rare cases due to multiple reconciliation attempts or incomplete deletion.

#### Deletion Duration Metrics

**Metrics:**
- `watcher_pipelinerun_delete_duration_seconds` (Histogram)
  - Labels: pipeline, status, namespace
- `watcher_taskrun_delete_duration_seconds` (Histogram)
  - Labels: pipeline, status, task, taskrun, namespace

#### Deletion Count Metrics

**Metrics:**
- `watcher_pipelinerun_delete_count` (Counter)
  - Labels: status, namespace
- `watcher_taskrun_delete_count` (Counter)
  - Labels: status, namespace

---

## Reference

### Command-Line Short Names

→ Lines 1427-1446: Short names for command-line arguments
  Source: Reference section

| Full Parameter Name | Short Parameter Name |
|---------------------|---------------------|
| pipelinerun | pr |
| taskrun | tr |
| describe | desc |

---

## Appendices

### A. Query Method Decision Guide

| Method | Best For | Complexity | Configuration |
|--------|----------|------------|---------------|
| UUID-based queries (Job 3) | Production use, stable workflows | Low | Results API environment variable + token |
| Name-based queries (Job 4) | Development, familiar naming | Medium | opc config set with host + token |

**Choose based on:**
- **UUID-based:** Production systems, automation, stable API access
- **Name-based:** Development workflows, interactive use, Technology Preview evaluation

### B. Workflow Coverage Analysis

| Stage | Coverage | Jobs | Notes |
|-------|----------|------|-------|
| Get Started | ✅ | Job 1 | Conceptual understanding |
| Configure | ✅ | Job 2 | LokiStack, database, retention |
| Observe | ✅ | Jobs 3, 4 | UUID and name-based queries |
| Monitor | ✅ | Job 5 | Tekton Results metrics |
| Troubleshoot | ❌ | - | No troubleshooting content |
| Upgrade | ❌ | - | No upgrade content |

### Gaps Identified

| Stage | Gap | Recommendation |
|-------|-----|----------------|
| Troubleshoot | No troubleshooting procedures | Add common issues: authentication failures, connection errors, missing logs |
| Upgrade | No upgrade procedures | Add version upgrade section if Tekton Results has independent releases |

---

## Navigation Guide

### By User Journey

**Platform Engineer enabling Tekton Results for new cluster:**
1. Job 1: Understand Tekton Results architecture
2. Job 2: Configure LokiStack forwarding, external database, retention policy
3. Job 3: Prepare opc utility and test queries
4. Job 5: Configure ServiceMonitor and verify metrics

**Platform Engineer querying archived runs:**
1. Job 3: Access archived information using UUID-based queries
   - OR Job 4: Access archived information using name-based queries
2. Use search examples for common patterns
3. Refer to reference sections for CEL field documentation

---

## Document Statistics

**Workflow Coverage:**
- Get Started: 1 job
- Configure: 1 job (3 major configuration tasks)
- Observe: 2 jobs (UUID-based and name-based approaches)
- Monitor: 1 job

**Main Jobs:** 5
**User Stories/Paths:** 15 themed sections
**Source Sections:** 17 referenced
**Platform/Tool Variations:** UUID vs name-based querying (2 approaches)

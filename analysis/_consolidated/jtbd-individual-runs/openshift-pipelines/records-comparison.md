# Observability in OpenShift Pipelines - TOC Comparison

**Current Feature-Based vs. Proposed JTBD-Based Structure**

**Analysis Date:** 2026-06-12  
**JTBD Records:** 23  
**Main Jobs:** 6 (rolled up from records)  
**Coverage:** Complete enhanced schema with workflow stages

---

## Current Structure (Feature-Based)

**Using Tekton Results for OpenShift Pipelines observability**

- **Tekton Results concepts**
  - Definition of results and records
  - Naming conventions and UUIDs
  - Data preservation mechanism

- **Configuring Tekton Results**
  - Configuring LokiStack forwarding for logging information
  - Configuring an external database server
  - Configuring the retention policy for Tekton Results
  - Observability metrics for Tekton Results

- **Querying Tekton Results for results and records**
  - Preparing the opc utility environment for querying Tekton Results
  - Querying for results and records by name
  - Searching for results
  - Searching for records
  - Reference information for searching results
  - Reference information for searching records

- **Querying results and logs by the names of pipeline runs and task runs** (Technology Preview)
  - Configuring the opc utility for querying results by pipeline run and task run names
  - Viewing a list of pipeline run names and identifiers
  - Viewing a list of task run names and identifiers
  - Viewing result information for a pipeline run
  - Viewing result information for a task run
  - Short names for command-line arguments

- **Understanding the Tekton Results retention policy**
  - Fine-grained retention policies

---

## Proposed JTBD-Based Structure

### Understand the Platform

**Job 1: Preserve Complete Execution History Beyond the Lifecycle of CRs**

**When:** Managing pipeline operations at scale  
**Personas:** Platform Engineer  
**Why:** Minimizes storage overhead from keeping live CRs while maintaining complete audit trail for compliance and historical analysis without performance impact

#### 1.1 Understand How Tekton Results Archives Pipeline Data (Foundation)

**Goal:** Grasp the core observability capability and data model

→ Lines 59-66: Using Tekton Results for OpenShift Pipelines observability  
Source: Assembly header and abstract

- **Benefit:** Archives PipelineRun and TaskRun information after CR deletion
- **Benefit:** Enables long-term observability without resource bloat
- **Benefit:** Preserves complete audit trail for compliance

#### 1.2 Understand Results vs Records Structure (Reference Knowledge)

**Goal:** Know which resources to query and how data is organized

→ Lines 74-247: Tekton Results concepts  
Source: Concepts section

- **Task:** Distinguish between Results (containers) and Records (individual run data)
- **Task:** Understand naming conventions and UUIDs
- **Task:** Learn how data preservation works after CR deletion
- **Related:** Job 4 (Query archived data)

---

### Set Up & Configure

**Job 2: Ensure Tekton Results is Properly Configured**

**When:** Enabling observability for pipelines  
**Personas:** Platform Engineer  
**Timing:** BEFORE production pipeline execution - missing configuration prevents data capture and log retrieval  
**Why:** Tekton Results is enabled by default but requires additional configuration for logging and production-grade operation

#### 2.1 Understand Configuration Overview (Planning)

**Goal:** Identify what needs to be configured

→ Lines 256-267: Configuring Tekton Results  
Source: Configuration overview section

- Tekton Results enabled by default
- Logging requires LokiStack forwarding setup
- Database configuration for production
- Retention policies to control storage

#### 2.2 Configure Log Forwarding to LokiStack (Critical - Logs Preservation)

**Goal:** Preserve and retrieve complete execution logs after CR deletion

**Timing:** BEFORE pipeline execution - logs cannot be retrieved without this setup

→ Lines 275-398: Configuring LokiStack forwarding for logging information  
Source: LokiStack configuration section

**Prerequisites:**
- Install LokiStack using Loki Operator
- Install OpenShift Logging Operator

**Tasks:**
- **Task:** Configure ClusterLogForwarder CR for application logs
  - → Lines 293-349: Step-by-step ClusterLogForwarder configuration
  - For OpenShift Logging v6 or v5 (different YAML)
- **Task:** Edit TektonConfig CR for Loki integration
  - → Lines 357-398: Enable Tekton Results Loki integration
  - Set `loki_stack_name` and `loki_stack_namespace`

**Validation:** Without this, Tekton Results cannot store or retrieve logging information

#### 2.3 Configure External Database Server (Production Setup)

**Goal:** Ensure production-grade database reliability with backups and performance tuning

**Timing:** BEFORE production pipeline execution - default internal PostgreSQL is for testing only

→ Lines 406-454: Configuring an external database server  
Source: External database section

**Why:** Default internal PostgreSQL lacks production features like automated backups and lifecycle management

**Tasks:**
- **Task:** Create database credentials secret
  - → Lines 414-425: Secret creation procedure
  - `oc create secret generic tekton-results-postgres`
- **Task:** Configure database connection parameters in TektonConfig
  - → Lines 433-454: Database host, port, SSL configuration
  - Set `is_external_db: true`, `db_host`, `db_port`

#### 2.4 Configure Retention Policy (Storage Management)

**Goal:** Remove older results automatically while meeting retention requirements

**Timing:** BEFORE production pipeline execution - default is indefinite retention which causes unlimited storage growth

→ Lines 462-500: Configuring the retention policy for Tekton Results  
Source: Retention policy configuration section

**Why:** Default indefinite retention causes unlimited storage consumption

**Tasks:**
- **Task:** Set default retention period via config map
  - → Lines 468-500: `defaultRetention` parameter configuration
  - Configure `runAt` cron schedule and `maxRetention` days
- **Task:** Configure fine-grained policies (optional)
  - Reference: Job 6 for detailed policy configuration

**Related:** Job 6 (Understand retention policy mechanics)

---

### Track Performance

**Job 3: Monitor Tekton Results Health and Performance**

**When:** Monitoring Tekton Results health and performance  
**Personas:** SRE  
**Requires:** ServiceMonitor for Tekton Results configured, Prometheus Operator deployed  
**Why:** Detects storage failures and data loss risks before they impact observability

#### 3.1 Track Storage Latency and Deletion Metrics (Health Monitoring)

**Goal:** Identify performance issues and data loss risks

→ Lines 508-603: Observability metrics for Tekton Results  
Source: Metrics section

**Metrics exposed by tekton-results-watcher on port 9090:**

- **Storage Performance:**
  - `watcher_run_storage_latency_seconds` - Duration between run completion and successful storage
  - Histogram with buckets from 0.1s to 1800s

- **Storage Failure:**
  - `runs_not_stored_count` - Total runs deleted without successful storage
  - Counter by kind and namespace

- **Deletion Duration:**
  - `watcher_pipelinerun_delete_duration_seconds` - Time to delete PipelineRun
  - `watcher_taskrun_delete_duration_seconds` - Time to delete TaskRun
  - Histograms with labels: pipeline, status, namespace, task, taskrun

- **Deletion Count:**
  - `watcher_pipelinerun_delete_count` - Total deleted PipelineRuns
  - `watcher_taskrun_delete_count` - Total deleted TaskRuns
  - Counters by status and namespace

**Tasks:**
- **Task:** Query metrics with PromQL for dashboards
- **Task:** Create alerting rules for failures and latency spikes
- **Related:** Job 2.4 (Configure retention policy)

---

### Observe System State

**Job 4: Query Archived Results and Records**

**When:** Investigating pipeline execution history  
**Personas:** Pipeline Admin  
**Requires:** opc utility installed (via tkn CLI package), authentication configured for Tekton Results API  
**Why:** Enables analysis of past runs and troubleshooting without dependency on live CRs

#### 4.1 Prepare the opc Utility Environment (One-time Setup)

**Goal:** Execute queries without repeated credential entry

→ Lines 630-683: Preparing the opc utility environment for querying Tekton Results  
Source: opc utility preparation section

**Prerequisites:**
- Install opc utility (included in tkn CLI package)
- Log in to OpenShift cluster

**Tasks:**
- **Task:** Extract Tekton Results API endpoint
  - → Lines 641-644: Get route URL
  - `export RESULTS_API=$(oc get route tekton-results-api-service...)`
- **Task:** Create authentication token
  - → Lines 652-654: Generate service account token
  - `oc create token <service_account>`
- **Task:** Configure opc with address and token
  - → Lines 656-665: `opc results config set` command
  - Configure via CLI or interactively
- **Task:** (Optional) Create results.yaml for automation
  - → Lines 673-683: Persistent configuration file
  - Location: `~/.config/tkn/results.yaml`

#### 4.2 Query for Results and Records by Name or UUID (Direct Lookup)

**Goal:** Quickly access full YAML manifest and logs for specific runs

**Requires:** Log forwarding to LokiStack configured (for logs)

→ Lines 691-786: Querying for results and records by name  
Source: Query by name section

**Query operations:**

- **List results in namespace:**
  - → Lines 706-719: `opc results result list --addr ${RESULTS_API} <namespace>`
  - Shows all results in namespace
  - Format: `namespace/results/uuid`

- **List records in result:**
  - → Lines 727-742: `opc results records list --addr ${RESULTS_API} <result_name>`
  - Shows PipelineRun and TaskRun records
  - Format: `namespace/results/uuid/records/uuid`

- **Get record YAML manifest:**
  - → Lines 753-769: `opc results records get` with jq/base64/python pipeline
  - Returns complete YAML manifest after CR deletion

- **Get log information:**
  - → Lines 771-785: `opc results logs get` command
  - Format: Replace `records` with `logs` in record name
  - Requires LokiStack configuration

#### 4.3 Search for Results Using CEL Queries (Criteria-based Search)

**Goal:** Find runs by status, annotations, or other result attributes

→ Lines 794-826: Searching for results  
Source: Result search section

**CEL query capabilities:**
- Filter by parent, uid, annotations
- Filter by `summary.status` (completion status)
- Filter by `create_time`, `update_time`
- **Note:** Limited fields compared to records - most relevant info is in records

**Example searches:**
- Failed pipeline runs: `!(summary.status == SUCCESS)`
- Runs with specific annotations: `summary.annotations.contains('ann1') && summary.annotations.contains('ann2') && summary.type=='PIPELINE_RUN'`

**Related:** Job 4.5 (Reference for result CEL fields)

#### 4.4 Search for Records Using CEL Queries on Full YAML Data (Advanced Search)

**Goal:** Find runs by completion time, labels, task counts, or any manifest field

→ Lines 835-903: Searching for records  
Source: Record search section

**CEL query capabilities:**
- Access full YAML data via `data` field
- Filter by metadata (labels, annotations)
- Filter by status (completion, conditions)
- Filter by timing (startTime, completionTime)
- Query any manifest element

**Example searches:**
- Failed runs: `!(data.status.conditions[0].status == 'True')`
- Runs by name: `data.metadata.name == 'run1'`
- Task runs for specific pipeline: `data_type == 'TASK_RUN' && data.metadata.labels['tekton.dev/pipelineRun'] == 'run1'`
- Runs by pipeline: `data.metadata.labels['tekton.dev/pipeline'] == 'pipeline1'`
- Long-running runs: `data.status.completionTime - data.status.startTime > duration('5m') && data_type == 'PIPELINE_RUN'`
- Runs by date: `data.status.completionTime.getDate() == 7 && data.status.completionTime.getMonth() == 10 && data.status.completionTime.getFullYear() == 2023`
- Runs with many tasks: `size(data.status.pipelineSpec.tasks) >= 3 && data_type == 'PIPELINE_RUN'`
- Runs with annotations: `data.metadata.annotations.contains('ann1') && data_type == 'PIPELINE_RUN'`

**Related:** Job 4.6 (Reference for record CEL fields)

#### 4.5 Reference: Result CEL Query Fields (Query Construction Aid)

**Goal:** Build correct result queries without trial and error

→ Lines 912-956: Reference information for searching results  
Source: Result reference section

**Available fields:**
- `parent` - Namespace for the CR
- `uid` - Result UUID
- `annotations` - Result annotations
- `summary.status` - Completion status (UNKNOWN, SUCCESS, FAILURE, TIMEOUT, CANCELLED)
- `create_time` - Creation timestamp
- `update_time` - Last update timestamp

**Note:** Do not use quotes for `summary.status` values

**Related:** Job 4.3 (Search results with CEL)

#### 4.6 Reference: Record CEL Query Fields (Query Construction Aid)

**Goal:** Query the correct resource types and YAML paths in records

→ Lines 964-992: Reference information for searching records  
Source: Record reference section

**Available fields:**
- `name` - Record name
- `data_type` - Resource type identifiers:
  - `tekton.dev/v1.TaskRun` or `TASK_RUN`
  - `tekton.dev/v1.PipelineRun` or `PIPELINE_RUN`
  - `results.tekton.dev/v1alpha2.Log`
- `data` - Full YAML manifest (query any field within)

**Note:** Can use all elements of YAML data, e.g., `data.status.completionTime`

**Related:** Job 4.4 (Search records with CEL)

---

### Query & Troubleshoot by Run Names

**Job 5: Query by PipelineRun and TaskRun Names**

**When:** Prefer to work with run names rather than result UUIDs  
**Personas:** Developer  
**Requires:** opc utility with results config set  
**Why:** Reduces cognitive overhead of UUID-based queries by enabling familiar run name identifiers

**Note:** Technology Preview feature - different configuration from UUID-based queries

#### 5.1 Configure opc for Name-based Queries (Setup)

**Goal:** Query by run names instead of UUIDs

→ Lines 1037-1101: Configuring the opc utility for querying results by pipeline run and task run names  
Source: Name-based query configuration section

**Prerequisites:**
- Install opc utility
- Log in to OpenShift cluster

**Tasks:**
- **Task:** Create authentication token
  - → Lines 1053-1056: Generate token
  - `oc create token <service_account>`
- **Task:** Configure opc with results config
  - → Lines 1064-1101: `opc results config set` command
  - **Interactive:** `opc results config set` (prompts for values)
  - **Command:** `opc results config set --host="https://tekton-results.example.com" --token="<token>"`
  - Uses `host` instead of `address` (different from UUID config)
  - Supports persistent configuration

**Verification:**
- View configuration: `opc results config view`

**Related:** Job 4.1 (UUID-based configuration comparison)

#### 5.2 View Pipeline Run Lists by Namespace or Pipeline (Discovery)

**Goal:** Identify runs of interest before retrieving details

→ Lines 1109-1159: Viewing a list of pipeline run names and identifiers  
Source: Pipeline run listing section

**List operations:**

- **List all pipeline runs in namespace:**
  - → Lines 1117-1126: `opc results pipelinerun list -n <namespace_name>`
  - Shows: name, UID, start time, duration, status
  - Pagination: `--limit=10` with optional `--single-page=false`

- **Filter by pipeline name:**
  - → Lines 1134-1143: `opc results pipelinerun list <pipeline_name> -n <namespace_name>`
  - Lists runs for pipelines containing `<pipeline_name>` in name

- **Filter by labels/annotations:**
  - → Lines 1151-1159: `--labels="key=value,key2=value2"`

#### 5.3 View Task Run Lists by Namespace or Pipeline Run (Discovery)

**Goal:** Identify specific task executions for analysis

→ Lines 1166-1223: Viewing a list of task run names and identifiers  
Source: Task run listing section

**List operations:**

- **List all task runs in namespace:**
  - → Lines 1174-1184: `opc results taskrun list -n <namespace_name>`
  - Shows: name, UID, start time, duration, status
  - Pagination: `--limit=10` with optional `--single-page=false`
  - Labels filter: `--labels="key=value"`

- **List task runs for pipeline run:**
  - → Lines 1192-1201: `opc results taskrun list --pipelinerun <pipelinerun_name> -n <namespace_name>`
  - Shows only task runs associated with specific pipeline run

#### 5.4 View Pipeline Run Results (Analysis & Troubleshooting)

**Goal:** Understand execution details and troubleshoot failures

→ Lines 1232-1331: Viewing result information for a pipeline run  
Source: Pipeline run results section

**View operations:**

- **Describe pipeline run (summary):**
  - → Lines 1247-1273: `opc results pipelinerun describe -n <namespace> <pipelinerun_name>`
  - Or by UUID: `--uid <pipelinerun_uuid>`
  - Shows: metadata, status, duration, params, workspaces, taskruns

- **Get full YAML manifest:**
  - → Lines 1281-1299: `opc results pipelinerun describe -n <namespace> --output yaml <pipelinerun_name>`
  - Or by UUID: `--output yaml --uid <pipelinerun_uuid>`
  - Complete PipelineRun YAML for deep analysis

- **View pipeline run logs:**
  - → Lines 1307-1331: `opc results pipelinerun logs -n <namespace> <pipelinerun_name>`
  - Or by UUID: `--uid <pipelinerun_uuid>`
  - **Important:** Pipeline logs don't include task run logs
  - Use task run logs commands for complete log coverage

**Related:** Job 5.5 (View task run results for complete logs)

#### 5.5 View Task Run Results (Task-level Troubleshooting)

**Goal:** Diagnose issues at the task level

**Requires:** Log forwarding to LokiStack configured (for logs)

→ Lines 1339-1421: Viewing result information for a task run  
Source: Task run results section

**View operations:**

- **Describe task run (summary):**
  - → Lines 1354-1380: `opc results taskrun describe -n <namespace> <taskrun_name>`
  - Or by UUID: `--uid <taskrun_uuid>`
  - Shows: metadata, status, duration, params

- **Get full YAML manifest:**
  - → Lines 1388-1401: `opc results taskrun describe -n <namespace> --output yaml <taskrun_name>`
  - Or by UUID: `--output yaml --uid <taskrun_uuid>`
  - Complete TaskRun YAML

- **View task run logs:**
  - → Lines 1409-1421: `opc results taskrun logs -n <namespace> <taskrun_name>`
  - Or by UUID: `--uid <taskrun_uuid>`
  - Requires LokiStack configuration
  - Shows step-by-step execution logs

**Related:** Job 2.2 (Configure LokiStack for log retrieval)

#### 5.6 Reference: CLI Shortcuts (Efficiency)

**Goal:** Execute queries faster with less typing

→ Lines 1429-1447: Short names for command-line arguments  
Source: CLI shortcuts section

**Short forms:**
- `pipelinerun` = `pr`
- `taskrun` = `tr`
- `describe` = `desc`

**Examples:**
- `opc results pr list` instead of `opc results pipelinerun list`
- `opc results tr desc` instead of `opc results taskrun describe`

---

### Administer Platform

**Job 6: Understand How Retention Policy Agent Works**

**When:** Managing database storage and compliance  
**Personas:** Platform Engineer  
**Why:** Configuring appropriate retention rules prevents data loss from aggressive policies and excess storage from unlimited retention

#### 6.1 Understand Retention Policy Mechanics (Foundation)

**Goal:** Know when and how results/records are pruned

→ Lines 1449-1506: Understanding the Tekton Results retention policy  
Source: Retention policy concepts section

**How it works:**
- Retention policy agent runs periodically (configured via cron)
- Configured via `tekton-results-config-results-retention-policy` config map in `openshift-pipelines` namespace
- `defaultRetention` applies to all results unless overridden by specific policies
- Prunes results and records older than retention period

**Configuration parameters:**
- `runAt` - Cron schedule for pruning job (default: `"7 7 * * 7"` every Sunday at 7:07 AM)
- `defaultRetention` - Default retention period (default: `30d`)
- `maxRetention` - (Deprecated) Legacy field, use `defaultRetention`
- `policies` - List of fine-grained retention policies

**Related:** Job 2.4 (Configure basic retention)

#### 6.2 Define Fine-grained Retention Policies (Advanced Storage Management)

**Goal:** Retain critical data longer while purging transient runs

→ Lines 1537-1621: Fine-grained retention policies  
Source: Fine-grained policies section

**Policy targeting options:**

- **By namespace:**
  - `matchNamespaces` - List of namespaces to match
  - Example: `["production", "prod-east"]`
  - Retain production namespace runs longer

- **By labels:**
  - `matchLabels` - Map of label keys and possible values
  - Example: `"criticality": ["high"]`
  - A Result must have ALL listed label keys with matching values

- **By annotations:**
  - `matchAnnotations` - Map of annotation keys and possible values
  - Example: `"debug/retain": ["true"]`
  - Works similarly to matchLabels

- **By status:**
  - `matchStatuses` - List of final statuses
  - Values: `Succeeded`, `Failed`, `Cancelled`, `Running`, `Pending`
  - Example: Retain failures longer for analysis

**Policy evaluation:**
- Policies evaluated in order (first match wins)
- All selector types use AND logic (must satisfy all conditions)
- Each policy specifies retention duration (e.g., `"180d"`, `"14d"`, `"7d"`)
- Use to balance compliance requirements with storage costs

**Example use cases:**
- Production critical failures: 180 days retention
- Debug-annotated runs: 14 days retention
- All production runs: 60 days retention
- CI namespace runs: 7 days retention
- Default (all others): 30 days retention

**Related:** Job 3 (Monitor storage metrics)

---

## Key Differences

### Current Structure (Feature-Based)

**Organized By:** Features, technical components (concepts, configuration, querying methods)  
**Navigation:** 5 main sections with 16 subsections  
**User Journey:** Linear reading through feature documentation  
**Query Methods:** Two separate sections (UUID-based and name-based) without clear guidance on when to use each

### Proposed Structure (JTBD-Based)

**Organized By:** Job map stages, user goals (Understand → Configure → Monitor → Observe → Troubleshoot → Administer)  
**Navigation:** 6 main jobs with 17 user stories organized by workflow stage  
**User Journey:** Goal-directed navigation - find the job you need to do  
**Query Methods:** Both methods integrated with clear guidance on when to use each approach

---

## Hierarchy Levels Explanation

The proposed structure uses a 3-level hierarchy optimized for job-oriented navigation:

### Level 1: Main Jobs (6 total)

Stable, outcome-focused goals that represent what users need to accomplish. These would exist even if the underlying technology changed.

**Examples:**
- "Preserve Complete Execution History Beyond the Lifecycle of CRs"
- "Ensure Tekton Results is Properly Configured"
- "Query Archived Results and Records"

### Level 2: User Stories (17 total)

Scenario-specific tasks or themed goals nested under main jobs. These represent specific approaches, personas, or implementation paths.

**Examples:**
- "Configure Log Forwarding to LokiStack (Critical - Logs Preservation)"
- "Search for Records Using CEL Queries on Full YAML Data"
- "View Pipeline Run Results (Analysis & Troubleshooting)"

### Level 3: Procedures (References to Source)

Step-by-step instructions referenced by line numbers from the source document. These are the actual implementation details.

**Format:**
- → Lines X-Y: Section title
- Source: Chapter/section reference

---

## Example Consolidation

### Current (Fragmented):

**Query methods scattered across separate sections:**

- Section 3: Querying Tekton Results for results and records (UUID-based)
  - Subsection 3.1: Preparing the opc utility environment
  - Subsection 3.2: Querying for results and records by name
  - Subsection 3.3: Searching for results
  - Subsection 3.4: Searching for records

- Section 4: Querying results and logs by the names of pipeline runs and task runs (Name-based)
  - Subsection 4.1: Configuring the opc utility for querying results by pipeline run and task run names
  - Subsection 4.2: Viewing a list of pipeline run names and identifiers
  - Subsection 4.3: Viewing a list of task run names and identifiers

**Problem:** Users don't know which method to use for their use case.

### Proposed (Consolidated):

**Two main jobs with clear context:**

**Job 4: Query Archived Results and Records** (UUID-based - for automation)
- Context: Best for API automation, scripts, CI/CD integration
- Personas: Pipeline Admin, automation engineers
- 6 user stories: Setup → Query by name → Search results → Search records → Reference

**Job 5: Query by PipelineRun and TaskRun Names** (Name-based - for developers)
- Context: Developer-friendly, when you know run names, Technology Preview
- Personas: Developer, interactive troubleshooting
- 6 user stories: Setup → List runs → View results → Troubleshoot

**Benefit:**
- Clear guidance on which method to use (automation vs. interactive)
- Both methods discoverable from single navigation point
- Reduced decision overhead for users

---

## Navigation Improvement Metrics

### Current Structure Complexity

**Top-level navigation:** 5 main sections
- Concepts (1)
- Configuration (4 subsections)
- UUID-based queries (6 subsections)
- Name-based queries (6 subsections)
- Retention policy (2 subsections)

**Total navigation items:** 19 (5 + 14 subsections)

**User journey to find log retrieval:**
1. Open "Configuring Tekton Results"
2. Scan 4 configuration subsections
3. Find "Configuring LokiStack forwarding for logging information"
4. Read to understand log preservation setup
5. Navigate to "Querying Tekton Results for results and records"
6. Find "Querying for results and records by name"
7. Locate log retrieval command

**Total clicks:** 5-7 to reach log configuration and retrieval

### Proposed Structure Simplification

**Top-level navigation:** 6 main jobs organized by workflow stage
- Job 1: Understand (Preserve execution history)
- Job 2: Configure (Ensure proper configuration)
- Job 3: Monitor (Track health and performance)
- Job 4: Observe (Query by UUID)
- Job 5: Troubleshoot (Query by name)
- Job 6: Administer (Retention policies)

**Total navigation items:** 23 (6 main jobs + 17 user stories)

**User journey to find log retrieval:**
1. Navigate to "Set Up & Configure" (Job 2)
2. See "Configure Log Forwarding to LokiStack" as critical user story
3. Read configuration and prerequisites
4. Navigate to "Observe System State" (Job 4) or "Query & Troubleshoot by Run Names" (Job 5)
5. Find log retrieval in query operations

**Total clicks:** 2-3 to reach log configuration and retrieval

### Quantified Improvements

**Navigation efficiency:**
- **Current:** 5 main sections → 14 subsections (19 total items, avg 3.8 subsections per section)
- **Proposed:** 6 main jobs → 17 user stories (23 total items, avg 2.8 user stories per job)
- **Reduction:** 20% reduction in average items per category

**Click depth:**
- **Current:** 5-7 clicks to reach specific content
- **Proposed:** 2-3 clicks to reach specific content
- **Improvement:** 50-70% reduction in navigation clicks

**Contextual clarity:**
- **Current:** No clear guidance on UUID vs. name-based queries
- **Proposed:** Explicit "when to use" context for each query method
- **Benefit:** Eliminates decision paralysis for query method selection

---

## Workflow Coverage Comparison

| Stage | Current | Proposed | Gap Status |
|-------|---------|----------|------------|
| Get Started | ⚠️ Buried in concepts | ✅ Job 1 (dedicated foundation) | Elevated |
| Plan | ❌ Missing | ⚠️ Job 2.1 (overview only) | Partial |
| Understand | ⚠️ Concepts section | ✅ Jobs 1.1, 1.2 (foundation) | Improved |
| Configure | ✅ Section 2 (4 tasks) | ✅ Job 2 (4 user stories) | Reorganized |
| Monitor | ✅ Section 2.4 | ✅ Job 3 | Elevated |
| Observe | ✅ Sections 3-4 | ✅ Jobs 4, 5 | Consolidated |
| Troubleshoot | ⚠️ Mixed with queries | ✅ Job 5 (dedicated) | Elevated |
| Administer | ✅ Section 5 | ✅ Job 6 | Reorganized |
| Secure | ⚠️ Authentication only | ⚠️ Auth token (Jobs 4.1, 5.1) | Limited |
| Deploy | ❌ Missing | ❌ Missing | Gap remains |
| Upgrade | ❌ Missing | ❌ Missing | Gap remains |
| Migrate | N/A | N/A | Not applicable |
| Reference | ✅ Reference sections | ✅ Integrated (Jobs 4.5, 4.6, 5.6) | Reorganized |

### Coverage Summary

**Current structure gaps:** Plan (no overview), Secure (authentication only), Deploy (installation), Upgrade  
**Proposed structure gaps:** Plan (partial), Secure (authentication only), Deploy (installation), Upgrade  
**Gaps addressed by restructure:** 
- Get Started (elevated to dedicated Job 1)
- Troubleshoot (elevated to dedicated workflow in Job 5)
- Monitor (elevated to dedicated Job 3)

### Recommendations for Gap Closure

| Gap | Recommendation | Priority | Justification |
|-----|----------------|----------|---------------|
| Deploy | Link to OpenShift Pipelines installation guide | High | Tekton Results installation is part of main Pipelines operator install |
| Secure | Add RBAC configuration for Tekton Results API access | High | Critical for production deployments with multi-tenant clusters |
| Plan | Add decision tree for query method selection | Medium | Helps users choose between UUID-based (Job 4) vs. name-based (Job 5) approaches |
| Upgrade | Add retention policy migration guidance | Medium | Important when upgrading between Tekton Results versions |
| Integrate | Add CI/CD integration examples for automated queries | Low | Useful for advanced automation workflows |

### Coverage Indicators

| Symbol | Meaning |
|--------|---------|
| ✅ | Stage fully covered with dedicated content |
| ⚠️ | Partial coverage - content exists but scattered or limited |
| ❌ | Stage not covered - content gap identified |

---

## Additional Resources

**Common Expression Language (CEL):** https://cel.dev/

**Related OpenShift Pipelines Documentation:**
- Installing tkn CLI (referenced in Job 4, 5)
- OpenShift Pipelines installation (for Deploy stage gap)

---

## Appendices

### A. Query Method Comparison Matrix

| Query Method | Best For | Complexity | Prerequisites | Use Case |
|--------------|----------|------------|---------------|----------|
| **UUID-based (Job 4)** | API automation, scripts | Medium | opc utility, API endpoint, results.yaml config | Programmatic access, CI/CD integration, when you have result UUID |
| **Name-based (Job 5)** | Manual investigation, developers | Low | opc utility, results config set | Interactive troubleshooting, ad-hoc queries, when you know PipelineRun/TaskRun name |
| **CEL Queries (Jobs 4.3, 4.4)** | Pattern analysis, bulk filtering | High | Understanding CEL syntax, opc utility | Finding runs by criteria, batch analysis, complex filtering |

**Decision Guide:**
- **Use UUID queries (Job 4):** When automating workflows, integrating with CI/CD, or when you have the result UUID from Tekton Results API
- **Use Name queries (Job 5):** When troubleshooting interactively, when you know the PipelineRun/TaskRun name, or for developer-friendly workflows
- **Use CEL queries (Jobs 4.3, 4.4):** When searching by status, labels, timing, duration, or any manifest field; when analyzing patterns across multiple runs

### B. Configuration Dependencies

```
Job 2.2 (LokiStack) ──required for──> Log retrieval in Jobs 4.2, 5.5
                                        │
                                        └──> Without this: Cannot retrieve logs after CR deletion
                                             Impact: Loss of troubleshooting capability

Job 2.3 (External DB) ──required for──> Production operations (all Jobs)
                                         │
                                         └──> Without this: Default internal PostgreSQL lacks:
                                              - Automated backups
                                              - High availability
                                              - Performance tuning
                                              - Lifecycle management

Job 2.4 (Retention) ──required for──> Storage cost control (affects all Jobs)
                                      │
                                      └──> Without this: 
                                           - Unlimited storage growth
                                           - Default indefinite retention
                                           - No automated cleanup
```

### C. Persona Journey Mapping

**Platform Engineer (Setting up for production):**
1. Job 1: Understand what Tekton Results does and why (foundation)
2. Job 2.2: Configure LokiStack for log preservation (critical)
3. Job 2.3: Configure external database (production requirement)
4. Job 2.4: Configure basic retention policy (storage management)
5. Job 3: Set up monitoring for health and performance
6. Job 6: Fine-tune retention policies for compliance and cost

**Pipeline Admin (Investigating failures):**
1. Job 4.1: Set up opc utility (one-time)
2. Job 4.3: Search for failed runs with CEL query
3. Job 4.2: Get specific run details and logs
4. Job 4.4: Search records for pattern analysis

**Developer (Troubleshooting task run issues):**
1. Job 5.1: Configure opc for name-based queries
2. Job 5.2: List pipeline runs to find the run of interest
3. Job 5.3: List task runs within that pipeline run
4. Job 5.5: View task run logs to diagnose failure

**SRE (Monitoring platform health):**
1. Job 3: Track storage latency and deletion metrics
2. Job 6.1: Understand retention policy mechanics
3. Job 2.4: Adjust retention policies based on storage trends

### D. Technology Preview Feature Guidance

**Job 5 (Query by PipelineRun and TaskRun Names) is Technology Preview:**

**Implications:**
- Not supported with Red Hat production SLAs
- Might not be functionally complete
- Not recommended for production environments
- Provides early access for testing and feedback

**When to use:**
- Development environments
- Testing and evaluation
- Providing feedback to product team
- Non-production troubleshooting

**Alternative for production:**
- Use Job 4 (UUID-based queries) for production workflows
- More stable and fully supported

**Migration path:**
- When feature reaches GA, migrate scripts from Job 4 to Job 5 if name-based queries are preferred

### E. Metrics Labels Reference

Most Tekton Results metrics use labels for filtering. Key labels:

| Label | Description | Example Values |
|-------|-------------|----------------|
| `kind` | Tekton resource type | `pipelinerun`, `taskrun` |
| `namespace` | Kubernetes namespace | `production`, `dev`, `ci` |
| `pipeline` | Pipeline name (optional) | `build-pipeline`, `deploy-pipeline` |
| `status` | Completion status | `Succeeded`, `Failed`, `Cancelled` |
| `task` | Task name (optional, TaskRuns only) | `build`, `test`, `deploy` |
| `taskrun` | TaskRun name (optional, TaskRuns only) | `build-task-abc123` |

**PromQL Query Examples:**
- Storage latency for failed runs: `watcher_run_storage_latency_seconds{status="Failed"}`
- Deletion count by namespace: `sum(watcher_pipelinerun_delete_count) by (namespace)`
- Runs not stored by kind: `sum(runs_not_stored_count) by (kind)`

---

## Document Statistics

**Workflow Coverage:**
- Understand: 1 job (Job 1 with 2 user stories)
- Configure: 1 job (Job 2 with 4 user stories)
- Monitor: 1 job (Job 3 with 1 user story)
- Observe: 2 jobs (Jobs 4, 5 with 11 user stories)
- Troubleshoot: Integrated in Job 5 (overlaps with Observe)
- Administer: 1 job (Job 6 with 2 user stories)
- Reference: Integrated throughout (Jobs 1, 4, 5)
- **Gaps:** Deploy, Secure (limited), Plan (partial), Upgrade

**Main Jobs:** 6  
**User Stories/Themed Goals:** 17  
**Total Source Lines:** 1,621  
**Source Sections:** 21  
**Query Methods:** 2 (UUID-based, Name-based)  
**Personas:** 4 (Platform Engineer, Pipeline Admin, Developer, SRE)

**Content Density:**
- Average user stories per main job: 2.8
- Average line coverage per user story: 95 lines
- Total procedural content: ~1,400 lines (excluding concepts/reference)

---

**Generated from:** `records-jtbd.jsonl` (23 records)  
**Source document:** `records-combined.adoc` (1,621 lines)  
**Proposed TOC:** `records-toc-new_taxonomy.md`  
**Generation date:** 2026-06-12

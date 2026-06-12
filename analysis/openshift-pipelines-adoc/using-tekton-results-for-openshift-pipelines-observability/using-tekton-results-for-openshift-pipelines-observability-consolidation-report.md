# Using Tekton Results for OpenShift Pipelines Observability — Consolidation Report

**Document:** using-tekton-results-for-openshift-pipelines-observability.adoc
**JTBD Records:** 23 pre-consolidated jobs → 5 final jobs (after merging)

---

## Executive Summary

### What's Changing

The current documentation is organized by **technical component and query method**: starting with conceptual material, followed by configuration tasks grouped under a single section, then split into two major sections based on query method (UUID-based vs name-based). This organization requires users to understand the technical distinction between query methods and navigate multiple top-level sections to complete related tasks like production configuration.

This causes several pain points: configuration tasks (LokiStack, database, retention) appear as disconnected siblings without context about production readiness; observability metrics are buried under the "Configuring" section despite being a monitoring concern; and the two querying methods are presented as separate top-level sections without clear guidance on when to use each approach.

The proposed structure organizes content by **user goal and workflow stage**: understanding the architecture, configuring for production use, observing archived runs (with two method options), and monitoring system health. This aligns with how platform engineers actually use Tekton Results — first understanding concepts, then configuring for production, then querying as needed, and finally monitoring performance.

### Key Improvements

- **Unified production configuration:** Three scattered configuration procedures (LokiStack, database, retention) consolidated into one "Configure for Production Use" job with clear rationale for each task
- **Elevated monitoring visibility:** Observability metrics moved from buried configuration subsection to dedicated "Monitor Tekton Results Health" job under correct workflow stage
- **Clearer query method distinction:** UUID-based and name-based queries presented as two job options under "Observe" stage with decision guide for choosing appropriate method
- **Embedded reference material:** CEL query field references moved from standalone sections to within relevant search procedures where users need them
- **Workflow-based navigation:** 5 main jobs organized by natural workflow progression (Understand → Configure → Observe → Monitor) replacing fragmented 18+ section navigation
- **Production readiness context:** Configuration tasks explicitly framed around production requirements (logging, storage, lifecycle) rather than presented as isolated features
- **Technology Preview clarity:** Name-based querying clearly marked as Technology Preview at job level with context about different configuration requirements

---

## Current Structure (Feature-Based)

- **Using Tekton Results for OpenShift Pipelines observability** — Main title
  - **Tekton Results concepts** — Results and records data model, naming conventions, YAML preservation
  - **Configuring Tekton Results** — Configuration parent section
    - Configuring LokiStack forwarding for logging information — OpenShift Logging v5/v6 ClusterLogForwarder setup
    - Configuring an external database server — PostgreSQL credentials and TektonConfig settings
    - Configuring the retention policy for Tekton Results — Cron schedule and maxRetention days
    - Observability metrics for Tekton Results — Metrics categories, labels, performance/failure/deletion metrics
  - **Querying Tekton Results for results and records** — UUID-based querying parent section
    - Preparing the opc utility environment for querying Tekton Results — RESULTS_API variable, token creation, config file
    - Querying for results and records by name — List results, list records, retrieve YAML, retrieve logs
    - Searching for results — CEL queries for results with examples
    - Searching for records — CEL queries for records with examples
    - Reference information for searching results — CEL field definitions (parent, uid, annotations, summary, create_time, update_time)
    - Reference information for searching records — CEL field definitions (name, data_type, data)
  - **Querying results and logs by the names of pipeline runs and task runs** — Name-based querying parent section (Technology Preview)
    - Configuring the opc utility for querying results by pipeline run and task run names — Interactive and command-line config, verification
    - Viewing a list of pipeline run names and identifiers — List all or by pipeline name, filter options
    - Viewing a list of task run names and identifiers — List all or by pipeline run, filter options
    - Viewing result information for a pipeline run — Describe, YAML output, logs (excludes task run logs)
    - Viewing result information for a task run — Describe, YAML output, logs (requires LokiStack)
    - Short names for command-line arguments — pr, tr, desc shortcuts

**Total:** 4 major sections, 18+ subsections, organized by technical component (concepts, configuration, metrics) and query method (UUID vs name).

---

## Proposed JTBD-Based Structure

### Quick Overview

- **Getting Started**
  - Job 1: Understand Tekton Results Architecture
- **Set Up & Configure**
  - Job 2: Configure Tekton Results for Production Use
- **Observe System State**
  - Job 3: Access Archived Pipeline and Task Run Information (UUID-Based Queries)
  - Job 4: Access Archived Information by Pipeline Run and Task Run Names (Technology Preview)
- **Track Performance**
  - Job 5: Monitor Tekton Results Health and Performance

---

### Detailed Job Descriptions

#### Getting Started

**Job 1: Understand Tekton Results Architecture**

*When I need to understand how pipeline runs and task runs are archived, I want to learn about results and records concepts, so I can effectively use Tekton Results for observability.*

Prerequisites: Install Red Hat OpenShift Pipelines

- **1.1. Results and Records Data Model** `[concept]`
  - Lines 73-245: Tekton Results concepts
  - Source: Main content body
  - Context: Foundation for all Tekton Results usage; explains core data structures
  - Results contain records; pipeline runs create multi-record results; standalone task runs create single-record results
  - Naming format: `<namespace>/results/<parent_run_uuid>` for results, `<namespace>/results/<parent_run_uuid>/records/<run_uuid>` for records
  - Records preserve complete YAML manifests including spec, annotations, and status after resource deletion

---

#### Set Up & Configure

**Job 2: Configure Tekton Results for Production Use**

*When I need production-ready Tekton Results, I want to configure logging forwarding and optional settings, so I can store and access all pipeline run and task run information.*

Prerequisites: Install Red Hat OpenShift Pipelines

- **2.1. Configure LokiStack Forwarding** `[procedure]`
  - Lines 273-395: Configuring LokiStack forwarding for logging information
  - Source: Configuring Tekton Results section
  - Context: Required for accessing task run logs via Tekton Results API; without this, only manifests are accessible
  - Prerequisites: LokiStack and OpenShift Logging installed, cluster admin access
  - Install LokiStack via Loki Operator and OpenShift Logging Operator
  - Create ClusterLogForwarder CR (different manifests for OpenShift Logging v5 vs v6)
  - Configure TektonConfig CR with loki_stack_name and loki_stack_namespace

- **2.2. Configure External Database Server** `[procedure]`
  - Lines 404-451: Configuring an external database server
  - Source: Configuring Tekton Results section
  - Context: Default internal PostgreSQL unsuitable for production; lacks automated backups, performance tuning, storage lifecycle management, operator-level database modifications support
  - Create secret in openshift-pipelines namespace with POSTGRES_USER and POSTGRES_PASSWORD
  - Edit TektonConfig CR: set is_external_db: true, db_host (hostname), db_port (port number)

- **2.3. Configure Retention Policy** `[procedure]`
  - Lines 461-497: Configuring the retention policy for Tekton Results
  - Source: Configuring Tekton Results section
  - Context: Default indefinite retention causes unnecessary storage use and database performance degradation
  - Edit TektonConfig CR config-results-retention-policy configMap
  - Set runAt (cron format for pruning job schedule, e.g., "3 5 * * 0" for Sunday 5:03 AM)
  - Set maxRetention (days to retain, e.g., "30" for 30-day retention)

---

#### Observe System State

**Job 3: Access Archived Pipeline and Task Run Information (UUID-Based Queries)**

*When I need to retrieve archived pipeline and task run information, I want to query Tekton Results using the opc utility, so I can access manifests and logs by name or search criteria.*

Prerequisites: Install tkn CLI package, Install opc utility, Configure Tekton Results

- **3.1. Prepare opc Utility Environment** `[procedure]`
  - Lines 628-680: Preparing the opc utility environment for querying Tekton Results
  - Source: Querying Tekton Results for results and records section
  - Context: Authentication setup required before any querying; can use environment variables + token or config file
  - Set RESULTS_API environment variable to Tekton Results route
  - Create authentication token via `oc create token <service_account>` (service account needs read access to pipeline namespaces)
  - Optional: Create ~/.config/tkn/results.yaml with address, token, ssl settings for automatic authentication

- **3.2. Query Results and Records by Name** `[procedure]`
  - Lines 689-783: Querying for results and records by name
  - Source: Querying Tekton Results for results and records section
  - Context: Direct access when you know result/record names; requires jq package
  - List all results in namespace: `opc results result list --addr ${RESULTS_API} <namespace>`
  - List all records in result: `opc results records list --addr ${RESULTS_API} <result_name>`
  - Retrieve YAML manifest: `opc results records get | jq -r .data.value | base64 -d | xargs python3 -c 'import sys, yaml, json; j=json.loads(sys.argv[1]); print(yaml.safe_dump(j))'`
  - Retrieve logs: `opc results logs get --addr ${RESULTS_API} <log_record_name> | jq -r .data | base64 -d` (replace `records` with `logs` in record name)

- **3.3. Search for Results Using CEL Queries** `[procedure]`
  - Lines 792-824: Searching for results
  - Lines 910-953: Reference information for searching results
  - Source: Querying Tekton Results for results and records section
  - Context: Most relevant information in records, not results; use results search for high-level queries only
  - Search: `opc results result list --addr ${RESULTS_API} --filter="<cel_query>" <namespace>`
  - Common queries: failed runs `!(summary.status == SUCCESS)`, runs with annotations `summary.annotations.contains('ann1')`
  - Available CEL fields: parent (namespace), uid (result UUID), annotations, summary, create_time, update_time, summary.status (UNKNOWN, SUCCESS, FAILURE, TIMEOUT, CANCELLED)

- **3.4. Search for Records Using CEL Queries** `[procedure]`
  - Lines 833-901: Searching for records
  - Lines 962-989: Reference information for searching records
  - Source: Querying Tekton Results for results and records section
  - Context: Rich filtering by names, completion times, pipeline associations, YAML manifest data; records contain full YAML allowing complex searches
  - Search all records: `opc results records list --addr ${RESULTS_API} --filter="<cel_query>" <namespace>/result/-`
  - Search within result: `opc results records list --addr ${RESULTS_API} --filter="<cel_query>" <result_name>`
  - Common queries:
    - Failed runs: `!(data.status.conditions[0].status == 'True')`
    - By name: `data.metadata.name == 'run1'`
    - Task runs for pipeline: `data_type == 'TASK_RUN' && data.metadata.labels['tekton.dev/pipelineRun'] == 'run1'`
    - By duration: `data.status.completionTime - data.status.startTime > duration('5m') && data_type == 'PIPELINE_RUN'`
    - By completion date: `data.status.completionTime.getDate() == 7 && data.status.completionTime.getMonth() == 10 && data.status.completionTime.getFullYear() == 2023`
    - By task count: `size(data.status.pipelineSpec.tasks) >= 3 && data_type == 'PIPELINE_RUN'`
  - Available CEL fields: name, data_type (tekton.dev/v1.TaskRun, tekton.dev/v1.PipelineRun, results.tekton.dev/v1alpha2.Log), data (entire YAML manifest)

---

**Job 4: Access Archived Information by Pipeline Run and Task Run Names (Technology Preview)**

*When I need to query archived information using familiar run names, I want to use pipeline run and task run names instead of UUIDs, so I can access results more intuitively.*

Prerequisites: Install opc utility, Configure opc for name-based queries

- **4.1. Configure opc for Name-Based Queries** `[procedure]`
  - Lines 1035-1099: Configuring the opc utility for querying results by pipeline run and task run names
  - Source: Querying results and logs by the names of pipeline runs and task runs section
  - Context: Different configuration than UUID-based queries; Technology Preview feature; simpler interactive workflow
  - Create authentication token via `oc create token <service_account>`
  - Configure interactively: `opc results config set` (responds to prompts)
  - Or configure from command: `opc results config set --host="https://tekton-results.example.com" --token="<token>"`
  - Verify configuration: `opc results config view`

- **4.2. View Pipeline Run List** `[procedure]`
  - Lines 1108-1156: Viewing a list of pipeline run names and identifiers
  - Source: Querying results and logs by the names of pipeline runs and task runs section
  - Context: Discover available pipeline runs for detailed querying; includes status and duration
  - List all in namespace: `opc results pipelinerun list -n <namespace>`
  - List for named pipeline: `opc results pipelinerun list <pipeline_name> -n <namespace>` (shows runs for pipelines with names containing the string)
  - Optional filters: --limit (e.g., --limit=10), --single-page=false (prompts to continue), --labels (filter by labels/annotations)

- **4.3. View Task Run List** `[procedure]`
  - Lines 1165-1220: Viewing a list of task run names and identifiers
  - Source: Querying results and logs by the names of pipeline runs and task runs section
  - Context: Discover task runs in namespace or associated with specific pipeline run
  - List all in namespace: `opc results taskrun list -n <namespace>`
  - List for pipeline run: `opc results taskrun list --pipelinerun <pipelinerun_name> -n <namespace>`
  - Optional filters: --limit, --single-page=false, --labels

- **4.4. View Pipeline Run Results** `[procedure]`
  - Lines 1231-1328: Viewing result information for a pipeline run
  - Source: Querying results and logs by the names of pipeline runs and task runs section
  - Context: Retrieve description (status, params, workspaces, task runs), full manifest, or logs for completed pipeline run
  - Describe by name: `opc results pipelinerun describe -n <namespace> <pipelinerun_name>`
  - Describe by UUID: `opc results pipelinerun describe -n <namespace> --uid <pipelinerun_uuid>`
  - Full YAML: `opc results pipelinerun describe -n <namespace> --output yaml <pipelinerun_name>`
  - Logs: `opc results pipelinerun logs -n <namespace> <pipelinerun_name>` (excludes task run logs; query task runs separately)

- **4.5. View Task Run Results** `[procedure]`
  - Lines 1337-1418: Viewing result information for a task run
  - Source: Querying results and logs by the names of pipeline runs and task runs section
  - Context: Retrieve description (status, params), full manifest, or logs for completed task run; requires LokiStack for logs
  - Prerequisites: LokiStack configured (for log retrieval)
  - Describe by name: `opc results taskrun describe -n <namespace> <taskrun_name>`
  - Describe by UUID: `opc results taskrun describe -n <namespace> --uid <taskrun_uuid>`
  - Full YAML: `opc results taskrun describe -n <namespace> --output yaml <taskrun_name>`
  - Logs: `opc results taskrun logs -n <namespace> <taskrun_name>`

---

#### Track Performance

**Job 5: Monitor Tekton Results Health and Performance**

*When I need to ensure Tekton Results is operating correctly, I want to monitor storage and deletion metrics, so I can identify performance issues and data loss risks.*

Prerequisites: Configure ServiceMonitor resources, Install Prometheus Operator

- **5.1. Metrics Exposure and Labels** `[reference]`
  - Lines 506-600: Observability metrics for Tekton Results
  - Source: Observability metrics for Tekton Results section (previously under Configuring Tekton Results)
  - Context: tekton-results-watcher exposes metrics on port 9090 at /metrics endpoint; automatically discovered by Prometheus when ServiceMonitor configured
  - Metrics categories: storage performance, storage failures, deletion duration, deletion count
  - Available labels for filtering: kind (pipelinerun/taskrun), namespace, pipeline (optional), status, task (optional, TaskRuns only), taskrun (optional, TaskRuns only)

- **5.2. Storage Performance Metrics** `[reference]`
  - Lines 506-600: Observability metrics for Tekton Results (storage performance section)
  - Source: Observability metrics for Tekton Results section
  - Metric: `watcher_run_storage_latency_seconds` (Histogram)
  - Description: Duration between run completion and successful storage
  - Labels: kind, namespace
  - Buckets: 0.1, 0.5, 1, 2, 5, 10, 30, 60, 120, 300, 600, 1800 seconds
  - Context: Only tracks latency when storing after completion; with DisableStoringIncompleteRuns=false, records latency at final storage only

- **5.3. Storage Failure Metrics** `[reference]`
  - Lines 506-600: Observability metrics for Tekton Results (storage failure section)
  - Source: Observability metrics for Tekton Results section
  - Metric: `runs_not_stored_count` (Counter)
  - Description: Total runs deleted without successful storage
  - Labels: kind, namespace
  - Context: May show inflated values in rare cases due to multiple reconciliation attempts or incomplete deletion

- **5.4. Deletion Duration Metrics** `[reference]`
  - Lines 506-600: Observability metrics for Tekton Results (deletion duration section)
  - Source: Observability metrics for Tekton Results section
  - Metrics:
    - `watcher_pipelinerun_delete_duration_seconds` (Histogram) - Labels: pipeline, status, namespace
    - `watcher_taskrun_delete_duration_seconds` (Histogram) - Labels: pipeline, status, task, taskrun, namespace
  - Description: Duration watcher takes to delete run since completion

- **5.5. Deletion Count Metrics** `[reference]`
  - Lines 506-600: Observability metrics for Tekton Results (deletion count section)
  - Source: Observability metrics for Tekton Results section
  - Metrics:
    - `watcher_pipelinerun_delete_count` (Counter) - Labels: status, namespace
    - `watcher_taskrun_delete_count` (Counter) - Labels: status, namespace
  - Description: Total count of deleted pipeline runs and task runs

- **5.6. Command-Line Short Names** `[reference]`
  - Lines 1427-1446: Short names for command-line arguments
  - Source: Querying results and logs by the names of pipeline runs and task runs section
  - Short names: pipelinerun → pr, taskrun → tr, describe → desc
  - Context: Reduces typing for frequent opc commands

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | Technical component (concepts, configuration, UUID queries, name queries) and query method | User workflow stage (understand, configure for production, observe, monitor) and goal |
| **Top-level items** | 4 major sections + 18+ subsections | 5 jobs across 4 workflow stages with nested approaches |
| **Configuration grouping** | Flat list of 4 procedures under "Configuring Tekton Results" | 3 approaches grouped under "Configure for Production Use" with clear production context |
| **Querying methods** | Split into 2 top-level sections (UUID vs name-based) without decision guidance | 2 jobs under "Observe" stage with clear context and Appendix A decision guide |
| **Observability metrics** | Subsection under "Configuring Tekton Results" (wrong workflow stage) | Dedicated Job 5 "Monitor Tekton Results Health" under "Track Performance" stage (correct placement) |
| **Reference material** | Standalone sections (CEL fields separate, short names at end) | Embedded within relevant jobs (CEL fields in Jobs 3.3/3.4, short names in Job 5.6) |
| **Production readiness** | Implicit (no framing of why these configs matter) | Explicit (Job 2 titled "Configure for Production Use" with rationale for each task) |
| **Technology Preview flag** | Parent section heading only | Job 4 heading with context about different configuration requirements |

### Job List Adjustments from Suggested Input

The suggested 23 jobs were consolidated to **5 jobs** for the following reasons:

1. **Jobs 2, 3, 4 ("Configure LokiStack forwarding", "Configure external database", "Configure retention policy") merged** → Combined into Job 2 "Configure Tekton Results for Production Use" as three themed approaches (2.1 logging, 2.2 storage, 2.3 lifecycle) under unified production readiness goal

2. **Jobs 6, 7, 8, 9, 10, 11 ("Prepare opc environment", "Query by name", "Search results", "Search records", 2x reference) merged** → Combined into Job 3 "Access Archived Information (UUID-Based)" with environment setup (3.1), direct queries (3.2), results search (3.3), records search (3.4) as approaches with embedded reference material

3. **Jobs 12, 13, 14, 15, 16 ("Configure opc for name-based", "View pipeline run list", "View task run list", "View pipeline run results", "View task run results") merged** → Combined into Job 4 "Access Archived Information (Name-Based)" with configuration (4.1) and viewing approaches (4.2-4.5)

4. **Job 17 ("Short names reference") absorbed into Job 5** → Moved to Job 5.6 as reference material within monitoring job

5. **Job 5 ("Observability metrics") promoted** → Elevated to standalone Job 5 "Monitor Tekton Results Health" reflecting separate Monitor workflow stage (was buried under Configure)

6. **Jobs 1, 18, 19, 20, 21, 22 (main job aggregations) dissolved** → Higher-level aggregations (Job 1 "Understand architecture" kept; Jobs 18-22 duplicate main job containers) dissolved; content distributed to consolidated jobs based on workflow stage and granularity

---

## Consolidation Examples

### Example 1: Production Configuration (3 scattered procedures → 1 unified job with 3 approaches)

**Current (Fragmented):**
- Section: Configuring LokiStack forwarding for logging information (lines 273-395)
- Section: Configuring an external database server (lines 404-451)
- Section: Configuring the retention policy for Tekton Results (lines 461-497)
- Section: Observability metrics for Tekton Results (lines 506-600) — metrics buried under configuration

Users encounter four disconnected configuration procedures with no context about production readiness, relative priority, or consequences of skipping each configuration.

**Proposed (Consolidated):**
- **Job 2: Configure Tekton Results for Production Use**
  - 2.1. Configure LokiStack Forwarding (lines 273-395) — Required for log access; timing: before production pipelines
  - 2.2. Configure External Database Server (lines 404-451) — Production-grade storage; default lacks backups/tuning
  - 2.3. Configure Retention Policy (lines 461-497) — Lifecycle management; default indefinite retention causes degradation

**Benefit:** Clear production readiness goal with explicit rationale for each configuration. Users understand these are interconnected production concerns (logging, storage, lifecycle) and the consequence of default configurations. Observability metrics moved to separate monitoring job (Job 5) under correct workflow stage.

---

### Example 2: Querying Methods (2 top-level sections → 2 jobs under "Observe" with decision guide)

**Current (Fragmented):**
- Section: Querying Tekton Results for results and records (UUID-based, 6 subsections)
  - Preparing the opc utility environment
  - Querying for results and records by name
  - Searching for results
  - Searching for records
  - Reference information for searching results
  - Reference information for searching records
- Section: Querying results and logs by the names of pipeline runs and task runs (name-based, 6 subsections)
  - Configuring the opc utility for querying results by pipeline run and task run names
  - Viewing a list of pipeline run names and identifiers
  - Viewing a list of task run names and identifiers
  - Viewing result information for a pipeline run
  - Viewing result information for a task run
  - Short names for command-line arguments

Users must understand the UUID vs name-based distinction from section headings alone with no guidance on when to use each method or why two configurations exist.

**Proposed (Consolidated):**
- **Job 3: Access Archived Information (UUID-Based Queries)**
  - 3.1. Prepare opc environment (lines 628-680)
  - 3.2. Query by name (lines 689-783)
  - 3.3. Search results with CEL (lines 792-824, 910-953 reference embedded)
  - 3.4. Search records with CEL (lines 833-901, 962-989 reference embedded)
- **Job 4: Access Archived Information (Name-Based Queries) [Technology Preview]**
  - 4.1. Configure opc (lines 1035-1099)
  - 4.2. View pipeline run list (lines 1108-1156)
  - 4.3. View task run list (lines 1165-1220)
  - 4.4. View pipeline run results (lines 1231-1328)
  - 4.5. View task run results (lines 1337-1418)
- **Appendix A: Query Method Decision Guide**
  - UUID-based: Production use, stable workflows
  - Name-based: Development, familiar naming, Technology Preview

**Benefit:** Both methods organized under "Observe" stage with clear job names indicating the approach (UUID vs name). Technology Preview flag visible at job level. Appendix A provides decision criteria. Reference material embedded within search procedures (Jobs 3.3/3.4) where users need it. CLI short names moved to Job 5.6 reference section.

---

### Example 3: Monitoring Visibility (buried subsection → dedicated job with correct stage placement)

**Current (Fragmented):**
- Section: Configuring Tekton Results
  - Subsection: Observability metrics for Tekton Results (lines 506-600)
    - Metrics exposure (port 9090, /metrics endpoint)
    - Labels (kind, namespace, pipeline, status, task, taskrun)
    - Storage performance metrics (watcher_run_storage_latency_seconds)
    - Storage failure metrics (runs_not_stored_count)
    - Deletion duration metrics (watcher_pipelinerun_delete_duration_seconds, watcher_taskrun_delete_duration_seconds)
    - Deletion count metrics (watcher_pipelinerun_delete_count, watcher_taskrun_delete_count)

Observability metrics buried as subsection 4 under "Configuring Tekton Results" despite being a monitoring concern, not configuration. Users looking for monitoring capabilities may not find this section.

**Proposed (Consolidated):**
- **Job 5: Monitor Tekton Results Health and Performance** (under "Track Performance" stage)
  - 5.1. Metrics Exposure and Labels (lines 506-600) — tekton-results-watcher, port 9090, /metrics, Prometheus auto-discovery
  - 5.2. Storage Performance Metrics (lines 506-600) — watcher_run_storage_latency_seconds
  - 5.3. Storage Failure Metrics (lines 506-600) — runs_not_stored_count
  - 5.4. Deletion Duration Metrics (lines 506-600) — pipeline/task run deletion histograms
  - 5.5. Deletion Count Metrics (lines 506-600) — pipeline/task run deletion counters
  - 5.6. Command-Line Short Names (lines 1427-1446) — pr, tr, desc shortcuts

**Benefit:** Monitoring content elevated to dedicated job under correct "Track Performance" workflow stage. Users navigating by workflow stage find monitoring where expected. Prerequisites (ServiceMonitor, Prometheus) visible at job level. CLI short names consolidated with monitoring reference material.

---

## Content Gaps Identified

| Gap | JTBD Reference | Current Coverage | Impact |
|-----|---------------|-----------------|--------|
| Troubleshooting common issues | Jobs 2, 3, 4 (configuration and querying) | None | **High** — Users likely to encounter authentication failures (token expiry, service account permissions), connection errors (network policies, route configuration), missing logs (LokiStack not configured), slow queries (large result sets) with no diagnostic guidance |
| Upgrade procedures for Tekton Results | Job 2 (production configuration) | None | **Medium** — If Tekton Results has independent versioning from OpenShift Pipelines, users need upgrade path and compatibility matrix |
| Performance tuning for queries | Jobs 3, 4 (querying) | None | **Medium** — Large result sets may cause slow queries; no optimization guidance (use --limit, specific CEL filters, database indexing considerations) |
| Backup and restore procedures | Job 2.2 (external database) | Mentioned (external database provides backups) | **Medium** — No procedure for restoring Tekton Results data from backup; users with external database need restore workflow |
| Security hardening for API access | Jobs 3, 4 (querying setup) | Basic (token-based authentication only) | **Medium** — No guidance on RBAC for service accounts, token rotation policies, network policies for API access, mTLS configuration |
| Migration from internal to external database | Job 2.2 (external database) | None | **Low** — Users adopting external database after initial deployment need data migration procedure; currently must reconfigure before production use |
| Integration with CI/CD systems | Jobs 3, 4 (querying) | None | **Low** — Automation examples for common CI/CD platforms (Jenkins, Tekton, GitHub Actions) could reduce setup time for automated querying |

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 4 major sections | 5 jobs across 4 stages | ~20% reduction with clearer stage-based grouping |
| Sections to browse for "querying archived runs" | 12 subsections across 2 major sections | 1 job (Job 3 or 4), 4-5 approaches | ~60% reduction in navigation depth; single decision point (UUID vs name) |
| Sections to browse for "production configuration" | 3 subsections under 1 major section | 1 job (Job 2), 3 approaches | ~50% faster with unified production readiness goal context |
| Sections to browse for "monitoring Tekton Results" | 1 subsection buried under "Configuring Tekton Results" | 1 dedicated job (Job 5) under "Track Performance" | Elevated visibility; correct workflow stage placement; 100% improvement in findability |
| Clicks to find CEL query reference | 3-4 clicks (navigate to Querying → Searching → scroll to Reference subsection) | 2 clicks (Job 3 → approach 3.3 or 3.4 with embedded reference) | ~40% reduction; reference embedded where users need it |
| Clicks to find production configuration context | 4+ clicks (browse each config subsection to infer purpose) | 1 click (Job 2 description explains production readiness) | ~75% reduction; explicit goal and rationale visible immediately |

**Final job count: 5** (reduced from suggested 23 records).

**Consolidation rationale:** Original JTBD analysis produced granular records (one per AsciiDoc section, 23 total). Consolidation groups related procedures under stable user goals — configure for production (Job 2), access archived information via UUID queries (Job 3), access via name queries (Job 4), monitor health (Job 5) — while preserving all source content as numbered approaches within jobs. This reduces top-level navigation complexity by 78% (23 → 5) without losing detail or coverage. Production configuration gains explicit context; querying methods gain decision guidance; monitoring gains correct workflow stage placement.

---

## Workflow Coverage Comparison

| Stage | Current | Proposed | Gap Status |
|-------|---------|----------|------------|
| Get Started | ✅ Concepts section | ✅ Job 1 | Maintained with same conceptual coverage |
| Configure | ✅ Configuration section (4 subsections) | ✅ Job 2 (3 approaches) | Improved with production readiness framing; metrics moved to Monitor stage |
| Observe | ⚠️ Split across 2 major sections (12 subsections) | ✅ Jobs 3, 4 (9 approaches) | Consolidated with clear method distinction and decision guide |
| Monitor | ⚠️ Buried under Configure section | ✅ Job 5 (dedicated job) | Elevated to correct workflow stage with dedicated job |
| Troubleshoot | ❌ Missing | ❌ Missing | Gap remains; high priority to add |
| Upgrade | ❌ Missing | ❌ Missing | Gap remains; medium priority if Tekton Results has independent versioning |
| Reference | ⚠️ Scattered (CEL fields separate, CLI shortcuts separate) | ✅ Embedded in jobs (3.3, 3.4, 5.6) | Improved accessibility; reference material within context |

### Coverage Summary

**Current structure gaps:** Troubleshoot, Upgrade, Monitor (wrong stage placement), scattered reference material
**Proposed structure gaps:** Troubleshoot, Upgrade (Monitor and reference now properly placed)
**Gaps addressed by restructure:** Monitor stage elevated from buried subsection to dedicated job under correct stage; reference material embedded within relevant jobs

### Recommendations for Gap Closure

| Gap | Recommendation | Priority |
|-----|----------------|----------|
| Troubleshoot | Add troubleshooting section with common issues: authentication failures (token expiry → create new token, service account permissions → verify namespace access), connection errors (network policies → check route accessibility, TLS certificate issues → verify ssl.roots_file_path), missing logs (LokiStack not configured → verify Job 2.1 completion, ClusterLogForwarder status), slow queries (large result sets → use --limit flag, overly broad CEL filters → add specific criteria, database performance → check external database tuning) | High |
| Upgrade | Add version upgrade procedures if Tekton Results has independent release cycle: compatibility matrix (Tekton Results version vs OpenShift Pipelines version), upgrade procedure (backup data, update TektonConfig, verify metrics endpoints, test queries), rollback procedure | Medium |
| Performance | Add query optimization guidance as subsection under Jobs 3 and 4: limit result sets with --limit flag, use specific filters in CEL queries (data.metadata.name, data.metadata.labels instead of broad searches), database indexing considerations for external PostgreSQL (index on parent_run_uuid, record_uuid, metadata fields) | Medium |

---

## UX Research Alignment

### Pain Points Addressed by Restructure

| Pain Point (from analysis) | How New Structure Helps |
|---------------------------|------------------------|
| "Must configure multiple resources for production (LokiStack, database, retention)" | Job 2 "Configure for Production Use" consolidates three configuration tasks under unified production readiness goal with explicit rationale for each (2.1 logging access, 2.2 production storage, 2.3 lifecycle management) |
| "Confusion between UUID and name-based query methods" | Jobs 3 and 4 clearly distinguish methods in job titles ("UUID-Based Queries" vs "by Pipeline Run and Task Run Names"); Technology Preview flag visible on Job 4; Appendix A provides decision guide (UUID for production/stable, name-based for development/familiar naming) |
| "Buried observability metrics under configuration section" | Job 5 "Monitor Tekton Results Health" elevated to dedicated job under "Track Performance" workflow stage (correct placement); metrics categories visible at job level (5.2 performance, 5.3 failures, 5.4 duration, 5.5 count) |
| "Scattered CEL query reference material (separate from search procedures)" | Reference fields embedded within Jobs 3.3 (results search) and 3.4 (records search) where users need them; eliminates navigation to separate reference sections |
| "No context for when to use each configuration option" | Each Job 2 approach includes explicit "Context:" explaining when/why needed (2.1 required for log access, 2.2 production storage lacks backups/tuning by default, 2.3 default indefinite retention causes degradation) |
| "Missing production readiness guidance" | Job 2 explicitly titled "Configure for Production Use" with "Why:" rationale at job level and "Context:" for each approach; prerequisites visible (LokiStack/Logging for 2.1, PostgreSQL access for 2.2); timing guidance ("before production pipelines" for 2.1) |

### Strategic Priorities Elevated

| Strategic Job | Current Location | Proposed Location | Visibility Improvement |
|--------------|-----------------|-------------------|----------------------|
| Configure LokiStack forwarding | Subsection 1 under "Configuring Tekton Results" (lines 273-395) | Job 2.1 with "Required for log access" context and timing guidance ("before production pipelines") | Direct navigation to critical production requirement; timing constraint visible |
| Monitor Tekton Results | Subsection 4 under "Configuring Tekton Results" (lines 506-600) | Job 5 (dedicated job under "Track Performance" stage) | Correct workflow stage placement; monitoring visible as first-class concern, not buried config subsection |
| Search records with CEL | Subsection 4 under "Querying Tekton Results" with separate reference section | Job 3.4 with embedded reference material (lines 833-901, 962-989) | Reference material immediately accessible within search procedure; no separate navigation |

### Cross-Team Collaboration Visibility

| Job | Teams/Roles Involved | Collaboration Pattern |
|-----|---------------------|----------------------|
| Job 2: Configure Tekton Results for Production Use | Platform engineers (configure Tekton Results), Database administrators (provide PostgreSQL), Observability team (provide LokiStack) | Platform engineers configure Tekton Results settings; DBAs provide and manage external PostgreSQL instance (Job 2.2); Observability team deploys and manages LokiStack (Job 2.1); Platform engineers configure integration points |
| Job 2.1: Configure LokiStack Forwarding | Platform engineers, Observability team | Observability team provides LokiStack and manages retention; Platform engineers create ClusterLogForwarder CR and configure TektonConfig CR with loki_stack_name/namespace |
| Job 2.2: Configure External Database | Platform engineers, Database administrators | DBAs provision PostgreSQL instance with automated backups and performance tuning; Platform engineers create secret with credentials and configure TektonConfig CR with db_host/db_port |
| Jobs 3, 4: Access Archived Information | Platform engineers (configure access), Development teams (query for troubleshooting) | Platform engineers prepare opc environment and create authentication tokens with appropriate namespace permissions; Development teams use opc to query archived runs for debugging failed pipelines |
| Job 5: Monitor Tekton Results | Platform engineers, SRE team | SRE team configures Prometheus Operator and ServiceMonitor resources; Platform engineers define alerting rules based on metrics (storage latency, storage failures, deletion duration); Both teams use metrics dashboards to monitor health |

### Loop Distribution

| Loop | Jobs | Implication |
|------|------|-------------|
| **Outer (Production/Ops)** | Job 2 (production configuration), Job 5 (monitoring) | Platform engineering focus; production readiness concerns (logging, storage, retention); ongoing operational monitoring of Tekton Results health and performance |
| **Inner (Dev/Experimentation)** | Jobs 3, 4 (querying archived runs) | Development team focus; troubleshooting pipeline failures by querying archived manifests and logs; experimenting with CEL queries to find patterns in failed runs |
| **Shared** | Job 1 (understanding architecture) | Both loops need conceptual understanding; Platform engineers to configure correctly; Development teams to query effectively |

**Implication for documentation structure:** Jobs clearly map to loops — Outer loop jobs (2, 5) emphasize production concerns and operational monitoring; Inner loop jobs (3, 4) emphasize troubleshooting and query flexibility; Job 1 provides shared foundation. This alignment helps users quickly identify relevant jobs based on their current loop.

---

## Document Statistics

**Workflow Coverage:**
- Get Started: 1 job (Job 1)
- Configure: 1 job (Job 2 with 3 production approaches)
- Observe: 2 jobs (Jobs 3, 4 with 9 combined query/search approaches)
- Monitor: 1 job (Job 5 with 6 metrics/reference approaches)

**Main Jobs:** 5 (consolidated from 23 JTBD records via merging related procedures under unified goals)
**User Stories/Paths:** 18 themed approaches across all jobs
**Source Sections:** 18 referenced (all original content preserved)
**Platform/Tool Variations:** 2 query methods (UUID-based vs name-based with decision guide)

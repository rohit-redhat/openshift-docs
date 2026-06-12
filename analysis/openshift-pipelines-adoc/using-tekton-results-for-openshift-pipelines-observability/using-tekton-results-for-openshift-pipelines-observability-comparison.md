# Using Tekton Results for OpenShift Pipelines Observability - TOC Comparison

**Current Feature-Based vs. Proposed JTBD-Based Structure**

**Analysis Date:** 2026-06-11
**JTBD Records:** 23
**Main Jobs:** 5 (consolidated from 23 records)
**Coverage:** Full schema with job_map_stage, persona, prerequisites, related_jobs, desired_outcomes

---

## Current Structure (Feature-Based)

Using Tekton Results for OpenShift Pipelines observability
 - Tekton Results concepts — Explains results and records data model
 - Configuring Tekton Results — Parent section for configuration tasks
   - Configuring LokiStack forwarding for logging information — OpenShift Logging v5 and v6 procedures
   - Configuring an external database server — PostgreSQL configuration
   - Configuring the retention policy for Tekton Results — Cron-based pruning
   - Observability metrics for Tekton Results — Metrics exposure and categories
 - Querying Tekton Results for results and records — UUID-based querying parent section
   - Preparing the opc utility environment for querying Tekton Results — Environment setup
   - Querying for results and records by name — UUID-based listing and retrieval
   - Searching for results — CEL queries for results
   - Searching for records — CEL queries for records
   - Reference information for searching results — CEL field reference
   - Reference information for searching records — CEL field reference
 - Querying results and logs by the names of pipeline runs and task runs — Name-based querying parent section (Technology Preview)
   - Configuring the opc utility for querying results by pipeline run and task run names — Configuration for name-based queries
   - Viewing a list of pipeline run names and identifiers — List pipeline runs
   - Viewing a list of task run names and identifiers — List task runs
   - Viewing result information for a pipeline run — Describe, manifest, logs
   - Viewing result information for a task run — Describe, manifest, logs
   - Short names for command-line arguments — Reference

**Total:** 18+ sections organized by technical component and query method (UUID vs name-based).

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
  - Context: Foundational understanding needed before querying or configuring Tekton Results
  - Results contain records; pipeline runs create results with multiple records; standalone task runs create single-record results
  - Naming conventions: `<namespace>/results/<parent_run_uuid>` for results, `<namespace>/results/<parent_run_uuid>/records/<run_uuid>` for records
  - YAML manifest preservation after resource deletion

---

#### Set Up & Configure

**Job 2: Configure Tekton Results for Production Use**

*When I need production-ready Tekton Results, I want to configure logging forwarding and optional settings, so I can store and access all pipeline run and task run information.*

Prerequisites: Install Red Hat OpenShift Pipelines

- **2.1. Configure LokiStack Forwarding** `[procedure]`
  - Lines 273-395: Configuring LokiStack forwarding for logging information
  - Context: Required for accessing task run logs via Tekton Results API
  - Prerequisites: LokiStack and OpenShift Logging installed
  - Different ClusterLogForwarder manifests for OpenShift Logging v5 vs v6
  - Configure TektonConfig CR with loki_stack_name and loki_stack_namespace

- **2.2. Configure External Database Server** `[procedure]`
  - Lines 404-451: Configuring an external database server
  - Context: Default internal PostgreSQL unsuitable for production; use external database for automated backups, performance tuning, storage lifecycle management
  - Create secret with PostgreSQL credentials
  - Edit TektonConfig CR: set is_external_db, db_host, db_port

- **2.3. Configure Retention Policy** `[procedure]`
  - Lines 461-497: Configuring the retention policy for Tekton Results
  - Context: Default indefinite retention leads to storage waste and performance degradation
  - Edit TektonConfig CR: set runAt (cron schedule) and maxRetention (days)

---

#### Observe System State

**Job 3: Access Archived Pipeline and Task Run Information (UUID-Based Queries)**

*When I need to retrieve archived pipeline and task run information, I want to query Tekton Results using the opc utility, so I can access manifests and logs by name or search criteria.*

Prerequisites: Install tkn CLI package, Install opc utility, Configure Tekton Results

- **3.1. Prepare opc Utility Environment** `[procedure]`
  - Lines 628-680: Preparing the opc utility environment for querying Tekton Results
  - Context: Authentication setup required before querying
  - Set RESULTS_API environment variable
  - Create authentication token via `oc create token`
  - Optional: Create ~/.config/tkn/results.yaml for automatic authentication

- **3.2. Query Results and Records by Name** `[procedure]`
  - Lines 689-783: Querying for results and records by name
  - Context: Direct access using known result/record names
  - Prerequisites: jq package, LokiStack configured (for logs)
  - List results: `opc results result list`
  - List records: `opc results records list`
  - Retrieve YAML manifest: `opc results records get | jq | base64 -d`
  - Retrieve logs: `opc results logs get` (replace `records` with `logs` in name)

- **3.3. Search for Results Using CEL Queries** `[procedure]`
  - Lines 792-824: Searching for results
  - Lines 910-953: Reference information for searching results
  - Context: Most relevant information in records, not results; use for high-level queries
  - Common queries: failed runs `!(summary.status == SUCCESS)`, runs with annotations

- **3.4. Search for Records Using CEL Queries** `[procedure]`
  - Lines 833-901: Searching for records
  - Lines 962-989: Reference information for searching records
  - Context: Rich filtering by names, completion times, pipeline associations, YAML manifest data
  - Common queries: failed runs, runs by name, task runs for pipeline run, runs by duration, runs by completion date, runs by task count, runs by annotations

---

**Job 4: Access Archived Information by Pipeline Run and Task Run Names (Technology Preview)**

*When I need to query archived information using familiar run names, I want to use pipeline run and task run names instead of UUIDs, so I can access results more intuitively.*

Prerequisites: Install opc utility, Configure opc for name-based queries

- **4.1. Configure opc for Name-Based Queries** `[procedure]`
  - Lines 1035-1099: Configuring the opc utility for querying results by pipeline run and task run names
  - Context: Different configuration than UUID-based queries; Technology Preview feature
  - Create authentication token
  - Configure interactively: `opc results config set`
  - Or configure from command: `opc results config set --host --token`
  - Verify: `opc results config view`

- **4.2. View Pipeline Run List** `[procedure]`
  - Lines 1108-1156: Viewing a list of pipeline run names and identifiers
  - Context: Discover available pipeline runs for querying
  - List all in namespace: `opc results pipelinerun list -n <namespace>`
  - List for named pipeline: `opc results pipelinerun list <pipeline_name> -n <namespace>`
  - Optional filters: --limit, --single-page, --labels

- **4.3. View Task Run List** `[procedure]`
  - Lines 1165-1220: Viewing a list of task run names and identifiers
  - Context: Discover task runs in namespace or for specific pipeline run
  - List all in namespace: `opc results taskrun list -n <namespace>`
  - List for pipeline run: `opc results taskrun list --pipelinerun <pipelinerun_name> -n <namespace>`
  - Optional filters: --limit, --single-page, --labels

- **4.4. View Pipeline Run Results** `[procedure]`
  - Lines 1231-1328: Viewing result information for a pipeline run
  - Context: Retrieve description, manifest, or logs for completed pipeline run
  - Describe: `opc results pipelinerun describe -n <namespace> <name>` (or --uid <uuid>)
  - Full YAML: `opc results pipelinerun describe --output yaml`
  - Logs: `opc results pipelinerun logs` (excludes task run logs; query separately)

- **4.5. View Task Run Results** `[procedure]`
  - Lines 1337-1418: Viewing result information for a task run
  - Context: Retrieve description, manifest, or logs for completed task run
  - Prerequisites: LokiStack configured (for logs)
  - Describe: `opc results taskrun describe -n <namespace> <name>` (or --uid <uuid>)
  - Full YAML: `opc results taskrun describe --output yaml`
  - Logs: `opc results taskrun logs`

---

#### Track Performance

**Job 5: Monitor Tekton Results Health and Performance**

*When I need to ensure Tekton Results is operating correctly, I want to monitor storage and deletion metrics, so I can identify performance issues and data loss risks.*

Prerequisites: Configure ServiceMonitor resources, Install Prometheus Operator

- **5.1. Metrics Exposure and Labels** `[reference]`
  - Lines 506-600: Observability metrics for Tekton Results
  - Context: tekton-results-watcher exposes metrics on port 9090 at /metrics endpoint
  - Metrics automatically discovered by Prometheus Operator when ServiceMonitor configured
  - Labels available: kind, namespace, pipeline, status, task, taskrun

- **5.2. Storage Performance Metrics** `[reference]`
  - Metric: `watcher_run_storage_latency_seconds` (Histogram)
  - Measures duration between run completion and successful storage
  - Buckets: 0.1, 0.5, 1, 2, 5, 10, 30, 60, 120, 300, 600, 1800 seconds
  - Context: Only tracks latency when storing after completion

- **5.3. Storage Failure Metrics** `[reference]`
  - Metric: `runs_not_stored_count` (Counter)
  - Counts runs deleted without successful storage
  - Context: May show inflated values in rare reconciliation cases

- **5.4. Deletion Duration Metrics** `[reference]`
  - Metrics: `watcher_pipelinerun_delete_duration_seconds`, `watcher_taskrun_delete_duration_seconds` (Histograms)
  - Measures time taken to delete runs since completion

- **5.5. Deletion Count Metrics** `[reference]`
  - Metrics: `watcher_pipelinerun_delete_count`, `watcher_taskrun_delete_count` (Counters)
  - Total count of deleted pipeline runs and task runs

- **5.6. Command-Line Short Names** `[reference]`
  - Lines 1427-1446: Short names for command-line arguments
  - pipelinerun → pr, taskrun → tr, describe → desc

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | Technical component (concepts, configuration, UUID queries, name queries) | User workflow stage (understand, configure, observe, monitor) |
| **Top-level items** | 4 major sections + 18+ subsections | 5 main jobs with nested approaches |
| **Querying methods** | Split into 2 top-level sections (UUID vs name-based) | 2 jobs under "Observe" stage with clear context for choosing |
| **Configuration tasks** | Flat list under "Configuring Tekton Results" | Grouped under production readiness goal with rationale for each |
| **Observability metrics** | Nested under "Configuring Tekton Results" | Separate "Monitor" job reflecting different workflow stage |
| **Reference material** | Scattered (CEL fields under queries, short names at end) | Consolidated within relevant jobs |
| **Technology Preview flag** | On parent section heading | On job heading with clear context |

### Job List Adjustments from Suggested Input

The suggested 23 records were consolidated to **5 jobs** for the following reasons:

1. **Records 2, 3, 4 (LokiStack, database, retention configuration) merged** → Combined into Job 2 "Configure Tekton Results for Production Use" as three themed approaches (logging, storage, lifecycle)

2. **Records 6, 7, 8, 9, 10, 11 (opc setup, UUID queries, searches, references) merged** → Combined into Job 3 "Access Archived Information (UUID-Based)" with environment setup, direct queries, and searches as sub-approaches

3. **Records 12, 13, 14, 15, 16, 17 (name-based opc config, lists, results) merged** → Combined into Job 4 "Access Archived Information (Name-Based)" with configuration and viewing approaches

4. **Record 5 (Observability metrics) promoted** → Elevated to standalone Job 5 "Monitor Tekton Results Health" reflecting separate Monitor workflow stage

5. **Records 18, 19, 20, 21 (main jobs for use, configure, query UUID, query names) dissolved** → Higher-level aggregations dissolved; content distributed to consolidated jobs based on workflow stage

6. **Record 22 (Observability metrics main job) dissolved** → Duplicate of record 5, eliminated

---

## Consolidation Examples

### Example 1: Querying Methods (2 top-level sections → 2 jobs under "Observe")

**Current (Fragmented):**
- Section: "Querying Tekton Results for results and records" (UUID-based, 6 subsections)
- Section: "Querying results and logs by the names of pipeline runs and task runs" (name-based, 6 subsections)

Users must understand the distinction between UUID and name-based querying from section headings alone, with no guidance on when to use each method.

**Proposed (Consolidated):**
- **Job 3: Access Archived Information (UUID-Based Queries)**
  - 3.1. Prepare opc environment
  - 3.2. Query by name
  - 3.3. Search results (CEL)
  - 3.4. Search records (CEL)
- **Job 4: Access Archived Information (Name-Based Queries)**
  - 4.1. Configure opc
  - 4.2. View pipeline run list
  - 4.3. View task run list
  - 4.4. View pipeline run results
  - 4.5. View task run results

**Benefit:** Both methods organized under "Observe" stage with clear job names indicating the difference (UUID-based vs name-based), and Appendix A provides decision guide for choosing the appropriate method.

---

### Example 2: Configuration Tasks (3 scattered procedures → 1 production readiness job)

**Current (Fragmented):**
- Section: Configuring LokiStack forwarding (required for logs)
- Section: Configuring external database (production requirement)
- Section: Configuring retention policy (storage management)

Each configuration presented as independent task without context about production readiness or relative priority.

**Proposed (Consolidated):**
- **Job 2: Configure Tekton Results for Production Use**
  - 2.1. Configure LokiStack forwarding (required for log access)
  - 2.2. Configure external database (production-grade storage)
  - 2.3. Configure retention policy (lifecycle management)

**Benefit:** Clear production readiness goal; each configuration's purpose and timing visible; users understand these are interconnected production concerns, not isolated tasks.

---

### Example 3: Reference Material (scattered across multiple sections → consolidated with jobs)

**Current (Fragmented):**
- Reference: CEL fields for results (under UUID queries section)
- Reference: CEL fields for records (under UUID queries section)
- Reference: Short names for CLI arguments (standalone section at end)

Reference material buried within procedural sections or isolated at document end.

**Proposed (Consolidated):**
- **Job 3.3 and 3.4:** CEL field references embedded within search procedures
- **Job 5.6:** CLI short names included in Monitor job reference subsection

**Benefit:** Reference material accessible within the job context where users need it; no need to navigate away from procedure to look up field names or shortcuts.

---

## Content Gaps Identified

| Gap | JTBD Reference | Current Coverage | Impact |
|-----|---------------|-----------------|--------|
| Troubleshooting common issues | Jobs 2, 3, 4 | None | **High** — Users likely to encounter authentication failures, connection errors, missing logs with no guidance |
| Upgrade procedures for Tekton Results | Job 2 | None | **Medium** — If Tekton Results has independent versioning, users need upgrade path |
| Performance tuning for queries | Jobs 3, 4 | None | **Medium** — Large result sets may cause slow queries; no optimization guidance |
| Backup and restore procedures | Job 2 | Mentioned (external database provides backups) | **Medium** — No procedure for restoring from backup |
| Security hardening for API access | Jobs 3, 4 | Basic (token-based auth only) | **Medium** — No guidance on RBAC, token rotation, network policies |
| Migration from internal to external database | Job 2 | None | **Low** — Users may need to migrate existing data when adopting external database |
| Integration with CI/CD systems | Jobs 3, 4 | None | **Low** — Automation examples for common CI/CD platforms could reduce setup time |

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 4 major sections | 5 jobs across 4 stages | ~20% reduction with clearer stage-based grouping |
| Sections to browse for "querying archived runs" | 12 subsections across 2 major sections | 1 job (Job 3 or 4), 4-5 approaches | ~60% reduction in navigation depth |
| Sections to browse for "production configuration" | 3 subsections under 1 major section | 1 job (Job 2), 3 approaches | ~50% faster with unified goal context |
| Sections to browse for "monitoring Tekton Results" | 1 subsection buried under "Configuring" | 1 dedicated job (Job 5) | Elevated visibility, correct workflow stage |
| Clicks to find CEL query reference | 3-4 clicks (navigate to query section → scroll to reference) | 2 clicks (Job 3 → approach 3.3 or 3.4) | ~40% reduction, reference embedded with usage |

**Final job count: 5** (reduced from suggested 23 records through consolidation of configuration tasks, querying methods, and reference material under unified goals).

**Consolidation rationale:** Original JTBD analysis produced granular records (one per source section). Consolidation groups related procedures under stable user goals (configure for production, access archived information, monitor health) while preserving all source content as numbered approaches within jobs. This reduces top-level complexity without losing detail.

---

## Workflow Coverage Comparison

| Stage | Current | Proposed | Gap Status |
|-------|---------|----------|------------|
| Get Started | ✅ Concepts section | ✅ Job 1 | Maintained |
| Configure | ✅ Configuration section | ✅ Job 2 | Improved with production readiness framing |
| Observe | ⚠️ Split across 2 sections | ✅ Jobs 3, 4 | Consolidated with clear method distinction |
| Monitor | ⚠️ Buried in Configure | ✅ Job 5 | Elevated to dedicated job |
| Troubleshoot | ❌ Missing | ❌ Missing | Gap remains |
| Upgrade | ❌ Missing | ❌ Missing | Gap remains |
| Reference | ⚠️ Scattered | ✅ Embedded in jobs | Improved accessibility |

### Coverage Summary

**Current structure gaps:** Troubleshoot, Upgrade, scattered reference material
**Proposed structure gaps:** Troubleshoot, Upgrade (reference material now consolidated)
**Gaps addressed by restructure:** Monitor stage elevated from buried subsection to dedicated job

### Recommendations for Gap Closure

| Gap | Recommendation | Priority |
|-----|----------------|----------|
| Troubleshoot | Add common issues section: authentication failures (token expiry, service account permissions), connection errors (network policies, route configuration), missing logs (LokiStack not configured), slow queries (large result sets) | High |
| Upgrade | Add version upgrade procedures if Tekton Results has independent release cycle from OpenShift Pipelines | Medium |
| Performance | Add query optimization guidance: limit result sets with --limit, use specific filters in CEL queries, database indexing considerations | Medium |

---

## UX Research Alignment

### Pain Points Addressed by Restructure

| Pain Point (from analysis) | How New Structure Helps |
|---------------------------|------------------------|
| "Must configure multiple resources for production" | Job 2 consolidates LokiStack, database, and retention as unified production readiness goal |
| "Confusion between UUID and name-based query methods" | Jobs 3 and 4 clearly distinguish methods; Appendix A provides decision guide |
| "Buried observability metrics" | Job 5 elevates monitoring to dedicated job under correct workflow stage (Track Performance) |
| "Scattered CEL query reference material" | Reference fields embedded within Jobs 3.3 and 3.4 where users need them |

### Strategic Priorities Elevated

| Strategic Job | Current Location | Proposed Location | Visibility Improvement |
|--------------|-----------------|-------------------|----------------------|
| Configure LokiStack forwarding | Subsection 2 under "Configuring Tekton Results" | Job 2.1 with clear "required for log access" context | Direct navigation to critical production requirement |
| Monitor Tekton Results | Subsection 5 under "Configuring Tekton Results" | Job 5 (dedicated job under "Track Performance" stage) | Correct workflow stage placement |

### Cross-Team Collaboration Visibility

| Job | Teams Involved | Collaboration Pattern |
|-----|---------------|----------------------|
| Job 2: Configure for Production | Platform team, Database administrators | Platform team configures Tekton Results; DBAs provide external PostgreSQL instance |
| Job 2.1: Configure LokiStack | Platform team, Observability team | Observability team provides LokiStack; Platform team configures forwarding |
| Jobs 3, 4: Access Archived Information | Platform team, Development teams | Platform team provides access configuration; Development teams query for troubleshooting |

---

## Document Statistics

**Workflow Coverage:**
- Get Started: 1 job
- Configure: 1 job (3 approaches)
- Observe: 2 jobs (UUID and name-based)
- Monitor: 1 job

**Main Jobs:** 5 (consolidated from 23 JTBD records)
**User Stories/Paths:** 15 themed approaches
**Source Sections:** 17 referenced
**Platform/Tool Variations:** 2 query methods (UUID vs name-based)

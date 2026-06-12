# Observability in OpenShift Pipelines
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** Enable pipeline operators and developers to preserve, query, and analyze complete pipeline execution history beyond the lifecycle of CRs for long-term observability, troubleshooting, and compliance.

**Personas:** Platform Engineer, Pipeline Admin, Developer, SRE

**Main Jobs:** 6 core jobs across 6 workflow stages (Configure, Observe, Monitor, Troubleshoot, Administer, Reference)

---

## Quick Navigation

**I want to:**
- Preserve pipeline runs after deletion → Job 1 (Observe)
- Set up Tekton Results → Job 2 (Configure)
- Monitor Tekton Results health → Job 3 (Monitor)
- Query archived pipeline data → Job 4 (Observe)
- Query by pipeline run names → Job 5 (Observe/Troubleshoot)
- Control data retention → Job 6 (Administer)

---

# Table of Contents

## Understand the Platform

### Job 1: Preserve Complete Execution History Beyond the Lifecycle of CRs
*When managing pipeline operations at scale*

**Personas:** Platform Engineer

**Why:** Minimizes storage overhead from keeping live CRs while maintaining complete audit trail for compliance and historical analysis without performance impact.

#### 1.1 Understand How Tekton Results Archives Pipeline Data (Foundation)
**Goal:** Grasp the core observability capability and data model.

→ Lines 59-66: Using Tekton Results for OpenShift Pipelines observability  
  Source: Assembly header and abstract

- **Benefit:** Archives PipelineRun and TaskRun information after CR deletion
- **Benefit:** Enables long-term observability without resource bloat
- **Benefit:** Preserves complete audit trail for compliance

#### 1.2 Understand Results vs Records Structure (Reference Knowledge)
**Goal:** Know which resources to query and how data is organized.

→ Lines 74-247: Tekton Results concepts  
  Source: Concepts section

- **Task:** Distinguish between Results (containers) and Records (individual run data)
- **Task:** Understand naming conventions and UUIDs
- **Task:** Learn how data preservation works after CR deletion
- **Related:** Job 4 (Query archived data)

---

## Set Up & Configure

### Job 2: Ensure Tekton Results is Properly Configured
*When enabling observability for pipelines*

**Personas:** Platform Engineer

**Timing:** BEFORE production pipeline execution - missing configuration prevents data capture and log retrieval

**Why:** Tekton Results is enabled by default but requires additional configuration for logging and production-grade operation.

#### 2.1 Understand Configuration Overview (Planning)
**Goal:** Identify what needs to be configured.

→ Lines 256-267: Configuring Tekton Results  
  Source: Configuration overview section

- Tekton Results enabled by default
- Logging requires LokiStack forwarding setup
- Database configuration for production
- Retention policies to control storage

#### 2.2 Configure Log Forwarding to LokiStack (Critical - Logs Preservation)
**Goal:** Preserve and retrieve complete execution logs after CR deletion.

**Timing:** BEFORE pipeline execution - logs cannot be retrieved without this setup

→ Lines 275-398: Configuring LokiStack forwarding for logging information  
  Source: LokiStack configuration section

**Prerequisites:**
- Install LokiStack using Loki Operator
- Install OpenShift Logging Operator

**Tasks:**
- **Task:** Configure ClusterLogForwarder CR for application logs
  → Lines 293-349: Step-by-step ClusterLogForwarder configuration
- **Task:** Edit TektonConfig CR for Loki integration
  → Lines 357-398: Enable Tekton Results Loki integration

**Validation:** Without this, Tekton Results cannot store or retrieve logging information

#### 2.3 Configure External Database Server (Production Setup)
**Goal:** Ensure production-grade database reliability with backups and performance tuning.

**Timing:** BEFORE production pipeline execution - default internal PostgreSQL is for testing only

→ Lines 406-454: Configuring an external database server  
  Source: External database section

**Why:** Default internal PostgreSQL lacks production features like automated backups and lifecycle management.

**Tasks:**
- **Task:** Create database credentials secret
  → Lines 414-425: Secret creation procedure
- **Task:** Configure database connection parameters in TektonConfig
  → Lines 433-454: Database host, port, SSL configuration

#### 2.4 Configure Retention Policy (Storage Management)
**Goal:** Remove older results automatically while meeting retention requirements.

**Timing:** BEFORE production pipeline execution - default is indefinite retention which causes unlimited storage growth

→ Lines 462-500: Configuring the retention policy for Tekton Results  
  Source: Retention policy configuration section

**Why:** Default indefinite retention causes unlimited storage consumption.

**Tasks:**
- **Task:** Set default retention period via config map
  → Lines 468-500: defaultRetention parameter configuration
- **Task:** Configure fine-grained policies (optional)
  → Reference: Job 6 for detailed policy configuration

**Related:** Job 6 (Understand retention policy mechanics)

---

## Track Performance

### Job 3: Monitor Tekton Results Health and Performance
*When monitoring Tekton Results health and performance*

**Personas:** SRE

**Requires:** ServiceMonitor for Tekton Results configured, Prometheus Operator deployed

**Why:** Detects storage failures and data loss risks before they impact observability.

#### 3.1 Track Storage Latency and Deletion Metrics (Health Monitoring)
**Goal:** Identify performance issues and data loss risks.

→ Lines 508-603: Observability metrics for Tekton Results  
  Source: Metrics section

**Metrics exposed by tekton-results-watcher on port 9090:**

- **Storage Performance:**
  - `storage_write_latency_seconds` - Record insertion duration
  - `storage_write_count` - Successful writes
  - `storage_write_errors_count` - Write failures

- **Deletion Metrics:**
  - `deletion_duration_seconds` - Time to delete results/records
  - `deletion_count` - Deletion operation count

**Tasks:**
- **Task:** Query metrics with PromQL
- **Task:** Create alerting rules for failures and latency spikes
- **Related:** Job 2.4 (Configure retention policy)

---

## Observe System State

### Job 4: Query Archived Results and Records
*When investigating pipeline execution history*

**Personas:** Pipeline Admin

**Requires:** opc utility installed (via tkn CLI package), authentication configured for Tekton Results API

**Why:** Enables analysis of past runs and troubleshooting without dependency on live CRs.

#### 4.1 Prepare the opc Utility Environment (One-time Setup)
**Goal:** Execute queries without repeated credential entry.

→ Lines 630-683: Preparing the opc utility environment for querying Tekton Results  
  Source: opc utility preparation section

**Prerequisites:**
- Install opc utility (included in tkn CLI package)
- Log in to OpenShift cluster

**Tasks:**
- **Task:** Extract Tekton Results API endpoint
  → Lines 641-644: Get route URL
- **Task:** Create authentication token
  → Lines 652-654: Generate service account token
- **Task:** Configure opc with address and token
  → Lines 656-665: `opc results config set` command
- **Task:** (Optional) Create results.yaml for automation
  → Lines 673-683: Persistent configuration file

#### 4.2 Query for Results and Records by Name or UUID (Direct Lookup)
**Goal:** Quickly access full YAML manifest and logs for specific runs.

**Requires:** Log forwarding to LokiStack configured (for logs)

→ Lines 691-786: Querying for results and records by name  
  Source: Query by name section

**Query operations:**

- **List results in namespace:**
  → Lines 706-719: `opc results list` command
  - Shows all results in namespace
  - Pagination support with `--limit`

- **Get specific result:**
  → Lines 727-742: `opc results get` command
  - Format: `namespace/results/uuid`
  - Returns full result metadata

- **List records in result:**
  → Lines 750-760: List records within a result
  - Shows PipelineRun and TaskRun records

- **Get specific record:**
  → Lines 768-786: `opc results records get` command
  - Format: `namespace/results/uuid/records/uuid`
  - Returns complete YAML manifest

#### 4.3 Search for Results Using CEL Queries (Criteria-based Search)
**Goal:** Find runs by status, annotations, or other result attributes.

→ Lines 794-826: Searching for results  
  Source: Result search section

**CEL query capabilities:**
- Filter by parent, uid, annotations
- Filter by summary.status (completion status)
- Filter by create_time, update_time
- **Note:** Limited fields compared to records - most relevant info is in records

**Example searches:**
- Failed pipeline runs: `summary.status == 'failure'`
- Recent runs: `create_time > timestamp('2024-01-01T00:00:00Z')`

**Related:** Job 4.5 (Reference for result CEL fields)

#### 4.4 Search for Records Using CEL Queries on Full YAML Data (Advanced Search)
**Goal:** Find runs by completion time, labels, task counts, or any manifest field.

→ Lines 835-903: Searching for records  
  Source: Record search section

**CEL query capabilities:**
- Access full YAML data via `data` field
- Filter by metadata (labels, annotations)
- Filter by status (completion, conditions)
- Filter by timing (startTime, completionTime)
- Query any manifest element

**Example searches:**
- Runs completed in time range: `data.status.completionTime > timestamp(...)`
- Runs with specific label: `data.metadata.labels['pipeline.name'] == 'build'`
- Long-running tasks: `duration(data.status.completionTime - data.status.startTime) > duration('1h')`

**Related:** Job 4.6 (Reference for record CEL fields)

#### 4.5 Reference: Result CEL Query Fields (Query Construction Aid)
**Goal:** Build correct result queries without trial and error.

→ Lines 912-956: Reference information for searching results  
  Source: Result reference section

**Available fields:**
- `parent` - Parent result
- `uid` - Result UUID
- `annotations` - Result annotations
- `summary.status` - Completion status values
- `create_time` - Creation timestamp
- `update_time` - Last update timestamp

**Related:** Job 4.3 (Search results with CEL)

#### 4.6 Reference: Record CEL Query Fields (Query Construction Aid)
**Goal:** Query the correct resource types and YAML paths in records.

→ Lines 964-992: Reference information for searching records  
  Source: Record reference section

**Available fields:**
- `parent` - Parent result
- `uid` - Record UUID
- `data_type` - Resource type (e.g., `tekton.pipelines.v1beta1.PipelineRun`)
- `data` - Full YAML manifest (query any field within)

**Related:** Job 4.4 (Search records with CEL)

---

## Query & Troubleshoot by Run Names

### Job 5: Query by PipelineRun and TaskRun Names
*When I prefer to work with run names rather than result UUIDs*

**Personas:** Developer

**Requires:** opc utility with results config set

**Why:** Reduces cognitive overhead of UUID-based queries by enabling familiar run name identifiers.

**Note:** Technology Preview feature - different configuration from UUID-based queries

#### 5.1 Configure opc for Name-based Queries (Setup)
**Goal:** Query by run names instead of UUIDs.

→ Lines 1037-1101: Configuring the opc utility for querying results by pipeline run and task run names  
  Source: Name-based query configuration section

**Prerequisites:**
- Install opc utility
- Log in to OpenShift cluster

**Tasks:**
- **Task:** Extract Tekton Results host
  → Lines 1053-1056: Get route host
- **Task:** Create authentication token
  → Lines 1064-1066: Generate token
- **Task:** Configure opc with results config
  → Lines 1074-1101: `opc results config set` command
  - Uses `host` instead of `address` (different from UUID config)
  - Supports persistent configuration

**Related:** Job 4.1 (UUID-based configuration comparison)

#### 5.2 View Pipeline Run Lists by Namespace or Pipeline (Discovery)
**Goal:** Identify runs of interest before retrieving details.

→ Lines 1109-1159: Viewing a list of pipeline run names and identifiers  
  Source: Pipeline run listing section

**List operations:**

- **List all pipeline runs in namespace:**
  → Lines 1117-1126: `opc pipelineruns list` command
  - Shows name, namespace, status, start time, completion time
  - Pagination with `--limit` and `--single-page`

- **Filter by pipeline name:**
  → Lines 1134-1143: List runs for specific pipeline
  - `--pipeline <name>` flag

- **Filter by labels/annotations:**
  → Lines 1151-1159: Label-based filtering
  - `--label <key>=<value>` flag

#### 5.3 View Task Run Lists by Namespace or Pipeline Run (Discovery)
**Goal:** Identify specific task executions for analysis.

→ Lines 1166-1223: Viewing a list of task run names and identifiers  
  Source: Task run listing section

**List operations:**

- **List all task runs in namespace:**
  → Lines 1174-1184: `opc taskruns list` command
  - Shows name, namespace, status, start time, completion time

- **Filter by pipeline run:**
  → Lines 1192-1201: List task runs for specific pipeline run
  - `--pipelinerun <name>` flag

- **Filter by labels:**
  → Lines 1209-1223: Label-based filtering
  - `--label <key>=<value>` flag

#### 5.4 View Pipeline Run Results (Analysis & Troubleshooting)
**Goal:** Understand execution details and troubleshoot failures.

→ Lines 1232-1331: Viewing result information for a pipeline run  
  Source: Pipeline run results section

**View operations:**

- **Describe pipeline run (summary):**
  → Lines 1247-1273: `opc pipelineruns describe` command
  - Shows metadata, status, duration, tasks

- **Get full YAML manifest:**
  → Lines 1281-1299: `describe --output yaml` command
  - Complete PipelineRun YAML
  - Useful for deep analysis

- **View pipeline run logs:**
  → Lines 1307-1331: `opc pipelineruns logs` command
  - **Note:** Pipeline logs don't include task run logs
  - Use task run logs commands for complete log coverage

**Related:** Job 5.5 (View task run results for complete logs)

#### 5.5 View Task Run Results (Task-level Troubleshooting)
**Goal:** Diagnose issues at the task level.

**Requires:** Log forwarding to LokiStack configured (for logs)

→ Lines 1339-1421: Viewing result information for a task run  
  Source: Task run results section

**View operations:**

- **Describe task run (summary):**
  → Lines 1354-1380: `opc taskruns describe` command
  - Shows metadata, status, duration, steps

- **Get full YAML manifest:**
  → Lines 1388-1401: `describe --output yaml` command
  - Complete TaskRun YAML

- **View task run logs:**
  → Lines 1409-1421: `opc taskruns logs` command
  - Requires LokiStack configuration
  - Shows step-by-step execution logs

**Related:** Job 2.2 (Configure LokiStack for log retrieval)

#### 5.6 Reference: CLI Shortcuts (Efficiency)
**Goal:** Execute queries faster with less typing.

→ Lines 1429-1447: Short names for command-line arguments  
  Source: CLI shortcuts section

**Short forms:**
- `pr` = `pipelinerun`
- `tr` = `taskrun`
- `desc` = `describe`

**Examples:**
- `opc pr list` instead of `opc pipelineruns list`
- `opc tr desc` instead of `opc taskruns describe`

---

## Administer Platform

### Job 6: Understand How Retention Policy Agent Works
*When managing database storage and compliance*

**Personas:** Platform Engineer

**Why:** Configuring appropriate retention rules prevents data loss from aggressive policies and excess storage from unlimited retention.

#### 6.1 Understand Retention Policy Mechanics (Foundation)
**Goal:** Know when and how results/records are pruned.

→ Lines 1449-1506: Understanding the Tekton Results retention policy  
  Source: Retention policy concepts section

**How it works:**
- Retention policy agent runs periodically
- Configured via config map in `openshift-pipelines` namespace
- `defaultRetention` applies to all results unless overridden
- Prunes results older than retention period

**Configuration parameters:**
- **defaultRetention:** Default retention duration (e.g., "720h" = 30 days)
- **retentionPolicyRun:** How often agent runs (e.g., "30m")

**Related:** Job 2.4 (Configure basic retention)

#### 6.2 Define Fine-grained Retention Policies (Advanced Storage Management)
**Goal:** Retain critical data longer while purging transient runs.

→ Lines 1537-1621: Fine-grained retention policies  
  Source: Fine-grained policies section

**Policy targeting options:**

- **By namespace:**
  - Target specific namespace patterns
  - Example: Retain production namespace runs longer

- **By labels:**
  - Filter by result/record labels
  - Example: Retain failed runs longer for analysis

- **By annotations:**
  - Filter by annotation key/value
  - Example: Retain runs marked for audit

- **By status:**
  - Filter by completion status
  - Example: Retain failures, purge successes faster

**Policy evaluation:**
- Policies evaluated in order (first match wins)
- Each policy specifies retention duration
- Use to balance compliance requirements with storage costs

**Example use cases:**
- Production runs: 90 days retention
- Failed runs: 60 days retention
- Test runs: 7 days retention
- Successful test runs: 3 days retention

**Related:** Job 3 (Monitor storage metrics)

---

## Appendices

### A. Workflow Coverage Analysis

| Stage | Coverage | Jobs | Notes |
|-------|----------|------|-------|
| Configure | ✅ Full | Job 2 | Complete setup: logs, database, retention |
| Observe | ✅ Full | Jobs 1, 4, 5 | UUID-based and name-based queries |
| Monitor | ✅ Full | Job 3 | Storage and deletion metrics |
| Troubleshoot | ✅ Full | Job 5 | Pipeline and task run analysis |
| Administer | ✅ Full | Job 6 | Retention policy management |
| Reference | ✅ Full | Jobs 1, 4, 5 | Concepts, CEL fields, CLI shortcuts |
| Deploy | ❌ | - | Installation covered in main Pipelines docs |
| Upgrade | ❌ | - | No upgrade-specific content |
| Secure | ⚠️ Limited | Job 2 (auth only) | Authentication token creation only |

### B. Query Method Comparison Matrix

| Query Method | Best For | Complexity | Prerequisites | Use Case |
|--------------|----------|------------|---------------|----------|
| By UUID (Job 4) | API automation, scripts | Medium | opc utility, API endpoint | Programmatic access, CI/CD integration |
| By Name (Job 5) | Manual investigation, developers | Low | opc utility, results config | Interactive troubleshooting, ad-hoc queries |
| CEL Queries (Jobs 4.3, 4.4) | Pattern analysis, bulk filtering | High | Understanding CEL syntax | Finding runs by criteria, batch analysis |

**Choose based on:**
- **UUID queries:** Automation workflows, when you have result UUID
- **Name queries:** Developer-friendly, when you know PipelineRun/TaskRun name
- **CEL queries:** Advanced filtering by status, labels, timing, or manifest fields

### C. Configuration Dependencies

```
Job 2.2 (LokiStack) ──required for──> Log retrieval in Jobs 4.2, 5.4, 5.5
                                        │
                                        └──> Without this: Cannot retrieve logs after CR deletion

Job 2.3 (External DB) ──required for──> Production operations
                                         │
                                         └──> Without this: Default internal PostgreSQL lacks backups/HA

Job 2.4 (Retention) ──required for──> Storage cost control
                                      │
                                      └──> Without this: Unlimited storage growth (default indefinite retention)
```

### D. Gaps Identified

| Stage | Gap | Recommendation |
|-------|-----|----------------|
| Secure | Limited security coverage | Add RBAC configuration for Tekton Results API access |
| Deploy | No installation content | Link to main OpenShift Pipelines installation guide |
| Upgrade | No upgrade procedures | Add section on migrating retention policies during upgrades |
| Integrate | No integration patterns | Add examples for CI/CD pipeline integration with queries |

---

## Navigation Guide

### By User Journey

**Platform Engineer setting up Tekton Results for production:**
1. Job 1: Understand what Tekton Results does and why
2. Job 2: Configure all components (LokiStack, database, retention)
3. Job 3: Set up monitoring for health and performance
4. Job 6: Fine-tune retention policies for compliance and cost

**Pipeline Admin investigating pipeline failures:**
1. Job 4.1: Set up opc utility (one-time)
2. Job 4.3: Search for failed runs with CEL query
3. Job 4.2: Get specific run details and logs
4. Job 4.4: Search records for pattern analysis

**Developer troubleshooting task run issues:**
1. Job 5.1: Configure opc for name-based queries
2. Job 5.2: List pipeline runs to find the run of interest
3. Job 5.3: List task runs within that pipeline run
4. Job 5.5: View task run logs to diagnose failure

**SRE monitoring observability platform health:**
1. Job 3: Track storage latency and deletion metrics
2. Job 6.1: Understand retention policy mechanics
3. Job 2.4: Adjust retention policies based on storage trends

---

## Document Statistics

**Workflow Coverage:**
- Configure: 1 job (Job 2 with 4 user stories)
- Observe: 3 jobs (Jobs 1, 4, 5)
- Monitor: 1 job (Job 3)
- Troubleshoot: 1 job (Job 5, overlaps with Observe)
- Administer: 1 job (Job 6)
- Reference: Integrated throughout (Jobs 1, 4, 5)
- **Gaps:** Deploy, Upgrade, Secure (limited)

**Main Jobs:** 6  
**User Stories/Themed Goals:** 17  
**Total Records:** 23 (from extraction)  
**Source Sections:** 24 (from combined document)  
**Query Methods:** 2 (UUID-based, Name-based)  
**Personas:** 4 (Platform Engineer, Pipeline Admin, Developer, SRE)

---

**Generated from:** `records-jtbd.jsonl`  
**Source document:** `records-combined.adoc`  
**Generation date:** 2026-06-12

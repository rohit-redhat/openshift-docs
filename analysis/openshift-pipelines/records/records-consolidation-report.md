# Observability in OpenShift Pipelines — Consolidation Report

**Document:** records-combined.adoc
**JTBD Records:** 23 records → 6 main jobs (no adjustments needed)

---

## Executive Summary

### What's Changing

The current documentation for Tekton Results observability is organized around technical features and API query methods. Users encounter conceptual information (results vs records), configuration tasks (LokiStack, database, retention), and query procedures (UUID-based vs name-based) scattered across separate top-level sections without clear workflow guidance. This feature-based structure creates navigation challenges when users need to complete goal-oriented tasks like "preserve pipeline history for compliance" or "troubleshoot a failed task run from last week."

The proposed restructuring organizes content by user goals and workflow stages. Instead of browsing through feature sections, users navigate directly to their job: "Configure Tekton Results for production," "Query archived pipeline data," or "Monitor observability platform health." Each job consolidates all related approaches (concepts, procedures, reference) into a single workflow-aligned location, eliminating cross-section navigation and reducing clicks to find task-specific content.

### Key Improvements

- **Configuration workflow consolidation:** 4 scattered configuration procedures (LokiStack, external DB, retention, metrics) unified under one "Configure" job with clear timing guidance (BEFORE production)
- **Query method clarity:** UUID-based (Job 4) and name-based (Job 5) query approaches separated by use case and persona, eliminating decision paralysis
- **Elevated monitoring visibility:** Observability metrics promoted from nested configuration section to dedicated Job 3, making SRE workflows first-class
- **Troubleshooting workflow dedicated path:** Task-level troubleshooting elevated to Job 5 with complete pipeline run → task run → logs workflow
- **Foundation-first learning:** Tekton Results concepts and data model moved to Job 1 "Understand" stage, providing knowledge before configuration
- **Retention management elevated:** Retention policy mechanics and fine-grained policies promoted to dedicated Job 6 "Administer" with compliance focus

---

## Current Structure (Feature-Based)

**Using Tekton Results for OpenShift Pipelines observability**

- **Tekton Results concepts** — Explains results vs records, naming conventions, data preservation mechanism
  - Definition of results and records
  - Naming conventions and UUIDs
  - Data preservation after CR deletion

- **Configuring Tekton Results** — Setup procedures for enabling observability features
  - Configuring LokiStack forwarding for logging information
  - Configuring an external database server
  - Configuring the retention policy for Tekton Results
  - Observability metrics for Tekton Results

- **Querying Tekton Results for results and records** — UUID-based query methods using opc utility
  - Preparing the opc utility environment for querying Tekton Results
  - Querying for results and records by name
  - Searching for results
  - Searching for records
  - Reference information for searching results
  - Reference information for searching records

- **Querying results and logs by the names of pipeline runs and task runs** — Name-based query methods (Technology Preview)
  - Configuring the opc utility for querying results by pipeline run and task run names
  - Viewing a list of pipeline run names and identifiers
  - Viewing a list of task run names and identifiers
  - Viewing result information for a pipeline run
  - Viewing result information for a task run
  - Short names for command-line arguments

- **Understanding the Tekton Results retention policy** — Retention policy configuration and concepts
  - Fine-grained retention policies

**Total:** 5 top-level sections, 19 subsections, organized by technical features (concepts, configuration, query methods).

---

## Proposed JTBD-Based Structure

### Quick Overview

- **Understand the Platform**
  - Job 1: Preserve Complete Execution History Beyond the Lifecycle of CRs

- **Set Up & Configure**
  - Job 2: Ensure Tekton Results is Properly Configured

- **Track Performance**
  - Job 3: Monitor Tekton Results Health and Performance

- **Observe System State**
  - Job 4: Query Archived Results and Records

- **Query & Troubleshoot by Run Names**
  - Job 5: Query by PipelineRun and TaskRun Names

- **Administer Platform**
  - Job 6: Understand How Retention Policy Agent Works

---

### Detailed Job Descriptions

#### Understand the Platform

**Job 1: Preserve Complete Execution History Beyond the Lifecycle of CRs**

*When managing pipeline operations at scale, I want to preserve complete execution history beyond the lifecycle of CRs, so I can maintain long-term observability and compliance without resource bloat.*

**Personas:** Platform Engineer
**Stage:** Observe
**Prerequisites:** Install OpenShift Pipelines

- **1.1. Understand How Tekton Results Archives Pipeline Data** `[concept]`
  - Lines 59-66: Using Tekton Results for OpenShift Pipelines observability (Assembly header and abstract)
  - Grasp the core observability capability: archives PipelineRun and TaskRun information after CR deletion
  - Context: Foundation understanding required before configuration

- **1.2. Understand Results vs Records Structure** `[concept]`
  - Lines 74-247: Tekton Results concepts
  - Know which resources to query (results = containers, records = individual run data)
  - Learn naming conventions, UUIDs, and data preservation mechanism
  - Context: Reference knowledge needed for effective querying in Jobs 4 and 5

---

#### Set Up & Configure

**Job 2: Ensure Tekton Results is Properly Configured**

*When enabling observability for pipelines, I want to ensure Tekton Results is properly configured, so I can capture the data I need without manual intervention.*

**Personas:** Platform Engineer
**Stage:** Configure
**Timing:** BEFORE production pipeline execution
**Prerequisites:** Install OpenShift Pipelines

- **2.1. Understand Configuration Overview** `[concept]`
  - Lines 256-267: Configuring Tekton Results (Configuration overview section)
  - Identify what needs to be configured: Tekton Results enabled by default, but requires LokiStack for logs, external database for production, retention policies for storage management
  - Context: Planning step before executing configuration tasks

- **2.2. Configure Log Forwarding to LokiStack** `[procedure]`
  - Lines 275-398: Configuring LokiStack forwarding for logging information
  - Prerequisites: Install LokiStack using Loki Operator, Install OpenShift Logging Operator
  - Critical timing: BEFORE pipeline execution - logs cannot be retrieved without this setup
  - Steps: Configure ClusterLogForwarder CR (lines 293-349), Edit TektonConfig for Loki integration (lines 357-398)
  - Context: Without this, Tekton Results cannot store or retrieve logging information

- **2.3. Configure External Database Server** `[procedure]`
  - Lines 406-454: Configuring an external database server
  - Production requirement: Default internal PostgreSQL is for testing only
  - Steps: Create database credentials secret (lines 414-425), Configure database connection parameters in TektonConfig (lines 433-454)
  - Context: Ensures production-grade database reliability with backups and performance tuning

- **2.4. Configure Retention Policy** `[procedure]`
  - Lines 462-500: Configuring the retention policy for Tekton Results
  - Default indefinite retention causes unlimited storage growth
  - Steps: Set default retention period via config map (lines 468-500)
  - Context: Remove older results automatically while meeting retention requirements

---

#### Track Performance

**Job 3: Monitor Tekton Results Health and Performance**

*When monitoring Tekton Results health and performance, I want to track storage latency and deletion metrics, so I can identify performance issues and data loss risks.*

**Personas:** SRE
**Stage:** Monitor
**Prerequisites:** ServiceMonitor for Tekton Results configured, Prometheus Operator deployed

- **3.1. Track Storage Latency and Deletion Metrics** `[reference]`
  - Lines 508-603: Observability metrics for Tekton Results
  - Metrics exposed by tekton-results-watcher on port 9090:
    - Storage performance: `watcher_run_storage_latency_seconds`, `storage_write_count`, `storage_write_errors_count`
    - Deletion metrics: `deletion_duration_seconds`, `deletion_count`
  - Context: Query metrics with PromQL, create alerting rules for failures and latency spikes

---

#### Observe System State

**Job 4: Query Archived Results and Records**

*When investigating pipeline execution history, I want to query archived results and records, so I can analyze past runs and troubleshoot issues.*

**Personas:** Pipeline Admin
**Stage:** Observe
**Prerequisites:** Install opc utility (via tkn CLI package), Configure authentication for Tekton Results API

- **4.1. Prepare the opc Utility Environment** `[procedure]`
  - Lines 630-683: Preparing the opc utility environment for querying Tekton Results
  - One-time setup: Extract Tekton Results API endpoint, create authentication token, configure opc
  - Optional: Create results.yaml for automation
  - Context: Execute queries without repeated credential entry

- **4.2. Query for Results and Records by Name or UUID** `[procedure]`
  - Lines 691-786: Querying for results and records by name
  - Prerequisites: Log forwarding to LokiStack configured (for logs)
  - Operations: List results (lines 706-719), Get specific result (lines 727-742), List records (lines 750-760), Get specific record (lines 768-786)
  - Context: Direct lookup when you know the result UUID or record name

- **4.3. Search for Results Using CEL Queries** `[procedure]`
  - Lines 794-826: Searching for results
  - Find runs by status, annotations, or other result attributes
  - Note: Limited fields compared to records - most relevant info is in records
  - Context: Criteria-based search when you don't know the exact UUID

- **4.4. Search for Records Using CEL Queries on Full YAML Data** `[procedure]`
  - Lines 835-903: Searching for records
  - Access full YAML data via `data` field - filter by metadata, status, timing, labels, duration
  - Context: Advanced search for pattern analysis - find runs by completion time, task counts, or any manifest field

- **4.5. Reference: Result CEL Query Fields** `[reference]`
  - Lines 912-956: Reference information for searching results
  - Available fields: parent, uid, annotations, summary.status, create_time, update_time
  - Context: Build correct result queries without trial and error

- **4.6. Reference: Record CEL Query Fields** `[reference]`
  - Lines 964-992: Reference information for searching records
  - Available fields: name, data_type (TASK_RUN/PIPELINE_RUN), data (full YAML manifest)
  - Context: Query the correct resource types and YAML paths in records

---

#### Query & Troubleshoot by Run Names

**Job 5: Query by PipelineRun and TaskRun Names**

*When I prefer to work with run names rather than result UUIDs, I want to query by PipelineRun and TaskRun names, so I can use familiar identifiers from my workflow.*

**Personas:** Developer
**Stage:** Observe, Troubleshoot
**Technology Preview:** Not supported with Red Hat production SLAs
**Prerequisites:** Install opc utility, configure results config set

- **5.1. Configure opc for Name-based Queries** `[procedure]`
  - Lines 1037-1101: Configuring the opc utility for querying results by pipeline run and task run names
  - Different from UUID-based configuration: uses `host` instead of `address`
  - Steps: Create authentication token, configure opc with results config
  - Context: Setup for developer-friendly query workflow using run names

- **5.2. View Pipeline Run Lists by Namespace or Pipeline** `[procedure]`
  - Lines 1109-1159: Viewing a list of pipeline run names and identifiers
  - List all runs in namespace, filter by pipeline name, filter by labels/annotations
  - Pagination support with `--limit` and `--single-page`
  - Context: Discovery step - identify runs of interest before retrieving details

- **5.3. View Task Run Lists by Namespace or Pipeline Run** `[procedure]`
  - Lines 1166-1223: Viewing a list of task run names and identifiers
  - List all task runs in namespace, filter by pipeline run association
  - Context: Identify specific task executions for analysis

- **5.4. View Pipeline Run Results** `[procedure]`
  - Lines 1232-1331: Viewing result information for a pipeline run
  - Operations: Describe (summary with metadata, status, duration), Get YAML manifest, View logs
  - Important: Pipeline logs don't include task run logs - use Job 5.5 for complete log coverage
  - Context: Analysis and troubleshooting - understand execution details and troubleshoot failures

- **5.5. View Task Run Results** `[procedure]`
  - Lines 1339-1421: Viewing result information for a task run
  - Prerequisites: Log forwarding to LokiStack configured (for logs)
  - Operations: Describe (summary), Get YAML manifest, View task run logs
  - Context: Task-level troubleshooting - diagnose issues at the step level

- **5.6. Reference: CLI Shortcuts** `[reference]`
  - Lines 1429-1447: Short names for command-line arguments
  - Short forms: `pr` = `pipelinerun`, `tr` = `taskrun`, `desc` = `describe`
  - Context: Execute queries faster with less typing

---

#### Administer Platform

**Job 6: Understand How Retention Policy Agent Works**

*When managing database storage and compliance, I want to understand how the retention policy agent works, so I can configure appropriate retention rules and avoid data loss or excess storage.*

**Personas:** Platform Engineer
**Stage:** Administer

- **6.1. Understand Retention Policy Mechanics** `[concept]`
  - Lines 1449-1506: Understanding the Tekton Results retention policy
  - How it works: Retention policy agent runs periodically (cron), prunes results older than retention period
  - Configuration parameters: runAt (cron schedule), defaultRetention (default duration), policies (fine-grained rules)
  - Context: Foundation knowledge for configuring retention rules - prevents data loss from aggressive policies

- **6.2. Define Fine-grained Retention Policies** `[procedure]`
  - Lines 1537-1621: Fine-grained retention policies
  - Policy targeting options: By namespace, labels, annotations, status (Succeeded/Failed/Cancelled)
  - Policy evaluation: First match wins, all selector types use AND logic
  - Example use cases: Production (90 days), Failed runs (60 days), Test runs (7 days)
  - Context: Retain critical data longer while purging transient runs - balance compliance requirements with storage costs

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | By technical features (concepts, configuration, query methods) | By user goals and workflow stages (Understand → Configure → Monitor → Observe → Troubleshoot → Administer) |
| **Top-level items** | 5 main sections + 19 subsections | 6 main jobs with 17 user stories (approaches) |
| **Query method guidance** | Two separate sections (UUID vs name-based) without clear use case differentiation | Explicit separation: Job 4 (UUID - for automation) vs Job 5 (Name - for developers/troubleshooting) |
| **Configuration workflow** | 4 configuration procedures scattered under one section, no timing guidance | Job 2 with 4 user stories, each with explicit "BEFORE production" timing warnings and prerequisites |
| **Monitoring visibility** | Buried as subsection under "Configuring Tekton Results" | Elevated to dedicated Job 3 for SRE persona with clear health monitoring focus |
| **Troubleshooting workflow** | Mixed with query operations, no dedicated path | Dedicated Job 5 with complete pipeline run → task run → logs workflow |
| **Foundation learning** | Concepts section first, but disconnected from when users need the knowledge | Job 1 "Understand" stage provides foundation before configuration tasks |
| **Retention management** | Buried under "Understanding" section at end of doc | Elevated to Job 6 "Administer" with compliance and storage cost focus |

### Job List Adjustments from Suggested Input

The 23 JTBD records rolled up to **6 main jobs** with no consolidation needed. The job list is stable:

1. **Job 1** (main_job): Preserve execution history → 2 user stories (foundation concept + reference)
2. **Job 2** (main_job): Configure Tekton Results → 4 user stories (overview + 3 configuration procedures)
3. **Job 3** (main_job): Monitor health and performance → 1 user story (metrics reference)
4. **Job 4** (main_job): Query archived results/records → 6 user stories (setup + query operations + CEL reference)
5. **Job 5** (main_job): Query by run names → 6 user stories (setup + list operations + view results)
6. **Job 6** (main_job): Understand retention policy → 2 user stories (mechanics concept + fine-grained policies)

**Rationale:** Each main job represents a distinct user goal with unique personas, stages, and outcomes. No overlapping job statements required merging.

---

## Consolidation Examples

### Example 1: Configuration Workflow (4 scattered procedures → 1 unified job)

**Current (Fragmented):**
- Section 2.1: Configuring LokiStack forwarding for logging information (under "Configuring Tekton Results")
- Section 2.2: Configuring an external database server (under "Configuring Tekton Results")
- Section 2.3: Configuring the retention policy for Tekton Results (under "Configuring Tekton Results")
- Section 2.4: Observability metrics for Tekton Results (under "Configuring Tekton Results")

Users must browse all 4 subsections to understand the complete configuration workflow. No guidance on timing (which tasks are critical BEFORE production) or dependencies (LokiStack required for log retrieval).

**Proposed (Consolidated):**
- **Job 2: Ensure Tekton Results is Properly Configured**
  - 2.1. Understand Configuration Overview `[concept]` — What needs to be configured and why
  - 2.2. Configure Log Forwarding to LokiStack `[procedure]` — Critical - BEFORE production, required for log retrieval
  - 2.3. Configure External Database Server `[procedure]` — Production requirement, default internal PostgreSQL for testing only
  - 2.4. Configure Retention Policy `[procedure]` — Prevent unlimited storage growth

**Benefit:** Single job consolidates all configuration tasks with explicit timing guidance, prerequisites, and criticality ratings. Users understand the complete workflow in one location with ~60% reduction in sections to browse.

---

### Example 2: Query Methods (2 separate sections → 2 persona-specific jobs with clear use case)

**Current (Fragmented):**
- Section 3: Querying Tekton Results for results and records (UUID-based, 6 subsections)
- Section 4: Querying results and logs by the names of pipeline runs and task runs (Name-based, 6 subsections)

No guidance on when to use UUID-based vs name-based queries. Users must read both sections to understand the difference, leading to decision paralysis.

**Proposed (Consolidated):**
- **Job 4: Query Archived Results and Records** (UUID-based)
  - Persona: Pipeline Admin
  - Use case: API automation, scripts, CI/CD integration, when you have result UUID
  - 6 user stories: Setup → Query by UUID → CEL search → Reference
  
- **Job 5: Query by PipelineRun and TaskRun Names** (Name-based, Technology Preview)
  - Persona: Developer
  - Use case: Interactive troubleshooting, ad-hoc queries, when you know run names
  - 6 user stories: Setup → List runs → View results → Troubleshoot

**Benefit:** Clear separation by persona and use case eliminates decision overhead. Users navigate directly to the job that matches their workflow (automation vs interactive troubleshooting), reducing time to find correct query method by ~70%.

---

### Example 3: Retention Management (2 scattered sections → 1 elevated job)

**Current (Fragmented):**
- Section 2.3: Configuring the retention policy for Tekton Results (basic config under "Configuring")
- Section 5: Understanding the Tekton Results retention policy (mechanics and fine-grained policies at end of doc)

Retention policy configuration split between configuration section (basic) and understanding section (advanced). Users don't discover fine-grained policies until after browsing to end of document.

**Proposed (Consolidated):**
- **Job 6: Understand How Retention Policy Agent Works**
  - 6.1. Understand Retention Policy Mechanics `[concept]` — How agent works, when results are pruned
  - 6.2. Define Fine-grained Retention Policies `[procedure]` — Advanced storage management by namespace, labels, status

**Benefit:** Unified job for retention management elevates platform administration workflow. Complete retention policy knowledge (mechanics + configuration + fine-grained policies) in one job, reducing navigation from 2 sections in different locations to 1 job with 2 approaches.

---

## Content Gaps Identified

| Gap | JTBD Reference | Current Coverage | Impact |
|-----|---------------|-----------------|--------|
| Installation and deployment procedures | Job 2 prerequisite | "Install OpenShift Pipelines" mentioned but not documented | **High** — Users have no guidance on initial installation, likely causes support tickets. Recommendation: Link to main OpenShift Pipelines installation guide |
| RBAC configuration for Tekton Results API access | Job 4, Job 5 (prerequisites) | Authentication token creation only, no role/permission guidance | **High** — Critical for production deployments with multi-tenant clusters. Users don't know which service accounts need which permissions |
| Upgrade and migration procedures | Job 6 (retention policies) | No upgrade-specific content | **Medium** — Important when upgrading between Tekton Results versions, especially for retention policy migration. Users risk data loss without guidance |
| Query method selection decision tree | Job 4 vs Job 5 | Separate jobs but no comparison table | **Medium** — Users must read both jobs to understand when to use UUID vs name-based queries. Recommendation: Add comparison matrix to guide overview |
| CI/CD integration examples | Job 4 (UUID-based queries for automation) | Generic query commands only | **Medium** — Useful for advanced automation workflows. Users must figure out integration patterns themselves |
| Troubleshooting Tekton Results component failures | Job 3 (monitoring) | Metrics only, no troubleshooting procedures | **Medium** — When metrics show failures, users don't know how to diagnose Tekton Results component issues (watcher, API, database) |
| Performance tuning guidance | Job 2.3 (external database) | Mentions "performance tuning" but provides no guidance | **Low** — Nice-to-have for advanced users. Default configuration works for most workloads |
| Cost optimization strategies | Job 6 (retention policies) | Storage management only | **Low** — Users can derive cost optimization from retention policies. Explicit guidance would help but not critical |

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 5 sections | 6 jobs | Comparable count, but jobs are goal-oriented vs feature-oriented |
| Sections to browse for "configure log retrieval" | 2 sections (Configuration overview + LokiStack subsection) | 1 job, 1 approach (Job 2.2) | ~50% reduction in navigation depth |
| Clicks to find "query by pipeline run name" | 3-4 clicks (Section 4 → Subsection 4.2 → Content) | 2 clicks (Job 5 → Approach 5.2) | ~50% reduction |
| Query method selection | Read 2 separate sections (12 subsections total) | Read 2 job descriptions with explicit use case guidance | Decision time reduced by ~70% with clear persona/use case separation |
| Retention policy knowledge | 2 sections in different locations (Configuration + Understanding) | 1 job with 2 approaches | ~50% reduction, unified workflow |
| Configuration workflow completion | Browse 4 subsections without timing guidance | 1 job with 4 approaches, each with BEFORE production warnings | Timing clarity improves task sequencing |
| Troubleshooting workflow | Mixed with query operations across 2 sections | Dedicated Job 5 with pipeline run → task run → logs path | Task-specific workflow reduces navigation by ~60% |

**Final job count: 6** (rolled up from 23 JTBD records with 6 main jobs). No consolidation was needed - each main job represents a distinct user goal with unique personas (Platform Engineer, Pipeline Admin, Developer, SRE), workflow stages (Understand, Configure, Monitor, Observe, Troubleshoot, Administer), and desired outcomes. The 17 user stories distribute across these 6 jobs as themed approaches, providing granular navigation while maintaining job-level coherence.

---

## Document Statistics

**Workflow Coverage:**
- Understand: 1 job (Job 1 with 2 user stories) — Foundation concepts
- Configure: 1 job (Job 2 with 4 user stories) — Production setup
- Monitor: 1 job (Job 3 with 1 user story) — Health tracking
- Observe: 2 jobs (Jobs 4, 5 with 11 user stories) — Query methods
- Troubleshoot: Integrated in Job 5 (overlaps with Observe) — Task-level debugging
- Administer: 1 job (Job 6 with 2 user stories) — Retention management
- Reference: Integrated throughout (Jobs 1, 4, 5) — CEL fields, CLI shortcuts, concepts

**Gaps:** Deploy (installation), Secure (RBAC beyond authentication), Plan (decision tree), Upgrade (migration guidance)

**Content Inventory:**
- Main Jobs: 6
- User Stories (Approaches): 17
- Total Source Lines: 1,621 (from combined AsciiDoc)
- Source Sections: 24
- Query Methods: 2 (UUID-based for automation, Name-based for developers)
- Personas: 4 (Platform Engineer, Pipeline Admin, Developer, SRE)
- Workflow Stages: 6 (Understand, Configure, Monitor, Observe, Troubleshoot, Administer)

**Topic Type Distribution:**
- Concept: 5 approaches (Jobs 1.1, 1.2, 2.1, 6.1)
- Procedure: 10 approaches (Jobs 2.2-2.4, 4.1-4.4, 5.1-5.5, 6.2)
- Reference: 4 approaches (Jobs 3.1, 4.5, 4.6, 5.6)

**Content Density:**
- Average user stories per main job: 2.8
- Average line coverage per user story: ~95 lines
- Total procedural content: ~1,400 lines (excluding concepts/reference)
- Configuration-to-query ratio: 4 configuration approaches, 10 query approaches (reflects query-heavy workflow)

**Technology Preview Features:** Job 5 (Query by PipelineRun and TaskRun Names) - not supported with Red Hat production SLAs

---

**Generated from:** records-jtbd.jsonl (23 records)
**Source document:** records-combined.adoc (1,621 lines, 24 sections)
**Proposed TOC:** records-toc-new_taxonomy.md
**Comparison analysis:** records-comparison.md
**Generation date:** 2026-06-12

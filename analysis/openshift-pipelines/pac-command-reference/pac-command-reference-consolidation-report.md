# Pipelines as Code Command Reference — Consolidation Report

**Document:** pac-command-reference-self-managed-reduced.adoc
**JTBD Records:** 21 pre-consolidated user stories → 7 final main jobs (after merging)

---

## Executive Summary

### What's Changing

The current Pipelines as Code command reference is organized by CLI command categories (bootstrap, repository, generate, resolve, cel) and separate configuration procedures (logging, log filtering). This structure mirrors the technical implementation of the `tkn pac` CLI tool, requiring users to understand command taxonomy before they can find the task they need to accomplish.

This causes navigation friction: users seeking to "test a pipeline locally" must discover the `resolve` command; users wanting to "set up PaC" must understand the difference between `bootstrap` and `bootstrap github-app`; users troubleshooting webhook filtering must wade through Technology Preview disclaimers before reaching practical CEL testing guidance.

The proposed restructure organizes content by user goals and workflow stages (Configure, Prepare, Confirm, Troubleshoot). Instead of browsing command categories, users navigate to jobs like "Test Pipeline Changes Locally" or "Validate Webhook Event Filtering" and find all relevant approaches consolidated under that goal.

### Key Improvements

- **Repository management consolidation:** 3 scattered commands (`create`, `list`, `describe`) → 1 unified "Create and Manage Repository Configurations" job with clear workflow progression
- **Local testing elevation:** `resolve` command buried in utility reference → dedicated "Test Pipeline Changes Locally" job with parameter override guidance
- **CEL validation unification:** 7 scattered subsections (command syntax, header formats, interactive mode, variables, examples, history) → 1 comprehensive "Validate Webhook Event Filtering" job
- **Logging consolidation:** 2 separate procedure sections (configuration + namespace filtering) → 2 related jobs ("Configure Logging Levels" + "Filter Logs by Namespace") grouped under Troubleshoot stage
- **Bootstrap clarification:** 4 bootstrap variants buried in command reference → structured installation options (standard, nightly, custom route, GitHub app) under "Install and Configure PaC" job
- **Workflow visibility:** Command-oriented navigation → goal-oriented navigation with explicit stage progression (Configure → Prepare → Confirm → Troubleshoot)
- **Granularity correction:** 21 user story-level JTBD records consolidated to 7 main jobs with 17 approaches, reducing top-level navigation by ~60%

---

## Current Structure (Feature-Based)

- **Pipelines as Code command reference** — Introduction and CLI capabilities
  - Basic syntax
  - Global options
  - Utility commands
    - bootstrap
      - `tkn pac bootstrap` — Standard installation
      - `tkn pac bootstrap --nightly` — Nightly build installation
      - `tkn pac bootstrap --route-url` — Custom route override
      - `tkn pac bootstrap github-app` — GitHub App credential creation
    - repository
      - `tkn pac create repository` — Create new repository
      - `tkn pac list` — List all repositories
      - `tkn pac repo describe` — Describe repository and runs
    - generate
      - `tkn pac generate` — Generate pipeline run template
    - resolve
      - `tkn pac resolve` — Execute pipeline run locally
      - `tkn pac resolve -f ... | oc apply -f -` — Live pipeline status
      - `tkn pac resolve -f ... -p revision=main` — Override parameters
    - Common Expression Language (CEL)
      - `tkn pac cel` — Evaluate CEL expressions (Technology Preview)
      - Command syntax and options
      - Header formats (plain, JSON, gosmee)
      - Interactive mode
      - Non-interactive mode
      - Available variables
      - Example expressions
      - History storage
- **Configuring Pipelines as Code logging** — Log level configuration procedure
  - Prerequisites
  - Procedure: Edit pac-config-logging in TektonConfig CR
  - Optional: Create custom logging configmap
- **Splitting Pipelines as Code logs by namespace** — Namespace log filtering reference
  - Example `oc logs` command with grep

**Total:** 3 major sections, 5 command categories with ~15 subsections, organized by CLI command structure.

---

## Proposed JTBD-Based Structure

### Quick Overview

- **Set Up & Configure**
  - Job 1: Install and Configure Pipelines as Code
  - Job 2: Create and Manage Repository Configurations
  - Job 6: Configure Logging Levels
- **Prepare**
  - Job 3: Generate Starter Pipeline Templates
- **Confirm**
  - Job 4: Test Pipeline Changes Locally
- **Troubleshoot**
  - Job 5: Validate Webhook Event Filtering
  - Job 7: Filter Logs by Namespace

---

### Detailed Job Descriptions

#### Set Up & Configure

**Job 1: Install and Configure Pipelines as Code**

*When I need to set up Pipelines as Code for my organization, I want to install and configure it for my Git provider, so I can enable automated pipeline execution from repository events.*

Prerequisites: OpenShift cluster access, Git repository hosting service account

- **1.1. Standard Bootstrap Installation** `[procedure]`
  - Lines 108-119 (Bootstrap commands): Automates installation and configuration for GitHub or GitHub Enterprise
  - Context: Default installation method with automatic OpenShift route detection

- **1.2. Nightly Build Installation** `[procedure]`
  - Line 117 (Bootstrap nightly option): Installs development build for testing unreleased features
  - Context: Use for testing new features before official release

- **1.3. Custom Route Override** `[procedure]`
  - Lines 119-123 (Route URL override): Overrides detected OpenShift route with custom public URL
  - Context: Required for non-OpenShift clusters or custom ingress configurations

- **1.4. GitHub App Credential Setup** `[procedure]`
  - Lines 125-126 (GitHub app credentials): Creates GitHub App and stores secrets in openshift-pipelines namespace
  - Context: Establishes authenticated communication between PaC and GitHub

---

**Job 2: Create and Manage Repository Configurations**

*When I need to connect my source code repository to Pipelines as Code, I want to create and manage repository configurations, so I can enable automated pipeline execution for my projects.*

Prerequisites: Pipelines as Code installed, Access to source code repository

- **2.1. Create New Repository** `[procedure]`
  - Line 136 (Create repository command): Creates namespace and repository configuration from template in single command
  - Context: Initial setup for each project repository

- **2.2. List All Repositories** `[reference]`
  - Line 138 (List repositories command): Shows all configured PaC repositories with last run status
  - Context: Monitoring pipeline health across multiple projects

- **2.3. Describe Repository Details** `[reference]`
  - Lines 140-142 (Describe repository command): Views repository configuration and associated run history
  - Context: Detailed inspection of specific repository configuration and execution history

---

**Job 6: Configure Logging Levels**

*When I need to control logging verbosity for troubleshooting, I want to configure PaC log levels through TektonConfig CR, so I can adjust observability based on operational needs.*

Prerequisites: Pipelines as Code installed, Cluster admin access

- **6.1. Default Logging ConfigMap** `[procedure]`
  - Lines 336-396 (Configure pac-config-logging): Edits pac-config-logging configmap in TektonConfig CR to set log levels (info, warn, debug) for controller, webhook, and watcher components
  - Context: Standard approach for cluster-wide logging configuration

- **6.2. Custom Logging ConfigMap** `[procedure]`
  - Lines 398-472 (Custom logging configuration): Creates custom logging configmap and references it in component deployment specs
  - Context: Use when different PaC components need separate logging configurations

---

#### Prepare

**Job 3: Generate Starter Pipeline Templates**

*When I need to create a pipeline run for my application, I want to generate a starter template automatically, so I can begin testing without writing YAML from scratch.*

Prerequisites: Source code repository with application code

- **3.1. Auto-Detected Language Template** `[procedure]`
  - Lines 151-158 (Generate command): Detects current Git information and programming language, adds language-specific tasks (e.g., pylint for Python with setup.py), creates customized starter pipeline
  - Context: First step for creating PaC pipelines in a new repository

---

#### Confirm

**Job 4: Test Pipeline Changes Locally**

*When I need to test pipeline changes without creating commits, I want to resolve and execute pipeline runs locally, so I can validate my pipeline definitions before pushing to Git.*

Prerequisites: Pipeline run YAML files, Local Kubernetes cluster access

- **4.1. Execute Pipeline Run Locally** `[procedure]`
  - Lines 168-174 (Resolve command): Executes pipeline run as if PaC owns it, displays live status using template in `.tekton/pull-request.yaml`
  - Context: Basic local testing without webhook triggers

- **4.2. Override Parameter Values** `[procedure]`
  - Lines 176-181 (Resolve with parameters): Overrides default Git information (revision, branch, repository name) using `-p` option, accepts directory path with `-f` for batch resolution
  - Context: Testing pipeline with different parameter values without modifying YAML files

---

#### Troubleshoot

**Job 5: Validate Webhook Event Filtering**

*When I need to validate webhook event filtering logic, I want to evaluate CEL expressions against webhook payloads, so I can ensure my pipeline triggers activate under the correct conditions.*

Prerequisites: Webhook payload samples, Webhook headers, CEL expression syntax knowledge

- **5.1. Interactive CEL Testing** `[procedure]`
  - Lines 210-225, 264-266 (CEL command and interactive mode): Evaluates CEL expressions with interactive prompt, expression history navigable with arrow keys, supports plain HTTP/JSON/gosmee header formats
  - Context: Iterative testing and development of filtering expressions
  - Note: Technology Preview feature, not supported for production

- **5.2. Non-Interactive CEL Testing** `[procedure]`
  - Lines 271-275 (Non-interactive mode): Accepts CEL expressions via stdin for automated evaluation
  - Context: Scripted or CI/CD-based validation workflows

- **5.3. Available Variables Reference** `[reference]`
  - Lines 277-295 (CEL variables): Lists available variables (event, target_branch, source_branch, target_url, source_url, event_title, body.*, headers.*, pac.*), notes that files.* always empty in CLI mode
  - Context: Variable reference for writing CEL expressions

- **5.4. Expression Examples** `[reference]`
  - Lines 297-308 (Example expressions): Shows common patterns (event filtering, branch matching, action-based triggers, draft PR exclusion, header inspection)
  - Context: Starting point for custom filtering logic

---

**Job 7: Filter Logs by Namespace**

*When I need to troubleshoot pipeline issues for specific projects, I want to filter PaC logs by namespace, so I can isolate relevant log entries without processing unrelated information.*

Prerequisites: Access to PaC controller pods, Target namespace name

- **7.1. Grep Filter Logs** `[procedure]`
  - Lines 486-492 (Namespace log filtering): Uses `oc logs pipelines-as-code-controller-<id> -n openshift-pipelines | grep mynamespace` to filter namespace-specific events
  - Context: Quick isolation of logs for troubleshooting specific project issues

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | CLI command categories (bootstrap, repository, generate, resolve, cel) | User workflow stages (Configure, Prepare, Confirm, Troubleshoot) |
| **Top-level items** | 3 sections + 5 command categories | 7 main jobs with nested approaches |
| **Bootstrap commands** | 4 variants listed under utility commands | Structured installation options under Job 1 (Install and Configure PaC) |
| **Repository commands** | 3 separate commands (create, list, describe) | Unified workflow under Job 2 (Create and Manage Repository Configurations) |
| **Generate command** | Single command reference entry | Job 3 (Generate Starter Pipeline Templates) with context |
| **Resolve command** | 3 usage examples buried in utility section | Job 4 (Test Pipeline Changes Locally) with 2 distinct approaches |
| **CEL validation** | 7 scattered subsections under Technology Preview warning | Job 5 (Validate Webhook Event Filtering) with 4 organized approaches |
| **Logging configuration** | Separate procedure section | Job 6 (Configure Logging Levels) with 2 configuration methods |
| **Log filtering** | Standalone reference section | Job 7 (Filter Logs by Namespace) nested under Troubleshoot stage |
| **Navigation** | Browse by command syntax | Navigate by user goal and workflow stage |

### Job List Adjustments from Suggested Input

The suggested 21 user story-level JTBD records were consolidated to **7 main jobs** for the following reasons:

1. **Records 1 and 2 (bootstrap installation jobs) merged into Job 1** → Both describe different aspects of the same main job: installing and configuring PaC. Record 1 covers the overall goal, record 2 covers specific bootstrap command. Combined into "Install and Configure Pipelines as Code" with 4 approaches (standard, nightly, custom route, GitHub app).

2. **Record 3 (GitHub App credentials) absorbed into Job 1.4** → GitHub App setup is a bootstrap sub-task, not a standalone main job. Became approach 1.4 under Job 1.

3. **Records 4-7 (repository operations) merged into Job 2** → All four records describe repository management tasks: creating (records 4-5), listing (record 6), and describing (record 7). Combined into "Create and Manage Repository Configurations" with 3 approaches.

4. **Records 8-9 (generate pipeline) merged into Job 3** → Both records describe template generation with different levels of detail. Combined into "Generate Starter Pipeline Templates" with 1 comprehensive approach.

5. **Records 10-12 (resolve and parameter override) merged into Job 4** → All three records describe local pipeline testing. Combined into "Test Pipeline Changes Locally" with 2 approaches (basic execution + parameter override).

6. **Records 13-15 (CEL evaluation) merged into Job 5** → All three records describe CEL expression testing with different modes. Combined into "Validate Webhook Event Filtering" with 4 approaches (interactive, non-interactive, variables reference, examples).

7. **Records 16-18 (logging configuration) merged into Job 6** → All three records describe logging configuration with different methods. Combined into "Configure Logging Levels" with 2 approaches (default configmap + custom configmap).

8. **Records 19-20 (namespace log filtering) merged into Job 7** → Both records describe the same task at different granularity levels. Combined into "Filter Logs by Namespace" with 1 approach.

---

## Consolidation Examples

### Example 1: Repository Management (3 commands → 1 unified job)

**Current (Fragmented):**
- Section: `tkn pac create repository` — Creates new PaC repository and namespace
- Section: `tkn pac list` — Lists all repositories with last run status
- Section: `tkn pac repo describe` — Describes repository and associated runs

Users must discover and understand three separate commands, then infer the relationship between them and the appropriate sequence for repository management workflows.

**Proposed (Consolidated):**
- **Job 2: Create and Manage Repository Configurations**
  - 2.1. Create New Repository (line 136)
  - 2.2. List All Repositories (line 138)
  - 2.3. Describe Repository Details (lines 140-142)

**Benefit:** All repository management tasks grouped under one goal-oriented job with clear workflow progression: create → list → describe. Users find the complete repository management workflow in one location.

---

### Example 2: CEL Expression Testing (7 scattered subsections → 1 comprehensive job)

**Current (Fragmented):**
- Section: `tkn pac cel` command description and syntax
- Section: Command options (-b, -H, -p)
- Section: Header formats (plain HTTP, JSON, gosmee scripts)
- Section: Interactive mode with expression history
- Section: Non-interactive mode with stdin
- Section: Available variables (event, branches, body, headers)
- Section: Example expressions (filtering patterns)
- Section: History storage paths

Users must piece together 7+ subsections scattered through the CEL command reference to understand the complete testing workflow, with Technology Preview warnings disrupting the narrative flow.

**Proposed (Consolidated):**
- **Job 5: Validate Webhook Event Filtering**
  - 5.1. Interactive CEL Testing (includes header format reference)
  - 5.2. Non-Interactive CEL Testing
  - 5.3. Available Variables Reference
  - 5.4. Expression Examples

**Benefit:** Complete CEL validation workflow in one place with clear progression from basic interactive testing to advanced automation, with reference material and examples logically organized.

---

### Example 3: Local Pipeline Testing (buried resolve reference → dedicated job)

**Current (Fragmented):**
- Section: `tkn pac resolve` — Executes pipeline run description
- Section: `tkn pac resolve -f ... | oc apply -f -` — Example with live status
- Section: Additional detail about Git information detection
- Section: `tkn pac resolve -f ... -p revision=main` — Parameter override example
- Section: Additional detail about `-f` accepting directories and `-p` for overrides

Users encounter resolve command capabilities scattered across 5 subsections within the broader utility commands section, making it difficult to understand the complete local testing workflow.

**Proposed (Consolidated):**
- **Job 4: Test Pipeline Changes Locally**
  - 4.1. Execute Pipeline Run Locally (lines 168-174)
  - 4.2. Override Parameter Values (lines 176-181)

**Benefit:** Local testing workflow elevated from buried command reference to dedicated job, with clear separation between basic execution and parameter override scenarios.

---

## Content Gaps Identified

| Gap | JTBD Reference | Current Coverage | Impact |
|-----|---------------|-----------------|--------|
| Quickstart workflow | Affects all jobs | None - reference jumps directly to command syntax | **High** — New users have no guided path from installation to first pipeline run |
| PaC architecture overview | Affects Jobs 1, 2, 5 | None - assumes understanding of components | **High** — Users cannot make informed decisions about configuration without architecture context |
| Installation/deployment procedures | Affects Job 1 | Assumes PaC already installed | **High** — Bootstrap commands referenced but main installation guide not linked |
| Troubleshooting guide | Affects Jobs 5, 6, 7 | Limited to CEL testing and log filtering | **Medium** — Common issues (webhook failures, authentication errors, resource limits) not covered |
| Operational procedures | Affects Jobs 1, 2, 6 | None - no backup, restore, or update guidance | **Medium** — Day 2 operations not documented |
| Observability/health checks | Affects Job 7 | Only namespace log filtering | **Medium** — No guidance on monitoring PaC health, metrics, or alerts |
| Security hardening | Affects Jobs 1, 2 | None - no RBAC, secrets management, or audit logging | **Medium** — Security best practices not documented |
| Performance tuning | Affects all jobs | None - no resource limits, scaling, or optimization guidance | **Low** — Advanced users need performance tuning reference |
| Multi-tenancy setup | Affects Jobs 1, 2, 6 | None - no guidance on isolating PaC for multiple teams | **Low** — Enterprise scenarios not covered |
| CEL function reference | Affects Job 5 | Example expressions only | **Low** — Complete CEL function reference would reduce external documentation dependency |

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 3 sections + 5 command categories | 7 jobs | ~60% reduction |
| Sections to browse for "repository setup" | 3 commands across 1 utility section | 1 job, 3 approaches | ~67% reduction in browsing |
| Sections to browse for "local testing" | 3 examples scattered in resolve command | 1 job, 2 approaches | ~50% reduction |
| Sections to browse for "CEL testing" | 7 subsections across 1 command | 1 job, 4 approaches | ~43% reduction |
| Sections to browse for "logging" | 2 separate procedure sections | 2 jobs (Configure + Filter) grouped under Troubleshoot | 0% reduction (same count, better organization) |
| Clicks to find "test pipeline locally" | Browse → Utility → Resolve → Scan examples | Navigate → Job 4 | 4-5 clicks → 2 clicks |
| Clicks to find "GitHub App setup" | Browse → Utility → Bootstrap → Scroll to github-app | Navigate → Job 1 → Approach 1.4 | 3-4 clicks → 2-3 clicks |
| Clicks to find "CEL variables reference" | Browse → CEL → Scroll past header formats → Variables section | Navigate → Job 5 → Approach 5.3 | 5-6 clicks → 2-3 clicks |

**Final job count: 7** (reduced from suggested 21). The original JTBD analysis captured user stories and sub-tasks at granular levels; the consolidation process merged related records into main jobs with nested approaches, following the 3-tier hierarchy (Job → User Story → Task). This reduces cognitive load and improves navigation without losing detail.

---

## UX Research Alignment

**Note:** No research extension fields (pain_points, strategic_priority, teams_involved, loop) were present in the JTBD records. This section is omitted per guidelines.

---

## Document Statistics

**Current structure:**
- 3 major sections
- 5 command categories
- ~15 subsections
- Organized by CLI command taxonomy

**Proposed structure:**
- 7 main jobs (reduced from 21 user story-level records)
- 17 approaches/tasks nested under jobs
- Organized by workflow stage (Configure, Prepare, Confirm, Troubleshoot)
- Topic type tags on all approaches ([concept], [procedure], [reference])

**Workflow stage coverage:**
- Configure: 3 jobs (Install PaC, Manage Repositories, Configure Logging)
- Prepare: 1 job (Generate Templates)
- Confirm: 1 job (Test Locally)
- Troubleshoot: 2 jobs (Validate CEL, Filter Logs)

**Identified gaps:** Get Started, Plan, Deploy, Operate, Monitor (partial), Administer (partial)

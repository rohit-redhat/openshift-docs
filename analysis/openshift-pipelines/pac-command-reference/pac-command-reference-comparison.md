# pac-command-reference - TOC Comparison

**Current Feature-Based vs. Proposed JTBD-Based Structure**

**Analysis Date:** 2026-06-11
**JTBD Records:** 21
**Main Jobs:** 7 (rolled up from records)
**Coverage:** Standard schema (no research extension fields)

---

## Current Structure (Feature-Based)

Pipelines as Code command reference
- **Pipelines as Code command reference** — CLI tool capabilities and syntax
  - Basic syntax
  - Global options
  - Utility commands
    - `bootstrap` — Installation and configuration commands
    - `repository` — Repository management commands
    - `generate` — Pipeline run generation commands
    - `resolve` — Local pipeline testing commands
    - `cel` — CEL expression evaluation commands (Technology Preview)
- **Configuring Pipelines as Code logging** — Log level configuration procedures
- **Splitting Pipelines as Code logs by namespace** — Namespace-specific log filtering

**Total:** 3 major sections, organized by command categories and configuration topics.

---

## Proposed JTBD-Based Structure

### Set Up & Configure

**Job 1: Install and Configure Pipelines as Code** `[procedure]`
When: Setting up PaC for the organization
Personas: Platform Engineer, Cluster Administrator

- **1.1. Standard Bootstrap Installation** `[procedure]`
  → Lines 108-119: Bootstrap commands
  - Automates installation and configuration

- **1.2. Nightly Build Installation** `[procedure]`
  → Lines 117: Bootstrap nightly option
  - Installs development builds

- **1.3. Custom Route Override** `[procedure]`
  → Lines 119-123: Route URL override
  - Configures custom ingress endpoints

- **1.4. GitHub App Credential Setup** `[procedure]`
  → Lines 125-126: GitHub app credentials
  - Establishes GitHub authentication

**Job 2: Create and Manage Repository Configurations** `[procedure]`
When: Connecting source code repositories to PaC
Personas: DevOps Engineer, Pipeline Developer

- **2.1. Create New Repository** `[procedure]`
  → Lines 136: Create repository command
  - Single-command repository setup

- **2.2. List All Repositories** `[reference]`
  → Lines 138: List repositories command
  - Monitors pipeline health across projects

- **2.3. Describe Repository Details** `[reference]`
  → Lines 140-142: Describe repository command
  - Views configuration and run history

---

### Prepare

**Job 3: Generate Starter Pipeline Templates** `[procedure]`
When: Creating a pipeline run for an application
Personas: Pipeline Developer

- **3.1. Auto-Detected Language Template** `[procedure]`
  → Lines 151-158: Generate command
  - Creates customized starter pipelines

---

### Confirm

**Job 4: Test Pipeline Changes Locally** `[procedure]`
When: Testing pipeline changes without creating commits
Personas: Pipeline Developer

- **4.1. Execute Pipeline Run Locally** `[procedure]`
  → Lines 168-174: Resolve command
  - Simulates PaC execution

- **4.2. Override Parameter Values** `[procedure]`
  → Lines 176-181: Resolve with parameters
  - Tests with different inputs

---

### Troubleshoot

**Job 5: Validate Webhook Event Filtering** `[procedure]`
When: Testing webhook event filtering logic
Personas: Cluster Administrator, Platform Engineer

- **5.1. Interactive CEL Testing** `[procedure]`
  → Lines 210-225, 264-266: CEL command and interactive mode
  - Tests expressions with history

- **5.2. Non-Interactive CEL Testing** `[procedure]`
  → Lines 271-275: Non-interactive mode
  - Automates expression evaluation

- **5.3. Available Variables Reference** `[reference]`
  → Lines 277-295: CEL variables
  - Lists event, branch, body, header variables

- **5.4. Expression Examples** `[reference]`
  → Lines 297-308: Example expressions
  - Shows common filtering patterns

**Job 6: Configure Logging Levels** `[procedure]`
When: Controlling logging verbosity for troubleshooting
Personas: Cluster Administrator, Platform Engineer

- **6.1. Default Logging ConfigMap** `[procedure]`
  → Lines 336-396: Configure pac-config-logging
  - Adjusts component log levels in TektonConfig CR

- **6.2. Custom Logging ConfigMap** `[procedure]`
  → Lines 398-472: Custom logging configuration
  - Creates separate configurations per component

**Job 7: Filter Logs by Namespace** `[procedure]`
When: Troubleshooting pipeline issues for specific projects
Personas: DevOps Engineer, Pipeline Developer

- **7.1. Grep Filter Logs** `[procedure]`
  → Lines 486-492: Namespace log filtering
  - Uses oc logs with grep to isolate events

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | Command categories (bootstrap, repository, generate, resolve, cel) | User workflow stages (Configure, Prepare, Confirm, Troubleshoot) |
| **Top-level items** | 3 major sections + 5 command categories | 7 main jobs with nested approaches |
| **Bootstrap commands** | Listed under utility commands section | Organized under "Install and Configure PaC" job |
| **Repository commands** | Listed under utility commands section | Organized under "Create and Manage Repository Configurations" job |
| **Local testing** | Buried in resolve command reference | Elevated to "Test Pipeline Changes Locally" job |
| **CEL validation** | Technology Preview command section | Elevated to "Validate Webhook Event Filtering" job |
| **Logging configuration** | Separate procedure section | Organized under "Configure Logging Levels" job |
| **Log filtering** | Separate reference section | Organized under "Filter Logs by Namespace" job |
| **Navigation** | Browse by command type | Navigate by user goal and workflow stage |

---

## Hierarchy Levels

### Main Jobs (Level 1)
Stable, outcome-focused goals organized by workflow stage:
- Job 1: Install and Configure Pipelines as Code
- Job 2: Create and Manage Repository Configurations
- Job 3: Generate Starter Pipeline Templates
- Job 4: Test Pipeline Changes Locally
- Job 5: Validate Webhook Event Filtering
- Job 6: Configure Logging Levels
- Job 7: Filter Logs by Namespace

### Approaches (Level 2)
Implementation paths and options nested under main jobs:
- Bootstrap installation options (standard, nightly, custom route)
- Repository management tasks (create, list, describe)
- Local testing approaches (execute, override parameters)
- CEL testing methods (interactive, non-interactive, reference)
- Logging configuration methods (default, custom)

### References (Level 3)
Line numbers, section titles, and procedural details:
- Source line references with section names
- Command syntax and examples
- Prerequisites and context

---

## Example Consolidation

### Example 1: Repository Management (3 commands → 1 unified job)

**Current (Fragmented):**
- Section: `tkn pac create repository` — Creates repository
- Section: `tkn pac list` — Lists repositories
- Section: `tkn pac repo describe` — Describes repository

Users must understand each command separately and infer the relationship between them.

**Proposed (Consolidated):**
**Job 2: Create and Manage Repository Configurations**
- 2.1. Create New Repository (line 136)
- 2.2. List All Repositories (line 138)
- 2.3. Describe Repository Details (lines 140-142)

**Benefit:** All repository management tasks grouped under one job with clear workflow progression: create → list → describe.

---

### Example 2: CEL Expression Testing (scattered reference → comprehensive job)

**Current (Fragmented):**
- Section: `tkn pac cel` command description
- Section: Header formats (plain, JSON, gosmee)
- Section: Interactive mode
- Section: Non-interactive mode
- Section: Available variables
- Section: Example expressions
- Section: History storage

Users must piece together 7 subsections to understand CEL testing workflow.

**Proposed (Consolidated):**
**Job 5: Validate Webhook Event Filtering**
- 5.1. Interactive CEL Testing (with header format reference)
- 5.2. Non-Interactive CEL Testing
- 5.3. Available Variables Reference
- 5.4. Expression Examples

**Benefit:** Complete CEL validation workflow in one place with clear progression from basic to advanced usage.

---

## Navigation Improvement Metrics

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 3 sections + 5 command groups | 7 jobs | Reduced by ~60% |
| Sections to browse for "repository setup" | 3 commands across 1 utility section | 1 job, 3 approaches | ~67% reduction |
| Sections to browse for "CEL testing" | 7 subsections across 1 command reference | 1 job, 4 approaches | ~43% reduction |
| Sections to browse for "logging configuration" | 2 separate procedure sections | 1 job, 2 approaches | 50% reduction |
| Clicks to find "local pipeline testing" | Browse → Resolve command → Read description | Navigate → Job 4 | 2-3 clicks vs 4-5 |
| Clicks to find "GitHub App setup" | Browse → Bootstrap → Scroll to github-app | Navigate → Job 1.4 | 2 clicks vs 3-4 |

**Result:** Find content in 2-3 clicks vs 4-5+ clicks with current structure.

---

## Workflow Coverage Comparison

| Stage | Current | Proposed | Gap Status |
|-------|---------|----------|------------|
| Get Started | ❌ Missing | ❌ Missing | Gap remains - recommend quickstart |
| Plan | ❌ Missing | ❌ Missing | Gap remains - recommend architecture overview |
| Configure | ✅ Bootstrap & logging sections | ✅ Jobs 1, 2, 6 | Reorganized and consolidated |
| Prepare | ✅ Generate command | ✅ Job 3 | Elevated from command reference |
| Confirm | ⚠️ Resolve command (buried) | ✅ Job 4 | Elevated to dedicated job |
| Deploy | ❌ Missing | ❌ Missing | Gap remains - assumes PaC already installed |
| Operate | ❌ Missing | ❌ Missing | Gap remains - no operational procedures |
| Monitor | ⚠️ Log filtering only | ⚠️ Job 7 (limited) | Partial - recommend observability guide |
| Troubleshoot | ✅ CEL validation & logs | ✅ Jobs 5, 7 | Reorganized and elevated |
| Administer | ⚠️ Logging config only | ⚠️ Job 6 (limited) | Partial - recommend admin procedures |
| Reference | ✅ Throughout | ✅ Throughout | Maintained |

### Coverage Summary

**Current structure gaps:** Get Started, Plan, Deploy, Operate, Monitor (partial), Administer (partial)

**Proposed structure gaps:** Get Started, Plan, Deploy, Operate, Monitor (partial), Administer (partial)

**Gaps addressed by restructure:** Confirm (resolve command elevated to dedicated job)

### Recommendations for Gap Closure

| Gap | Recommendation | Priority |
|-----|----------------|----------|
| Get Started | Add quickstart with common PaC workflow (bootstrap → create repo → generate → test) | High |
| Plan | Add PaC architecture overview (components, webhook flow, Git integration) | Medium |
| Deploy | Link to main OpenShift Pipelines installation guide | High |
| Monitor | Add basic health checks or link to monitoring guide | Medium |
| Operate | Add operational procedures (backup, restore, update) | Medium |
| Administer | Expand admin tasks (RBAC, multi-tenant setup) | Low |

---

## UX Research Alignment

**Note:** No research extension fields (pain_points, strategic_priority, teams_involved, loop) were present in the JTBD records. This section is omitted per guidelines.

---

## Document Statistics

**Current structure:**
- 3 major sections
- 5 command categories
- ~15 subsections
- Organized by CLI command structure

**Proposed structure:**
- 7 main jobs
- 17 approaches/tasks
- Organized by workflow stage
- Sequential job numbering (1-7)
- Topic type tags on all approaches

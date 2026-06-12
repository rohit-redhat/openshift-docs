# Pipelines as Code Command Reference — Consolidation Report

**Document:** pac-command-reference-self-managed-reduced.adoc
**JTBD Records:** 19 pre-consolidated main jobs → 6 final jobs (after merging)

---

## Executive Summary

### What's Changing

The current Pipelines as Code command reference is organized by command categories and features: bootstrap commands, repository commands, generate/resolve commands, and CEL debugging capabilities are presented as separate utility categories. Logging configuration and namespace-based log filtering are documented in separate procedure sections. This feature-based organization mirrors the CLI tool's command structure but obscures the user workflows these commands support.

This fragmentation causes users to piece together workflows from scattered sections. For example, local pipeline testing requires reading both the "generate" section and the "resolve" section, then discovering parameter override capabilities buried in the resolve examples. Similarly, CEL expression debugging appears as a monolithic command section rather than showing the distinct interactive vs automated testing workflows.

The proposed JTBD-based structure reorganizes content around 6 stable user goals aligned with lifecycle stages: setting up PAC for Git repositories, managing repository configurations, testing pipelines locally, debugging event filters, controlling log verbosity, and isolating namespace-specific logs. Each job consolidates related commands and approaches, making workflows explicit and reducing navigation complexity.

### Key Improvements

- **Bootstrap consolidation:** 3 installation approaches (standard, custom route, nightly build) plus GitHub app creation unified under "Set Up Pipelines as Code for Git Repository" instead of scattered bootstrap options
- **Repository lifecycle clarity:** Create, list, and describe commands grouped as "Manage Pipelines as Code Repositories" showing complete repository management workflow
- **Local testing workflow:** Generate and resolve commands consolidated into "Test Pipeline Runs Locally" with parameter override as explicit capability (3 approaches instead of 2 disconnected commands)
- **CEL debugging workflow:** Interactive and noninteractive testing modes plus reference material unified under "Debug Event Filtering Logic" instead of subsections in a command reference
- **Logging configuration:** Default and custom logging approaches consolidated as "Control Log Verbosity for PAC Components" distinguishing operational needs
- **Troubleshooting integration:** Namespace log filtering integrated into troubleshooting workflow alongside CEL debugging (Jobs 4 and 6)
- **Workflow stage alignment:** Jobs organized by Get Started → Administer → Develop → Troubleshoot → Configure progression matching user journey
- **Reduced top-level navigation:** 3 feature-based sections reduced to 6 goal-based jobs with clearer semantic organization

---

## Current Structure (Feature-Based)

- **Pipelines as Code command reference** — Main assembly introducing tkn pac CLI capabilities
  - Basic syntax — Command format and usage examples
  - Global options — Help and global flags
  - **Utility commands** — Command categories grouped by function
    - bootstrap — Installation and configuration commands
      - `tkn pac bootstrap` — Standard installation for GitHub/GitHub Enterprise
      - `tkn pac bootstrap --nightly` — Nightly build installation
      - `tkn pac bootstrap --route-url` — Custom route URL override
      - `tkn pac bootstrap github-app` — GitHub application creation
    - repository — Repository management commands
      - `tkn pac create repository` — Create new PAC repository
      - `tkn pac list` — List all repositories
      - `tkn pac repo describe` — Describe repository and runs
    - generate — Pipeline run generation
      - `tkn pac generate` — Generate basic pipeline run
    - resolve — Pipeline run resolution
      - `tkn pac resolve` — Execute pipeline as if PAC owns it
      - Parameter override examples — Override Git parameters with -p flag
    - **Common Expression Language (CEL)** — CEL expression evaluation (Technology Preview)
      - Command syntax and options
      - Header formats (plain HTTP, JSON, gosmee scripts)
      - Interactive mode — REPL with persistent history
      - Noninteractive mode — stdin input for automation
      - Available variables — event, branch, URL, header, body variables
      - Example expressions — Event filtering, branch matching, header inspection
      - History storage — Persistent history location
- **Configuring Pipelines as Code logging** — Standalone procedure for logging configuration
  - Prerequisites — PAC installed, TektonConfig access
  - Procedure
    - Edit loglevel fields in TektonConfig CR
    - Optional: Create custom logging config map
- **Splitting Pipelines as Code logs by namespace** — Standalone reference for log filtering
  - oc logs command with grep filtering by namespace

**Total:** 3 chapters (command reference, logging config, log splitting), 10+ sections, organized by feature categories (bootstrap, repository, generate, resolve, CEL, logging).

---

## Proposed JTBD-Based Structure

### Quick Overview

- **Getting Started**
  - Job 1: Set Up Pipelines as Code for Git Repository
- **Administer Platform**
  - Job 2: Manage Pipelines as Code Repositories
- **Develop & Test**
  - Job 3: Test Pipeline Runs Locally
- **Troubleshoot Issues**
  - Job 4: Debug Event Filtering Logic
- **Configure Platform**
  - Job 5: Control Log Verbosity for PAC Components
- **Troubleshoot Issues**
  - Job 6: Isolate Logs for Specific Namespace

---

### Detailed Job Descriptions

#### Getting Started

**Job 1: Set Up Pipelines as Code for Git Repository**

*When I need to bootstrap Pipelines as Code installation and integrate with my Git provider, I want to install and configure PAC, so I can start using GitOps-based pipeline automation quickly.*

Prerequisites: Install OpenShift Pipelines, tkn CLI with pac plugin, cluster-admin access

- **1.1. Standard Bootstrap Installation** `[procedure]`
  - Lines 108-120 (modules/op-pipelines-as-code-command-reference.adoc): Bootstrap command with automatic route detection
  - Context: Use for standard OpenShift installations where automatic route detection is sufficient

- **1.2. Bootstrap with Custom Route** `[procedure]`
  - Lines 119-124 (modules/op-pipelines-as-code-command-reference.adoc): Override default route URL for custom ingress
  - Context: Use for non-OpenShift clusters or custom ingress requirements

- **1.3. Nightly Build Installation** `[procedure]`
  - Lines 117-118 (modules/op-pipelines-as-code-command-reference.adoc): Install latest nightly build
  - Context: Use for testing latest features before official release

- **1.4. GitHub Application Setup** `[procedure]`
  - Lines 125-127 (modules/op-pipelines-as-code-command-reference.adoc): Create GitHub OAuth application and secrets
  - Context: Required for GitHub integration after bootstrap

#### Administer Platform

**Job 2: Manage Pipelines as Code Repositories**

*When I need to onboard Git repositories and track their integration status, I want to create and view repository configurations, so I can ensure proper pipeline automation for my projects.*

Prerequisites: Bootstrap Pipelines as Code, access to target namespace, Git repository URL

- **2.1. Create New Repository** `[procedure]`
  - Lines 136-137 (modules/op-pipelines-as-code-command-reference.adoc): Create PAC repository and namespace
  - Context: Use when onboarding new Git repository to PAC

- **2.2. List All Repositories** `[procedure]`
  - Lines 138-139 (modules/op-pipelines-as-code-command-reference.adoc): Display all repositories with last run status
  - Context: Use for quick health check across all repositories

- **2.3. Describe Repository Details** `[procedure]`
  - Lines 140-142 (modules/op-pipelines-as-code-command-reference.adoc): Show detailed repository and run information
  - Context: Use for troubleshooting or reviewing run history

#### Develop & Test

**Job 3: Test Pipeline Runs Locally**

*When I need to validate pipeline logic before committing to Git, I want to generate and resolve pipeline definitions locally, so I can reduce commit noise and iterate faster on pipeline development.*

Prerequisites: Pipeline run templates in .tekton directory

- **3.1. Generate Basic Pipeline Run** `[procedure]`
  - Lines 144-159 (modules/op-pipelines-as-code-command-reference.adoc): Generate starter pipeline with language detection
  - Context: Use when creating initial pipeline run template

- **3.2. Resolve Pipeline Run Locally** `[procedure]`
  - Lines 161-175 (modules/op-pipelines-as-code-command-reference.adoc): Execute pipeline as if PAC owns it
  - Context: Use for testing pipeline without committing to Git

- **3.3. Override Git Parameters** `[procedure]`
  - Lines 176-182 (modules/op-pipelines-as-code-command-reference.adoc): Test with different branches or repository configurations
  - Context: Use when testing multi-repository pipelines or different parameter combinations

#### Troubleshoot Issues

**Job 4: Debug Event Filtering Logic**

*When I need to verify CEL expressions match expected webhook events, I want to evaluate expressions against webhook data, so I can ensure event filters work correctly before deploying.*

Prerequisites: Webhook payload and header data, CEL expression syntax knowledge

- **4.1. Test Expressions Interactively** `[procedure]`
  - Lines 264-266, 311-316 (modules/op-pipelines-as-code-command-reference.adoc): Interactive REPL with persistent history
  - Context: Use for rapid iteration on CEL expression logic

- **4.2. Automate Expression Validation** `[procedure]`
  - Lines 268-275 (modules/op-pipelines-as-code-command-reference.adoc): Noninteractive mode accepting expressions via stdin
  - Context: Use for CI/CD integration and automated testing

- **4.3. Understand CEL Variables** `[reference]`
  - Lines 277-291 (modules/op-pipelines-as-code-command-reference.adoc): Available variables for filtering events
  - Context: Reference when writing CEL expressions

- **4.4. Use Common Expression Patterns** `[reference]`
  - Lines 299-309 (modules/op-pipelines-as-code-command-reference.adoc): Example expressions for typical use cases
  - Context: Reference for common filtering scenarios

#### Configure Platform

**Job 5: Control Log Verbosity for PAC Components**

*When I need to adjust log detail based on operational requirements, I want to configure logging levels through TektonConfig, so I can minimize noise in production or increase detail for troubleshooting.*

Prerequisites: PAC installed, cluster-admin access to TektonConfig

- **5.1. Configure Default Log Levels** `[procedure]`
  - Lines 348-397 (modules/op-configuring-pipelines-as-code-logging.adoc): Edit loglevel fields for pac-watcher, webhook, and controller
  - Context: Use for standard logging configuration changes

- **5.2. Create Custom Logging Configuration** `[procedure]`
  - Lines 398-472 (modules/op-configuring-pipelines-as-code-logging.adoc): Create custom config map with specialized logging
  - Context: Use when advanced logging requirements need custom zap logger configuration

#### Troubleshoot Issues

**Job 6: Isolate Logs for Specific Namespace**

*When I need to troubleshoot issues for individual teams or projects, I want to filter PAC logs by namespace information, so I can efficiently isolate problems in multi-tenant environments.*

Prerequisites: PAC running, oc CLI installed, target namespace name

- **6.1. Filter Logs by Namespace** `[procedure]`
  - Lines 486-493 (modules/op-splitting-pipelines-as-code-logs-by-namespace.adoc): Use oc logs with grep to extract namespace-specific entries
  - Context: Use when troubleshooting specific namespace issues

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | Command categories (bootstrap, repository, generate, resolve, CEL) | User goals and lifecycle stages (Get Started, Develop, Troubleshoot, Configure, Administer) |
| **Top-level items** | 3 sections (command reference + 2 procedures) | 6 main jobs with nested approaches |
| **Bootstrap installation** | 4 bootstrap command variations listed sequentially | Job 1: 4 installation approaches organized by deployment scenario |
| **Repository management** | 3 commands under "repository" utility category | Job 2: Repository lifecycle workflow (create → list → describe) |
| **Local testing** | 2 separate utility categories (generate, resolve) | Job 3: Complete local testing workflow with 3 approaches |
| **CEL debugging** | 1 command section with 6 subsections | Job 4: Debugging workflow separating interactive/automated testing + reference |
| **Logging configuration** | Standalone procedure section | Job 5: Operational configuration with 2 approaches (default vs custom) |
| **Log filtering** | Standalone reference section | Job 6: Integrated into troubleshooting workflow |
| **Navigation model** | Browse by command name (tkn pac bootstrap, tkn pac generate) | Navigate by goal (Set Up, Test Locally, Debug Filters), then choose approach |
| **Workflow visibility** | Implicit (user must infer workflow from commands) | Explicit (jobs show when/why to use each command) |
| **Troubleshooting** | Scattered (CEL in command reference, logs in separate sections) | Unified (Jobs 4 and 6 in Troubleshoot stage) |

### Job List Adjustments from Suggested Input

The suggested 19 jobs were consolidated to **6 jobs** for the following reasons:

1. **Jobs 1, 2, and 3 (bootstrap approaches) merged into Job 1** → All three represent installation approaches for the same goal (bootstrap PAC for Git repository). Job 1 now includes standard bootstrap (Job 2), custom route bootstrap (merged from Job 1), and nightly build (merged from Job 1) as approaches, plus GitHub app creation (Job 3) as final setup step.

2. **Jobs 5, 6, and 7 (repository operations) merged into Job 2** → Create repository (Job 5), list repositories (Job 6), and describe repository (Job 7) are all repository management operations. Consolidated into single job showing repository lifecycle.

3. **Jobs 9, 10, and 11 (local testing) merged into Job 3** → Generate pipeline run (Job 9), resolve pipeline run (Job 10), and override parameters (Job 11) form a complete local testing workflow. Consolidated into single job with 3 approaches.

4. **Jobs 13 and 14 (CEL testing) merged into Job 4** → Interactive CEL testing (Job 13) and noninteractive CEL testing (Job 14) serve the same goal (debug event filtering). Consolidated with CEL variables and examples as reference material.

5. **Jobs 16 and 17 (logging configuration) merged into Job 5** → Configure default log levels (Job 16) and create custom logging config (Job 17) are two approaches to controlling log verbosity. Consolidated into single job.

6. **Job 19 absorbed into Job 6** → Namespace log filtering (Job 19) is the single approach for isolating namespace-specific logs in troubleshooting workflow.

7. **Jobs 4, 8, 12, 15, and 18 dissolved** → These were user stories or variations of the main jobs above, not distinct main jobs. Content absorbed into parent jobs as approaches or context.

---

## Consolidation Examples

### Example 1: Local Pipeline Testing (2 disconnected commands → 1 unified workflow)

**Current (Fragmented):**
- Section: generate (lines 144-159) — Generate basic pipeline run with language detection
- Section: resolve (lines 161-175) — Execute pipeline run as if PAC owns it
- Section: resolve (lines 176-182) — Parameter override buried in resolve examples

Users must connect that "generate" creates the template and "resolve" tests it, with parameter override as a hidden capability.

**Proposed (Consolidated):**
- **Job 3: Test Pipeline Runs Locally**
  - 3.1. Generate Basic Pipeline Run (lines 144-159)
  - 3.2. Resolve Pipeline Run Locally (lines 161-175)
  - 3.3. Override Git Parameters (lines 176-182)

**Benefit:** Complete local testing workflow in one place - generate template, test locally, override parameters for different scenarios. Reduces clicks from 2+ sections to 1 job with explicit workflow.

---

### Example 2: CEL Expression Debugging (Subsections scattered in command reference → 1 workflow job)

**Current (Fragmented):**
- Section: Common Expression Language (CEL) (lines 184-316)
  - Interactive mode (lines 264-266)
  - Noninteractive mode (lines 268-275)
  - Available variables (lines 277-291)
  - Example expressions (lines 299-309)
  - History storage (lines 310-316)

All CEL content is under one command section, but the workflow distinction between interactive iteration and automated testing is buried in subsections.

**Proposed (Consolidated):**
- **Job 4: Debug Event Filtering Logic**
  - 4.1. Test Expressions Interactively (lines 264-266, 311-316)
  - 4.2. Automate Expression Validation (lines 268-275)
  - 4.3. Understand CEL Variables (reference, lines 277-291)
  - 4.4. Use Common Expression Patterns (reference, lines 299-309)

**Benefit:** CEL debugging workflow is explicit - iterate interactively during development, automate validation in CI/CD, reference variables and patterns as needed. Workflow stages are clear instead of hidden in subsections.

---

### Example 3: Repository Lifecycle Management (3 commands listed sequentially → 1 management workflow)

**Current (Fragmented):**
- Section: repository (lines 129-142)
  - `tkn pac create repository` (lines 136-137)
  - `tkn pac list` (lines 138-139)
  - `tkn pac repo describe` (lines 140-142)

Commands are listed without workflow context. User must infer the lifecycle pattern.

**Proposed (Consolidated):**
- **Job 2: Manage Pipelines as Code Repositories**
  - 2.1. Create New Repository (lines 136-137)
  - 2.2. List All Repositories (lines 138-139)
  - 2.3. Describe Repository Details (lines 140-142)

**Benefit:** Repository management workflow is explicit - create repositories to onboard projects, list to monitor health, describe for detailed inspection. Natural progression from creation to ongoing management.

---

## Content Gaps Identified

| Gap | JTBD Reference | Current Coverage | Impact |
|-----|---------------|-----------------|--------|
| No observability or metrics monitoring guidance | Would fit in new "Monitor Pipeline Performance" job | Not mentioned | **High** — Users lack guidance on viewing pipeline run metrics, health checks, or performance monitoring beyond basic repository status |
| No PAC upgrade or migration procedures | Would fit in new "Upgrade PAC Installation" job | Not mentioned | **High** — Users upgrading PAC versions have no guidance on compatibility, migration steps, or version-specific changes |
| No authentication and authorization configuration | Would fit in existing Job 1 or new "Secure PAC" job | GitHub app creation only (lines 125-127) | **Medium** — Limited to GitHub OAuth app setup, no RBAC, secret management, or other Git provider auth |
| No webhook configuration guidance | Would fit in existing Job 1 or new setup job | Bootstrapping mentions webhooks (line 123) but no configuration details | **Medium** — Users must configure webhooks manually without step-by-step guidance |
| No backup and restore procedures | Would fit in new "Operate PAC" job | Not mentioned | **Medium** — Platform engineers lack operational guidance for disaster recovery |
| Limited error handling and failure troubleshooting | Would enhance Jobs 4 and 6 | CEL debugging exists, but no general troubleshooting workflow | **Medium** — Users have CEL debugging but lack guidance for common PAC failures, webhook issues, or pipeline run errors |
| No Git provider comparison or selection guidance | Would fit in existing Job 1 or new planning job | GitHub/GitHub Enterprise mentioned but no provider comparison | **Low** — Users evaluating PAC don't have guidance on Git provider trade-offs (GitHub vs GitLab vs Gitea, etc.) |
| No performance tuning or optimization | Would fit in new "Optimize PAC" job | Not mentioned | **Low** — Advanced users lack guidance on scaling PAC, optimizing webhook processing, or tuning for large deployments |

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 3 sections (command reference, 2 procedures) | 6 jobs | Semantic organization by user goal vs feature category |
| Sections to browse for "install PAC" | 1 section (Utility commands → bootstrap) | 1 job (Getting Started → Job 1) | Same clicks, clearer workflow context |
| Sections to browse for "test pipeline locally" | 2 sections (generate + resolve) | 1 job (Develop & Test → Job 3) | ~50% reduction in sections |
| Sections to browse for "CEL debugging" | 1 section with 6 subsections | 1 job (Troubleshoot → Job 4) | Same clicks, workflow clarity improved |
| Sections to browse for "repository management" | 1 section (repository commands) | 1 job (Administer → Job 2) | Same clicks, lifecycle clarity added |
| Sections to browse for "logging configuration" | 1 separate procedure section | 1 job (Configure → Job 5) | Integrated into workflow stages |
| Clicks to find "namespace log filtering" | 1 separate reference section | 1 job (Troubleshoot → Job 6) | Troubleshooting context now explicit |
| Workflow stage visibility | Implicit (inferred from command sequence) | Explicit (Get Started → Administer → Develop → Troubleshoot → Configure) | User journey now visible |

**Final job count: 6** (reduced from suggested 19). Consolidation rationale: Related commands and approaches unified under stable user goals. Bootstrap installation variations (4 approaches) consolidated into Job 1. Repository operations (3 commands) consolidated into Job 2. Local testing workflow (generate + resolve + parameter override) consolidated into Job 3. CEL debugging modes (interactive + noninteractive + reference) consolidated into Job 4. Logging configuration (default + custom) consolidated into Job 5. Namespace filtering stands alone as Job 6. Result: clearer workflows, reduced navigation complexity, explicit lifecycle stages.

---

## UX Research Alignment

*Note: This section is not applicable as the JTBD records do not contain research extension fields (pain_points, strategic_priority, teams_involved, loop). The consolidation is based on structural analysis and workflow optimization.*

---

## Document Statistics

### Workflow Coverage

| Stage | Jobs | Coverage Status |
|-------|------|-----------------|
| Get Started | Job 1 | ✅ Bootstrap installation and configuration |
| Configure | Job 5 | ✅ Logging configuration |
| Develop | Job 3 | ✅ Local testing workflow |
| Administer | Job 2 | ✅ Repository lifecycle management |
| Troubleshoot | Jobs 4, 6 | ✅ CEL debugging and log filtering |
| Monitor | - | ❌ Gap identified |
| Upgrade | - | ❌ Gap identified |
| Secure | - | ⚠️ Limited (GitHub app only) |
| Operate | - | ❌ Gap identified |
| Reference | All jobs | ✅ CLI command reference embedded throughout |

### Summary Statistics

- **Main Jobs:** 6 (consolidated from 19 pre-analysis records)
- **Approaches/Tasks:** 15 total across all jobs
- **Source Modules:** 3 AsciiDoc modules
  - modules/op-pipelines-as-code-command-reference.adoc (lines 72-316)
  - modules/op-configuring-pipelines-as-code-logging.adoc (lines 326-472)
  - modules/op-splitting-pipelines-as-code-logs-by-namespace.adoc (lines 482-493)
- **Command Variations:** 8 primary commands (bootstrap, create repository, list, describe, generate, resolve, cel, oc logs)
- **Content Type Distribution:**
  - Procedures: 11 approaches
  - Reference: 4 approaches (CEL variables, expression patterns)
  - Concepts: 0 (command reference guide)

### Consolidation Impact

- **Pre-consolidation:** 19 JTBD records from analysis
- **Post-consolidation:** 6 main jobs
- **Reduction:** 68% fewer top-level items
- **Rationale:** Bootstrap approaches merged (4 → 1 job), repository operations merged (3 → 1 job), local testing workflow merged (3 → 1 job), CEL debugging modes merged (2 → 1 job), logging config merged (2 → 1 job), namespace filtering standalone (1 → 1 job)

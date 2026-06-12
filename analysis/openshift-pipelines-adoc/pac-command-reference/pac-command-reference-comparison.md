# Pipelines as Code Command Reference - TOC Comparison

**Current Feature-Based vs. Proposed JTBD-Based Structure**

**Analysis Date:** 2026-06-11
**JTBD Records:** 19
**Main Jobs:** 6 (rolled up from records)
**Coverage:** 100% enhanced schema

---

## Current Structure (Feature-Based)

**Pipelines as Code command reference**
- **Pipelines as Code command reference**
  - Basic syntax (lines 90-96)
  - Global options (lines 98-104)
  - Utility commands (lines 106-316)
    - bootstrap (lines 108-127)
    - repository (lines 129-142)
    - generate (lines 144-159)
    - resolve (lines 161-182)
    - Common Expression Language (CEL) (lines 184-316)
      - Header formats (lines 226-262)
      - Interactive mode (lines 264-266)
      - Noninteractive mode (lines 268-275)
      - Available variables (lines 277-291)
      - Example expressions (lines 299-309)
      - History storage (lines 310-316)
- **Configuring Pipelines as Code logging** (lines 326-472)
  - Prerequisites (lines 332-334)
  - Procedure (lines 336-472)
- **Splitting Pipelines as Code logs by namespace** (lines 482-493)

**Total:** 3 main sections organized by command/feature categories, with nested subsections for command options and configuration procedures.

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
  - Lines 108-120 (modules/op-pipelines-as-code-command-reference.adoc): Bootstrap command with automatic route detection for GitHub/GitHub Enterprise
  - Context: Use for standard OpenShift installations where automatic route detection is sufficient

- **1.2. Bootstrap with Custom Route** `[procedure]`
  - Lines 119-124 (modules/op-pipelines-as-code-command-reference.adoc): Override default route URL for custom ingress configurations
  - Context: Use for non-OpenShift clusters or custom ingress requirements

- **1.3. Nightly Build Installation** `[procedure]`
  - Lines 117-118 (modules/op-pipelines-as-code-command-reference.adoc): Install latest nightly build of PAC
  - Context: Use for testing latest features before official release

- **1.4. GitHub Application Setup** `[procedure]`
  - Lines 125-127 (modules/op-pipelines-as-code-command-reference.adoc): Create GitHub OAuth application and secrets
  - Context: Required for GitHub integration after bootstrap

#### Administer Platform

**Job 2: Manage Pipelines as Code Repositories**

*When I need to onboard Git repositories and track their integration status, I want to create and view repository configurations, so I can ensure proper pipeline automation for my projects.*

Prerequisites: Bootstrap Pipelines as Code, access to target namespace, Git repository URL

- **2.1. Create New Repository** `[procedure]`
  - Lines 136-137 (modules/op-pipelines-as-code-command-reference.adoc): Create PAC repository and namespace based on pipeline run template
  - Context: Use when onboarding new Git repository to PAC

- **2.2. List All Repositories** `[procedure]`
  - Lines 138-139 (modules/op-pipelines-as-code-command-reference.adoc): Display all repositories with last run status
  - Context: Use for quick health check across all repositories

- **2.3. Describe Repository Details** `[procedure]`
  - Lines 140-142 (modules/op-pipelines-as-code-command-reference.adoc): Show detailed information about specific repository and associated runs
  - Context: Use for troubleshooting or reviewing run history

#### Develop & Test

**Job 3: Test Pipeline Runs Locally**

*When I need to validate pipeline logic before committing to Git, I want to generate and resolve pipeline definitions locally, so I can reduce commit noise and iterate faster on pipeline development.*

Prerequisites: Pipeline run templates in .tekton directory

- **3.1. Generate Basic Pipeline Run** `[procedure]`
  - Lines 144-159 (modules/op-pipelines-as-code-command-reference.adoc): Generate starter pipeline with language detection and automatic Git info
  - Context: Use when creating initial pipeline run template for repository

- **3.2. Resolve Pipeline Run Locally** `[procedure]`
  - Lines 161-175 (modules/op-pipelines-as-code-command-reference.adoc): Execute pipeline as if PAC owns it, with auto-detected Git context
  - Context: Use for testing pipeline without committing to Git

- **3.3. Override Git Parameters** `[procedure]`
  - Lines 176-182 (modules/op-pipelines-as-code-command-reference.adoc): Test with different branches or repository configurations using -p flags
  - Context: Use when testing multi-repository pipelines or different parameter combinations

#### Troubleshoot Issues

**Job 4: Debug Event Filtering Logic**

*When I need to verify CEL expressions match expected webhook events, I want to evaluate expressions against webhook data, so I can ensure event filters work correctly before deploying.*

Prerequisites: Webhook payload and header data, CEL expression syntax knowledge

- **4.1. Test Expressions Interactively** `[procedure]`
  - Lines 264-266, 311-316 (modules/op-pipelines-as-code-command-reference.adoc): Interactive REPL with persistent history for iterative expression development
  - Context: Use for rapid iteration on CEL expression logic

- **4.2. Automate Expression Validation** `[procedure]`
  - Lines 268-275 (modules/op-pipelines-as-code-command-reference.adoc): Noninteractive mode accepting CEL expressions via stdin
  - Context: Use for CI/CD integration and automated testing

- **4.3. Understand CEL Variables** `[reference]`
  - Lines 277-291 (modules/op-pipelines-as-code-command-reference.adoc): Available variables for filtering and inspecting events
  - Context: Reference when writing CEL expressions

- **4.4. Use Common Expression Patterns** `[reference]`
  - Lines 299-309 (modules/op-pipelines-as-code-command-reference.adoc): Example expressions for typical use cases
  - Context: Reference for common filtering scenarios

#### Configure Platform

**Job 5: Control Log Verbosity for PAC Components**

*When I need to adjust log detail based on operational requirements, I want to configure logging levels through TektonConfig, so I can minimize noise in production or increase detail for troubleshooting.*

Prerequisites: PAC installed, cluster-admin access to TektonConfig

- **5.1. Configure Default Log Levels** `[procedure]`
  - Lines 348-397 (modules/op-configuring-pipelines-as-code-logging.adoc): Edit loglevel fields for pac-watcher, webhook, and controller components
  - Context: Use for standard logging configuration changes

- **5.2. Create Custom Logging Configuration** `[procedure]`
  - Lines 398-472 (modules/op-configuring-pipelines-as-code-logging.adoc): Create custom config map with specialized logging formats or handlers
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
| **Organizing principle** | Commands and features (bootstrap, repository, generate, etc.) | User goals and workflow stages (Get Started, Develop, Troubleshoot) |
| **Top-level items** | 3 sections (command reference, logging config, log splitting) | 6 main jobs with nested approaches |
| **Bootstrap installation** | Single section with all options mixed | Job 1 with 4 distinct approaches based on deployment scenario |
| **Repository management** | Three commands listed sequentially | Job 2 with operations organized by management workflow (create, list, describe) |
| **Local testing** | Two separate commands (generate, resolve) | Job 3 consolidating full local testing workflow with parameter override capability |
| **CEL debugging** | One command section with subsections for modes | Job 4 separating interactive vs automated testing with reference material |
| **Logging configuration** | Separate procedure section | Job 5 distinguishing default vs custom configuration approaches |
| **Log filtering** | Standalone reference section | Job 6 integrated into troubleshooting workflow |
| **Navigation model** | Browse by command name | Navigate by goal, then choose approach based on context |

### Job List Adjustments from Suggested Input

The suggested 19 JTBD records were consolidated to **6 main jobs** for the following reasons:

1. **Jobs 2 and 3 (bootstrap approaches) merged into Job 1** → Both are installation approaches for the same goal (bootstrap PAC). Job 1 now includes standard bootstrap, custom route, nightly build, and GitHub app creation as different approaches.

2. **Jobs 5, 6, and 7 (repository operations) merged into Job 2** → All three are repository management operations (create, list, describe). Consolidated into single repository management job with three operational approaches.

3. **Jobs 9, 10, and 11 (local testing) merged into Job 3** → Generate, resolve, and parameter override are all part of the local testing workflow. Consolidated into single testing job with three approaches.

4. **Jobs 13 and 14 (CEL testing modes) merged into Job 4** → Interactive and noninteractive CEL testing serve the same goal (debug event filtering). Consolidated with reference material as supporting content.

5. **Jobs 16 and 17 (logging configuration) merged into Job 5** → Default and custom logging configuration are two approaches to the same goal (control log verbosity). Consolidated into single logging job.

6. **Job 19 absorbed into Job 6** → Log filtering by namespace is the single approach for isolating namespace-specific logs.

---

## Example Consolidation

### Example 1: CEL Expression Testing (Multiple testing modes → 1 unified job)

**Current (Fragmented):**
- Section: Common Expression Language (CEL) (lines 184-316)
  - Interactive mode (lines 264-266)
  - Noninteractive mode (lines 268-275)
  - Available variables (lines 277-291)
  - Example expressions (lines 299-309)

Users must understand this is a single debugging workflow with different execution modes, but the structure presents it as separate features.

**Proposed (Consolidated):**
- **Job 4: Debug Event Filtering Logic**
  - 4.1. Test Expressions Interactively (lines 264-266, 311-316)
  - 4.2. Automate Expression Validation (lines 268-275)
  - 4.3. Understand CEL Variables (lines 277-291)
  - 4.4. Use Common Expression Patterns (lines 299-309)

**Benefit:** One place to learn CEL debugging with clear separation of interactive vs automated testing and supporting reference material.

---

### Example 2: Repository Management (3 scattered commands → 1 workflow job)

**Current (Fragmented):**
- Section: repository (lines 129-142)
  - `tkn pac create repository` (line 136)
  - `tkn pac list` (line 138)
  - `tkn pac repo describe` (line 140)

Commands are listed sequentially without workflow context.

**Proposed (Consolidated):**
- **Job 2: Manage Pipelines as Code Repositories**
  - 2.1. Create New Repository (lines 136-137)
  - 2.2. List All Repositories (lines 138-139)
  - 2.3. Describe Repository Details (lines 140-142)

**Benefit:** Repository lifecycle management workflow is clear - create, monitor, inspect.

---

### Example 3: Local Testing Workflow (2 commands + parameter override → 1 development job)

**Current (Fragmented):**
- Section: generate (lines 144-159)
- Section: resolve (lines 161-182)
  - Parameter override example buried in resolve section (lines 176-182)

Users must piece together that generate and resolve form a development workflow.

**Proposed (Consolidated):**
- **Job 3: Test Pipeline Runs Locally**
  - 3.1. Generate Basic Pipeline Run (lines 144-159)
  - 3.2. Resolve Pipeline Run Locally (lines 161-175)
  - 3.3. Override Git Parameters (lines 176-182)

**Benefit:** Complete local testing workflow in one place with parameter override as explicit capability.

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 3 sections | 6 jobs | Semantic organization by goal |
| Clicks to find "bootstrap installation" | Browse "Utility commands" → "bootstrap" | Navigate "Getting Started" → Job 1 | ~33% more intuitive |
| Clicks to find "local testing workflow" | Browse "Utility commands" → "generate" AND "resolve" | Navigate "Develop & Test" → Job 3 | 2 sections → 1 job |
| Clicks to find "CEL debugging" | Browse "Utility commands" → "CEL" subsections | Navigate "Troubleshoot" → Job 4 | Workflow-aligned |
| Clicks to find "repository management" | Browse "Utility commands" → "repository" | Navigate "Administer" → Job 2 | Lifecycle clarity |
| Sections to browse for "logging configuration" | 1 dedicated procedure section (no workflow context) | Navigate "Configure" → Job 5 (with troubleshooting Job 6 nearby) | Operational context |

**Final job count: 6** (reduced from suggested 19). Consolidation groups related commands and approaches under stable user goals, making the reference more navigable and reducing cognitive load for users learning the CLI tool.

---

## Workflow Coverage Comparison

| Stage | Current | Proposed | Gap Status |
|-------|---------|----------|------------|
| Get Started | ✅ Bootstrap section | ✅ Job 1 | Improved organization |
| Configure | ✅ Logging config | ✅ Job 5 | Elevated to workflow stage |
| Develop | ⚠️ Generate/resolve scattered | ✅ Job 3 | Consolidated workflow |
| Administer | ✅ Repository commands | ✅ Job 2 | Lifecycle clarity |
| Troubleshoot | ⚠️ CEL debugging, log filtering separate | ✅ Jobs 4, 6 | Integrated troubleshooting |
| Monitor | ❌ Missing | ❌ Missing | Gap remains |
| Upgrade | ❌ Missing | ❌ Missing | Gap remains |
| Reference | ✅ Command syntax throughout | ✅ Embedded in all jobs | Maintained |

### Coverage Summary

**Current structure gaps:** Monitor, Upgrade, scattered local testing workflow
**Proposed structure gaps:** Monitor, Upgrade (same gaps)
**Gaps addressed by restructure:** Local testing workflow consolidated, troubleshooting integrated

### Recommendations for Gap Closure

| Gap | Recommendation | Priority |
|-----|----------------|----------|
| Monitor | Add section on viewing pipeline run metrics and health checks | High |
| Upgrade | Add PAC upgrade procedures and version migration guidance | Medium |
| Secure | Add authentication and authorization configuration | Medium |
| Operate | Add backup/restore and high availability content | Low |

---

## UI and CLI Path Documentation

**Note:** This is a CLI-focused reference guide. All procedures are command-line based. The OpenShift web console is used only for TektonConfig editing (Job 5), where both UI and CLI paths exist:

**Configure Default Log Levels (Job 5.1)**
- **UI Path:** Administration → CustomResourceDefinitions → Search "tektonconfigs.operator.tekton.dev" → TektonConfig → config instance → YAML tab → Edit loglevel fields
  - Context: Easier for administrators without oc CLI access
- **CLI Path:** `oc edit tektonconfig config` → Edit `.options.configMaps.pac-config-logging.data.loglevel.*` fields
  - Context: Faster for automation and scripting

All other jobs are CLI-only by nature (tkn pac commands, oc logs with grep).

---

## Success Criteria

**A good command reference structure:**

- User can find commands by what they need to accomplish (bootstrap, test locally, debug filters)
- User can see the workflow context for each command (when to use, prerequisites)
- Commands are grouped by lifecycle stage, not alphabetically
- Related commands are consolidated under common goals
- Both interactive and automated usage patterns are documented
- Reference material (variables, examples) is embedded with relevant jobs
- No procedural steps are gated by persona - anyone with required permissions can execute

This restructure achieves all criteria by organizing around 6 stable user goals with clear workflow progression.

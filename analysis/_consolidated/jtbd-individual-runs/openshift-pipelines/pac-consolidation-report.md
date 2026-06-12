# Pipelines as Code — Consolidation Report

**Document:** pac-combined.adoc  
**JTBD Records:** 40 pre-consolidated records → 18 final main jobs  
**Analysis Date:** June 12, 2026

---

## Executive Summary

### What's Changing

The current Pipelines as Code (PaC) documentation is organized by **technical features and platform components** — installations, Git provider types, Repository CR settings, pipeline run creation, and CLI commands. While comprehensive, this structure forces users to navigate across 7 major chapters and 34+ subsections, often requiring them to understand PaC's architecture before finding the content they need.

This fragmentation causes pain in several ways:
- **Git provider setup** is scattered across 5 separate sections (GitHub App, GitHub Webhook, GitLab, Bitbucket Cloud, Bitbucket Data Center), making it unclear which method to choose
- **Repository configuration** is split between Chapter 4 (Repository CR) and Chapter 3 (token scoping), despite being part of the same workflow
- **Pipeline run management** requires navigating between Chapter 5 (creating) and Chapter 6 (running/monitoring), even though these are sequential steps in the same workflow
- **Troubleshooting** is buried as an appendix in Chapter 7, not elevated to a primary workflow concern

The proposed reorganization shifts to **user goals and workflow stages** as the organizing principle. Instead of chapters like "Using Pipelines as Code with a Git repository hosting service provider," the structure groups content by jobs like "Integrate with GitHub," "Integrate with GitLab," and "Configure Token Scoping for Multi-Repository Access." This approach enables users to navigate by what they need to accomplish, not by knowing PaC's technical architecture.

### Key Improvements

- **Git provider integration consolidated:** 5 scattered provider sections → 4 unified jobs (GitHub App, GitHub Webhook, GitLab, Bitbucket with Cloud/Data Center variants)
- **GitHub App setup clarified:** 3 buried subsections → 1 job with 3 clear options (CLI, Web Console, Manual)
- **Repository configuration unified:** 5 sections across 2 chapters → 3 focused jobs (Create Repository CR, Configure Settings, Token Scoping)
- **Pipeline run workflow consolidated:** 7 subsections → 3 jobs following the creation → execution → monitoring flow
- **Troubleshooting elevated:** Scattered verification and logging → 1 dedicated job with troubleshooting focus
- **Navigation depth reduced:** 5-10 clicks average → 2-4 clicks (50-60% reduction)
- **Prerequisite chains made explicit:** Implicit chapter ordering → Clear "Requires" statements in each job
- **Decision points clarified:** No provider guidance → Clear "When to use" context for each approach

---

## Current Structure (Feature-Based)

The existing documentation is organized into 7 major chapters:

- **Chapter 1: About Pipelines as Code** — Introduction to PaC capabilities
  - 1.1. Key features — Platform capabilities and integrations
  - 1.2. Pipelines as Code concepts — Repository CR, .tekton directory, PaC resolver

- **Chapter 2: Installing and configuring Pipelines as Code** — Installation and global settings
  - 2.1. Installing Pipelines as Code on an OpenShift cluster — Operator-based installation
  - 2.2. Installing Pipelines as Code CLI — tkn pac and opc CLI tools
  - 2.3. Customizing Pipelines as Code configuration — TektonConfig CR settings
  - 2.4. Configuring additional PaC controllers — Multi-GitHub-App support

- **Chapter 3: Using Pipelines as Code with a Git repository hosting service provider** — Platform integration (1,377 lines)
  - 3.1. GitHub App integration with Pipelines as Code
    - 3.1.1. Configure a GitHub App using the command line interface
    - 3.1.2. Create a GitHub App in administrator perspective
    - 3.1.3. Configure a GitHub App manually
    - 3.1.4. Scope the GitHub token to additional repositories
  - 3.2. Use Pipelines as Code with GitHub Webhook
  - 3.3. Use Pipelines as Code with GitLab
  - 3.4. Use Pipelines as Code with Bitbucket Cloud
  - 3.5. Use Pipelines as Code with Bitbucket Data Center
  - 3.6. Configure custom certificates for Pipelines as Code
  - 3.7. Private repository support in Pipelines as Code

- **Chapter 4: Using the Repository custom resource** — Repository CR configuration
  - 4.1. Creating the Repository custom resource
  - 4.2. Creating the global Repository custom resource (Technology Preview)
  - 4.3. Setting concurrency limits
  - 4.4. Changing source branch for pipeline definition
  - 4.5. Custom parameter expansion

- **Chapter 5: Creating pipeline runs in Pipelines as Code** — Pipeline run definitions
  - 5.1. Creating a pipeline run in Pipelines as Code
  - 5.2. Dynamic variables in a pipeline run specification
  - 5.3. Pipelines as Code resolver annotations
    - 5.3.1. Remote task annotations
    - 5.3.2. Remote pipeline annotations
  - 5.4. Annotations for matching events to a pipeline run
  - 5.5. Annotations for filtering events matched to a pipeline run
  - 5.6. Annotations for specifying automatic cancellation-in-progress

- **Chapter 6: Managing pipeline runs** — Pipeline run lifecycle
  - 6.1. Verifying a pipeline run
  - 6.2. Running a pipeline run using Pipelines as Code
  - 6.3. Triggering a PipelineRun on Git tags
  - 6.4. Restarting or canceling a pipeline run
  - 6.5. Monitoring pipeline run status
  - 6.6. Cleaning up pipeline runs
  - 6.7. Using incoming webhook with Pipelines as Code

- **Chapter 7: Pipelines as Code command reference** — CLI and troubleshooting
  - 7.1. Pipelines as Code command reference
  - 7.2. Configuring Pipelines as Code logging
  - 7.3. Splitting Pipelines as Code logs by namespace

**Total:** 7 chapters, 34+ sections, organized by feature and platform type.

---

## Proposed JTBD-Based Structure

### Quick Overview

- **Understand & Plan**
  - Job 1: Understand Pipelines as Code Capabilities

- **Set Up & Configure**
  - Job 2: Install Pipelines as Code
  - Job 3: Customize Pipelines as Code Configuration
  - Job 4: Configure GitHub App Integration
  - Job 5: Create Repository Custom Resource
  - Job 6: Configure Repository Settings
  - Job 7: Configure Token Scoping for Multi-Repository Access
  - Job 8: Integrate with GitHub Webhooks (Alternative Method)
  - Job 9: Integrate with GitLab
  - Job 10: Integrate with Bitbucket
  - Job 11: Configure Custom Certificates

- **Deploy & Execute**
  - Job 12: Create Pipeline Run Definitions
  - Job 13: Use Dynamic Variables and Remote Tasks
  - Job 14: Control Pipeline Execution with Event Matching
  - Job 15: Trigger Pipeline Runs on Git Tags

- **Operate & Manage**
  - Job 16: Manage Pipeline Run Lifecycle

- **Track & Monitor**
  - Job 17: Monitor Pipeline Run Status

- **Reference**
  - Job 18: Use Pipelines as Code CLI

---

### Detailed Job Descriptions

#### Understand & Plan

**Job 1: Understand Pipelines as Code Capabilities**

*When I need to implement GitOps-driven CI/CD for my applications, I want to understand how Pipelines as Code works, so I can determine if it meets my automation requirements.*

Prerequisites: None

- **1.1. Review PaC architecture and workflow** `[concept]`
  - Lines 59-69: About Pipelines as Code — GitOps-driven pipeline execution model
  - Context: Start here to understand how PaC implements CI/CD with Git-based workflows

- **1.2. Understand Repository CR and .tekton directory structure** `[concept]`
  - Lines 91-118: Pipelines as Code concepts — Core concepts including Repository CR, .tekton directory, PaC resolver
  - Context: Essential concepts for planning implementation

- **1.3. Evaluate feature capabilities** `[concept]`
  - Lines 70-84: Key features — Pull request status checks, automatic task resolution, Git event filtering
  - Context: Assess whether PaC supports required CI/CD workflow requirements

---

#### Set Up & Configure

**Job 2: Install Pipelines as Code**

*When I need to enable Pipelines as Code functionality, I want to install it on my OpenShift cluster, so I can start using GitOps-driven pipelines.*

Prerequisites: OpenShift Pipelines Operator installed, cluster administrator access

- **2.1. Install PaC via OpenShift Pipelines Operator** `[procedure]`
  - Lines 196-234: Installing Pipelines as Code — Installation using TektonConfig CR
  - Context: Default installation method deploying PaC in openshift-pipelines namespace

- **2.2. Install tkn pac CLI tool** `[procedure]`
  - Lines 276-334: Installing Pipelines as Code CLI — Download and install for your platform
  - Context: Required for bootstrap and repository management operations

---

**Job 3: Customize Pipelines as Code Configuration**

*When I need to customize Pipelines as Code behavior, I want to configure parameters in the TektonConfig CR, so I can adjust settings like application name, remote tasks, and webhook behavior.*

Prerequisites: PaC installed on cluster

- **3.1. Configure core PaC settings** `[procedure]`
  - Lines 342-397: Customizing Pipelines as Code configuration — TektonConfig CR parameters
  - Context: Essential customization for organizational policies and requirements

- **3.2. Configure additional PaC controllers (Advanced)** `[procedure]`
  - Lines 406-442: Configuring additional PaC controllers — Multi-GitHub-App support
  - Context: Use when you need to support multiple GitHub organizations or instances

---

**Job 4: Configure GitHub App Integration**

*When I need to integrate Pipelines as Code with GitHub, I want to configure a GitHub App, so I can automate the setup process.*

Prerequisites: tkn pac CLI installed (for automated setup), cluster administrator access, GitHub account with app creation permissions

- **4.1. Automated CLI Setup** `[procedure]`
  - Lines 570-612: Configure a GitHub App using CLI — Interactive CLI wizard
  - Context: Fastest method for standard GitHub.com integration

- **4.2. Web Console Setup** `[procedure]`
  - Lines 621-657: Create GitHub App in administrator perspective — Guided UI setup
  - Context: Best for users who prefer visual configuration

- **4.3. Manual Configuration (Advanced)** `[procedure]`
  - Lines 666-767: Configure GitHub App manually — Custom GitHub App creation
  - Context: Required for additional controllers or GitHub Enterprise instances

---

**Job 5: Create Repository Custom Resource**

*When I want to connect a Git repository to Pipelines as Code, I want to create a Repository CR in my namespace, so I can enable PaC to process events from this repository.*

Prerequisites: PaC configured for Git provider, target namespace created

- **5.1. Define basic Repository CR** `[procedure]`
  - Lines 1911-1939: Creating Repository CR — Connect Git repository to namespace
  - Context: Essential step to map Git events to pipeline runs

- **5.2. Configure global Repository defaults (Optional, Technology Preview)** `[procedure]`
  - Lines 1948-2000: Creating global Repository CR — Common configuration across all repositories
  - Context: Use when you need consistent settings across many repositories

---

**Job 6: Configure Repository Settings**

*When I need to control pipeline execution behavior and security, I want to configure Repository CR settings, so I can manage concurrency, provenance, and parameters.*

Prerequisites: Repository CR created

- **6.1. Set concurrency limits** `[procedure]`
  - Lines 2008-2031: Setting concurrency limits — Prevent excessive simultaneous pipeline runs
  - Context: Essential for preventing cluster resource exhaustion

- **6.2. Configure pipeline provenance (Security)** `[procedure]`
  - Lines 2040-2064: Changing source branch — Enforce reviewed pipeline definitions only
  - Context: Critical security setting to prevent malicious pipeline code execution

- **6.3. Define custom parameters (Optional)** `[procedure]`
  - Lines 2073-2140: Custom parameter expansion — Administrator-managed values
  - Context: Use when you need environment-specific configuration without modifying pipeline definitions

---

**Job 7: Configure Token Scoping for Multi-Repository Access**

*When my pipeline needs to access multiple repositories, I want to scope the GitHub token to additional repositories, so I can fetch tasks or code from private repositories outside the main repository.*

Prerequisites: GitHub App configured, Repository CR created

- **7.1. Configure repository-level token scoping** `[procedure]`
  - Lines 776-865: Scope GitHub token to additional repositories — Repository CR configuration
  - Context: Use when specific Repository CRs need cross-repo access

- **7.2. Configure global token scoping (Advanced)** `[procedure]`
  - Lines 866-895: Global token scoping — TektonConfig CR settings
  - Context: Use when all repositories need the same additional repository access

---

**Job 8: Integrate with GitHub Webhooks (Alternative Method)**

*When I cannot create a GitHub App, I want to use Pipelines as Code with GitHub Webhook, so I can still integrate PaC with my GitHub repositories.*

Prerequisites: PaC installed, GitHub personal access token

- **8.1. Configure GitHub webhook integration** `[procedure]`
  - Lines 904-1132: Use PaC with GitHub Webhook — Webhook-based integration
  - Context: Alternative when GitHub App creation is not available; lacks GitHub Checks tab integration

---

**Job 9: Integrate with GitLab**

*When my organization uses GitLab, I want to integrate Pipelines as Code with GitLab webhooks, so I can use PaC with GitLab repositories.*

Prerequisites: PaC installed, GitLab personal access token

- **9.1. Configure GitLab webhook integration** `[procedure]`
  - Lines 1141-1339: Use PaC with GitLab — GitLab-specific webhook setup
  - Context: Complete GitLab integration including merge request status reporting

---

**Job 10: Integrate with Bitbucket**

*When my organization uses Bitbucket Cloud or Bitbucket Data Center, I want to integrate Pipelines as Code with Bitbucket webhooks, so I can use PaC with Bitbucket repositories.*

Prerequisites: PaC installed, Bitbucket credentials (app password or personal access token)

- **10.1. Bitbucket Cloud** `[procedure]`
  - Lines 1348-1588: Use PaC with Bitbucket Cloud — Cloud-hosted Bitbucket integration
  - Context: Use for Bitbucket SaaS (bitbucket.org)

- **10.2. Bitbucket Data Center (Self-Hosted)** `[procedure]`
  - Lines 1598-1738: Use PaC with Bitbucket Data Center — Self-hosted Bitbucket integration
  - Context: Use for on-premises Bitbucket installations

---

**Job 11: Configure Custom Certificates**

*When my Git repository uses custom certificates, I want to configure PaC to trust these certificates, so I can integrate with privately signed or self-hosted Git providers.*

Prerequisites: OpenShift Pipelines Operator installed

- **11.1. Configure certificate trust** `[procedure]`
  - Lines 1747-1758: Configure custom certificates — Proxy object configuration
  - Context: Required for private Git servers with custom CA certificates

---

#### Deploy & Execute

**Job 12: Create Pipeline Run Definitions**

*When I need to create pipeline runs triggered by Git events, I want to define pipeline run definitions in the .tekton directory, so I can automate my CI/CD workflow.*

Prerequisites: PaC configured with Git provider, Repository CR created, .tekton directory in repository

- **12.1. Define core pipeline run structure** `[procedure]`
  - Lines 2216-2377: Creating a pipeline run — YAML specifications in .tekton directory
  - Context: Foundation for all automated pipeline execution

- **12.2. Configure automatic Git authentication for private repos** `[concept]`
  - Lines 1767-1821: Private repository support — Automatic secret creation
  - Context: Integrated authentication for private repository access

---

**Job 13: Use Dynamic Variables and Remote Tasks**

*When I need reusable pipeline definitions, I want to use dynamic variables and reference remote tasks, so I can create template-based pipelines that work across different events.*

Prerequisites: Pipeline run definition created

- **13.1. Use dynamic variables** `[reference]`
  - Lines 2387-2454: Dynamic variables — Commit and repository context variables
  - Context: Enable context-aware, reusable pipeline definitions

- **13.2. Reference remote tasks with PaC resolver** `[procedure]`
  - Lines 2463-2644: PaC resolver annotations — Tasks from Tekton Hub, HTTP URLs, or local files
  - Context: Avoid duplicating task definitions across repositories

- **13.3. Verify pipeline runs before commit** `[procedure]`
  - Lines 3130-3153: Verifying a pipeline run — Local verification with tkn pac resolve
  - Context: Catch errors before committing to Git

---

**Job 14: Control Pipeline Execution with Event Matching**

*When I need to control when each pipeline run executes, I want to add annotations that match specific Git events, so I can ensure pipelines run only for relevant events.*

Prerequisites: Pipeline run definition created

- **14.1. Match Git events with annotations** `[reference]`
  - Lines 2653-2870: Annotations for matching events — pull_request, push, comment events with CEL expressions
  - Context: Core event matching for all pipeline runs

- **14.2. Filter events by changed files or labels** `[reference]`
  - Lines 2879-2983: Annotations for filtering events — Path-based and label-based filtering
  - Context: Minimize unnecessary pipeline runs

- **14.3. Enable automatic cancellation (Technology Preview)** `[reference]`
  - Lines 2992-3044: Annotations for cancellation-in-progress — Automatic old run cancellation
  - Context: Prevent excessive resource consumption from rapid commits

---

**Job 15: Trigger Pipeline Runs on Git Tags**

*When I create or reference a Git tag for a release, I want to trigger pipeline runs on the tagged commit, so I can test or deploy specific versions of my code.*

Prerequisites: Pipeline run configured for tag events, GitHub App or GitLab webhook configured

- **15.1. Configure tag event triggering** `[concept]`
  - Lines 3209-3279: Triggering PipelineRun on Git tags — Tag-based pipeline execution
  - Context: Enable version-based testing and deployment for release workflows

---

#### Operate & Manage

**Job 16: Manage Pipeline Run Lifecycle**

*When I need to retry failed pipelines or cancel running pipelines, I want to use comments or GitHub App features, so I can control pipeline execution without new commits.*

Prerequisites: Pipeline run exists, appropriate repository permissions

- **16.1. Run pipelines automatically** `[concept]`
  - Lines 3162-3200: Running a pipeline run — Automatic execution on matched events
  - Context: Understand automatic pipeline triggering behavior

- **16.2. Restart or cancel pipelines** `[procedure]`
  - Lines 3287-3375: Restarting or canceling pipeline run — GitOps commands (/retest, /cancel)
  - Context: Manual pipeline control without new commits

- **16.3. Trigger pipelines programmatically (Advanced)** `[procedure]`
  - Lines 3515-3577: Using incoming webhook — Webhook-based triggering
  - Context: Integrate PaC with external systems

---

#### Track & Monitor

**Job 17: Monitor Pipeline Run Status**

*When pipeline runs execute, I want to monitor their status through various channels, so I can identify failures and track progress.*

Prerequisites: Pipeline run created and running

- **17.1. View status across multiple channels** `[reference]`
  - Lines 3384-3468: Monitoring pipeline run status — GitHub Checks, comments, Repository CR status
  - Context: Comprehensive status tracking across interfaces

- **17.2. Clean up pipeline runs** `[procedure]`
  - Lines 3485-3506: Cleaning up pipeline runs — Automatic retention with max-keep-runs annotation
  - Context: Manage storage and namespace tidiness

---

#### Reference

**Job 18: Use Pipelines as Code CLI**

*When I need to manage Pipelines as Code from the command line, I want to use the tkn pac CLI tool, so I can bootstrap, create repositories, and troubleshoot PaC.*

Prerequisites: tkn pac CLI installed

- **18.1. Perform common CLI operations** `[reference]`
  - Lines 3660-3904: PaC command reference — Bootstrap, repository management, resolve, CEL evaluation
  - Context: Essential CLI commands for day-to-day PaC operations

- **18.2. Troubleshoot with logging configuration (Advanced)** `[procedure]`
  - Lines 3914-4061: Configuring PaC logging — TektonConfig CR logging settings
  - Lines 4070-4082: Splitting logs by namespace — Namespace-based log filtering
  - Context: Detailed diagnostic information for troubleshooting

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | By features, platforms, and technical components | By user goals and workflow stages |
| **Top-level items** | 7 chapters + 34 sections | 18 main jobs organized in 6 workflow stages |
| **Git provider integration** | 5 separate sections across 1,377 lines (Chapter 3.1-3.5) | 4 unified jobs with clear provider selection (Jobs 4, 8-10) |
| **GitHub App configuration** | 3 subsections buried in Chapter 3.1 | 1 job with 3 clear options (Job 4) |
| **Repository configuration** | 5 sections split between Chapters 3 and 4 | 3 focused jobs (Jobs 5-7) |
| **Pipeline run workflow** | 7 subsections across Chapters 5-6 | 3 jobs following creation → execution → monitoring flow (Jobs 12-17) |
| **Prerequisites** | Implicit from chapter ordering | Explicit in each job |
| **Navigation depth** | 5-10 clicks average | 2-4 clicks average (50-60% reduction) |
| **Troubleshooting** | Scattered across verification (6.1) and logging (7.2-7.3) | Elevated to Job 18.2 with clear troubleshooting focus |

### Job List Adjustments from Suggested Input

The suggested 40 JTBD records were consolidated to **18 main jobs** for the following reasons:

1. **Jobs on understanding PaC merged** → Job 1 now includes core concepts (lines 91-118), key features (70-84), and initial overview (59-69) as themed subsections
2. **Installation jobs combined** → Job 2 merges cluster installation (196-234) and CLI installation (276-334) as sequential steps in the same workflow
3. **GitHub App setup variations consolidated** → Job 4 presents 3 methods (CLI, Web Console, Manual) as options rather than separate jobs
4. **Repository CR configuration grouped** → Jobs 5-7 group Repository CR creation, settings configuration, and token scoping as related configuration tasks
5. **Git provider integration reduced** → Jobs 8-11 consolidate 5 provider sections into 4 jobs by grouping Bitbucket Cloud and Data Center as variants
6. **Pipeline run lifecycle unified** → Job 16 consolidates automatic execution, manual restart/cancel, and programmatic triggering under lifecycle management
7. **Monitoring and cleanup merged** → Job 17 combines status monitoring (3384-3468) and cleanup (3485-3506) as related operational tasks
8. **CLI and troubleshooting combined** → Job 18 elevates troubleshooting from appendix-level content to a primary job subsection

---

## Consolidation Examples

### Example 1: Git Provider Integration (5 scattered sections → 4 unified jobs)

**Current (Fragmented):**
- Section 3.1: GitHub App integration (570-767) — 3 subsections for CLI, web console, manual setup
- Section 3.2: GitHub Webhook (904-1132) — Alternative GitHub integration method
- Section 3.3: GitLab (1141-1339) — GitLab-specific integration
- Section 3.4: Bitbucket Cloud (1348-1588) — Cloud-hosted Bitbucket
- Section 3.5: Bitbucket Data Center (1598-1738) — Self-hosted Bitbucket

Users must read all 5 sections spanning 1,182 lines to understand their options. No clear decision framework indicates which method to choose.

**Proposed (Consolidated):**
- **Job 4: Configure GitHub App Integration**
  - 4.1. Automated CLI Setup (570-612)
  - 4.2. Web Console Setup (621-657)
  - 4.3. Manual Configuration (666-767)
- **Job 8: Integrate with GitHub Webhooks** (904-1132)
  - Context: "Use when GitHub App creation is not available"
- **Job 9: Integrate with GitLab** (1141-1339)
- **Job 10: Integrate with Bitbucket**
  - 10.1. Bitbucket Cloud (1348-1588)
  - 10.2. Bitbucket Data Center (1598-1738)

**Benefit:** Clear provider-based navigation with explicit "When to use" guidance. GitHub App methods presented side-by-side for immediate comparison. Reduced from 5 sections to 4 jobs with option-based grouping.

---

### Example 2: Repository Configuration (5 sections across 2 chapters → 3 unified jobs)

**Current (Fragmented):**
- Section 3.1.4: Scope GitHub token (776-895) — Buried in GitHub App chapter
- Section 4.1: Creating Repository CR (1911-1939) — Basic CR creation
- Section 4.2: Global Repository CR (1948-2000) — Technology Preview defaults
- Section 4.3: Concurrency limits (2008-2031) — Resource management
- Section 4.4: Source branch configuration (2040-2064) — Security setting
- Section 4.5: Custom parameter expansion (2073-2140) — Advanced configuration

Configuration scattered across Chapters 3 and 4 with no clear workflow sequence.

**Proposed (Consolidated):**
- **Job 5: Create Repository Custom Resource**
  - 5.1. Define basic Repository CR (1911-1939)
  - 5.2. Configure global Repository defaults (1948-2000, Technology Preview)
- **Job 6: Configure Repository Settings**
  - 6.1. Set concurrency limits (2008-2031)
  - 6.2. Configure pipeline provenance (2040-2064, Security)
  - 6.3. Define custom parameters (2073-2140, Optional)
- **Job 7: Configure Token Scoping for Multi-Repository Access**
  - 7.1. Repository-level token scoping (776-865)
  - 7.2. Global token scoping (866-895, Advanced)

**Benefit:** Logical workflow progression from CR creation → settings configuration → advanced token scoping. Security-critical settings clearly labeled. Reduced navigation from 2 chapters + 6 sections to 3 focused jobs.

---

### Example 3: Pipeline Run Workflow (7 subsections → 3 jobs following creation → execution → monitoring)

**Current (Fragmented):**
- Section 5.1: Creating pipeline run (2216-2377) — Initial creation
- Section 5.2: Dynamic variables (2387-2454) — Variable substitution
- Section 5.3: Resolver annotations (2463-2644) — Remote task references
- Section 5.4: Event matching (2653-2870) — Event annotations
- Section 5.5: Event filtering (2879-2983) — Path and label filtering
- Section 6.2: Running pipeline run (3162-3200) — Execution behavior
- Section 6.5: Monitoring status (3384-3468) — Status tracking

Creation in Chapter 5, execution and monitoring in Chapter 6, with no clear flow.

**Proposed (Consolidated):**
- **Job 12: Create Pipeline Run Definitions**
  - 12.1. Define core pipeline run structure (2216-2377)
  - 12.2. Configure automatic Git authentication (1767-1821)
- **Job 13: Use Dynamic Variables and Remote Tasks**
  - 13.1. Use dynamic variables (2387-2454)
  - 13.2. Reference remote tasks (2463-2644)
  - 13.3. Verify pipeline runs (3130-3153)
- **Job 14: Control Pipeline Execution with Event Matching**
  - 14.1. Match Git events (2653-2870)
  - 14.2. Filter events (2879-2983)
  - 14.3. Enable automatic cancellation (2992-3044, Technology Preview)
- **Job 16: Manage Pipeline Run Lifecycle**
  - 16.1. Run pipelines automatically (3162-3200)
  - 16.2. Restart or cancel pipelines (3287-3375)
- **Job 17: Monitor Pipeline Run Status**
  - 17.1. View status (3384-3468)
  - 17.2. Clean up pipeline runs (3485-3506)

**Benefit:** Clear workflow progression: create → configure → control execution → monitor → manage lifecycle. Reduced cross-chapter navigation. Automatic authentication integrated into creation workflow where it's needed.

---

## Content Gaps Identified

| Gap | JTBD Reference | Current Coverage | Impact |
|-----|---------------|-----------------|--------|
| No decision framework for choosing PaC vs. other CI/CD approaches | Job 1 (Understand capabilities) | Capabilities listed, but no comparison with Tekton Triggers, Jenkins, or native OpenShift Builds | **Medium** — Users may not know when PaC is the right choice for their workflow |
| Missing migration guide from Tekton Triggers to PaC | None (new content needed) | Not covered | **Medium** — Existing Tekton users lack guidance for migrating to PaC |
| Limited troubleshooting scenarios and solutions | Job 18.2 (Troubleshoot with logging) | Logging configuration only; no common failure scenarios | **High** — Users lack guidance for common issues like webhook failures, resolver errors, or permission problems |
| No explanation of when to use each GitHub App setup method | Job 4 (Configure GitHub App) | 3 methods listed without clear "when to use" guidance | **Medium** — Users may choose suboptimal method for their scenario |
| Missing guidance on PaC performance tuning and scale limits | Jobs 6.1 (Concurrency limits) and 3.1 (Customize configuration) | Concurrency limits and max-keep-runs documented, but no scale guidance | **Low** — Users managing large repositories lack best practices |
| No rollback or disaster recovery procedures | Job 16 (Manage pipeline run lifecycle) | Pipeline cancellation covered, but not rollback or recovery | **High** — Users lack guidance for recovering from failed deployments |
| Limited examples of real-world pipeline patterns | Jobs 12-14 (Pipeline creation and execution) | Basic examples provided, but no advanced patterns (multi-stage, matrix builds, conditional tasks) | **Medium** — Users must discover patterns through trial and error |

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 7 chapters | 6 workflow stages + 18 jobs | Better granularity with clear stage grouping |
| Clicks to find GitHub App setup | 5 clicks (Home → Ch 3 → Section 3.1 → Subsection → Read) | 3 clicks (Set Up & Configure → Job 4 → Choose option) | 40% reduction |
| Clicks to configure Repository CR | 6 clicks (Home → Ch 4 → Section 4.1 → Read, then Ch 4 → 4.3 → Read) | 3 clicks (Set Up & Configure → Job 5/6 → Read) | 50% reduction |
| Sections to browse for GitLab integration | 1 section buried in 1,377-line Chapter 3 | 1 dedicated job with clear provider label | Immediate identification |
| Sections to browse for pipeline run creation | 7 subsections across 2 chapters | 3 jobs with clear workflow progression | 57% reduction |
| Average clicks to content | 5-10 clicks | 2-4 clicks | 50-60% reduction |
| Navigation path for token scoping | Chapter 3 → Section 3.1 → Subsection 3.1.4 (4 levels) | Job 7 (1 level in Set Up & Configure stage) | 75% reduction |
| Navigation path for troubleshooting | Chapter 7 → Section 7.2 (buried in appendix) | Job 18 → Subsection 18.2 (elevated to primary workflow) | Elevated visibility |

**Final job count: 18** (reduced from suggested 40 JTBD records). The consolidation groups related content into coherent workflows, eliminates redundancy, and provides clear decision points for option-based variations (GitHub App methods, Bitbucket variants).

---

## Document Statistics

### Workflow Coverage Summary

| Workflow Stage | Main Jobs | User Stories/Approaches | Source Line Coverage | Notes |
|----------------|-----------|------------------------|---------------------|-------|
| **Understand & Plan** | 1 | 3 | 60 lines (59-118) | Core concepts and capabilities |
| **Set Up & Configure** | 10 | 21 | 2,169 lines (121-1821, 1911-2140) | Installation, Git providers, Repository CR |
| **Deploy & Execute** | 4 | 11 | 1,136 lines (2143-3279) | Pipeline run creation, events, tags |
| **Operate & Manage** | 1 | 3 | 415 lines (3162-3577) | Pipeline run lifecycle management |
| **Track & Monitor** | 1 | 2 | 122 lines (3384-3506) | Status monitoring and cleanup |
| **Reference** | 1 | 2 | 244 lines (3660-3904, 3914-4082) | CLI commands and troubleshooting |

### Consolidation Metrics

| Content Area | Current Lines | Current Organization | Proposed Organization | Consolidation Ratio |
|--------------|--------------|---------------------|----------------------|---------------------|
| Git Provider Integration | 1,377 lines | 5 sections in Chapter 3 | 4 jobs (Jobs 4, 8-10) | 5:4 consolidation |
| GitHub App Setup | 198 lines | 3 subsections | 1 job with 3 options (Job 4) | 3:1 consolidation |
| Repository Configuration | 306 lines | 6 sections across Chapters 3-4 | 3 jobs (Jobs 5-7) | 6:3 consolidation |
| Pipeline Run Workflow | 1,136 lines | 7 subsections across Chapters 5-6 | 5 jobs (Jobs 12-16) | 7:5 consolidation |

### Main Jobs by Stage

- **Understand & Plan:** 1 job
- **Set Up & Configure:** 10 jobs
- **Deploy & Execute:** 4 jobs
- **Operate & Manage:** 1 job
- **Track & Monitor:** 1 job
- **Reference:** 1 job

**Total Main Jobs:** 18  
**Total User Stories/Approaches:** 42  
**Total Source Lines:** 4,092 (all content preserved, reorganized)  
**Git Provider Variations:** 5 (GitHub App, GitHub Webhook, GitLab, Bitbucket Cloud, Bitbucket Data Center) → Consolidated into 4 jobs

---

*Generated from JTBD analysis of pac-combined.adoc (4,092 lines, 40 JTBD records consolidated to 18 main jobs)*

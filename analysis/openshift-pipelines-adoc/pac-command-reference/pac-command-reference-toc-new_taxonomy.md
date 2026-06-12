# Pipelines as Code Command Reference
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** Enable platform engineers and developers to install, configure, test, and troubleshoot Pipelines as Code using CLI commands and logging configuration.

**Personas:** Platform engineer, Developer

**Main Jobs:** 6 core jobs across 5 workflow stages

---

## Quick Navigation

**I want to:**
- Install and configure Pipelines as Code -> Job 1 (Get Started)
- Create GitHub application for PAC -> Job 1 (Get Started)
- Create and view PAC repositories -> Job 2 (Administer)
- Test pipeline runs locally -> Job 3 (Develop)
- Override parameters during testing -> Job 3 (Develop)
- Debug CEL event filters -> Job 4 (Troubleshoot)
- Test CEL expressions interactively -> Job 4 (Troubleshoot)
- Configure log verbosity -> Job 5 (Configure)
- View logs for specific namespace -> Job 6 (Troubleshoot)

---

# Table of Contents

## Getting Started

### Job 1: Set Up Pipelines as Code for Git Repository
*When I need to bootstrap Pipelines as Code installation and integrate with my Git provider*

**Personas:** Platform engineer

**Timing:** BEFORE Job 2 (Create Pipelines as Code repository) - installation required

**Requires:** Install OpenShift Pipelines, tkn CLI with pac plugin, cluster-admin access

#### Bootstrap Installation Approaches

**Context:** Two distinct bootstrap approaches exist depending on deployment needs and Git provider.

- **Option A: Standard Bootstrap Installation**
  (For general installation with automatic route detection)
  
  → Lines 108-120: Bootstrap command reference
    Source: modules/op-pipelines-as-code-command-reference.adoc
  
  - Installs PAC for Git providers (GitHub, GitHub Enterprise)
  - Automatic OpenShift route detection
  - Single command completion

- **Option B: Bootstrap with Custom Route**
  (For custom ingress configurations)
  
  → Lines 119-124: Route URL override option
    Source: modules/op-pipelines-as-code-command-reference.adoc
  
  - Override default route URL
  - Custom ingress endpoint specification
  - Non-OpenShift cluster support

- **Option C: Nightly Build Installation**
  (For testing latest features)
  
  → Lines 117-118: Nightly build option
    Source: modules/op-pipelines-as-code-command-reference.adoc

#### GitHub Application Setup

**Context:** Required for GitHub OAuth integration and webhook automation.

- **Task:** Create GitHub Application and Secrets
  
  → Lines 125-127: GitHub app creation command
    Source: modules/op-pipelines-as-code-command-reference.adoc
  
  - Prerequisites: Bootstrap PAC, GitHub organization admin access
  - Automatic OAuth app setup
  - Secret generation in openshift-pipelines namespace

---

## Administer Platform

### Job 2: Manage Pipelines as Code Repositories
*When I need to onboard Git repositories and track their integration status*

**Personas:** Developer

**Requires:** Bootstrap Pipelines as Code, access to target namespace, Git repository URL

#### Repository Management Operations

- **Task 2.1: Create New Repository**
  (Onboard Git repository to Pipelines as Code)
  
  → Lines 136-137: Create repository command
    Source: modules/op-pipelines-as-code-command-reference.adoc
  
  - Single-command repository creation
  - Automatic namespace setup
  - Pipeline run template generation

- **Task 2.2: List All Repositories**
  (View repository status and recent runs)
  
  → Lines 138-139: List repositories command
    Source: modules/op-pipelines-as-code-command-reference.adoc
  
  - Quick repository health check
  - Last run status visibility
  - Multi-namespace overview

- **Task 2.3: Describe Repository Details**
  (Inspect specific repository and run history)
  
  → Lines 140-142: Describe repository command
    Source: modules/op-pipelines-as-code-command-reference.adoc
  
  - Complete repository details
  - Associated runs history
  - Troubleshooting information

---

## Develop & Test

### Job 3: Test Pipeline Runs Locally
*When I need to validate pipeline logic before committing to Git*

**Personas:** Developer

**Requires:** Pipeline run templates in .tekton directory

**Why:** Reduces commit noise and enables faster iteration on pipeline development

#### Local Testing Workflow

- **Task 3.1: Generate Basic Pipeline Run**
  (Create starter pipeline with automatic detection)
  
  → Lines 144-159: Generate command reference
    Source: modules/op-pipelines-as-code-command-reference.adoc
  
  - Language-specific task detection (e.g., pylint for Python)
  - Automatic Git information detection
  - Repository directory scaffolding

- **Task 3.2: Resolve Pipeline Run Locally**
  (Test execution without Git commit)
  
  → Lines 161-175: Resolve command reference
    Source: modules/op-pipelines-as-code-command-reference.adoc
  
  - Execute as if PAC owns pipeline
  - Auto-detect current Git context
  - Pipe to `oc apply` for immediate execution
  - Local Kubernetes cluster required

- **Task 3.3: Override Git Parameters**
  (Test different branches or repository configurations)
  
  → Lines 176-182: Parameter override examples
    Source: modules/op-pipelines-as-code-command-reference.adoc
  
  - Override revision, repo_name, and other parameters
  - Test multi-repository pipelines
  - Branch switching without changing Git state
  - File and directory input support

---

## Troubleshoot Issues

### Job 4: Debug Event Filtering Logic
*When I need to verify CEL expressions match expected webhook events*

**Personas:** Platform engineer

**Requires:** Webhook payload and header data, CEL expression syntax knowledge

**Note:** Technology Preview feature for advanced event filtering debugging

#### CEL Expression Testing

- **Task 4.1: Test Expressions Interactively**
  (Iterate on expression logic with real webhook data)
  
  → Lines 264-266, 311-316: Interactive mode description
    Source: modules/op-pipelines-as-code-command-reference.adoc
  
  - REPL with arrow key navigation
  - Persistent expression history across sessions
  - Real-time evaluation against webhook payload
  - Command: `tkn pac cel -b body.json -H headers.txt`

- **Task 4.2: Automate Expression Validation**
  (CI/CD integration for expression testing)
  
  → Lines 268-275: Noninteractive mode usage
    Source: modules/op-pipelines-as-code-command-reference.adoc
  
  - stdin input for automation
  - Example: `echo 'event == "pull_request"' | tkn pac cel -b body.json -H headers.txt`
  - Testing framework integration

- **Task 4.3: Understand CEL Variables**
  (Reference for available expression variables)
  
  → Lines 277-291: CEL variables documentation
    Source: modules/op-pipelines-as-code-command-reference.adoc
  
  Available variables:
  - `event`, `target_branch`, `source_branch`
  - `target_url`, `source_url`, `event_title`
  - `body.*` (webhook payload fields)
  - `headers.*` (HTTP headers)
  - `pac.*` (backward compatibility)
  
  **Note:** `files.*` variables always empty in CLI mode

- **Task 4.4: Use Common Expression Patterns**
  (Example expressions for typical use cases)
  
  → Lines 299-309: Example expressions
    Source: modules/op-pipelines-as-code-command-reference.adoc
  
  - Event and branch filtering
  - Header inspection
  - Draft PR exclusion
  - Branch pattern matching

---

## Configure Platform

### Job 5: Control Log Verbosity for PAC Components
*When I need to adjust log detail based on operational requirements*

**Personas:** Platform engineer

**Requires:** PAC installed, cluster-admin access to TektonConfig, OpenShift web console or oc CLI access

#### Logging Configuration Approaches

- **Task 5.1: Configure Default Log Levels**
  (Adjust component-specific log verbosity)
  
  → Lines 348-397: TektonConfig log level fields
    Source: modules/op-configuring-pipelines-as-code-logging.adoc
  
  Component log levels:
  - `loglevel.pac-watcher` - watcher component
  - `loglevel.pipelines-as-code-webhook` - webhook component
  - `loglevel.pipelinesascode` - controller component
  
  **Procedure:**
  1. Navigate to Administration → CustomResourceDefinitions
  2. Search for `tektonconfigs.operator.tekton.dev`
  3. Click config instance → YAML tab
  4. Edit loglevel fields under `.options.configMaps.pac-config-logging.data`

- **Task 5.2: Create Custom Logging Configuration**
  (Apply specialized logging formats or handlers)
  
  → Lines 398-472: Custom logging config map setup
    Source: modules/op-configuring-pipelines-as-code-logging.adoc
  
  - Create custom config map (e.g., `custom-pac-config-logging`)
  - Reference via `CONFIG_LOGGING_NAME` environment variable
  - zap logger configuration understanding required
  - Independent control per deployment (controller, watcher, webhook)

---

## Troubleshoot Issues

### Job 6: Isolate Logs for Specific Namespace
*When I need to troubleshoot issues for individual teams or projects*

**Personas:** Platform engineer

**Requires:** PAC running, oc CLI installed, target namespace name, PAC controller pod name

#### Namespace-Scoped Log Filtering

- **Task: Filter Logs by Namespace**
  (Extract relevant log entries for namespace)
  
  → Lines 486-493: Log filtering procedure
    Source: modules/op-splitting-pipelines-as-code-logs-by-namespace.adoc
  
  - Command: `oc logs pipelines-as-code-controller-<unique_id> -n openshift-pipelines | grep mynamespace`
  - Single-command filtering
  - Multi-tenant environment support
  - Efficient troubleshooting isolation

---

## Appendices

### A. Command Quick Reference

| Command | Purpose | Job Reference |
|---------|---------|---------------|
| `tkn pac bootstrap` | Install and configure PAC | Job 1 |
| `tkn pac bootstrap github-app` | Create GitHub application | Job 1 |
| `tkn pac create repository` | Create new repository | Job 2 |
| `tkn pac list` | List all repositories | Job 2 |
| `tkn pac repo describe` | Describe repository details | Job 2 |
| `tkn pac generate` | Generate basic pipeline run | Job 3 |
| `tkn pac resolve` | Resolve pipeline locally | Job 3 |
| `tkn pac cel` | Evaluate CEL expressions | Job 4 |

### B. Workflow Coverage Analysis

| Stage | Coverage | Jobs | Notes |
|-------|----------|------|-------|
| Get Started | ✅ | Job 1 | Bootstrap installation and configuration |
| Configure | ✅ | Job 5 | Logging configuration via TektonConfig |
| Develop | ✅ | Job 3 | Local testing workflow |
| Administer | ✅ | Job 2 | Repository lifecycle management |
| Troubleshoot | ✅ | Jobs 4, 6 | CEL debugging and log filtering |
| Monitor | ❌ | - | No observability content |
| Upgrade | ❌ | - | No upgrade procedures |
| Reference | ✅ | All jobs | CLI command reference throughout |

### Gaps Identified

| Stage | Gap | Recommendation |
|-------|-----|----------------|
| Monitor | No observability guidance | Add section on viewing pipeline run metrics |
| Upgrade | No upgrade procedures | Add PAC upgrade and migration content |
| Secure | No security configuration | Add authentication and authorization setup |
| Operate | Limited operational guidance | Add backup/restore, high availability content |

---

## Navigation Guide

### By User Journey

**Platform Engineer installing PAC:**
1. Job 1: Bootstrap installation and configure Git provider
2. Job 5: Configure logging for operational needs
3. Job 2: Create initial repository configurations

**Developer onboarding to PAC:**
1. Job 3.1: Generate basic pipeline run template
2. Job 3.2: Test pipeline locally before committing
3. Job 2.1: Create repository in PAC

**Platform Engineer troubleshooting:**
1. Job 6: Filter logs by namespace
2. Job 4: Debug CEL event filters
3. Job 2.3: Describe repository for run history

**Advanced Developer testing workflows:**
1. Job 3.3: Override parameters for branch testing
2. Job 3.2: Resolve and apply to local cluster
3. Job 4.1: Test CEL expressions interactively

---

## Document Statistics

**Workflow Coverage:**
- Get Started: 1 job
- Configure: 1 job
- Develop: 1 job
- Administer: 1 job
- Troubleshoot: 2 jobs
- Monitor: Gap identified
- Upgrade: Gap identified

**Main Jobs:** 6
**User Stories/Paths:** 15 approaches
**Source Sections:** 3 modules (op-pipelines-as-code-command-reference, op-configuring-pipelines-as-code-logging, op-splitting-pipelines-as-code-logs-by-namespace)
**Command Variations:** 8 primary commands with options

# Pipelines as Code Command Reference
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** This reference guide helps platform engineers, DevOps engineers, and pipeline developers control Pipelines as Code using CLI tools and logging configurations.

**Personas:** Platform Engineer, Cluster Administrator, DevOps Engineer, Pipeline Developer

**Main Jobs:** 7 core jobs across 4 workflow stages (Configure, Prepare, Confirm, Troubleshoot)

---

## Quick Navigation

**I want to:**
- Set up Pipelines as Code for my organization → Job 1 (Configure)
- Connect my repository to PaC → Job 2 (Configure)
- Create a starter pipeline template → Job 3 (Prepare)
- Test my pipeline locally → Job 4 (Confirm)
- Validate webhook filtering logic → Job 5 (Troubleshoot)
- Control logging verbosity → Job 6 (Configure)
- View logs for specific namespaces → Job 7 (Troubleshoot)

---

# Table of Contents

## Set Up & Configure

### Job 1: Install and Configure Pipelines as Code
*When I need to set up Pipelines as Code for my organization*

**Personas:** Platform Engineer, Cluster Administrator

**Prerequisites:** OpenShift cluster access, Git repository hosting service account

#### Bootstrap Installation Options

- **Standard Bootstrap Installation**
  → Lines 108-119: Bootstrap commands
  - Automates installation and configuration
  - Detects OpenShift routes automatically
  - Integrates with GitHub or GitHub Enterprise

- **Nightly Build Installation**
  → Lines 117: Bootstrap nightly option
  - Installs latest development build
  - For testing unreleased features

- **Custom Route Override**
  → Lines 119-123: Route URL override
  - Override detected OpenShift route
  - Specify public URL for ingress endpoint
  - Required for non-OpenShift clusters

- **GitHub App Credential Setup**
  → Lines 125-126: GitHub app credentials
  - Creates GitHub App automatically
  - Stores secrets in openshift-pipelines namespace
  - Establishes authenticated PaC-GitHub communication

---

### Job 2: Create and Manage Repository Configurations
*When I need to connect my source code repository to Pipelines as Code*

**Personas:** DevOps Engineer, Pipeline Developer

**Prerequisites:** Pipelines as Code installed, Access to source code repository

#### Repository Management Tasks

- **Create New Repository**
  → Lines 136: Create repository command
  - Creates namespace automatically
  - Generates repository configuration from template
  - Single-command setup

- **List All Repositories**
  → Lines 138: List repositories command
  - Shows all configured PaC repositories
  - Displays last run status
  - Monitors pipeline health across projects

- **Describe Repository Details**
  → Lines 140-142: Describe repository command
  - Views repository configuration
  - Shows associated runs and history
  - Understands pipeline execution patterns

---

## Prepare

### Job 3: Generate Starter Pipeline Templates
*When I need to create a pipeline run for my application*

**Personas:** Pipeline Developer

**Prerequisites:** Source code repository with application code

#### Template Generation

- **Auto-Detected Language Template**
  → Lines 151-158: Generate command
  - Detects current Git information automatically
  - Identifies programming language
  - Adds language-specific tasks (e.g., pylint for Python)
  - Creates customized starter pipeline without manual configuration

---

## Confirm

### Job 4: Test Pipeline Changes Locally
*When I need to test pipeline changes without creating commits*

**Personas:** Pipeline Developer

**Prerequisites:** Pipeline run YAML files, Local Kubernetes cluster access

**Why:** Reduces iteration time and avoids polluting Git history with test commits

#### Local Testing Approaches

- **Execute Pipeline Run Locally**
  → Lines 168-174: Resolve command
  - Simulates PaC execution environment
  - Observes live pipeline run
  - Tests without triggering webhooks

- **Override Parameter Values**
  → Lines 176-181: Resolve with parameters
  - Tests with different parameter values
  - Validates pipeline behavior with various inputs
  - Avoids modifying YAML files for testing
  - Accepts directory path for batch resolution

---

## Troubleshoot

### Job 5: Validate Webhook Event Filtering
*When I need to validate webhook event filtering logic*

**Personas:** Cluster Administrator, Platform Engineer

**Prerequisites:** Webhook payload samples, Webhook headers, CEL expression syntax knowledge

**Timing:** TECHNOLOGY PREVIEW FEATURE - not supported for production use

#### CEL Expression Evaluation

- **Interactive CEL Testing**
  → Lines 210-225, 264-266: CEL command and interactive mode
  - Tests CEL expressions against webhook payloads
  - Uses expression history with arrow key navigation
  - Validates filtering before production deployment
  - Supports plain HTTP, JSON, or Gosmee-generated header formats

- **Non-Interactive CEL Testing**
  → Lines 271-275: Non-interactive mode
  - Accepts expressions via stdin
  - Automates testing in scripts
  - Evaluates without interactive prompt

- **Available Variables Reference**
  → Lines 277-295: CEL variables
  - `event`: Event type (push, pull_request)
  - `target_branch`, `source_branch`: Branch names
  - `target_url`, `source_url`: Repository URLs
  - `event_title`: PR title or commit message
  - `body.*`: All webhook payload fields
  - `headers.*`: All HTTP headers
  - Note: `files.*` always empty in CLI mode

- **Expression Examples**
  → Lines 297-308: Example expressions
  - Event and branch filtering
  - Branch pattern matching with regex
  - Action-specific triggers
  - Draft PR exclusion
  - Header inspection

---

### Job 6: Configure Logging Levels
*When I need to control logging verbosity for troubleshooting*

**Personas:** Cluster Administrator, Platform Engineer

**Prerequisites:** Pipelines as Code installed, Cluster admin access

#### Logging Configuration Methods

- **Default Logging ConfigMap**
  → Lines 336-396: Configure pac-config-logging
  - Edits pac-config-logging configmap in TektonConfig CR
  - Sets log levels for controller, webhook, and watcher components
  - Adjusts observability based on operational needs
  - Supported levels: info, warn, debug

- **Custom Logging ConfigMap**
  → Lines 398-472: Custom logging configuration
  - Creates custom logging configmap
  - References custom configmap in deployment specs
  - Maintains separate configurations per component
  - Provides component-specific logging flexibility

---

### Job 7: Filter Logs by Namespace
*When I need to troubleshoot pipeline issues for specific projects*

**Personas:** DevOps Engineer, Pipeline Developer

**Prerequisites:** Access to PaC controller pods, Target namespace name

#### Namespace Log Filtering

- **Grep Filter Logs**
  → Lines 486-492: Namespace log filtering
  - Uses `oc logs` with grep to filter namespace events
  - Isolates relevant log entries
  - Reduces noise from other namespaces
  - Example: `oc logs pipelines-as-code-controller-<id> -n openshift-pipelines | grep mynamespace`

---

## Appendices

### A. Command Quick Reference

| Command | Purpose | Key Options |
|---------|---------|-------------|
| `tkn pac bootstrap` | Install and configure PaC | `--nightly`, `--route-url` |
| `tkn pac bootstrap github-app` | Create GitHub App credentials | (none) |
| `tkn pac create repository` | Create new PaC repository | (template-based) |
| `tkn pac list` | List repositories with status | (none) |
| `tkn pac repo describe` | View repository details and runs | (none) |
| `tkn pac generate` | Generate starter pipeline | (auto-detects language) |
| `tkn pac resolve` | Execute pipeline locally | `-f`, `-p` for parameters |
| `tkn pac cel` | Evaluate CEL expressions | `-b` (body), `-H` (headers), `-p` (provider) |

### B. Workflow Coverage Analysis

| Stage | Coverage | Jobs | Notes |
|-------|----------|------|-------|
| Get Started | ❌ | - | No quickstart or overview content |
| Plan | ❌ | - | No architecture or decision guidance |
| Configure | ✅ | Jobs 1, 2, 6 | Bootstrap, repository setup, logging |
| Deploy | ❌ | - | No deployment procedures (assumes installed) |
| Prepare | ✅ | Job 3 | Pipeline template generation |
| Confirm | ✅ | Job 4 | Local pipeline testing |
| Operate | ❌ | - | No operational procedures |
| Monitor | ⚠️ Limited | Job 7 (partial) | Only namespace log filtering |
| Troubleshoot | ✅ | Jobs 5, 7 | CEL validation, log filtering |
| Administer | ⚠️ Limited | Job 6 | Logging configuration only |
| Reference | ✅ | All jobs | Command reference throughout |

### Gaps Identified

| Gap | Recommendation | Priority |
|-----|----------------|----------|
| Get Started | Add quickstart with common workflow | High |
| Architecture | Add PaC component architecture overview | Medium |
| Deploy | Link to main PaC installation guide | High |
| Operate | Add operational procedures (backup, restore) | Medium |
| Monitor | Add observability guide link or basic health checks | Medium |

---

## Navigation Guide

### By User Journey

**Platform Engineer setting up PaC for organization:**
1. Job 1: Install and Configure Pipelines as Code
2. Job 2: Create and Manage Repository Configurations
3. Job 6: Configure Logging Levels
4. Job 5: Validate Webhook Event Filtering

**Pipeline Developer creating and testing pipelines:**
1. Job 3: Generate Starter Pipeline Templates
2. Job 4: Test Pipeline Changes Locally
3. Job 7: Filter Logs by Namespace

**Cluster Administrator troubleshooting issues:**
1. Job 6: Configure Logging Levels
2. Job 7: Filter Logs by Namespace
3. Job 5: Validate Webhook Event Filtering

---

## Document Statistics

**Workflow Coverage:**
- Configure: 3 jobs
- Prepare: 1 job
- Confirm: 1 job
- Troubleshoot: 2 jobs
- **Gaps:** Get Started, Plan, Deploy, Operate, Monitor (limited), Administer (limited)

**Main Jobs:** 7
**Approaches/Tasks:** 17
**Source Sections:** 5 major sections
**Platform/Tool Variations:** GitHub, GitHub Enterprise, OpenShift routes

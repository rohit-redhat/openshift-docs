# Using the Repository Custom Resource
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** Enable platform engineers to configure Repository custom resources for connecting Git repositories to Pipelines as Code

**Personas:** Platform engineer

**Main Jobs:** 4 core jobs across 2 workflow stages (Prepare, Modify)

---

## Quick Navigation

**I want to:**
- Connect my repository to trigger pipelines -> Job 1 (Prepare)
- Apply settings across all repositories -> Job 1.1 (Prepare)
- Control concurrent pipeline runs -> Job 2 (Modify)
- Enforce pipeline code review -> Job 3 (Modify)
- Inject centralized configuration -> Job 4 (Prepare)

---

# Table of Contents

## Set Up Repository Integration

### Job 1: Connect Source Repository to Pipeline System
*When I need to connect my source code repository to the pipeline system*

**Personas:** Platform engineer

#### 1.1 Basic Repository Setup (Standard Approach)
**Goal:** Establish event matching between repository URL and pipeline namespace.

- **Task:** Create Repository CR in target namespace
  → Lines 76-103: Creating the Repository custom resource
  Source: modules/op-creating-repository-cr.adoc (REFERENCE)
  - Define repository URL for event matching
  - Specify target namespace (my-pipeline-ci)
  - Match pipeline runs from .tekton/ directory
  - **Security Note:** CR must be in same namespace as pipelines; use `pipelinesascode.tekton.dev/target-namespace` annotation to prevent cross-namespace execution

#### 1.2 Global Repository Configuration (Centralized Approach)
**Goal:** Apply common settings organization-wide without repetition.

**Personas:** Platform engineer (with administrator access)
**Status:** Technology Preview

- **Task:** Create global Repository CR in openshift-pipelines namespace
  → Lines 113-164: Creating the global Repository custom resource
  Source: modules/op-creating-global-repository-cr.adoc (PROCEDURE)
  - **Prerequisites:**
    - Administrator access to openshift-pipelines namespace
    - Logged in via oc CLI
  - Create CR named "pipelines-as-code"
  - Configure common GitLab webhook secrets (git_provider, webhook_secret)
  - Settings apply by default to all subsequent Repository CRs

## Control Pipeline Execution

### Job 2: Limit Concurrent Pipeline Runs
*When multiple pipeline runs could be triggered simultaneously for my repository*

**Personas:** Platform engineer
**Requires:** Existing Repository CR

- **Task:** Set concurrency_limit in Repository spec
  → Lines 173-196: Setting concurrency limits
  Source: modules/op-setting-concurrency-limits-in-repository-crd.adoc (REFERENCE)
  - Define maximum simultaneous runs (concurrency_limit: <number>)
  - **Behavior:** Pipeline runs queue and execute in alphabetical order
  - **Use Case:** Prevent resource exhaustion when pull request triggers multiple .tekton pipelines

### Job 3: Enforce Pipeline Code Review
*When I need to ensure pipeline definitions are reviewed before execution*

**Personas:** Platform engineer
**Why:** Prevents execution of unreviewed or malicious pipeline code from pull requests
**Requires:** Pipeline definitions merged into default branch

- **Task:** Configure pipeline definition source branch
  → Lines 205-228: Changing the source branch for the pipeline definition
  Source: modules/op-changing-source-branch-in-repository-crd.adoc (REFERENCE)
  - Set `pipelinerun_provenance: "default_branch"` in Repository CR settings
  - Pipeline definitions fetched from default branch (main/master/trunk)
  - **Security:** Requires merge review of all pipeline changes before execution

## Manage Pipeline Configuration

### Job 4: Inject Centralized Configuration into Pipeline Runs
*When I need to inject environment-specific or administratively-controlled values into pipeline runs*

**Personas:** Platform engineer
**Why:** Separate environment-specific configuration from pipeline code in Git

#### 4.1 Define Custom Parameters
**Goal:** Centrally manage values without modifying Git-based pipeline definitions.

- **Task:** Add params field to Repository CR
  → Lines 238-305: Custom parameter expansion
  Source: modules/op-custom-parameter-expansion.adoc (CONCEPT)
  - Define literal values (e.g., company: "ABC Company")
  - Reference Kubernetes secrets (secret_ref with name/key)
  - **Expansion:** Parameters replace {{ .params.company }} in PipelineRun and remotely fetched tasks
  - **Use Cases:**
    - Registry URLs varying by push vs. pull request
    - Account UUIDs managed by administrators
    - Environment-specific endpoints

#### 4.2 Apply Conditional Parameter Expansion
**Goal:** Use different parameter values based on event type.

- **Task:** Add CEL filters to parameter definitions
  → Lines 288-304: Custom parameter expansion with CEL filters
  Source: modules/op-custom-parameter-expansion.adoc (CONCEPT)
  - Filter format: `filter: pac.event_type == "pull_request"`
  - **Behavior:** First matching filter wins when multiple params share same name
  - Combine filters for push and pull_request events

---

## Appendices

### A. Repository CR Configuration Decision Guide

| Configuration Type | Use When | Scope | Prerequisites |
|-------------------|----------|-------|---------------|
| **Basic Repository CR** | Single repository setup | Namespace | None |
| **Global Repository CR** | Organization-wide defaults | Cluster (openshift-pipelines ns) | Admin access (Tech Preview) |
| **Concurrency limits** | Resource control needed | Per-repository | Existing Repository CR |
| **Default branch provenance** | Security review required | Per-repository | Merged pipeline defs |
| **Custom parameters** | Central config management | Per-repository | Repository CR, secret management |

**Choose based on:**
- **Basic Repository CR:** Starting point for all Pipelines as Code setups
- **Global Repository CR:** Reduce repetition across many repositories with shared secrets
- **Concurrency limits:** Prevent resource exhaustion in high-activity repositories
- **Default branch provenance:** Enforce security review on all pipeline code changes
- **Custom parameters:** Manage environment-specific values outside Git

### B. Workflow Coverage Analysis

| Stage | Coverage | Jobs | Notes |
|-------|----------|------|-------|
| Prepare | ✅ | Jobs 1, 4 | Repository creation, configuration management |
| Modify | ✅ | Jobs 2, 3 | Concurrency control, security policies |
| Execute | ❌ | - | No content on running pipelines (covered elsewhere) |
| Monitor | ❌ | - | No content on viewing pipeline run status |

### C. Gaps Identified

| Stage | Gap | Recommendation |
|-------|-----|----------------|
| Execute | No pipeline execution guidance | Link to "Running Pipelines as Code" guide |
| Monitor | No repository status monitoring | Add section on viewing last pipeline run status (mentioned in abstract but not documented) |
| Troubleshoot | No troubleshooting content | Add common Repository CR issues and resolutions |

---

## Navigation Guide

### By User Journey

**Platform Engineer setting up first repository:**
1. Job 1.1: Create basic Repository CR with repository URL
2. Job 3: Configure default branch provenance for security
3. Job 4.1: Define custom parameters for environment-specific values

**Platform Engineer managing multiple repositories:**
1. Job 1.2: Create global Repository CR with common secrets
2. Job 2: Set concurrency limits per repository as needed
3. Job 4.2: Apply conditional parameters based on event type

**Platform Engineer hardening security:**
1. Job 3: Enforce default branch provenance
2. Job 1.1: Use target-namespace annotation to prevent cross-namespace execution
3. Job 4.1: Store sensitive parameters in Kubernetes secrets (not literal values)

---

## Document Statistics

**Workflow Coverage:**
- Prepare: 2 jobs (Repository setup, Configuration management)
- Modify: 2 jobs (Concurrency control, Security policies)
- Execute: Gap identified
- Monitor: Gap identified

**Main Jobs:** 4
**User Stories/Paths:** 5 (2 under Job 1, 2 under Job 4, plus 3 standalone)
**Source Sections:** 5 modules (1 concept, 1 procedure, 3 reference)
**Platform/Tool Variations:** 1 (Global vs. basic Repository CR)

# Using the Repository Custom Resource
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** Enable platform engineers and cluster administrators to create and configure Repository CRs for automating pipeline runs triggered by Git repository events.

**Personas:** Platform engineer, Cluster administrator

**Main Jobs:** 5 core jobs across 2 workflow stages (Configure, Secure)

---

## Quick Navigation

**I want to:**
- Create a Repository CR for my Git repository → Job 1 (Configure)
- Set up shared configuration for multiple repositories → Job 2 (Configure)
- Control how many pipeline runs execute simultaneously → Job 3 (Configure)
- Enforce pipeline definition review before execution → Job 4 (Secure)
- Manage environment-specific parameters centrally → Job 5 (Configure)

---

# Table of Contents

## Set Up & Configure

### Job 1: Create a Repository CR That Matches Events from My Git Repository
*When I need to enable Pipelines as Code for my source repository*

**Personas:** Platform engineer

**Why:** Connects Git repository events to automated pipeline runs in the target namespace

#### 1.1 Create Repository CR Using tkn pac CLI or kubectl

**Goal:** Define the repository URL and namespace to enable event matching.

- **Task:** Create Repository CR with repository URL
  → Lines 80-96: Creating the Repository custom resource
  Source: Module op-creating-repository-cr.adoc
  - Specify repository URL in spec
  - Define target namespace
  - Event matching occurs when URLs match

#### 1.2 Use Explicit Namespace Targeting for Multi-Repository Scenarios

**Goal:** Prevent unauthorized pipeline runs when multiple Repository CRs could match the same event.

- **Task:** Add target-namespace annotation
  → Lines 98-103: Creating the Repository custom resource
  Source: Module op-creating-repository-cr.adoc
  - Add pipelinesascode.tekton.dev/target-namespace annotation
  - Prevents malicious actors from executing pipelines in unauthorized namespaces
  - Overrides oldest-match default behavior

**Context:** Critical for multi-tenant environments where namespace isolation must be enforced

---

### Job 2: Create a Global Repository CR with Shared Configuration
*When I manage multiple repositories with common settings*

**Personas:** Cluster administrator

**Timing:** BEFORE creating repository-specific Repository CRs - common settings apply by default

**Requires:** Administrator access to openshift-pipelines namespace, Git provider secrets created

#### 2.1 Create Global Repository CR Named pipelines-as-code

**Goal:** Provide common Git provider credentials to all repository CRs automatically.

- **Task:** Create Repository CR in openshift-pipelines namespace
  → Lines 134-164: Creating the global Repository custom resource
  Source: Module op-creating-global-repository-cr.adoc
  - Must be named "pipelines-as-code"
  - Include common secrets (git_provider, webhook_secret)
  - All subsequently created Repository CRs inherit these settings

**Note:** Technology Preview feature. Example shows GitLab configuration but pattern applies to other Git providers.

---

### Job 3: Set Concurrency Limits on a Repository CR
*When I need to control resource usage for pipeline runs*

**Personas:** Platform engineer

**Why:** Prevents resource exhaustion from concurrent pipeline runs overwhelming cluster resources

#### 3.1 Configure concurrency_limit in Repository CR Spec

**Goal:** Define maximum number of simultaneously executing pipeline runs.

- **Task:** Set concurrency_limit field
  → Lines 179-196: Setting concurrency limits
  Source: Module op-setting-concurrency-limits-in-repository-crd.adoc
  - Add concurrency_limit: \<number\> to Repository CR spec
  - Pipeline runs execute in alphabetical order when queued
  - Only specified number run simultaneously, rest queue

**Context:** If you have three pipeline runs in .tekton directory and set concurrency_limit to 1, all runs execute alphabetically with only one running at a time.

---

## Secure Your Environment

### Job 4: Configure the Repository CR to Fetch Pipeline Definitions from the Default Branch
*When I need to enforce pipeline definition review before execution*

**Personas:** Platform engineer

**Why:** Ensures all pipeline changes undergo merge review process, eliminating risk of unreviewed pipeline definitions executing from pull requests

**Timing:** Configure before accepting pull requests from external contributors - prevents pipeline definition injection

#### 4.1 Set pipelinerun_provenance to default_branch

**Goal:** Force all pipelines to use reviewed definitions from the default branch.

- **Task:** Configure pipelinerun_provenance setting
  → Lines 211-223: Changing the source branch for the pipeline definition
  Source: Module op-changing-source-branch-in-repository-crd.adoc
  - Add settings.pipelinerun_provenance: "default_branch" to Repository CR
  - Overrides default behavior of fetching from event branch
  - Requires merging pipeline definition to default branch before execution

**Security Impact:** With default behavior, Pipelines as Code uses pipeline definition from the submitted pull request. This setting requires merge reviews to verify all changes before execution.

---

## Set Up & Configure

### Job 5: Define Custom Parameters in the Repository CR
*When I need to manage pipeline parameters centrally without modifying pipeline runs in Git*

**Personas:** Platform engineer

**Requires:** Pipeline runs using custom parameters, understanding of difference between Tekton parameters and custom parameters

**Why:** Enables administrator-managed values (registry URLs, account identifiers) to be controlled from Repository CR location, separate from developer-controlled pipeline definitions

#### 5.1 Define Static Custom Parameters

**Goal:** Inject administrator-managed values into all matching pipeline runs.

- **Task:** Add params field with name and value
  → Lines 254-280: Custom parameter expansion
  Source: Module op-custom-parameter-expansion.adoc
  - Define params with name and value fields
  - Values replace custom parameters in pipeline runs and remote tasks
  - Alternative: Use secret_ref to retrieve values from Kubernetes secrets

**Example:**
```yaml
params:
  - name: company
    value: "ABC Company"
```

**Note:** Use custom parameters only when Tekton PipelineRun parameters are insufficient. Custom parameters are defined in Repository CR location, not alongside Pipeline in Git repository.

#### 5.2 Define Event-Specific Parameters with CEL Filters

**Goal:** Provide different parameter values for different event types (push vs pull request).

- **Task:** Add filter field with CEL expression
  → Lines 288-304: Custom parameter expansion
  Source: Module op-custom-parameter-expansion.adoc
  - Define multiple params with same name and different filters
  - First matching filter wins
  - Example filter: `pac.event_type == "pull_request"`

**Context:** Use when parameter values differ between event types. For example, different registry URLs for push events versus pull requests.

---

## Appendices

### A. Repository CR Configuration Quick Reference

| Feature | Field | Purpose |
|---------|-------|---------|
| Event matching | spec.url | Match repository URL to trigger events |
| Namespace targeting | annotation: pipelinesascode.tekton.dev/target-namespace | Force specific namespace (security) |
| Concurrency control | spec.concurrency_limit | Limit simultaneous pipeline runs |
| Pipeline provenance | spec.settings.pipelinerun_provenance | Fetch definitions from default branch |
| Custom parameters | spec.params | Centrally manage parameter values |

### B. Security Configuration Checklist

- [ ] **Namespace isolation:** Add target-namespace annotation in multi-tenant environments
- [ ] **Pipeline review:** Set pipelinerun_provenance to default_branch for external contributors
- [ ] **Secret management:** Use secret_ref for sensitive custom parameter values
- [ ] **Concurrency limits:** Set appropriate limits to prevent resource exhaustion

### C. Workflow Coverage Analysis

| Stage | Coverage | Jobs | Notes |
|-------|----------|------|-------|
| Configure | ✅ | Jobs 1, 2, 3, 5 | Repository CR creation and configuration |
| Secure | ✅ | Job 4 | Pipeline definition provenance control |
| Monitor | ❌ | - | No content for observing Repository CR status |
| Troubleshoot | ❌ | - | No troubleshooting procedures |
| Reference | ⚠️ Limited | Implied in procedures | No dedicated reference section for all fields |

### Gaps Identified

| Stage | Gap | Recommendation |
|-------|-----|----------------|
| Monitor | No observability for Repository CR status | Add section on viewing Repository CR status and last pipeline run information |
| Troubleshoot | No troubleshooting procedures | Add common issues: event not matching, pipeline runs not triggering, namespace conflicts |
| Reference | No complete Repository CR spec reference | Add comprehensive field reference table with all available fields |

---

## Navigation Guide

### By User Journey

**Platform Engineer enabling Pipelines as Code for first repository:**
1. Job 1: Create Repository CR with repository URL and namespace
2. Job 3: Set concurrency limits to prevent resource exhaustion
3. Job 5: Define custom parameters for environment-specific values

**Platform Engineer securing pipeline execution:**
1. Job 4: Configure pipeline definition provenance to enforce review
2. Job 1.2: Add explicit namespace targeting annotation
3. Job 5.2: Use event-specific parameters with CEL filters

**Cluster Administrator setting up centralized configuration:**
1. Job 2: Create global Repository CR with common settings
2. Job 5: Define shared custom parameters across all repositories

---

## Document Statistics

**Workflow Coverage:**
- Configure: 4 jobs (Jobs 1, 2, 3, 5)
- Secure: 1 job (Job 4)
- Monitor: Gap identified
- Troubleshoot: Gap identified
- Reference: Limited coverage

**Main Jobs:** 5
**Themed Sections:** 8 (approaches/tasks)
**Source Sections:** 5 modules referenced
**Feature Variations:** Global vs repository-specific configuration, static vs secret-referenced parameters, static vs CEL-filtered parameters

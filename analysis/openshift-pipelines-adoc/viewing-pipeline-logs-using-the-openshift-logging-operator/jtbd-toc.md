# Viewing pipeline logs by using the OpenShift Logging Operator
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** Enable cluster administrators to access and analyze pipeline logs independently of pod lifecycle using the Kibana web console.

**Personas:** Cluster administrator

**Main Jobs:** 1 core job across 1 workflow stage

---

## Quick Navigation

**I want to:**
- View pipeline logs after pods are deleted → Job 1 (Observe)
- Troubleshoot pipeline failures using Kibana → Job 1 (Observe)
- Access historical pipeline run logs → Job 1 (Observe)
- Set up log retention for pipelines → Job 1 (Observe)

---

# Table of Contents

## Observe System State

### Job 1: Access Pipeline Logs Independently of Pod Lifecycle
*When pipeline runs, task runs, and event listeners complete and their pods are deleted*

**Personas:** Cluster administrator

**Timing:** AFTER installing OpenShift Logging and Elasticsearch Operators - logs cannot be viewed in Kibana without these prerequisites

**Requires:** OpenShift Elasticsearch Operator installed, OpenShift Logging Operator installed, cluster administrator permissions

**Why:** Pipeline pods are ephemeral and consuming cluster resources; logs must remain accessible for troubleshooting and audit requirements after pod deletion

#### 1.1 Configure Kibana for Pipeline Log Access (The "Complete Setup")
**Goal:** Establish the log viewing infrastructure in Kibana to query pipeline logs.

- **Task:** Access Kibana web console
  → Lines 97-99: Web console access procedure
  Source: Procedure section, Step 1
  - Navigate via Observability menu
  - Grid icon → Observability → Logging

- **Task:** Create index pattern for pipeline logs
  → Lines 101-106: Index pattern creation
  Source: Procedure section, Step 3
  - Navigate to Management panel
  - Define index pattern using wildcard `*`
  - Configure @timestamp as time filter field
  - Two-step wizard workflow

- **Task:** Configure filters for Tekton pipeline containers
  → Lines 107-172: Filter configuration with DSL queries
  Source: Procedure section, Step 4
  - Add filter for Tekton-managed containers
  - Exclude `place-tools` container
  - Filter by pipelineRun labels for highlighting
  - Filter by pipeline labels for highlighting
  - Use Query DSL or graphical drop-down menus

- **Task:** Select relevant log fields for display
  → Lines 173-178: Field selection
  Source: Procedure section, Step 4
  - Select `kubernetes.flat_labels` field
  - Select `message` field
  - Ensure fields appear in Selected fields list

- **Validation:** View filtered pipeline log messages
  → Lines 179-182: Verification step
  Source: Procedure section, final step
  - Message field displays pipeline logs
  - Filtered by Tekton-specific labels

---

## Appendices

### A. Kibana Filter Query Reference

| Filter Purpose | Query Type | Example |
|----------------|------------|---------|
| Tekton-managed containers | DSL match query | `app_kubernetes_io/managed-by=tekton-pipelines` |
| Exclude place-tools | Graphical drop-down | Field negation filter |
| PipelineRun highlighting | DSL match query | `tekton_dev/pipelineRun=` |
| Pipeline highlighting | DSL match query | `tekton_dev/pipeline=` |

### B. Workflow Coverage Analysis

| Stage | Coverage | Jobs | Notes |
|-------|----------|------|-------|
| Get Started | ❌ | - | No onboarding content; assumes operators already installed |
| Configure | ⚠️ Limited | Job 1 (partial) | Kibana configuration only; Operator installation not covered |
| Observe | ✅ | Job 1 | Core log viewing and filtering |
| Troubleshoot | ❌ | - | No troubleshooting guidance for failed queries or missing logs |
| Reference | ⚠️ Limited | - | Filter query examples provided but no comprehensive reference |

### Gaps Identified

| Stage | Gap | Recommendation |
|-------|-----|----------------|
| Get Started | No installation guidance for OpenShift Logging/Elasticsearch Operators | Link to installation guide or add prerequisite setup section |
| Troubleshoot | No guidance for common Kibana query issues | Add troubleshooting section for missing logs, failed filters, or permission errors |
| Reference | Limited filter query reference | Expand reference with additional query patterns for different log types |
| Configure | No log retention policy configuration | Add guidance on configuring retention periods for pipeline logs |

---

## Navigation Guide

### By User Journey

**Cluster administrator troubleshooting pipeline failures:**
1. Job 1, Task 1: Access Kibana web console
2. Job 1, Task 2: Create index pattern
3. Job 1, Task 3: Configure filters for Tekton containers
4. Job 1, Task 4: Select log fields
5. Job 1, Validation: View filtered messages

**Cluster administrator setting up audit log access:**
1. Job 1, Task 1: Access Kibana web console
2. Job 1, Task 2: Create index pattern
3. Job 1, Task 3: Configure filters (focus on pipelineRun labels)
4. Job 1, Task 4: Select relevant fields for audit reports

---

## Document Statistics

**Workflow Coverage:**
- Get Started: Gap identified
- Configure: Limited coverage (1 job, partial)
- Observe: 1 job
- Troubleshoot: Gap identified
- Reference: Limited coverage

**Main Jobs:** 1
**User Stories/Paths:** 1 (Kibana configuration approach)
**Source Sections:** 1 procedure module
**Platform/Tool Variations:** 1 (Kibana web console; no CLI alternative documented)

# Using Manual Approval in OpenShift Pipelines - TOC Comparison

**Current Feature-Based vs. Proposed JTBD-Based Structure**

**Analysis Date:** 2026-06-11
**JTBD Records:** 12
**Main Jobs:** 4 (consolidated from 12 records)
**Coverage:** 593-line assembly covering concept, procedures, and reference material

---

## Current Structure (Feature-Based)

**Using manual approval in OpenShift Pipelines**

- **Enabling the manual approval gate controller** — Procedure for applying ManualApprovalGate CR
- **Specifying a manual approval task** — Procedure with multiple approval configuration examples
- **Approving a manual approval task** — Concept overview
  - Approving a manual approval task by using the web console — UI-based procedure
  - Approving a manual approval task by using the command line — CLI-based procedure
- **Behavior of ApprovalTask with groups and users** — Concept explaining group approval mechanics

**Total:** 1 assembly (6 included modules), organized by feature/action sequence.

---

## Proposed JTBD-Based Structure

### Quick Overview

- **Set Up Approval Infrastructure**
  - Job 1: Enable the Manual Approval Gate Controller
- **Plan Your Approval Strategy**
  - Job 2: Understand Group Approval Behavior
- **Configure Approval Gates**
  - Job 3: Specify Manual Approval Tasks in Pipelines
- **Execute Approvals**
  - Job 4: Approve or Reject Manual Approval Tasks

---

### Detailed Job Descriptions

#### Set Up Approval Infrastructure

**Job 1: Enable the Manual Approval Gate Controller**

*When I need to implement manual approval gates in my CI/CD pipelines, I want to enable the manual approval gate controller, so I can pause pipeline execution until authorized users provide approval.*

Prerequisites: OpenShift Pipelines Operator installed, Administrator permissions for openshift-pipelines namespace, Logged in with oc CLI

- **1.1. Apply ManualApprovalGate Custom Resource** `[procedure]`
  - Lines 86-136: Enabling the manual approval gate controller
  - Create CR manifest, apply via oc CLI, verify READY status
  - Context: Required one-time setup before approval tasks can be used

---

#### Plan Your Approval Strategy

**Job 2: Understand Group Approval Behavior**

*When I configure approval tasks with groups as a CI/CD engineer, I want to understand how the controller tracks individual group member approvals, so I can design effective approval policies with team-based authorization.*

Prerequisites: Understanding of approval task configuration, Groups created in OpenShift

- **2.1. Learn How Controller Tracks Group Member Approvals** `[concept]`
  - Lines 518-588: Behavior of ApprovalTask with groups and users
  - Group-level state updates, member-level tracking, mixed policies
  - Context: Read before configuring group-based approval tasks to understand mechanics

---

#### Configure Approval Gates

**Job 3: Specify Manual Approval Tasks in Pipelines**

*When I need to implement governance gates in my deployment pipeline, I want to specify manual approval tasks at critical stages, so I can ensure only authorized stakeholders can advance pipeline execution to production.*

Prerequisites: Manual approval gate controller enabled, Pipeline YAML specification, Groups and users created (for group approval)

- **3.1. Configure Basic Deployment Pipeline with Approval Gate** `[procedure]`
  - Lines 157-200: Specifying a manual approval task (basic example)
  - Add ApprovalTask to Pipeline, specify approvers, set threshold, configure dependencies
  - Context: Standard build->test->approval->deploy workflow

- **3.2. Configure Status Tracking for Approval Lifecycle** `[procedure]`
  - Lines 202-261: Specifying a manual approval task (with status fields)
  - Track state, approvals received, approver responses, timeout
  - Includes parameter reference table
  - Context: When visibility into approval progress is needed

- **3.3. Implement Multi-User Approval (Quorum-Based)** `[procedure]`
  - Lines 265-301: Multi-user approval example
  - Multiple individual users, quorum threshold (e.g., 2 of 3)
  - Context: When no single approver should authorize critical deployments

- **3.4. Implement Group-Based Approval (Team Authorization)** `[procedure]`
  - Lines 303-338: Group-based approval example
  - Specify groups as approvers (group:team-name), set threshold
  - Context: When teams own approval, reduces maintenance of approver lists

- **3.5. Implement Mixed User and Group Approval (Hybrid Policies)** `[procedure]`
  - Lines 340-377: Mixed user and group approval example
  - Combine individual users and groups for complex policies
  - Context: Patterns like "tech lead OR (QA + security)"

---

#### Execute Approvals

**Job 4: Approve or Reject Manual Approval Tasks**

*When my pipeline reaches an approval task as an authorized approver, I want to review and approve or reject the task, so I can control whether the pipeline proceeds to the next stage.*

Prerequisites: Pipeline running with approval task, User listed as approver, Access to web console or opc CLI

- **4.1. Approve or Reject via Web Console** `[procedure]`
  - Lines 406-432: Approving via web console
  - Navigate via notification/Approvals tab/PipelineRun details, select action, enter reason
  - Prerequisites: OpenShift Pipelines console plugin enabled
  - Context: For users who prefer UI-based workflow, no CLI expertise required

- **4.2. Approve or Reject via Command Line** `[procedure]`
  - Lines 445-510: Approving via CLI
  - Commands: opc approvaltask list/describe/approve/reject
  - Prerequisites: opc CLI utility installed
  - Context: For terminal-based workflow, automation, CI/CD integration

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | Action sequence (enable -> specify -> approve) | Workflow stage and user goal (setup -> plan -> configure -> execute) |
| **Top-level items** | 4 modules (enabling, specifying, approving concept, behavior concept) | 4 main jobs with 2-5 approaches each |
| **Approval configuration examples** | All under "Specifying a manual approval task" | Organized as 5 distinct approaches under Job 3 (basic, status, multi-user, group, mixed) |
| **Group approval behavior** | Separate concept at end | Elevated to Job 2 (Plan stage) to inform configuration decisions |
| **Approval execution** | Split into concept + 2 procedures (console, CLI) | Consolidated under Job 4 with 2 approaches (console, CLI) |
| **Navigation for finding approval patterns** | Read through "Specifying" section to find examples | Choose from 5 labeled approaches based on approval strategy |
| **Persona visibility** | Implicit (inferred from prerequisites) | Explicit (stated for each job) |
| **Workflow context** | Linear reading | Goal-directed: plan strategy -> configure -> execute |

---

## Consolidation Examples

### Example 1: Approval Execution (2 procedures + 1 concept → 1 unified job)

**Current (Fragmented):**
- "Approving a manual approval task" (concept overview, lines 386-399)
- "Approving a manual approval task by using the web console" (procedure, lines 406-432)
- "Approving a manual approval task by using the command line" (procedure, lines 445-510)

Users must read a concept module, then choose between two separate procedure modules.

**Proposed (Consolidated):**
- **Job 4: Approve or Reject Manual Approval Tasks**
  - 4.1. Approve or Reject via Web Console (lines 406-432)
  - 4.2. Approve or Reject via Command Line (lines 445-510)

**Benefit:** One job presents both approaches side-by-side with clear context for when to use each method. Concept content integrated into job description.

---

### Example 2: Approval Configuration Patterns (5 examples scattered → 5 labeled approaches)

**Current (Fragmented):**
- Basic deployment pipeline example (lines 157-200)
- Status tracking example (lines 202-261)
- Multi-user approval example (lines 265-301)
- Group-based approval example (lines 303-338)
- Mixed user and group approval example (lines 340-377)

All examples under one "Specifying a manual approval task" procedure. Users must read sequentially to find the pattern they need.

**Proposed (Consolidated):**
- **Job 3: Specify Manual Approval Tasks in Pipelines**
  - 3.1. Basic Deployment Pipeline
  - 3.2. Status Tracking
  - 3.3. Multi-User Approval (Quorum)
  - 3.4. Group-Based Approval (Teams)
  - 3.5. Mixed User and Group Approval

**Benefit:** Each approval pattern is a labeled approach with clear context statement. Users can jump directly to their approval strategy without reading all examples.

---

## Navigation Improvement

**Current:** Browse 4 top-level modules sequentially to find content
**Proposed:** Navigate 4 main jobs -> choose approach based on goal
**Reduction:** ~50% fewer decision points (4 jobs vs 4 modules + 5 examples to parse)

**Task-specific navigation improvements:**

| User Goal | Current Path | Proposed Path | Clicks/Sections |
|-----------|-------------|---------------|-----------------|
| Enable approval controller | Read "Enabling the manual approval gate controller" module | Job 1 -> 1.1 | Same (1 section) |
| Understand group approvals | Read "Behavior of ApprovalTask" at end | Job 2 (elevated to Plan stage) | 1 section, elevated priority |
| Configure team-based approval | Read "Specifying" module, find group example (~line 303) | Job 3 -> 3.4 (Group-Based Approval) | 1 click vs reading through examples |
| Approve via CLI | Read "Approving" concept, find CLI procedure | Job 4 -> 4.2 (Command Line) | 1 click vs 2 modules |

**Final job count: 4** (no adjustment needed from JTBD records).

---

## Workflow Coverage Comparison

| Stage | Current | Proposed | Gap Status |
|-------|---------|----------|------------|
| Plan | ⚠️ Scattered | ✅ Job 2 | Improved - group behavior elevated to planning stage |
| Configure | ✅ Enable + Specify | ✅ Jobs 1, 3 | Reorganized - approval patterns labeled and navigable |
| Execute | ✅ Approving modules | ✅ Job 4 | Consolidated - concept + procedures merged |
| Monitor | ⚠️ Limited | ⚠️ Limited | Partial - status tracking in Job 3.2, no dedicated monitoring job |
| Troubleshoot | ❌ Missing | ❌ Missing | Gap remains - no troubleshooting content |
| Reference | ⚠️ Parameter table only | ⚠️ Parameter table only | Partial - reference table in Job 3.2 |

### Coverage Summary

**Current structure gaps:** Dedicated monitoring job, troubleshooting procedures, comprehensive reference
**Proposed structure gaps:** Dedicated monitoring job, troubleshooting procedures, comprehensive reference
**Gaps addressed by restructure:** Planning stage (group behavior elevated from end to beginning)

### Recommendations for Gap Closure

| Gap | Recommendation | Priority |
|-----|----------------|----------|
| Monitor | Add job for monitoring approval task status across pipelines (oc get approvaltasks, dashboard views) | Medium |
| Troubleshoot | Add common issues: controller not ready, approval stuck, permission errors, group misconfiguration | High |
| Reference | Expand parameter reference, add ApprovalTask API spec, example library with more patterns | Medium |
| Upgrade | Document upgrade behavior for Tech Preview to GA transition | Low (future) |

---

## Success Metrics

**Navigation efficiency:**
- Find group approval configuration: 1 click (Job 3 -> 3.4) vs reading through all examples
- Understand group mechanics before configuring: Job 2 elevated to Plan stage vs buried at end
- Choose approval pattern: 5 labeled approaches vs 5 unlabeled examples

**Content discoverability:**
- Approval strategies visible at a glance (Jobs 3.1-3.5 labeled)
- Execution methods side-by-side (Jobs 4.1-4.2)
- Planning content elevated (Job 2 before configuration)

**Workflow alignment:**
- Setup -> Plan -> Configure -> Execute progression
- Prerequisites explicit for each job
- Personas stated for each job (Platform admin, CI/CD engineer, Release manager)

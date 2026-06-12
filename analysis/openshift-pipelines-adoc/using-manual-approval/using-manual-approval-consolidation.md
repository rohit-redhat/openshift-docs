# Using Manual Approval in OpenShift Pipelines — Consolidation Report

**Document:** using-manual-approval.adoc
**JTBD Records:** 12 records → 4 final main jobs (8 user stories consolidated under main jobs)

---

## Executive Summary

### What's Changing

The current structure organizes content by action sequence (enable -> specify -> approve) with approval configuration examples embedded within a single "Specifying" procedure. This approach requires users to read through multiple examples sequentially to find the approval pattern they need, and buries the conceptual understanding of group approval behavior at the end of the guide.

The proposed JTBD-based structure reorganizes content by workflow stage and user goal: setup -> plan -> configure -> execute. This elevates planning content (understanding group approval mechanics) before configuration, labels each approval configuration pattern as a distinct approach, and consolidates approval execution methods under a single job with clear context for UI vs CLI workflows.

### Key Improvements

- **Group approval planning elevated:** Concept explaining group behavior moved from end of guide to Job 2 (Plan stage), ensuring users understand mechanics before configuring group-based approvals.
- **Approval patterns labeled and navigable:** 5 approval configuration examples (basic, status tracking, multi-user, group-based, mixed) become distinct approaches under Job 3 with clear context statements.
- **Execution methods consolidated:** Approval concept + 2 separate procedures (console, CLI) consolidated under Job 4 with side-by-side approaches.
- **Persona visibility:** Platform administrator, CI/CD engineer, and Release manager personas explicitly stated for each job, clarifying who performs which tasks.
- **Workflow progression:** Natural flow from setup (enable controller) -> plan (understand groups) -> configure (specify tasks) -> execute (approve/reject).
- **Context-driven navigation:** Each approach includes "Context:" statement explaining when/why to use it, enabling goal-directed navigation instead of sequential reading.

---

## Current Structure (Feature-Based)

- **Using manual approval in OpenShift Pipelines** (Assembly)
  - Technology Preview notice — Feature status warning
  - Enabling the manual approval gate controller — Procedure for applying ManualApprovalGate CR
  - Specifying a manual approval task — Procedure with embedded examples
    - Basic deployment pipeline example
    - Status tracking example
    - Multi-user approval example
    - Group-based approval example
    - Mixed user and group approval example
    - Parameter reference table
  - Approving a manual approval task — Concept overview
    - Approving via web console — UI-based procedure
    - Approving via command line — CLI-based procedure
  - Behavior of ApprovalTask with groups and users — Concept explaining group approval mechanics

**Total:** 1 assembly, 6 included modules (2 concepts, 4 procedures), organized by action sequence.

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
  - Lines 86-136 (Enabling the manual approval gate controller): Create ManualApprovalGate CR manifest, apply using oc CLI, verify READY status is True
  - Context: Required one-time cluster setup before any approval tasks can be configured

---

#### Plan Your Approval Strategy

**Job 2: Understand Group Approval Behavior**

*When I configure approval tasks with groups as a CI/CD engineer, I want to understand how the controller tracks individual group member approvals, so I can design effective approval policies with team-based authorization.*

Prerequisites: Understanding of approval task configuration, Groups created in OpenShift

- **2.1. Learn How Controller Tracks Group Member Approvals** `[concept]`
  - Lines 518-588 (Behavior of ApprovalTask with groups and users): Group-level approval state updates based on member approvals, individual member tracking, mixed user and group policies, runtime ApprovalTask structure
  - Context: Read before configuring group-based approval tasks to understand how group state changes and member approvals are tracked

---

#### Configure Approval Gates

**Job 3: Specify Manual Approval Tasks in Pipelines**

*When I need to implement governance gates in my deployment pipeline, I want to specify manual approval tasks at critical stages, so I can ensure only authorized stakeholders can advance pipeline execution to production.*

Prerequisites: Manual approval gate controller enabled, Pipeline YAML specification, Groups and users created (for group approval)

- **3.1. Configure Basic Deployment Pipeline with Approval Gate** `[procedure]`
  - Lines 157-200 (Specifying a manual approval task - basic example): Add ApprovalTask to Pipeline definition, specify approvers list (users/groups), set numberOfApprovalsRequired, add description, configure runAfter dependencies
  - Context: Standard build->test->approval->deploy workflow

- **3.2. Configure Status Tracking for Approval Lifecycle** `[procedure]`
  - Lines 202-261 (Specifying a manual approval task - with status fields): Track approval state (pending/approved/rejected), monitor approvals received vs required, view approver responses, track start time and timeout
  - Includes parameter reference table (approvers, description, numberOfApprovalsRequired, timeout, state, approvalsReceived, approversResponse)
  - Context: When visibility into approval progress is needed during pipeline execution

- **3.3. Implement Multi-User Approval (Quorum-Based)** `[procedure]`
  - Lines 265-301 (Multi-user approval example): Configure multiple individual users as approvers with quorum threshold (e.g., 2 of 3 approvers)
  - Context: When no single approver should authorize critical deployments, implements quorum-based authorization

- **3.4. Implement Group-Based Approval (Team Authorization)** `[procedure]`
  - Lines 303-338 (Group-based approval example): Specify groups as approvers using group:team-name syntax, set approval threshold across groups
  - Context: When teams (not individuals) own approval responsibility, reduces maintenance of approver lists when team membership changes

- **3.5. Implement Mixed User and Group Approval (Hybrid Policies)** `[procedure]`
  - Lines 340-377 (Mixed user and group approval example): Combine individual users and groups in approvers list to support complex policies
  - Context: Patterns like "tech lead OR (QA + security)" requiring sign-off from specific roles and teams

---

#### Execute Approvals

**Job 4: Approve or Reject Manual Approval Tasks**

*When my pipeline reaches an approval task as an authorized approver, I want to review and approve or reject the task, so I can control whether the pipeline proceeds to the next stage.*

Prerequisites: Pipeline running with approval task, User listed as approver in task configuration, Access to web console or opc CLI

- **4.1. Approve or Reject via Web Console** `[procedure]`
  - Lines 406-432 (Approving via web console): Navigate to approval task (via notification, Approvals tab, or PipelineRun details), select Approve or Reject from kebab menu, enter reason message, submit decision
  - Prerequisites: OpenShift Pipelines console plugin enabled
  - Context: For users who prefer UI-based workflow, no CLI expertise required

- **4.2. Approve or Reject via Command Line** `[procedure]`
  - Lines 445-510 (Approving via CLI): List approval tasks (opc approvaltask list), describe task details (opc approvaltask describe), approve (opc approvaltask approve) or reject (opc approvaltask reject) with optional message parameter
  - Prerequisites: opc CLI utility installed (included with tkn package)
  - Context: For terminal-based workflow, automation, and CI/CD integration

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | Action sequence (enable -> specify -> approve) | Workflow stage and user goal (setup -> plan -> configure -> execute) |
| **Top-level items** | 4 top-level modules (enabling, specifying, approving, behavior) | 4 main jobs with 2-5 approaches each |
| **Approval patterns** | 5 examples embedded in "Specifying" procedure | 5 labeled approaches under Job 3 (3.1-3.5) |
| **Group approval concept** | Separate module at end of guide | Job 2 in Plan stage (before configuration) |
| **Approval execution** | Concept + 2 separate procedures | 1 job with 2 approaches (console, CLI) |
| **Navigation for patterns** | Sequential reading through examples | Direct navigation to labeled approach |
| **Persona visibility** | Implicit in prerequisites | Explicit for each job |
| **Context guidance** | Minimal (descriptions only) | Context statement for each approach |

### Job List Adjustments from Suggested Input

The suggested 12 records were consolidated to **4 main jobs** for the following reasons:

1. **Records 2-8 (7 user stories) nested under Jobs 1, 2, 3** → User stories representing different approaches to main jobs were properly nested rather than promoted to top level
2. **Records 10-11 (2 approval execution user stories) consolidated under Job 4** → UI and CLI approval methods are implementation approaches for the same job (approve/reject tasks), not separate jobs
3. **Record 9 (approving concept) absorbed into Job 4** → Concept content integrated into job description and user story context, not separate job

**No jobs were dissolved or eliminated.** All 12 records map to the 4 main jobs (4 main job records + 8 user story records nested appropriately).

---

## Consolidation Examples

### Example 1: Approval Execution (Concept + 2 procedures → 1 unified job)

**Current (Fragmented):**
- Section: "Approving a manual approval task" (lines 386-399) — Concept explaining approval behavior, rejection consequences, ability to change approval
- Section: "Approving a manual approval task by using the web console" (lines 406-432) — UI-based procedure with navigation paths
- Section: "Approving a manual approval task by using the command line" (lines 445-510) — CLI-based procedure with opc commands

Users must read a concept module, then choose between two separate procedure modules. Concept content is separate from execution instructions.

**Proposed (Consolidated):**
- **Job 4: Approve or Reject Manual Approval Tasks**
  - 4.1. Approve or Reject via Web Console (lines 406-432)
  - 4.2. Approve or Reject via Command Line (lines 445-510)

**Benefit:** One job with integrated concept content (in job description) and two side-by-side approaches with clear context for UI vs CLI workflows. Users choose their method immediately without reading separate concept module.

---

### Example 2: Approval Configuration Patterns (5 examples scattered → 5 labeled approaches)

**Current (Fragmented):**
- Lines 157-200: Basic deployment pipeline example
- Lines 202-261: Status tracking example with parameter table
- Lines 265-301: Multi-user approval example
- Lines 303-338: Group-based approval example
- Lines 340-377: Mixed user and group approval example

All examples under one "Specifying a manual approval task" procedure. Users must read through all examples sequentially to find the pattern matching their approval strategy.

**Proposed (Consolidated):**
- **Job 3: Specify Manual Approval Tasks in Pipelines**
  - 3.1. Basic Deployment Pipeline (lines 157-200)
  - 3.2. Status Tracking (lines 202-261)
  - 3.3. Multi-User Approval (lines 265-301)
  - 3.4. Group-Based Approval (lines 303-338)
  - 3.5. Mixed User and Group Approval (lines 340-377)

**Benefit:** Each approval pattern is a labeled approach with context statement explaining when to use it. Users can navigate directly to their approval strategy (quorum-based, team-based, hybrid) without reading all examples.

---

### Example 3: Group Approval Understanding (Concept elevated from end to planning stage)

**Current (Buried):**
- Section: "Behavior of ApprovalTask with groups and users" (lines 518-588) — Final section explaining how controller tracks group member approvals, group state changes, runtime structure

Concept appears after all configuration examples. Users who configure group-based approvals in Job 3 may not understand mechanics until reading end of guide.

**Proposed (Elevated):**
- **Job 2: Understand Group Approval Behavior** (Plan stage, before Job 3)
  - 2.1. Learn How Controller Tracks Group Member Approvals (lines 518-588)

**Benefit:** Planning content appears before configuration, ensuring users understand group approval mechanics before specifying group-based approval tasks. Follows natural workflow: plan -> configure.

---

## Content Gaps Identified

| Gap | JTBD Reference | Current Coverage | Impact |
|-----|---------------|-----------------|--------|
| Monitoring approval tasks across pipelines | Job 4 (Execute) | Only status tracking in configuration (Job 3.2) | **Medium** — Users need to monitor pending approvals across multiple pipeline runs, not just within one configuration |
| Troubleshooting controller not ready | Job 1 (Setup) | None — only verification step | **High** — Users may encounter READY=False status with no guidance on resolution |
| Troubleshooting approval task stuck | Job 4 (Execute) | None | **High** — Users may face approval tasks that don't respond, no guidance on resolution |
| Permission errors for approvers | Job 4 (Execute) | None | **Medium** — Users listed as approvers may lack permissions, no troubleshooting guidance |
| Group misconfiguration issues | Job 2, 3 (Plan, Configure) | None | **Medium** — Users may specify non-existent groups or groups without members |
| Comprehensive parameter reference | Job 3 (Configure) | Parameter table in lines 243-261 | **Medium** — Table covers main parameters, but no API spec or exhaustive reference |
| Approval task timeout behavior | Job 3 (Configure) | Mentioned (default 1 hour), no detail | **Low** — What happens at timeout? How to handle timeout failures? |
| Technology Preview to GA migration | All jobs | Tech Preview notice only | **Low** — Future: How to migrate when feature reaches GA? |

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 4 modules | 4 jobs | Same count, better labels |
| Sections to browse for group approval configuration | 2 (behavior concept + specifying procedure, find example) | 2 (Job 2 to understand, Job 3.4 to configure) | ~50% clearer - labeled approach vs buried example |
| Sections to browse for approving via CLI | 2 (approving concept + CLI procedure) | 1 (Job 4 -> 4.2) | 50% reduction |
| Understanding before configuring groups | Read to end of guide | Job 2 (before Job 3) | Elevated to planning stage |
| Choosing approval pattern | Read through 5 examples | Navigate to 1 of 5 labeled approaches | 80% faster - direct navigation |
| Context for when to use each approach | Minimal (example descriptions) | Explicit context statements | Qualitative improvement |

**Final job count: 4** (no reduction from suggested main jobs). The 12 JTBD records included 4 main jobs and 8 user stories, properly hierarchized.

---

## Document Statistics

**Workflow Coverage:**
- Setup: Job 1 (enable controller)
- Plan: Job 2 (understand group behavior)
- Configure: Job 3 (specify approval tasks with 5 patterns)
- Execute: Job 4 (approve/reject via console or CLI)
- Monitor: Partial (status tracking in Job 3.2, gap for cross-pipeline monitoring)
- Troubleshoot: Gap (no troubleshooting content)
- Reference: Partial (parameter table in Job 3.2, gap for comprehensive API reference)

**Main Jobs:** 4
**User Stories/Approaches:** 8 (2 under Job 1, 1 under Job 2, 5 under Job 3, 2 under Job 4)
**Source Sections:** 593 lines (reduced assembly)
**Approval Strategy Variations:** 5 (basic, status tracking, multi-user, group-based, mixed)
**Personas:** 3 (Platform administrator, CI/CD engineer, Release manager)

**Technology Preview Status:** This feature is not production-ready and lacks Red Hat SLA support. Users should expect potential changes before GA release.

# Using Manual Approval in OpenShift Pipelines
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** Enable controlled deployments through manual approval gates that pause pipeline execution until authorized stakeholders provide approval.

**Personas:** Platform administrator, CI/CD engineer, Release manager

**Main Jobs:** 4 core jobs across 4 workflow stages (Plan, Configure, Execute, Monitor)

**Scope:** Technology Preview feature for OpenShift Pipelines manual approval gates

---

## Quick Navigation

**I want to:**
- Set up manual approvals in my cluster → Job 1 (Configure)
- Add approval gates to my pipeline → Job 2 (Configure)
- Understand how group approvals work → Job 3 (Plan)
- Approve or reject a pending task → Job 4 (Execute)

---

# Table of Contents

## Choose Your Approach

### Job 1: Enable the Manual Approval Gate Controller
*When implementing manual approval gates in CI/CD pipelines*

**Personas:** Platform administrator

**Prerequisites:** OpenShift Pipelines Operator installed, Administrator permissions for openshift-pipelines namespace, Logged in with oc CLI

**Timing:** BEFORE Job 2 (Specify Manual Approval Tasks) - controller must be running before approval tasks can be configured

#### 1.1 Apply ManualApprovalGate Custom Resource `[procedure]`

→ Lines 86-136: Enabling the manual approval gate controller
  Source: Root assembly, Procedure module

- Create ManualApprovalGate CR manifest
- Apply CR using oc CLI
- Verify controller READY status is True
- Context: CLI-only approach for enabling approval functionality

---

## Plan Your Approval Strategy

### Job 2: Understand Group Approval Behavior
*When configuring approval tasks with groups*

**Personas:** CI/CD engineer

**Prerequisites:** Understanding of approval task configuration, Groups created in OpenShift

#### 2.1 Learn How Controller Tracks Group Member Approvals `[concept]`

→ Lines 518-588: Behavior of ApprovalTask with groups and users
  Source: Root assembly, Concept module

- Group-level approval state updates based on member approvals
- Individual member actions tracked in users list
- Mixed user and group approval policies
- Context: Understanding before configuring group-based approvals

**Note:** Includes runtime ApprovalTask structure example (for inspection only, not for manual application)

---

## Set Up Approval Gates

### Job 3: Specify Manual Approval Tasks in Pipelines
*When implementing governance gates in deployment pipelines*

**Personas:** CI/CD engineer

**Prerequisites:** Manual approval gate controller enabled, Pipeline YAML specification, Groups and users created for group approval

**Why:** Prevents unauthorized deployments through controlled authorization gates

#### 3.1 Configure Basic Deployment Pipeline with Approval Gate `[procedure]`

→ Lines 157-200: Specifying a manual approval task (basic example)
  Source: Root assembly, Procedure module

- Add ApprovalTask to Pipeline definition
- Specify approvers list (users/groups)
- Set numberOfApprovalsRequired threshold
- Add description for approval context
- Configure runAfter dependencies (build->test->approval->deploy)
- Context: Standard approval gate in build-test-deploy workflow

#### 3.2 Configure Status Tracking for Approval Lifecycle `[procedure]`

→ Lines 202-261: Specifying a manual approval task (with status)
  Source: Root assembly, Procedure module (includes parameter reference table)

- Track approval state (pending/approved/rejected)
- Monitor approvals received vs required
- View approver responses
- Track start time and timeout
- Context: When visibility into approval progress is needed

#### 3.3 Implement Multi-User Approval (Quorum-Based) `[procedure]`

→ Lines 265-301: Multi-user approval example
  Source: Root assembly, Procedure module

- Configure multiple individual users as approvers
- Set quorum threshold (e.g., 2 of 3 approvers)
- Context: When no single approver should authorize critical deployments

#### 3.4 Implement Group-Based Approval (Team Authorization) `[procedure]`

→ Lines 303-338: Group-based approval example
  Source: Root assembly, Procedure module

- Specify groups as approvers (group:team-name syntax)
- Set approval threshold across groups
- Context: When teams (not individuals) own approval responsibility, reduces maintenance of approver lists

#### 3.5 Implement Mixed User and Group Approval (Hybrid Policies) `[procedure]`

→ Lines 340-377: Mixed user and group approval example
  Source: Root assembly, Procedure module

- Combine individual users and groups in approvers list
- Support patterns like "tech lead OR (QA + security)"
- Context: When complex approval policies require sign-off from specific roles and teams

---

## Execute Approvals

### Job 4: Approve or Reject Manual Approval Tasks
*When pipeline reaches an approval task*

**Personas:** Release manager

**Prerequisites:** Pipeline running with approval task, User listed as approver, Access to web console or opc CLI

#### 4.1 Approve or Reject via Web Console `[procedure]`

→ Lines 406-432: Approving via web console
  Source: Root assembly, Procedure module

**Prerequisites:** OpenShift Pipelines console plugin enabled

- Navigate to approval task (notification, Approvals tab, or PipelineRun details)
- Select Approve or Reject from kebab menu
- Enter reason message
- Submit decision
- Context: For users who prefer UI-based workflow, no CLI expertise required

**Additional resources:**
- Enabling the OpenShift Pipelines console plugin

#### 4.2 Approve or Reject via Command Line `[procedure]`

→ Lines 445-510: Approving via CLI
  Source: Root assembly, Procedure module

**Prerequisites:** opc CLI utility installed (same package as tkn)

- List approval tasks: `opc approvaltask list`
- Describe task details: `opc approvaltask describe <name>`
- Approve task: `opc approvaltask approve <name> -m <message>`
- Reject task: `opc approvaltask reject <name> -m <message>`
- Context: For terminal-based workflow, automation, and CI/CD integration

**Additional resources:**
- Installing tkn (includes opc utility)

---

## Workflow Coverage

| Stage | Coverage | Jobs | Notes |
|-------|----------|------|-------|
| Plan | ✅ | Job 2 | Understanding group approval behavior |
| Configure | ✅ | Jobs 1, 3 | Enable controller, specify approval tasks |
| Execute | ✅ | Job 4 | Approve/reject tasks |
| Monitor | ⚠️ Limited | Job 3.2 (partial) | Status tracking covered in configuration, no dedicated monitoring job |
| Troubleshoot | ❌ | - | No troubleshooting content |
| Reference | ⚠️ Limited | Job 3.2 (partial) | Parameter reference table in configuration section |

### Gaps Identified

| Stage | Gap | Recommendation |
|-------|-----|----------------|
| Monitor | No dedicated monitoring/observability | Add job for monitoring approval task progress across pipelines |
| Troubleshoot | No troubleshooting procedures | Add common issues: controller not ready, approval task stuck, permission errors |
| Reference | Limited reference material | Add comprehensive parameter reference, API specs, examples library |

---

## Navigation Guide

### By User Journey

**Platform Administrator deploying manual approvals:**
1. Job 1: Enable the Manual Approval Gate Controller
2. Job 2: Understand Group Approval Behavior (if using groups)
3. Job 3: Specify Manual Approval Tasks in Pipelines (collaborate with CI/CD engineer)

**CI/CD Engineer adding approval gates to pipelines:**
1. Job 2: Understand Group Approval Behavior (plan approval strategy)
2. Job 3: Specify Manual Approval Tasks in Pipelines (choose approach: user/group/mixed)

**Release Manager approving deployments:**
1. Job 4: Approve or Reject Manual Approval Tasks (via console or CLI)

---

## Document Statistics

**Workflow Coverage:**
- Plan: 1 job (understand group behavior)
- Configure: 2 jobs (enable controller, specify tasks)
- Execute: 1 job (approve/reject)
- Monitor: Partial (status tracking in configuration)
- Troubleshoot: Gap identified
- Reference: Partial (parameter table)

**Main Jobs:** 4
**User Stories/Procedures:** 8
**Source Sections:** 593 lines (reduced assembly)
**Approval Strategy Variations:** 4 (individual users, groups, mixed, status tracking)

**Technology Preview:** This feature is not production-ready and lacks Red Hat SLA support.

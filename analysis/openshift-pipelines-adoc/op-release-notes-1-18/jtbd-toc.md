# OpenShift Pipelines 1.18 Release Notes
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** Help administrators and developers understand version 1.18 changes, assess upgrade impact, and leverage new capabilities.

**Personas:** Platform administrator, Cluster administrator, Pipeline developer

**Main Jobs:** 6 core jobs across Planning, What's New, and Reference stages

---

## Quick Navigation

**I want to:**
- Check if my cluster supports Pipelines 1.18 → Job 1 (Plan)
- See what's new in this release → Job 2 (What's New)
- Identify breaking changes before upgrading → Job 3 (What's New)
- Review known issues → Job 4 (What's New)
- Understand fixed bugs → Job 5 (What's New)
- Evaluate the 1.18.1 patch → Job 6 (What's New)

---

# Table of Contents

## Plan Your Installation or Upgrade

### Job 1: Verify Version Compatibility
*When evaluating OpenShift Pipelines for my cluster*

**Personas:** Platform administrator, Cluster administrator

**Why:** Incompatible versions can cause installation failures or runtime issues

→ Lines 89-124: Compatibility and support matrix
  Source: Module op-tkn-pipelines-compatibility-support-matrix.adoc

- Component versions for Pipelines 1.22, 1.21, 1.20
- OpenShift version support (4.14-4.21)
- Technology Preview vs GA status indicators
- Console plugin version alignment

---

## What's New

### Job 2: Understand What's Included in OpenShift Pipelines 1.18
*When planning an upgrade or new installation*

**Personas:** Platform administrator, Pipeline developer

→ Lines 134-138: Release overview
  Source: op-release-notes-1-18.adoc

#### 2.1. Pipelines Component Enhancements `[concept]`

→ Lines 144-173: Pipelines new features
  Source: op-release-notes-1-18.adoc, Section "Pipelines"

- **Improved log messages** - Enhanced readability when empty variables are present
- **Configurable resolution timeouts** - Flexibility for pipeline resolvers
  - `default-maximum-resolution-timeout`: Global timeout (default 1m)
  - `fetch-timeout`: Bundle resolver timeout

#### 2.2. Operator Enhancements `[concept]`

→ Lines 176-258: Operator new features
  Source: op-release-notes-1-18.adoc, Section "Operator"

- **Community tasks** - 8 pre-built tasks installed by default
  - argocd-task-sync-and-wait, git-cli, helm-upgrade-from-repo, helm-upgrade-from-source
  - jib-maven, kubeconfig-creator, pull-request, trigger-jenkins-job
  
- **Container deployment via TektonConfig CR** `[procedure]`
  - Deploy custom containers (example: kube-rbac-proxy)
  - Lines 192-218: Configuration example
  
- **StatefulSet ordinals for high availability** `[concept]` (Technology Preview)
  - Alternative to leader election mechanism
  - Balanced workload distribution vs quick failover
  - Lines 219-258: Configuration and comparison

#### 2.3. Triggers Enhancements `[concept]`

→ Lines 260-284: Triggers new features
  Source: op-release-notes-1-18.adoc, Section "Triggers"

- **ImagePullSecrets support** - EventListener can pull from private registries

#### 2.4. CLI Updates `[reference]`

→ Lines 285-293: CLI new features
  Source: op-release-notes-1-18.adoc, Section "CLI"

- Pipelines as Code version 0.33.0
- CLI version 0.40.0
- Results version 0.14.0
- Manual Approval Gate version 0.5.0

#### 2.5. Pipelines as Code Enhancements `[concept]`

→ Lines 294-428: Pipelines as Code new features
  Source: op-release-notes-1-18.adoc, Section "Pipelines as Code"

**Triggering improvements:**
- **Path-based triggering** `[procedure]` (Lines 294-314)
  - `on-path-change` and `on-path-change-ignore` annotations
  - Simplified alternative to CEL expressions
  
- **Comment-based triggering** `[procedure]` (Lines 315-332)
  - `on-comment` annotation for GitHub pushed commits
  
- **Label-based triggering** `[concept]` (Lines 425-428)
  - `on-label` annotation for PR labels
  - Supported: GitHub, GitLab, Gitea (not Bitbucket)

**Lifecycle management:**
- **Auto-cancel on PR close/merge** (Technology Preview) (Lines 374-404)
  - `cancel-in-progress: true` annotation
  
- **Auto-cancel on new commits** (Lines 406-422)
  - Older PipelineRuns canceled when new commits trigger runs

**Configuration improvements:**
- **Pattern testing** `[procedure]` (Lines 334-356)
  - `tkn pac info globbing` command for validating patterns
  
- **Comma support in annotations** `[reference]` (Lines 357-373)
  - HTML entity `&#44;` for branch names with commas

**Fixed:**
- `.pathChanged()` function working with Bitbucket Data Center

#### 2.6. Tekton Results Enhancements `[concept]`

→ Lines 429-439: Tekton Results new features
  Source: op-release-notes-1-18.adoc, Section "Tekton Results"

- **General Availability status** - Production-ready with SLA support
- **Default installation** - Configured automatically via TektonConfig CR
- **Proxy environment variable support** - For console plugin authorization
- **Enhanced logging** - LokiStack logs include container names

#### 2.7. Tekton Cache `[concept]` (Technology Preview)

→ Lines 440-465: Tekton Cache new features
  Source: op-release-notes-1-18.adoc, Section "Tekton Cache"

- **cache-upload and cache-fetch step actions**
  - Preserve build dependencies
  - Storage: S3 bucket, GCS bucket, or OCI repository
  - Installed by default in openshift-pipelines namespace

---

### Job 3: Identify Breaking Changes
*When planning an upgrade to Pipelines 1.18*

**Personas:** Platform administrator, Cluster administrator

**Timing:** BEFORE upgrading - migration planning required

→ Lines 466-472: Breaking changes
  Source: op-release-notes-1-18.adoc

#### 3.1. Tekton Results Log Forwarding Removed `[concept]`

- **What changed:** Log forwarding to PV, S3, or GCS buckets no longer supported
- **Impact:** Must migrate to alternative logging solution (e.g., LokiStack)
- **Action required:** Plan logging migration before upgrading

#### 3.2. Versioned Tasks Cleanup `[reference]`

- **What changed:** Only latest two minor versions of tasks retained
- **Versions kept in 1.18:** `*-1-17-0` and `*-1-18-0`
- **Impact:** Older versioned tasks removed from openshift-pipelines namespace
- **Action required:** Update task references in pipeline definitions

---

### Job 4: Review Known Issues
*When deploying or operating Pipelines 1.18*

**Personas:** Platform administrator, Cluster administrator

→ Lines 473-477: Known issues
  Source: op-release-notes-1-18.adoc

#### 4.1. TektonConfig Result Section Changes `[procedure]`

**Issue:** Parameter changes in `result:` section of TektonConfig CR don't apply automatically

**Workaround:** Manually restart Results API server deployment/pod in openshift-pipelines namespace

---

### Job 5: Understand Fixed Issues
*When evaluating the stability of Pipelines 1.18*

**Personas:** Platform administrator, Pipeline developer

→ Lines 478-553: Fixed issues
  Source: op-release-notes-1-18.adoc

#### 5.1. Controller Stability Fixes `[reference]`

- **Matrix parameters crash** - Controller no longer crashes with mixed regular and matrix parameters
- **Injected sidecars** - Fixed Kubernetes version checking issue
- **Resource limits** - Memory and ephemeral storage requests no longer exceed limits
- **Result ordering** - Duplicate keys removed while preserving order

#### 5.2. Web Console Fixes `[reference]`

- **Resolver-based rerun** - Fixed "Invalid PipelineRun configuration" error
- **Output tab** - Shows results instead of error when PipelineRun fails

#### 5.3. Task and Step Action Fixes `[reference]`

- **buildah task** - Fixed failure when CONTEXT and DOCKERFILE in different directories
- **Step action parameters** - Fixed using parameters as default values
- **Symlink handling** - PipelineRuns no longer fail with invalid symlinks

#### 5.4. Pipelines as Code Fixes `[reference]`

**GitLab:**
- Fixed status updates for relative path instances
- Fixed check name display for multiple simultaneous runs
- Fixed PR status reporting for forked repositories

**GitHub:**
- Fixed multiline comment handling with `{{ trigger_comment }}`
- Fixed `/test branch:<branch>` command parsing
- Fixed unauthorized user triggering with GitOps commands
- Fixed pending check creation without matching PipelineRun

**Bitbucket Data Center:**
- Fixed `.pathChanged()` function
- Fixed `body.changes` field access in push events
- Fixed `on-cel-expression` annotation on push events

**General PAC:**
- Fixed `generateName` field matching for incoming webhooks
- Fixed empty `[]` value handling in annotations
- Fixed Repository CR creation without valid URL

---

### Job 6: Evaluate the 1.18.1 Patch
*When assessing urgency of upgrading from 1.18.0*

**Personas:** Platform administrator

→ Lines 554-576: Release notes for 1.18.1
  Source: op-release-notes-1-18.adoc

#### 6.1. Patch Release Fixed Issues `[reference]`

**Critical fixes:**
- **TektonConfig propagation** - Configuration options now correctly propagate to TektonResult CR
- **PAC controller crash** - Fixed "index out of range" error
- **cancel-in-progress behavior** - Fixed unintended cancellation without annotation
- **Web console display** - Fixed duplicate TaskRun objects and incorrect status

**Other fixes:**
- **generateName with cancel-in-progress** - PAC now cancels correctly
- **Operator bundle name** - Displays correct name (openshift-pipelines-operator-rh)
- **Label-based triggering** - Fixed unintentional triggering on label addition

---

## Appendices

### A. Technology Preview vs GA Features

| Feature | Status | Section |
|---------|--------|---------|
| StatefulSet ordinals for HA | Technology Preview | Job 2.2 |
| Cancellation-in-progress in PAC | Technology Preview | Job 2.5 |
| Tekton Cache | Technology Preview | Job 2.7 |
| Tekton Results | General Availability | Job 2.6 |

### B. Quick Reference - Component Versions

| Component | Version in 1.18 |
|-----------|-----------------|
| Pipelines as Code | 0.33.0 |
| CLI | 0.40.0 |
| Results | 0.14.0 |
| Manual Approval Gate | 0.5.0 |

---

## Navigation Guide

### By User Journey

**Platform administrator upgrading from 1.17:**
1. Job 1: Verify OpenShift version compatibility
2. Job 3: Identify breaking changes (log forwarding, versioned tasks)
3. Job 4: Review known issues (TektonConfig parameter changes)
4. Job 2: Understand new features (Tekton Results GA, community tasks)
5. Job 5: Review fixed issues

**Pipeline developer evaluating new capabilities:**
1. Job 2.1: Pipelines enhancements (logs, timeouts)
2. Job 2.2: Community tasks availability
3. Job 2.5: Pipelines as Code improvements (path-based, comment-based triggers)
4. Job 2.7: Tekton Cache for build optimization
5. Job 5: Review PAC-related fixes

**Cluster administrator planning production deployment:**
1. Job 1: Verify compatibility matrix
2. Job 2.6: Tekton Results GA status
3. Job 3: Breaking changes impact assessment
4. Job 4: Known issues and workarounds
5. Job 6: Evaluate 1.18.1 patch necessity

---

## Document Statistics

**Workflow Coverage:**
- Plan: 1 job
- What's New: 5 jobs
- Configure: Gap identified
- Deploy: Gap identified
- Monitor: Gap identified
- Troubleshoot: Partially covered (known issues)
- Reference: Embedded throughout

**Main Jobs:** 6
**User Stories/Approaches:** 21
**Source Sections:** 10
**Component Categories:** 7 (Pipelines, Operator, Triggers, CLI, PAC, Results, Cache)

**Note:** This is a release notes document, so Configure/Deploy/Monitor jobs are not expected. The focus is on informing users of changes, not providing setup procedures.

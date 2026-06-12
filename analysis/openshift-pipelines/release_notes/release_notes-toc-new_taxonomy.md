# OpenShift Pipelines 1.22 Release Notes
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** Help users understand what's new, plan upgrades, and evaluate features in OpenShift Pipelines 1.22

**Personas:**
- Platform administrator
- Pipeline developer
- Operator/SRE
- Security/Compliance officer

**Main Jobs:** 10 core jobs across 4 workflow stages

---

## Quick Navigation

**I want to:**
- Verify my cluster version is supported → Job 1 (Planning for Upgrade)
- Evaluate new features → Job 2 (Evaluating New Capabilities)
- Explore Technology Preview capabilities → Job 3 (Evaluating New Capabilities)
- Understand breaking changes → Job 4 (Planning for Upgrade)
- Review known issues and workarounds → Job 5 (Understanding Risks)
- See what bugs were fixed → Job 6 (Evaluating New Capabilities)
- Identify deprecated features → Job 7 (Preparing for Future Releases)
- Prepare for removed features → Job 8 (Planning for Upgrade)

---

# Table of Contents

## Planning for Upgrade

### Job 1: Verify Cluster Compatibility
*When planning to upgrade OpenShift Pipelines*

**Personas:** Platform administrator
**Why:** Avoid compatibility issues and ensure successful deployment

#### 1.1 Check Cluster Version Support
**Goal:** Confirm your OpenShift cluster version is supported by Pipelines 1.22

- **Task:** Review OpenShift version support matrix
  → Lines 109: OpenShift version compatibility information
  Source: Compatibility and support matrix

#### 1.2 Identify Technology Preview Components
**Goal:** Understand which components are production-ready vs experimental

- **Task:** Review GA vs Technology Preview status for each component
  → Lines 93-115: Component support status table
  Source: Compatibility and support matrix
  - Distinguish between supported and Technology Preview features
  - Assess organizational risk tolerance for Technology Preview usage

#### 1.3 Plan Multi-Cluster Rollout Strategy
**Goal:** Coordinate upgrades across clusters running different versions

*For Platform administrators managing multiple clusters:*

- **Task:** Identify eligible clusters for upgrade
  → Lines 109: OpenShift version support range
  Source: Compatibility and support matrix
- **Task:** Align Pipelines upgrades with cluster lifecycle schedules

---

### Job 4: Identify Breaking Changes
*When planning an upgrade*

**Personas:** Platform administrator
**Timing:** BEFORE upgrading to Pipelines 1.22 - prevents pipeline failures and downtime
**Why:** Prepare migration steps and avoid disruption to existing pipelines

#### 4.1 Review Console Plugin Changes
**Goal:** Ensure Pipelines UI remains accessible after upgrade

- **Task:** Verify console plugin enablement requirements
  → Lines 363-368: Console plugin configuration requirements
  Source: Breaking changes - User interface
  - Enable console plugin explicitly to maintain UI navigation
  - Prevent user confusion from missing UI elements

---

### Job 8: Prepare for Removed Features
*When upgrading from previous releases*

**Personas:** Platform administrator
**Timing:** BEFORE upgrading - configuration changes cannot be deferred
**Requires:** Audit of existing configurations for removed features

#### 8.1 Migrate Affinity Assistant Configuration
**Goal:** Update TektonConfig to use new feature flag

- **Task:** Replace disable-affinity-assistant with coschedule feature flag
  → Lines 610-613: Migration from disable-affinity-assistant field
  Source: Removed features
  - Update TektonConfig CR before upgrade
  - Maintain affinity assistant control after upgrade

#### 8.2 Plan Tekton Hub Catalog Migration
**Goal:** Maintain task catalog functionality after public hub removal

*For teams using hub.tekton.dev:*

- **Task:** Deploy self-hosted Tekton Hub instances
  → Lines 615-618: Public Tekton Hub catalog removal notice
  Source: Removed features
  - Evaluate alternative task catalog solutions
  - Plan Hub instance deployment strategy
  - Support developers' catalog requirements

---

## Evaluating New Capabilities

### Job 2: Evaluate New Pipelines Features and Enhancements
*When planning to adopt a new Pipelines release*

**Personas:** Pipeline developer, Operator/SRE, Security/Compliance officer
**Goal:** Identify improvements that benefit CI/CD workflows

#### 2.1 Security Enhancements

##### User Namespace Isolation (Pipelines)
*For Pipeline developers on OCP 4.20+:*

- **Task:** Configure hostUsers in podTemplate
  → Lines 148-151: User namespace support without CRI-O annotations
  Source: New features and enhancements - Pipelines
  - Enable Kubernetes-native security
  - Migrate from buildah-ns task
  - Improve pipeline security through namespace isolation

##### HTTP Resolver Content Verification (Pipelines)
*For Pipeline developers fetching content from HTTP sources:*

- **Task:** Verify content integrity using hash parameters
  → Lines 153-156: HTTP resolver hash verification
  Source: New features and enhancements - Pipelines
  - Prevent execution of tampered content
  - Match security level of git and bundle resolvers
  - Prevent supply chain attacks

##### Webhook Signature Validation (Pipelines as Code)
*For Security/Compliance officers using Forgejo or Gitea:*

- **Task:** Enforce webhook signature validation
  → Lines 281-284: Webhook signature enforcement for Forgejo/Gitea
  Source: New features and enhancements - Pipelines as Code
  - Prevent spoofed webhook requests
  - Ensure only trusted sources trigger pipelines

#### 2.2 Performance and Reliability Enhancements

##### Resolver Caching (Pipelines)
*For Pipeline developers with frequent remote resource fetching:*

- **Task:** Enable resolver caching
  → Lines 158-167: Resolver caching feature
  Source: New features and enhancements - Pipelines
  - Prevent pipeline failures from rate limiting
  - Reduce API calls to remote resolvers
  - Configure caching mode appropriate for security requirements

##### Changed Files Caching (Pipelines as Code)
*For Pipeline developers using file-based trigger filtering:*

- **Task:** Leverage per-event file caching
  → Lines 210-213: Changed files caching for path filtering
  Source: New features and enhancements - Pipelines as Code
  - Reduce VCS API calls
  - Prevent API rate limit errors
  - Improve pipeline trigger performance

#### 2.3 Pipeline Logic and Flexibility Enhancements

##### Array Values in When Expressions (Pipelines)
*For Pipeline developers building complex conditional logic:*

- **Task:** Use array values in when expressions
  → Lines 169-172: Array value support in when expressions
  Source: New features and enhancements - Pipelines
  - Implement flexible conditional execution patterns
  - Simplify complex pipeline logic
  - Reduce pipeline code duplication

##### CEL Expressions for Templating (Pipelines as Code)
*For Pipeline developers creating dynamic templates:*

- **Task:** Use CEL expressions for complex logic
  → Lines 287-297: CEL expression support in templates
  Source: New features and enhancements - Pipelines as Code
  - Implement conditional behavior beyond variable substitution
  - Handle string manipulation in templates
  - Reduce pipeline code duplication

#### 2.4 Operational Improvements

##### Automatic ServiceMonitor Creation (Operator)
*For Operators/SREs integrating with OpenShift monitoring:*

- **Task:** Leverage automatic ServiceMonitor creation
  → Lines 202-205: Automatic ServiceMonitor resource creation
  Source: New features and enhancements - Operator
  - Simplify monitoring setup
  - Collect metrics without manual configuration
  - Enable proactive pipeline health monitoring

##### Update Comment Strategy (Pipelines as Code)
*For Pipeline developers managing pull requests:*

- **Task:** Use update comment strategy
  → Lines 216-219: Update comment strategy feature
  Source: New features and enhancements - Pipelines as Code
  - Reduce comment noise in pull requests
  - Improve repository readability
  - Configure comment strategy in Repository CR

##### Skip CI Tags (Pipelines as Code)
*For Pipeline developers managing work-in-progress commits:*

- **Task:** Skip pipeline execution using commit message tags
  → Lines 221-240: Skip CI tag support
  Source: New features and enhancements - Pipelines as Code
  - Avoid unnecessary CI runs for incomplete work
  - Save compute resources
  - Improve commit workflow flexibility
  - **Note:** GitLab behavior considerations included

##### Glob Patterns for GitHub App Tokens (Pipelines as Code)
*For Platform administrators managing many repositories:*

- **Task:** Use glob patterns for GitHub App token scoping
  → Lines 243-278: Glob pattern support for GitHub App tokens
  Source: New features and enhancements - Pipelines as Code
  - Grant access to multiple repositories efficiently
  - Simplify token scoping for private Git submodules
  - Reduce configuration overhead for multi-repository setups

#### 2.5 User Experience Improvements

##### ANSI Color Support in Logs (User Interface)
*For Pipeline developers reviewing pipeline logs:*

- **Task:** View logs with ANSI color support
  → Lines 307-310: ANSI color support in console logs
  Source: New features and enhancements - User interface
  - Read structured output more easily
  - Identify errors quickly
  - Improve log readability

---

### Job 3: Explore Technology Preview Features
*When assessing readiness for distributed pipeline architectures*

**Personas:** Platform administrator
**Why:** Understand benefits and risks before planning production adoption

**Note:** Technology Preview features are NOT supported for production use

#### 3.1 Multi-Cluster Hub and Spoke Architecture
**Goal:** Centralize pipeline management across clusters

*For Platform administrators architecting multi-cluster deployments:*

- **Task:** Configure Hub and Spoke roles in TektonConfig
  → Lines 320-337: Hub and Spoke role configuration
  Source: Technology Preview features - Multi-cluster
  - Centralize pipeline visibility and control
  - Scale pipeline execution across multiple clusters
  - Configure Results for centralized logging
  - Plan network connectivity between clusters

#### 3.2 Results Auto-Scaling in Hub Mode
**Goal:** Optimize resource usage based on multi-cluster role

*For Platform administrators using Hub mode:*

- **Task:** Leverage automatic Results component scaling
  → Lines 339-342: Results auto-scaling in Hub mode
  Source: Technology Preview features - Multi-cluster
  - Reduce resource consumption on Hub cluster
  - Maintain proper Results functionality on Spoke clusters

#### 3.3 Tekton Scheduler Integration with Kueue
**Goal:** Implement advanced queuing and resource management policies

*For Platform administrators managing pipeline resource allocation:*

- **Task:** Integrate Tekton Scheduler with Kueue
  → Lines 344-351: Tekton Scheduler and Kueue integration
  Source: Technology Preview features - Multi-cluster
  - Implement fair-share resource allocation
  - Prevent pipeline resource starvation
  - Support multi-tenant pipeline environments
  - **Requires:** Kueue installed (upstream component)

---

### Job 6: Review Fixed Issues
*When evaluating an upgrade*

**Personas:** Platform administrator, Pipeline developer, Operator/SRE, Security/Compliance officer
**Goal:** Determine if the release resolves problems affecting pipelines

#### 6.1 Critical Fixes - Pipelines

##### Affinity Assistant Service Account Inheritance
*For Pipeline developers using workspaces in restricted environments:*

- **Fix:** Service account properly inherited by Affinity Assistant
  → Lines 406-409: Affinity Assistant SCC permission fix
  Source: Fixed issues - Pipelines
  - Enable workspace usage in security-restricted environments
  - Eliminate need for manual SCC configuration
  - Prevent PipelineRun blockages

##### TaskRun Error Messages
*For Pipeline developers troubleshooting failed TaskRuns:*

- **Fix:** Clear error messages for pod configuration issues
  → Lines 411-414: Improved TaskRun error messages
  Source: Fixed issues - Pipelines
  - Reduce time to diagnose failures
  - Avoid waiting for timeout periods
  - Improve debugging experience

##### Reconciliation Performance
*For Platform administrators managing cluster stability:*

- **Fix:** Controller reconciliation for pipelines without timeouts
  → Lines 416-419: Reconciliation performance fix
  Source: Fixed issues - Pipelines
  - Improve controller performance
  - Reduce cluster resource consumption
  - Enhance scalability

##### Parameter Default Resolution
*For Pipeline developers using parameter references:*

- **Fix:** Parameter defaults can reference other parameters
  → Lines 421-424: Parameter default resolution fix
  Source: Fixed issues - Pipelines
  - Enable parameter reference chains
  - Simplify pipeline configuration
  - Reduce code duplication

#### 6.2 Critical Fixes - Operator

##### Webhook Cleanup on Uninstall
*For Platform administrators managing operator lifecycle:*

- **Fix:** Webhooks cleaned up automatically on uninstall
  → Lines 459-462: Webhook cleanup fix
  Source: Fixed issues - Operator
  - Ensure complete cleanup on uninstall
  - Prevent resource leaks

##### Prometheus Metrics in Custom Namespace
*For Platform administrators using custom namespaces:*

- **Fix:** Metrics collection works in custom namespace installations
  → Lines 464-467: Prometheus metrics fix for custom namespaces
  Source: Fixed issues - Operator
  - Enable monitoring in non-default namespace deployments
  - Eliminate PrometheusKubernetesListWatchFailures alerts

#### 6.3 Critical Fixes - Pipelines as Code

##### CEL Custom Repository Parameters
*For Pipeline developers using CEL expressions:*

- **Fix:** Custom Repository parameters recognized in CEL
  → Lines 473-508: CEL custom parameter recognition fix
  Source: Fixed issues - Pipelines as Code
  - Enable custom parameter usage in CEL
  - Eliminate undeclared reference errors
  - Support repository-specific logic

##### GitLab Skip CI Directive
*For Pipeline developers using GitLab:*

- **Fix:** [skip ci] commit messages now honored
  → Lines 511-514: GitLab skip ci directive fix
  Source: Fixed issues - Pipelines as Code
  - Reduce unnecessary pipeline runs
  - Save compute resources

##### Custom Hub Catalog URLs
*For Pipeline developers using versioned custom catalogs:*

- **Fix:** Versioned custom hub catalog URLs work correctly
  → Lines 516-519: Custom hub URL parsing fix
  Source: Fixed issues - Pipelines as Code
  - Enable custom catalog references with versions
  - Fix task resolution failures

##### tkn pac cel Error Messages
*For Pipeline developers using CLI:*

- **Fix:** Clear error messages for missing required flags
  → Lines 521-524: tkn pac cel error message fix
  Source: Fixed issues - Pipelines as Code
  - Improve CLI usability
  - Reduce confusion from misleading errors

##### GitHub pull_request_number Population
*For Pipeline developers using GitHub merge commits:*

- **Fix:** pull_request_number reliably populated
  → Lines 526-529: GitHub pull_request_number fix
  Source: Fixed issues - Pipelines as Code
  - Ensure reliable variable population
  - Eliminate intermittent pipeline failures

##### GitLab Path-Based Filtering
*For Pipeline developers using path filters:*

- **Fix:** All modified files evaluated for GitLab push events
  → Lines 531-534: GitLab file pagination fix
  Source: Fixed issues - Pipelines as Code
  - Ensure complete file evaluation
  - Prevent missed pipeline triggers

##### GitLab Commit Statuses
*For Pipeline developers monitoring GitLab MRs:*

- **Fix:** Commit statuses correctly reflect pipeline state
  → Lines 536-539: GitLab status mapping fix
  Source: Fixed issues - Pipelines as Code
  - Improve GitLab status accuracy
  - Reduce developer confusion

##### ok-to-test Security Fix
*For Security/Compliance officers using remember-ok-to-test=false:*

- **Fix:** Permissions re-evaluated per commit
  → Lines 551-554: ok-to-test authorization bypass fix
  Source: Fixed issues - Pipelines as Code
  - Enforce proper authorization checks
  - Prevent security bypass
  - Prevent unauthorized code execution in CI

##### Bitbucket Cloud Pipeline Statuses
*For Pipeline developers using Bitbucket Cloud:*

- **Fix:** Individual status for each pipeline run
  → Lines 562-565: Bitbucket status overwrite fix
  Source: Fixed issues - Pipelines as Code
  - View all pipeline run statuses in Bitbucket
  - Improve pipeline debugging

##### CEL Label Event Evaluation
*For Pipeline developers using label-based filtering:*

- **Fix:** CEL expressions evaluate correctly during labeling events
  → Lines 568-571: CEL label event evaluation fix
  Source: Fixed issues - Pipelines as Code
  - Enable label-based pipeline triggering
  - Implement approval workflows via labels

##### Deleted PipelineRun Status Updates
*For Pipeline developers managing PipelineRun lifecycle:*

- **Fix:** Git provider status updated when PipelineRun deleted/canceled
  → Lines 573-576: Deleted PipelineRun status update fix
  Source: Fixed issues - Pipelines as Code
  - Ensure accurate status in Git provider
  - Avoid stuck pending statuses

#### 6.4 User Interface Fixes

##### Log Whitespace Preservation
*For Pipeline developers viewing logs:*

- **Fix:** Whitespace and formatting preserved in logs
  → Lines 582-585: Log formatting preservation fix
  Source: Fixed issues - User interface
  - Improve log readability
  - Preserve structured and tabular output

##### Pipeline Builder TaskSidebar
*For Pipeline developers using Pipeline Builder:*

- **Fix:** TaskSidebar displays correctly
  → Lines 587-590: TaskSidebar display fix
  Source: Fixed issues - User interface
  - Fix Pipeline Builder usability
  - Enable proper task configuration

---

## Understanding Risks

### Job 5: Review Known Issues and Workarounds
*When assessing release risks*

**Personas:** Platform administrator, Operator/SRE, Pipeline developer
**Goal:** Understand risks before upgrading and prepare mitigation

#### 5.1 buildah-ns Task on OCP 4.20+
**Issue:** buildah-ns task fails on OpenShift 4.20 or later

*For Pipeline developers on OCP 4.20+:*

- **Workaround:** Migrate to standard buildah task with hostUsers configuration
  → Lines 373-378: buildah-ns task issue and migration guidance
  Source: Known issues - buildah-ns
  - Prevent buildah-ns task failures
  - Migrate to supported user namespace approach
  - Update affected pipeline definitions

#### 5.2 tkn CLI in Multicluster Environments
**Issue:** Several tkn commands not supported in multicluster setups

*For Operators/SREs in multicluster deployments:*

- **Limitation:** Identify unsupported tkn commands in Hub/Spoke clusters
  → Lines 380-392: tkn CLI multicluster limitations
  Source: Known issues - tkn CLI multicluster
  - Avoid relying on unsupported commands
  - Plan operational workflows for multicluster
  - Identify alternative tools for multicluster management

#### 5.3 opc results logs Command
**Issue:** opc results logs limited to 300 lines

*For Operators/SREs retrieving pipeline logs:*

- **Workaround:** Use alternative opc results commands for complete logs
  → Lines 394-399: opc results logs limitation and workaround
  Source: Known issues - opc results logs
  - Access complete log output beyond 300 line limit
  - Avoid truncated logs during troubleshooting

---

## Preparing for Future Releases

### Job 7: Understand Deprecated Features
*When planning for future upgrades*

**Personas:** Platform administrator, Pipeline developer
**Goal:** Plan migration away from features scheduled for removal

#### 7.1 openshift-pipelines-client RPM
**Deprecation:** May be removed in Pipelines 1.23

*For Platform administrators distributing CLI via RPM:*

- **Action:** Plan migration to alternative distribution methods
  → Lines 597-600: openshift-pipelines-client RPM deprecation notice
  Source: Deprecated features
  - Ensure continued CLI availability
  - Identify alternative CLI distribution methods
  - Minimize disruption to user workflows

#### 7.2 pipelinerun_status Field in Repository CR
**Deprecation:** May be removed in Pipelines 1.23

*For Pipeline developers using pipelinerun_status:*

- **Action:** Plan migration to alternative approaches
  → Lines 602-605: pipelinerun_status field deprecation notice
  Source: Deprecated features
  - Update Repository CR configurations
  - Identify replacement approaches
  - Maintain pipeline status visibility

---

## Appendices

### A. Workflow Coverage Analysis

| Stage | Coverage | Jobs | Notes |
|-------|----------|------|-------|
| Plan | ✅ | Jobs 1, 4, 7, 8 | Compatibility check, breaking changes, deprecations, removals |
| Evaluate | ✅ | Jobs 2, 3, 6 | New features, Technology Preview, fixed issues |
| Troubleshoot | ✅ | Job 5 | Known issues and workarounds |
| Upgrade | ✅ | Jobs 4, 8 | Breaking changes and removed features |
| Deploy | ❌ | - | Not applicable for release notes |
| Monitor | ❌ | - | Not applicable for release notes |
| Configure | ❌ | - | Not applicable for release notes |

### Gaps Identified

| Stage | Gap | Explanation |
|-------|-----|-------------|
| Deploy | No deployment content | Release notes focus on planning and evaluation, not procedures |
| Monitor | No monitoring content | Release notes document features, not operational guidance |
| Configure | No configuration content | Release notes reference features but don't provide configuration guides |

**Note:** These gaps are expected for release notes documentation. Procedural content belongs in product documentation.

---

### B. Component Version Compatibility Quick Reference

Refer to Compatibility and Support Matrix (Job 1) for:
- Supported OpenShift versions
- GA vs Technology Preview component status
- Multi-cluster support matrix

---

## Navigation Guide

### By User Journey

#### Platform Administrator Planning Upgrade Path:
1. Job 1: Verify Cluster Compatibility
2. Job 4: Identify Breaking Changes
3. Job 7: Understand Deprecated Features
4. Job 8: Prepare for Removed Features
5. Job 5: Review Known Issues and Workarounds
6. Job 6: Review Fixed Issues

#### Pipeline Developer Evaluating New Features:
1. Job 2: Evaluate New Pipelines Features and Enhancements
2. Job 3: Explore Technology Preview Features
3. Job 6: Review Fixed Issues
4. Job 5: Review Known Issues and Workarounds

#### Security/Compliance Officer Assessing Security Improvements:
1. Job 2: Evaluate New Pipelines Features and Enhancements (Section 2.1: Security Enhancements)
2. Job 6: Review Fixed Issues (Section 6.3: ok-to-test Security Fix)
3. Job 3: Explore Technology Preview Features

#### Operator/SRE Understanding Operational Changes:
1. Job 2: Evaluate New Pipelines Features and Enhancements (Section 2.4: Operational Improvements)
2. Job 5: Review Known Issues and Workarounds
3. Job 6: Review Fixed Issues (Section 6.2: Operator Fixes)

---

## Document Statistics

**Workflow Coverage:**
- Plan: 4 jobs (Jobs 1, 4, 7, 8)
- Evaluate: 3 jobs (Jobs 2, 3, 6)
- Troubleshoot: 1 job (Job 5)
- Upgrade: 2 jobs (Jobs 4, 8)

**Main Jobs:** 8
**User Stories/Paths:** 44
**Source Sections:** 15
**Personas Identified:** 4 (Platform administrator, Pipeline developer, Operator/SRE, Security/Compliance officer)

**Total Records Analyzed:** 52 JTBD records
- Main jobs: 10
- User stories: 42

**Key Sections Covered:**
- Compatibility and support matrix
- New features and enhancements (Pipelines, Operator, Pipelines as Code, User interface)
- Technology Preview features (Multi-cluster)
- Breaking changes
- Known issues
- Fixed issues
- Deprecated features
- Removed features

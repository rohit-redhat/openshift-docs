# OpenShift Pipelines Release Notes 1.22 — Consolidation Report

**Document:** op-release-notes-1-22-consolidation-report.md
**JTBD Records:** 59 jobs identified from release notes analysis

---

## Executive Summary

### What's Changing

The current OpenShift Pipelines 1.22 release notes are organized by **product component and feature area** (Pipelines, Pipelines as Code, OpenShift Pipelines console, Multi-cluster features), which mirrors the engineering team's internal product structure. While this organization reflects how the product is built, it creates navigation challenges for users who approach the documentation with specific goals in mind — such as improving pipeline security, optimizing performance, troubleshooting specific issues, or planning migrations.

This component-based structure scatters related user tasks across multiple sections. For example, a security engineer seeking to harden pipeline deployments must navigate through user namespace isolation in the Pipelines section, webhook signature validation in the Pipelines as Code section, and HTTP resolver integrity checks also in the Pipelines section. Similarly, performance optimization features like resolver caching, StepAction resolution, file caching, and GitHub GraphQL batching are distributed across Pipelines and Pipelines as Code sections without a clear performance-focused grouping.

The proposed JTBD-based structure reorganizes the same content around **user goals and workflow stages**, grouping related capabilities by the jobs users are trying to accomplish. Security features are consolidated under dedicated security jobs, performance optimizations are grouped together, troubleshooting content is organized by problem domain rather than component, and migration guidance is centralized for upgrade planning.

### Key Improvements

- **Security hardening unified:** 4 security-related features scattered across 3 sections (user namespace isolation, HTTP integrity checks, webhook signature validation, ok-to-test re-evaluation) → dedicated Security configuration jobs (Jobs 2, 3, 16, 49)
- **Performance optimization surfaced:** 8 performance features distributed across 2 sections (resolver caching, concurrent StepAction resolution, ServiceMonitor automation, PAC file caching, GitHub GraphQL batching, automatic Results scaling, reconciliation optimization, status update fixes) → dedicated Optimize Performance jobs (Jobs 4, 8, 11-12, 18, 21, 30, 37)
- **Troubleshooting centralized:** 32 bug fixes and known issues distributed across 5 component sections → organized by symptom and failure mode in dedicated Troubleshoot jobs (Jobs 24-55)
- **Multi-cluster features consolidated:** 4 multi-cluster Technology Preview features (configuration, automatic scaling, scheduler integration, UI differentiation) → unified multi-cluster workflow (Jobs 20-23)
- **Migration guidance grouped:** 4 breaking changes and deprecation notices → unified Migration & Deprecation jobs (Jobs 24, 56-59) with clear timing guidance
- **Pipeline behavior configuration consolidated:** 6 pipeline behavior features (array values in when expressions, display names, embedded pipelines, PVC quota handling, per-task timeouts) → grouped Configure Pipeline Behavior jobs (Jobs 5-7, 9-10)
- **PAC features organized by use case:** 7 PAC features (comment strategies, skip tags, glob patterns, CEL expressions, ANSI colors) → grouped Use Pipelines Features jobs (Jobs 13-15, 17, 19)
- **Resolved issues grouped by functional area:** 28 resolved issues across 4 sections → organized by problem domain (parameter references, resilience, platform support, cleanup, metrics) for easier troubleshooting (Jobs 28-55)

---

## Current Structure (Feature-Based)

The current release notes are organized as follows:

- **Introduction and Overview** — Product description, lifecycle policy, navigation
  - What's new overview
  - Compatibility and support matrix (versions, component status GA vs TP)
- **Release Notes for 1.22**
  - **New features and enhancements**
    - Pipelines (10 features: hostUsers, HTTP hash, resolver caching, array values, display names, embedded pipelines, concurrent StepAction, PVC quota, per-task timeout, ServiceMonitor)
    - Pipelines as Code (12 features: file caching, update comment, skip tags, glob patterns, webhook validation, CEL expressions, GitHub GraphQL)
    - OpenShift Pipelines console (1 feature: ANSI color codes)
    - Multi-cluster features (4 features: configuration, automatic scaling, Tekton Scheduler, federated UI) - Technology Preview
  - **Breaking changes** (3 items: console plugin enablement, disable-affinity-assistant removal, Tekton Hub removal)
  - **Known issues** (3 items: buildah-ns workaround, tkn CLI multicluster limitations, opc results logs limit)
  - **Resolved issues** (26 fixes across 4 sections: Pipelines, Operator, Pipelines as Code, OpenShift Pipelines console)
  - **Deprecation notices** (2 items: openshift-pipelines-client RPM, pipelinerun_status field)

**Total:** 1 main assembly with ~7 top-level sections, organized by component and release note type (new/breaking/known/resolved/deprecated).

---

## Proposed JTBD-Based Structure

### Quick Overview

- **Evaluate Platform Readiness**
  - Job 1: Verify platform compatibility for OpenShift Pipelines 1.22
  - Job 20: Configure multi-cluster mode in TektonConfig (Technology Preview)
- **Enhance Pipeline Security**
  - Job 2: Isolate user namespaces for TaskRuns and PipelineRuns on OpenShift 4.20+
  - Job 3: Verify HTTP resolver content integrity with hash parameter
  - Job 16: Enforce webhook signature validation for Forgejo and Gitea providers
- **Configure Pipeline Behavior**
  - Job 4: Reduce remote resource fetches and avoid API rate limits with resolver caching
  - Job 5: Use array values in when expression inputs for conditional logic
  - Job 6: Add display names to pipeline steps for better readability
  - Job 7: Execute embedded pipelines within pipelines
  - Job 9: Handle PVC quota limits gracefully without immediate PipelineRun failure
  - Job 10: Override individual task timeouts at PipelineRun level
- **Optimize Pipeline Performance**
  - Job 8: Reduce TaskRun startup time with concurrent StepAction resolution
  - Job 11: Enable automatic metrics discovery for Tekton Results and Pipelines webhook
  - Job 12: Reduce VCS API load with Pipelines as Code file caching
  - Job 18: Improve Pipelines as Code performance with batched GitHub GraphQL API calls
  - Job 21: Optimize Hub cluster resources with automatic Results scaling in multi-cluster mode (Technology Preview)
  - Job 30: Reduce controller reconciliation load for runs without timeouts
  - Job 37: Reduce API server load from PipelineRun status updates
- **Use Pipelines Features**
  - Job 13: Reduce comment noise with update comment strategy for GitLab and GitHub
  - Job 14: Skip pipeline execution for work-in-progress commits with commit message tags
  - Job 15: Use glob patterns for GitHub App token scoping in Pipelines as Code
  - Job 17: Use CEL expressions in Pipelines as Code pipeline templates
  - Job 19: View ANSI color codes in OpenShift console log viewer
  - Job 22: Install and manage Tekton Scheduler with Pipelines Operator (Technology Preview)
  - Job 23: Differentiate federated PipelineRuns in multi-cluster UI (Technology Preview)
- **Troubleshoot Breaking Changes & Known Issues**
  - Job 24: Enable console plugin explicitly after upgrading to Pipelines 1.22
  - Job 25: Work around buildah-ns task failure on OpenShift 4.20+
  - Job 26: Understand tkn CLI limitations in multicluster environments
  - Job 27: Work around opc results logs get command line limit
- **Troubleshoot Resolved Issues**
  - Job 28: Ensure Affinity Assistant pods inherit correct service account
  - Job 29: Identify TaskRun pod configuration errors early with clear error messages
  - Job 31: Use parameter references in pipeline parameter defaults
  - Job 32: Improve PipelineRun resilience to retryable TaskRef errors
  - Job 33: Use Kubernetes-native sidecars with proper signal handling
  - Job 34: Inspect timed-out TaskRun pods when keep-pod-on-cancel enabled
  - Job 35: View StepAction status in correct chronological order
  - Job 36: Run TaskRuns successfully on arm64 clusters
  - Job 38: Ensure operator webhooks are cleaned up when namespace is deleted
  - Job 39: Fix Prometheus metrics collection when Operator installed in custom namespace
  - Job 40-55: Various Pipelines as Code and console fixes
- **Plan Migration & Deprecation**
  - Job 56: Plan migration from openshift-pipelines-client RPM
  - Job 57: Stop using pipelinerun_status field in Repository CR
  - Job 58: Migrate from disable-affinity-assistant to coschedule feature flag
  - Job 59: Migrate from public Tekton Hub to custom self-hosted Hub or alternative catalogs

---

### Detailed Job Descriptions

#### Evaluate Platform Readiness

**Job 1: Verify platform compatibility for OpenShift Pipelines 1.22**

*When planning to deploy or upgrade to OpenShift Pipelines 1.22, I want to confirm compatibility with my OpenShift Container Platform version and understand component status (GA vs TP), so I can ensure a supported deployment.*

Prerequisites: OpenShift cluster version, current Pipelines version (if upgrading)

- **1.1. Review compatibility matrix for supported OpenShift versions** `[reference]`
  - Compatibility and support matrix (Introduction): Lists OpenShift 4.14-4.21 support, component versions (Pipelines 1.9.x, Triggers 0.35.x, CLI 0.44.x, Chains 0.26.x GA, Hub 1.23.x TP, PAC 0.42.x GA, Results 0.18.x GA, Manual Approval Gate 0.8.x TP, Pruner 0.3.x GA, Cache 0.3.x GA)
  - Context: Use before deployment or upgrade to verify platform compatibility and component GA/TP status

**Job 20: Configure multi-cluster mode in TektonConfig (Technology Preview)**

*When planning multi-cluster Pipelines deployment, I want to enable and configure multi-cluster setup with Hub or Spoke role, so I can centralize pipeline management across multiple OpenShift clusters.*

Prerequisites: Multiple OpenShift clusters, TektonConfig custom resource, understanding of Hub/Spoke architecture

- **20.1. Enable multi-cluster mode and set role** `[procedure]`
  - Multi-cluster configuration (New Features - Multi-cluster): Set multi-cluster-disabled to false and configure multi-cluster-role as Hub or Spoke
  - Context: Technology Preview feature for centralized Results API and distributed execution

---

#### Enhance Pipeline Security

**Job 2: Isolate user namespaces for TaskRuns and PipelineRuns on OpenShift 4.20+**

*When securing pipeline workloads with Kubernetes-native user namespace isolation, I want to configure hostUsers in podTemplate to control host user namespace sharing without legacy CRI-O annotations, so I can improve security posture on OpenShift 4.20+.*

Prerequisites: OpenShift 4.20 or later, TaskRun or PipelineRun definitions

- **2.1. Configure hostUsers setting in podTemplate** `[procedure]`
  - hostUsers support in podTemplate (New Features - Pipelines): Set hostUsers to false in TaskRun or PipelineRun podTemplate for user namespace isolation
  - Context: Kubernetes-native approach replaces legacy io.kubernetes.cri-o.userns-mode annotation removed in OpenShift 4.20

**Job 3: Verify HTTP resolver content integrity with hash parameter**

*When fetching pipeline resources from HTTP sources, I want to ensure fetched content matches expected hash to prevent tampering or corruption, so I can improve security for HTTP-sourced resources.*

Prerequisites: HTTP resolver usage, SHA-256 or SHA-512 hash of expected content

- **3.1. Use hash parameter for content verification** `[procedure]`
  - HTTP resolver hash parameter (New Features - Pipelines): Add hash parameter with SHA-256 or SHA-512 value to HTTP resolver configuration
  - Context: Similar security model to git resolver hash validation

**Job 16: Enforce webhook signature validation for Forgejo and Gitea providers**

*When using Pipelines as Code with Forgejo or Gitea VCS providers, I want to ensure incoming webhook requests are validated and authenticated from trusted sources, so I can prevent spoofed webhook attacks.*

Prerequisites: Pipelines as Code with Forgejo or Gitea provider

- **16.1. Verify webhook signature validation enabled** `[reference]`
  - Webhook signature validation (New Features - Pipelines as Code): Confirms signature validation enabled for Forgejo and Gitea, rejecting unauthenticated requests
  - Context: Automatically enabled in 1.22, prevents spoofed webhook requests

---

#### Configure Pipeline Behavior

**Job 4: Reduce remote resource fetches and avoid API rate limits with resolver caching**

*When running pipelines that repeatedly fetch the same remote resources, I want to enable resolver caching to minimize redundant fetches and prevent API rate limit errors, so I can improve pipeline reliability.*

Prerequisites: Bundle, git, or cluster resolver usage

- **4.1. Configure resolver cache mode** `[procedure]`
  - Resolver caching (New Features - Pipelines): Set cache mode to auto (default), always, or never for bundle, git, and cluster resolvers
  - Context: auto caches automatically, always forces caching, never disables caching

**Job 5: Use array values in when expression inputs for conditional logic**

*When building pipelines with conditional task execution based on array parameters or results, I want to evaluate array values in when expression inputs to enable flexible conditional logic, so I can create more sophisticated pipeline workflows.*

Prerequisites: Pipeline definitions with when expressions

- **5.1. Use array values in when expression input attribute** `[procedure]`
  - Array values in when expressions (New Features - Pipelines): Reference array parameters or results in when expression input attribute
  - Context: Enables conditional logic based on array contents

**Job 6: Add display names to pipeline steps for better readability**

*When creating or maintaining Task definitions for CI/CD pipelines, I want to add human-readable display names to steps that improve pipeline monitoring and readability, so I can more easily identify steps in UI and logs.*

Prerequisites: Task definitions

- **6.1. Add displayName field to Step objects** `[procedure]`
  - displayName field for Step objects (New Features - Pipelines): Add displayName field to Step objects in Task definitions
  - Context: Display names appear in UI and monitoring, improving step identification

**Job 7: Execute embedded pipelines within pipelines**

*When building complex pipeline workflows that require nested pipeline execution, I want to use PipelineSpec field under tasks to execute embedded pipelines directly, so I can create pipelines-in-pipelines compositions.*

Prerequisites: Pipeline definitions

- **7.1. Use PipelineSpec field under tasks** `[procedure]`
  - Embedded pipelines via PipelineSpec (New Features - Pipelines): Add PipelineSpec field under tasks in Pipeline definitions
  - Context: Enables pipelines-in-pipelines functionality for complex workflows

**Job 9: Handle PVC quota limits gracefully without immediate PipelineRun failure**

*When operating in environments with PVC quota limits, I want to allow PipelineRuns to requeue and retry when PVC quota is hit instead of failing immediately, so I can recover from temporary quota issues.*

Prerequisites: Environments with PVC quota limits

- **9.1. Benefit from automatic PVC quota requeue behavior** `[reference]`
  - PVC quota limit handling (New Features - Pipelines): PipelineRun automatically requeued when PVC creation hits quota, succeeds when quota becomes available
  - Context: Automatically enabled in 1.22, improves resilience to temporary quota issues

**Job 10: Override individual task timeouts at PipelineRun level**

*When managing pipeline executions where different tasks need different timeout values, I want to set specific timeout values for individual tasks using spec.taskRunSpecs[].timeout field, so I can have finer-grained timeout control.*

Prerequisites: PipelineRun definitions with tasks requiring different timeouts

- **10.1. Set per-task timeout in PipelineRun** `[procedure]`
  - Per-task timeout override (New Features - Pipelines): Use spec.taskRunSpecs[].timeout field in PipelineRun to set individual task timeouts
  - Context: Individual task timeouts honored separately from overall PipelineRun timeout

---

#### Optimize Pipeline Performance

**Job 8: Reduce TaskRun startup time with concurrent StepAction resolution**

*When running TaskRuns that use multiple remote StepActions, I want to benefit from concurrent StepAction resolution to minimize startup delays, so I can improve pipeline performance.*

Prerequisites: TaskRuns using remote StepActions

- **8.1. Benefit from concurrent StepAction resolution** `[reference]`
  - Concurrent StepAction resolution (New Features - Pipelines): StepActions resolved concurrently not sequentially
  - Context: Automatically enabled in 1.22, reduces TaskRun startup time

**Job 11: Enable automatic metrics discovery for Tekton Results and Pipelines webhook**

*When setting up monitoring and alerting for Pipelines components, I want to use automatically created ServiceMonitor resources for Prometheus Operator integration, so I can avoid manual ServiceMonitor creation.*

Prerequisites: Prometheus Operator installed

- **11.1. Benefit from automatic ServiceMonitor creation** `[reference]`
  - Automatic ServiceMonitor creation (New Features - Pipelines): ServiceMonitor automatically created for tekton-results and tekton-pipelines-webhook
  - Context: Automatically enabled in 1.22, Prometheus Operator automatically discovers metrics endpoints

**Job 12: Reduce VCS API load with Pipelines as Code file caching**

*When using PAC with path-based filtering that makes many API calls, I want to enable caching of changed files per event to minimize VCS API calls and avoid rate limits, so I can improve performance and reliability.*

Prerequisites: Pipelines as Code with path-based filtering (path.pathChanged() or on-path-change annotations)

- **12.1. Benefit from file caching per event** `[reference]`
  - PAC file caching (New Features - Pipelines as Code): Changed files cached per event, path.pathChanged() and on-path-change annotations use cache
  - Context: Automatically enabled in 1.22, reduces API rate limit risk

**Job 18: Improve Pipelines as Code performance with batched GitHub GraphQL API calls**

*When using PAC with GitHub or GitHub Enterprise with many .tekton files, I want to benefit from batched GraphQL API calls that reduce GitHub API call count, so I can improve performance and avoid rate limits.*

Prerequisites: Pipelines as Code with GitHub or GitHub Enterprise, multiple .tekton files

- **18.1. Benefit from GitHub GraphQL batching** `[reference]`
  - GitHub GraphQL batching (New Features - Pipelines as Code): Multiple .tekton files fetched in single GraphQL request
  - Context: Automatically enabled in 1.22 for GitHub and GitHub Enterprise

**Job 21: Optimize Hub cluster resources with automatic Results scaling in multi-cluster mode (Technology Preview)**

*When operating multi-cluster Hub with centralized Results API, I want to reduce Hub cluster resource usage by automatically scaling down watcher and retention-policy-agent to zero replicas, so I can optimize Hub cluster resources.*

Prerequisites: Multi-cluster Hub configuration, Tekton Results installed

- **21.1. Benefit from automatic Results component scaling** `[reference]`
  - Automatic Results scaling on Hub (New Features - Multi-cluster): watcher and retention-policy-agent replicas automatically set to 0 on Hub
  - Context: Technology Preview feature, components only needed on Spoke clusters

**Job 30: Reduce controller reconciliation load for runs without timeouts**

*When operating pipelines controller with many running TaskRuns and PipelineRuns, I want to ensure runs without timeout configurations do not cause excessive reconciliation loops, so I can reduce controller CPU usage and improve cluster performance.*

Prerequisites: TaskRuns and PipelineRuns without timeout configurations

- **30.1. Benefit from reconciliation optimization** `[reference]`
  - Reconciliation optimization fix (Resolved Issues - Pipelines): Reconciliation only on actual changes, not excessive loops for runs without timeouts
  - Context: Fixed in 1.22, improves controller performance and cluster scalability

**Job 37: Reduce API server load from PipelineRun status updates**

*When operating large-scale pipelines with many status updates, I want to ensure consistent array ordering in PipelineRun status to reduce invalid status updates, so I can improve API server performance and cluster stability.*

Prerequisites: Large-scale pipeline deployments

- **37.1. Benefit from status update optimization** `[reference]`
  - Status update optimization via consistent array ordering (Resolved Issues - Pipelines): Array ordering consistent in status, reducing invalid status updates
  - Context: Fixed in 1.22, improves API server performance

---

#### Use Pipelines Features

**Job 13: Reduce comment noise with update comment strategy for GitLab and GitHub**

*When managing Pipelines as Code with GitLab or GitHub webhooks, I want to maintain single status comment per PipelineRun that updates instead of creating multiple comments, so I can reduce repository comment clutter.*

Prerequisites: Pipelines as Code with GitLab or GitHub webhooks

- **13.1. Use update comment strategy** `[procedure]`
  - Update comment strategy (New Features - Pipelines as Code): Configure update comment strategy to maintain single comment updated with new status and current commit SHA
  - Context: Reduces comment noise in repositories

**Job 14: Skip pipeline execution for work-in-progress commits with commit message tags**

*When pushing work-in-progress or minor commits that should not trigger pipelines, I want to use commit message tags to skip pipeline execution and save resources, so I can avoid unnecessary pipeline runs.*

Prerequisites: Pipelines as Code configured for repository

- **14.1. Use skip tags in commit messages** `[procedure]`
  - Commit skip tags (New Features - Pipelines as Code): Use [skip ci], [ci skip], [skip tkn], or [tkn skip] tags (case-insensitive) in commit messages
  - Context: Pipeline execution skipped for tagged commits; GitLab may generate extra list entry

**Job 15: Use glob patterns for GitHub App token scoping in Pipelines as Code**

*When managing many private Git submodules with GitHub App, I want to grant token access to multiple repositories using wildcard patterns in single configuration, so I can simplify management of private submodules.*

Prerequisites: GitHub App configuration, private submodules

- **15.1. Configure glob patterns for token scoping** `[procedure]`
  - Glob patterns for GitHub App scoping (New Features - Pipelines as Code): Use glob patterns like owner/* in secret-github-app-scope-extra-repos or github_app_token_scope_repos
  - Context: Works in global config maps and Repository CR

**Job 17: Use CEL expressions in Pipelines as Code pipeline templates**

*When creating dynamic pipeline templates in Pipelines as Code, I want to use cel: prefix to evaluate Common Expression Language expressions inline in templates, so I can perform conditional logic and complex string composition.*

Prerequisites: Pipelines as Code templates

- **17.1. Use CEL expressions with cel: prefix** `[procedure]`
  - CEL expressions in templates (New Features - Pipelines as Code): Use cel: prefix for ternary operations, presence checks, and complex string composition with body, headers, files, pac namespaces
  - Context: Enables dynamic template generation with inline logic

**Job 19: View ANSI color codes in OpenShift console log viewer**

*When viewing TaskRun and PipelineRun logs in OpenShift console, I want to see colored logs with ANSI color code support for better readability, so I can improve visual distinction in output.*

Prerequisites: OpenShift console access

- **19.1. Benefit from ANSI color code rendering** `[reference]`
  - ANSI color code support (New Features - OpenShift Pipelines console): ANSI color codes rendered in console log viewer
  - Context: Automatically enabled in 1.22, improves log readability

**Job 22: Install and manage Tekton Scheduler with Pipelines Operator (Technology Preview)**

*When setting up resource allocation and queuing for pipelines, I want to deploy Tekton Scheduler (Tekton-Kueue) using Pipelines Operator for pipeline resource management, so I can enable queue-based resource allocation.*

Prerequisites: Upstream Kueue installed, TektonConfig custom resource

- **22.1. Configure Tekton Scheduler in TektonConfig** `[procedure]`
  - Tekton Scheduler management (New Features - Multi-cluster): Configure scheduler section in TektonConfig CR with default queue name, multi-cluster support available
  - Context: Technology Preview feature, requires upstream Kueue installation

**Job 23: Differentiate federated PipelineRuns in multi-cluster UI (Technology Preview)**

*When viewing PipelineRuns in multi-cluster UI, I want to visually distinguish between local Hub PipelineRuns and federated PipelineRuns using icon indicator, so I can improve multi-cluster visibility.*

Prerequisites: Multi-cluster Hub configuration, OpenShift console access

- **23.1. Identify federated PipelineRuns by icon** `[reference]`
  - Federated PipelineRun visual indicator (New Features - Multi-cluster): Icon differentiates local vs federated PipelineRuns based on managedBy field
  - Context: Technology Preview feature for multi-cluster UI

---

#### Troubleshoot Breaking Changes & Known Issues

**Job 24: Enable console plugin explicitly after upgrading to Pipelines 1.22**

*When upgrading to OpenShift Pipelines 1.22 with console plugin changes, I want to understand that console plugin must be explicitly enabled for Pipelines section to appear, so I can restore console navigation.*

Prerequisites: Upgrading to OpenShift Pipelines 1.22  
Timing: DURING upgrade to 1.22 - console plugin requires explicit enablement

- **24.1. Enable console plugin in TektonConfig** `[procedure]`
  - Console plugin explicit enablement (Breaking Changes): Console plugin requires explicit enablement, legacy static console plugin deprecated
  - Context: Breaking change, Pipelines navigation not visible by default after upgrade

**Job 25: Work around buildah-ns task failure on OpenShift 4.20+**

*When using buildah-ns task on OpenShift 4.20 or later, I want to use standard buildah task with hostUsers: false in PodTemplate to enable user namespaces, so I can work around buildah-ns failure.*

Prerequisites: OpenShift 4.20+, buildah-ns task usage

- **25.1. Use buildah task with hostUsers: false** `[procedure]`
  - buildah-ns task workaround (Known Issues - Pipelines): Use buildah task with hostUsers: false in PodTemplate instead of buildah-ns
  - Context: CRI-O annotation io.kubernetes.cri-o.userns-mode removed in OpenShift 4.20

**Job 26: Understand tkn CLI limitations in multicluster environments**

*When operating tkn CLI tool in multicluster Hub and Spoke setup, I want to recognize which tkn commands do not work correctly in multicluster and use alternatives, so I can avoid command failures.*

Prerequisites: Multi-cluster Hub or Spoke configuration, tkn CLI

- **26.1. Identify failing tkn commands on Hub** `[reference]`
  - tkn CLI multicluster limitations (Known Issues - CLI): tkn taskrun list, pipelinerun describe, pipelinerun logs, pipelinerun cancel fail on Hub
  - Context: Use OpenShift console or oc commands for multicluster management

**Job 27: Work around opc results logs get command line limit**

*When retrieving logs from Tekton Results with more than 300 lines, I want to use opc results pipelinerun logs or opc results taskrun logs commands for complete output, so I can view complete logs.*

Prerequisites: opc CLI, Tekton Results

- **27.1. Use pipelinerun logs or taskrun logs commands** `[procedure]`
  - opc results logs workaround (Known Issues - CLI): Use opc results pipelinerun logs or opc results taskrun logs instead of opc results logs get
  - Context: logs get limited to 300 lines, command deprecated

---

#### Troubleshoot Resolved Issues

**Job 28: Ensure Affinity Assistant pods inherit correct service account**

*When using affinity assistant to co-schedule tasks with shared workspaces, I want to verify Affinity Assistant pods use PipelineRun service account instead of default service account, so I can ensure correct SCC permissions.*

Prerequisites: Affinity assistant usage, workspaces

- **28.1. Verify service account inheritance** `[reference]`
  - Affinity Assistant service account fix (Resolved Issues - Pipelines): Affinity Assistant inherits PipelineRun service account, correct SCC permissions applied
  - Context: Fixed in 1.22

**Job 29: Identify TaskRun pod configuration errors early with clear error messages**

*When TaskRuns failing to start due to missing config maps or secrets, I want to receive immediate clear error messages identifying specific configuration issues, so I can troubleshoot faster without waiting for timeout.*

Prerequisites: TaskRun definitions with config maps or secrets

- **29.1. Benefit from early error detection** `[reference]`
  - Early TaskRun pod configuration errors (Resolved Issues - Pipelines): TaskRun fails immediately with clear error identifying specific missing resource (config map or secret)
  - Context: Fixed in 1.22, no timeout waiting for generic error

**Job 31: Use parameter references in pipeline parameter defaults**

*When defining pipeline parameters with fallback patterns, I want to reference other parameters in default values to enable flexible fallback patterns, so I can create sophisticated parameter dependency chains.*

Prerequisites: Pipeline parameter definitions

- **31.1. Reference other parameters in defaults** `[reference]`
  - Parameter references in defaults fix (Resolved Issues - Pipelines): Parameter defaults support references to other parameters, arbitrary dependency chains work, circular dependencies detected with clear errors
  - Context: Fixed in 1.22, supports all parameter types (string, array, object)

**Job 32: Improve PipelineRun resilience to retryable TaskRef errors**

*When running PipelineRuns that reference remote tasks, I want to ensure PipelineRuns retry on retryable TaskRef reconciliation errors instead of failing, so I can improve resilience to transient issues.*

Prerequisites: PipelineRuns with remote TaskRef

- **32.1. Benefit from TaskRef error resilience** `[reference]`
  - TaskRef error resilience fix (Resolved Issues - Pipelines): PipelineRuns retry on retryable errors, only explicit validation errors cause failure
  - Context: Fixed in 1.22

**Job 33: Use Kubernetes-native sidecars with proper signal handling**

*When running TaskRuns with Kubernetes-native sidecars, I want to ensure sidecars handle signals correctly and operate reliably, so I can avoid init container restarts.*

Prerequisites: TaskRuns with Kubernetes-native sidecars

- **33.1. Benefit from sidecar signal handling** `[reference]`
  - Sidecar signal handling fix (Resolved Issues - Pipelines): Signal handling added to SidecarLog results, no repeated init container restarts
  - Context: Fixed in 1.22

**Job 34: Inspect timed-out TaskRun pods when keep-pod-on-cancel enabled**

*When debugging timed-out TaskRuns with keep-pod-on-cancel feature flag, I want to ensure pods are retained for timed-out TaskRuns for debugging purposes, so I can inspect pod state.*

Prerequisites: keep-pod-on-cancel feature flag enabled

- **34.1. Benefit from pod retention on timeout** `[reference]`
  - Pod retention on timeout fix (Resolved Issues - Pipelines): keep-pod-on-cancel feature flag honored, pods retained on timeout
  - Context: Fixed in 1.22

**Job 35: View StepAction status in correct chronological order**

*When reviewing task execution timeline using StepAction, I want to see status steps displayed in correct sequential order for accurate interpretation, so I can understand execution flow.*

Prerequisites: StepAction usage

- **35.1. Benefit from chronological ordering** `[reference]`
  - StepAction chronological ordering fix (Resolved Issues - Pipelines): Status steps in correct order, accurate execution timeline
  - Context: Fixed in 1.22

**Job 36: Run TaskRuns successfully on arm64 clusters**

*When operating TaskRuns on arm64 Kubernetes clusters, I want to ensure TaskRuns execute reliably on arm64 architecture without platform variant issues, so I can support arm64 environments.*

Prerequisites: arm64 Kubernetes clusters

- **36.1. Benefit from arm64 platform support** `[reference]`
  - arm64 platform support fix (Resolved Issues - Pipelines): TaskRuns succeed on arm64 clusters, entrypoint handles Linux platform variants
  - Context: Fixed in 1.22

**Job 38: Ensure operator webhooks are cleaned up when namespace is deleted**

*When uninstalling Pipelines Operator by deleting openshift-pipelines namespace, I want to verify all operator webhooks are removed with proper owner references, so I can avoid orphaned webhooks.*

Prerequisites: Pipelines Operator installed

- **38.1. Benefit from webhook cleanup** `[reference]`
  - Webhook cleanup on namespace deletion (Resolved Issues - Operator): Owner references added to webhooks (proxy.operator.tekton.dev, validation.pipelinesascode.tekton.dev, namespace.operator.tekton.dev), cleaned up on namespace deletion
  - Context: Fixed in 1.22

**Job 39: Fix Prometheus metrics collection when Operator installed in custom namespace**

*When Pipelines Operator installed in non-default namespace like openshift-pipelines, I want to ensure ServiceMonitor targets correct namespace for metrics scraping, so I can avoid PrometheusKubernetesListWatchFailures alerts.*

Prerequisites: Pipelines Operator in custom namespace, Prometheus

- **39.1. Benefit from ServiceMonitor namespace fix** `[reference]`
  - ServiceMonitor namespace fix (Resolved Issues - Operator): ServiceMonitor auto-targets operator namespace, no hardcoded openshift-operators reference
  - Context: Fixed in 1.22

(Jobs 40-55: Various Pipelines as Code and console fixes - detailed descriptions omitted for brevity in this consolidation report, see full TOC for complete details)

---

#### Plan Migration & Deprecation

**Job 56: Plan migration from openshift-pipelines-client RPM**

*When using openshift-pipelines-client RPM for tkn CLI, I want to identify alternative distribution method before RPM is removed in 1.23, so I can maintain tkn CLI access.*

Prerequisites: Current use of openshift-pipelines-client RPM  
Timing: BEFORE Pipelines 1.23 - RPM will be removed

- **56.1. Identify alternative tkn CLI distribution** `[concept]`
  - RPM deprecation notice (Deprecation Notices): openshift-pipelines-client RPM deprecated, will be removed in Pipelines 1.23
  - Context: Plan migration to alternative installation method

**Job 57: Stop using pipelinerun_status field in Repository CR**

*When using Pipelines as Code Repository custom resources, I want to update configurations to avoid pipelinerun_status field before removal in 1.23, so I can maintain compatibility with future releases.*

Prerequisites: Repository CR with pipelinerun_status field  
Timing: BEFORE Pipelines 1.23 - field will be removed

- **57.1. Update integrations to avoid pipelinerun_status** `[concept]`
  - pipelinerun_status deprecation (Deprecation Notices - Pipelines as Code): pipelinerun_status field deprecated, will be removed in Pipelines 1.23
  - Context: Update integrations and automation

**Job 58: Migrate from disable-affinity-assistant to coschedule feature flag**

*When upgrading to Pipelines 1.22 with affinity assistant configuration, I want to update TektonConfig to use coschedule feature flag instead of removed disable-affinity-assistant field, so I can maintain affinity assistant configuration.*

Prerequisites: TektonConfig with disable-affinity-assistant field  
Timing: DURING upgrade to 1.22 - breaking change in configuration

- **58.1. Replace disable-affinity-assistant with coschedule** `[procedure]`
  - disable-affinity-assistant removal (Breaking Changes): disable-affinity-assistant field removed from TektonConfig, replaced with coschedule feature flag
  - Context: Breaking change requiring configuration update

**Job 59: Migrate from public Tekton Hub to custom self-hosted Hub or alternative catalogs**

*When using public Tekton Hub (hub.tekton.dev) for pipeline resources, I want to migrate to custom self-hosted Tekton Hub instances or other task catalogs, so I can maintain access to task catalog.*

Prerequisites: Current use of hub.tekton.dev  
Timing: BEFORE relying on hub.tekton.dev - public hub removed

- **59.1. Deploy custom Hub or identify alternative** `[procedure]`
  - Tekton Hub removal (Breaking Changes): Public Tekton Hub (hub.tekton.dev) removed, no default built-in catalog
  - Context: Deploy custom self-hosted Hub or use Artifact Hub

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | Product components and feature areas | User goals and workflow stages |
| **Top-level items** | 7 sections (Compatibility, New features, Breaking changes, Known issues, Resolved issues, Deprecation) | 59 jobs organized into 8 workflow stages |
| **Security features** | Scattered across 3 sections (Pipelines, PAC, Resolved) | Consolidated into 4 dedicated security jobs (Jobs 2, 3, 16, 49) |
| **Performance optimization** | Mixed with features in 2 sections (Pipelines, PAC) | Consolidated into 8 dedicated performance jobs (Jobs 4, 8, 11-12, 18, 21, 30, 37) |
| **Troubleshooting** | Separated by issue type (Breaking/Known/Resolved) and component | Unified by problem domain (32 jobs) |
| **Multi-cluster features** | Single Technology Preview section | Workflow-integrated (4 jobs: evaluation, optimization, installation, UI) |
| **Migration guidance** | Separated (Breaking changes, Deprecation notices) | Unified Migration & Deprecation (4 jobs with timing guidance) |
| **PAC features** | Single component section | Organized by use case (reduce noise, skip execution, scope tokens, etc.) |

### Job List Adjustments from Suggested Input

The analysis identified **59 jobs** which were organized into workflow stages. No jobs were merged or consolidated — each represents a distinct user goal with unique content and context.

**Rationale for 59-job count:**
- Release notes naturally have high job count due to covering new features, breaking changes, known issues, resolved issues, and deprecations across multiple components
- Each bug fix represents a distinct troubleshooting job
- Breaking changes and deprecations require separate migration jobs with timing guidance
- Technology Preview features require separate evaluation jobs
- Security and performance features warrant dedicated jobs for discoverability

---

## Consolidation Examples

### Example 1: Security Hardening (4 scattered features → 4 unified jobs under "Enhance Pipeline Security")

**Current (Fragmented):**
- Section: Pipelines - hostUsers support (lines 148-151)
- Section: Pipelines - HTTP resolver hash (lines 153-156)
- Section: Pipelines as Code - Webhook validation (lines 281-284)
- Section: Resolved Issues - PAC - ok-to-test re-evaluation (lines 551-554)

Users seeking to harden pipeline security must navigate across New Features Pipelines, New Features PAC, and Resolved Issues PAC sections to find all security-related capabilities.

**Proposed (Consolidated):**
- **Enhance Pipeline Security** (workflow stage)
  - Job 2: Isolate user namespaces (Pipelines, lines 148-151)
  - Job 3: Verify HTTP resolver content integrity (Pipelines, lines 153-156)
  - Job 16: Enforce webhook signature validation (PAC, lines 281-284)
  - Job 49: Re-evaluate /ok-to-test approvals (Resolved - PAC, lines 551-554)

**Benefit:** Security engineers find all security hardening features in one dedicated section, regardless of component origin!

---

### Example 2: Performance Optimization (8 scattered features → 8 unified jobs under "Optimize Pipeline Performance")

**Current (Fragmented):**
- Section: Pipelines - Resolver caching (lines 158-167)
- Section: Pipelines - Concurrent StepAction resolution (lines 184-187)
- Section: Pipelines - ServiceMonitor automation (lines 202-205)
- Section: Pipelines as Code - File caching (lines 210-213)
- Section: Pipelines as Code - GitHub GraphQL batching (lines 299-302)
- Section: Multi-cluster - Automatic Results scaling (lines 339-342)
- Section: Resolved Issues - Pipelines - Reconciliation optimization (lines 416-419)
- Section: Resolved Issues - Pipelines - Status update optimization (lines 451-454)

Users seeking performance improvements must search through New Features Pipelines, New Features PAC, Multi-cluster, and Resolved Issues sections.

**Proposed (Consolidated):**
- **Optimize Pipeline Performance** (workflow stage)
  - Job 4: Reduce remote resource fetches with resolver caching
  - Job 8: Reduce TaskRun startup time with concurrent StepAction
  - Job 11: Enable automatic metrics discovery
  - Job 12: Reduce VCS API load with file caching
  - Job 18: Improve PAC performance with GitHub GraphQL
  - Job 21: Optimize Hub cluster resources
  - Job 30: Reduce controller reconciliation load
  - Job 37: Reduce API server load from status updates

**Benefit:** Platform administrators find all performance optimization features grouped together, spanning both new features and resolved performance issues!

---

### Example 3: Troubleshooting (32 scattered fixes → 32 organized jobs by problem domain)

**Current (Fragmented):**
- Section: Breaking Changes (3 items across console and configuration)
- Section: Known Issues (3 items across Pipelines and CLI)
- Section: Resolved Issues - Pipelines (7 fixes)
- Section: Resolved Issues - Operator (2 fixes)
- Section: Resolved Issues - Pipelines as Code (16 fixes)
- Section: Resolved Issues - Console (2 fixes)

Users troubleshooting issues must know which component is affected and which issue type (breaking/known/resolved) to navigate correctly.

**Proposed (Consolidated):**
- **Troubleshoot Breaking Changes & Known Issues** (Jobs 24-27)
  - Console plugin enablement (Breaking)
  - buildah-ns workaround (Known)
  - tkn CLI multicluster limitations (Known)
  - opc results logs limit (Known)
- **Troubleshoot Resolved Issues** (Jobs 28-55)
  - Organized by functional area: service accounts, pod configuration, parameters, resilience, sidecars, debugging, platform support, cleanup, metrics, PAC fixes, console fixes

**Benefit:** Users find troubleshooting content organized by symptom and problem domain, not by component or issue type!

---

## Content Gaps Identified

| Gap | JTBD Reference | Current Coverage | Impact |
|-----|---------------|-----------------|--------|
| Monitor pipeline health and metrics | Performance jobs (11, 30, 37, 39) | Only ServiceMonitor automation and metrics fixes mentioned | **Medium** — Users need guidance on using ServiceMonitor and interpreting metrics for pipeline health |
| Governance and retention policies | No dedicated jobs | Not covered in 1.22 release notes (covered in Results docs) | **Low** — Retention policy configuration exists in other docs, not critical for release notes |
| Multi-cluster troubleshooting beyond tkn CLI | Job 26 (tkn limitations) | Only tkn CLI limitations mentioned | **Medium** — Users need troubleshooting guidance for multi-cluster federation issues beyond CLI |
| Rollback procedures for breaking changes | Jobs 24, 58, 59 (breaking changes) | Only forward migration described | **Low** — Breaking changes may need rollback guidance, but typically not expected in release notes |
| Multi-cluster architecture and design patterns | Job 20 (configuration) | Only configuration settings mentioned | **Medium** — Users need architectural guidance for Hub/Spoke design, but appropriate for separate architecture doc |

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 7 sections (Compatibility, New features, Breaking, Known, Resolved, Deprecation, Resources) | 8 workflow stages with 59 jobs | Organized by user goals not component |
| Sections to browse for "security hardening" | 3 sections (Pipelines, PAC, Resolved-PAC) | 1 workflow stage (Enhance Pipeline Security), 4 jobs | ~66% reduction in navigation |
| Sections to browse for "performance optimization" | 4 sections (Pipelines, PAC, Multi-cluster, Resolved-Pipelines) | 1 workflow stage (Optimize Performance), 8 jobs | ~75% reduction in navigation |
| Sections to browse for "troubleshooting issues" | 6 sections (Breaking, Known-Pipelines, Known-CLI, Resolved-Pipelines, Resolved-Operator, Resolved-PAC, Resolved-Console) | 2 workflow stages (Breaking/Known, Resolved), 32 jobs | Organized by problem domain |
| Sections to browse for "migration planning" | 2 sections (Breaking changes, Deprecation notices) | 1 workflow stage (Migration & Deprecation), 4 jobs with timing | Consolidated with timing guidance |
| Clicks to find "multi-cluster setup" | 2+ clicks (navigate to Multi-cluster section, find specific feature) | 2 clicks (Evaluate Platform Readiness → Job 20-23) | Grouped workflow |

**Final job count: 59** (from 59 JTBD records). No consolidation was performed because each job represents a distinct user goal:
- New features: 27 jobs (compatibility, security, behavior, performance, features, multi-cluster)
- Breaking changes: 4 jobs (console plugin, affinity-assistant, Tekton Hub, RPM deprecation)
- Known issues: 3 jobs (buildah-ns, tkn CLI, opc results)
- Resolved issues: 28 jobs (organized by functional area)
- Deprecation: 2 jobs (RPM, pipelinerun_status) merged into migration jobs

Release notes naturally have higher job counts because they document discrete changes (features, fixes, deprecations) rather than comprehensive task workflows. Each job maps to a specific user goal (adopt new feature, work around known issue, fix resolved problem, plan migration).

---

## Document Statistics

**Current Structure:**
- Top-level sections: 7
- Component subsections: ~4 (Pipelines, PAC, Console, Multi-cluster within New Features)
- Total line references: 618 lines
- Organization: Component-based with issue type separation

**Proposed Structure:**
- Main jobs: 59
- Workflow stages: 8
  - Evaluate Platform Readiness: 2 jobs
  - Enhance Pipeline Security: 4 jobs (includes 1 from Resolved)
  - Configure Pipeline Behavior: 6 jobs
  - Optimize Pipeline Performance: 8 jobs (includes 3 from Resolved)
  - Use Pipelines Features: 7 jobs
  - Troubleshoot Breaking Changes & Known Issues: 4 jobs
  - Troubleshoot Resolved Issues: 28 jobs
  - Plan Migration & Deprecation: 4 jobs
- Line coverage: 618 lines (100% of source)
- Organization: Workflow-based with functional grouping

**Key Metrics:**
- Jobs addressing security: 4 (Jobs 2, 3, 16, 49)
- Jobs addressing performance: 8 (Jobs 4, 8, 11-12, 18, 21, 30, 37)
- Jobs addressing new features: 27 (compatibility, security, behavior, performance, features, multi-cluster)
- Jobs addressing troubleshooting: 32 (4 breaking/known, 28 resolved)
- Jobs addressing migration/deprecation: 4 (Jobs 24, 56-59)
- Technology Preview features: 4 (Jobs 20-23 multi-cluster)
- Jobs with timing guidance: 4 (Jobs 24, 56, 57, 58, 59)

---

**Generated:** 2026-06-11  
**Source Document:** op-release-notes-1-22-self-managed-reduced.adoc (Lines 1-618)  
**JTBD Analysis:** 59 records

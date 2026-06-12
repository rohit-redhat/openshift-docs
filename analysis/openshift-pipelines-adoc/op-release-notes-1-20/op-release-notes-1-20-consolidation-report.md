# OpenShift Pipelines 1.20 Release Notes — Consolidation Report

**Document:** op-release-notes-1-20-self-managed-reduced.adoc  
**JTBD Records:** 31 pre-consolidated jobs → 15 final main jobs (after merging user stories into parent jobs)

**Generated:** 2026-06-11

---

## Executive Summary

### What's Changing

The current OpenShift Pipelines 1.20 release notes are organized primarily by **component and feature categories** (Operator, Pruner, Triggers, Results, Pipelines as Code, Breaking Changes, Known Issues, Fixed Issues, Deprecated Features). This structure mirrors the engineering architecture rather than user goals and workflows.

This organizing principle creates navigation friction because users must translate their goals ("I need to set up FIPS compliance" or "I need to migrate from Tekton Hub") into component knowledge ("Which section covers FIPS?") and scan multiple sections to understand a single workflow. For example, understanding Pipelines as Code capabilities requires reading across New Features, Breaking Changes, Known Issues, and Fixed Issues sections, with related information scattered throughout.

The proposed structure reorganizes content by **user goals and workflow stages** (Evaluate, Use, Optimize, Migrate, Troubleshoot, Plan), grouping related approaches under unified jobs that represent complete user objectives. This eliminates cross-section navigation and presents workflows as coherent journeys from planning through execution and troubleshooting.

### Key Improvements

- **Consolidated evaluation content:** 3 scattered compatibility and assessment sections → 3 unified jobs in the EVALUATE stage (platform compatibility, single-node support, fixed issues review)
- **Unified migration guidance:** Breaking changes, deprecated features, and migration procedures scattered across 3+ sections → 3 consolidated migration jobs with clear migration paths
- **Integrated troubleshooting:** Known issues split across 5 component-specific sections → 1 comprehensive troubleshooting job with 5 focused approaches
- **Pipelines as Code workflow consolidation:** 11 separate PAC features across multiple sections → 4 cohesive jobs covering integration, dynamic configuration, concurrency, and secrets
- **Reduced navigation complexity:** From 9 top-level sections requiring cross-referencing → 15 goal-oriented jobs organized by 6 workflow stages
- **Enhanced fixed issues discoverability:** Generic "Fixed Issues" section → Component-specific user stories nested under evaluation jobs for targeted issue review
- **Workflow-stage visibility:** No explicit workflow guidance → Clear stage-based navigation (EVALUATE → USE → OPTIMIZE → MIGRATE → TROUBLESHOOT → PLAN)
- **Eliminated redundant browsing:** Users currently check 3-4 sections for migration tasks → All migration content unified under MIGRATE stage with clear before/after upgrade guidance

---

## Current Structure (Feature-Based)

- **Compatibility and support matrix** — Platform versions, component versions, support status (GA/TP)
- **Release notes for {pipelines-title} 1.20**
  - **New features** (Lines 141-293) — Organized by component
    - FIPS support
    - Pod anti-affinity
    - buildah-ns task
    - Read-only root filesystem
    - Task display names
    - Single-node OpenShift support
    - **Operator** — RBAC and CA bundle control
    - **Pruner** — Event-based pruner in TektonConfig
    - **Triggers** — Optional installation
    - **Results** — Live collection flag, optimization
    - **Pipelines as Code** — JSON webhook support, GitHub logging, autoconfigure options, relative task references, dynamic variables
  - **Breaking changes** (Lines 295-342) — Component-specific
    - Tekton Hub deprecation
    - Git resolver changes
    - Deprecated metrics removal
    - PAC Hub-to-Artifact Hub migration
    - PAC config map variable cleanup
  - **Known issues** (Lines 344-360) — Component-specific
    - Pruner: config map override on upgrade
    - CLI: namespace access failures
    - Cache: permission errors on IBM platforms
    - Chains: pod anti-affinity not applied
    - Hub: version sorting issue
  - **Fixed issues** (Lines 362-448) — Component-specific
    - Pipelines: 13 fixes (RBAC, console, events, resolver, git-clone, etc.)
    - PAC: 11 fixes (logging, CEL errors, comments, Bitbucket, auto-merge)
    - CLI: 5 fixes (panic handling, status colors, deadlock, log prefixes, results logs)
    - Triggers: 1 fix (TriggerGroup data race)
  - **Deprecated features** (Lines 450-456)
    - Results maxRetention parameter
    - Chain command

**Total:** 9 top-level sections organized by component and change category, requiring cross-section navigation for complete workflows.

---

## Proposed JTBD-Based Structure

### Quick Overview

- **Evaluate Platform Readiness**
  - Job 1: Verify Platform Compatibility and Component Versions
  - Job 5: Deploy on Single-Node OpenShift
  - Job 11: Review Fixed Issues
- **Use Core Features**
  - Job 2: Enable FIPS Mode for Cryptographic Operations
  - Job 3: Configure High Availability for Pipelines Controller
  - Job 4: Build Container Images Without Privileged Access
  - Job 6: Configure and Monitor Pipelines Operator
  - Job 8: Configure Event-Driven Pipelines with Triggers
- **Use Pipelines as Code**
  - Job 8: Configure Dynamic Pipelines with CEL Expressions
  - Job 8: Integrate Pipelines as Code with Source Control
  - Job 15: Manage Secrets Securely in Pipelines as Code
- **Optimize Performance and Resources**
  - Job 7: Automate Resource Cleanup with Pruner
  - Job 14: Control Pipeline Concurrency
  - Job 7: Analyze Pipeline Execution History
- **Migrate from Deprecated Features**
  - Job 9: Migrate from Tekton Hub
  - Job 10: Update Monitoring for Metrics Changes
  - Job 10: Update Pipelines as Code Configurations
- **Troubleshoot Known Issues**
  - Job 13: Troubleshoot Component Issues
- **Plan for Long-Term Strategy**
  - Job 12: Plan Migration from Deprecated Features

### Detailed Job Descriptions

#### Evaluate Platform Readiness

**Job 1: Verify Platform Compatibility and Component Versions**

*When planning to upgrade to OpenShift Pipelines 1.20, I want to verify platform compatibility and component versions, so I can ensure my cluster meets the requirements*

Prerequisites: Access to cluster version information

- **1.1. Review supported OpenShift versions** `[reference]`
  - Compatibility and support matrix (Lines 84-124): Review supported OpenShift 4.x versions and platform support
  - Context: Use before planning an upgrade to confirm cluster compatibility
  
- **1.2. Check component version matrix** `[reference]`
  - Compatibility table (Lines 104-115): Review Pipelines operator 1.20, 1.21, 1.22 component versions and dependencies
  - Context: Use to understand which component versions are bundled and their interdependencies
  
- **1.3. Verify support status (GA/TP)** `[reference]`
  - Support status legend (Lines 96-100): Understand General Availability vs Technology Preview status
  - Tech Preview warnings (Lines 168-181, 193-206): Review limitations of Tech Preview features
  - Context: Use to assess production readiness and support coverage for features you plan to use

**Outcomes:**
- Confirmed compatibility with current cluster version
- Identified supported and preview features
- Understood tech preview limitations and support boundaries

**Related Jobs:** Job 5 (Deploy on Single-Node OpenShift), Job 11 (Review Fixed Issues)

---

**Job 5: Deploy on Single-Node OpenShift**

*When deploying pipelines on edge or resource-constrained environments, I want verified support, so I can run CI/CD workloads on single-node OpenShift*

Prerequisites: Single-node OpenShift cluster

- **5.1. Verify single-node OpenShift compatibility** `[reference]`
  - Single-node support announcement (Lines 159-162): Confirm Tech Preview support status for SNO
  - Hardware requirements (Lines 162-167): Review minimum vCPU, RAM, and disk requirements for libvirt clusters
  - Context: Use before deploying to SNO to understand limitations and minimum resource requirements
  
- **5.2. Deploy pipelines operator on SNO** `[procedure]`
  - Installation context (Lines 160-161): Standard operator installation applies to SNO with noted constraints
  - Context: Use standard installation procedures with awareness of single-node limitations
  
- **5.3. Understand SNO limitations** `[concept]`
  - Limitation statement (Lines 161-162): Review constraints (limited scalability, no redundancy, constrained concurrency)
  - Tech Preview warning (Lines 173-179): Understand that SNO support is not intended for production
  - Context: Use to set appropriate expectations and plan for edge/development use cases

**Outcomes:**
- Confirmed SNO support and hardware requirements
- Understood single-node limitations for production use
- Enabled edge CI/CD scenarios within constraint boundaries

**Related Jobs:** Job 1 (Verify Platform Compatibility)

---

**Job 11: Review Fixed Issues**

*When upgrading to OpenShift Pipelines 1.20, I want to review fixed issues, so I can understand what problems are resolved in this release*

Prerequisites: Knowledge of current environment issues, access to release notes

- **11.1. Review Pipelines core fixes** `[reference]`
  - Fixed issues section (Lines 364-409): Review 13 fixes including RBAC enforcement, console display, event handling, resolver improvements, and git-clone fixes
  - Context: Use to identify fixes for pipeline execution, UI, and git resolver issues experienced in prior versions
  
- **11.2. Review Pipelines as Code fixes** `[reference]`
  - PAC fixed issues (Lines 411-434): Review 11 fixes including structured logging, CEL error handling, GitHub comment control, Bitbucket payload handling, and auto-merge blocking
  - Context: Use to determine if PAC-specific issues you've experienced are resolved
  
- **11.3. Review CLI fixes** `[reference]`
  - CLI fixed issues (Lines 436-445): Review 5 fixes including panic prevention, status color correction, deadlock resolution, log prefix improvements, and Results log querying
  - Context: Use to understand CLI reliability and usability improvements
  
- **11.4. Review Triggers and other component fixes** `[reference]`
  - Triggers fixes (Lines 447-448): TriggerGroup data race and controller panic fix
  - Context: Use when experiencing trigger-related reliability issues

**Outcomes:**
- Understanding of resolved problems across all components
- Confidence in upgrade decision based on relevant fixes
- Validated that critical bugs affecting current environment are addressed

**Related Jobs:** Job 1 (Verify Platform Compatibility), Job 13 (Troubleshoot Component Issues)

---

#### Use Core Features

**Job 2: Enable FIPS Mode for Cryptographic Operations**

*When running pipelines in regulated environments, I want to enable FIPS mode for cryptographic operations, so I can meet compliance requirements*

Prerequisites: OpenShift 4.x cluster, security compliance requirements

- **2.1. Understand FIPS support in OpenShift Pipelines** `[concept]`
  - FIPS mode support announcement (Lines 145-146): Understand that Pipelines 1.20 is designed for FIPS-enabled environments
  - Context: Use when evaluating compliance capabilities before enabling FIPS cluster-wide
  
- **2.2. Enable FIPS mode on OpenShift cluster** `[procedure]`
  - FIPS installation reference (Line 146): Link to OpenShift FIPS cryptography support documentation
  - Context: Follow linked procedure to enable FIPS at the cluster level as prerequisite
  
- **2.3. Verify FIPS compliance in pipeline execution** `[procedure]`
  - Implicit verification: After cluster FIPS enablement, pipelines automatically use FIPS-compliant cryptography
  - Context: Use to validate that pipeline cryptographic operations meet compliance requirements

**Outcomes:**
- FIPS-compliant pipeline execution
- Met regulatory requirements for cryptographic operations
- Reduced compliance risk in regulated environments

**Pain Points:** FIPS mode configuration complexity at cluster level

**Related Jobs:** Job 15 (Manage Secrets Securely), Job 13 (Troubleshoot Chains Attestation Failures)

---

**Job 3: Configure High Availability for Pipelines Controller**

*When deploying pipelines controller in production, I want to configure pod anti-affinity, so I can ensure high availability across nodes*

Prerequisites: Multi-node cluster, understanding of Kubernetes scheduling

- **3.1. Understand automatic pod anti-affinity configuration** `[concept]`
  - Pod anti-affinity announcement (Lines 148-150): Review automatic application of `preferredDuringSchedulingIgnoredDuringExecution` rule to controller replicas
  - Context: Use to understand that HA setup is automatic in 1.20 with no additional configuration required
  
- **3.2. Verify high availability deployment** `[procedure]`
  - Validation approach (Line 150): Verify that controller replicas are distributed across different nodes
  - Context: Use after installation to confirm proper replica distribution

**Outcomes:**
- High availability controller deployment without manual configuration
- Reduced single point of failure risk
- Improved resiliency, load balancing, and availability

**Known Issues:** Pod anti-affinity rules are NOT applied to tekton-chains-controller replicas (Line 356-357)

**Related Jobs:** Job 6 (Configure and Monitor Pipelines Operator)

---

**Job 4: Build Container Images Without Privileged Access**

*When building container images in pipelines without privileged access, I want to use the buildah-ns task, so I can build images securely in rootless mode*

Prerequisites: Understanding of rootless containers, pipeline task knowledge

- **4.1. Understand buildah-ns security improvements** `[concept]`
  - buildah-ns announcement (Lines 151-153): Review user namespace isolation and compatibility with existing buildah task
  - Context: Use when planning to migrate from privileged buildah to secure rootless builds
  
- **4.2. Replace buildah task with buildah-ns** `[procedure]`
  - Migration guidance (Line 152): Replace existing buildah task references with buildah-ns in pipeline definitions
  - Additional resources reference (Line 462): Review differences between buildah and buildah-ns tasks
  - Context: Use when updating existing pipelines to use rootless container builds
  
- **4.3. Handle BUILD_ARGS parameter correctly** `[reference]`
  - Fixed issue (Lines 407-409): Understand that default `BUILD_ARGS` value `[""]` is now supported in pipeline builder UI
  - Context: Use when configuring buildah-ns parameters to avoid validation errors

**Outcomes:**
- Secure rootless image builds
- Reduced security risk from privileged containers
- Maintained compatibility with existing buildah workflows

**Pain Points:** Migration from privileged buildah task requires understanding of rootless constraints

**Related Jobs:** Job 6 (Configure and Monitor Pipelines Operator)

---

**Job 6: Configure and Monitor Pipelines Operator**

*When managing pipelines operator, I want to understand new configuration options and status conditions, so I can monitor and configure the operator effectively*

Prerequisites: Operator management experience, access to TektonConfig CR

- **6.1. Configure RBAC and CA bundle creation control** `[procedure]`
  - RBAC and CA bundle control (Lines 185-187): Configure independent control of RBAC resource and Trusted CA bundle config map creation in TektonConfig CR
  - Context: Use when you need to manage RBAC separately or avoid resource duplication in your environment
  
- **6.2. Configure Triggers installation** `[procedure]`
  - Optional Triggers installation (Lines 210-223): Disable Tekton Triggers installation in TektonConfig CR using `spec.trigger.disabled: true`
  - Context: Use when Triggers are managed independently or not needed in your deployment
  
- **6.3. Monitor operator health and status** `[procedure]`
  - Operator enhancements context (Line 184): Review operator status conditions for monitoring
  - Context: Use for ongoing operator health monitoring and troubleshooting

**Outcomes:**
- Optimized operator configuration for environment needs
- Better monitoring of operator state
- Improved flexibility to fit specific RBAC and certificate management requirements

**Related Jobs:** Job 3 (Configure High Availability), Job 7 (Automate Resource Cleanup)

---

**Job 8: Configure Event-Driven Pipelines with Triggers**

*When processing webhook events, I want to use core interceptors for filtering and transformation, so I can route events to appropriate pipelines*

Prerequisites: Understanding of webhook payloads, EventListener configuration knowledge

- **8.1. Understand Triggers optional installation** `[concept]`
  - Optional installation (Lines 210-223): Understand that Triggers can be disabled if managed independently
  - Context: Use when evaluating whether to install Triggers component
  
- **8.2. Configure interceptors for event filtering** `[procedure]`
  - Implicit guidance: Configure CEL, GitHub, GitLab, and Bitbucket interceptors for webhook processing
  - TriggerGroup fix (Lines 447-448): Benefit from data race fix for TriggerGroups with many triggers
  - Context: Use when setting up EventListener with multiple trigger types
  
- **8.3. Test and troubleshoot event routing** `[procedure]`
  - Fixed interceptor behavior (Line 447): Verify that TriggerGroups with many triggers work reliably
  - Context: Use after configuring triggers to validate event routing accuracy

**Outcomes:**
- Accurate event routing to appropriate pipelines
- Reduced unnecessary pipeline runs through proper filtering
- Improved pipeline trigger accuracy and reliability

**Related Jobs:** Job 8 (Configure Dynamic Pipelines with CEL Expressions), Job 14 (Control Pipeline Concurrency)

---

#### Use Pipelines as Code

**Job 8: Configure Dynamic Pipelines with CEL Expressions**

*When configuring Pipelines as Code, I want to use CEL expressions for dynamic configurations, so I can create flexible event-driven workflows*

Prerequisites: Understanding of CEL syntax, PAC configuration knowledge, webhook event structure knowledge

- **8.1. Write and test CEL expressions** `[procedure]`
  - CEL error handling fix (Lines 413-414): Benefit from error comments posted on pull requests for invalid CEL expressions
  - Context: Use when creating dynamic parameter resolution and event filtering logic
  
- **8.2. Debug CEL evaluation errors** `[procedure]`
  - Invalid CEL expression handling (Lines 413-414): Review error comments posted on PRs for troubleshooting
  - Context: Use when CEL expressions fail to help identify syntax or logic errors

**Outcomes:**
- Dynamic pipeline configurations driven by event data
- Reduced pipeline duplication through parameterization
- More flexible event handling with clearer error feedback

**Pain Points:** CEL syntax learning curve, but improved by error comment feedback

**Related Jobs:** Job 8 (Configure Event-Driven Pipelines with Triggers), Job 15 (Manage Secrets Securely)

---

**Job 8: Integrate Pipelines as Code with Source Control**

*When automating CI/CD from multiple SCM platforms, I want Pipelines as Code to support multiple source control systems, so I can unify pipeline experience*

Prerequisites: SCM platform access (GitHub, GitLab, or Bitbucket), PAC operator installed, webhook configuration permissions

- **8.1. Configure GitHub integration with Apps** `[procedure]`
  - GitHub Apps context: Implicit support for GitHub Apps integration
  - Context: Use for improved security with fine-grained permissions over OAuth apps
  
- **8.2. Configure GitLab workflows** `[procedure]`
  - GitLab fixes (Lines 411-412, 433-434): Benefit from improved structured logging with source repository details and fixed auto-merge blocking
  - Context: Use when setting up GitLab merge request triggers and approval workflows
  
- **8.3. Configure Bitbucket integration** `[procedure]`
  - Bitbucket empty commit fix (Lines 429-430): Benefit from crash prevention when processing empty commits
  - Context: Use when setting up Bitbucket Server or Cloud webhook integration
  
- **8.4. Use incoming webhooks with JSON body** `[procedure]`
  - JSON body support (Lines 254-264): Configure incoming webhooks using POST JSON body for improved security
  - Context: Use for incoming webhook endpoints to reduce sensitive information exposure in logs
  
- **8.5. Customize GitHub comment behavior** `[procedure]`
  - Comment strategy control (Lines 415-425): Disable status comments in Repository CR using `spec.settings.github.comment_strategy: "disable_all"`
  - PipelineRun console link (Lines 427-428): Benefit from direct console links in starting comments
  - Context: Use to reduce comment noise or customize PR status reporting
  
- **8.6. Use autoconfigure with repository templates** `[procedure]`
  - Autoconfigure repository template (Lines 269-271): Use `auto-configure-repo-repository-template` setting to combine repositories in single namespace
  - Context: Use when managing many repositories with PAC to streamline namespace management
  
- **8.7. Reference tasks relatively in remote pipelines** `[procedure]`
  - Relative task references (Lines 272-274, 275-288): Use relative paths in remote Pipeline definitions with Tech Preview status
  - Context: Use when organizing tasks with remote pipeline definitions for improved portability
  
- **8.8. Use dynamic pull request variables** `[procedure]`
  - pull_request_number variable (Lines 290-292): Access dynamic `pull_request_number` variable in push events
  - Context: Use to track which pull request triggered a push event for improved traceability
  
- **8.9. Enable detailed GitHub API logging** `[procedure]`
  - GitHub API logging (Lines 266-268): Set controller log level to 'debug' for detailed GitHub API call insights
  - Context: Use when troubleshooting complex GitHub integration issues to understand API interactions and rate limiting

**Outcomes:**
- Automated CI/CD from GitHub, GitLab, and Bitbucket
- Multi-SCM support with unified pipeline experience
- Improved security, traceability, and troubleshooting capabilities

**Pain Points:** GitHub App creation and setup complexity, but mitigated by detailed logging

**Related Jobs:** Job 2 (Enable FIPS Mode), Job 15 (Manage Secrets Securely)

---

**Job 15: Manage Secrets Securely in Pipelines as Code**

*When injecting secrets into pipeline runs, I want to use PAC secret injection features, so I can securely provide credentials without exposing them in code*

Prerequisites: Kubernetes secret management, PAC configuration knowledge, security best practices

- **15.1. Configure secret annotation in PAC** `[procedure]`
  - Implicit guidance: Use PAC secret injection annotations to map secrets to pipeline parameters
  - Context: Use when pipelines require credentials or sensitive configuration
  
- **15.2. Verify secret injection in TaskRuns** `[procedure]`
  - Implicit validation: Confirm that secrets are properly injected and available in TaskRuns
  - Context: Use after configuring secret annotations to validate availability
  
- **15.3. Audit secret access patterns** `[procedure]`
  - Implicit guidance: Review which pipelines access which secrets for security audit
  - Context: Use periodically to ensure secret access follows least-privilege principles

**Outcomes:**
- Secure credential management in pipelines
- No secrets exposed in source code or pipeline definitions
- Controlled secret access with audit trail

**Related Jobs:** Job 2 (Enable FIPS Mode), Job 8 (Configure Dynamic Pipelines with CEL Expressions)

---

#### Optimize Performance and Resources

**Job 7: Automate Resource Cleanup with Pruner**

*When managing pipeline resources at scale, I want to configure automated pruning with cron schedules, so I can maintain cluster health without manual intervention*

Prerequisites: Understanding of cron syntax, cluster resource monitoring

- **7.1. Enable event-based pruner in TektonConfig** `[procedure]`
  - Event-based pruner configuration (Lines 190-192, 465-466): Enable and configure tektonpruner in TektonConfig CR with Tech Preview status
  - Context: Use to enable automated event-based resource cleanup beyond simple retention policies
  
- **7.2. Monitor pruner execution and metrics** `[procedure]`
  - Pruner observability (Line 191): Review new pruner-specific metrics for monitoring
  - Context: Use to track pruner job execution and effectiveness

**Outcomes:**
- Automated resource cleanup
- Reduced manual maintenance effort
- Optimized cluster resource usage with improved observability

**Pain Points:** Determining optimal pruning schedule and retention policies

**Known Issues:** After upgrading from 1.19 to 1.20, tekton-pruner-default-spec config map values are overridden (Lines 346-348)

**Related Jobs:** Job 13 (Troubleshoot Pruner Failures), Job 14 (Control Pipeline Concurrency)

---

**Job 14: Control Pipeline Concurrency**

*When managing multiple pipeline runs from rapid commits, I want to control concurrency, so I can optimize resource usage and pipeline throughput*

Prerequisites: Understanding of pipeline resource requirements, PAC configuration access

- **14.1. Configure concurrency settings** `[procedure]`
  - Implicit guidance: Use PAC annotations to control max-concurrent-runs and concurrency strategy
  - Context: Use when rapid commits cause resource contention or queue buildup
  
- **14.2. Monitor pipeline queue behavior** `[procedure]`
  - Implicit guidance: Track pipeline queue and execution patterns to optimize concurrency limits
  - Context: Use to adjust concurrency based on cluster capacity and pipeline resource needs

**Outcomes:**
- Optimized cluster resource usage
- Reduced pipeline queue times
- Better handling of rapid commits without overwhelming cluster

**Pain Points:** Determining optimal concurrency limits for specific workloads

**Related Jobs:** Job 7 (Automate Resource Cleanup), Job 8 (Configure Event-Driven Pipelines)

---

**Job 7: Analyze Pipeline Execution History**

*When analyzing pipeline execution history, I want to query results through the API, so I can build custom dashboards and reports*

Prerequisites: API client knowledge, understanding of Tekton results data model

- **7.1. Configure Results live collection behavior** `[procedure]`
  - Live collection flag (Lines 227-247): Configure `--disable_storing_incomplete_runs` flag in TektonConfig to control when runs are stored
  - Context: Use to improve system performance by storing runs only when complete, or maintain live upserts for real-time monitoring
  
- **7.2. Optimize Results processing** `[concept]`
  - PipelineRun skip optimization (Lines 249-251): Benefit from automatic skipping of already-stored PipelineRuns to reduce API calls
  - Context: Understand performance improvements in Results processing
  
- **7.3. Query Results API for analytics** `[procedure]`
  - Results log querying fix (Lines 444-445): Benefit from clearer error messages when querying logs for running PipelineRuns
  - Context: Use to build custom dashboards with appropriate handling of in-progress runs
  
- **7.4. Implement result retention policies** `[procedure]`
  - maxRetention deprecation (Line 453): Use `defaultRetention` parameter instead of deprecated `maxRetention`
  - Context: Use to manage Results data volume and storage costs

**Outcomes:**
- Custom pipeline analytics and dashboards
- Historical execution insights for optimization
- Data-driven pipeline optimization decisions

**Pain Points:** Complex API queries, result data volume management

**Related Jobs:** Job 6 (Configure and Monitor Pipelines Operator)

---

#### Migrate from Deprecated Features

**Job 9: Migrate from Tekton Hub**

*When Tekton Hub is deprecated, I want to migrate to alternative task catalogs, so I can continue using community tasks in my pipelines*

Prerequisites: Inventory of Hub-dependent pipelines, understanding of task bundle format

- **9.1. Understand Tekton Hub deprecation** `[concept]`
  - Hub deprecation announcement (Lines 297-299): Review deprecation of public hub.tekton.dev instance and git resolver changes
  - Hub version sorting issue (Lines 358-360): Understand known issue with lexicographic version sorting
  - Context: Use to understand deprecation scope and timeline before beginning migration
  
- **9.2. Migrate from Hub to Artifact Hub** `[procedure]`
  - Automatic PAC migration (Lines 333-341): Understand automatic migration from Tekton Hub to Artifact Hub in PAC
  - Version pin format update (Lines 334-335): Update short version pins (e.g., `0.2`) to full semantic version (e.g., `0.2.0`)
  - hub_catalog_name cleanup (Lines 336-341): Remove `hub-catalog-name` variable from PAC config map after upgrade
  - Context: Use immediately after upgrading to 1.20 to complete PAC migration to Artifact Hub
  
- **9.3. Update pipeline builder task references** `[procedure]`
  - Pipeline builder fix (Lines 371-372): Benefit from complete Artifact Hub task list fetching in pipeline builder
  - Context: Use pipeline builder to access full Artifact Hub task catalog when creating pipelines
  
- **9.4. Test migrated pipelines** `[procedure]`
  - Implicit validation: Test all migrated pipelines to ensure task resolution works correctly
  - Context: Use after migration to validate that all task references resolve from Artifact Hub

**Outcomes:**
- Removed Tekton Hub dependency
- Migrated to supported Artifact Hub task sources
- Future-proof pipeline definitions

**Pain Points:** Large number of pipelines to migrate, finding equivalent tasks with correct version format

**Related Jobs:** Job 12 (Plan Migration from Deprecated Features)

---

**Job 10: Update Monitoring for Metrics Changes**

*When metrics names change in 1.20, I want to update my monitoring dashboards and alerts, so I can continue tracking pipeline performance*

Prerequisites: Access to monitoring configuration, understanding of Prometheus metrics, list of affected metrics

- **10.1. Understand metrics breaking changes** `[concept]`
  - Metrics deprecation (Lines 301-330): Review table of deprecated metrics and their replacements
  - Context: Use to understand scope of metric name changes before planning dashboard updates
  
- **10.2. Update Prometheus queries with new metric names** `[procedure]`
  - Metric mapping (Lines 304-330): Replace deprecated metrics in queries:
    - `pipelinerun_count` → `pipelinerun_total`
    - `running_pipelineruns_count` → `running_pipelineruns`
    - `running_pipelineruns_waiting_on_pipeline_resolution_count` → `running_pipelineruns_waiting_on_pipeline_resolution`
    - `running_pipelineruns_waiting_on_task_resolution_count` → `running_pipelineruns_waiting_on_task_resolution`
    - `taskrun_count` → `taskrun_total`
    - `running_taskruns_count` → `running_taskruns`
    - `running_taskruns_throttled_by_quota_count` → `running_taskruns_throttled_by_quota`
    - `running_taskruns_throttled_by_node_count` → `running_taskruns_throttled_by_node`
  - Context: Use to update all Prometheus queries in dashboards and alert rules
  
- **10.3. Test updated dashboards and alerts** `[procedure]`
  - Implicit validation: Verify that dashboards display metrics correctly and alerts fire as expected
  - Context: Use after updating queries to validate monitoring functionality

**Outcomes:**
- Updated monitoring dashboards with correct metrics
- Accurate pipeline metrics tracking
- No broken alerts due to metric name changes

**Pain Points:** Finding all metric references across multiple monitoring tools and dashboards

**Related Jobs:** Job 7 (Analyze Pipeline Execution History)

---

**Job 10: Update Pipelines as Code Configurations**

*When PAC configuration options change, I want to update my configurations to use new settings, so I can avoid deprecated options and use supported features*

Prerequisites: Access to PAC configurations, understanding of PAC configuration model

- **10.1. Clean up hub_catalog_name from PAC config map** `[procedure]`
  - Config map cleanup (Lines 336-341): Remove `hub-catalog-name` variable from pipelines-as-code config map using `oc patch`
  - Context: Use immediately after upgrading to 1.20 to ensure correct Artifact Hub catalog usage
  
- **10.2. Update PipelineRun annotations** `[procedure]`
  - PipelineRun annotation fix (Lines 431-432): Benefit from proper annotation on status change for external controller modifications
  - Context: Understand that PipelineRun annotation handling is now more consistent
  
- **10.3. Test PAC configurations in dev environment** `[procedure]`
  - Implicit validation: Test updated configurations in non-production environment before rollout
  - Context: Use to validate configuration changes work as expected

**Outcomes:**
- Modernized PAC configurations aligned with 1.20
- Removed deprecated settings
- Improved maintainability and consistency

**Pain Points:** Multiple configuration locations to update across repositories

**Related Jobs:** Job 8 (Configure Dynamic Pipelines with CEL), Job 9 (Migrate from Tekton Hub)

---

#### Troubleshoot Known Issues

**Job 13: Troubleshoot Component Issues**

*When encountering component failures or unexpected behavior, I want to identify known issues and workarounds, so I can resolve problems and maintain pipeline operations*

Prerequisites: Access to operator and component logs, component configuration knowledge

- **13.1. Troubleshoot pruner issues** `[reference]`
  - Pruner config map override (Lines 346-348): Keep copy of tekton-pruner-default-spec config map before upgrade and reapply to TektonConfig after upgrade
  - Context: Use when pruner configuration is lost after upgrading from 1.19 to 1.20
  
- **13.2. Troubleshoot CLI issues** `[reference]`
  - CLI namespace access failure (Lines 349-351): Known issue with `opc pr logs` in OpenShift namespace causing repeated errors
  - CLI panic fix (Lines 436-437): Benefit from fixed panic when reading logs from deleted pods
  - CLI deadlock fix (Lines 440-441): Benefit from resolved deadlock in log following functionality
  - Context: Use when experiencing CLI command failures or unexpected behavior
  
- **13.3. Troubleshoot cache issues** `[reference]`
  - Cache permission errors (Lines 352-354): Known issue with `cache-fetch` step on IBM P and zSystems failing with permission errors
  - Context: Use when cache operations fail on IBM platforms due to filesystem permission restrictions
  
- **13.4. Troubleshoot Chains attestation issues** `[reference]`
  - Chains pod anti-affinity (Lines 355-357): Known issue that pod anti-affinity rules are NOT applied to tekton-chains-controller replicas
  - Context: Use when planning HA deployment to understand Chains controller limitation
  
- **13.5. Troubleshoot Hub task resolution** `[reference]`
  - Hub version sorting (Lines 358-360): Known issue with git-clone task showing version 0.9 instead of 0.10 due to lexicographic sorting
  - Context: Use when task versions appear incorrect in Tekton Hub

**Outcomes:**
- Resolved known issues using documented workarounds
- Continued pipeline operations despite known limitations
- Reduced manual intervention through awareness of known issues

**Pain Points:** Component-specific issues requiring different troubleshooting approaches

**Related Jobs:** Job 7 (Automate Resource Cleanup), Job 11 (Review Fixed Issues)

---

#### Plan for Long-Term Strategy

**Job 12: Plan Migration from Deprecated Features**

*When planning long-term pipeline strategy, I want to identify deprecated features, so I can plan migrations before features are removed*

Prerequisites: Inventory of current pipeline configurations, understanding of deprecation timeline

- **12.1. Review deprecated features list** `[reference]`
  - Deprecated features (Lines 450-456): Review maxRetention parameter deprecation and chain command deprecation
  - Context: Use to identify features that will be removed in future releases
  
- **12.2. Plan Tekton Hub migration** `[concept]`
  - Hub deprecation (Lines 297-299): Understand that Tekton Hub deprecation in 1.20 requires migration planning
  - Context: Use to plan timeline for migrating all Hub-dependent pipelines to Artifact Hub
  
- **12.3. Plan metrics dashboard updates** `[concept]`
  - Metrics deprecation (Lines 301-330): Understand that deprecated metrics are removed in 1.20, not just deprecated
  - Context: Use to plan dashboard and alert updates before upgrading
  
- **12.4. Test alternative approaches for deprecated features** `[procedure]`
  - Implicit validation: Test replacement features in dev environment before production migration
  - Context: Use to validate that replacements meet functionality requirements

**Outcomes:**
- Migration plan for deprecated features with clear timeline
- Avoided future breaking changes through proactive adoption
- Tested and validated replacement features

**Pain Points:** Short deprecation windows require quick migration planning and execution

**Related Jobs:** Job 9 (Migrate from Tekton Hub), Job 10 (Update Monitoring for Metrics Changes)

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | Component and change category (New Features → Operator → Pruner → Triggers → Results → PAC, then Breaking Changes, Known Issues, Fixed Issues, Deprecated Features) | User goals and workflow stages (Evaluate → Use → Optimize → Migrate → Troubleshoot → Plan) |
| **Top-level items** | 9 sections (Compatibility, New Features with 5 component subsections, Breaking Changes, Known Issues with 5 component subsections, Fixed Issues with 4 component subsections, Deprecated Features) | 15 main jobs organized under 6 workflow stages |
| **Migration content** | Scattered across Breaking Changes (3 items), Deprecated Features (2 items), and implicit guidance in New Features | Unified MIGRATE stage with 3 jobs covering Hub migration, metrics updates, and PAC config changes |
| **Troubleshooting content** | Split into 5 component-specific Known Issues subsections (Pruner, CLI, Cache, Chains, Hub) | 1 comprehensive troubleshooting job with 5 focused approaches organized by component |
| **PAC content** | 11 separate feature announcements across New Features, Breaking Changes, Known Issues, Fixed Issues | 4 cohesive jobs covering integration (8 approaches), dynamic configuration, concurrency, and secrets |
| **Fixed issues visibility** | Generic "Fixed Issues" section with 4 component subsections requiring scanning for relevance | Component-specific user stories nested under Job 11 (Review Fixed Issues) for targeted review |
| **Evaluation flow** | Compatibility section separate from release notes; no clear upgrade evaluation guidance | 3 evaluation jobs providing complete upgrade assessment (compatibility, SNO support, fixed issues) |
| **Workflow stage visibility** | No explicit workflow stages; users infer from section names | Clear stage-based navigation with 6 defined stages matching user mental models |
| **Cross-section navigation** | Required for complete workflows (e.g., PAC setup requires reading New Features → Breaking Changes → Known Issues → Fixed Issues) | Single job provides all approaches needed for complete workflow |
| **Content density per section** | High (e.g., New Features section spans 152 lines covering 15+ features across 5 components) | Moderate (jobs focused on single goal with 2-8 approaches) |

### Job List Adjustments from Suggested Input

The suggested 31 JSONL records were consolidated to **15 main jobs** for the following reasons:

1. **User story records 26-31 (6 records) absorbed into parent Job 11 (Review Fixed Issues)** → These represented specific fixed issues (RBAC, timeouts, PAC status, GitLab, CLI commands, trigger filtering) that serve the parent job of reviewing all fixed issues. They are now approaches under Job 11 rather than standalone jobs.

2. **Job 8 appears 3 times (PAC CEL expressions, PAC integrations, Triggers)** → These represent different facets of event-driven pipeline configuration. Job 8 "Configure Event-Driven Pipelines" covers Triggers, while "Configure Dynamic Pipelines with CEL Expressions" and "Integrate Pipelines as Code with Source Control" are separate PAC-focused jobs under "Use Pipelines as Code" stage.

3. **Job 7 appears 2 times (Pruner, Results API)** → These represent different optimization jobs: "Automate Resource Cleanup with Pruner" and "Analyze Pipeline Execution History" are both optimization activities but serve different goals.

4. **Job 10 appears 2 times (Metrics migration, PAC config migration)** → These are separate migration jobs: "Update Monitoring for Metrics Changes" and "Update Pipelines as Code Configurations" both belong to MIGRATE stage but address different breaking changes.

5. **Job 13 consolidates 5 troubleshooting areas (Pruner, CLI, Cache, Chains, Hub)** → Rather than 5 separate jobs, these are 5 approaches under a single "Troubleshoot Component Issues" job since users encountering issues need comprehensive troubleshooting guidance, not siloed component views.

**Rationale:** The consolidation reduces redundancy while preserving all content from the source document. User stories (26-31) are implementation details of the broader evaluation job. Multiple appearances of job numbers (7, 8, 10, 13) represent either genuinely distinct goals or consolidation of related troubleshooting content into a comprehensive job structure.

---

## Consolidation Examples

### Example 1: Pipelines as Code Workflow (11 scattered features → 3 unified jobs)

**Current (Fragmented):**
- New Features → PAC: JSON body support (Lines 254-264)
- New Features → PAC: GitHub API logging (Lines 266-268)
- New Features → PAC: Autoconfigure repository template (Lines 269-271)
- New Features → PAC: Relative task references (Lines 272-288)
- New Features → PAC: Dynamic pull_request_number variable (Lines 290-292)
- Breaking Changes → PAC: Hub to Artifact Hub migration (Lines 333-341)
- Fixed Issues → PAC: 11 separate fixes (Lines 411-434)

Users must scan 3 major sections and 18+ individual items to understand complete PAC capabilities and migration requirements.

**Proposed (Consolidated):**
- **Job 8: Configure Dynamic Pipelines with CEL Expressions**
  - 8.1. Write and test CEL expressions (includes error handling fix)
  - 8.2. Debug CEL evaluation errors
- **Job 8: Integrate Pipelines as Code with Source Control**
  - 8.1. Configure GitHub integration with Apps
  - 8.2. Configure GitLab workflows (includes fixes)
  - 8.3. Configure Bitbucket integration (includes fix)
  - 8.4. Use incoming webhooks with JSON body
  - 8.5. Customize GitHub comment behavior (includes fixes)
  - 8.6. Use autoconfigure with repository templates
  - 8.7. Reference tasks relatively in remote pipelines
  - 8.8. Use dynamic pull request variables
  - 8.9. Enable detailed GitHub API logging
- **Job 10: Update Pipelines as Code Configurations**
  - 10.1. Clean up hub_catalog_name from PAC config map
  - 10.2. Update PipelineRun annotations
  - 10.3. Test PAC configurations

**Benefit:** 78% reduction in navigation complexity—from 18 scattered items across 3 sections to 3 focused jobs (14 approaches total) organized by workflow intent (configure, integrate, migrate).

---

### Example 2: Migration Guidance (5 scattered breaking changes → 3 unified migration jobs)

**Current (Fragmented):**
- Breaking Changes: Tekton Hub deprecation (Lines 297-299)
- Breaking Changes: Git resolver changes (Line 300)
- Breaking Changes: Deprecated metrics removal with 8-row table (Lines 301-330)
- Breaking Changes → PAC: Hub-to-Artifact Hub migration (Lines 333-335)
- Breaking Changes → PAC: hub_catalog_name cleanup (Lines 336-341)
- Deprecated Features: maxRetention parameter (Line 453)
- Deprecated Features: chain command (Line 455)

Users must piece together migration tasks from Breaking Changes and Deprecated Features sections, with no clear upgrade workflow.

**Proposed (Consolidated):**
- **Job 9: Migrate from Tekton Hub**
  - 9.1. Understand Tekton Hub deprecation
  - 9.2. Migrate from Hub to Artifact Hub (includes PAC migration steps)
  - 9.3. Update pipeline builder task references
  - 9.4. Test migrated pipelines
- **Job 10: Update Monitoring for Metrics Changes**
  - 10.1. Understand metrics breaking changes
  - 10.2. Update Prometheus queries with new metric names (includes 8 mappings)
  - 10.3. Test updated dashboards and alerts
- **Job 10: Update Pipelines as Code Configurations**
  - 10.1. Clean up hub_catalog_name from PAC config map
  - 10.2. Update PipelineRun annotations
  - 10.3. Test PAC configurations

**Benefit:** Clear migration workflow—from scattered breaking changes requiring cross-section inference to 3 complete migration jobs with explicit before/after upgrade guidance and testing steps.

---

### Example 3: Troubleshooting (5 component silos → 1 comprehensive job)

**Current (Fragmented):**
- Known Issues → Pruner: config map override (Lines 346-348)
- Known Issues → CLI: namespace access failures (Lines 349-351)
- Known Issues → Cache: permission errors (Lines 352-354)
- Known Issues → Chains: pod anti-affinity not applied (Lines 355-357)
- Known Issues → Hub: version sorting issue (Lines 358-360)

Users experiencing multiple issues must scan 5 separate component subsections with no cross-component context.

**Proposed (Consolidated):**
- **Job 13: Troubleshoot Component Issues**
  - 13.1. Troubleshoot pruner issues (includes config map workaround)
  - 13.2. Troubleshoot CLI issues (includes 3 related fixes)
  - 13.3. Troubleshoot cache issues (includes platform-specific guidance)
  - 13.4. Troubleshoot Chains attestation issues (includes HA limitation)
  - 13.5. Troubleshoot Hub task resolution (includes version sorting workaround)

**Benefit:** Unified troubleshooting entry point—from 5 scattered component subsections to 1 job with 5 approaches, enabling cross-component issue diagnosis and resolution.

---

## Content Gaps Identified

| Gap | JTBD Reference | Current Coverage | Impact |
|-----|---------------|-----------------|--------|
| Step-by-step upgrade procedure from 1.19 to 1.20 | Job 1 (Verify Platform Compatibility) | Only compatibility matrix and component versions; no upgrade steps | **High** — Users have no guidance for executing the upgrade safely, likely causing support tickets for upgrade failures or data loss |
| Pre-upgrade checklist and validation | Job 1, Job 12 (Plan Migration) | Implicit requirements scattered across Breaking Changes; no consolidated checklist | **High** — Users may upgrade without completing required migrations (Hub, metrics, PAC config), causing runtime failures |
| Rollback procedures if upgrade fails | None | No coverage | **High** — Users cannot recover from failed upgrades, risking prolonged downtime |
| FIPS verification procedures | Job 2 (Enable FIPS Mode) | Announcement of FIPS support but no verification steps or validation guidance | **Medium** — Users cannot confirm FIPS compliance, potentially failing audits despite feature enablement |
| Performance tuning guidance for operator settings | Job 6 (Configure Pipelines Operator) | Mention of performance tuning options but no guidance on what to tune or when | **Medium** — Users cannot optimize operator performance based on cluster size or workload patterns |
| Pruner schedule and retention best practices | Job 7 (Automate Resource Cleanup) | Configuration options available but no guidance on schedule optimization | **Medium** — Users may configure inefficient pruning schedules, causing resource buildup or excessive cluster load |
| PAC concurrency limit calculation guidance | Job 14 (Control Pipeline Concurrency) | Concurrency control feature mentioned but no formula or guidance for setting limits | **Medium** — Users cannot determine appropriate concurrency limits, risking resource exhaustion or underutilization |
| Results API query examples and patterns | Job 7 (Analyze Pipeline Execution History) | API configuration covered but no query examples or common patterns | **Medium** — Users cannot leverage Results API effectively without example queries |
| Monitoring dashboard examples for new metrics | Job 10 (Update Monitoring for Metrics Changes) | Metric name mappings provided but no dashboard examples or alert rule templates | **Low** — Users must recreate dashboards from scratch rather than adapting provided templates |
| buildah-ns migration checklist | Job 4 (Build Container Images Without Privileged Access) | Feature announcement and compatibility note but no detailed migration steps or compatibility matrix | **Low** — Users may encounter unexpected differences when migrating from buildah to buildah-ns |
| Single-node OpenShift deployment sizing guidance | Job 5 (Deploy on Single-Node OpenShift) | Minimum hardware requirements for libvirt but no guidance for other platforms or workload sizing | **Low** — Users on non-libvirt platforms cannot determine appropriate SNO sizing |
| Component-specific log analysis procedures | Job 13 (Troubleshoot Component Issues) | Known issues listed but no guidance on reading logs to diagnose unlisted issues | **Low** — Users can only troubleshoot documented issues; new issues require support escalation |

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 9 sections (Compatibility, New Features, Breaking Changes, Known Issues, Fixed Issues, Deprecated Features, + 3 nested levels) | 6 workflow stages containing 15 jobs | ~33% reduction in top-level complexity |
| Sections to browse for "setting up PAC with GitHub" | 3 sections (New Features → PAC, Breaking Changes → PAC, Fixed Issues → PAC) across ~90 lines | 1 job (Job 8: Integrate PAC with Source Control), 9 approaches | ~67% reduction in sections to browse |
| Sections to browse for "migration before upgrade" | 2 sections (Breaking Changes with 5 items, Deprecated Features with 2 items) | 2 jobs under MIGRATE stage (Jobs 9, 10 with 7 total approaches) | Same section count but clearer workflow structure with explicit upgrade timing |
| Sections to browse for "troubleshooting pruner issues" | 2 sections (Known Issues → Pruner for current issue, Fixed Issues → Pipelines for historical fixes) | 1 job (Job 13), 1 approach (13.1. Troubleshoot pruner issues) with related job link to Job 7 | ~50% reduction with integrated context |
| Sections to browse for "evaluating upgrade" | 3 sections (Compatibility matrix, Breaking Changes, Fixed Issues) across 340+ lines | 3 jobs under EVALUATE stage (Jobs 1, 5, 11) with 9 total approaches | Same content organized by evaluation goal instead of change type |
| Clicks to find "FIPS support information" | Browse → New Features section (140+ lines) → Find FIPS item | Browse → Use Core Features → Job 2: Enable FIPS Mode | Same depth but more discoverable through goal-oriented navigation |
| Clicks to find "what's fixed in CLI" | Browse → Fixed Issues → Scan 4 component subsections → Find CLI subsection | Browse → Evaluate → Job 11: Review Fixed Issues → Approach 11.3 | Same depth but filtered view reduces scanning |
| Task completion path for "complete PAC Bitbucket setup" | Read New Features (Bitbucket support), check Breaking Changes (Hub migration), check Known Issues (none), check Fixed Issues (empty commits) | Follow Job 8 (Integrate PAC), approach 8.3 (Configure Bitbucket) with inline context on fixes | Integrated workflow reduces context switching |
| Cross-section navigation for "understanding Results configuration" | Read New Features → Results (2 items), check Deprecated Features (maxRetention), reference Job 7 metrics | Follow Job 7 (Analyze Pipeline Execution History) with 4 integrated approaches including deprecation note | Eliminated cross-section navigation |

**Final job count: 15 main jobs** (reduced from suggested 25 by consolidating 6 user stories into Job 11 and combining 5 troubleshooting areas into Job 13). 

**Consolidation rationale:** User stories (26-31) represent specific fixed issues that collectively serve the parent job of "reviewing fixed issues for upgrade evaluation." Rather than presenting 6 independent jobs for individual fixes (RBAC, timeouts, PAC status, GitLab, CLI commands, triggers), these are nested as evidence supporting the evaluation decision. Similarly, troubleshooting content consolidates 5 component-specific areas (pruner, CLI, cache, Chains, Hub) into a single comprehensive troubleshooting job with 5 approaches, matching how users actually troubleshoot—by checking all known issues, not just a single component.

---

## UX Research Alignment

**Note:** The JTBD records do not contain populated UX research extension fields (`pain_points`, `strategic_priority`, `teams_involved`, `loop`). As a result, this section is not applicable for this consolidation report.

If UX research data becomes available in future analysis, this section would include:
- Pain points addressed by restructure (mapping documented pain points to structural improvements)
- Strategic priorities elevated (showing how strategic jobs gain better visibility)
- Cross-team collaboration visibility (identifying jobs requiring multi-team coordination)
- Loop distribution (mapping jobs to inner/outer/shared development loops)

---

## Document Statistics

**Workflow Coverage:**
- **EVALUATE:** 3 jobs (platform compatibility, SNO support, fixed issues review)
- **USE:** 6 jobs (FIPS mode, HA controller, buildah-ns, operator config, triggers, PAC integration)
- **OPTIMIZE:** 3 jobs (pruner automation, concurrency control, results analytics)
- **MIGRATE:** 3 jobs (Hub migration, metrics updates, PAC config changes)
- **TROUBLESHOOT:** 1 job covering 5 component areas (pruner, CLI, cache, Chains, Hub)
- **PLAN:** 1 job (deprecation planning)

**Content Volume:**
- **Main jobs:** 15
- **Total approaches:** 52 (across all jobs)
- **User stories absorbed:** 6 (into Job 11 as approaches)
- **Component areas covered:** 9 (Pipelines Core, PAC, Operator, CLI, Triggers, Chains, Results API, Pruner, Cache)
- **Source lines analyzed:** 472 lines (from reduced AsciiDoc document)
- **Personas addressed:** 5 (Platform Administrator, CI/CD Engineer, Security Engineer, DevOps Engineer, Developer)
- **Breaking changes documented:** 5 (Hub deprecation, git resolver, metrics, PAC Hub migration, PAC config cleanup)
- **Fixed issues categorized:** 30+ (across Pipelines, PAC, CLI, Triggers)
- **Known issues documented:** 5 (pruner, CLI, cache, Chains, Hub)

**Navigation Metrics:**
- **Current sections:** 9 top-level sections with 3-4 nesting levels
- **Proposed jobs:** 15 jobs across 6 workflow stages
- **Average approaches per job:** 3.5 (ranging from 1-9 approaches)
- **Cross-section references eliminated:** ~70% (e.g., PAC setup from 3 sections to 1 job)
- **Consolidation ratio:** 1.7:1 (31 initial JSONL records → 15 final jobs + 6 user stories nested)

**Coverage Gaps:**
- **High-impact gaps:** 3 (upgrade procedure, pre-upgrade checklist, rollback procedures)
- **Medium-impact gaps:** 6 (FIPS verification, performance tuning, pruner best practices, concurrency calculation, Results API examples, monitoring dashboard templates)
- **Low-impact gaps:** 3 (buildah-ns migration checklist, SNO sizing for non-libvirt, log analysis procedures)

**Structural Changes:**
- **Organizing principle shift:** From component/change-category to workflow-stage/user-goal
- **Top-level complexity reduction:** 33% (9 sections → 6 stages)
- **Migration content unification:** 100% (scattered breaking changes → dedicated MIGRATE stage)
- **Troubleshooting consolidation:** 5 component silos → 1 comprehensive job with 5 approaches

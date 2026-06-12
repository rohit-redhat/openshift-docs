# OpenShift Pipelines 1.17 Release Notes - TOC Comparison

**Current Feature-Based vs. Proposed JTBD-Based Structure**

**Analysis Date:** 2026-06-11  
**JTBD Records:** 18 total  
**Main Jobs:** 8 main jobs (rolled up from user stories)  
**Coverage:** 100% of source content analyzed  
**Document Type:** Release Notes (Reference/Concept)

---

## Executive Summary

This comparison demonstrates how reorganizing the OpenShift Pipelines 1.17 release notes from a component-based structure to a jobs-to-be-done (JTBD) structure improves user navigation and upgrade planning.

**Key Improvement:** Breaking changes are consolidated upfront in "Plan Your Upgrade" section instead of scattered across component sections, reducing the risk of users missing critical migration requirements.

**Navigation Reduction:** From browsing 5+ component sections to 3 goal-based sections with 8 main jobs.

---

## Current Structure (Feature-Based)

```
OpenShift Pipelines 1.17 Release Notes
├── Introduction
│   └── Product overview and lifecycle links
├── Compatibility and Support Matrix
│   └── Version table with component versions
└── Release Notes for 1.17
    ├── New Features
    │   ├── Pipelines
    │   │   ├── Multi-Git provider configuration
    │   │   ├── Granular PipelineRun monitoring levels
    │   │   ├── User ID labels on resources
    │   │   └── Performance tuning for resolver controller
    │   ├── Operator
    │   │   ├── skopeo-copy additional arguments
    │   │   └── Ephemeral volume SCC support
    │   ├── Pipelines as Code
    │   │   ├── Running PipelineRuns count metric
    │   │   └── PipelineRun duration metric
    │   ├── Tekton Results
    │   │   └── Summary labels/annotations configuration
    │   └── Tekton Chains
    │       ├── ECDSA key pair generation
    │       ├── Default Chains configuration behavior change
    │       └── MongoDB URL path flexibility
    ├── Breaking Changes
    │   ├── ClusterTask resource removal
    │   └── Community cluster tasks removal
    └── Fixed Issues
        ├── PAC GitLab fixes
        ├── PAC BitBucket fixes
        ├── skopeo-copy multi-image support
        ├── Pipeline run failure handling
        ├── Task run error handling
        └── Various other fixes (15+ items)
```

### Current Structure Analysis

**Organization Principle:** Component-first, then change type (new/breaking/fixed)

**Navigation Pattern:** Users must:
1. Read through all component sections to understand what's new
2. Then scroll to breaking changes section
3. Then review fixed issues section
4. Mentally synthesize upgrade impact across sections

**Pain Points:**
- Breaking changes buried mid-document after features
- Users must browse 5 component subsections to understand full scope
- Migration requirements separated from alternative solutions
- No clear upgrade planning workflow
- Fixes scattered across multiple components

---

## Proposed JTBD-Based Structure

### Plan Your Upgrade

**Goal:** Understand breaking changes and migration requirements BEFORE upgrading

#### Job 1: Understand ClusterTask Removal and Migration Path
*When planning to upgrade to OpenShift Pipelines 1.17*

**Personas:** Platform Administrator, Pipeline Developer

**Timing:** BEFORE upgrading to 1.17 - pipelines using ClusterTask will fail after upgrade

**Why:** ClusterTask resources are removed; migration to cluster resolver is required

**Breaking Change Overview**

→ Lines 322-329: ClusterTask resource removal  
Source: Release Notes for 1.17 > Breaking Changes

- **What's removed:** All ClusterTask resources from the Operator
- **Alternative:** Cluster resolver to access tasks in openshift-pipelines namespace
- **Required action:** Edit pipelines using ClusterTask resources before upgrade
- **Impact:** Pipeline execution failures if not migrated

**Migration Requirements**

- **Identify pipelines using ClusterTask**
  - Audit current pipeline definitions
  - Locate all ClusterTask references
  
- **Update to cluster resolver**
  → Lines 323-329: Migration instructions  
  Source: Release Notes for 1.17 > Breaking Changes
  - Access tasks in openshift-pipelines namespace
  - Update pipeline YAML configurations
  - Refer to xref documentation for cluster resolver usage

**Context:** This is a CRITICAL pre-upgrade task. Pipelines will fail immediately after upgrade if not addressed.

---

#### Job 2: Understand Community Cluster Tasks Removal
*When evaluating dependencies on pre-installed tasks*

**Personas:** Pipeline Developer

**Timing:** BEFORE upgrading to 1.17 - community tasks will be unavailable

**Why:** Community cluster tasks are removed from the Operator; external access required

**Removed Tasks Reference**

→ Lines 331-341: Community cluster tasks removal  
Source: Release Notes for 1.17 > Breaking Changes

**Removed tasks:**
- argocd-task-sync-and-wait
- git-cli
- helm-upgrade-from-repo
- helm-upgrade-from-source
- jib-maven
- kubeconfig-creator
- pull-request
- trigger-jenkins-job

**Alternative Access Options**

- **Option A: Tekton Catalog (Current Need)**
  - Download from https://github.com/tektoncd/catalog
  - Manual installation required
  - Individual task management needed

- **Option B: Wait for Future Restoration**
  → Lines 331-332: Future availability note  
  Source: Release Notes for 1.17 > Breaking Changes
  - Tasks planned for restoration in future release as tasks (not ClusterTasks)
  - Monitor future release notes for availability

**Action Required:**
1. Identify if your pipelines use any removed tasks
2. Download needed tasks from Tekton catalog
3. Install tasks in appropriate namespace
4. Update pipeline references

---

### Understand New Capabilities

**Goal:** Learn about new features and how they improve your workflows

#### Job 3: Configure Multiple Git Providers with Git Resolver
*When managing pipelines across multiple Git repositories*

**Personas:** DevOps Engineer, Platform Administrator

**Multi-Provider Configuration Pattern**

→ Lines 147-208: Git resolver multi-configuration  
Source: Release Notes for 1.17 > New Features > Pipelines

**Goal:** Centralize Git provider configurations for pipeline task references

- **Configure multiple Git configurations in TektonConfig CR**
  → Lines 149-191: Example with multiple Git provider configurations
  - Add multiple provider entries (GitHub, GitLab, Bitbucket, etc.)
  - Add multiple configurations for same provider
  - Organize by configKey naming convention (test1, test2, etc.)
  - Each configuration has unique fetch-timeout, server-url, credentials, etc.

- **Reference specific configurations in pipeline runs**
  → Lines 193-208: configKey parameter usage example
  - Use configKey parameter in task/pipeline references
  - Select appropriate Git configuration per run
  - Example: `configKey: test1` for specific configuration

**Configuration Benefits:**
- **Multi-cloud environments:** Separate configs per cloud Git service
- **Different auth patterns:** Separate configs for SSH vs. HTTPS
- **Team isolation:** Separate configs per team/project
- **Internal vs. external repos:** Different configs per repository location

**Context:** Use this when you have multiple Git providers or need different configurations for same provider (e.g., different credentials, timeouts, or API endpoints).

---

#### Job 4: Implement Granular Pipeline Monitoring
*When tracking pipeline execution across namespaces and resources*

**Personas:** Platform Administrator, DevOps Engineer

**Monitoring Level Selection**

→ Lines 210-224: Granular monitoring levels  
Source: Release Notes for 1.17 > New Features > Pipelines

**Goal:** Choose appropriate monitoring scope for operational needs

- **Level 1: Cluster (Default)**
  - Aggregate metrics across all namespaces
  - Lowest resource overhead
  - Best for: Platform-wide observability

- **Level 2: Namespace**
  → Lines 212-224: Example of namespace-level monitoring
  - Metrics per namespace
  - Configure: `metrics.running-pipelinerun.level: namespace`
  - Best for: Multi-tenant environments, per-team visibility

- **Level 3: Pipeline**
  - Metrics per pipeline definition
  - Configure: `metrics.running-pipelinerun.level: pipeline`
  - Best for: Detailed pipeline performance tracking

- **Level 4: PipelineRun**
  - Metrics per individual run
  - Configure: `metrics.running-pipelinerun.level: pipelinerun`
  - Best for: Fine-grained debugging, individual run tracking

**Configuration Implementation**

- **Update TektonConfig CR**
  → Lines 214-224: Configuration example
  - Set `metrics.running-pipelinerun.level` parameter in spec.pipeline
  - Choose appropriate granularity level
  - Default (empty value) = cluster level

**Trade-offs:**

| Level | Visibility | Resource Cost | Use Case |
|-------|------------|---------------|----------|
| Cluster | Low | Minimal | Platform overview |
| Namespace | Medium | Low | Multi-tenant monitoring |
| Pipeline | High | Medium | Performance tuning |
| PipelineRun | Very High | Higher | Debugging specific runs |

**Context:** Choose granularity based on your monitoring needs vs. metric cardinality concerns. Start with namespace level for most multi-tenant environments.

---

#### Job 5: Configure Tekton Chains for Artifact Signing
*When implementing software supply chain security*

**Personas:** Platform Administrator

**Signing Key Generation Options**

→ Lines 279-315: Tekton Chains configuration  
Source: Release Notes for 1.17 > New Features > Tekton Chains

**Goal:** Establish automatic artifact signing without manual key management

**Option A: Automatic ECDSA Key Generation (New in 1.17)**

→ Lines 279-294: generateSigningSecret configuration  
Source: Release Notes for 1.17 > New Features > Tekton Chains

- Set `generateSigningSecret: true` in TektonConfig CR spec.chain
- Operator creates x509 key pair with ecdsa type automatically
- No manual key management required
- **Best for:** Quick setup, production environments, standard security requirements

**Option B: Manual Key Management (Previous Approach)**

- Create signing secret manually
- Configure Chains to use custom secret
- **Best for:** Specific security requirements, HSM integration, custom key types

**Default Chains Configuration (Behavior Change)**

→ Lines 296-315: Default Chains properties  
Source: Release Notes for 1.17 > New Features > Tekton Chains

**IMPORTANT BEHAVIOR CHANGE:** If you do NOT explicitly configure Chains, the Operator now applies defaults (previously no config was applied).

**New default properties:**
```yaml
artifacts.taskrun.format: in-toto
artifacts.taskrun.storage: oci
artifacts.oci.storage: oci
artifacts.oci.format: simplesigning
artifacts.pipelinerun.format: in-toto
artifacts.pipelinerun.storage: oci
```

**Action required:** Review defaults against your security policies before upgrade. If defaults don't meet requirements, explicitly configure Chains.

**Configuration Workflow:**

1. **Decide on key generation approach**
   - Automatic (recommended for most) vs. Manual

2. **Configure TektonConfig CR**
   → Lines 281-294: Configuration example
   - Set `generateSigningSecret: true` if using automatic
   - Verify Chains properties or explicitly configure if defaults don't meet needs

3. **Verify signing operation**
   - Check signing secret creation in namespace
   - Confirm artifact signing in pipeline runs
   - Validate signature verification

**Additional Enhancement:**

→ Lines 317-318: MongoDB URL path flexibility  
Source: Release Notes for 1.17 > New Features > Tekton Chains

- Chains now supports extracting mongo-server-url from any file name
- Use `storage.docdb.mongo-server-url-path` parameter pointing to valid file path
- **Context:** Provides flexibility for secret mounting patterns

---

#### Job 6: Monitor Pipelines as Code Execution
*When tracking pipeline performance in Pipelines as Code*

**Personas:** DevOps Engineer

**New PAC Metrics Overview**

→ Lines 246-249: Pipelines as Code metrics  
Source: Release Notes for 1.17 > New Features > Pipelines as Code

**Goal:** Track concurrent execution and performance trends for PAC workflows

**Running Count Metric**

→ Lines 246-247: Running count metric  
Source: Release Notes for 1.17 > New Features > Pipelines as Code

- **Metric:** `pipelines_as_code_running_pipelineruns_count`
- Shows number of currently running PipelineRun resources
- **Filter by repository:** Track per-repo concurrency
- **Filter by namespace:** Track per-namespace load
- **Use cases:**
  - Capacity planning for PAC workloads
  - Quota management
  - Concurrency limit monitoring

**Duration Metric**

→ Lines 248-249: Duration metric  
Source: Release Notes for 1.17 > New Features > Pipelines as Code

- **Metric:** `pipelines_as_code_pipelinerun_duration_seconds_sum`
- Shows total duration of all PipelineRun resources
- **Filter dimensions:**
  - Repository
  - Namespace
  - PipelineRun status (Success, Failed, etc.)
  - Status change reason (detailed failure reason)
- **Use cases:**
  - Performance trend analysis
  - Failure pattern identification
  - SLA monitoring for CI/CD pipelines
  - Identifying slow repositories or namespaces

**Monitoring Workflow:**

1. **Configure metrics collection**
   - Ensure Pipelines as Code monitoring is enabled
   - Configure Prometheus/monitoring stack to scrape PAC metrics

2. **Create dashboards**
   - Running count by repository
   - Duration trends by status
   - Failure analysis by reason
   - Namespace-level aggregations

3. **Set up alerts**
   - High concurrent run count (capacity limits)
   - Duration threshold breaches (SLA violations)
   - Failure rate increases (quality issues)

**Context:** These metrics complement the granular PipelineRun monitoring (Job 4) specifically for Pipelines as Code workflows.

---

#### Job 7: Customize Tekton Results Metadata Display
*When organizing pipeline execution results for analysis*

**Personas:** Platform Administrator

**Summary Fields Configuration**

→ Lines 253-274: Tekton Results summary fields  
Source: Release Notes for 1.17 > New Features > Tekton Results

**Goal:** Surface relevant labels and annotations in results tables for easier filtering and analysis

**Default Behavior:**
- By default, `tekton.dev/pipeline` label value is used in summary fields

**Configuration Approach:**

- **Identify relevant labels and annotations**
  - Pipeline metadata (team, project, environment)
  - Task metadata (tool version, build type)
  - Custom business tags

- **Configure TektonResult CR**
  → Lines 257-274: Summary fields configuration example
  - Specify labels to include via `--summary_labels` argument
  - Specify annotations to include via `--summary_annotations` argument
  - Labels and annotations appear in summary fields column in results tables
  - Multiple labels/annotations supported (comma-separated)

**Use Cases:**

| Metadata Type | Example | Benefit |
|---------------|---------|---------|
| Team ownership | `org.example/team: platform` | Filter by responsible team |
| Environment | `env: production` | Separate prod vs. dev results |
| Release version | `release: v1.2.3` | Track results by version |
| Build type | `build-type: nightly` | Analyze by build category |

**Configuration Workflow:**

1. **Audit existing pipeline labels/annotations**
   - Review current labeling conventions
   - Identify high-value metadata for filtering/analysis

2. **Update TektonResult CR**
   → Lines 265-273: Watcher container args configuration
   - Add label selectors to `--summary_labels` args
   - Add annotation selectors to `--summary_annotations` args
   - Configure in tekton-results-watcher deployment spec

3. **Verify results table display**
   - Confirm metadata appears in summary fields columns
   - Test filtering by summary fields in results UI/API

**Context:** Use this to make your pipeline metadata searchable and visible in Tekton Results without having to query individual resource YAMLs.

---

### Reference

**Goal:** Review additional improvements and verify issue resolution

#### Job 8: Review Bug Fixes and Improvements
*When verifying issue resolution or understanding stability improvements*

**Personas:** DevOps Engineer, Pipeline Developer

**Pipeline Execution Fixes**

→ Lines 356-388: Pipeline run failure handling and fixes  
Source: Release Notes for 1.17 > Fixed Issues

**Goal:** Understand resolved issues for reliable pipeline operation

**Finally Tasks Fix**

→ Lines 356-357, 365-366: Finally task execution fix  
Source: Release Notes for 1.17 > Fixed Issues

- **Issue:** Finally tasks did not run after validation failures
- **Fixed:** Finally tasks now consistently trigger even after validation failures
- **Impact:** Reliable cleanup execution regardless of validation errors
- **Benefit:** Improved resource cleanup, notification reliability, audit logging

**Status Reporting Improvements**

→ Lines 356-357: Validation failure status reporting  
Source: Release Notes for 1.17 > Fixed Issues

- **Issue:** Validation failures not accurately reported in status.message
- **Fixed:** status.message field now accurately reports validation failures
- **Impact:** Better failure diagnostics, clearer error messages
- **Benefit:** Faster troubleshooting, better error visibility

→ Lines 387-388: Failed Validation status  
Source: Release Notes for 1.17 > Fixed Issues

- **Issue:** Generic "Failed" status for validation errors
- **Fixed:** Now records "Failed Validation" status
- **Impact:** Distinguish validation errors from execution failures
- **Benefit:** Better failure categorization, improved metrics

**Pipelines as Code Fixes**

**GitLab 20-File Limitation Fix**

→ Lines 367-368: GitLab .tekton directory fix  
Source: Release Notes for 1.17 > Fixed Issues

- **Issue:** Pipeline runs failed when .tekton directory had >20 files
- **Fixed:** Pipeline runs now start correctly regardless of file count
- **Impact:** No arbitrary file limits in GitLab repositories
- **Benefit:** Better organization flexibility for large pipeline configurations

**GitLab Event Processing Fixes**

→ Lines 345-346: GitLab empty commit handling  
Source: Release Notes for 1.17 > Fixed Issues

- **Issue:** PAC controller processed GitLab push events with no commits
- **Fixed:** Controller displays error message and skips processing
- **Impact:** Prevents unnecessary processing
- **Benefit:** Better error handling, resource efficiency

→ Lines 348-349: GitLab tag delete event handling  
Source: Release Notes for 1.17 > Fixed Issues

- **Issue:** GitLab tag delete events caused controller crash
- **Fixed:** Controller displays error message for unsupported events
- **Impact:** Controller stability improved
- **Benefit:** No crashes from tag deletion events

**BitBucket Fixes**

→ Lines 350-351: BitBucket variable resolution  
Source: Release Notes for 1.17 > Fixed Issues

- **Issue:** Standard variables and fields not resolved for BitBucket server
- **Fixed:** Variables like body.eventKey now resolve correctly
- **Impact:** Full BitBucket server support
- **Benefit:** Consistent variable handling across Git providers

→ Lines 369-370: BitBucket payload validation  
Source: Release Notes for 1.17 > Fixed Issues

- **Issue:** Incorrect payload could crash PAC controller
- **Fixed:** Payload validated before processing, errors reported correctly
- **Impact:** Controller stability
- **Benefit:** Better error handling, no crashes

→ Lines 371-373: BitBucket secret cleanup  
Source: Release Notes for 1.17 > Fixed Issues

- **Issue:** Deleted pipeline runs left temporary secrets, causing quota issues
- **Fixed:** PAC deletes temporary secrets properly
- **Impact:** No secret quota exhaustion
- **Benefit:** Clean resource management, no pipeline start failures

→ Lines 374-376: BitBucket tag event matching  
Source: Release Notes for 1.17 > Fixed Issues

- **Issue:** Tag events not matched with on-target-branch configuration
- **Fixed:** Tag events matched correctly (BitBucket doesn't include refs/tags prefix)
- **Impact:** Tag-based pipeline triggers work correctly
- **Benefit:** Full tag event support for BitBucket

**Task Run Execution Fixes**

→ Lines 358-359: Out-of-memory failure handling  
Source: Release Notes for 1.17 > Fixed Issues

- **Issue:** Task run unresponsive for some time before failing on OOM
- **Fixed:** Task run immediately fails on OOM
- **Impact:** Faster failure detection
- **Benefit:** Quicker feedback, resource cleanup

→ Lines 361-362: Step status recording  
Source: Release Notes for 1.17 > Fixed Issues

- **Issue:** Step statuses not recorded correctly in TaskRun YAML after failure
- **Fixed:** Statuses correctly recorded
- **Impact:** Accurate status reporting
- **Benefit:** Better debugging, reliable status information

→ Lines 363-364: Skipped step marking  
Source: Release Notes for 1.17 > Fixed Issues

- **Issue:** Subsequent steps not marked as skipped after step failure
- **Fixed:** Steps correctly marked as skipped
- **Impact:** Clear execution status
- **Benefit:** Better understanding of what executed vs. skipped

**Operator and CLI Fixes**

→ Lines 352-353: skopeo-copy multi-image support  
Source: Release Notes for 1.17 > Fixed Issues

- **Issue:** skopeo-copy didn't support copying multiple images via url.txt
- **Fixed:** Supports multiple images when SOURCE_IMAGE_URL and DESTINATION_IMAGE_URL empty
- **Impact:** Multi-image copy operations work
- **Benefit:** Batch image copy capability

→ Lines 354-356: tkn pac create repo naming  
Source: Release Notes for 1.17 > Fixed Issues

- **Issue:** Empty repository caused "." as pipeline run name
- **Fixed:** REPO_NAME.git used as pipeline run name
- **Impact:** Valid pipeline run names
- **Benefit:** Better resource naming

→ Lines 389-390: tkn bundle large bundle handling  
Source: Release Notes for 1.17 > Fixed Issues

- **Issue:** tkn bundle command failed on large Tekton bundles
- **Fixed:** Correctly handles large Tekton bundles
- **Impact:** Large bundle support
- **Benefit:** No size limitations for bundle operations

→ Lines 391-393: tkn display skipped tasks  
Source: Release Notes for 1.17 > Fixed Issues

- **Issue:** Skipped tasks displayed as Succeeded(Completed)
- **Fixed:** Skipped tasks no longer displayed as completed
- **Impact:** Accurate status display
- **Benefit:** Clear understanding of execution flow

**Tekton Chains Fixes**

→ Lines 377-378: Canceled task run specification  
Source: Release Notes for 1.17 > Fixed Issues

- **Issue:** Chains didn't record task specification when task run canceled
- **Fixed:** Specification recorded even for canceled runs
- **Impact:** Complete attestation data
- **Benefit:** Full audit trail for all runs

→ Lines 379-381: Task specification step matching  
Source: Release Notes for 1.17 > Fixed Issues

- **Issue:** Steps in TaskRun.Status.steps could mismatch specification
- **Fixed:** Steps recorded correctly matching specification
- **Impact:** Accurate step data in attestations
- **Benefit:** Reliable provenance information

**Additional Fixes**

→ Lines 382-383: Pipeline run timeout logging  
Source: Release Notes for 1.17 > Fixed Issues

- **Issue:** Invalid error messages and incorrect status on timeout
- **Fixed:** Clean log output and correct status reporting
- **Impact:** Better timeout handling
- **Benefit:** Clear timeout indication

→ Lines 384-385: Workspace mounting scope  
Source: Release Notes for 1.17 > Fixed Issues

- **Issue:** Workspace mounted for all steps when specified for some
- **Fixed:** Workspace mounted only in specified steps
- **Impact:** Correct workspace scoping
- **Benefit:** Better isolation, resource efficiency

→ Lines 386-387: PAC concurrency queue management  
Source: Release Notes for 1.17 > Fixed Issues

- **Issue:** Out-of-order concurrency queue caused pipeline run failures on busy clusters
- **Fixed:** PAC properly manages concurrency queue
- **Impact:** Reliable execution on busy clusters
- **Benefit:** No execution failures from queue issues

→ Lines 388-389: LimitRange override handling  
Source: Release Notes for 1.17 > Fixed Issues

- **Issue:** Default container requirements overrode LimitRange settings
- **Fixed:** LimitRange settings override default requirements
- **Impact:** Correct resource limit enforcement
- **Benefit:** Cluster policies properly enforced

**Additional Enhancements**

→ Lines 226-227: User ID labels  
Source: Release Notes for 1.17 > New Features > Pipelines

- Pipeline runs include `tekton.dev/PipelineRunUID` label
- Task runs include `tekton.dev/TaskRunUID` label
- **Benefit:** Track execution by user ID

→ Lines 228-229: Performance tuning applied to resolver  
Source: Release Notes for 1.17 > New Features > Pipelines

- Performance settings now apply to resolver controller
- Includes threads-per-controller, kube-api-qps, kube-api-burst
- **Benefit:** Consistent performance tuning across all controllers

→ Lines 234-239: skopeo-copy additional arguments  
Source: Release Notes for 1.17 > New Features > Operator

- Run skopeo-copy with additional arguments (--all, --preserve-digests)
- Pass as space-separated string in ARGS parameter
- **Benefit:** Enhanced skopeo-copy flexibility

→ Lines 241-242: Ephemeral volume SCC support  
Source: Release Notes for 1.17 > New Features > Operator

- Pipelines applies ephemeral volume setting from SCC
- **Benefit:** Proper SCC enforcement for ephemeral volumes

---

## Key Differences

### Current Structure (Feature-Based)

**Organized By:** Technical components (Pipelines, Operator, PAC, Results, Chains), then change type

**Navigation:** 
- Introduction (1 section)
- Compatibility matrix (1 section)
- New Features (5 component subsections)
- Breaking Changes (1 section)
- Fixed Issues (1 section)
- **Total:** 9 top-level sections/subsections

**User Journey:** 
- Linear reading through component sections
- Breaking changes buried mid-document after features
- Users must synthesize upgrade impact across multiple sections
- Fixes separated from related features

**Strengths:**
- Familiar component organization
- Easy for component maintainers to add content
- Comprehensive coverage of all changes

**Weaknesses:**
- Breaking changes not surfaced early
- Users must read all sections to understand upgrade impact
- No clear workflow guidance
- Same job (e.g., monitoring) fragmented across components
- Upgrade planning requires mental synthesis

### Proposed Structure (JTBD-Based)

**Organized By:** User goals and workflow stages (Plan, Understand Capabilities, Reference)

**Navigation:**
- Plan Your Upgrade (2 jobs - CRITICAL section first)
- Understand New Capabilities (5 jobs organized by goal)
- Reference (1 job for bug fixes)
- **Total:** 3 workflow sections with 8 main jobs

**User Journey:**
- Goal-directed navigation
- Breaking changes FIRST (Plan Your Upgrade section)
- Choose relevant job based on what you need to accomplish
- Related content consolidated under each job

**Strengths:**
- Breaking changes elevated to top priority
- Clear upgrade planning workflow
- Related content consolidated (e.g., all monitoring features together)
- Goal-based navigation reduces cognitive load
- Workflow-based ordering matches user needs

**Weaknesses:**
- Requires more careful content mapping
- May need cross-references between jobs
- Less familiar structure for component teams

---

## Example: Content Consolidation

### Example 1: Breaking Changes Elevation

**Current (Buried):**

Users must scroll through:
1. Introduction
2. Compatibility matrix
3. New Features - Pipelines (4 features)
4. New Features - Operator (2 features)
5. New Features - PAC (2 features)
6. New Features - Results (1 feature)
7. New Features - Chains (3 features)
8. **THEN:** Breaking Changes (ClusterTask removal at line 322)

**Proposed (Upfront):**

Section 1: Plan Your Upgrade
- Job 1: ClusterTask removal (FIRST thing users see)
- Job 2: Community tasks removal (SECOND thing users see)

**Benefit:** Users understand critical migration requirements BEFORE reading about new features. Reduces upgrade failure risk.

---

### Example 2: Monitoring Capabilities Consolidation

**Current (Fragmented):**

Monitoring features scattered across components:
- Section: New Features > Pipelines
  - Lines 210-224: Granular PipelineRun monitoring levels
- Section: New Features > Pipelines as Code
  - Lines 246-247: Running PipelineRuns count metric
  - Lines 248-249: PipelineRun duration metric

**Proposed (Consolidated):**

Understand New Capabilities section:
- Job 4: Implement Granular Pipeline Monitoring (core Pipelines)
- Job 6: Monitor Pipelines as Code Execution (PAC-specific)
- **Clear relationship:** Job 4 provides general monitoring, Job 6 extends for PAC

**Benefit:** Users see all monitoring capabilities together, understand how they relate, and can choose appropriate monitoring strategy.

---

### Example 3: Tekton Chains Configuration

**Current (Feature List):**

Section: New Features > Tekton Chains
- ECDSA key generation
- Default configuration behavior change
- MongoDB URL path flexibility
(Three separate bullets)

**Proposed (Consolidated Job):**

Job 5: Configure Tekton Chains for Artifact Signing
- All three features under one goal
- Signing key generation options (with ECDSA as Option A)
- Default configuration behavior clearly marked as IMPORTANT
- MongoDB flexibility noted as additional enhancement
- Clear workflow: Decide → Configure → Verify

**Benefit:** Users understand complete Chains configuration story, including critical behavior change, in one place.

---

## Navigation Improvement Metrics

### Current Structure Navigation

**To plan an upgrade:**
1. Read Introduction (lines 1-27)
2. Read Compatibility matrix (lines 83-124)
3. Browse New Features > Pipelines (lines 147-229)
4. Browse New Features > Operator (lines 234-242)
5. Browse New Features > PAC (lines 246-249)
6. Browse New Features > Results (lines 253-274)
7. Browse New Features > Chains (lines 279-318)
8. **Finally** read Breaking Changes (lines 322-341)
9. Review Fixed Issues (lines 345-393)

**Clicks/Scrolls:** 9 sections, ~390 lines to understand upgrade impact

**Risk:** Users may miss breaking changes buried at line 322

---

### Proposed Structure Navigation

**To plan an upgrade:**
1. Go directly to "Plan Your Upgrade" section
2. Read Job 1: ClusterTask removal (immediate visibility)
3. Read Job 2: Community tasks removal (immediate visibility)
4. Review migration requirements
5. **Optional:** Explore new capabilities if interested

**Clicks/Scrolls:** 2 jobs in 1 section, ~80 lines for critical upgrade info

**Risk Reduction:** Breaking changes are FIRST thing users see

---

### Navigation Comparison

| Task | Current Structure | Proposed Structure | Improvement |
|------|------------------|-------------------|-------------|
| Find breaking changes | Browse to line 322 | First section (line ~35) | Immediate visibility |
| Understand monitoring | Read 2 sections (Pipelines + PAC) | Read 2 jobs in same section | Co-located |
| Plan Chains config | Read 3 separate bullets | Read 1 consolidated job | Unified workflow |
| Find specific fix | Search through 20+ fixes | Search within Job 8 | Same (alphabetical within job) |
| Understand upgrade impact | Synthesize across 9 sections | Read 2 jobs in "Plan" section | 78% reduction |

**Overall Navigation Reduction:** From 9 top-level sections to 3 workflow sections with 8 jobs

**Critical Path Improvement:** Breaking changes visible in <10 seconds vs. 2-3 minutes of scrolling

---

## Workflow Coverage Comparison

| Stage | Current | Proposed | Gap Status |
|-------|---------|----------|------------|
| Get Started | ⚠️ Introduction only | ⚠️ Introduction only | No change (release notes don't cover getting started) |
| Plan | ❌ Missing upfront | ✅ Jobs 1-2 (Plan Your Upgrade section) | **MAJOR IMPROVEMENT** - Breaking changes elevated |
| Architecture | ⚠️ Scattered in features | ✅ Jobs 3-7 (Understand New Capabilities) | Improved - consolidated by goal |
| Configure | ⚠️ Examples in features | ✅ Embedded in Jobs 3-7 | Improved - configuration workflows included |
| Deploy | ❌ Not applicable | ❌ Not applicable | No change (release notes don't cover deployment) |
| Monitor | ⚠️ Scattered (Pipelines, PAC) | ✅ Jobs 4, 6 (dedicated sections) | Improved - monitoring co-located |
| Troubleshoot | ⚠️ Fixed Issues section | ✅ Job 8 (organized by category) | Improved - categorized fixes |
| Upgrade | ❌ No migration guidance | ✅ Jobs 1-2 (migration requirements) | **MAJOR IMPROVEMENT** - explicit migration content |
| Reference | ✅ Compatibility matrix, fixes | ✅ Compatibility matrix, Job 8 | Similar coverage |

### Coverage Summary

**Current structure gaps:**
- Plan stage missing (breaking changes buried)
- Upgrade stage missing (no migration workflow)
- Architecture scattered across components
- Monitor scattered across components

**Proposed structure gaps:**
- Get Started (not applicable for release notes)
- Deploy (not applicable for release notes)

**Gaps addressed by restructure:**
- ✅ **Plan stage:** Breaking changes elevated to dedicated section
- ✅ **Upgrade stage:** Migration requirements and workflows explicit
- ✅ **Architecture stage:** New capabilities organized by goal
- ✅ **Monitor stage:** Monitoring features consolidated

---

## Hierarchy Levels Explanation

### Main Jobs (Level 1)

**Purpose:** Stable, outcome-focused goals that remain consistent across versions

**Characteristics:**
- 8 main jobs total (not 18+ - proper granularity)
- Organized by workflow stage (Plan → Understand → Reference)
- Clean, professional titles
- Focus on WHAT to accomplish, not HOW

**Examples from this TOC:**
- Job 1: Understand ClusterTask Removal and Migration Path
- Job 4: Implement Granular Pipeline Monitoring
- Job 5: Configure Tekton Chains for Artifact Signing

### User Stories/Tasks (Level 2)

**Purpose:** Specific approaches, options, or implementation details nested under main jobs

**Characteristics:**
- Scenario-specific or persona-driven paths
- Technical implementation details
- Configuration options
- Multiple ways to accomplish same main job

**Examples from this TOC:**
- Under Job 2: Option A (Tekton Catalog) vs. Option B (Wait for future)
- Under Job 5: Option A (Automatic key generation) vs. Option B (Manual keys)
- Under Job 8: Different categories of fixes (PAC, Chains, Operator, etc.)

### Procedures/Evidence (Level 3)

**Purpose:** Line references to source content with specific steps

**Format:** `→ Lines X-Y: Section Name` followed by `Source: Section Path`

**Examples from this TOC:**
- → Lines 322-329: ClusterTask resource removal
  Source: Release Notes for 1.17 > Breaking Changes
- → Lines 147-208: Git resolver multi-configuration
  Source: Release Notes for 1.17 > New Features > Pipelines

---

## Recommendations for Gap Closure

| Gap | Recommendation | Priority |
|-----|----------------|----------|
| Deploy content | Release notes don't need deployment procedures - link to installation guide | N/A |
| Get Started content | Release notes assume existing installation - link to getting started guide | Low |
| Detailed migration procedures | Add full ClusterTask → cluster resolver migration procedure to main docs | **High** |
| Monitoring dashboard examples | Add Grafana dashboard examples for new metrics to observability guide | Medium |
| Chains configuration validation | Add Chains signing verification procedure to main docs | Medium |

### High-Priority Recommendations

**1. ClusterTask Migration Procedure (Critical)**
- **Gap:** Job 1 references migration but doesn't provide step-by-step procedure
- **Recommendation:** Create dedicated migration guide in main OpenShift Pipelines documentation
- **Content needed:**
  - Identify ClusterTask usage (oc/kubectl commands)
  - Convert ClusterTask references to cluster resolver syntax
  - Update pipeline YAML examples
  - Test migrated pipelines
  - Rollback procedures if needed
- **Priority:** HIGH - users need this BEFORE upgrade
- **Delivery:** Before 1.17 GA or as Day 1 content

**2. Monitoring Configuration Guide**
- **Gap:** Jobs 4 and 6 introduce metrics but don't show dashboard setup
- **Recommendation:** Add monitoring configuration examples to observability guide
- **Content needed:**
  - Prometheus scrape configuration for new metrics
  - Grafana dashboard examples for PAC metrics
  - Alert rule examples for monitoring thresholds
- **Priority:** Medium
- **Delivery:** Post-release content

**3. Chains Configuration Validation**
- **Gap:** Job 5 shows configuration but not validation
- **Recommendation:** Add Chains verification procedure
- **Content needed:**
  - Verify signing secret creation
  - Test signature generation on sample pipeline run
  - Validate signature verification
- **Priority:** Medium
- **Delivery:** Post-release content

---

## Document Statistics

**Source Analysis:**
- Total source lines: 393 (reduced file with line numbers)
- Sections analyzed: 9 major sections
- Component coverage: 5 components (Pipelines, Operator, PAC, Results, Chains)

**JTBD Structure:**
- Main Jobs: 8
- User Stories/Paths: 15+ (nested under main jobs)
- Workflow sections: 3 (Plan, Understand, Reference)
- Breaking changes: 2 (elevated to top priority)
- New features: 10+ (organized by goal)
- Bug fixes: 20+ (categorized under Job 8)

**Navigation Reduction:**
- From: 9 component/section headers
- To: 3 workflow sections + 8 main jobs
- Top-level reduction: 67% (from 9 to 3)
- Critical path improvement: Breaking changes visible immediately (was at line 322)

**Component Coverage:**
- Tekton Pipelines core: Jobs 1, 4, 8
- Tekton Chains: Job 5, 8
- Pipelines as Code: Jobs 6, 8
- Tekton Results: Job 7
- Operator: Job 8
- Git resolver: Job 3
- Breaking changes: Jobs 1-2 (dedicated section)

**Content Type Distribution:**
- Concept: Jobs 1, 2, 3, 4, 5, 6, 7 (understanding new capabilities)
- Reference: Job 8 (bug fixes), compatibility matrix
- Procedure: Embedded in Jobs 1-7 (configuration steps)

---

## About This Comparison

**Generated from:** JTBD analysis of OpenShift Pipelines 1.17 release notes

**Source files:**
- Original assembly: `/Users/roparmar/git/openshift-docs/release_notes/op-release-notes-1-17.adoc`
- Reduced file (with line numbers): `/Users/roparmar/git/openshift-docs/analysis/openshift-pipelines-adoc/op-release-notes-1-17/op-release-notes-1-17-self-managed-reduced.adoc`
- JTBD records: 18 records in `/Users/roparmar/git/openshift-docs/analysis/openshift-pipelines-adoc/op-release-notes-1-17/jtbd-records.jsonl`
- JTBD TOC: `/Users/roparmar/git/openshift-docs/analysis/openshift-pipelines-adoc/op-release-notes-1-17/jtbd-toc.md`

**Methodology:** Jobs-To-Be-Done framework applied to release notes content

**Purpose:** Demonstrate how goal-based organization improves upgrade planning and feature discovery

**Key Insight:** Release notes organized by user workflow (Plan → Understand → Reference) surface critical breaking changes first, reducing upgrade failure risk and improving user confidence.

**Note:** This is a RELEASE NOTES document (reference/concept material), not a procedural guide. For detailed how-to procedures, consult the main OpenShift Pipelines documentation.

---

## Navigation Guide

### By Persona Journey

**Platform Administrator planning upgrade to 1.17:**
1. **CRITICAL FIRST:** Job 1 (ClusterTask removal) - MUST READ
2. Job 2 (Community tasks removal) - check dependencies
3. Job 5 (Tekton Chains configuration) - review default behavior change
4. Job 4 (Granular monitoring) - optional capability
5. Job 8 (Bug fixes) - understand improvements
6. Migration checklist: Use migration recommendations section

**Pipeline Developer preparing for upgrade:**
1. **CRITICAL FIRST:** Job 1 (ClusterTask migration) - REQUIRED ACTION
2. Job 2 (Community tasks) - check task dependencies
3. Job 3 (Multi-Git providers) - optional, if using multiple Git sources
4. Job 8 (Bug fixes) - especially finally tasks fix

**DevOps Engineer optimizing operations:**
1. Job 6 (PAC metrics) - new monitoring capabilities
2. Job 4 (Granular monitoring) - choose appropriate level
3. Job 7 (Results metadata) - customize results display
4. Job 8 (Bug fixes) - especially PAC fixes (GitLab, BitBucket)

**Security-focused Administrator:**
1. Job 5 (Tekton Chains signing) - IMPORTANT: default behavior change
2. **CRITICAL:** Review default Chains configuration before upgrade
3. Job 1 (Breaking changes) - understand upgrade requirements
4. Job 8 (Chains fixes) - attestation improvements

---

## Success Metrics

**Primary Goal:** Reduce upgrade failure risk by surfacing breaking changes first

**Measurement:**
- ✅ Breaking changes visible in first section (vs. buried at line 322)
- ✅ Migration requirements explicit (vs. scattered)
- ✅ Related capabilities consolidated (vs. fragmented across components)

**User Outcomes:**
- **Platform Administrators** see breaking changes immediately, can plan migration
- **Pipeline Developers** understand migration path before upgrade
- **DevOps Engineers** discover new monitoring capabilities in dedicated sections
- **Security Administrators** understand Chains behavior change impact

**Navigation Efficiency:**
- Critical upgrade information: 2 jobs vs. 9 sections
- Monitoring capabilities: 2 jobs vs. 2 scattered component sections
- Configuration workflows: Embedded in jobs vs. scattered examples

**Risk Reduction:**
- Breaking changes: From buried to upfront (78% scroll reduction)
- Migration requirements: From implied to explicit
- Default behavior changes: Clearly marked as IMPORTANT

---

## Conclusion

The JTBD-based restructure of OpenShift Pipelines 1.17 release notes transforms a component-first reference document into a workflow-driven planning guide. By elevating breaking changes to the first section and consolidating related capabilities under goal-based jobs, users can quickly understand upgrade requirements and discover new features relevant to their workflows.

**Primary Benefit:** Users see critical migration requirements (ClusterTask removal, community tasks removal) FIRST, before reading about new features, dramatically reducing upgrade failure risk.

**Secondary Benefits:**
- Related monitoring capabilities consolidated (general monitoring + PAC metrics)
- Configuration workflows explicit (Chains signing with behavior change warning)
- Bug fixes organized by category for easier assessment

This structure is particularly effective for release notes because it prioritizes **what users must do** (migrate ClusterTasks) over **what's new** (features), aligning with the primary release notes job: safe upgrade planning.

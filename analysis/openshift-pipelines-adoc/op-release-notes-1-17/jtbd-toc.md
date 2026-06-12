# OpenShift Pipelines 1.17 Release Notes
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** Help users understand what's new, what's changed, and how to plan upgrades to OpenShift Pipelines 1.17

**Personas:** Platform Administrator, Pipeline Developer, DevOps Engineer

**Main Jobs:** 8 core jobs across 4 workflow stages

---

## Quick Navigation

**I want to:**
- Understand breaking changes before upgrading → Job 1 (Plan)
- Learn about removed features and alternatives → Job 2 (Plan)
- Configure multiple Git providers → Job 3 (Architecture)
- Set up granular pipeline monitoring → Job 4 (Architecture)
- Configure Tekton Chains signing → Job 5 (Architecture)
- Monitor Pipelines as Code metrics → Job 6 (Architecture)
- Customize Tekton Results metadata → Job 7 (Architecture)
- Review bug fixes and improvements → Job 8 (Reference)

---

# Table of Contents

## Plan Your Upgrade

### Job 1: Understand ClusterTask Removal and Migration Path
*When planning to upgrade to OpenShift Pipelines 1.17*

**Personas:** Platform Administrator, Pipeline Developer

**Timing:** BEFORE upgrading to 1.17 - pipelines using ClusterTask will fail after upgrade

**Why:** ClusterTask resources are removed; migration to cluster resolver is required to prevent pipeline failures

#### Breaking Change Overview

→ Lines 322-329: ClusterTask resource removal
  Source: What's New section

- **What's removed:** All ClusterTask resources from the Operator
- **Alternative:** Cluster resolver to access tasks in `openshift-pipelines` namespace
- **Required action:** Edit pipelines using ClusterTask resources before upgrade
- **Impact:** Pipeline execution failures if not migrated

#### Migration Requirements

- **Task:** Identify pipelines using ClusterTask
  - Audit current pipeline definitions
  - Locate all ClusterTask references
  
- **Task:** Update to cluster resolver
  → Lines 323-329: Migration instructions
  - Access tasks in `openshift-pipelines` namespace
  - Update pipeline YAML configurations

---

### Job 2: Understand Community Cluster Tasks Removal
*When evaluating dependencies on pre-installed tasks*

**Personas:** Pipeline Developer

**Timing:** BEFORE upgrading to 1.17 - community tasks will be unavailable

**Why:** Community cluster tasks are removed from the Operator; external access required

#### Removed Tasks Reference

→ Lines 331-341: Community cluster tasks removal
  Source: Deprecated and Removed Features section

- **Removed tasks:**
  - `argocd-task-sync-and-wait`
  - `git-cli`
  - `helm-upgrade-from-repo`
  - `helm-upgrade-from-source`
  - `jib-maven`
  - `kubeconfig-creator`
  - `pull-request`
  - `trigger-jenkins-job`

#### Alternative Access

- **Option A: Tekton Catalog** (For current needs)
  - Download from https://github.com/tektoncd/catalog
  - Manual installation required
  - Individual task management

- **Option B: Wait for Future Update** (For planned restoration)
  → Lines 331-341: Future plans
  - Tasks planned for restoration in future release
  - Monitor release notes for availability

---

## Understand New Capabilities

### Job 3: Configure Multiple Git Providers with Git Resolver
*When managing pipelines across multiple Git repositories*

**Personas:** DevOps Engineer, Platform Administrator

#### Multi-Provider Configuration Pattern

→ Lines 147-208: Git resolver multi-configuration
  Source: New Features and Enhancements section

**Goal:** Centralize Git provider configurations for pipeline task references

- **Task:** Define multiple Git configurations in TektonConfig CR
  - Add multiple provider entries (GitHub, GitLab, Bitbucket, etc.)
  - Add multiple configurations for same provider
  - Organize by configKey naming convention

- **Task:** Reference specific configurations in pipeline runs
  → Lines 193-208: configKey parameter usage
  - Use `configKey` parameter in task/pipeline references
  - Select appropriate Git configuration per run
  - Example: `configKey: test1` for specific configuration

#### Configuration Benefits

- **For multi-cloud environments:** Separate configs per cloud Git service
- **For different auth patterns:** Separate configs for SSH vs. HTTPS
- **For team isolation:** Separate configs per team/project

---

### Job 4: Implement Granular Pipeline Monitoring
*When tracking pipeline execution across namespaces and resources*

**Personas:** Platform Administrator, DevOps Engineer

#### Monitoring Level Selection

→ Lines 210-224: Granular monitoring levels
  Source: New Features and Enhancements section

**Goal:** Choose appropriate monitoring scope for operational needs

- **Level 1: Cluster** (Default)
  - Aggregate metrics across all namespaces
  - Best for: Platform-wide observability
  
- **Level 2: Namespace**
  - Metrics per namespace
  - Best for: Multi-tenant environments
  - Configure: `metrics.running-pipelinerun.level: namespace`
  
- **Level 3: Pipeline**
  - Metrics per pipeline definition
  - Best for: Detailed pipeline performance tracking
  - Configure: `metrics.running-pipelinerun.level: pipeline`
  
- **Level 4: PipelineRun**
  - Metrics per individual run
  - Best for: Fine-grained debugging
  - Configure: `metrics.running-pipelinerun.level: pipelinerun`

#### Configuration Implementation

- **Task:** Update TektonConfig CR
  → Lines 212-224: Parameter configuration
  - Set `metrics.running-pipelinerun.level` parameter
  - Choose appropriate granularity level
  - Consider resource overhead vs. visibility needs

#### Trade-offs

| Level | Visibility | Resource Cost | Use Case |
|-------|------------|---------------|----------|
| Cluster | Low | Minimal | Platform overview |
| Namespace | Medium | Low | Multi-tenant monitoring |
| Pipeline | High | Medium | Performance tuning |
| PipelineRun | Very High | Higher | Debugging specific runs |

---

### Job 5: Configure Tekton Chains for Artifact Signing
*When implementing software supply chain security*

**Personas:** Platform Administrator

#### Signing Key Generation Options

→ Lines 279-315: Tekton Chains configuration
  Source: New Features and Enhancements section

**Goal:** Establish automatic artifact signing without manual key management

- **Option A: Automatic ecdsa Key Generation** (New in 1.17)
  → Lines 279-294: generateSigningSecret configuration
  - Set `generateSigningSecret: true` in TektonConfig CR
  - Operator creates x509 key pair with ecdsa type
  - No manual key management required
  - **Best for:** Quick setup, production environments

- **Option B: Manual Key Management** (Previous approach)
  - Create signing secret manually
  - Configure Chains to use custom secret
  - **Best for:** Specific security requirements, HSM integration

#### Default Chains Configuration (Behavior Change)

→ Lines 296-315: Default Chains properties
  Source: New Features and Enhancements section

**Important:** If you do NOT explicitly configure Chains, the Operator now applies defaults

**New default properties:**
- `artifacts.taskrun.format: in-toto`
- `artifacts.taskrun.storage: tekton`
- `artifacts.oci.storage: oci`
- `transparency.enabled: true`

**Action required:** Review defaults against security policies before upgrade

#### Configuration Workflow

1. **Task:** Decide on key generation approach
   - Automatic (recommended) vs. Manual
   
2. **Task:** Configure TektonConfig CR
   → Lines 279-294: Configuration example
   - Set `generateSigningSecret` if using automatic
   - Verify Chains properties or accept defaults
   
3. **Task:** Verify signing operation
   - Check signing secret creation
   - Confirm artifact signing in pipeline runs

---

### Job 6: Monitor Pipelines as Code Execution
*When tracking pipeline performance in Pipelines as Code*

**Personas:** DevOps Engineer

#### New PAC Metrics Overview

→ Lines 246-249: Pipelines as Code metrics
  Source: New Features and Enhancements section

**Goal:** Track concurrent execution and performance trends

#### Running Count Metric

- **Metric:** `pipelines_as_code_running_pipelineruns_count`
  → Lines 246-247: Running count metric
  - Shows number of currently running PipelineRun resources
  - **Filter by repository:** Track per-repo concurrency
  - **Filter by namespace:** Track per-namespace load
  - **Use case:** Capacity planning, quota management

#### Duration Metric

- **Metric:** `pipelines_as_code_pipelinerun_duration_seconds_sum`
  → Lines 248-249: Duration metric
  - Shows total duration of all PipelineRun resources
  - **Filter dimensions:**
    - Repository
    - Namespace
    - PipelineRun status (Success, Failed, etc.)
    - Status change reason (detailed failure reason)
  - **Use cases:**
    - Performance trend analysis
    - Failure pattern identification
    - SLA monitoring

#### Monitoring Workflow

1. **Task:** Configure metrics collection
   - Ensure Pipelines as Code monitoring is enabled
   - Configure Prometheus/monitoring stack

2. **Task:** Create dashboards
   - Running count by repository
   - Duration trends by status
   - Failure analysis by reason

3. **Task:** Set up alerts
   - High concurrent run count
   - Duration threshold breaches
   - Failure rate increases

---

### Job 7: Customize Tekton Results Metadata Display
*When organizing pipeline execution results for analysis*

**Personas:** Platform Administrator

#### Summary Fields Configuration

→ Lines 253-274: Tekton Results summary fields
  Source: New Features and Enhancements section

**Goal:** Surface relevant labels and annotations in results tables for easier filtering and analysis

#### Configuration Approach

- **Task:** Identify relevant labels and annotations
  - Pipeline metadata (team, project, environment)
  - Task metadata (tool version, build type)
  - Custom business tags

- **Task:** Configure TektonResult CR
  → Lines 253-274: Summary fields configuration
  - Specify which labels to include in summary
  - Specify which annotations to include in summary
  - Labels and annotations appear in results table columns

#### Use Cases

| Metadata Type | Example | Benefit |
|---------------|---------|---------|
| Team ownership | `team: platform` | Filter by responsible team |
| Environment | `env: production` | Separate prod vs. dev results |
| Release version | `release: v1.2.3` | Track results by version |
| Build type | `build-type: nightly` | Analyze by build category |

#### Configuration Workflow

1. **Task:** Audit existing pipeline labels/annotations
   - Review current labeling conventions
   - Identify high-value metadata

2. **Task:** Update TektonResult CR
   - Add label selectors to summary fields
   - Add annotation selectors to summary fields

3. **Task:** Verify results table display
   - Confirm metadata appears in columns
   - Test filtering by summary fields

---

## Reference

### Job 8: Review Bug Fixes and Improvements
*When verifying issue resolution or understanding stability improvements*

**Personas:** DevOps Engineer, Pipeline Developer

#### Pipeline Execution Fixes

→ Lines 356-388: Pipeline run failure handling
  Source: Bug Fixes section

**Goal:** Understand resolved issues for reliable pipeline operation

#### Finally Tasks Fix

- **Issue:** Finally tasks did not run after validation failures
  → Lines 356-357: Finally task fix
  - **Fixed:** Finally tasks now consistently trigger even after validation failures
  - **Impact:** Reliable cleanup execution
  - **Benefit:** Improved resource cleanup and notification reliability

#### Status Reporting Fix

- **Issue:** Validation failures not accurately reported in status.message
  - **Fixed:** Validation failures now appear correctly in status field
  - **Impact:** Better failure diagnostics
  - **Benefit:** Faster troubleshooting

#### Pipelines as Code Fixes

**GitLab 20-File Limitation Fix**

→ Lines 367-368: GitLab .tekton directory fix
  Source: Bug Fixes section

- **Issue:** Pipeline runs failed when `.tekton` directory had >20 files
  - **Fixed:** Pipeline runs now start correctly regardless of file count
  - **Impact:** No arbitrary file limits in GitLab repositories
  - **Benefit:** Better organization flexibility for large pipeline configurations

#### Additional Bug Fixes

→ Lines 356-388: Complete bug fix list
  Source: Bug Fixes section

Review complete list of resolved issues including:
- TaskRun failure handling improvements
- Resource cleanup fixes
- Status reporting enhancements
- Edge case resolutions

---

## Appendices

### A. Migration Checklist

**Pre-Upgrade Actions:**

- [ ] **ClusterTask Migration (Critical)**
  - [ ] Identify all pipelines using ClusterTask
  - [ ] Update to cluster resolver pattern
  - [ ] Test updated pipelines
  
- [ ] **Community Tasks Migration**
  - [ ] Identify dependencies on removed tasks
  - [ ] Download from Tekton catalog if needed
  - [ ] Install required tasks in cluster

- [ ] **Chains Configuration Review**
  - [ ] Review new default Chains properties
  - [ ] Decide: accept defaults or customize
  - [ ] Configure generateSigningSecret if desired

**Post-Upgrade Validation:**

- [ ] Verify pipelines execute successfully
- [ ] Confirm finally tasks run correctly
- [ ] Check monitoring metrics at desired granularity
- [ ] Validate artifact signing operation (if using Chains)

---

### B. Feature Decision Matrix

| Feature | Who Benefits | When to Use | Configuration Required |
|---------|--------------|-------------|------------------------|
| Multi-Git resolver | Teams with multiple Git providers | Multiple GitHub/GitLab/Bitbucket repos | TektonConfig CR update |
| Granular monitoring | Platform teams, SREs | Multi-tenant environments | TektonConfig CR update |
| Auto signing keys | Security teams | Supply chain security needs | TektonConfig CR update |
| PAC metrics | DevOps teams using PAC | Performance tracking | Monitoring stack configuration |
| Results metadata | Teams with complex pipelines | Custom filtering needs | TektonResult CR update |

---

### C. Workflow Coverage Analysis

| Stage | Coverage | Jobs | Notes |
|-------|----------|------|-------|
| Plan | ✅ | Jobs 1-2 | Breaking changes, deprecations |
| Architecture | ✅ | Jobs 3-7 | New features, configuration patterns |
| Reference | ✅ | Job 8 | Bug fixes, compatibility |
| Configure | ⚠️ Limited | Embedded in Jobs 3-7 | Configuration steps within feature jobs |
| Deploy | ❌ | - | Not applicable for release notes |
| Monitor | ✅ | Jobs 4, 6 | Monitoring capabilities |
| Troubleshoot | ⚠️ Limited | Job 8 | Bug fixes improve troubleshooting |
| Upgrade | ✅ | Jobs 1-2 | Upgrade planning content |

### Gaps Identified

| Stage | Gap | Recommendation |
|-------|-----|----------------|
| Deploy | No deployment content | Release notes don't cover deployment; link to installation guide |
| Migrate | Limited migration details | Add detailed ClusterTask to cluster resolver migration procedure |
| Troubleshoot | No new troubleshooting features | Document improved error messages in future releases |

---

## Navigation Guide

### By User Journey

**Platform Administrator upgrading to 1.17:**
1. Job 1: Understand ClusterTask removal
2. Job 2: Review community tasks removal
3. Job 5: Configure Tekton Chains signing
4. Job 4: Set up granular monitoring
5. Job 8: Review bug fixes

**Pipeline Developer preparing for upgrade:**
1. Job 1: Migration path for ClusterTask
2. Job 2: Alternative sources for community tasks
3. Job 3: Multi-Git provider configuration (if applicable)
4. Job 8: Finally tasks fix verification

**DevOps Engineer optimizing operations:**
1. Job 6: Monitor Pipelines as Code metrics
2. Job 4: Granular monitoring implementation
3. Job 7: Customize Results metadata
4. Job 8: Review performance fixes

**Security-focused Administrator:**
1. Job 5: Tekton Chains automatic signing
2. Job 1: Understand breaking changes
3. Job 8: Review security-related fixes

---

## Document Statistics

**Workflow Coverage:**
- Plan: 2 jobs
- Architecture: 5 jobs
- Reference: 1 job
- Monitoring: 2 jobs (embedded)
- Migration: Content embedded in Jobs 1-2

**Main Jobs:** 8

**User Stories/Paths:** 15+

**Source Sections:** 8 distinct evidence ranges

**Component Coverage:**
- Tekton Pipelines core: Jobs 1, 2, 4, 8
- Tekton Chains: Job 5
- Pipelines as Code: Jobs 6, 8
- Tekton Results: Job 7
- Git resolver: Job 3

**Breaking Changes:** 2 (ClusterTask removal, Community tasks removal)

**New Features:** 5 major capabilities

**Bug Fixes:** 3+ documented improvements

---

## About This TOC

**Generated from:** JTBD analysis of OpenShift Pipelines 1.17 release notes

**Methodology:** Jobs-To-Be-Done framework applied to release notes content

**Purpose:** Help users navigate release notes by goals rather than sequential reading

**Note:** This is a RELEASE NOTES document (reference/concept material), not a procedural guide. For how-to procedures, consult the main OpenShift Pipelines documentation.

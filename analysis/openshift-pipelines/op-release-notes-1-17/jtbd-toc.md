# JTBD-Oriented TOC: OpenShift Pipelines 1.17 Release Notes

## Analysis Summary
- **Source Document**: op-release-notes-1-17
- **Initial JTBD Records**: 40
- **Consolidated Main Jobs**: 8
- **Date**: 2026-06-12

## Main Jobs (Consolidated)

### 1. Learn what's new in OpenShift Pipelines 1.17
**Why?** To understand new capabilities, improvements, and changes before upgrading or using new features.

**Current Approaches**:
- Compatibility and support matrix [reference]
- Release notes overview [reference]
- New features in Pipelines component [reference]
- New features in Operator component [reference]
- New features in Pipelines as Code [reference]
- New features in Tekton Results [reference]
- New features in Tekton Chains [reference]

**Source Evidence**:
- → Lines 89-123: Compatibility and support matrix
- → Lines 134-393: Release notes for OpenShift Pipelines GA 1.17

---

### 2. Configure and manage Git providers in pipelines
**Why?** To integrate multiple Git repositories and providers into pipeline workflows.

**Current Approaches**:
- Configure multiple Git providers using Git resolver [procedure]
- Specify Git configuration in task runs and pipeline runs [procedure]

**Source Evidence**:
- → Lines 147-208: Configure multiple Git providers by using the Git resolver

---

### 3. Monitor and track pipeline execution
**Why?** To observe pipeline performance, identify bottlenecks, and track resource usage.

**Current Approaches**:
- Configure monitoring level for PipelineRun resources [procedure]
- Track user execution via ID labels [reference]
- Monitor running PipelineRun count in Pipelines as Code [reference]
- Track total duration of PipelineRun resources [reference]

**Source Evidence**:
- → Lines 210-224: Monitor running PipelineRun resources at namespace/pipeline/pipelinerun level
- → Lines 226-227: User ID labels in YAML manifests
- → Lines 246-247: pipelines_as_code_running_pipelineruns_count metric
- → Lines 248-249: pipelines_as_code_pipelinerun_duration_seconds_sum metric

---

### 4. Optimize pipeline performance and resource usage
**Why?** To improve pipeline execution speed and manage cluster resources efficiently.

**Current Approaches**:
- Apply performance tuning values to all controllers [procedure]
- Apply security context constraints [reference]
- Configure LimitRange settings [reference]
- Mount workspaces only in specified steps [reference]

**Source Evidence**:
- → Lines 228-229: Configure performance tuning in TektonConfig CR
- → Lines 241: Ephemeral volume setting of SCC application
- → Lines 385: LimitRange overrides default container resource requirements
- → Lines 381: Workspace mounted only in specified steps

---

### 5. Configure Tekton components (Results and Chains)
**Why?** To customize artifact signing, result storage, and metadata tracking.

**Current Approaches**:
- Include custom labels and annotations in Tekton Results [procedure]
- Generate ecdsa key pairs for artifact signing [procedure]
- Use default Tekton Chains configuration [reference]
- Extract mongo-server-url from custom file paths [reference]

**Source Evidence**:
- → Lines 253-274: Configure summary fields in TektonResult CR
- → Lines 279-294: Generate x509 key pair of ecdsa type
- → Lines 296-315: Default Chains configuration properties
- → Lines 317-318: storage.docdb.mongo-server-url-path parameter

---

### 6. Migrate from deprecated features
**Why?** To ensure pipelines continue working after upgrading to version 1.17.

**Current Approaches**:
- Migrate from ClusterTask resources to cluster resolver [procedure]
- Replace removed community cluster tasks [procedure]

**Source Evidence**:
- → Lines 322-329: ClusterTask resource removed from Operator
- → Lines 331-340: Community cluster tasks removed, download from Tekton catalog

---

### 7. Use Operator tasks and commands
**Why?** To execute pipeline tasks with advanced options and parameters.

**Current Approaches**:
- Run skopeo-copy with additional arguments [procedure]
- Copy multiple images with skopeo-copy task [procedure]
- Read large Tekton bundles [reference]

**Source Evidence**:
- → Lines 233-239: Run skopeo-copy command with --all and --preserve-digests
- → Lines 351: Use url.txt file for multiple image copying
- → Lines 389: Correct handling of large Tekton bundles

---

### 8. Troubleshoot pipeline and task run issues
**Why?** To identify and resolve failures in pipeline execution.

**Current Approaches**:
- Handle GitLab push events without commits [reference]
- Handle GitLab tag delete events [reference]
- Resolve Bitbucket server variables and fields [reference]
- Handle pipeline run validation failures [reference]
- Handle out-of-memory pod failures [reference]
- Process array results from CustomRun resources [reference]
- Record task run step statuses accurately [reference]
- Mark subsequent steps as skipped after failures [reference]
- Execute finally tasks after validation failures [reference]
- Start pipeline runs with many .tekton files [reference]
- Handle incorrect BitBucket event payloads [reference]
- Clean up temporary Git authentication secrets [reference]
- Match tag events in BitBucket [reference]
- Record task specifications when canceled [reference]
- Record task steps accurately in Tekton Chains [reference]
- Handle pipeline run timeouts correctly [reference]
- Manage concurrency queue in busy clusters [reference]
- Identify validation failure status [reference]
- View skipped tasks correctly [reference]

**Source Evidence**:
- → Lines 345-391: Fixed issues section covering 20+ resolved bugs

---

## Proposed Structure

```
Release notes for Red Hat OpenShift Pipelines 1.17

├── Compatibility and support matrix
│   └── Version compatibility table
│
├── What's new in OpenShift Pipelines 1.17
│   ├── New features in Pipelines
│   ├── New features in Operator
│   ├── New features in Pipelines as Code
│   ├── New features in Tekton Results
│   └── New features in Tekton Chains
│
├── Breaking changes
│   ├── ClusterTask resource removal
│   └── Community cluster tasks removal
│
└── Fixed issues
    ├── Pipelines as Code fixes
    ├── Operator and task fixes
    ├── Tekton Chains fixes
    └── General pipeline execution fixes
```

## Consolidation Notes

**Main Job #1** consolidates all "learn about new features" jobs since users consult release notes with the primary goal of understanding what changed.

**Main Job #2** focuses specifically on Git provider configuration, a significant new feature.

**Main Job #3** consolidates all monitoring and tracking jobs since they share the common goal of observing pipeline behavior.

**Main Job #4** groups performance and resource optimization features.

**Main Job #5** groups Tekton Results and Chains configuration jobs.

**Main Job #6** addresses migration from deprecated features, critical for upgrade planning.

**Main Job #7** consolidates Operator task usage jobs.

**Main Job #8** consolidates all fixed issues since users troubleshooting problems look for known issue resolutions.

## Why? Ladder Test Results

| Main Job | Pass/Fail | Reasoning |
|----------|-----------|-----------|
| 1. Learn what's new | ✓ Pass | Can't go higher - this is the top-level goal when reading release notes |
| 2. Configure Git providers | ✓ Pass | Serves Job #1 (part of learning new features) |
| 3. Monitor pipeline execution | ✓ Pass | Serves operational goals, not just learning |
| 4. Optimize performance | ✓ Pass | Serves operational goals, not just learning |
| 5. Configure Tekton components | ✓ Pass | Serves operational goals, not just learning |
| 6. Migrate from deprecated features | ✓ Pass | Serves upgrade planning, not just learning |
| 7. Use Operator tasks | ✓ Pass | Serves operational goals, not just learning |
| 8. Troubleshoot issues | ✓ Pass | Serves problem resolution, not just learning |

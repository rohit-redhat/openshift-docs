# Structure Comparison: OpenShift Pipelines 1.17 Release Notes

## Current Structure → Proposed JTBD Structure

### Overview
- **Document**: op-release-notes-1-17
- **Current Approach**: Feature-component organization (Pipelines, Operator, PAC, Results, Chains)
- **Proposed Approach**: Job-to-be-done organization
- **Date**: 2026-06-12

---

## Side-by-Side Comparison

| Current Structure | Proposed JTBD Structure |
|-------------------|------------------------|
| **Release notes for Red Hat OpenShift Pipelines 1.17** | **Release notes for Red Hat OpenShift Pipelines 1.17** |
| | |
| **Compatibility and support matrix** | **1. Learn what's new in OpenShift Pipelines 1.17** |
| - Version compatibility table | - Compatibility and support matrix |
| - Component versions | - Overview of new features |
| - OpenShift version support | - Breaking changes summary |
| - Support status (GA/TP) | - Fixed issues summary |
| | |
| **New features** | **2. Configure and manage Git providers in pipelines** |
| → Pipelines | - Configure multiple Git providers using Git resolver |
| → Operator | - Specify Git configuration in task runs and pipeline runs |
| → Pipelines as Code | |
| → Tekton Results | **3. Monitor and track pipeline execution** |
| → Tekton Chains | - Configure monitoring level for PipelineRun resources |
| | - Track user execution via ID labels |
| | - Monitor running PipelineRun count in Pipelines as Code |
| | - Track total duration of PipelineRun resources |
| | |
| **Breaking changes** | **4. Optimize pipeline performance and resource usage** |
| - ClusterTask resource removal | - Apply performance tuning values to all controllers |
| - Community cluster tasks removal | - Apply security context constraints |
| | - Configure LimitRange settings |
| | - Mount workspaces only in specified steps |
| | |
| **Fixed issues** | **5. Configure Tekton components (Results and Chains)** |
| - Pipelines as Code fixes | - Include custom labels and annotations in Tekton Results |
| - Operator and task fixes | - Generate ecdsa key pairs for artifact signing |
| - Tekton Chains fixes | - Use default Tekton Chains configuration |
| - General pipeline execution fixes | - Extract mongo-server-url from custom file paths |
| | |
| | **6. Migrate from deprecated features** |
| | - Migrate from ClusterTask resources to cluster resolver |
| | - Replace removed community cluster tasks |
| | |
| | **7. Use Operator tasks and commands** |
| | - Run skopeo-copy with additional arguments |
| | - Copy multiple images with skopeo-copy task |
| | - Read large Tekton bundles |
| | |
| | **8. Troubleshoot pipeline and task run issues** |
| | - Handle GitLab and BitBucket event issues |
| | - Resolve variable and field resolution problems |
| | - Fix pipeline run validation and failure handling |
| | - Address resource management issues |
| | - Correct task run status recording |

---

## Detailed Mapping

### Current: Compatibility and support matrix
**Maps to**: JTBD Job #1 (Learn what's new)
- **Rationale**: Understanding compatibility is part of learning what's new and planning upgrades
- **Change**: Integrated into comprehensive "What's new" section

---

### Current: New features → Pipelines
**Maps to**: Multiple JTBD Jobs
- **Job #2**: Configure Git providers (lines 147-208)
- **Job #3**: Monitor PipelineRun resources (lines 210-224)
- **Job #3**: Track user execution (lines 226-227)
- **Job #4**: Apply performance tuning (lines 228-229)
- **Rationale**: Single component section split by actual user goals

---

### Current: New features → Operator
**Maps to**: JTBD Job #7 (Use Operator tasks)
- **Job #7**: Run skopeo-copy with arguments (lines 233-239)
- **Job #4**: Apply SCC settings (line 241)
- **Rationale**: Grouped by operational task execution goal

---

### Current: New features → Pipelines as Code
**Maps to**: JTBD Job #3 (Monitor pipeline execution)
- **Job #3**: Monitor running PipelineRun count (lines 246-247)
- **Job #3**: Track PipelineRun duration (lines 248-249)
- **Rationale**: Monitoring features grouped together regardless of component

---

### Current: New features → Tekton Results
**Maps to**: JTBD Job #5 (Configure Tekton components)
- **Job #5**: Configure summary labels and annotations (lines 253-274)
- **Rationale**: Configuration task grouped with other Tekton component configuration

---

### Current: New features → Tekton Chains
**Maps to**: JTBD Job #5 (Configure Tekton components)
- **Job #5**: Generate ecdsa key pairs (lines 279-294)
- **Job #5**: Use default Chains configuration (lines 296-315)
- **Job #5**: Extract mongo-server-url (lines 317-318)
- **Rationale**: All Chains configuration grouped together by goal

---

### Current: Breaking changes
**Maps to**: JTBD Job #6 (Migrate from deprecated features)
- **Job #6**: Migrate from ClusterTask (lines 322-329)
- **Job #6**: Replace community cluster tasks (lines 331-340)
- **Rationale**: Breaking changes reframed as migration actions
- **Change**: Action-oriented instead of warning-oriented

---

### Current: Fixed issues
**Maps to**: JTBD Job #8 (Troubleshoot issues)
- **All 20+ fixed issues** (lines 345-391)
- **Rationale**: Users troubleshooting look for issue resolutions
- **Change**: Grouped by problem domain (GitLab/BitBucket events, validation, resource management, status recording)

---

## Key Structural Changes

### 1. Component-Based → Goal-Based Organization
**Current**: Features organized by component (Pipelines, Operator, PAC, Results, Chains)
**Proposed**: Features organized by user goal (configure, monitor, optimize, troubleshoot)

**Benefit**: Users find information based on what they want to accomplish, not which component provides it.

---

### 2. Integrated Compatibility Information
**Current**: Standalone compatibility matrix section
**Proposed**: Integrated into "Learn what's new" job

**Benefit**: Users learning about the release see compatibility requirements in context.

---

### 3. Action-Oriented Migration Guidance
**Current**: "Breaking changes" (passive, warning)
**Proposed**: "Migrate from deprecated features" (active, instructional)

**Benefit**: Users focus on required actions rather than just warnings.

---

### 4. Grouped Monitoring Features
**Current**: Monitoring features scattered across Pipelines and PAC sections
**Proposed**: All monitoring features in Job #3

**Benefit**: Users seeking monitoring capabilities find all options in one place.

---

### 5. Consolidated Troubleshooting
**Current**: Fixed issues listed chronologically or by component
**Proposed**: Fixed issues grouped by problem domain

**Benefit**: Users troubleshooting specific types of issues find relevant fixes faster.

---

## Information Architecture Changes

### Reduction in Top-Level Sections
- **Current**: 4 top-level sections (Compatibility, New features, Breaking changes, Fixed issues)
- **Proposed**: 8 job-oriented sections
- **Net Change**: +4 sections, but with clearer purpose and scope

### Information Depth Changes
- **Current**: 2-3 levels deep (Section → Component → Feature)
- **Proposed**: 2-3 levels deep (Job → Approach → Details)
- **Net Change**: Similar depth, better organization by goal

### Cross-Component Integration
- **Current**: Features isolated by component
- **Proposed**: Related features grouped by goal across components
- **Example**: All monitoring features together regardless of component

---

## User Impact Analysis

### For Administrators Planning Upgrades
**Current Path**: 
1. Read compatibility matrix
2. Scan all "New features" subsections
3. Read "Breaking changes"
4. Review "Fixed issues"

**Proposed Path**:
1. Read Job #1 (Learn what's new) for overview
2. Read Job #6 (Migrate from deprecated features) for required actions
3. Review specific jobs for features of interest

**Improvement**: More efficient upgrade planning with consolidated view.

---

### For Users Seeking New Capabilities
**Current Path**:
1. Read all component sections under "New features"
2. Infer which features apply to their goals

**Proposed Path**:
1. Identify relevant job (configure, monitor, optimize)
2. Read approaches within that job

**Improvement**: Faster discovery of relevant features.

---

### For Users Troubleshooting Issues
**Current Path**:
1. Scan entire "Fixed issues" list
2. Search for symptoms or error messages

**Proposed Path**:
1. Navigate to Job #8 (Troubleshoot)
2. Review fixes grouped by problem domain

**Improvement**: Faster issue resolution with domain grouping.

---

## Content Gaps Identified

### Missing Content for Complete Job Support

**Job #2: Configure Git providers**
- ✗ Prerequisites for Git provider configuration
- ✗ Verification steps after configuration
- ✗ Troubleshooting common Git resolver issues

**Job #3: Monitor pipeline execution**
- ✗ How to access and interpret metrics
- ✗ Metric retention and storage considerations
- ✗ Integration with external monitoring tools

**Job #4: Optimize performance**
- ✗ Performance tuning value recommendations
- ✗ Resource requirement calculation guidance
- ✗ Performance benchmarking procedures

**Job #6: Migrate from deprecated features**
- ✗ Step-by-step migration procedures
- ✗ Verification steps after migration
- ✗ Rollback procedures if migration fails

**Job #8: Troubleshoot issues**
- ✗ Diagnostic procedures for identifying issues
- ✗ Log file locations and interpretation
- ✗ Support case opening procedures

---

## Migration Effort Assessment

### Content Reorganization Required
- **Effort**: Medium
- **Reason**: Content exists but needs regrouping and cross-referencing

### New Content Creation Required
- **Effort**: High
- **Reason**: Significant gaps in procedural and troubleshooting content

### Cross-Reference Updates Required
- **Effort**: Medium
- **Reason**: Many internal and external links will need updating

---

## Recommendations

### Phase 1: Quick Wins (Low Effort, High Impact)
1. Add executive summary to Job #1 with compatibility matrix
2. Rename "Breaking changes" to "Migrate from deprecated features"
3. Group fixed issues by problem domain in Job #8

### Phase 2: Structural Reorganization (Medium Effort)
1. Reorganize new features by job instead of component
2. Consolidate monitoring features into Job #3
3. Create cross-component groupings for Jobs #4-#7

### Phase 3: Content Enhancement (High Effort)
1. Add missing prerequisites and verification steps
2. Create step-by-step migration procedures
3. Develop comprehensive troubleshooting procedures
4. Add metric access and interpretation guidance

---

## Conclusion

The proposed JTBD structure transforms release notes from a component-focused changelog into a goal-oriented reference. Users can more efficiently find information relevant to their specific jobs: learning about changes, configuring features, monitoring execution, optimizing performance, migrating from deprecated features, and troubleshooting issues.

**Key Benefit**: Reduced time-to-value for users consulting release notes, with clearer paths to accomplishing their goals.

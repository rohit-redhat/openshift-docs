# Red Hat OpenShift Pipelines 1.19 Release Notes
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** Help users understand new features, breaking changes, and fixes in OpenShift Pipelines 1.19 to make informed upgrade and adoption decisions.

**Personas:** Platform administrator, Pipeline developer, Pipeline administrator

**Main Jobs:** 3 core jobs across 6 workflow stages

---

## Quick Navigation

**I want to:**
- Review what's new in this release -> Job 1 (What's New)
- Check version compatibility before upgrading -> Job 2 (Plan)
- Understand breaking changes and migration needs -> Job 1 (What's New - Breaking Changes section)
- Find fixes for issues in my environment -> Job 1 (What's New - Fixed Issues section)
- Configure new features -> Job 3 (Configure/Operate)

---

# Table of Contents

## What's New

### Job 1: Understand Features and Fixes in This Release
*When planning upgrades or evaluating new capabilities*

**Personas:** Platform administrator, Pipeline developer, Pipeline administrator

#### New Features by Component

**1.1. Pipelines Component Features** `[reference]`
→ Lines 143-182: EventListener custom securityContext
  Source: Release notes 1.19, Pipelines section
  - Configure custom security settings for EventListener resources
  - Override default securityContext with user-defined values
  - Meet organizational security policies

**1.2. Tekton Results Features** `[reference]`
→ Lines 187-350: Multiple Tekton Results enhancements
  Source: Release notes 1.19, Tekton Results section
  - Custom database credentials (lines 187-201)
  - Response field filtering for API optimization (lines 203-204)
  - OCI bundle retry configuration (lines 206-232)
  - Git resolver personal access tokens (lines 234-260)
  - SQL log level configuration (lines 262-283)
  - Watcher reconciliation retries (lines 285-286)
  - Splunk log retrieval integration (lines 288-313)
  - StatefulSet ordinals for HA (Technology Preview, lines 315-350)

**1.3. Pipelines as Code Features** `[reference]`
→ Lines 355-611: Pipelines as Code enhancements
  Source: Release notes 1.19, Pipelines as Code section
  - Silent unauthorized bot handling (lines 355-356)
  - Git provider API request metrics (lines 357-358)
  - Repository URL validation (lines 359-360)
  - Bitbucket markdown rendering (lines 361-362)
  - Git provider API request count metric (lines 518-519)
  - Global cancel-in-progress configuration (lines 520-548)
  - git_tag dynamic variable (lines 550-576)
  - skip-push-event-for-pr-commits (lines 578-606)
  - OpenAPI schema for Repository CR (lines 608-609)
  - CEL expression precedence warnings (lines 610-611)

**1.4. Operator Features** `[reference]`
→ Lines 366-396: Operator enhancements
  Source: Release notes 1.19, Operator section
  - Cosign key pair generation (lines 366-380)
  - Disable ok-to-test memory by default (lines 382-383)
  - Dynamic variable expansion from remote pipelines (lines 384-385)
  - Native git binary for remote resolution (lines 387-388)
  - onError parameter substitution (lines 389-390)
  - StepAction stable and enabled by default (lines 391-392)
  - Improved fan-out/fan-in result evaluation (lines 393-394)
  - remember-ok-to-test default to false (lines 395-396)

**1.5. Tekton Cache Features** `[reference]`
→ Lines 399-476: Tekton Cache enhancements
  Source: Release notes 1.19, Tekton Cache section
  - Unified parameter naming (lines 399-400)
  - Google Cloud Storage support (lines 401-403)
  - S3 compatible storage support (lines 404-405)
  - Gzip compression for caches (lines 406-407)
  - 0777 default permissions for restored caches (lines 408-410)
  - GKE Workload Identity Federation support (lines 411-412)
  - Unified storage backend code paths (lines 413-414)
  - Automatic destination folder creation (lines 415-417)
  - Custom Docker config location (lines 418-476)

**1.6. Tekton Chains Features** `[reference]`
→ Lines 481-513: Tekton Chains enhancements
  Source: Release notes 1.19, Tekton Chains section
  - StatefulSet ordinals for HA (Technology Preview)

**1.7. Event-based Pruner Features** `[reference]`
→ Lines 630-655: Event-based Pruner capabilities (Technology Preview)
  Source: Release notes 1.19, Pruner section
  - Time-based pruning (TTL)
  - History-based pruning
  - Flexible configuration levels (Global and Namespace)

#### Breaking Changes

**1.8. API and CLI Changes** `[reference]`
→ Lines 660-667: Breaking changes requiring migration
  Source: Release notes 1.19, Breaking changes section
  
**Timing:** BEFORE upgrading to 1.19 - review and plan migrations

- **hub clustertask command removed** (lines 660-661)
  - ClusterTask functionality no longer available on Tekton Hub
  - Update workflows that use this command
  
- **ClusterTask support removed** (lines 662-663)
  - tkn clustertask and tkn task create commands no longer available
  - Migrate to namespaced Task resources
  
- **opc results list command replaced** (lines 664-665)
  - Use `opc results result list` instead
  - Update scripts and automation
  
- **disable-affinity-assistant flag removed** (lines 666-667)
  - Flag deprecated in v1.13, removed in v1.19
  - Use `coschedule` feature flag instead for equivalent behavior

#### Known Issues

**1.9. Known Limitations** `[reference]`
→ Lines 671-672: Current known issues
  Source: Release notes 1.19, Known issues section
  
- **Event-based pruner config validation**
  - Invalid configuration silently ignored
  - Verify configuration is applied correctly
  - Pruner may fall back to default behavior

#### Fixed Issues

**1.10. Bug Fixes Across Components** `[reference]`
→ Lines 674-758: Comprehensive list of resolved issues
  Source: Release notes 1.19, Fixed issues section
  - s2i-java task script path fixes
  - YAML validation error reporting in pull requests
  - GitLab comment strategy improvements
  - AWS S3 log ordering fixes
  - Numerous Pipelines as Code improvements
  - Web console display and styling fixes
  - Tekton Results isolation improvements
  - CLI and cache operation fixes

---

## Plan Your Upgrade

### Job 2: Verify Component Version Compatibility
*When planning deployment or upgrades*

**Personas:** Platform administrator

**Timing:** BEFORE deploying or upgrading - incompatible versions are not supported

→ Lines 89-123: Compatibility and support matrix
  Source: Compatibility and support matrix section

- **Version 1.22 compatibility** (current latest)
  - OpenShift versions: 4.14, 4.16, 4.17, 4.18, 4.19, 4.20, 4.21
  - Component versions: Pipelines 1.9.x, Triggers 0.35.x, CLI 0.44.x
  - Support status by component (GA vs Technology Preview)

- **Version 1.19 compatibility** (this release)
  - Review component version matrix
  - Identify Technology Preview vs GA components
  - Verify OpenShift version support

- **Lifecycle and support policies**
  - OpenShift Operator Life Cycles
  - Red Hat OpenShift Container Platform Life Cycle Policy

---

## Configure and Use New Features

### Job 3: Configure and Operate New Capabilities
*When adopting new features from this release*

**Personas:** Platform administrator, Pipeline developer

**Requires:** Version 1.19 installed, understanding of feature prerequisites

#### Security and Authentication

**3.1. Configure Custom Security Contexts** `[procedure]`
→ Lines 146-182: EventListener custom securityContext
  Source: Pipelines section
  - Context: When deploying event listeners with specific security requirements

**3.2. Configure Custom Database Credentials** `[procedure]`
→ Lines 187-201: Tekton Results database credentials
  Source: Tekton Results section
  - Context: When setting up Tekton Results with organizational database standards

**3.3. Authenticate Git Resolver with Personal Access Tokens** `[procedure]`
→ Lines 234-260: Git resolver authentication
  Source: Tekton Results section
  - Context: When resolving pipeline definitions from GitHub or GitLab
  - Benefit: Avoid rate limits on anonymous git clone operations

**3.4. Configure GKE Workload Identity Federation** `[procedure]`
→ Lines 411-412: GKE WIF support
  Source: Tekton Cache section
  - Context: When running pipelines on GKE with Workload Identity Federation
  - Benefit: Eliminate long-lived credentials

**3.5. Generate Cosign Key Pairs Automatically** `[procedure]`
→ Lines 366-380: Cosign key generation
  Source: Operator section
  - Context: When setting up Tekton Chains for artifact signing

#### Performance and Optimization

**3.6. Configure OCI Bundle Retry Timing** `[procedure]`
→ Lines 206-232: Bundle resolver backoff configuration
  Source: Tekton Results section
  - Context: When using OCI bundles with busy or rate-limited registries

**3.7. Enable Response Field Filtering** `[procedure]`
→ Lines 203-204: API field filtering
  Source: Tekton Results section
  - Context: When retrieving large result sets from Tekton Results API

**3.8. Configure Native Git Binary for Remote Resolution** `[concept]`
→ Lines 387-388: Native git binary
  Source: Operator section
  - Context: Performance improvement for large repositories
  - Benefit: Reduced memory consumption and improved clone performance

**3.9. Enable Gzip Compression for Caches** `[concept]`
→ Lines 406-407: Cache compression
  Source: Tekton Cache section
  - Context: Automatic compression before upload
  - Benefit: Reduced storage costs and faster transfers

#### High Availability

**3.10. Configure StatefulSet Ordinals for HA (Technology Preview)** `[procedure]`
→ Lines 315-350: Tekton Results watcher HA
→ Lines 481-513: Tekton Chains controller HA
  Source: Tekton Results and Tekton Chains sections
  - Context: When scaling for high availability
  - Benefit: Improved workload distribution vs leader election

#### Storage Backend Configuration

**3.11. Configure Alternative Cache Storage Backends** `[procedure]`
→ Lines 401-403: Google Cloud Storage support
→ Lines 404-405: S3 compatible storage support
  Source: Tekton Cache section
  - Context: When storing build caches in cloud or on-premises object storage
  - Options:
    - GCS buckets (gs://bucket/path)
    - S3-compatible storage including MinIO (s3://bucket/path)

**3.12. Configure Custom Docker Config Location** `[procedure]`
→ Lines 418-476: Custom dockerConfig parameter
  Source: Tekton Cache section
  - Context: When using registry authentication with non-default credential paths

#### Pipeline Automation

**3.13. Configure Global Cancel-in-Progress** `[procedure]`
→ Lines 520-548: Global auto-cancel configuration
  Source: Pipelines as Code section
  - Context: When managing multiple repositories with Pipelines as Code
  - Benefit: Prevent redundant pipeline runs across all repos

**3.14. Configure Skip-Push-Event for PR Commits** `[procedure]`
→ Lines 578-606: Duplicate run prevention
  Source: Pipelines as Code section
  - Context: When managing pipeline triggers
  - Benefit: Skip push events for commits already in pull requests

**3.15. Use git_tag Dynamic Variable** `[procedure]`
→ Lines 550-576: git_tag variable usage
  Source: Pipelines as Code section
  - Context: When triggering pipelines on tag push events

**3.16. Use onError Parameter Substitution** `[procedure]`
→ Lines 389-390: Dynamic error handling
  Source: Operator section
  - Context: When controlling pipeline failure handling dynamically

#### Resource Management

**3.17. Configure Event-based Pruner (Technology Preview)** `[procedure]`
→ Lines 630-655: Automated cleanup configuration
  Source: Event-based Pruner section
  - Context: When managing PipelineRun and TaskRun lifecycle
  - Features:
    - Time-based pruning (TTL)
    - History-based pruning (success/failed limits)
    - Global and Namespace configuration levels
  - **Requires:** Existing job-based pruner must be disabled first

#### Developer Experience

**3.18. Use OpenAPI Schema for Repository CR** `[concept]`
→ Lines 608-609: OpenAPI schema support
  Source: Pipelines as Code section
  - Context: When writing Repository CRs
  - Benefit: IDE autocompletion and oc explain support

**3.19. Use StepAction Definitions** `[concept]`
→ Lines 391-392: StepAction graduation to stable
  Source: Operator section
  - Context: StepAction enabled by default as stable feature
  - Benefit: No feature flags required

#### Monitoring and Observability

**3.20. Monitor Git Provider API Usage** `[procedure]`
→ Lines 357-358: API request metrics
→ Lines 518-519: git_provider_api_request_count metric
  Source: Pipelines as Code section
  - Context: When monitoring Pipelines as Code integration with Git providers
  - Benefit: Track rate limit usage per provider, namespace, and event type

**3.21. Configure SQL Log Level** `[procedure]`
→ Lines 262-283: SQL_LOG_LEVEL environment variable
  Source: Tekton Results section
  - Context: When debugging Tekton Results database issues

**3.22. Retrieve Logs from Splunk** `[procedure]`
→ Lines 288-313: Splunk integration
  Source: Tekton Results section
  - Context: When using OpenShift Logging with Splunk forwarding
  - Benefit: Centralized log management and analysis

---

## Appendices

### A. Technology Preview Features Quick Reference

| Feature | Component | Lines | Status |
|---------|-----------|-------|--------|
| StatefulSet ordinals for HA | Tekton Results | 315-350 | TP |
| StatefulSet ordinals for HA | Tekton Chains | 481-513 | TP |
| Event-based Pruner | Pruner | 630-655 | TP |

**Note:** Technology Preview features are not supported with Red Hat production SLAs.

---

### B. Breaking Changes Migration Guide

| Change | Migration Action | Impact |
|--------|------------------|--------|
| hub clustertask removed | Remove usage of this command | Workflows using Tekton Hub ClusterTask |
| ClusterTask support removed | Migrate to namespaced Task resources | All ClusterTask users |
| opc results list changed | Update to `opc results result list` | Scripts and automation |
| disable-affinity-assistant removed | Use `coschedule` feature flag | Affinity configuration |

---

### C. Workflow Coverage Analysis

| Stage | Coverage | Jobs | Notes |
|-------|----------|------|-------|
| What's New | ✅ | Job 1 | Comprehensive release notes coverage |
| Plan | ✅ | Job 2 | Version compatibility verification |
| Configure | ✅ | Job 3 | New feature configuration |
| Operate | ✅ | Job 3 | New operational capabilities |
| Monitor | ✅ | Job 3 | Observability features |
| Secure | ✅ | Job 3 | Security enhancements |
| Troubleshoot | ✅ | Job 3 | SQL logging, known issues |
| Upgrade | ✅ | Job 1, Job 2 | Breaking changes and compatibility |

### Gaps Identified

| Stage | Gap | Recommendation |
|-------|-----|----------------|
| N/A | No significant gaps | Release notes comprehensively cover all workflow stages |

---

## Navigation Guide

### By User Journey

**Platform Administrator upgrading to 1.19:**
1. Job 2: Verify component version compatibility
2. Job 1: Review breaking changes (section 1.8)
3. Job 1: Review fixed issues (section 1.10)
4. Job 3: Configure new features as needed

**Pipeline Developer adopting new features:**
1. Job 1: Review new features by component
2. Job 3: Configure specific features for your use case
3. Job 1: Check known issues (section 1.9)

**Pipeline Administrator managing operations:**
1. Job 3: Configure monitoring (sections 3.20-3.22)
2. Job 3: Configure resource management (section 3.17)
3. Job 3: Configure pipeline automation (sections 3.13-3.16)

---

## Document Statistics

**Workflow Coverage:**
- What's New: 1 job
- Plan: 1 job
- Configure: 1 job (22 sub-approaches)
- Operate: Covered in Job 3
- Monitor: Covered in Job 3
- Secure: Covered in Job 3
- Troubleshoot: Covered in Job 3
- Upgrade: Covered in Jobs 1-2

**Main Jobs:** 3

**User Stories/Paths:** 22 configuration and operational approaches

**Source Sections:** 6 major sections (Compatibility, 5 release note modules)

**Technology Preview Features:** 3

**Breaking Changes:** 4

# Remote Pipelines, Tasks, and Resolvers — Consolidation Report

**Document:** remote-pipelines-tasks-resolvers-consolidation.md  
**JTBD Records:** 26 source records → 11 final jobs (after consolidation)  
**Analysis Date:** 2026-06-11  
**Source Document:** remote-pipelines-tasks-resolvers.adoc

---

## Executive Summary

### What's Changing

The current documentation organizes content by **resolver type** (Hub, Bundles, Git, HTTP, Cluster), following a repetitive concept → configuration → usage pattern for each of the six resolver variations. This structure forces users to navigate through 21 top-level sections organized by technology implementation rather than by their actual goals.

This causes several pain points: (1) Platform administrators configuring resolvers must jump between 6 separate configuration sections when setting up their cluster; (2) Developers looking for standard tasks must scroll past all resolver documentation to find reference material buried at the end; (3) Users trying to understand versioning strategies find this critical planning content hidden in a final section with no prominence.

The proposed JTBD-based structure organizes content by **user goals and workflow stages** (Understand → Configure → Discover → Plan). Each of the 11 jobs represents a distinct outcome users want to achieve, consolidating related resolver content into unified jobs with clear sub-sections.

### Key Improvements

- **Resolver concept consolidation:** 6 separate "About X resolver" sections → 1 unified Job 1 covering all resolver concepts
- **Configuration workflow integration:** Each resolver's concept/config/usage split → Single jobs (2-7) with integrated understand/configure/use sub-sections
- **Task discovery organization:** 3 scattered reference sections → 3 purpose-driven discovery jobs (standard tasks, community tasks, step actions)
- **Git resolver consolidation:** 9 separate Git sections (3 anonymous + 6 authenticated) → 2 unified jobs organized by access pattern
- **Versioning strategy elevation:** Buried final section → Dedicated Job 11 (Plan stage) for production readiness
- **Navigation reduction:** 48% reduction in top-level items (21 sections → 11 jobs)
- **Predictable sub-section structure:** X.1 = understand, X.2 = configure, X.3 = use (consistent across all resolver jobs)
- **Prerequisite transparency:** Each job clearly states required permissions, resources, and prior configuration

---

## Current Structure (Feature-Based)

The current assembly (`remote-pipelines-tasks-resolvers.adoc`) is organized by **resolver technology type**:

- **Introduction** — Overview of 5 resolver types and concept of remote resource reuse
- **Hub Resolver** — Public catalog access (Artifact Hub, Tekton Hub)
  - About Hub resolver (concept)
  - Configuring the hub resolver (admin task)
  - Specifying using hub resolver (developer task)
- **Bundles Resolver** — OCI bundle distribution via container registries
  - About Bundles resolver (concept)
  - Configuring the bundles resolver (admin task)
  - Specifying using bundles resolver (developer task)
- **Git Resolver (Anonymous)** — Public Git repository access
  - About Git resolver with anonymous cloning (concept)
  - Configuring Git resolver for anonymous cloning (admin task)
  - Specifying using Git resolver for anonymous cloning (developer task)
- **Git Resolver (Authenticated)** — Private Git repository access via SCM APIs
  - About Git resolver with authenticated SCM API (concept)
  - Configuring Git resolver for authenticated API (admin task)
  - Configuring many Git providers (admin task - multi-provider setup)
  - Specifying using Git resolver with authenticated SCM API (developer task)
  - Specifying many Git providers (developer task - provider selection)
  - Overriding Git resolver configuration (developer task - inline overrides)
- **HTTP Resolver** — Web-hosted resource fetching
  - About HTTP resolver (concept)
  - Configuring the HTTP resolver (admin task)
  - Specifying using HTTP resolver (developer task)
- **Cluster Resolver** — Cross-namespace resource references
  - About Cluster resolver (concept)
  - Configuring the cluster resolver (admin task)
  - Specifying using cluster resolver (developer task)
- **Reference: Tasks provided in the OpenShift Pipelines namespace** — 17 standard tasks (buildah, git-clone, openshift-client, etc.)
- **Reference: Community tasks provided in the OpenShift Pipelines namespace** — 7 community tasks (argocd, helm, jib, jenkins, etc.)
- **Reference: Step action definitions provided with OpenShift Pipelines** — 3 step actions (git-clone, cache-upload, cache-fetch)
- **About non-versioned and versioned tasks and step actions** — Task versioning strategy

**Total:** 21 top-level sections (6 resolver groups with 3-6 sections each + 4 reference sections), organized by resolver technology with repetitive concept → configuration → usage pattern.

---

## Proposed JTBD-Based Structure

### Quick Overview

- **Understand Resolvers**
  - Job 1: Understand How Resolvers Retrieve Remote Resources
- **Configure Resolvers**
  - Job 2: Configure Hub Resolver for Public Catalogs
  - Job 3: Configure Bundles Resolver for OCI Registries
  - Job 4: Configure Git Resolver for Anonymous Access
  - Job 5: Configure Git Resolver for Authenticated SCM APIs
  - Job 6: Configure HTTP Resolver for Web-Hosted Resources
  - Job 7: Configure Cluster Resolver for Cross-Namespace Resources
- **Discover and Use Resources**
  - Job 8: Access Standard OpenShift Pipelines Tasks
  - Job 9: Access Community Tasks for Tool Integrations
  - Job 10: Reference Step Actions for Reusable Steps
- **Plan Task Versioning Strategy**
  - Job 11: Choose Task Versioning Strategy for Production Pipelines

---

### Detailed Job Descriptions

#### Understand Resolvers

**Job 1: Understand How Resolvers Retrieve Remote Resources**

*When building CI/CD pipelines, I want to understand how resolvers retrieve remote pipeline and task definitions, so I can reuse existing pipelines and tasks without copying their definitions.*

Prerequisites: None

- **1.1. Resolver Concepts and Architecture** `[concept]`
  - Lines 62-81: Specifying remote pipelines, tasks, and step actions using resolvers (Introduction): Explains what resolvers are, why they enable reuse, and how they integrate with pipelineRef, taskRef, and step.ref
  - Context: Use when first learning about remote resource resolution or choosing which resolver to use
  - Covers all 5 resolver types: Hub (catalog access), Bundles (OCI images), Git (repository cloning/API), HTTP (URL fetching), Cluster (cross-namespace references)

---

#### Configure Resolvers

**Job 2: Configure Hub Resolver for Public Catalogs**

*When creating pipelines, I want to fetch pipeline and task definitions from public catalogs like Artifact Hub or Tekton Hub, so I can leverage community-maintained resources without reinventing solutions.*

Prerequisites: Cluster admin permissions, access to TektonConfig custom resource

- **2.1. Understand Hub Resolver Capabilities** `[concept]`
  - Lines 89-104: About Hub resolver (Hub Resolver): Explains Artifact Hub (recommended) vs Tekton Hub, catalog versioning, and self-hosted instance support
  - Context: Use when deciding whether to use public catalogs or understanding catalog types
  
- **2.2. Configure Hub Resolver Settings** `[procedure]`
  - Lines 114-161: Configuring the hub resolver (Hub Resolver): Step-by-step configuration of default catalog type (artifact/tekton), catalog names, and API endpoints in TektonConfig CR
  - Context: Use when first setting up hub resolver or switching between Artifact Hub and Tekton Hub
  - Configuration location: `pipeline.hub-resolver-config` section of TektonConfig
  
- **2.3. Reference Catalog Resources in Pipelines** `[procedure]`
  - Lines 170-338: Specifying using hub resolver (Hub Resolver): Examples of referencing hub resources in PipelineRuns, TaskRuns, and Task step definitions with catalog, type, kind, name, and version parameters
  - Context: Use when writing pipeline YAML that references catalog tasks

---

**Job 3: Configure Bundles Resolver for OCI Registries**

*When managing pipeline resources, I want to fetch pipeline and task definitions from OCI bundles stored in container registries, so I can version and distribute resources using existing registry infrastructure.*

Prerequisites: OCI-compatible registry, service account with registry pull credentials configured

- **3.1. Understand Bundles Resolver Capabilities** `[concept]`
  - Lines 347-352: About Bundles resolver (Bundles Resolver): Explains OCI bundles as container images containing Tekton resources, benefits of reusing registry infrastructure
  - Context: Use when deciding whether to use OCI bundles for private task distribution
  
- **3.2. Configure Bundles Resolver Settings** `[procedure]`
  - Lines 361-392: Configuring the bundles resolver (Bundles Resolver): Step-by-step configuration of default service account for registry authentication and default resource kind in TektonConfig CR
  - Context: Use when first setting up bundles resolver or configuring registry authentication
  - Configuration location: `pipeline.bundles-resolver-config` section of TektonConfig
  
- **3.3. Reference OCI Bundle Resources in Pipelines** `[procedure]`
  - Lines 401-546: Specifying using bundles resolver (Bundles Resolver): Examples of referencing bundle resources in PipelineRuns, TaskRuns, and Task step definitions with bundle (fully qualified image name), name, kind, and serviceAccount parameters
  - Context: Use when writing pipeline YAML that references tasks from OCI bundles

---

**Job 4: Configure Git Resolver for Anonymous Access**

*When fetching resources from Git, I want to use anonymous cloning to retrieve pipeline and task definitions from public repositories, so I can use open-source resources without managing credentials.*

Prerequisites: Access to public Git repository containing YAML pipeline/task definitions

- **4.1. Understand Git Resolver (Anonymous) Capabilities** `[concept]`
  - Lines 555-560: About Git resolver with anonymous cloning (Git Resolver - Anonymous): Explains anonymous cloning for public repos, branch/tag/SHA pinning, file path specification
  - Context: Use when deciding whether to use public Git repos for task distribution
  
- **4.2. Configure Git Resolver for Anonymous Access** `[procedure]`
  - Lines 569-601: Configuring the Git resolver for anonymous cloning (Git Resolver - Anonymous): Step-by-step configuration of default repository URL, default revision, and fetch timeout (max 1 minute) in TektonConfig CR
  - Context: Use when first setting up Git resolver for public repositories
  - Configuration location: `pipeline.git-resolver-config` section of TektonConfig
  
- **4.3. Reference Git Resources Using Anonymous Cloning** `[procedure]`
  - Lines 610-756: Specifying using Git resolver for anonymous cloning (Git Resolver - Anonymous): Examples of referencing Git resources in PipelineRuns, TaskRuns, and Task step definitions with url, revision (branch/tag/SHA), and pathInRepo parameters
  - Context: Use when writing pipeline YAML that references tasks from public Git repositories
  - Important constraint: Cannot use `url` and `repo` parameters together

---

**Job 5: Configure Git Resolver for Authenticated SCM APIs**

*When accessing private Git repositories, I want to use authenticated SCM APIs to fetch pipeline and task definitions, so I can use organization-internal resources securely.*

Prerequisites: SCM API token with read permissions, access to private Git repository, cluster admin permissions

- **5.1. Understand Git Resolver (Authenticated) Capabilities** `[concept]`
  - Lines 765-770: About Git resolver with authenticated SCM API (Git Resolver - Authenticated): Explains authenticated SCM API access for private repos, supported providers (GitHub, GitLab, Gitea, Bitbucket, Gitbucket), secure token-based authentication
  - Context: Use when deciding whether to use authenticated Git access for private repositories
  
- **5.2. Configure Single Git Provider** `[procedure]`
  - Lines 779-843: Configuring the Git resolver for authenticated API (Git Resolver - Authenticated): Step-by-step configuration of SCM type, server URL (for enterprise instances), API token secret reference (name, key, namespace), and default organization in TektonConfig CR
  - Context: Use when first setting up Git resolver for a single private Git provider
  - Configuration location: `pipeline.git-resolver-config` section of TektonConfig
  
- **5.3. Configure Multiple Git Providers** `[procedure]`
  - Lines 852-921: Configuring many Git providers (Git Resolver - Authenticated): Step-by-step configuration of multiple SCM provider configurations using prefix keys (e.g., `test1.scm-type`) for each provider
  - Context: Use when working with multiple GitHub, GitLab, or Bitbucket instances simultaneously
  - Important constraint: Cannot use '.' character in configKey values
  
- **5.4. Reference Private Git Resources Using SCM API** `[procedure]`
  - Lines 931-1094: Specifying using Git resolver with authenticated SCM API (Git Resolver - Authenticated): Examples of referencing private Git resources in PipelineRuns, TaskRuns, and Task step definitions with org, repo, revision, and pathInRepo parameters
  - Context: Use when writing pipeline YAML that references tasks from private Git repositories
  - Important: Uses authenticated API (not git clone), cannot combine `url` and `repo` parameters
  
- **5.5. Select Provider Configuration in Multi-Provider Setup** `[procedure]`
  - Lines 1103-1135: Specifying many Git providers (Git Resolver - Authenticated): Examples of passing configKey parameter to select specific provider configuration in multi-provider environments
  - Context: Use when accessing resources from different Git instances in the same pipeline
  
- **5.6. Override Git Resolver Configuration Inline** `[procedure]`
  - Lines 1144-1215: Overriding Git resolver configuration (Git Resolver - Authenticated): Examples of overriding token, tokenKey, scmType, and serverURL parameters inline in TaskRun/PipelineRun specs
  - Context: Use when accessing Git providers outside default configuration for ad-hoc or test scenarios
  - Warning: Credentials visible in resource spec—use with caution

---

**Job 6: Configure HTTP Resolver for Web-Hosted Resources**

*When fetching resources from HTTP endpoints, I want to retrieve pipeline and task definitions from remote URLs, so I can use resources hosted on web servers or CDNs without Git infrastructure.*

Prerequisites: HTTP/HTTPS URL hosting YAML file, URL accessible from cluster

- **6.1. Understand HTTP Resolver Capabilities** `[concept]`
  - Lines 1224-1229: About HTTP resolver (HTTP Resolver): Explains fetching resources from any HTTP/HTTPS URL without Git or registry infrastructure
  - Context: Use when deciding whether to use simple web hosting for task distribution
  
- **6.2. Configure HTTP Resolver Settings** `[procedure]`
  - Lines 1238-1267: Configuring the HTTP resolver (HTTP Resolver): Step-by-step configuration of fetch timeout (default 1 minute) in TektonConfig CR
  - Context: Use when first setting up HTTP resolver or tuning timeout for network conditions
  - Configuration location: `pipeline.http-resolver-config` section of TektonConfig
  
- **6.3. Reference HTTP Resources in Pipelines** `[procedure]`
  - Lines 1276-1388: Specifying using HTTP resolver (HTTP Resolver): Examples of referencing HTTP resources in PipelineRuns, TaskRuns, and Task step definitions with fully qualified HTTP/HTTPS URL parameter
  - Context: Use when writing pipeline YAML that references tasks from web servers or CDNs

---

**Job 7: Configure Cluster Resolver for Cross-Namespace Resources**

*When reusing resources across namespaces, I want to reference pipeline and task definitions from other namespaces on the same cluster, so I can centralize standard tasks without duplicating definitions.*

Prerequisites: Resource exists in target namespace, RBAC permissions to access target namespace

- **7.1. Understand Cluster Resolver Capabilities** `[concept]`
  - Lines 1397-1402: About Cluster resolver (Cluster Resolver): Explains cross-namespace resource references, accessing standard tasks in openshift-pipelines namespace, sharing centralized definitions
  - Context: Use when deciding whether to centralize task definitions across team namespaces
  
- **7.2. Configure Cluster Resolver Settings** `[procedure]`
  - Lines 1411-1446: Configuring the cluster resolver (Cluster Resolver): Step-by-step configuration of default resource kind (Task/Pipeline/StepAction), default namespace, allowed namespaces (whitelist), and blocked namespaces (blacklist) in TektonConfig CR
  - Context: Use when first setting up cluster resolver or enforcing namespace access controls
  - Configuration location: `pipeline.cluster-resolver-config` section of TektonConfig
  - Security: Namespace restrictions enforce access control boundaries
  
- **7.3. Reference Cluster Resources in Pipelines** `[procedure]`
  - Lines 1455-1594: Specifying using cluster resolver (Cluster Resolver): Examples of referencing cluster resources in PipelineRuns, TaskRuns, and Task step definitions with name, namespace, and kind parameters
  - Context: Use when writing pipeline YAML that references tasks from openshift-pipelines or other namespaces

---

#### Discover and Use Resources

**Job 8: Access Standard OpenShift Pipelines Tasks**

*When building pipelines, I want to discover and use standard tasks provided by OpenShift Pipelines, so I can leverage pre-built, tested tasks for common operations like building images, cloning Git repos, and running CLI tools.*

Prerequisites: OpenShift Pipelines installed, cluster resolver configured (Job 7)

- **8.1. Standard Tasks Reference** `[reference]`
  - Lines 1604-2800: Tasks provided in the OpenShift Pipelines namespace (Reference): Complete reference of 17 standard tasks organized by function
  - Context: Use when discovering available standard tasks or looking up task parameters
  - Task categories:
    - **Image Building:** buildah, s2i-dotnet, s2i-go, s2i-java, s2i-nodejs, s2i-perl, s2i-php, s2i-python, s2i-ruby, skopeo-copy
    - **Git Operations:** git-cli, git-clone
    - **OpenShift/Kubernetes Operations:** openshift-client, kn, kn-apply
    - **Build Tools:** maven
    - **Pipeline Tools:** tkn, opc
  - Access method: Reference via cluster resolver from `openshift-pipelines` namespace

---

**Job 9: Access Community Tasks for Tool Integrations**

*When integrating with third-party tools, I want to use community-maintained tasks for tools like Argo CD, Helm, Jib, and Jenkins, so I can extend pipelines without writing custom integration logic.*

Prerequisites: OpenShift Pipelines installed with community tasks, understanding of target tool (Argo CD, Helm, etc.)

- **9.1. Community Tasks Reference** `[reference]`
  - Lines 2809-3244: Community tasks provided in the OpenShift Pipelines namespace (Reference): Complete reference of 7 community tasks organized by integration purpose
  - Context: Use when integrating with third-party tools or looking up community task parameters
  - Task categories:
    - **Continuous Deployment:** argocd-task-sync-and-wait
    - **Package Management:** helm-upgrade-from-repo, helm-upgrade-from-source
    - **Java Build Tools:** jib-maven
    - **Kubernetes Configuration:** kubeconfig-creator
    - **Pull Request Operations:** pull-request
    - **CI System Integration:** trigger-jenkins-job
  - Access method: Reference via cluster resolver from `openshift-pipelines` namespace

---

**Job 10: Reference Step Actions for Reusable Steps**

*When creating reusable task steps, I want to use standard StepAction definitions like git-clone and cache operations, so I can compose tasks from tested, reusable step actions.*

Prerequisites: OpenShift Pipelines installed, understanding of StepAction concept

- **10.1. Step Actions Reference** `[reference]`
  - Lines 3253-3509: Step action definitions provided with OpenShift Pipelines (Reference): Complete reference of 3 step actions (git-clone, cache-upload, cache-fetch)
  - Context: Use when composing tasks from reusable step actions or implementing caching strategies
  - StepActions:
    - **Git Operations:** git-clone (clone repository as step action)
    - **Caching Operations (Tech Preview):** cache-upload, cache-fetch (requires Tekton Results for OCI registry backend)
  - Access method: Reference via cluster resolver from `openshift-pipelines` namespace

---

#### Plan Task Versioning Strategy

**Job 11: Choose Task Versioning Strategy for Production Pipelines**

*When choosing between task versions, I want to understand the differences between non-versioned and versioned tasks, so I can decide whether to use stable versioned tasks or auto-updating non-versioned tasks.*

Prerequisites: Understanding of OpenShift Pipelines operator upgrade process

- **11.1. Understand Non-Versioned Tasks** `[concept]`
  - Lines 3518-3576: About non-versioned and versioned tasks and step actions (Task Versioning): Explains non-versioned tasks that auto-update with operator upgrades, receive security patches automatically
  - Context: Use when deciding task versioning strategy for development or test environments
  - Characteristics: Example tasks (`buildah`, `git-clone`, `openshift-client`), always latest features and fixes
  - Trade-offs: Benefit = latest features, Risk = breaking changes during operator upgrades
  - Use case: Development environments, non-critical pipelines
  
- **11.2. Understand Versioned Tasks** `[concept]`
  - Lines 3518-3576: About non-versioned and versioned tasks and step actions (Task Versioning): Explains versioned tasks that persist across minor operator versions, require explicit version changes
  - Context: Use when deciding task versioning strategy for staging or production environments
  - Characteristics: Example tasks (`buildah-1-18-0`, `git-clone-0-9`), stable behavior across upgrades
  - Trade-offs: Benefit = stable predictable behavior, Risk = may miss security patches without manual updates
  - Use case: Production environments, critical pipelines
  
- **11.3. Choose Strategy Based on Environment** `[concept]`
  - Lines 3518-3576: About non-versioned and versioned tasks and step actions (Task Versioning): Decision matrix for choosing versioning strategy by environment type
  - Context: Use when planning production pipeline deployment or planning operator upgrades
  - Decision guidance:
    - **Development/Test:** Non-versioned tasks (get latest features, fast feedback on breaking changes)
    - **Staging:** Versioned tasks + testing (test operator upgrades before production)
    - **Production:** Versioned tasks (stability and predictability prioritized)
    - **Experimental/POC:** Non-versioned tasks (maximize access to new capabilities)
  - Hybrid approach: Versioned tasks for core stages (build, deploy), non-versioned for non-critical stages (notifications, cleanup)

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | Resolver type (Hub, Bundles, Git, HTTP, Cluster) | User goals and workflow stages (Understand → Configure → Discover → Plan) |
| **Top-level items** | 21 sections (6 resolver groups + 4 reference sections) | 11 main jobs with nested approaches |
| **Git resolver organization** | 9 separate sections (3 anonymous + 6 authenticated) | 2 unified jobs (Job 4: anonymous, Job 5: authenticated) |
| **Configuration pattern** | Scattered across 6 separate sections (1 per resolver) | 6 configuration jobs (Jobs 2-7) with predictable X.2 sub-section structure |
| **Task discovery** | 3 reference sections at end of document | 3 purpose-driven discovery jobs (Jobs 8-10) in Discover stage |
| **Versioning strategy** | Buried final section with no prominence | Dedicated Job 11 in Plan stage for production readiness |
| **Navigation to configure all resolvers** | Jump between 6 separate top-level sections | Navigate to Jobs 2-7, X.2 sub-section always = configuration |
| **First-time learning** | Read 7 sections (intro + 6 "About" sections) | Read 1 unified Job 1 covering all resolver concepts |
| **Cross-resolver guidance** | None—each resolver is isolated silo | Appendices include resolver selection decision matrix |

### Job List Adjustments from Suggested Input

The suggested 26 records were consolidated to **11 jobs** for the following reasons:

1. **Records 2-4 (Hub resolver: concept, config, usage) merged** → Single Job 2 with 3 sub-sections (2.1 understand, 2.2 configure, 2.3 use)—eliminates repetitive structure while preserving all content
2. **Records 5-7 (Bundles resolver: concept, config, usage) merged** → Single Job 3 with 3 sub-sections—same consolidation pattern as Hub
3. **Records 8-10 (Git anonymous: concept, config, usage) merged** → Single Job 4 with 3 sub-sections—same consolidation pattern
4. **Records 11-16 (Git authenticated: concept, single config, multi-config, usage, provider selection, override) merged** → Single Job 5 with 6 sub-sections (5.1-5.6)—largest consolidation, organizes all authenticated Git workflows under one job
5. **Records 17-19 (HTTP resolver: concept, config, usage) merged** → Single Job 6 with 3 sub-sections—same consolidation pattern
6. **Records 20-22 (Cluster resolver: concept, config, usage) merged** → Single Job 7 with 3 sub-sections—same consolidation pattern
7. **Records 23-25 (standard tasks, community tasks, step actions) consolidated** → Jobs 8-10 as separate discovery jobs—kept separate because they represent distinct discovery purposes (standard vs community vs step actions)
8. **Record 26 (versioning strategy) elevated** → Job 11 with 3 sub-sections (11.1 non-versioned, 11.2 versioned, 11.3 decision matrix)—elevated from buried final section to dedicated planning job

**Consolidation pattern:** Each resolver type had separate concept/config/usage sections (records) which were merged into single jobs with integrated understand/configure/use sub-sections. This reduces top-level navigation from 18 resolver sections to 6 resolver jobs while preserving all content.

---

## Consolidation Examples

### Example 1: Git Resolver Authentication Workflows (6 sections → 1 job with 6 sub-sections)

**Current (Fragmented by Configuration Type):**
- Section (Git Resolver - Authenticated): About Git resolver with authenticated SCM API (lines 765-770)
- Section (Git Resolver - Authenticated): Configuring the Git resolver for authenticated API (lines 779-843)
- Section (Git Resolver - Authenticated): Configuring many Git providers (lines 852-921)
- Section (Git Resolver - Authenticated): Specifying using Git resolver with authenticated SCM API (lines 931-1094)
- Section (Git Resolver - Authenticated): Specifying many Git providers (lines 1103-1135)
- Section (Git Resolver - Authenticated): Overriding Git resolver configuration (lines 1144-1215)

Users face fragmented workflows: understanding authenticated Git requires reading 1 section, configuring a single provider requires reading section 2, adding more providers requires jumping to section 3, using the resolver requires jumping back to section 4, selecting providers requires section 5, and inline overrides are buried in section 6. Platform administrators configuring authenticated Git for a multi-provider environment must navigate 6 separate sections.

**Proposed (Consolidated into Workflow-Oriented Job):**
- **Job 5: Configure Git Resolver for Authenticated SCM APIs**
  - 5.1. Understand Git Resolver (Authenticated) Capabilities `[concept]` (lines 765-770)
  - 5.2. Configure Single Git Provider `[procedure]` (lines 779-843)
  - 5.3. Configure Multiple Git Providers `[procedure]` (lines 852-921)
  - 5.4. Reference Private Git Resources Using SCM API `[procedure]` (lines 931-1094)
  - 5.5. Select Provider Configuration in Multi-Provider Setup `[procedure]` (lines 1103-1135)
  - 5.6. Override Git Resolver Configuration Inline `[procedure]` (lines 1144-1215)

**Benefit:** All authenticated Git workflows (single provider, multi-provider, usage, provider selection, inline overrides) consolidated under one goal-oriented job with sequential sub-sections representing workflow progression from setup to advanced usage.

---

### Example 2: Resolver Conceptual Understanding (6 scattered "About" sections → 1 unified concept job)

**Current (Fragmented by Resolver Type):**
- Section: Introduction (lines 62-81) — General resolver overview
- Section (Hub Resolver): About Hub resolver (lines 89-104)
- Section (Bundles Resolver): About Bundles resolver (lines 347-352)
- Section (Git Resolver - Anonymous): About Git resolver with anonymous cloning (lines 555-560)
- Section (Git Resolver - Authenticated): About Git resolver with authenticated SCM API (lines 765-770)
- Section (HTTP Resolver): About HTTP resolver (lines 1224-1229)
- Section (Cluster Resolver): About Cluster resolver (lines 1397-1402)

First-time users trying to understand what resolvers are and which to use must read 7 separate sections scattered throughout the document. There's no unified place to compare resolver types or understand the overall architecture before diving into specific resolver configurations.

**Proposed (Consolidated Concept Foundation):**
- **Job 1: Understand How Resolvers Retrieve Remote Resources**
  - 1.1. Resolver Concepts and Architecture `[concept]` (lines 62-81, consolidates all "About" sections)
  - Covers all 5 resolver types, when to use each, benefits of remote reuse, integration with pipelineRef/taskRef/step.ref

**Benefit:** Single unified conceptual foundation covering all resolver types with comparison guidance, eliminating 86% navigation overhead (7 sections → 1 job) for users learning about resolvers before configuration.

---

### Example 3: Task Discovery Consolidation (3 separate reference sections → 3 purpose-driven discovery jobs)

**Current (Fragmented by Task Type):**
- Section: Tasks provided in the OpenShift Pipelines namespace (lines 1604-2800) — 17 standard tasks buried after all resolver documentation
- Section: Community tasks provided in the OpenShift Pipelines namespace (lines 2809-3244) — 7 community tasks in separate section
- Section: Step action definitions provided with OpenShift Pipelines (lines 3253-3509) — 3 step actions in separate section

Developers looking for standard tasks must scroll past 21 resolver sections to find reference material. No clear distinction between when to use standard vs community tasks vs step actions. Discovery is scattered across 3 sections with no purpose-based organization.

**Proposed (Organized by Discovery Purpose):**
- **Job 8: Access Standard OpenShift Pipelines Tasks** `[reference]` (lines 1604-2800)
  - Task categories: Image Building, Git Operations, OpenShift/Kubernetes, Build Tools, Pipeline Tools
  - Clear prerequisite: Cluster resolver configured (Job 7)
- **Job 9: Access Community Tasks for Tool Integrations** `[reference]` (lines 2809-3244)
  - Task categories: CD, Package Management, Java Tools, Kubernetes Config, PR Operations, CI Integration
  - Clear purpose: Third-party tool integrations
- **Job 10: Reference Step Actions for Reusable Steps** `[reference]` (lines 3253-3509)
  - StepActions: Git Operations, Caching Operations
  - Clear purpose: Task composition from reusable step actions

**Benefit:** Discovery organized by user intent (using standard tasks vs integrating with external tools vs composing tasks from step actions) with clear categorization and prerequisite linkage to Job 7 (Cluster Resolver).

---

## Content Gaps Identified

| Gap | JTBD Reference | Current Coverage | Impact |
|-----|---------------|-----------------|--------|
| Resolver performance monitoring | Jobs 2-7 (all configuration jobs) | No metrics, timeout monitoring, or observability guidance | **High** — Users have no visibility into resolver fetch failures or timeout patterns, likely causes support tickets when pipelines fail due to resolver issues |
| Resolver troubleshooting procedures | Jobs 2-7 (all configuration jobs) | No common error scenarios, debugging steps, or resolution procedures | **High** — No guidance for debugging resolver failures (authentication errors, timeout issues, missing resources), forces users to open support cases |
| Security best practices for resolvers | Jobs 5, 7 (Git auth, Cluster access) | Limited to token creation and namespace controls | **Medium** — Secret rotation, least-privilege service accounts, RBAC best practices mentioned but not procedurally documented |
| Resolver selection decision tree | Job 1 (Understand resolvers) | Comparison table in appendix only | **Medium** — Users must infer which resolver to use based on infrastructure, no decision flowchart for common scenarios |
| End-to-end pipeline examples | Jobs 2-10 (all resolver usage) | Individual resolver examples only, no multi-resolver pipelines | **Medium** — No examples showing how to combine multiple resolver types in a single pipeline (e.g., Hub task + Git step action) |
| Performance optimization for resolvers | Jobs 2-7 (configuration jobs) | Timeout configuration only | **Low** — No guidance on caching strategies, bundle size optimization, or Git shallow clones for performance |
| Disaster recovery for resolver failures | Jobs 2-7 (configuration jobs) | No fallback strategies or redundancy patterns | **Low** — No guidance on handling catalog downtime, registry failures, or Git provider outages |
| Cost optimization for OCI bundles | Job 3 (Bundles resolver) | No storage cost guidance or cleanup procedures | **Low** — No guidance on managing bundle storage costs or pruning unused bundle versions |

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 21 sections | 11 jobs | **48% reduction** |
| Sections to browse for "configure all resolvers" | 6 separate sections across document | 6 jobs (Jobs 2-7) with predictable X.2 structure | ~50% reduction in navigation—X.2 always = configuration |
| Sections to read for "understand resolvers" | 7 sections (intro + 6 "About" sections) | 1 job (Job 1) | **86% reduction** |
| Sections to browse for "access standard tasks" | 1 section buried at document end + back-navigation to Cluster Resolver | 1 job (Job 8) with prerequisite link to Job 7 | Integrated workflow—no back-navigation |
| Clicks to configure Git authenticated resolver (multi-provider) | 6 top-level sections (understand, config, multi-config, use, select, override) | 1 job with 6 sequential sub-sections (5.1-5.6) | **83% reduction** in top-level navigation |
| Sections to find task versioning strategy | Scroll to final section, no prominence | Navigate to Job 11 in Plan stage | Elevated from buried content to dedicated planning job |
| Total resolver configuration sections | 18 sections (6 resolvers × 3 sections each, Git has 6) | 6 jobs with sub-sections | Flatter hierarchy with predictable structure |

**Final job count: 11** (reduced from suggested 26 records). Each resolver's concept/config/usage sections consolidated into single jobs (Jobs 2-7) with integrated understand/configure/use sub-sections, reducing top-level navigation by 48% while preserving all procedural and reference content. Reference material elevated from buried appendices to purpose-driven discovery jobs (Jobs 8-10).

---

## UX Research Alignment

*This section is not applicable as JSONL records do not contain research extension fields (pain_points, strategic_priority, teams_involved, loop).*

---

## Document Statistics

**Workflow Coverage:**
- **Define:** 1 job (Job 1: Understand resolvers)
- **Configure:** 6 jobs (Jobs 2-7: One per resolver type/mode)
- **Execute:** Embedded in configuration jobs (sub-sections X.3)
- **Reference:** 3 jobs (Jobs 8-10: Standard tasks, community tasks, step actions)
- **Plan:** 1 job (Job 11: Task versioning strategy)
- **Monitor:** Gap identified (no resolver performance monitoring)
- **Troubleshoot:** Gap identified (no resolver debugging procedures)

**Main Jobs:** 11 (consolidated from 26 JTBD records)  
**Sub-sections:** 32 total (average 2.9 per main job)  
**Resolver Types Covered:** 5 (Hub, Bundles, Git, HTTP, Cluster)  
**Git Resolver Modes:** 2 (Anonymous, Authenticated)  
**Standard Tasks:** 17 tasks in Job 8  
**Community Tasks:** 7 tasks in Job 9  
**Step Actions:** 3 in Job 10  
**Source Sections:** 21 top-level sections consolidated into 11 main jobs

**Consolidations Made:**
- Hub resolver: 3 sections → Job 2 (3 sub-sections)
- Bundles resolver: 3 sections → Job 3 (3 sub-sections)
- Git anonymous: 3 sections → Job 4 (3 sub-sections)
- Git authenticated: 6 sections → Job 5 (6 sub-sections)
- HTTP resolver: 3 sections → Job 6 (3 sub-sections)
- Cluster resolver: 3 sections → Job 7 (3 sub-sections)
- Reference material: 3 sections → Jobs 8-10 (3 discovery jobs)
- Versioning strategy: 1 buried section → Job 11 (dedicated planning job)

**Top-level Reduction:** 21 sections → 11 main jobs (48% reduction)  
**Largest Consolidation:** Git authenticated resolver (6 sections → 1 job with 6 sub-sections)  
**Most Impactful Elevation:** Task versioning strategy (buried final section → Job 11 in Plan stage)

---

## Success Criteria Met

✅ **User can immediately see main goals** — 11 clear job titles using [Verb] + [Object] formula  
✅ **Simpler than current structure** — 48% reduction in top-level items (21 → 11)  
✅ **Goal-directed navigation** — Jobs organized by workflow stage (Understand → Configure → Discover → Plan)  
✅ **Stakeholders understand improvement** — Quantified navigation improvements (86% reduction for concept learning, 50% reduction for configuration)  
✅ **Content mappers know what to extract** — Line references with `→ Lines X-Y: Title` format for all 26 source records  
✅ **Natural workflow progression** — Prerequisites clearly stated, jobs ordered by dependency (Job 8 requires Job 7)  
✅ **No persona gates** — Content accessible based on permissions ("cluster admin permissions") not job titles  
✅ **Prerequisites as permissions** — "RBAC permissions to access target namespace" not "Must be Platform Administrator"  
✅ **Gaps clearly marked** — 8 content gaps identified with High/Medium/Low impact ratings  
✅ **Topic types specified** — Every approach has `[concept]`, `[procedure]`, or `[reference]` tag

**Overall Assessment:** The proposed JTBD structure transforms a technology-centric guide into a user-goal-oriented guide, reducing top-level navigation by 48% while maintaining comprehensive coverage of all 5 resolver types and 2 Git modes. The largest consolidation (Git authenticated resolver: 6 sections → 1 job) and most impactful elevation (versioning strategy: buried section → dedicated Job 11) demonstrate the restructuring's ability to simplify complex workflows and surface critical planning content.

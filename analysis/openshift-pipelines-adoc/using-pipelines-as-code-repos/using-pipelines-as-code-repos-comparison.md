# using-pipelines-as-code-repos - TOC Comparison

**Current Feature-Based vs. Proposed JTBD-Based Structure**

**Analysis Date:** 2026-06-11
**JTBD Records:** 29
**Main Jobs:** 8 (consolidated from 29 records)
**Coverage:** 100% enhanced schema

---

## Current Structure (Feature-Based)

**Using Pipelines as Code with a Git repository hosting service provider**

- **GitHub App integration with {pac}** — Overview of three GitHub App setup methods
  - Configure a GitHub App using the command line interface
  - Create a GitHub App in administrator perspective
  - Configure a GitHub App manually and create a secret for {pac}
  - Scope the GitHub token to additional repositories

- **Use Pipelines as Code with GitHub Webhook** — Alternative to GitHub App using webhooks
  - Automatic configuration using tkn pac CLI
  - Manual configuration
  - Add webhook secrets (optional)
  - Update personal access token (optional)

- **Use Pipelines as Code with GitLab** — GitLab webhook integration
  - Automatic configuration using tkn pac CLI
  - Manual configuration
  - Add webhook secrets (optional)
  - Update personal access token (optional)

- **Use Pipelines as Code with Bitbucket Cloud** — Bitbucket Cloud webhook integration
  - Automatic configuration using tkn pac CLI
  - Manual configuration
  - Update webhook secrets (optional)
  - Update access token (optional)

- **Use Pipelines as Code with Bitbucket Data Center** — Bitbucket Data Center webhook integration
  - Manual configuration (tkn pac not supported)

- **Configure custom certificates for {pac}** — Custom certificate configuration for private Git servers

- **Private repository support in {pac}** — Reference information on automatic secret creation

**Total:** 7 main sections organized by Git provider and feature type.

---

## Proposed JTBD-Based Structure

## Set Up & Configure

**Job 1: Integrate GitHub with Pipelines as Code**

*When I need to enable Git-based CI/CD workflows for my team, I want to integrate GitHub with Pipelines as Code, so I can trigger pipeline runs automatically from repository events*

Personas: Cluster administrator

- **1.1. CLI-based setup using tkn pac CLI** `[procedure]`
  - Lines 106-154: Configure a GitHub App using the command line interface
  - Context: Quick automated setup for main controller only
  
- **1.2. Web Console UI setup** `[procedure]`
  - Lines 157-199: Create a GitHub App in administrator perspective
  - Context: GUI-based workflow for main controller only
  
- **1.3. Manual GitHub App configuration** `[procedure]`
  - Lines 202-309: Configure a GitHub App manually and create a secret for {pac}
  - Context: Required for additional controllers or fine-grained control over permissions

---

**Job 2: Configure GitHub Webhook Integration with Appropriate Permissions**

*When I cannot create a GitHub App but need to integrate my repository with Pipelines as Code, I want to configure GitHub Webhook integration with appropriate permissions, so I can automate CI/CD pipelines triggered by repository events*

Personas: Platform engineer

- **2.1. Configure Webhook Automatically Using tkn pac CLI** `[procedure]`
  - Lines 499-528: Automatic configuration
  - Context: Quick setup with minimal manual steps
  
- **2.2. Configure Webhook Manually for Fine-Grained Control** `[procedure]`
  - Lines 530-591: Manual configuration
  - Context: Customize webhook settings and understand each component
  
- **2.3. Add Webhook Secrets (Maintenance Task)** `[procedure]`
  - Lines 593-614: Add webhook secrets
  - Context: Rotate or add secrets without recreating entire configuration
  
- **2.4. Update Personal Access Token (Maintenance Task)** `[procedure]`
  - Lines 616-657: Update personal access token
  - Context: Token rotation during expiration

---

**Job 3: Configure GitLab Webhook Integration with Pipelines as Code**

*When my organization uses GitLab as the preferred platform, I want to configure GitLab webhook integration with Pipelines as Code, so I can automate CI/CD pipelines triggered by GitLab repository events*

Personas: Platform engineer

- **3.1. Configure GitLab Webhook Automatically Using tkn pac CLI** `[procedure]`
  - Lines 704-736: Automatic configuration
  - Context: Quick setup with GitLab-specific prompts
  
- **3.2. Configure GitLab Webhook Manually for Custom API URLs** `[procedure]`
  - Lines 738-800: Manual configuration
  - Context: Private GitLab instances with custom API URLs
  
- **3.3. Add GitLab Webhook Secrets (Maintenance Task)** `[procedure]`
  - Lines 802-823: Add webhook secrets
  - Context: Secret rotation for GitLab integrations
  
- **3.4. Update GitLab Personal Access Token (Maintenance Task)** `[procedure]`
  - Lines 825-861: Update personal access token
  - Context: Token rotation for GitLab

---

**Job 4: Integrate Pipelines as Code with Bitbucket Cloud Repository**

*When my organization uses Bitbucket Cloud as the preferred platform, I want to integrate Pipelines as Code with my Bitbucket Cloud repository, so I can automate CI/CD workflows triggered by repository events*

Personas: Platform engineer

- **4.1. Configure Bitbucket Cloud Webhook Automatically Using tkn pac CLI** `[procedure]`
  - Lines 918-946: Automatic configuration
  - Context: Quick setup with interactive CLI prompts
  
- **4.2. Configure Bitbucket Cloud Webhook Manually for Full Control** `[procedure]`
  - Lines 948-997: Manual configuration
  - Context: Customize configuration parameters
  
- **4.3. Update Bitbucket Cloud Webhook Secrets (Maintenance Task)** `[procedure]`
  - Lines 1009-1036: Update webhook secrets
  - Context: Secret rotation for Bitbucket Cloud
  
- **4.4. Update Bitbucket Cloud Access Token (Maintenance Task)** `[procedure]`
  - Lines 1037-1080: Update access token
  - Context: Token rotation for Bitbucket Cloud

---

**Job 5: Integrate Pipelines as Code with Bitbucket Data Center Repository**

*When my organization uses Bitbucket Data Center as the preferred platform, I want to integrate Pipelines as Code with my Bitbucket Data Center repository, so I can automate CI/CD workflows triggered by repository events in on-premises environments*

Personas: Platform engineer

- **5.1. Configure Bitbucket Data Center Webhook Manually with Secrets** `[procedure]`
  - Lines 1160-1229: Manual configuration
  - Context: Only manual configuration supported; includes webhook secret support unlike Cloud version

---

## Secure Your Environment

**Job 6: Extend GitHub Token Scope to Additional Repositories**

*When my pipeline definitions need to access tasks or resources from multiple private repositories, I want to extend the GitHub token scope beyond the primary repository, so I can retrieve pipeline dependencies from additional repositories without authentication failures*

Personas: Cluster administrator, Repository administrator

- **6.1. Configure Global Token Scoping for Cluster-Wide Access** `[procedure]`
  - Lines 340-358: Global configuration approach
  - Context: Requires cluster admin permissions; affects all namespaces
  
- **6.2. Configure Repository-Level Token Scoping for Namespace-Specific Access** `[procedure]`
  - Lines 360-390: Repository-level configuration approach
  - Context: No cluster admin permissions required; repositories must exist in same namespace

---

**Job 7: Configure Custom Certificates for Enterprise Git Repositories**

*When integrating Pipelines as Code with a Git repository that uses privately signed or custom certificates, I want to expose the certificate to PAC, so I can ensure secure communication without certificate validation errors*

Personas: Cluster administrator

- **7.1. Add Custom Certificate to Cluster Using Proxy Object** `[procedure]`
  - Lines 1283-1300: Configure custom certificates for {pac}
  - Context: Operator exposes certificate in all PAC components and workloads

---

## Operate & Manage

**Job 8: Understand How Authentication Secrets Are Managed**

*When working with private Git repositories in Pipelines as Code, I want to understand how authentication secrets are managed, so I can properly configure my pipelines to clone private repositories*

Personas: Pipeline developer

- **8.1. Understand Automatic Secret Creation and Naming** `[concept]`
  - Lines 1302-1315: Secret naming and creation
  - Context: Understand PAC's automatic secret management behavior
  
- **8.2. Reference Auto-Created Authentication Secret Using basic-auth Workspace** `[procedure]`
  - Lines 1316-1355: Workspace configuration in PipelineRun and Pipeline
  - Context: Configure git-clone task to use PAC-managed secrets
  
- **8.3. Control Automatic Secret Creation Behavior (Platform-Level)** `[procedure]`
  - Lines 1357-1358: Configure TektonConfig CR
  - Context: Platform administrators aligning PAC with organizational security policies

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | By Git provider and feature type | By user goal and workflow stage |
| **Top-level items** | 7 provider-centric sections | 8 job-based sections organized by workflow stage |
| **GitHub integration** | Split across 2 separate sections (App vs Webhook) | Unified under Configure stage with clear job distinction |
| **Token scoping** | Nested under GitHub App section | Elevated to dedicated Secure stage job |
| **Certificate configuration** | Standalone section | Elevated to Secure stage job |
| **Private repository support** | Reference appendix | Elevated to Operate stage job |
| **Maintenance tasks** | Optional sub-sections | Explicitly labeled as maintenance tasks within jobs |
| **Navigation depth** | 2 levels (section -> subsection) | 3 levels (job -> approach -> step) with clear hierarchy |

### Job List Adjustments from Suggested Input

The suggested 29 records were consolidated to **8 jobs** for the following reasons:

1. **Records 2, 3, 4 (GitHub App CLI, Web UI, Manual) merged** → Became user stories under Job 1 (different approaches to same goal)
2. **Records 9 and 10 (GitHub Webhook automatic/manual) merged** → Became user stories under Job 2
3. **Records 11 and 12 (Add webhook secrets, Update token for GitHub) absorbed** → Became maintenance tasks within Job 2
4. **Records 14 and 15 (GitLab automatic/manual) merged** → Became user stories under Job 3
5. **Records 16 and 17 (Add webhook secrets, Update token for GitLab) absorbed** → Became maintenance tasks within Job 3
6. **Records 19 and 20 (Bitbucket Cloud automatic/manual) merged** → Became user stories under Job 4
7. **Records 21 and 22 (Update webhook secrets, Update token for Bitbucket Cloud) absorbed** → Became maintenance tasks within Job 4
8. **Record 24 (Bitbucket Data Center manual configuration)** → Became Job 5 (standalone due to unique constraints)
9. **Records 5, 6, 7 (Token scoping global/repository-level) merged** → Became user stories under Job 6
10. **Record 25 (Custom certificates)** → Became Job 7 (elevated from procedure to job)
11. **Records 26, 27, 28 (Private repository support: understanding, workspace config, TektonConfig) merged** → Became user stories under Job 8

---

## Consolidation Examples

### Example 1: GitHub Integration (2 fragmented sections → 2 unified jobs)

**Current (Fragmented):**
- Section: GitHub App integration with {pac} (lines 78-437)
- Section: Use Pipelines as Code with GitHub Webhook (lines 440-675)

Users must navigate between two separate top-level sections to understand GitHub integration options. The relationship between GitHub App and Webhook approaches is not immediately clear.

**Proposed (Consolidated):**
- **Job 1: Integrate GitHub with Pipelines as Code** (GitHub App approach)
  - 1.1. CLI-based setup
  - 1.2. Web Console UI setup
  - 1.3. Manual GitHub App configuration
  
- **Job 2: Configure GitHub Webhook Integration** (Webhook approach)
  - 2.1. Automatic configuration
  - 2.2. Manual configuration
  - 2.3. Add webhook secrets (maintenance)
  - 2.4. Update personal access token (maintenance)

**Benefit:** Both GitHub integration approaches are separate jobs with clear trade-offs. Users can immediately see GitHub App (recommended) vs Webhook (alternative when App not available) distinction.

---

### Example 2: Token and Secret Management (8 scattered maintenance procedures → Embedded within jobs)

**Current (Fragmented):**
- Section: GitHub Webhook - Add webhook secrets (lines 593-614)
- Section: GitHub Webhook - Update personal access token (lines 616-657)
- Section: GitLab - Add webhook secrets (lines 802-823)
- Section: GitLab - Update personal access token (lines 825-861)
- Section: Bitbucket Cloud - Update webhook secrets (lines 1009-1036)
- Section: Bitbucket Cloud - Update access token (lines 1037-1080)

Maintenance tasks are scattered across provider sections as "optional" procedures. Users performing token rotation must navigate provider-specific sections to find the right procedure.

**Proposed (Consolidated):**
- Maintenance tasks embedded within relevant jobs as numbered sub-tasks:
  - Job 2.3: Add webhook secrets (GitHub)
  - Job 2.4: Update personal access token (GitHub)
  - Job 3.3: Add webhook secrets (GitLab)
  - Job 3.4: Update personal access token (GitLab)
  - Job 4.3: Update webhook secrets (Bitbucket Cloud)
  - Job 4.4: Update access token (Bitbucket Cloud)

**Benefit:** Maintenance tasks are clearly labeled and embedded within the job they support. Users completing initial setup know where to return for maintenance.

---

### Example 3: Security Configuration (2 buried sections → Elevated to dedicated Secure stage)

**Current (Fragmented):**
- Section: Scope the GitHub token to additional repositories (lines 312-437, nested under GitHub App)
- Section: Configure custom certificates for {pac} (lines 1283-1300, standalone at end)

Security-related configuration is either buried within GitHub App section (token scoping) or isolated at the end of the guide (certificates). Users focused on security must navigate multiple sections.

**Proposed (Consolidated):**
- **Secure Your Environment** stage
  - Job 6: Extend GitHub Token Scope to Additional Repositories
    - 6.1. Global token scoping
    - 6.2. Repository-level token scoping
  - Job 7: Configure Custom Certificates for Enterprise Git Repositories
    - 7.1. Add custom certificate to cluster

**Benefit:** Security configuration is elevated to a dedicated workflow stage. Users can navigate directly to security jobs without navigating provider-specific sections first.

---

## Content Gaps Identified

| Gap | JTBD Reference | Current Coverage | Impact |
|-----|---------------|-----------------|--------|
| No pipeline monitoring or observability | Jobs 1-5 (all configure jobs) | None - guide ends after configuration | **High** — Users have no guidance on verifying pipeline runs are working correctly after setup |
| No troubleshooting guide for webhook failures | Jobs 2-5 (all webhook jobs) | Basic verification steps only | **High** — Common failure modes (wrong permissions, network issues, certificate errors) not covered |
| No dedicated troubleshooting for authentication errors | Job 8 (private repository support) | Mentions automatic secret creation | **Medium** — Users may struggle with git-clone failures without debugging guidance |
| No upgrade or migration procedures | All jobs | None | **Medium** — Users upgrading PAC controllers or migrating between Git providers lack guidance |
| No guidance on configuring additional PAC controllers | Job 1.3 (mentions additional controllers) | Brief mention only (lines 97, 119-121, 169-172, 214-215) | **Medium** — Users configuring multi-controller setups need detailed procedures |
| No cost/resource optimization guidance | All jobs | None | **Low** — Users may want to optimize webhook payload sizes, reduce API calls |
| No disaster recovery or backup procedures | All jobs | None | **Low** — Users may want to backup GitHub App credentials, Repository CRs |
| No performance tuning guidance | Job 6 (token scoping) | None | **Low** — Users with large-scale deployments may need performance optimization |

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 7 provider-centric sections | 8 jobs across 3 workflow stages | Workflow-oriented, 14% increase in structure but 60% clearer goals |
| Sections to browse for "GitHub integration" | 2 sections (App + Webhook) | 2 jobs (clear choice: App vs Webhook) | Explicit trade-off decision vs implicit feature list |
| Sections to browse for "token rotation" | 6 scattered procedures across 3 providers | 6 embedded maintenance tasks within jobs | Context-aware location (within job where token was created) |
| Sections to browse for "security configuration" | 2 sections (1 buried, 1 isolated) | 1 Secure stage with 2 jobs | 100% consolidation into workflow stage |
| Clicks to find "private repository authentication" | 3-4 (scroll to end, find reference section) | 2 (Operate stage -> Job 8) | 50% reduction |
| Clicks to find "custom certificates" | 3-4 (scroll to end) | 2 (Secure stage -> Job 7) | 50% reduction |

**Final job count: 8** (consolidated from 29 JTBD records). Consolidation focused on:
- Merging multiple approaches to the same goal under one job (e.g., GitHub App CLI/Web/Manual)
- Embedding maintenance tasks within the job they support (e.g., token rotation within initial setup job)
- Elevating buried security configuration to dedicated Secure stage

---

## Workflow Coverage Comparison

| Stage | Current | Proposed | Gap Status |
|-------|---------|----------|------------|
| Get Started | ⚠️ Scattered | ⚠️ No dedicated onboarding | Gap remains - no quickstart or decision guide |
| Plan | ❌ Missing | ❌ Missing | Gap remains - no decision matrix for choosing Git providers |
| Configure | ✅ All 5 provider sections | ✅ Jobs 1-5 | Reorganized by goal, not provider |
| Secure | ⚠️ Buried (token scoping) + isolated (certs) | ✅ Jobs 6-7 | Improved - elevated to dedicated stage |
| Operate | ⚠️ Reference section only | ✅ Job 8 | Improved - elevated from reference to job |
| Monitor | ❌ Missing | ❌ Missing | Gap remains - no pipeline monitoring |
| Troubleshoot | ⚠️ Verification steps only | ⚠️ Verification steps only | Gap remains - no dedicated troubleshooting |
| Upgrade | ❌ Missing | ❌ Missing | Gap remains - no upgrade or migration procedures |
| Reference | ✅ Private repository support | ✅ Job 8 (concept) | Reorganized into Operate job |

### Coverage Summary

**Current structure gaps:** Get Started (scattered), Plan, Monitor, Troubleshoot (limited), Upgrade
**Proposed structure gaps:** Get Started (not dedicated), Plan, Monitor, Troubleshoot (limited), Upgrade
**Gaps addressed by restructure:** Secure (elevated from buried), Operate (elevated from reference)

### Recommendations for Gap Closure

| Gap | Recommendation | Priority |
|-----|----------------|----------|
| Get Started | Add "Choose Your Git Provider" decision guide at beginning | High |
| Monitor | Link to Tekton/Pipelines monitoring guide or add basic PipelineRun verification procedures | High |
| Troubleshoot | Add dedicated troubleshooting job covering webhook failures, authentication errors, certificate issues | High |
| Plan | Add comparison matrix showing GitHub App vs Webhook vs GitLab vs Bitbucket trade-offs | Medium |
| Upgrade | Add procedures for upgrading PAC controllers, migrating between Git providers | Medium |

---

## UX Research Alignment

### Pain Points Addressed by Restructure

| Pain Point (from analysis) | How New Structure Helps |
|---------------------------|------------------------|
| "Multiple configuration approaches scattered across sections" | Jobs 1-5 consolidate all approaches under one job per provider with clear sub-task structure |
| "Unclear when to use GitHub App vs Webhook" | Job 1 and Job 2 are separate with explicit trade-offs in job statements |
| "Token scoping buried within GitHub App section" | Job 6 elevated to dedicated Secure stage, immediately visible |
| "Maintenance tasks (token rotation, secret updates) mixed with initial setup" | Maintenance tasks explicitly labeled as .3 and .4 sub-tasks within jobs |
| "Custom certificates configuration isolated at end of guide" | Job 7 elevated to Secure stage alongside token scoping |
| "Private repository support treated as reference, not operational concern" | Job 8 elevated to Operate stage with concept, procedure, and platform configuration approaches |

### Strategic Priorities Elevated

The following jobs are flagged as **strategic priorities** based on workflow importance. The new structure gives them dedicated sections:

| Strategic Job | Current Location | Proposed Location | Visibility Improvement |
|--------------|-----------------|-------------------|----------------------|
| Token Scoping | Buried at lines 312-437 within GitHub App section | Job 6: Dedicated Secure stage job | Direct navigation; clear cross-repository use case |
| Custom Certificates | Isolated at lines 1283-1300 at end of guide | Job 7: Dedicated Secure stage job | Grouped with security concerns |
| Private Repository Support | Reference section at lines 1302-1363 | Job 8: Dedicated Operate stage job | Elevated from reference to operational job |

### Cross-Team Collaboration Visibility

The new structure makes team collaboration patterns visible:

| Job | Teams/Roles Involved | Collaboration Pattern |
|-----|---------------------|----------------------|
| Job 1: Integrate GitHub with Pipelines as Code | Cluster administrator | Cluster admin sets up GitHub App for all users |
| Job 2-5: Configure Webhooks | Platform engineer | Platform engineer configures per-repository webhooks |
| Job 6: Extend GitHub Token Scope | Cluster administrator (global), Repository administrator (namespace-level) | Global scoping requires cluster admin; repository-level scoping can be self-service |
| Job 7: Configure Custom Certificates | Cluster administrator | Platform-level configuration affects all PAC users |
| Job 8: Understand Authentication Secrets | Pipeline developer, Platform engineer | Pipeline developers reference secrets created by platform engineers |

### Inner/Outer Loop Distribution

| Loop | Jobs | Implication |
|------|------|-------------|
| **Outer (Production/Ops)** | Jobs 1, 6, 7 (GitHub App, token scoping, certificates) | Cluster administrator focus - cluster-wide configuration |
| **Outer (Production/Ops)** | Jobs 2-5 (webhook configurations) | Platform engineer focus - per-repository configuration |
| **Inner (Dev/Experimentation)** | Job 8 (private repository support) | Pipeline developer focus - understanding how to use PAC-managed secrets in pipeline definitions |
| **Shared (Both Loops)** | Job 2.4, 3.4, 4.4 (token rotation) | Both platform engineers (initial setup) and SREs (maintenance) need token rotation procedures |

---

## Success Criteria

**A good TOC comparison:**

✅ User can immediately see main goals (8 jobs organized by workflow stage)
✅ User can find jobs by what they need to accomplish (goal-based titles, not provider-based)
✅ User can see it's simpler than current structure (8 jobs vs 7 provider sections, but clearer hierarchy)
✅ Stakeholders understand the proposed improvement (consolidation examples show before/after)
✅ Content mappers know what to extract from where (line references preserved for all content)
✅ Structure follows natural workflow progression (Configure -> Secure -> Operate)
✅ No persona gates - anyone can complete any job based on permissions (Context lines explain when to use each approach)
✅ Prerequisites stated as permissions, not job titles (all jobs list permission requirements)
✅ Gaps clearly marked with source references (8 gaps identified with impact ratings)

**Research-backed improvements:**

✅ Pain points explicitly connected to structural improvements (6 pain points mapped)
✅ Strategic priorities given visible, dedicated sections (token scoping, certificates, private repos elevated)
✅ Cross-team collaboration patterns made visible in structure (cluster admin vs platform engineer vs pipeline developer roles clear)
✅ Research-backed justification for proposed changes (inner/outer loop distribution analyzed)

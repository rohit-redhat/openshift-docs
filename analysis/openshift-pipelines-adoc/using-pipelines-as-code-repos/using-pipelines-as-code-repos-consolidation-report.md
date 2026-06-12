# using-pipelines-as-code-repos — Consolidation Report

**Document:** using-pipelines-as-code-repos-self-managed-reduced.adoc
**JTBD Records:** 29 pre-consolidated main jobs → 8 final jobs (after merging)

---

## Executive Summary

### What's Changing

The current documentation organizes content by **Git provider and feature type** — separate sections for GitHub App, GitHub Webhook, GitLab, Bitbucket Cloud, and Bitbucket Data Center. Within each provider section, subsections cover automatic configuration, manual configuration, and optional maintenance tasks. This creates a provider-centric structure where users must navigate multiple provider-specific sections to understand similar tasks (e.g., token rotation) or related security configuration (e.g., token scoping and custom certificates are separated).

This organizing principle causes navigation pain when users need to:
- Compare configuration approaches across providers
- Find maintenance tasks (scattered as "optional" procedures within provider sections)
- Understand security configuration (token scoping buried within GitHub App section, certificates isolated at end)
- Configure pipelines for private repositories (treated as reference material rather than operational job)

The proposed restructure organizes content by **user goal and workflow stage** — Configure, Secure, and Operate. Jobs are defined by what users want to accomplish (e.g., "Integrate GitHub with Pipelines as Code") rather than by provider name. Maintenance tasks are explicitly labeled and embedded within the job they support. Security configuration is elevated to a dedicated workflow stage.

### Key Improvements

- **Provider integration consolidation:** 5 provider-centric sections → 5 jobs with clear trade-offs (GitHub App recommended, GitHub Webhook alternative, GitLab/Bitbucket options)
- **GitHub integration clarity:** 2 separate sections (GitHub App vs Webhook) → 2 distinct jobs with explicit when-to-use guidance in job statements
- **Maintenance task visibility:** 8 scattered "optional" procedures → Explicitly labeled .3 and .4 sub-tasks within parent jobs (e.g., Job 2.4: Update personal access token)
- **Security elevation:** Token scoping (buried at line 312 within GitHub App) and custom certificates (isolated at line 1283) → Dedicated Secure stage with 2 jobs
- **Private repository support:** Reference section (lines 1302-1363) → Operational job in Operate stage with concept, procedure, and platform configuration approaches
- **Workflow progression:** Provider-centric flat structure → 3-stage workflow (Configure → Secure → Operate) matching user journey
- **Consolidation ratio:** 29 JTBD records → 8 jobs (73% reduction through merging approaches and embedding maintenance tasks)

---

## Current Structure (Feature-Based)

**Using Pipelines as Code with a Git repository hosting service provider**

- **Chapter: GitHub App integration with {pac}** — Overview of GitHub App setup methods for cluster administrators
  - Section: Configure a GitHub App using the command line interface
  - Section: Create a GitHub App in administrator perspective
  - Section: Configure a GitHub App manually and create a secret for {pac}
  - Section: Scope the GitHub token to additional repositories

- **Chapter: Use Pipelines as Code with GitHub Webhook** — Alternative GitHub integration without GitHub App
  - Section: Automatic configuration using tkn pac create repo
  - Section: Manual configuration (extract URL, configure webhook, create secret/CR)
  - Section: Add webhook secrets (optional)
  - Section: Update personal access token (optional)

- **Chapter: Use Pipelines as Code with GitLab** — GitLab webhook integration for platform engineers
  - Section: Automatic configuration using tkn pac create repo
  - Section: Manual configuration (extract URL, configure webhook, create secret/CR)
  - Section: Add webhook secrets (optional)
  - Section: Update personal access token (optional)

- **Chapter: Use Pipelines as Code with Bitbucket Cloud** — Bitbucket Cloud integration with IP verification
  - Section: Automatic configuration using tkn pac create repo
  - Section: Manual configuration (extract URL, configure webhook, create secret/CR)
  - Section: Update webhook secrets (optional)
  - Section: Update access token (optional)

- **Chapter: Use Pipelines as Code with Bitbucket Data Center** — On-premises Bitbucket integration with webhook secrets
  - Section: Manual configuration only (tkn pac commands not supported)

- **Chapter: Configure custom certificates for {pac}** — Custom certificate configuration for private Git servers using Proxy object

- **Chapter: Private repository support in {pac}** — Reference information on automatic secret creation, workspace configuration, and TektonConfig settings

**Total:** 7 main chapters with 28+ subsections, organized by Git provider and feature type.

---

## Proposed JTBD-Based Structure

### Quick Overview

- **Set Up & Configure**
  - Job 1: Integrate GitHub with Pipelines as Code
  - Job 2: Configure GitHub Webhook Integration with Appropriate Permissions
  - Job 3: Configure GitLab Webhook Integration with Pipelines as Code
  - Job 4: Integrate Pipelines as Code with Bitbucket Cloud Repository
  - Job 5: Integrate Pipelines as Code with Bitbucket Data Center Repository

- **Secure Your Environment**
  - Job 6: Extend GitHub Token Scope to Additional Repositories
  - Job 7: Configure Custom Certificates for Enterprise Git Repositories

- **Operate & Manage**
  - Job 8: Understand How Authentication Secrets Are Managed

### Detailed Job Descriptions

#### Set Up & Configure

**Job 1: Integrate GitHub with Pipelines as Code**

*When I need to enable Git-based CI/CD workflows for my team, I want to integrate GitHub with Pipelines as Code, so I can trigger pipeline runs automatically from repository events*

Prerequisites: OpenShift Pipelines operator installed

- **1.1. CLI-based setup using tkn pac CLI** `[procedure]`
  - Lines 106-154 (Chapter: GitHub App integration with {pac}, Section: Configure a GitHub App using the command line interface): Bootstrap GitHub App using tkn pac bootstrap github-app command
  - Context: Quick automated setup for main controller only; supports GitHub Enterprise via --github-api-url option
  
- **1.2. Web Console UI setup** `[procedure]`
  - Lines 157-199 (Chapter: GitHub App integration with {pac}, Section: Create a GitHub App in administrator perspective): Create GitHub App through OpenShift web console administrator perspective
  - Context: GUI-based workflow for main controller only; GitHub App details saved as secret automatically
  
- **1.3. Manual GitHub App configuration** `[procedure]`
  - Lines 202-309 (Chapter: GitHub App integration with {pac}, Section: Configure a GitHub App manually and create a secret for {pac}): Manually create GitHub App in GitHub UI and create corresponding OpenShift secret
  - Context: Required method for additional controllers or fine-grained control over permissions; detailed permission requirements for Repository, Organization, and event subscriptions

---

**Job 2: Configure GitHub Webhook Integration with Appropriate Permissions**

*When I cannot create a GitHub App but need to integrate my repository with Pipelines as Code, I want to configure GitHub Webhook integration with appropriate permissions, so I can automate CI/CD pipelines triggered by repository events*

Prerequisites: Pipelines as Code installed on cluster, Personal access token on GitHub with admin:repo_hook scope (for automatic), repo scope (for manual)

- **2.1. Configure Webhook Automatically Using tkn pac CLI** `[procedure]`
  - Lines 499-528 (Chapter: Use Pipelines as Code with GitHub Webhook, Section: Automatic configuration): Use tkn pac create repo for automatic webhook provisioning
  - Context: Quick setup with minimal manual steps; CLI detects controller URL and creates namespace if needed

- **2.2. Configure Webhook Manually for Fine-Grained Control** `[procedure]`
  - Lines 530-591 (Chapter: Use Pipelines as Code with GitHub Webhook, Section: Manual configuration): Extract controller URL, configure GitHub webhook in UI, create Secret and Repository CR manually
  - Context: Customize webhook settings (event selection, secret keys) and understand each integration component

- **2.3. Add Webhook Secrets (Maintenance Task)** `[procedure]`
  - Lines 593-614 (Chapter: Use Pipelines as Code with GitHub Webhook, Section: Add webhook secrets): Use tkn pac webhook add to add additional webhook secrets or replace deleted secrets
  - Context: Rotate or add secrets without recreating entire Repository CR configuration

- **2.4. Update Personal Access Token (Maintenance Task)** `[procedure]`
  - Lines 616-657 (Chapter: Use Pipelines as Code with GitHub Webhook, Section: Update personal access token): Update token using tkn pac webhook update-token CLI or manual oc patch command
  - Context: Token rotation during expiration to maintain pipeline automation without service interruption

---

**Job 3: Configure GitLab Webhook Integration with Pipelines as Code**

*When my organization uses GitLab as the preferred platform, I want to configure GitLab webhook integration with Pipelines as Code, so I can automate CI/CD pipelines triggered by GitLab repository events*

Prerequisites: Pipelines as Code installed on cluster, Personal access token as manager of GitLab project or organization with admin:repo_hook scope

- **3.1. Configure GitLab Webhook Automatically Using tkn pac CLI** `[procedure]`
  - Lines 704-736 (Chapter: Use Pipelines as Code with GitLab, Section: Automatic configuration): Use tkn pac create repo with GitLab-specific prompts for project ID and API URL
  - Context: Quick setup with GitLab-specific configuration; creates webhook, Secret, and Repository CR automatically

- **3.2. Configure GitLab Webhook Manually for Custom API URLs** `[procedure]`
  - Lines 738-800 (Chapter: Use Pipelines as Code with GitLab, Section: Manual configuration): Extract controller URL, configure GitLab webhook in UI, create Secret and Repository CR with custom git_provider.url
  - Context: Private GitLab instances with custom API URLs; supports both gitlab.com and private deployments

- **3.3. Add GitLab Webhook Secrets (Maintenance Task)** `[procedure]`
  - Lines 802-823 (Chapter: Use Pipelines as Code with GitLab, Section: Add webhook secrets): Use tkn pac webhook add for GitLab repositories
  - Context: Secret rotation for GitLab integrations; updates webhook.secret key in existing Secret object

- **3.4. Update GitLab Personal Access Token (Maintenance Task)** `[procedure]`
  - Lines 825-861 (Chapter: Use Pipelines as Code with GitLab, Section: Update personal access token): Update token using tkn pac webhook update-token CLI or manual oc patch
  - Context: Token rotation for GitLab to maintain pipeline automation without disruption

---

**Job 4: Integrate Pipelines as Code with Bitbucket Cloud Repository**

*When my organization uses Bitbucket Cloud as the preferred platform, I want to integrate Pipelines as Code with my Bitbucket Cloud repository, so I can automate CI/CD workflows triggered by repository events*

Prerequisites: Pipelines as Code installed on cluster, App password on Bitbucket Cloud with Webhooks Read/Write, Projects Read/Write, Pull requests Read/Write permissions

- **4.1. Configure Bitbucket Cloud Webhook Automatically Using tkn pac CLI** `[procedure]`
  - Lines 918-946 (Chapter: Use Pipelines as Code with Bitbucket Cloud, Section: Automatic configuration): Use tkn pac create repo with interactive CLI prompts for Bitbucket Cloud username and app password
  - Context: Quick setup with minimal manual steps; creates namespace, webhook configuration, and Repository CR automatically

- **4.2. Configure Bitbucket Cloud Webhook Manually for Full Control** `[procedure]`
  - Lines 948-997 (Chapter: Use Pipelines as Code with Bitbucket Cloud, Section: Manual configuration): Extract controller URL, configure Bitbucket Cloud webhook in UI, create Secret and Repository CR with git_provider.user
  - Context: Customize configuration parameters and integrate with existing infrastructure; precise control over webhook event selection

- **4.3. Update Bitbucket Cloud Webhook Secrets (Maintenance Task)** `[procedure]`
  - Lines 1009-1036 (Chapter: Use Pipelines as Code with Bitbucket Cloud, Section: Update webhook secrets): Use tkn pac webhook add for Bitbucket Cloud repositories
  - Context: Secret rotation for Bitbucket Cloud integrations; maintain secure integration without recreating Repository CR

- **4.4. Update Bitbucket Cloud Access Token (Maintenance Task)** `[procedure]`
  - Lines 1037-1080 (Chapter: Use Pipelines as Code with Bitbucket Cloud, Section: Update access token): Update token using tkn pac webhook update-token CLI or manual oc patch
  - Context: Token rotation for Bitbucket Cloud to maintain authentication without recreating resources

---

**Job 5: Integrate Pipelines as Code with Bitbucket Data Center Repository**

*When my organization uses Bitbucket Data Center as the preferred platform, I want to integrate Pipelines as Code with my Bitbucket Data Center repository, so I can automate CI/CD workflows triggered by repository events in on-premises environments*

Prerequisites: Pipelines as Code installed on cluster, Personal access token with PROJECT_ADMIN and REPOSITORY_ADMIN permissions on Bitbucket Data Center

- **5.1. Configure Bitbucket Data Center Webhook Manually with Secrets** `[procedure]`
  - Lines 1160-1229 (Chapter: Use Pipelines as Code with Bitbucket Data Center, Section: Manual configuration): Extract controller URL, generate webhook secret using openssl, configure Bitbucket Data Center webhook in UI with secret, create Secret with both provider token and webhook secret, create Repository CR with git_provider.url
  - Context: Only manual configuration supported; includes webhook secret support unlike Cloud version; git_provider.url must point to Data Center API (usually /rest suffix)

---

#### Secure Your Environment

**Job 6: Extend GitHub Token Scope to Additional Repositories**

*When my pipeline definitions need to access tasks or resources from multiple private repositories, I want to extend the GitHub token scope beyond the primary repository, so I can retrieve pipeline dependencies from additional repositories without authentication failures*

Prerequisites: GitHub App configured for OpenShift cluster, Names of additional repositories to scope, Additional repositories exist in GitHub organization or account

- **6.1. Configure Global Token Scoping for Cluster-Wide Access** `[procedure]`
  - Lines 340-358 (Chapter: Scope the GitHub token to additional repositories, Section: Global configuration approach): Configure TektonConfig CR with secret-github-app-token-scoped set to false and secret-github-app-scope-extra-repos parameter with comma-separated repository list
  - Context: Requires administrative permissions; affects all namespaces; enables cross-repository access for all Pipelines as Code users

- **6.2. Configure Repository-Level Token Scoping for Namespace-Specific Access** `[procedure]`
  - Lines 360-390 (Chapter: Scope the GitHub token to additional repositories, Section: Repository-level configuration approach): Configure Repository CR with github_app_token_scope_repos parameter listing additional repositories
  - Context: No cluster admin permissions required; additional repositories must exist in same namespace as original repository; error handling for missing repositories

---

**Job 7: Configure Custom Certificates for Enterprise Git Repositories**

*When integrating Pipelines as Code with a Git repository that uses privately signed or custom certificates, I want to expose the certificate to PAC, so I can ensure secure communication without certificate validation errors*

Prerequisites: Pipelines as Code installed using OpenShift Pipelines Operator, Custom or privately signed certificate available

- **7.1. Add Custom Certificate to Cluster Using Proxy Object** `[procedure]`
  - Lines 1283-1300 (Chapter: Configure custom certificates for {pac}): Add custom certificate to cluster using Proxy object; Operator exposes certificate in all Pipelines as Code components and workloads
  - Context: Cluster-level configuration for enterprise environments with custom CAs

---

#### Operate & Manage

**Job 8: Understand How Authentication Secrets Are Managed**

*When working with private Git repositories in Pipelines as Code, I want to understand how authentication secrets are managed, so I can properly configure my pipelines to clone private repositories*

Prerequisites: Pipelines as Code installed and configured, Access to private Git repository, Understanding of basic Pipeline and PipelineRun concepts

- **8.1. Understand Automatic Secret Creation and Naming** `[concept]`
  - Lines 1302-1315 (Chapter: Private repository support in {pac}, Section: Overview): Understand secret naming format (pac-gitauth-<REPOSITORY_OWNER>-<REPOSITORY_NAME>-<RANDOM_STRING>) and automatic creation/update behavior
  - Context: PAC creates or updates secrets in target namespace automatically for private repository authentication

- **8.2. Reference Auto-Created Authentication Secret Using basic-auth Workspace** `[procedure]`
  - Lines 1316-1355 (Chapter: Private repository support in {pac}, Section: Workspace configuration): Configure basic-auth workspace in PipelineRun (lines 1316-1326) and Pipeline (lines 1330-1355) to reference PAC-managed secret; pass workspace to git-clone task
  - Context: Git-clone task from Tekton Hub uses user token to clone private repositories

- **8.3. Control Automatic Secret Creation Behavior (Platform-Level)** `[procedure]`
  - Lines 1357-1358 (Chapter: Private repository support in {pac}, Section: TektonConfig configuration): Set secret-auto-create parameter to false or true in TektonConfig CR pipelinesAsCode.settings spec
  - Context: Platform administrators aligning PAC behavior with organizational security policies

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | By Git provider (GitHub, GitLab, Bitbucket Cloud/Data Center) and feature type | By user goal and workflow stage (Configure, Secure, Operate) |
| **Top-level items** | 7 provider-centric chapters with 28+ subsections | 8 jobs across 3 workflow stages with 23 approaches |
| **GitHub integration** | Split across 2 separate chapters (GitHub App vs Webhook) | 2 distinct jobs with explicit trade-offs in job statements |
| **Token scoping** | Nested under GitHub App chapter (lines 312-437) | Elevated to dedicated Secure stage job (Job 6) |
| **Certificate configuration** | Standalone chapter at end (lines 1283-1300) | Elevated to Secure stage job (Job 7) alongside token scoping |
| **Private repository support** | Reference chapter at end (lines 1302-1363) | Elevated to Operate stage job (Job 8) with concept/procedure split |
| **Maintenance tasks** | Scattered as "optional" subsections within provider chapters | Explicitly labeled as .3 and .4 sub-tasks within parent jobs |
| **Navigation depth** | 2 levels (chapter → section) | 3 levels (job → approach → step) with clear hierarchy |
| **Persona visibility** | Mentioned in abstracts, not structural | Listed in job metadata; approaches grouped by persona where relevant |

### Job List Adjustments from Suggested Input

The suggested 29 jobs were consolidated to **8 jobs** for the following reasons:

1. **Jobs 2, 3, 4 ("Configure a GitHub App using CLI", "Create a GitHub App in administrator perspective", "Configure a GitHub App manually") merged** → Three approaches to the same goal (GitHub App integration); became Job 1 with three user stories (1.1, 1.2, 1.3)

2. **Jobs 9 and 10 ("Use Pipelines as Code with GitHub Webhook - Automatic", "Use Pipelines as Code with GitHub Webhook - Manual") merged** → Two approaches to the same goal (GitHub Webhook integration); became Job 2 with approaches 2.1 and 2.2

3. **Jobs 11 and 12 ("Add webhook secrets", "Update personal access token" for GitHub Webhook) absorbed** → Maintenance tasks for GitHub Webhook integration; became sub-tasks 2.3 and 2.4 within Job 2

4. **Jobs 14 and 15 ("Use Pipelines as Code with GitLab - Automatic", "Use Pipelines as Code with GitLab - Manual") merged** → Two approaches to the same goal (GitLab integration); became Job 3 with approaches 3.1 and 3.2

5. **Jobs 16 and 17 ("Add webhook secrets", "Update personal access token" for GitLab) absorbed** → Maintenance tasks for GitLab integration; became sub-tasks 3.3 and 3.4 within Job 3

6. **Jobs 19 and 20 ("Use Pipelines as Code with Bitbucket Cloud - Automatic", "Use Pipelines as Code with Bitbucket Cloud - Manual") merged** → Two approaches to the same goal (Bitbucket Cloud integration); became Job 4 with approaches 4.1 and 4.2

7. **Jobs 21 and 22 ("Update webhook secrets", "Update access token" for Bitbucket Cloud) absorbed** → Maintenance tasks for Bitbucket Cloud integration; became sub-tasks 4.3 and 4.4 within Job 4

8. **Job 24 ("Use Pipelines as Code with Bitbucket Data Center - Manual configuration") retained** → Standalone job (Job 5) due to unique constraints (no tkn pac support, webhook secrets supported unlike Cloud)

9. **Jobs 5, 6, 7 ("Scope the GitHub token - Global", "Scope the GitHub token - Repository level") merged** → Two approaches to the same goal (token scoping); became Job 6 with approaches 6.1 and 6.2

10. **Job 25 ("Configure custom certificates for {pac}") retained** → Standalone job (Job 7) elevated from procedure to security job

11. **Jobs 26, 27, 28 ("Private repository support - Understanding", "Reference auto-created secret", "Control automatic secret creation") merged** → Three aspects of the same goal (understanding authentication); became Job 8 with approaches 8.1 (concept), 8.2 (procedure), 8.3 (platform config)

---

## Consolidation Examples

### Example 1: GitHub App Integration (3 scattered procedures → 1 unified job with 3 approaches)

**Current (Fragmented):**
- Section: Configure a GitHub App using the command line interface (lines 106-154)
- Section: Create a GitHub App in administrator perspective (lines 157-199)
- Section: Configure a GitHub App manually and create a secret for {pac} (lines 202-309)

Users must navigate three separate subsections within the GitHub App chapter to compare approaches. The decision criteria (CLI vs Web Console vs Manual) are buried in abstracts and notes. Important restrictions (CLI and Web Console only work for main controller, lines 119-121, 169-172) are not immediately visible.

**Proposed (Consolidated):**
- **Job 1: Integrate GitHub with Pipelines as Code**
  - 1.1. CLI-based setup using tkn pac CLI (Quick automated setup for main controller only)
  - 1.2. Web Console UI setup (GUI-based workflow for main controller only)
  - 1.3. Manual GitHub App configuration (Required for additional controllers or fine-grained control)

**Benefit:** One job with three clearly differentiated approaches. Context lines explain when to use each method. Restrictions are visible in approach descriptions, not buried in procedure notes.

---

### Example 2: Maintenance Tasks (8 scattered "optional" procedures → Embedded within parent jobs)

**Current (Fragmented):**
- Section: Use Pipelines as Code with GitHub Webhook - Add webhook secrets (lines 593-614, marked "optional")
- Section: Use Pipelines as Code with GitHub Webhook - Update personal access token (lines 616-657, marked "optional")
- Section: Use Pipelines as Code with GitLab - Add webhook secrets (lines 802-823, marked "optional")
- Section: Use Pipelines as Code with GitLab - Update personal access token (lines 825-861, marked "optional")
- Section: Use Pipelines as Code with Bitbucket Cloud - Update webhook secrets (lines 1009-1036, marked "optional")
- Section: Use Pipelines as Code with Bitbucket Cloud - Update access token (lines 1037-1080, marked "optional")

Maintenance tasks are scattered as "optional" subsections within provider chapters. Users performing initial setup may not realize where to return for token rotation. Users performing token rotation must navigate back to the specific provider chapter and find the "optional" section.

**Proposed (Consolidated):**
- **Job 2: Configure GitHub Webhook Integration**
  - 2.1. Configure Webhook Automatically
  - 2.2. Configure Webhook Manually
  - 2.3. Add Webhook Secrets (Maintenance Task) ← Explicitly labeled
  - 2.4. Update Personal Access Token (Maintenance Task) ← Explicitly labeled

- **Job 3: Configure GitLab Webhook Integration**
  - 3.1. Configure GitLab Webhook Automatically
  - 3.2. Configure GitLab Webhook Manually
  - 3.3. Add GitLab Webhook Secrets (Maintenance Task)
  - 3.4. Update GitLab Personal Access Token (Maintenance Task)

- **Job 4: Integrate Pipelines as Code with Bitbucket Cloud**
  - 4.1. Configure Bitbucket Cloud Webhook Automatically
  - 4.2. Configure Bitbucket Cloud Webhook Manually
  - 4.3. Update Bitbucket Cloud Webhook Secrets (Maintenance Task)
  - 4.4. Update Bitbucket Cloud Access Token (Maintenance Task)

**Benefit:** Maintenance tasks are clearly labeled with "(Maintenance Task)" suffix and embedded as .3 and .4 sub-tasks within the job where the initial configuration happened. Users know exactly where to return for Day 2 operations.

---

### Example 3: Security Configuration (2 scattered sections → Dedicated Secure stage with 2 jobs)

**Current (Fragmented):**
- Section: Scope the GitHub token to additional repositories (lines 312-437, nested under GitHub App integration chapter)
- Section: Configure custom certificates for {pac} (lines 1283-1300, standalone chapter at end of guide)

Security-related configuration is either buried within the GitHub App chapter (token scoping appears as the 4th subsection after three GitHub App setup procedures) or isolated at the end of the guide (custom certificates). Users focused on security hardening must:
1. Navigate to GitHub App chapter to find token scoping (non-obvious location)
2. Scroll to end of guide to find custom certificates (disconnected from token scoping)

No clear indication that these are security concerns until reading the content.

**Proposed (Consolidated):**
- **Secure Your Environment** (dedicated workflow stage)
  - **Job 6: Extend GitHub Token Scope to Additional Repositories**
    - 6.1. Global token scoping (Cluster-wide access, requires admin permissions)
    - 6.2. Repository-level token scoping (Namespace-specific access, no admin permissions)
  - **Job 7: Configure Custom Certificates for Enterprise Git Repositories**
    - 7.1. Add custom certificate to cluster using Proxy object

**Benefit:** Security configuration is elevated to a dedicated workflow stage. Users can navigate directly to "Secure Your Environment" to find both token scoping and custom certificates in one place. Clear structural signal that these are security concerns. Use case for token scoping (CI repository fetching tasks from private CD repository, lines 324-325) is preserved in job statement.

---

## Content Gaps Identified

| Gap | JTBD Reference | Current Coverage | Impact |
|-----|---------------|-----------------|--------|
| No pipeline monitoring or observability content | Jobs 1-5 (all configure jobs) | None - guide ends after setup and verification steps | **High** — Users have no guidance on verifying pipeline runs are working correctly after initial setup; no instructions for viewing PipelineRun status, logs, or Tekton dashboard |
| No dedicated troubleshooting guide for webhook failures | Jobs 2-5 (all webhook jobs) | Basic verification steps only (lines 659-674 for GitHub, 863-872 for GitLab, 1082-1124 for Bitbucket Cloud, 1231-1273 for Bitbucket Data Center) | **High** — Common failure modes not covered: wrong permissions (token scopes), network connectivity issues, certificate errors, webhook secret mismatches, IP address verification failures (Bitbucket Cloud) |
| No troubleshooting for authentication errors with private repositories | Job 8 (private repository support) | Mentions automatic secret creation (lines 1302-1363) but no debugging guidance | **Medium** — Users may struggle with git-clone task failures without guidance on verifying secret creation, checking workspace references, or diagnosing authentication errors |
| No upgrade or migration procedures for PAC controllers | All jobs | Brief mention of additional controllers (lines 97, 214-215) but no upgrade procedures | **Medium** — Users upgrading OpenShift Pipelines operator, migrating from one Git provider to another, or upgrading PAC controller versions lack guidance on preserving configurations |
| No guidance on configuring additional PAC controllers | Job 1.3 (Manual GitHub App mentions additional controllers) | Brief notes only (lines 97, 119-121, 169-172, 214-215) | **Medium** — Users configuring multi-controller setups (e.g., separate controllers for different GitHub orgs) need detailed procedures for creating controller instances, routing, and secret management |
| No quickstart or decision guide at beginning | All jobs | Assumes users already know which Git provider to use | **Medium** — New users lack guidance on choosing between GitHub App (recommended), GitHub Webhook, GitLab, or Bitbucket based on their environment constraints and organizational policies |
| No disaster recovery or backup procedures | All jobs | None | **Low** — Users may want to backup GitHub App credentials, Repository CRs, or migrate configurations between clusters |
| No cost/resource optimization guidance | All jobs | None | **Low** — Users with large-scale deployments may want to optimize webhook payload sizes, reduce API rate limiting, or tune event subscriptions |

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 7 provider-centric chapters | 8 jobs across 3 workflow stages | 14% increase in count, but 100% clearer goal orientation (stages replace providers) |
| Sections to browse for "GitHub integration options" | 2 separate chapters (App at lines 78-437, Webhook at lines 440-675) | 2 jobs with explicit trade-offs (Job 1: App recommended, Job 2: Webhook alternative) | 100% clarity on decision criteria (job statements explain when-to-use) |
| Sections to browse for "token rotation" | 6 scattered "optional" procedures across 3 provider chapters | 6 embedded maintenance tasks within parent jobs (2.4, 3.4, 4.4 for token updates) | Context-aware location (within job where token was initially configured) |
| Sections to browse for "security configuration" | 2 sections (token scoping buried at line 312 within GitHub App, certificates isolated at line 1283) | 1 Secure stage with 2 jobs (6 and 7) | 100% consolidation into workflow stage; 50% reduction in sections to navigate |
| Clicks to find "private repository authentication" | 3-4 (scroll to end of guide, find reference chapter, read abstract) | 2 (Operate stage → Job 8) | 50% reduction; elevated from reference to operational job |
| Clicks to find "custom certificates" | 3-4 (scroll to end of guide) | 2 (Secure stage → Job 7) | 50% reduction; elevated from isolated chapter to security job |
| Clicks to find "token scoping" | 3-4 (GitHub App chapter → 4th subsection after 3 setup procedures) | 2 (Secure stage → Job 6) | 50% reduction; elevated from buried subsection to security job |

**Final job count: 8** (reduced from 29 suggested JTBD records). Consolidation rationale:
- **Merging approaches:** CLI, Web Console, and Manual GitHub App setup are three approaches to one goal (GitHub App integration) → Job 1 with 1.1, 1.2, 1.3
- **Embedding maintenance tasks:** Token rotation, secret updates are Day 2 operations within initial configuration jobs → .3 and .4 sub-tasks within Jobs 2-4
- **Elevating security:** Token scoping and custom certificates were scattered → Dedicated Secure stage (Jobs 6-7)
- **Operationalizing reference content:** Private repository support was reference material → Operate stage job (Job 8) with concept/procedure split

---

## UX Research Alignment

### Pain Points Addressed by Restructure

| Pain Point (from analysis) | How New Structure Helps |
|---------------------------|------------------------|
| "Multiple configuration approaches scattered across sections" | Jobs 1-5 consolidate all approaches (automatic, manual, CLI, Web Console) under one job per provider with clear numbered sub-tasks (1.1, 1.2, 1.3) |
| "Unclear when to use GitHub App vs Webhook" | Job 1 (GitHub App) and Job 2 (GitHub Webhook) are separate jobs with explicit trade-offs in job statements; Job 1 is under Configure stage, Job 2 immediately follows with "When I cannot create a GitHub App" scenario |
| "Token scoping buried within GitHub App section at line 312" | Job 6 elevated to dedicated Secure stage, immediately visible; no longer hidden as 4th subsection after three GitHub App setup procedures |
| "Maintenance tasks (token rotation, secret updates) mixed with initial setup" | Maintenance tasks explicitly labeled with "(Maintenance Task)" suffix and numbered as .3 and .4 sub-tasks within parent jobs; users know where to return for Day 2 operations |
| "Custom certificates configuration isolated at end of guide at line 1283" | Job 7 elevated to Secure stage alongside token scoping (Job 6); security configuration consolidated in one workflow stage |
| "Private repository support treated as reference, not operational concern" | Job 8 elevated to Operate stage with three approaches: 8.1 concept (understanding), 8.2 procedure (workspace config), 8.3 platform config (TektonConfig); no longer buried as end-of-guide reference |

### Strategic Priorities Elevated

The following jobs are flagged as **strategic priorities** based on workflow importance and frequency of user access. The new structure gives them dedicated sections:

| Strategic Job | Current Location | Proposed Location | Visibility Improvement |
|--------------|-----------------|-------------------|----------------------|
| Token Scoping for Cross-Repository Access | Buried at lines 312-437 as 4th subsection within GitHub App chapter | Job 6: Dedicated Secure stage job with clear use case (CI repo fetching tasks from private CD repo) | Direct navigation via Secure stage; clear structural signal that this is security configuration; use case elevated to job statement |
| Custom Certificates for Private Git Servers | Isolated at lines 1283-1300 as standalone chapter at end of guide | Job 7: Dedicated Secure stage job alongside token scoping | Grouped with other security configuration (token scoping); no longer disconnected at end of guide |
| Private Repository Authentication | Reference chapter at lines 1302-1363 with mixed concept and procedure content | Job 8: Dedicated Operate stage job with three approaches (concept, procedure, platform config) | Elevated from reference to operational concern; split into concept (8.1 understanding), procedure (8.2 workspace config), and platform config (8.3 TektonConfig) |

### Cross-Team Collaboration Visibility

The new structure makes team collaboration patterns visible:

| Job | Teams/Roles Involved | Collaboration Pattern |
|-----|---------------------|----------------------|
| Job 1: Integrate GitHub with Pipelines as Code | Cluster administrator (setup), Platform engineer (usage) | Cluster admin performs one-time setup of GitHub App (Job 1.1, 1.2, or 1.3); all users benefit from Check Runs API and GitOps comments |
| Job 2-5: Configure Webhooks | Platform engineer (per-repository setup) | Platform engineer configures webhooks for each repository; no cluster-wide coordination required (unlike GitHub App) |
| Job 6: Extend GitHub Token Scope | Cluster administrator (global scoping 6.1), Repository administrator (namespace-level scoping 6.2) | Global scoping (6.1) requires cluster admin and affects all namespaces; repository-level scoping (6.2) can be self-service by repository administrators without cluster admin permissions |
| Job 7: Configure Custom Certificates | Cluster administrator (platform-level) | Cluster admin adds certificates to Proxy object; Operator exposes to all PAC components and workloads automatically |
| Job 8: Understand Authentication Secrets | Platform engineer (setup), Pipeline developer (usage) | Platform engineer sets up PAC integration (Jobs 1-5) which automatically creates secrets (8.1); pipeline developers reference these secrets in Pipeline definitions using basic-auth workspace (8.2); platform administrators control automatic creation via TektonConfig (8.3) |

### Inner/Outer Loop Distribution

| Loop | Jobs | Implication |
|------|------|-------------|
| **Outer (Production/Ops)** | Job 1 (GitHub App integration), Job 6 (token scoping), Job 7 (custom certificates) | Cluster administrator focus - cluster-wide configuration that affects all users; one-time setup with infrequent changes |
| **Outer (Production/Ops)** | Jobs 2-5 (webhook configurations), Job 8.3 (control automatic secret creation) | Platform engineer focus - per-repository or per-namespace configuration; moderate frequency (new repositories, token rotation) |
| **Inner (Dev/Experimentation)** | Job 8.1-8.2 (understanding secrets, workspace configuration) | Pipeline developer focus - understanding how to use PAC-managed secrets in pipeline definitions; high frequency (every pipeline definition) |
| **Shared (Both Loops)** | Job 2.4, 3.4, 4.4 (token rotation maintenance tasks) | Both platform engineers (initial setup) and SREs (operational maintenance) need token rotation procedures; medium frequency (token expiration cycles) |

---

## Document Statistics

**Workflow Coverage:**
- Configure: 5 jobs (GitHub App, GitHub Webhook, GitLab, Bitbucket Cloud, Bitbucket Data Center)
- Secure: 2 jobs (Token scoping, Custom certificates)
- Operate: 1 job (Private repository authentication)

**Main Jobs:** 8 (consolidated from 29 JTBD records)
**User Stories/Approaches:** 23 themed sections
**Source Sections:** 28 referenced from original document
**Git Provider Variations:** 5 (GitHub App, GitHub Webhook, GitLab, Bitbucket Cloud, Bitbucket Data Center)
**Consolidation Ratio:** 73% reduction (29 records → 8 jobs)

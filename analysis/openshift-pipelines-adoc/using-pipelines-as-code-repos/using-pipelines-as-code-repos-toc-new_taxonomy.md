# Using Pipelines as Code with Git Repository Hosting Service Providers
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** Enable cluster administrators and platform engineers to integrate Pipelines as Code with various Git repository hosting service providers for automated CI/CD workflows.

**Personas:** Cluster administrator, Platform engineer, Repository administrator, Pipeline developer, Platform administrator

**Main Jobs:** 10 core jobs across 3 workflow stages (Configure, Secure, Operate)

---

## Quick Navigation

**I want to:**
- Set up GitHub App integration -> Job 1 (Configure)
- Configure GitHub Webhook instead of App -> Job 2 (Configure)
- Integrate with GitLab -> Job 3 (Configure)
- Set up Bitbucket Cloud integration -> Job 4 (Configure)
- Configure Bitbucket Data Center -> Job 5 (Configure)
- Extend GitHub token scope to additional repositories -> Job 6 (Secure)
- Configure custom certificates for private Git servers -> Job 7 (Secure)
- Manage webhook secrets for existing setup -> Job 2.3 or 3.3 or 4.3 (Operate)
- Update personal access tokens -> Job 2.4 or 3.4 or 4.4 or 5.4 (Operate)
- Understand how private repository authentication works -> Job 9 (Configure)

---

# Table of Contents

## Set Up & Configure

### Job 1: Integrate GitHub with Pipelines as Code
*When I need to enable Git-based CI/CD workflows for my team, I want to integrate GitHub with Pipelines as Code, so I can trigger pipeline runs automatically from repository events*

**Personas:** Cluster administrator

**Requires:** OpenShift Pipelines operator installed

#### 1.1 Choose GitHub App Configuration Method

**Context:** Three approaches exist for GitHub App setup, each suited to different scenarios.

- **Option A: CLI-based setup using tkn pac CLI** (For quick automated setup)
  *Persona: Cluster administrator*
  → Lines 106-154: Configure a GitHub App using the command line interface
  Source: Chapter: GitHub App integration with {pac}, Section: Configure a GitHub App using the command line interface; module: modules/op-pac-configuring-github-app-cli.adoc lines 1-47
  - **Restriction:** Only works for main controller (not additional controllers)
  - Supports GitHub Enterprise via --github-api-url option
  - Minimizes manual configuration steps

- **Option B: Web Console UI setup** (For GUI-based workflows)
  *Persona: Cluster administrator*
  → Lines 157-199: Create a GitHub App in administrator perspective
  Source: Chapter: GitHub App integration with {pac}, Section: Create a GitHub App in administrator perspective; module: modules/op-creating-a-github-application-in-administrator-perspective.adoc lines 1-40
  - **Restriction:** Only works for main controller
  - GitHub App details saved as secret in openshift-pipelines namespace automatically
  - No CLI expertise required

- **Option C: Manual GitHub App configuration** (For fine-grained control and additional controllers)
  *Persona: Cluster administrator*
  → Lines 202-309: Configure a GitHub App manually and create a secret for {pac}
  Source: Chapter: GitHub App integration with {pac}, Section: Configure a GitHub App manually and create a secret for {pac}; module: modules/op-pac-configuring-github-app-manually.adoc lines 1-106
  - **Required method** for additional Pipelines as Code controllers
  - Detailed permission requirements: Repository permissions (lines 253-260), Organization permissions (lines 261-263), event subscriptions (lines 265-273)
  - GitHub Enterprise support automatic

---

### Job 2: Configure GitHub Webhook Integration with Appropriate Permissions
*When I cannot create a GitHub App but need to integrate my repository with Pipelines as Code, I want to configure GitHub Webhook integration with appropriate permissions, so I can automate CI/CD pipelines triggered by repository events*

**Personas:** Platform engineer

**Requires:** Pipelines as Code installed on cluster, Personal access token on GitHub with admin:repo_hook scope

**Why:** GitHub Webhook does not support Check Runs API or GitOps comments like /retest

#### 2.1 Configure Webhook Automatically Using tkn pac CLI

**Goal:** Provision webhooks and Repository CRs without manual GitHub UI configuration.

- **Task:** Run tkn pac create repo command
  → Lines 499-528: Automatic configuration
  Source: Chapter: Use Pipelines as Code with GitHub Webhook; module: modules/op-using-pipelines-as-code-with-github-webhook.adoc lines 58-87
  - CLI detects controller URL automatically
  - Creates namespace if needed
  - Sets up webhook and Repository CR

#### 2.2 Configure Webhook Manually for Fine-Grained Control

**Goal:** Customize webhook settings and understand each integration component.

- **Task:** Extract Pipelines as Code controller public URL
  → Lines 532-537: Extract controller URL
  Source: Chapter: Use Pipelines as Code with GitHub Webhook; module: modules/op-using-pipelines-as-code-with-github-webhook.adoc lines 89-94

- **Task:** Configure GitHub webhook in UI
  → Lines 539-556: GitHub webhook configuration
  Source: Chapter: Use Pipelines as Code with GitHub Webhook; module: modules/op-using-pipelines-as-code-with-github-webhook.adoc lines 97-114
  - Set payload URL to PAC controller
  - Generate webhook secret using openssl
  - Select events: Commit comments, Issue comments, Pull request, Pushes

- **Task:** Create Secret and Repository CR
  → Lines 558-591: Create Secret and Repository CR
  Source: Chapter: Use Pipelines as Code with GitHub Webhook; module: modules/op-using-pipelines-as-code-with-github-webhook.adoc lines 116-150
  - Secret contains personal access token and webhook secret
  - Repository CR references the secret

#### 2.3 Add Webhook Secrets (Maintenance Task)

**Goal:** Maintain secure webhook payload validation without recreating configuration.

- **Task:** Add webhook secret using tkn pac CLI
  → Lines 593-614: Add webhook secrets
  Source: Chapter: Use Pipelines as Code with GitHub Webhook; module: modules/op-using-pipelines-as-code-with-github-webhook.adoc lines 152-173
  - Updates existing Secret object with new webhook.secret key

#### 2.4 Update Personal Access Token (Maintenance Task)

**Goal:** Maintain pipeline automation without service interruption during token rotation.

- **Task:** Update token using tkn pac CLI or oc patch
  → Lines 616-657: Update personal access token
  Source: Chapter: Use Pipelines as Code with GitHub Webhook; module: modules/op-using-pipelines-as-code-with-github-webhook.adoc lines 175-216
  - Two approaches: CLI (tkn pac webhook update-token) or manual (oc patch)
  - Updates provider.token in Secret object

---

### Job 3: Configure GitLab Webhook Integration with Pipelines as Code
*When my organization uses GitLab as the preferred platform, I want to configure GitLab webhook integration with Pipelines as Code, so I can automate CI/CD pipelines triggered by GitLab repository events*

**Personas:** Platform engineer

**Requires:** Pipelines as Code installed on cluster, Personal access token as manager of GitLab project or organization

**Why:** Token scoped for specific project cannot access MR from forked repositories

#### 3.1 Configure GitLab Webhook Automatically Using tkn pac CLI

**Goal:** Provision webhooks and Repository CRs with GitLab-specific configuration without manual UI steps.

- **Task:** Run tkn pac create repo command with GitLab prompts
  → Lines 704-736: Automatic configuration
  Source: Chapter: Use Pipelines as Code with GitLab; module: modules/op-using-pipelines-as-code-with-gitlab.adoc lines 26-58
  - CLI prompts for GitLab-specific details including project ID and API URL
  - Creates webhook, Secret, and Repository CR automatically

#### 3.2 Configure GitLab Webhook Manually for Custom API URLs

**Goal:** Customize API URLs and settings for private GitLab instances.

- **Task:** Extract Pipelines as Code controller public URL
  → Lines 740-745: Extract controller URL
  Source: Chapter: Use Pipelines as Code with GitLab; module: modules/op-using-pipelines-as-code-with-gitlab.adoc lines 60-65

- **Task:** Configure GitLab webhook in UI
  → Lines 747-762: GitLab webhook configuration
  Source: Chapter: Use Pipelines as Code with GitLab; module: modules/op-using-pipelines-as-code-with-gitlab.adoc lines 67-82
  - Set URL to PAC controller
  - Generate webhook secret
  - Select events: Commit comments, Issue comments, Pull request, Pushes

- **Task:** Create Secret and Repository CR with custom API URL
  → Lines 764-800: Create Secret and Repository CR
  Source: Chapter: Use Pipelines as Code with GitLab; module: modules/op-using-pipelines-as-code-with-gitlab.adoc lines 84-122
  - Supports private GitLab instances with custom git_provider.url field

#### 3.3 Add GitLab Webhook Secrets (Maintenance Task)

**Goal:** Maintain secure webhook validation for GitLab integrations without full reconfiguration.

- **Task:** Add webhook secret using tkn pac CLI
  → Lines 802-823: Add webhook secrets
  Source: Chapter: Use Pipelines as Code with GitLab; module: modules/op-using-pipelines-as-code-with-gitlab.adoc lines 124-145
  - Updates webhook.secret key in existing OpenShift Secret object

#### 3.4 Update GitLab Personal Access Token (Maintenance Task)

**Goal:** Maintain pipeline automation for GitLab repositories without service interruption during token rotation.

- **Task:** Update token using tkn pac CLI or oc patch
  → Lines 825-861: Update personal access token
  Source: Chapter: Use Pipelines as Code with GitLab; module: modules/op-using-pipelines-as-code-with-gitlab.adoc lines 147-183
  - Two approaches: CLI or manual oc patch
  - Updates provider.token in Secret object

---

### Job 4: Integrate Pipelines as Code with Bitbucket Cloud Repository
*When my organization uses Bitbucket Cloud as the preferred platform, I want to integrate Pipelines as Code with my Bitbucket Cloud repository, so I can automate CI/CD workflows triggered by repository events*

**Personas:** Platform engineer

**Requires:** Pipelines as Code installed on cluster, App password on Bitbucket Cloud with Webhooks Read/Write, Projects Read/Write, Pull requests Read/Write permissions

**Why:** Bitbucket Cloud does not support webhook secrets; PAC verifies webhook sources by IP address instead

#### 4.1 Configure Bitbucket Cloud Webhook Automatically Using tkn pac CLI

**Goal:** Complete setup with minimal manual steps.

- **Task:** Run tkn pac create repo command
  → Lines 918-946: Automatic configuration
  Source: Chapter: Use Pipelines as Code with Bitbucket Cloud; module: modules/op-using-pipelines-as-code-with-bitbucket-cloud.adoc lines 33-61
  - Interactive CLI prompts guide through setup
  - Creates namespace, webhook configuration, and Repository CR automatically

#### 4.2 Configure Bitbucket Cloud Webhook Manually for Full Control

**Goal:** Customize configuration parameters and integrate with existing infrastructure.

- **Task:** Extract Pipelines as Code controller public URL
  → Lines 950-955: Extract controller URL
  Source: Chapter: Use Pipelines as Code with Bitbucket Cloud; module: modules/op-using-pipelines-as-code-with-bitbucket-cloud.adoc lines 63-68

- **Task:** Configure Bitbucket Cloud webhook in UI
  → Lines 957-968: Bitbucket Cloud webhook configuration
  Source: Chapter: Use Pipelines as Code with Bitbucket Cloud; module: modules/op-using-pipelines-as-code-with-bitbucket-cloud.adoc lines 70-81
  - Set URL to PAC controller
  - Select events: Repository Push, Pull Request Created/Updated/Comment created

- **Task:** Create Secret and Repository CR
  → Lines 969-997: Create Secret and Repository CR
  Source: Chapter: Use Pipelines as Code with Bitbucket Cloud; module: modules/op-using-pipelines-as-code-with-bitbucket-cloud.adoc lines 82-112
  - Secret contains app password
  - Repository CR references user and secret

#### 4.3 Update Bitbucket Cloud Webhook Secrets (Maintenance Task)

**Goal:** Maintain secure integration without recreating the entire Repository CR during secret rotation.

- **Task:** Add or update webhook secret using tkn pac CLI
  → Lines 1009-1036: Update webhook secrets
  Source: Chapter: Use Pipelines as Code with Bitbucket Cloud; module: modules/op-using-pipelines-as-code-with-bitbucket-cloud.adoc lines 124-150
  - Uses tkn pac webhook add command

#### 4.4 Update Bitbucket Cloud Access Token (Maintenance Task)

**Goal:** Maintain authentication without recreating resources during token rotation.

- **Task:** Update token using tkn pac CLI or oc patch
  → Lines 1037-1080: Update access token
  Source: Chapter: Use Pipelines as Code with Bitbucket Cloud; module: modules/op-using-pipelines-as-code-with-bitbucket-cloud.adoc lines 152-195
  - Two approaches: tkn pac webhook update-token CLI or manual oc patch

---

### Job 5: Integrate Pipelines as Code with Bitbucket Data Center Repository
*When my organization uses Bitbucket Data Center as the preferred platform, I want to integrate Pipelines as Code with my Bitbucket Data Center repository, so I can automate CI/CD workflows triggered by repository events in on-premises environments*

**Personas:** Platform engineer

**Requires:** Pipelines as Code installed on cluster, Personal access token with PROJECT_ADMIN and REPOSITORY_ADMIN permissions on Bitbucket Data Center

**Why:** Unlike Bitbucket Cloud, Bitbucket Data Center supports webhook secrets for secure payload validation

**Timing:** Manual configuration only - tkn pac commands not supported

#### 5.1 Configure Bitbucket Data Center Webhook Manually with Secrets

**Goal:** Establish secure on-premises CI/CD integration.

- **Task:** Extract Pipelines as Code controller public URL
  → Lines 1160-1165: Extract controller URL
  Source: Chapter: Use Pipelines as Code with Bitbucket Data Center; module: modules/op-using-pipelines-as-code-with-bitbucket-server.adoc lines 24-29

- **Task:** Generate webhook secret
  → Lines 1175-1180: Generate webhook secret
  Source: Chapter: Use Pipelines as Code with Bitbucket Data Center; module: modules/op-using-pipelines-as-code-with-bitbucket-server.adoc lines 39-44
  - Use openssl rand -hex 20 or similar tool

- **Task:** Configure Bitbucket Data Center webhook in UI with secret
  → Lines 1167-1189: Bitbucket Data Center webhook configuration
  Source: Chapter: Use Pipelines as Code with Bitbucket Data Center; module: modules/op-using-pipelines-as-code-with-bitbucket-server.adoc lines 31-53
  - Set URL to PAC controller
  - Add webhook secret for payload security
  - Select events: Repository Push, Repository Modified, Pull Request Opened/Source branch updated/Comment added

- **Task:** Create Secret with both provider token and webhook secret
  → Lines 1191-1198: Create Secret object
  Source: Chapter: Use Pipelines as Code with Bitbucket Data Center; module: modules/op-using-pipelines-as-code-with-bitbucket-server.adoc lines 55-62
  - Secret contains both provider.token and webhook.secret

- **Task:** Create Repository CR with git_provider.url
  → Lines 1200-1229: Create Repository CR
  Source: Chapter: Use Pipelines as Code with Bitbucket Data Center; module: modules/op-using-pipelines-as-code-with-bitbucket-server.adoc lines 64-94
  - git_provider.url points to Data Center API (usually with /rest suffix)

---

## Secure Your Environment

### Job 6: Extend GitHub Token Scope to Additional Repositories
*When my pipeline definitions need to access tasks or resources from multiple private repositories, I want to extend the GitHub token scope beyond the primary repository, so I can retrieve pipeline dependencies from additional repositories without authentication failures*

**Personas:** Cluster administrator, Repository administrator

**Requires:** GitHub App configured for OpenShift cluster, Names of additional repositories to scope

**Why:** Use case: CI repository with pipeline definition fetching tasks from private CD repository

#### 6.1 Configure Global Token Scoping for Cluster-Wide Access

**Goal:** Enable cross-repository access for all Pipelines as Code users without per-repository configuration.

- **Task:** Configure TektonConfig CR with secret-github-app-scope-extra-repos
  → Lines 340-358: Global configuration approach
  Source: Chapter: Scope the GitHub token to additional repositories; module: modules/op-scoping-github-token.adoc lines 27-45
  - Requires administrative permissions
  - Set secret-github-app-token-scoped to false
  - List repositories in secret-github-app-scope-extra-repos parameter

#### 6.2 Configure Repository-Level Token Scoping for Namespace-Specific Access

**Goal:** Enable cross-repository access without requiring cluster administrator permissions.

- **Task:** Configure Repository CR with github_app_token_scope_repos
  → Lines 360-390: Repository-level configuration approach
  Source: Chapter: Scope the GitHub token to additional repositories; module: modules/op-scoping-github-token.adoc lines 47-77
  - Does not require administrative permissions
  - Additional repositories must exist in same namespace as original repository
  - Error handling for missing repositories (lines 383-390)

---

### Job 7: Configure Custom Certificates for Enterprise Git Repositories
*When integrating Pipelines as Code with a Git repository that uses privately signed or custom certificates, I want to expose the certificate to PAC, so I can ensure secure communication without certificate validation errors*

**Personas:** Cluster administrator

**Requires:** Pipelines as Code installed using OpenShift Pipelines Operator, Custom or privately signed certificate available

#### 7.1 Add Custom Certificate to Cluster Using Proxy Object

**Goal:** Expose custom certificate in all Pipelines as Code components and workloads.

- **Task:** Add certificate to cluster using Proxy object
  → Lines 1283-1300: Configure custom certificates for {pac}
  Source: Chapter: Configure custom certificates for {pac}; module: modules/op-interfacing-pipelines-as-code-with-custom-certificates.adoc lines 1-14
  - Operator exposes certificate in all Pipelines as Code components and workloads

---

## Operate & Manage

### Job 8: Understand How Authentication Secrets Are Managed
*When working with private Git repositories in Pipelines as Code, I want to understand how authentication secrets are managed, so I can properly configure my pipelines to clone private repositories*

**Personas:** Pipeline developer

**Requires:** Pipelines as Code installed and configured, Access to private Git repository, Understanding of basic Pipeline and PipelineRun concepts

#### 8.1 Understand Automatic Secret Creation and Naming

**Goal:** Understand how PAC creates and names authentication secrets automatically.

- **Task:** Learn secret naming format
  → Lines 1302-1315: Secret naming and creation
  Source: Chapter: Private repository support in {pac}; module: modules/op-using-private-repositories-with-pipelines-as-code.adoc lines 1-14
  - Secret format: pac-gitauth-<REPOSITORY_OWNER>-<REPOSITORY_NAME>-<RANDOM_STRING>
  - PAC creates or updates secret in target namespace automatically

#### 8.2 Reference Auto-Created Authentication Secret Using basic-auth Workspace

**Goal:** Ensure git-clone task receives proper authentication credentials.

- **Task:** Configure basic-auth workspace in PipelineRun
  → Lines 1316-1326: PipelineRun workspace configuration
  Source: Chapter: Private repository support in {pac}; module: modules/op-using-private-repositories-with-pipelines-as-code.adoc lines 13-23
  - Reference secret with basic-auth workspace

- **Task:** Configure basic-auth workspace in Pipeline
  → Lines 1330-1355: Pipeline workspace configuration
  Source: Chapter: Private repository support in {pac}; module: modules/op-using-private-repositories-with-pipelines-as-code.adoc lines 27-52
  - Pass basic-auth workspace to git-clone task

#### 8.3 Control Automatic Secret Creation Behavior (Platform-Level)

**Goal:** Align with organizational security policies and secret management practices.

- **Task:** Configure secret-auto-create parameter in TektonConfig
  → Lines 1357-1358: Configure TektonConfig CR
  Source: Chapter: Private repository support in {pac}; module: modules/op-using-private-repositories-with-pipelines-as-code.adoc lines 54-55
  - Set secret-auto-create to false or true in TektonConfig CR pipelinesAsCode.settings spec

---

## Appendices

### A. Git Provider Comparison Matrix

| Provider | App/Webhook | Supported Features | Token Requirements | Limitations |
|----------|-------------|-------------------|-------------------|-------------|
| GitHub App | App | Check Runs API, GitOps comments (/retest) | GitHub App credentials | Recommended method |
| GitHub Webhook | Webhook | Basic webhook events | Personal access token with repo scope | No Check Runs API, no /retest |
| GitLab | Webhook | Merge request comments | Personal access token with api scope | Token scoped for project cannot access MR from forks |
| Bitbucket Cloud | Webhook | Basic webhook events | App password with Webhooks R/W | No webhook secrets (IP verification instead) |
| Bitbucket Data Center | Webhook | Webhook secrets supported | Personal token with PROJECT_ADMIN, REPOSITORY_ADMIN | Manual configuration only (no tkn pac) |

### B. Configuration Method Selection Guide

| Method | Best For | Complexity | Repeatability | Prerequisites |
|--------|----------|------------|---------------|---------------|
| tkn pac CLI (GitHub App) | Quick automated setup | Low | High | tkn CLI with pac plugin |
| Web Console (GitHub App) | GUI-based workflows | Low | Manual | OpenShift web console access |
| Manual (GitHub App) | Additional controllers, fine-grained control | Medium | High | GitHub UI access, oc CLI |
| tkn pac CLI (Webhooks) | Automated webhook setup | Low | High | tkn CLI with pac plugin |
| Manual (Webhooks) | Custom configurations | Medium | High | Git provider UI access, oc CLI |

### C. Workflow Coverage Analysis

| Stage | Coverage | Jobs | Notes |
|-------|----------|------|-------|
| Configure | ✅ | Jobs 1-5 | All major Git providers covered |
| Secure | ✅ | Jobs 6-7 | Token scoping, custom certificates |
| Operate | ✅ | Job 8 | Private repository authentication |
| Monitor | ❌ | - | No pipeline observability content in this guide |
| Troubleshoot | ⚠️ Limited | Verification steps within jobs | Only basic verification, no dedicated troubleshooting |
| Upgrade | ❌ | - | No token rotation or upgrade procedures (maintenance tasks embedded within jobs) |

### Gaps Identified

| Stage | Gap | Recommendation |
|-------|-----|----------------|
| Monitor | No pipeline monitoring | Link to Tekton monitoring guide |
| Troubleshoot | No dedicated troubleshooting section | Add troubleshooting guide for webhook failures, authentication errors |
| Upgrade | No controller upgrade procedures | Add section on upgrading PAC controllers and migrating configurations |

---

## Navigation Guide

### By User Journey

**Cluster Administrator setting up GitHub App integration:**
1. Job 1: Choose GitHub App configuration method (CLI, Web Console, or Manual)
2. Job 6: Extend GitHub token scope to additional repositories (if needed)
3. Job 7: Configure custom certificates (if using private Git servers)

**Platform Engineer integrating with GitLab:**
1. Job 3: Configure GitLab webhook integration (automatic or manual)
2. Job 8: Understand private repository authentication
3. Job 3.4: Update personal access token (when token expires)

**Platform Engineer integrating with Bitbucket Cloud:**
1. Job 4: Integrate with Bitbucket Cloud repository
2. Job 4.4: Update access token (maintenance task)

**Platform Engineer integrating with Bitbucket Data Center:**
1. Job 5: Configure Bitbucket Data Center webhook manually
2. Job 8: Understand private repository authentication

**Repository Administrator managing token scope:**
1. Job 6.2: Configure repository-level token scoping (no cluster admin needed)

---

## Document Statistics

**Workflow Coverage:**
- Configure: 5 jobs (GitHub App, GitHub Webhook, GitLab, Bitbucket Cloud, Bitbucket Data Center)
- Secure: 2 jobs (Token scoping, Custom certificates)
- Operate: 1 job (Private repository authentication)

**Main Jobs:** 8
**User Stories/Paths:** 23 themed sections
**Source Sections:** 28 referenced
**Git Provider Variations:** 5 (GitHub App, GitHub Webhook, GitLab, Bitbucket Cloud, Bitbucket Data Center)

# Using Pipelines as Code with a Git repository hosting service provider
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** This guide helps cluster administrators integrate Pipelines as Code with Git repository hosting services to enable automated CI/CD pipeline triggers from Git events.

**Personas:** Cluster administrator

**Main Jobs:** 5 core jobs across 3 workflow stages (Define, Prepare, Modify)

---

## Quick Navigation

**I want to:**
- Understand integration options → Job 1 (Define)
- Set up GitHub App integration → Job 2 (Prepare)
- Configure webhook-based integration → Job 2 (Prepare)
- Extend token scope to multiple repos → Job 3 (Modify)
- Configure custom certificates → Job 4 (Prepare)
- Understand private repository authentication → Job 5 (Prepare)

---

# Table of Contents

## Choose Your Approach

### Job 1: Understand Git Repository Integration Options
*When I need to integrate my Git repositories with OpenShift Pipelines*

**Personas:** Cluster administrator

#### Understanding GitHub App Integration

→ Lines 78-104: GitHub App integration with Pipelines as Code
  Source: Concept module

- GitHub Apps integrate Pipelines with Git-based workflows
- Cluster administrators configure single GitHub App for all users
- Webhooks point to Pipelines as Code controller endpoint
- Three setup methods available: tkn CLI, web console, manual
- Recommended integration method for GitHub repositories

**Key Decision:** GitHub App is the recommended service for GitHub integration. For non-GitHub platforms or when GitHub App cannot be created, webhook-based alternatives are available.

---

## Set Up & Configure

### Job 2: Integrate Git Repository Hosting Service with Pipelines as Code
*When I need to establish connection between Git repositories and OpenShift Pipelines*

**Personas:** Cluster administrator

#### 2.1. Configure GitHub App Using Command Line Interface [procedure]

→ Lines 106-155: Configure a GitHub App using the command line interface
  Source: Procedure module

**Context:** Use when you prefer automated CLI-based setup and are configuring the main (default) Pipelines as Code controller.

**Prerequisites:** 
- OpenShift CLI access as cluster administrator
- tkn command line utility with tkn pac plugin installed

**Key Steps:**
- Run `tkn pac bootstrap github-app`
- Specify GitHub API endpoint for GitHub Enterprise
- Verify app appears in GitHub account settings

**Limitations:** Only works for main controller; use manual method for additional controllers.

---

#### 2.2. Create GitHub App via Administrator Perspective [procedure]

→ Lines 157-200: Create a GitHub App in administrator perspective
  Source: Procedure module

**Context:** Use when you prefer visual/UI-based setup over CLI and are configuring the main controller.

**Prerequisites:**
- OpenShift Pipelines operator installed
- Access to OpenShift web console as administrator

**Key Steps:**
- Navigate to Pipelines page in admin perspective
- Click "Setup GitHub App"
- Enter GitHub App name and credentials
- Verify app details saved as secret in openshift-pipelines namespace

**Limitations:** Only works for main controller; use manual method for additional controllers.

---

#### 2.3. Configure GitHub App Manually [procedure]

→ Lines 202-310: Configure a GitHub App manually and create a secret for Pipelines as Code
  Source: Procedure module

**Context:** Required for configuring additional Pipelines as Code controllers or when you need full control over the GitHub App configuration.

**Prerequisites:**
- OpenShift Pipelines operator installed
- GitHub account with permissions to create GitHub Apps
- Cluster administrator access

**Key Steps:**
1. Sign in to GitHub and navigate to Developer Settings → GitHub Apps
2. Create new GitHub App with:
   - Webhook URL pointing to Pipelines as Code controller route
   - Webhook secret (generated with openssl)
   - Repository permissions: Checks, Contents, Issues, Pull request (Read & Write)
   - Organization permissions: Members (Read-only)
   - Event subscriptions: Check run, Pull request, Push, Issue comment, etc.
3. Generate and download private key
4. Create OpenShift secret with private key, App ID, and webhook secret
5. Install app on target repositories

**Benefits:** 
- Supports multiple controllers with separate GitHub Apps
- Full control over permissions and configuration
- Works with GitHub Enterprise

---

#### 2.4. Use GitHub Webhook (Alternative to GitHub App) [procedure]

→ Lines 440-675: Use Pipelines as Code with GitHub Webhook
  Source: Procedure module

**Context:** Use when you cannot create a GitHub App. Note that this approach does not support GitHub Check Runs API, so status appears as PR comments instead of the Checks tab.

**Prerequisites:**
- Pipelines as Code installed on cluster
- GitHub personal access token with appropriate scope

**Key Steps (Automated):**
- Run `tkn pac create repo` for interactive setup

**Key Steps (Manual):**
1. Extract Pipelines as Code controller public URL
2. Configure webhook in GitHub repository settings
3. Create OpenShift secret with personal access token and webhook secret
4. Create Repository custom resource

**Limitations:**
- No Check Runs API access
- No GitOps comments (/retest, /ok-to-test) support
- Must create new commits to restart CI

---

#### 2.5. Configure GitLab Integration [procedure]

→ Lines 677-882: Use Pipelines as Code with GitLab
  Source: Procedure module

**Context:** Use when your organization uses GitLab as the Git hosting platform.

**Prerequisites:**
- Pipelines as Code installed on cluster
- GitLab personal access token with api scope

**Key Steps (Automated):**
- Run `tkn pac create repo` with GitLab repository URL

**Key Steps (Manual):**
1. Extract Pipelines as Code controller public URL
2. Configure webhook in GitLab project settings
3. Create OpenShift secret with personal access token and webhook secret
4. Create Repository CR with GitLab-specific configuration

**Note:** For private GitLab instances, set git_provider.url to your GitLab API URL.

**Token Scope Limitation:** Tokens scoped to specific projects cannot access merge requests from forked repositories; Pipelines as Code will display results as comments.

---

#### 2.6. Configure Bitbucket Cloud Integration [procedure]

→ Lines 884-1132: Use Pipelines as Code with Bitbucket Cloud
  Source: Procedure module

**Context:** Use when your organization uses Bitbucket Cloud as the Git hosting platform.

**Prerequisites:**
- Pipelines as Code installed on cluster
- Bitbucket Cloud app password with appropriate permissions (Email, Workspace membership, Projects, Issues, Pull requests)

**Key Steps (Automated):**
- Run `tkn pac create repo` with Bitbucket Cloud repository URL

**Key Steps (Manual):**
1. Extract Pipelines as Code controller public URL
2. Configure webhook in Bitbucket Cloud repository settings
3. Create OpenShift secret with app password
4. Create Repository CR with Bitbucket username

**Security Note:** Bitbucket Cloud does not support webhook secrets. Pipelines as Code verifies that webhook requests come from Bitbucket Cloud IP addresses. You can disable this check or add additional safe IPs via TektonConfig settings.

---

#### 2.7. Configure Bitbucket Data Center Integration [procedure]

→ Lines 1134-1281: Use Pipelines as Code with Bitbucket Data Center
  Source: Procedure module

**Context:** Use when your organization uses on-premise Bitbucket Data Center.

**Prerequisites:**
- Pipelines as Code installed on cluster
- Bitbucket Data Center personal access token with PROJECT_ADMIN and REPOSITORY_ADMIN permissions
- Token must have access to forked repositories

**Key Steps:**
1. Extract Pipelines as Code controller public URL
2. Configure webhook in Bitbucket Data Center repository settings with webhook secret
3. Create OpenShift secret with personal access token and webhook secret
4. Create Repository CR with correct Bitbucket API URL (without /api/v1.0 suffix)

**Important:** Ensure git_provider.url points to the REST API endpoint (typically has /rest suffix, not /api/v1.0).

---

### Job 3: Scope the GitHub Token to Additional Repositories
*When my pipeline definitions need to access multiple private repositories beyond the main repository*

**Personas:** Cluster administrator
**Timing:** Configure after GitHub App setup, before running pipelines that require access to additional repositories

#### Global Configuration (Cross-Namespace Access)

→ Lines 340-358: Global token scope configuration in TektonConfig
  Source: Procedure module, configuration section

**Context:** Use when you need to grant access to repositories across different namespaces. Requires cluster administrator permissions.

**Configuration:**
- Set `secret-github-app-token-scoped: false` in TektonConfig CR
- Specify additional repositories in `secret-github-app-scope-extra-repos` parameter

**Example:**
```yaml
secret-github-app-scope-extra-repos: "owner2/project2, owner3/project3"
```

---

#### Repository-Level Configuration (Same Namespace)

→ Lines 360-391: Repository-level token scope in Repository CR
  Source: Procedure module, configuration section

**Context:** Use when additional repositories exist in the same namespace as the main repository. Does not require cluster administrator permissions.

**Configuration:**
- Specify additional repositories in `github_app_token_scope_repos` parameter of Repository CR

**Validation:** If any specified repositories do not exist in the namespace, token scoping fails with an error message.

---

### Job 4: Configure Custom Certificates for Pipelines as Code
*When my Git repository uses privately signed or custom certificates*

**Personas:** Cluster administrator

→ Lines 1283-1300: Configure custom certificates for Pipelines as Code
  Source: Procedure module

**Context:** Use when connecting to Git repositories that use non-standard certificate authorities (CAs), such as enterprise Git hosting services with internal CAs.

**Configuration:**
- Add custom certificate to cluster using the Proxy object
- OpenShift Pipelines Operator automatically exposes the certificate to all Pipelines components including Pipelines as Code

**Benefit:** Centralized certificate management; no need to distribute certificates to individual components.

---

### Job 5: Understand Private Repository Authentication
*When I need to reference how Pipelines as Code handles authentication to private repositories*

**Personas:** Cluster administrator

→ Lines 1302-1364: Private repository support in Pipelines as Code
  Source: Reference module

**How it works:**
- Pipelines as Code creates/updates a secret in the target namespace with format: `pac-gitauth-<REPOSITORY_OWNER>-<REPOSITORY_NAME>-<RANDOM_STRING>`
- This secret contains the user token for Git authentication
- git-clone task from Tekton Hub uses this token to clone private repositories

**Pipeline Configuration:**
1. Reference the secret in the pipelinerun with basic-auth workspace:
```yaml
workspace:
  - name: basic-auth
    secret:
      secretName: "{{ git_auth_secret }}"
```

2. Pass workspace to git-clone task in the pipeline definition

**Configuration:** Set `secret-auto-create` parameter in TektonConfig CR to control automatic secret creation behavior.

---

## Appendices

### A. Git Hosting Service Comparison Matrix

| Service | Integration Method | Token Type | Webhook Secret | GitOps Commands | Check Runs API |
|---------|-------------------|------------|----------------|----------------|----------------|
| GitHub | GitHub App (recommended) | GitHub App token | Yes | Yes | Yes |
| GitHub | Webhook | Personal access token | Yes | No | No |
| GitLab | Webhook | Personal access token | Yes | Yes | No |
| Bitbucket Cloud | Webhook | App password | No (IP verification) | Yes | No |
| Bitbucket Data Center | Webhook | Personal access token | Yes | Yes | No |

### B. Setup Method Selection Guide

| Method | Use Case | Supports Additional Controllers | Prerequisites |
|--------|----------|-------------------------------|---------------|
| tkn pac bootstrap | Quick automated setup for main controller | No | tkn CLI with pac plugin |
| Web console (Admin perspective) | Visual setup for main controller | No | OpenShift web console access |
| Manual GitHub App creation | Additional controllers or full control | Yes | GitHub account permissions |
| Webhook-based (non-GitHub App) | Cannot create GitHub App | N/A | Personal access token or app password |

### C. Workflow Coverage Analysis

| Stage | Coverage | Jobs | Notes |
|-------|----------|------|-------|
| Define | ✅ | Job 1 | Understanding integration options |
| Prepare | ✅ | Jobs 2, 4, 5 | Setup and configuration for all supported Git platforms |
| Execute | ❌ | - | Not covered; this guide focuses on setup, not pipeline execution |
| Modify | ✅ | Job 3 | Token scope extension for multi-repo access |
| Monitor | ❌ | - | Pipeline monitoring covered in separate guides |
| Troubleshoot | ⚠️ Limited | - | Limited troubleshooting guidance; mainly setup verification |

### Gaps Identified

| Stage | Gap | Recommendation |
|-------|-----|----------------|
| Execute | No pipeline execution guidance | Link to "Creating pipeline runs in Pipelines as Code" guide |
| Monitor | No pipeline monitoring content | Link to OpenShift Pipelines monitoring documentation |
| Troubleshoot | Limited troubleshooting procedures | Add common integration issues and resolutions section |

---

## Navigation Guide

### By User Journey

**Setting up GitHub integration for the first time:**
1. Job 1: Understand integration options → Choose GitHub App
2. Job 2.1: Configure GitHub App using CLI (easiest) OR
   Job 2.2: Configure via web console (visual) OR
   Job 2.3: Configure manually (full control)
3. Job 5: Reference private repository authentication if needed

**Setting up GitLab/Bitbucket integration:**
1. Job 1: Understand integration options
2. Job 2.5: Configure GitLab OR
   Job 2.6: Configure Bitbucket Cloud OR
   Job 2.7: Configure Bitbucket Data Center
3. Job 5: Reference private repository authentication if needed

**Managing multi-repository pipelines:**
1. Job 2: Set up base Git integration
2. Job 3: Scope GitHub token to additional repositories
3. Job 5: Reference private repository authentication

**Enterprise/custom certificate scenarios:**
1. Job 4: Configure custom certificates
2. Job 2: Set up Git integration with custom certificate trust

---

## Document Statistics

**Workflow Coverage:**
- Define: 1 job
- Prepare: 3 jobs
- Modify: 1 job
- Execute: Gap identified
- Monitor: Gap identified

**Main Jobs:** 5
**User Stories/Paths:** 7 (multiple integration approaches for Job 2)
**Source Sections:** 11 modules
**Platform/Tool Variations:** 5 Git hosting services (GitHub App, GitHub Webhook, GitLab, Bitbucket Cloud, Bitbucket Data Center)

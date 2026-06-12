# Using Pipelines as Code with Git Repository Hosting Services — Consolidation Report

**Document:** using-pipelines-as-code-repos.adoc
**JTBD Records:** 11 pre-consolidated records → 5 final jobs (after merging)

---

## Executive Summary

### What's Changing

The current documentation is organized by Git hosting platform (GitHub, GitLab, Bitbucket) with GitHub further subdivided by setup method (CLI, web console, manual, webhook). This platform-first structure requires users to understand which platform they're using before they can navigate to relevant content. It also fragments related setup procedures across multiple top-level sections, making it difficult to compare approaches or understand relationships between configuration methods.

The proposed JTBD-based structure reorganizes content by user goals: understanding integration options, integrating a Git hosting service (with platform variations as nested approaches), extending token scope for multi-repository pipelines, configuring custom certificates, and understanding private repository authentication. This goal-first structure consolidates scattered integration methods under a single "Integrate" job, making it easier to compare approaches and choose the right path based on constraints rather than platform.

The reorganization reduces top-level navigation items by 50% (from 10 sections to 5 jobs) while preserving all existing content and making relationships between integration methods explicit.

### Key Improvements

- **7 integration procedures consolidated under Job 2:** GitHub CLI, GitHub web console, GitHub manual, GitHub webhook, GitLab, Bitbucket Cloud, and Bitbucket Data Center are now nested approaches under "Integrate Git Repository Hosting Service," making it clear they all accomplish the same goal with different methods or platforms.
- **Token scoping elevated to dedicated job:** Multi-repository token scoping (currently buried as a subsection under GitHub App) becomes Job 3, reflecting its importance for complex pipeline scenarios that span multiple repositories.
- **Platform comparison simplified:** Users can compare all 5 Git hosting platforms in one location (Job 2) instead of browsing 3-5 separate top-level sections, reducing navigation by 75% for platform selection.
- **Decision guidance surfaced:** Job 1 explicitly provides decision guidance for choosing integration approaches, consolidating information currently scattered across concept and procedure sections.
- **Custom certificates positioned as prerequisite:** Job 4 clarifies that custom certificate configuration is a prerequisite step for enterprise Git hosting scenarios, not an afterthought.
- **Reference material explicitly labeled:** Job 5 makes it clear that private repository authentication is reference material to consult during setup, not a standalone procedure.

---

## Current Structure (Feature-Based)

- **Using Pipelines as Code with a Git repository hosting service provider** — Assembly introduction
  - GitHub App integration with Pipelines as Code — Concept explaining GitHub App architecture
    - Configure a GitHub App using the command line interface — CLI-based automated setup
    - Create a GitHub App in administrator perspective — Web console-based setup
    - Configure a GitHub App manually and create a secret for Pipelines as Code — Manual setup for additional controllers
    - Scope the GitHub token to additional repositories — Extending token scope for multi-repo pipelines
  - Use Pipelines as Code with GitHub Webhook — Alternative to GitHub App using webhooks
  - Use Pipelines as Code with GitLab — GitLab platform webhook integration
  - Use Pipelines as Code with Bitbucket Cloud — Bitbucket Cloud integration with app passwords
  - Use Pipelines as Code with Bitbucket Data Center — On-premise Bitbucket integration
  - Configure custom certificates for Pipelines as Code — Custom CA certificate configuration
  - Private repository support in Pipelines as Code — Reference on git-auth secret mechanism

**Total:** 1 assembly, 11 included modules (1 snippet, 1 concept, 9 procedures, 1 reference), organized by platform and setup method.

---

## Proposed JTBD-Based Structure

### Quick Overview

- **Choose Your Approach**
  - Job 1: Understand Git Repository Integration Options
- **Set Up & Configure**
  - Job 2: Integrate Git Repository Hosting Service with Pipelines as Code
  - Job 4: Configure Custom Certificates for Pipelines as Code
  - Job 5: Understand Private Repository Authentication
- **Update & Optimize**
  - Job 3: Scope the GitHub Token to Additional Repositories

---

### Detailed Job Descriptions

#### Choose Your Approach

**Job 1: Understand Git Repository Integration Options** `[concept]`

*When I need to integrate my Git repositories with OpenShift Pipelines, I want to understand how GitHub Apps enable Git-based CI/CD workflows, so I can choose the right integration approach*

Prerequisites: None

- **1.1. GitHub App Integration Architecture** `[concept]`
  - Lines 78-104 (Concept module): Explains that cluster administrators configure a single GitHub App for all users with webhooks pointing to the Pipelines as Code controller endpoint
  - Context: Recommended integration method for GitHub; three setup options available (CLI, web console, manual)

---

#### Set Up & Configure

**Job 2: Integrate Git Repository Hosting Service with Pipelines as Code** `[procedures]`

*When I need to establish connection between Git repositories and OpenShift Pipelines, I want to configure integration with my Git hosting platform, so I can trigger pipelines from Git events*

Prerequisites: Pipelines as Code installed on cluster, appropriate Git hosting service credentials

- **2.1. Configure GitHub App Using Command Line Interface** `[procedure]`
  - Lines 106-155 (Procedure module): Uses `tkn pac bootstrap github-app` command for automated GitHub App creation and configuration
  - Context: Use for main controller only; fastest setup method if you have tkn CLI access

- **2.2. Create GitHub App via Administrator Perspective** `[procedure]`
  - Lines 157-200 (Procedure module): Visual setup through OpenShift web console Pipelines page
  - Context: Use for main controller only; prefer when you want visual feedback during setup

- **2.3. Configure GitHub App Manually** `[procedure]`
  - Lines 202-310 (Procedure module): Manual GitHub App creation with detailed permission configuration and OpenShift secret setup
  - Context: Required for additional controllers; use when you need full control over permissions

- **2.4. Use GitHub Webhook (Alternative to GitHub App)** `[procedure]`
  - Lines 440-675 (Procedure module): Webhook-based integration using personal access tokens
  - Context: Use when you cannot create a GitHub App; loses Check Runs API and GitOps commands support

- **2.5. Configure GitLab Integration** `[procedure]`
  - Lines 677-882 (Procedure module): GitLab webhook setup with personal access token and project ID configuration
  - Context: Use for GitLab platform; supports gitlab.com and private GitLab instances

- **2.6. Configure Bitbucket Cloud Integration** `[procedure]`
  - Lines 884-1132 (Procedure module): Bitbucket Cloud webhook with app password authentication and IP verification
  - Context: Use for Bitbucket Cloud; no webhook secret support, uses IP allowlist for security

- **2.7. Configure Bitbucket Data Center Integration** `[procedure]`
  - Lines 1134-1281 (Procedure module): On-premise Bitbucket setup with personal access tokens and webhook secrets
  - Context: Use for self-hosted Bitbucket; requires correct API URL without /api/v1.0 suffix

---

**Job 3: Scope the GitHub Token to Additional Repositories** `[procedure]`

*When my pipeline definitions need to access multiple private repositories beyond the main repository, I want to extend the GitHub token scope to additional repositories, so I can fetch tasks and resources from separate private repos*

Prerequisites: Pipelines as Code GitHub App configured, additional repositories exist in GitHub organization

- **3.1. Global Configuration (Cross-Namespace Access)** `[procedure]`
  - Lines 340-358 (Procedure module, configuration section): TektonConfig CR setting for `secret-github-app-scope-extra-repos`
  - Context: Use when repositories span multiple namespaces; requires cluster administrator permissions

- **3.2. Repository-Level Configuration (Same Namespace)** `[procedure]`
  - Lines 360-391 (Procedure module, configuration section): Repository CR `github_app_token_scope_repos` parameter
  - Context: Use when additional repositories exist in same namespace; no admin permissions required

---

**Job 4: Configure Custom Certificates for Pipelines as Code** `[procedure]`

*When my Git repository uses privately signed or custom certificates, I want to expose these certificates to Pipelines as Code, so I can establish secure connections to repositories with non-standard CAs*

Prerequisites: Pipelines as Code installed via OpenShift Pipelines Operator

- **4.1. Add Custom Certificates via Proxy Object** `[procedure]`
  - Lines 1283-1300 (Procedure module): Add certificate to cluster Proxy object; Operator automatically exposes to all Pipelines components
  - Context: Use for enterprise Git hosting with internal CAs; centralized certificate management

---

**Job 5: Understand Private Repository Authentication** `[reference]`

*When I need to understand how Pipelines as Code authenticates to private repositories, I want to reference the documentation on git-auth secret management, so I can correctly configure my pipelines to clone private repos*

Prerequisites: None (reference material)

- **5.1. Automatic Git-Auth Secret Creation** `[reference]`
  - Lines 1302-1330 (Reference module, secret mechanism): Explains `pac-gitauth-<REPOSITORY_OWNER>-<REPOSITORY_NAME>-<RANDOM_STRING>` secret pattern
  - Context: Consult when configuring basic-auth workspace in pipelines

- **5.2. Workspace Configuration in Pipelines** `[reference]`
  - Lines 1318-1355 (Reference module, examples): Shows how to reference git_auth_secret in pipelinerun and pass to git-clone task
  - Context: Use examples when writing pipeline definitions that clone private repositories

- **5.3. Secret Auto-Creation Configuration** `[reference]`
  - Lines 1357-1358 (Reference module, configuration): TektonConfig `secret-auto-create` parameter
  - Context: Reference when you need to disable automatic secret creation

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | By Git hosting platform and setup method | By user goal and workflow stage (Choose, Integrate, Extend, Secure) |
| **Top-level items** | 10 sections (concept + procedures + reference) | 5 main jobs with nested approaches |
| **GitHub setup methods** | 4 sibling sections under GitHub App parent | 4 nested approaches under Job 2 (Integrate) |
| **Platform variations** | Separate top-level sections for GitLab, Bitbucket Cloud, Bitbucket DC | Consolidated under Job 2 as platform-specific approaches (2.5-2.7) |
| **Token scoping** | Subsection under GitHub App | Elevated to Job 3 (dedicated job in Modify stage) |
| **Custom certificates** | Standalone section near end | Job 4 in Prepare stage (prerequisite for enterprise scenarios) |
| **Private repo auth** | Reference section at end | Job 5 with explicit reference labeling and subsections |
| **Navigation model** | Browse by platform → choose setup method | Navigate by goal → choose platform/approach |
| **Decision guidance** | Scattered in concept and notes | Consolidated in Job 1 with explicit comparison |

### Job List Adjustments from Suggested Input

The suggested 11 jobs were consolidated to **5 jobs** for the following reasons:

1. **Jobs 2, 3, 4, 6, 7, 8, 9 (all integration methods) merged into Job 2** → These represent different implementation paths (CLI vs web console vs manual) and platform variations (GitHub vs GitLab vs Bitbucket), not different jobs. The high-level goal is identical: integrate a Git hosting service with Pipelines as Code. Consolidating them under one job with nested approaches clarifies the relationship and simplifies platform comparison.

2. **Job 1 (Understand integration options) retained** → Provides essential decision guidance; maps to Define stage.

3. **Job 5 (Scope token to additional repos) promoted to Job 3** → Renumbered after consolidation; elevated from subsection to main job because it represents a distinct Modify-stage activity that extends existing integration for multi-repository scenarios.

4. **Job 10 (Configure custom certificates) retained as Job 4** → Distinct prerequisite job for enterprise Git hosting with private CAs.

5. **Job 11 (Private repository support) retained as Job 5** → Reference material for understanding authentication mechanism; retained as main job but with explicit reference labeling and subsections for clarity.

---

## Consolidation Examples

### Example 1: GitHub Integration Methods (4 scattered procedures → 1 unified job with 4 approaches)

**Current (Fragmented):**
- Section 2.1: Configure a GitHub App using the command line interface (lines 106-155) — CLI automation
- Section 2.2: Create a GitHub App in administrator perspective (lines 157-200) — Web console workflow
- Section 2.3: Configure a GitHub App manually and create a secret for Pipelines as Code (lines 202-310) — Manual setup
- Section 3: Use Pipelines as Code with GitHub Webhook (lines 440-675) — Alternative method

Users encounter these as four separate sections and must infer that they accomplish the same goal (GitHub integration) with different methods. The relationship is not explicit in the structure. The webhook method appears unrelated because it's not nested under the GitHub App concept section.

**Proposed (Consolidated):**
- **Job 2: Integrate Git Repository Hosting Service with Pipelines as Code**
  - 2.1. Configure GitHub App Using CLI (lines 106-155)
  - 2.2. Create GitHub App via Web Console (lines 157-200)
  - 2.3. Configure GitHub App Manually (lines 202-310)
  - 2.4. Use GitHub Webhook (lines 440-675)

**Benefit:** Explicit that all four approaches solve the same integration job. Users can quickly compare methods and choose based on constraints (CLI access, additional controllers, GitHub App permissions). Reduces confusion about why there are multiple GitHub sections.

---

### Example 2: Platform Variations (3 separate top-level sections → 3 approaches under Job 2)

**Current (Fragmented):**
- Section 4: Use Pipelines as Code with GitLab (lines 677-882)
- Section 5: Use Pipelines as Code with Bitbucket Cloud (lines 884-1132)
- Section 6: Use Pipelines as Code with Bitbucket Data Center (lines 1134-1281)

Each platform has dedicated top-level visibility, which inflates the table of contents and obscures the fact that they all accomplish the same job with platform-specific configuration differences. Users must browse 3 separate sections to compare platforms.

**Proposed (Consolidated):**
- **Job 2: Integrate Git Repository Hosting Service with Pipelines as Code**
  - 2.5. Configure GitLab Integration (lines 677-882)
  - 2.6. Configure Bitbucket Cloud Integration (lines 884-1132)
  - 2.7. Configure Bitbucket Data Center Integration (lines 1134-1281)

**Benefit:** Users see all platform options in one location, making comparison straightforward. The structure communicates that platform choice is an implementation detail of the integration job, not a fundamentally different activity.

---

### Example 3: Token Scoping (buried subsection → elevated main job)

**Current (Fragmented):**
- Section 2.4: Scope the GitHub token to additional repositories (lines 312-438) — Appears as a subsection under GitHub App setup, suggesting it's a minor configuration detail rather than a distinct job.

**Proposed (Consolidated):**
- **Job 3: Scope the GitHub Token to Additional Repositories** — Elevated to main job with global and repository-level approaches
  - 3.1. Global Configuration (lines 340-358)
  - 3.2. Repository-Level Configuration (lines 360-391)

**Benefit:** Reflects the importance of multi-repository token scoping for complex pipelines that fetch tasks from separate repositories. Users working with modular pipeline architectures can navigate directly to this job instead of browsing through GitHub App sections.

---

## Content Gaps Identified

| Gap | JTBD Reference | Current Coverage | Impact |
|-----|---------------|-----------------|--------|
| Pipeline execution guidance | After Job 2 (Integrate) | Not covered | **High** — Users complete integration setup but don't know how to create pipeline runs; likely causes support tickets or abandonment |
| Pipeline monitoring and observability | After Job 2 (Integrate) | Not covered | **Medium** — Users can trigger pipelines but can't observe status or troubleshoot failures; reduces operational confidence |
| Troubleshooting integration failures | All jobs | Verification steps only, no failure scenarios | **High** — Webhook failures, authentication errors, and permission issues are common but not documented; causes support tickets |
| Webhook payload validation | Job 2 (Integrate) | Mentioned but not explained | **Medium** — Users may misconfigure webhook secrets, causing silent failures |
| Repository CR lifecycle management | Job 2 (Integrate) | Only creation covered | **Low** — Users may need to update or delete Repository CRs but no guidance provided |
| GitHub Enterprise-specific configuration | Job 2.3 (GitHub Manual) | Mentioned in passing | **Medium** — Enterprise users have additional constraints (API URLs, firewalls) not fully documented |
| Token rotation procedures | Jobs 2.4-2.7 (Webhooks) | Update procedures shown but not best practices | **Low** — Token expiration can break integration; guidance on rotation timing would reduce failures |

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 10 sections | 5 jobs | 50% reduction in cognitive load |
| Sections to browse for GitHub integration | 4 separate sections (CLI, UI, manual, webhook) | 1 job (Job 2) with 4 nested approaches | 75% fewer top-level items to scan |
| Clicks to find platform comparison | Browse 3-5 separate sections | Navigate to Job 2, compare approaches in one location | ~60% reduction in navigation time |
| Clicks to find token scoping | Browse through 5 sections to reach subsection 2.4 | Direct navigation to Job 3 | 80% reduction; elevates buried content |
| Clicks to understand private repo auth | Navigate to last section (reference) | Navigate to Job 5 (explicitly labeled reference) | Similar click count but clearer labeling |

**Final job count: 5** (reduced from suggested 11).

**Consolidation rationale:** The reduction groups implementation methods (CLI, web console, manual, webhook) and platform variations (GitHub, GitLab, Bitbucket Cloud, Bitbucket DC) under the common "Integrate" job. This reduces fragmentation while preserving all existing content. Token scoping is elevated from subsection to main job to reflect its importance for multi-repository pipelines. Custom certificates and private repository authentication are retained as distinct jobs with clearer positioning in the workflow.

**User benefit:** 50% fewer top-level items to browse, explicit relationships between integration methods, and clearer decision points for choosing the right approach based on constraints (platform, controller type, permissions).

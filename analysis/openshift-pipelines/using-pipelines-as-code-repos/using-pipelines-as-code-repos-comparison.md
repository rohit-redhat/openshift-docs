# Using Pipelines as Code with Git Repository Hosting Services - TOC Comparison

**Current Feature-Based vs. Proposed JTBD-Based Structure**

**Analysis Date:** 2026-06-12
**JTBD Records:** 11 pre-consolidated → 5 main jobs (after consolidation)
**Coverage:** 11 modules analyzed

---

## Current Structure (Feature-Based)

Using Pipelines as Code with a Git repository hosting service provider
- GitHub App integration with Pipelines as Code (concept)
  - Configure a GitHub App using the command line interface (procedure)
  - Create a GitHub App in administrator perspective (procedure)
  - Configure a GitHub App manually and create a secret for Pipelines as Code (procedure)
  - Scope the GitHub token to additional repositories (procedure)
- Use Pipelines as Code with GitHub Webhook (procedure)
- Use Pipelines as Code with GitLab (procedure)
- Use Pipelines as Code with Bitbucket Cloud (procedure)
- Use Pipelines as Code with Bitbucket Data Center (procedure)
- Configure custom certificates for Pipelines as Code (procedure)
- Private repository support in Pipelines as Code (reference)

**Total:** 1 assembly, 11 included modules, organized by Git hosting service platform

**Current organizing principle:** Platform/service-based organization (GitHub, GitLab, Bitbucket) with GitHub subdivided by setup method

---

## Proposed JTBD-Based Structure

## Choose Your Approach

**Job 1: Understand Git Repository Integration Options** [concept]
*When I need to integrate my Git repositories with OpenShift Pipelines*

Personas: Cluster administrator

→ Lines 78-104: GitHub App integration with Pipelines as Code
  Source: Concept module

- Explains integration architecture and options
- Recommends GitHub App as preferred method
- Lists three setup approaches

---

## Set Up & Configure

**Job 2: Integrate Git Repository Hosting Service with Pipelines as Code** [procedures]
*When I need to establish connection between Git repositories and OpenShift Pipelines*

Personas: Cluster administrator

**2.1. Configure GitHub App Using Command Line Interface** [procedure]

→ Lines 106-155: Configure a GitHub App using the command line interface
  Source: Procedure module

Context: Automated CLI-based setup for main controller

**2.2. Create GitHub App via Administrator Perspective** [procedure]

→ Lines 157-200: Create a GitHub App in administrator perspective
  Source: Procedure module

Context: Visual UI-based setup for main controller

**2.3. Configure GitHub App Manually** [procedure]

→ Lines 202-310: Configure a GitHub App manually and create a secret for Pipelines as Code
  Source: Procedure module

Context: Required for additional controllers or full control

**2.4. Use GitHub Webhook** [procedure]

→ Lines 440-675: Use Pipelines as Code with GitHub Webhook
  Source: Procedure module

Context: Alternative when GitHub App cannot be created

**2.5. Configure GitLab Integration** [procedure]

→ Lines 677-882: Use Pipelines as Code with GitLab
  Source: Procedure module

Context: GitLab platform integration

**2.6. Configure Bitbucket Cloud Integration** [procedure]

→ Lines 884-1132: Use Pipelines as Code with Bitbucket Cloud
  Source: Procedure module

Context: Bitbucket Cloud platform integration

**2.7. Configure Bitbucket Data Center Integration** [procedure]

→ Lines 1134-1281: Use Pipelines as Code with Bitbucket Data Center
  Source: Procedure module

Context: On-premise Bitbucket integration

---

**Job 3: Scope the GitHub Token to Additional Repositories** [procedure]
*When my pipeline definitions need to access multiple private repositories beyond the main repository*

Personas: Cluster administrator
Timing: BEFORE running multi-repo pipelines - configure after GitHub App setup

→ Lines 312-438: Scope the GitHub token to additional repositories
  Source: Procedure module

- 3.1. Global Configuration (Cross-Namespace Access)
  - Lines 340-358: TektonConfig CR configuration
- 3.2. Repository-Level Configuration (Same Namespace)
  - Lines 360-391: Repository CR configuration

---

**Job 4: Configure Custom Certificates for Pipelines as Code** [procedure]
*When my Git repository uses privately signed or custom certificates*

Personas: Cluster administrator

→ Lines 1283-1300: Configure custom certificates for Pipelines as Code
  Source: Procedure module

- Add certificates via Proxy object
- Operator exposes certificates to all components

---

**Job 5: Understand Private Repository Authentication** [reference]
*When I need to reference how Pipelines as Code handles authentication to private repositories*

Personas: Cluster administrator

→ Lines 1302-1364: Private repository support in Pipelines as Code
  Source: Reference module

- Automatic git-auth secret creation pattern
- Workspace configuration in pipelines
- Reference for git-clone task integration

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | By Git hosting platform (GitHub, GitLab, Bitbucket) | By job to be done (Understand, Integrate, Extend, Secure) |
| **Top-level items** | 10 sections (1 concept + 9 procedures + 1 reference) | 5 main jobs with nested implementation approaches |
| **GitHub setup methods** | Listed as sibling sections under GitHub App | Nested as alternative approaches under Job 2 (Integrate) |
| **Platform variations** | Separate top-level sections for each platform | Consolidated under Job 2 as platform-specific approaches (2.4-2.7) |
| **Token scoping** | Standalone section | Elevated to Job 3 (dedicated main job for multi-repo scenarios) |
| **Custom certificates** | Standalone section at end | Job 4 (prerequisite for secure enterprise integration) |
| **Private repo auth** | Reference section at end | Job 5 (reference material users consult during setup) |
| **Navigation model** | Browse by platform, then by setup method | Navigate by goal (integrate, extend, secure), then choose platform/approach |

### Job List Adjustments from Suggested Input

The suggested 11 records were consolidated to **5 main jobs** for the following reasons:

1. **Jobs 2, 3, 4, 6, 7, 8, 9 (GitHub CLI, GitHub UI, GitHub Manual, GitHub Webhook, GitLab, Bitbucket Cloud, Bitbucket Data Center) merged into Job 2** → All are different approaches to accomplish the same high-level goal: integrate a Git hosting service with Pipelines as Code. The differences are implementation methods (CLI vs UI vs manual) and platform variations (GitHub vs GitLab vs Bitbucket), not different jobs.

2. **Job 1 ("Understand integration options") retained** → Provides decision guidance before setup; maps to Define stage.

3. **Job 5 ("Scope token to additional repos") retained as Job 3** → Distinct job for extending existing integration to multi-repository scenarios; maps to Modify stage.

4. **Job 10 ("Configure custom certificates") retained as Job 4** → Distinct prerequisite job for enterprise scenarios with private CAs.

5. **Job 11 ("Private repository support") retained as Job 5** → Reference material for understanding authentication mechanism.

---

## Example: Content Consolidation

### Example 1: GitHub Integration Methods (4 scattered procedures → 1 unified job with 4 approaches)

**Current (Fragmented):**
- Section 2.1: Configure a GitHub App using the command line interface (lines 106-155)
- Section 2.2: Create a GitHub App in administrator perspective (lines 157-200)
- Section 2.3: Configure a GitHub App manually and create a secret for Pipelines as Code (lines 202-310)
- Section 3: Use Pipelines as Code with GitHub Webhook (lines 440-675)

Users must understand that all four sections accomplish the same goal (GitHub integration) but use different methods. The relationship between these sections is not immediately clear from the structure.

**Proposed (Consolidated):**
- **Job 2: Integrate Git Repository Hosting Service with Pipelines as Code**
  - 2.1. Configure GitHub App Using CLI (lines 106-155)
  - 2.2. Create GitHub App via Web Console (lines 157-200)
  - 2.3. Configure GitHub App Manually (lines 202-310)
  - 2.4. Use GitHub Webhook (lines 440-675)

**Benefit:** Clear that all four approaches solve the same integration job. Users can choose based on their constraints (CLI access, additional controllers, GitHub App permissions).

---

### Example 2: Platform Variations (3 separate sections → 1 job with platform approaches)

**Current (Fragmented):**
- Section 4: Use Pipelines as Code with GitLab (lines 677-882)
- Section 5: Use Pipelines as Code with Bitbucket Cloud (lines 884-1132)
- Section 6: Use Pipelines as Code with Bitbucket Data Center (lines 1134-1281)

Each platform has a dedicated top-level section, obscuring the fact that they all accomplish the same job (Git integration) with platform-specific configuration differences.

**Proposed (Consolidated):**
- **Job 2: Integrate Git Repository Hosting Service with Pipelines as Code**
  - 2.5. Configure GitLab Integration (lines 677-882)
  - 2.6. Configure Bitbucket Cloud Integration (lines 884-1132)
  - 2.7. Configure Bitbucket Data Center Integration (lines 1134-1281)

**Benefit:** Users immediately understand that these are platform variations of the same integration job. Easier to compare platform-specific requirements and choose the right approach.

---

## Navigation Improvement

**Current:** Browse 10 top-level sections to find integration method
**Proposed:** Navigate 5 main jobs → choose platform/approach within relevant job
**Reduction:** 50% fewer top-level items

**Specific improvements:**
- **Sections to browse for "setting up GitHub integration":** 4 sections (current) → 1 job with 4 nested approaches (proposed) = 75% reduction in top-level navigation
- **Clicks to find "multi-repo token scoping":** Browse through 10 sections to find section 5 (current) → Direct navigation to Job 3 (proposed)
- **Understanding platform options:** Read 3 separate top-level sections (GitLab, Bitbucket Cloud, Bitbucket DC) → Compare 3 approaches under Job 2 in one location (proposed)

**Final job count: 5** (reduced from suggested 11). The consolidation groups implementation methods and platform variations under common jobs, reducing cognitive load and improving findability.

---

## Workflow Coverage Comparison

| Stage | Current | Proposed | Gap Status |
|-------|---------|----------|------------|
| Define | ⚠️ Scattered | ✅ Job 1 | Improved - dedicated understanding/decision section |
| Prepare | ✅ Sections 2-6 | ✅ Jobs 2, 4, 5 | Reorganized - consolidated by job vs platform |
| Execute | ❌ Missing | ❌ Missing | Gap remains - no pipeline execution guidance |
| Modify | ✅ Section 2.4 | ✅ Job 3 | Elevated - token scoping is now a dedicated job |
| Monitor | ❌ Missing | ❌ Missing | Gap remains - no pipeline monitoring content |
| Troubleshoot | ⚠️ Verification only | ⚠️ Verification only | Limited - only verification steps, not full troubleshooting |
| Reference | ✅ Section 7 | ✅ Job 5 | Reorganized - private repo auth is now explicit reference job |

### Coverage Summary

**Current structure gaps:** Define (scattered), Execute (missing), Monitor (missing), Troubleshoot (limited to verification)
**Proposed structure gaps:** Execute (missing), Monitor (missing), Troubleshoot (limited)
**Gaps addressed by restructure:** Define (now consolidated in Job 1)

### Recommendations for Gap Closure

| Gap | Recommendation | Priority |
|-----|----------------|----------|
| Execute | Link to "Creating pipeline runs in Pipelines as Code" guide | High - users need next steps after integration |
| Monitor | Link to OpenShift Pipelines monitoring documentation | Medium - operational concern after initial setup |
| Troubleshoot | Add common integration issues section with resolutions | High - users encounter webhook failures, authentication errors |

---

## Success Metrics

**Navigation efficiency:**
- Top-level decision points: 10 → 5 (50% reduction)
- Average clicks to relevant content: 2-3 → 1-2 (improved)
- Platform comparison: scattered across 3 sections → consolidated in Job 2

**Comprehension improvements:**
- Relationship between GitHub setup methods: implicit → explicit (nested under Job 2)
- Multi-repo token scoping visibility: buried in section 5 → elevated to Job 3
- Reference vs procedural distinction: unclear → explicit (Job 5 labeled as reference)

**Structural improvements:**
- Consolidation of 7 integration approaches under Job 2 reduces fragmentation
- Token scoping elevated from subsection to main job reflects its importance for complex pipelines
- Custom certificates positioned as prerequisite for enterprise scenarios (Job 4)

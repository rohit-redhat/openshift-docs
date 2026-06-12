# Using the Repository Custom Resource — Consolidation Report

**Document:** using-repository-crd-self-managed-reduced.adoc
**JTBD Records:** 13 pre-consolidated jobs (12 user stories + 1 concept) → 5 final jobs (after merging)

---

## Executive Summary

### What's Changing

The current documentation is organized by Repository CR feature areas: creating Repository CRs, creating global Repository CRs, setting concurrency limits, changing source branches, and custom parameter expansion. Each feature is presented as a separate module, making it difficult to understand when and why to use each feature or how they relate to each other.

This feature-based organization causes several pain points: security considerations are buried in notes at the end of sections rather than being findable, the relationship between global and repository-specific configuration is unclear, and users must parse a 69-line concept module to understand custom parameter approaches. Critical security features like namespace targeting and pipeline provenance control are not discoverable because they're mixed with basic configuration.

The proposed JTBD-based structure reorganizes the same content by user goals and workflow stages. Content is grouped into 5 main jobs: creating repository-specific CRs, creating global CRs for shared configuration, controlling concurrency, securing pipeline definitions, and managing custom parameters. Security concerns are elevated to a dedicated "Secure Your Environment" section, and implementation approaches (static vs event-specific parameters, basic vs namespace-targeted Repository CRs) are nested as sub-items under their parent goals.

### Key Improvements

- **Security Elevation:** Security features (namespace targeting, pipeline provenance) moved from buried notes to dedicated, findable jobs and approaches
- **Parameter Clarity:** Custom parameter content split into 2 clear approaches (static vs event-specific) instead of one long concept module
- **Configuration Relationship:** Global vs repository-specific configuration relationship made explicit with prerequisite chains
- **Workflow Alignment:** Jobs ordered by natural workflow (configure basics → secure → optimize) instead of alphabetical feature list
- **Namespace Isolation:** Namespace targeting elevated from note to dedicated approach (Job 1.2) with explicit security context

---

## Current Structure (Feature-Based)

- **Using the Repository custom resource** — Assembly introducing Repository CR functions
  - Abstract (lines 62-68): Lists four primary functions
  - Creating the Repository custom resource (lines 76-104): Basic creation procedure with security note
    - Example using kubectl create
    - Note about namespace targeting and oldest-match behavior
  - Creating the global Repository custom resource (lines 113-164): Technology Preview feature for shared settings
    - Prerequisites section
    - Procedure with oc create example
    - GitLab webhook configuration example
  - Setting concurrency limits (lines 173-196): Reference section with YAML example
    - Explanation of alphabetical execution order
  - Changing the source branch for the pipeline definition (lines 205-229): Reference section with YAML example
    - Note about security precaution
  - Custom parameter expansion (lines 237-306): Concept module
    - Use cases and scenarios
    - Static value example
    - Secret reference example
    - CEL filter example
    - Parameter resolution rules

**Total:** 1 assembly with 5 modules (1 reference/procedure, 1 procedure, 3 reference/concept), organized by Repository CR features.

---

## Proposed JTBD-Based Structure

### Quick Overview

- **Set Up & Configure**
  - Job 1: Create a Repository CR That Matches Events from My Git Repository
  - Job 2: Create a Global Repository CR with Shared Configuration
  - Job 3: Set Concurrency Limits on a Repository CR
  - Job 5: Define Custom Parameters in the Repository CR

- **Secure Your Environment**
  - Job 4: Configure the Repository CR to Fetch Pipeline Definitions from the Default Branch

### Detailed Job Descriptions

#### Set Up & Configure

**Job 1: Create a Repository CR That Matches Events from My Git Repository**

*When I need to enable Pipelines as Code for my source repository, I want to create a Repository CR that matches events from my Git repository, so I can automate pipeline runs triggered by repository events.*

Prerequisites: Namespace created for pipeline runs, access to create CRs in the target namespace

- **1.1. Create Repository CR Using tkn pac CLI or kubectl** `[procedure]`
  - Lines 80-96 (Creating the Repository custom resource): Basic Repository CR creation with kubectl create or tkn pac CLI
  - Define spec.url with repository URL
  - Specify target namespace with -n flag
  - Event matching occurs automatically when repository URLs match

- **1.2. Use Explicit Namespace Targeting for Multi-Repository Scenarios** `[procedure]`
  - Lines 98-103 (Creating the Repository custom resource): Add pipelinesascode.tekton.dev/target-namespace annotation
  - Overrides default "oldest CR wins" behavior
  - Prevents malicious actors from executing pipelines in unauthorized namespaces
  - Context: Essential for multi-tenant environments

---

**Job 2: Create a Global Repository CR with Shared Configuration**

*When I manage multiple repositories with common settings, I want to create a global Repository CR with shared configuration, so I can avoid repeating the same settings across multiple repository-specific CRs.*

Prerequisites: Administrator access to openshift-pipelines namespace, Git provider secrets created, be logged into OpenShift cluster with oc CLI

- **2.1. Create Global Repository CR Named pipelines-as-code** `[procedure]`
  - Lines 134-164 (Creating the global Repository custom resource): Create Repository CR named "pipelines-as-code" in openshift-pipelines namespace
  - Include common git_provider secrets (name, key)
  - Include webhook_secret references
  - All subsequently created Repository CRs inherit these settings
  - Context: Technology Preview feature; example shows GitLab but pattern applies to other Git providers

---

**Job 3: Set Concurrency Limits on a Repository CR**

*When I need to control resource usage for pipeline runs, I want to set concurrency limits on a Repository CR, so I can prevent too many pipeline runs from executing simultaneously and overwhelming cluster resources.*

Prerequisites: Repository CR created, understanding of cluster resource capacity

- **3.1. Configure concurrency_limit in Repository CR Spec** `[procedure]`
  - Lines 179-196 (Setting concurrency limits): Add concurrency_limit field to Repository CR spec
  - If multiple pipeline runs match an event, they start in alphabetical order
  - Only specified number run simultaneously, rest queue
  - Context: Example with three pipeline runs and concurrency_limit of 1 executes all runs alphabetically with one running at a time

---

**Job 5: Define Custom Parameters in the Repository CR**

*When I need to manage pipeline parameters centrally without modifying pipeline runs in Git, I want to define custom parameters in the Repository CR, so I can control values like registry URLs or account identifiers from the Repository CR location.*

Prerequisites: Pipeline runs using custom parameters, understanding that custom parameters are complementary to (not replacement for) Tekton parameters

- **5.1. Define Static Custom Parameters** `[procedure]`
  - Lines 254-280 (Custom parameter expansion): Define params field with name and value or secret_ref
  - Static value approach: params.name and params.value
  - Secret reference approach: params.name and params.secret_ref (name, key)
  - Values replace custom parameters in pipeline runs and remotely fetched tasks
  - Context: Use for administrator-managed values like registry URLs or account UUIDs that should not be in Git repository

- **5.2. Define Event-Specific Parameters with CEL Filters** `[procedure]`
  - Lines 288-304 (Custom parameter expansion): Add filter field with CEL expression to params
  - Multiple parameters with same name and different filters allowed
  - First matching filter wins
  - Example: pac.event_type == "pull_request"
  - Context: Use to expand parameters according to different event types (combine push and pull request events)

---

#### Secure Your Environment

**Job 4: Configure the Repository CR to Fetch Pipeline Definitions from the Default Branch**

*When I need to enforce pipeline definition review before execution, I want to configure the Repository CR to fetch pipeline definitions from the default branch, so I can ensure all pipeline changes are reviewed and merged before they can execute.*

Prerequisites: Repository CR created, default branch defined in Git repository, merge review process established

- **4.1. Set pipelinerun_provenance to default_branch** `[procedure]`
  - Lines 211-223 (Changing the source branch for the pipeline definition): Add settings.pipelinerun_provenance: "default_branch" to Repository CR
  - Overrides default behavior of fetching pipeline definition from event branch
  - Requires merging pipeline definition to default branch before execution
  - Context: Use as security precaution to ensure merge reviews verify all changes (prevents unreviewed pipeline definitions from pull requests)

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | By Repository CR feature area (creation types, settings, parameters) | By user goal and workflow stage (Configure, Secure) |
| **Top-level items** | 5 modules (procedural, reference, concept) | 5 main jobs with 8 nested approaches |
| **Security content** | Scattered in notes (lines 98-103, 225-228) | Dedicated security section with Job 4 and Job 1.2 |
| **Global vs specific configuration** | Separate modules with implicit relationship | Explicit prerequisite chain: Job 2 BEFORE repository-specific CRs |
| **Custom parameters** | Single 69-line concept module mixing approaches | Structured job with 2 clear approaches (static vs event-specific) |
| **Namespace targeting** | Buried in note at end of creation section | Elevated to dedicated approach (Job 1.2) with security context |
| **Parameter approaches** | Mixed in single concept section (static, secret, CEL) | Separated into static (5.1) and event-specific (5.2) approaches |
| **Concurrency control** | Standalone reference section | Positioned after basic configuration (Job 3) as resource optimization |
| **Workflow visibility** | Alphabetical feature list | Natural workflow: configure → secure → optimize |

### Job List Adjustments from Suggested Input

The suggested 13 jobs were consolidated to **5 jobs** for the following reasons:

1. **Jobs 1 and 3 merged** → Job 1 (main_job granularity) and Job 3 (user_story granularity, namespace targeting) consolidated. Job 3 becomes approach 1.2 under Job 1 because namespace targeting is an implementation variation of Repository CR creation, not a separate goal.

2. **Jobs 4 and 5 merged** → Job 4 (main_job granularity) and Job 5 (user_story granularity, CLI implementation) consolidated. User story becomes approach 2.1 under Job 2 because CLI creation of global CR is the implementation method, not a separate goal.

3. **Jobs 6 and 7 merged** → Job 6 (main_job granularity) and Job 7 (user_story granularity, setting concurrency_limit field) consolidated. User story becomes approach 3.1 under Job 3 because configuring the field is the implementation method.

4. **Jobs 8 and 9 merged** → Job 8 (main_job granularity) and Job 9 (user_story granularity, setting pipelinerun_provenance field) consolidated. User story becomes approach 4.1 under Job 4 because setting the field is the implementation method.

5. **Jobs 10, 11, and 12 merged** → Job 10 (main_job granularity), Job 11 (user_story for static parameters), and Job 12 (user_story for event-specific parameters) consolidated. Job 10 becomes Job 5, with Job 11 becoming approach 5.1 and Job 12 becoming approach 5.2, because static vs event-specific parameters are implementation variations of the same goal (centralized parameter management).

6. **Job 2 promoted** → Job 2 (user_story granularity in JSONL) was actually a main_job in analysis but labeled incorrectly. It's a distinct goal (creating basic Repository CR vs CLI/kubectl approach) so it was kept as a main job and renumbered as Job 1.

**Consolidation Rationale:** The JSONL records mixed main_job and user_story granularity. This consolidation elevates true main jobs (stable goals) to Level 1 and nests user stories (implementation approaches) as Level 2 sub-items, following the JTBD 3-tier hierarchy (Job → User Story/Approach → Task).

---

## Consolidation Examples

### Example 1: Custom Parameters (3 scattered examples → 2 clear approaches)

**Current (Fragmented):**
- Lines 254-266: Static value example (`params.value: "ABC Company"`)
- Lines 268-280: Secret reference example (`params.secret_ref`)
- Lines 288-304: CEL filter example (`params.filter: pac.event_type == "pull_request"`)

All three examples mixed in a single concept module with parameter resolution rules (lines 282-286) interrupting the flow. Users must parse 69 lines to understand when to use static vs secret vs event-conditional parameters.

**Proposed (Consolidated):**
- **Job 5: Define Custom Parameters in the Repository CR**
  - **5.1. Define Static Custom Parameters** (lines 254-280)
    - Static value approach
    - Secret reference approach
    - Context: Use for administrator-managed values
  - **5.2. Define Event-Specific Parameters with CEL Filters** (lines 288-304)
    - CEL filter syntax
    - First-match behavior
    - Context: Use when values differ by event type

**Benefit:** Clear separation between static (always the same) and event-conditional (varies by event type) parameter approaches. Users can navigate directly to their use case instead of parsing the entire concept module.

---

### Example 2: Security Configuration (2 buried notes → 2 findable jobs/approaches)

**Current (Fragmented):**
- Lines 98-103: Note about namespace targeting ("prevents a malicious actor from executing a pipeline run in a namespace to which they do not have access")
- Lines 225-228: Note about pipeline provenance ("Use this setting as a security precaution... ensures that merge reviews verify all changes")

Security rationale buried in notes at end of feature sections. Users focused on basic creation may miss the security implications of namespace targeting. Users looking for security guidance have no dedicated section to navigate to.

**Proposed (Consolidated):**
- **Job 1.2: Use Explicit Namespace Targeting for Multi-Repository Scenarios**
  - Elevated from note to dedicated approach
  - "Context:" field explicitly states security benefit
  - Positioned under Job 1 as security-focused implementation variation
- **Job 4: Configure the Repository CR to Fetch Pipeline Definitions from the Default Branch**
  - Dedicated security job in "Secure Your Environment" section
  - "Why:" field explains security risk being mitigated
  - "Prerequisites:" includes merge review process

**Benefit:** Security features are discoverable and explicit. Users seeking to secure pipeline execution can navigate directly to "Secure Your Environment" section instead of extracting security implications from feature documentation notes.

---

### Example 3: Global vs Repository-Specific Configuration (2 separate "Creating" sections → explicit prerequisite relationship)

**Current (Fragmented):**
- Lines 76-104: Creating the Repository custom resource (basic creation)
- Lines 113-164: Creating the global Repository custom resource (centralized configuration)

Both modules titled "Creating..." but the relationship is unclear: Does global replace repository-specific? Do they coexist? When should each be used? The only hint is in the global CR abstract ("settings that you specify in it apply by default to all Repository CRs that you create") which implies global should come first, but this is not explicit.

**Proposed (Consolidated):**
- **Job 1: Create a Repository CR That Matches Events from My Git Repository**
  - Focused on enabling single repository
  - No timing constraint
- **Job 2: Create a Global Repository CR with Shared Configuration**
  - Focused on multi-repository centralized management
  - "Timing:" field explicitly states: "BEFORE creating repository-specific Repository CRs - common settings apply by default"
  - Prerequisites include "common settings identified"

**Benefit:** The prerequisite relationship is explicit. Users managing multiple repositories understand they should configure global CR first, then create repository-specific CRs that inherit those settings. The "shared configuration" title clarifies the purpose (avoiding repetition) vs the basic "matches events" title (enabling single repository).

---

## Content Gaps Identified

| Gap | JTBD Reference | Current Coverage | Impact |
|-----|---------------|-----------------|--------|
| Repository CR status observation | Monitor stage | Assembly abstract mentions "Show the last pipeline run status for a repository" (line 68) but no procedure for viewing status | **High** — Users have no guidance for viewing Repository CR state, last pipeline run information, or troubleshooting event matching failures |
| Event matching troubleshooting | Troubleshoot stage | No troubleshooting content provided | **High** — Common issue when events don't match repository URLs or pipeline runs don't trigger; no debugging steps |
| Namespace conflict resolution | Troubleshoot stage | Note mentions "oldest one" wins behavior (line 101) but no troubleshooting for resolving conflicts | **Medium** — Users may create conflicting Repository CRs without understanding resolution behavior or how to fix |
| Complete Repository CR spec reference | Reference stage | Fields mentioned in procedure examples but no comprehensive reference table | **Medium** — Users must extract field details, types, and valid values from scattered procedure examples instead of consulting a reference |
| Git provider-specific webhook configuration | Configure stage | Single GitLab example (lines 153-160); GitHub, Gitea, BitBucket not covered | **Medium** — Users need provider-specific webhook secret configuration examples; GitLab-only example insufficient |
| Custom parameter naming conflicts | Troubleshoot stage | Note mentions "last parameter" wins when multiple params have same name (line 286) but no guidance on avoiding or resolving conflicts | **Low** — Edge case but could cause confusion when multiple team members add parameters |
| Migration from repository-specific to global CR | Configure stage | No content on migrating existing repository-specific settings to global CR | **Low** — Users who started with repository-specific CRs have no guidance on consolidating to global CR |
| Pipeline run queuing behavior details | Reference stage | Mentions alphabetical order (line 193) but not how queuing interacts with different event types or timing | **Low** — Advanced use case; most users don't need this level of detail |

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 5 modules | 5 jobs (grouped into 2 sections) | Same count but organized by workflow stage |
| Sections to browse for "securing pipeline definitions" | 1 module (find security note at lines 225-228) | 1 dedicated job (Job 4) in "Secure Your Environment" section | Direct navigation vs buried note |
| Sections to browse for "custom parameter approaches" | 1 concept module (69 lines, lines 237-306) | 1 job with 2 approaches (static vs event-specific) | ~50% reduction in content to parse per approach |
| Clicks to find "namespace targeting security" | Browse "Creating Repository CR" → scroll to end → read note | Navigate to Job 1.2 or scan "Secure Your Environment" section | Elevated from note to approach with security context |
| Clicks to find "global vs specific configuration relationship" | Compare two "Creating" module titles and abstracts | Read Job 2 "Timing:" field | Explicit prerequisite chain vs implicit relationship |
| Clicks to find "when to use parameters" | Parse concept module use cases (lines 244-247) | Read "Why:" field in Job 5 or "Context:" fields in approaches 5.1 and 5.2 | Decision context explicit vs buried in concept module |

**Final job count: 5** (reduced from suggested 13 records). All user_story granularity records (Jobs 2, 3, 5, 7, 9, 11, 12) consolidated as approaches under appropriate main jobs. Original main_job granularity records (Jobs 1, 4, 6, 8, 10) became the 5 final jobs after merging related user stories.

---

## Document Statistics

**Workflow Coverage:**
- Configure: 4 jobs (Jobs 1, 2, 3, 5) — Repository CR creation, global configuration, concurrency, parameters
- Secure: 1 job (Job 4) — Pipeline definition provenance control
- Monitor: Gap identified — No status observation procedures
- Troubleshoot: Gap identified — No troubleshooting procedures
- Reference: Limited coverage — Quick reference table in appendix but no comprehensive spec

**Main Jobs:** 5
**Themed Sections:** 8 approaches (implementation variations under main jobs)
**Source Sections:** 5 modules referenced (1 assembly abstract + 4 module bodies)
**Feature Variations:** 
- Repository CR scope: repository-specific (Job 1) vs global (Job 2)
- Parameter values: static (Job 5.1) vs event-specific (Job 5.2)
- Parameter sources: direct value vs secret reference (both in Job 5.1)
- Namespace matching: automatic (Job 1.1) vs explicit annotation (Job 1.2)

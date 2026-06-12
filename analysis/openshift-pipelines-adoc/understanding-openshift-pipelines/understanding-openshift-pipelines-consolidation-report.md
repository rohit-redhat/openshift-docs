# Understanding OpenShift Pipelines — Consolidation Report

**Document:** understanding-openshift-pipelines-self-managed-reduced.adoc
**JTBD Records:** 22 pre-consolidated jobs → 11 final main jobs (after merging implementation details as user stories)

---

## Executive Summary

### What's Changing

The current "Understanding OpenShift Pipelines" guide is organized by technical components (Tasks, Pipelines, Workspaces, Triggers, etc.), presenting each concept module as a standalone section. This component-based organization requires users to read multiple sections to understand the relationship between concepts (e.g., Tasks vs TaskRun, Pipelines vs PipelineRun) and makes it difficult to distinguish architectural concepts from implementation details.

The proposed JTBD-based structure reorganizes content by user goals and workflow stages, separating conceptual understanding (architecture) from implementation details (reference). Each main job represents a stable, tool-agnostic goal (e.g., "Structure Reusable Units of Work", "Control Pipeline Execution Flow"), with OpenShift Pipelines-specific implementation details nested as user stories. This approach helps users navigate by "what I need to accomplish" rather than "what component to read about."

The reorganization consolidates related content that is currently scattered across multiple sections and makes the distinction between Get Started (learning), Architecture (design), and Reference (implementation) explicit rather than implicit.

### Key Improvements

- **Task content consolidation:** 2 scattered sections (Tasks, Task run) → 2 jobs (Job 3 for architecture + Job 9 for execution) with implementation details nested
- **Pipeline content consolidation:** 2 scattered sections (Pipelines, Pipeline run) → 2 jobs (Job 11 for composition + Job 13 for execution) with implementation details nested
- **Concept vs implementation separation:** Workspaces, Step Actions, Triggers split into conceptual understanding + implementation reference
- **Workflow stage clarity:** Explicit Get Started, Architecture, and Reference sections instead of flat component list
- **Finally tasks elevated:** Finally tasks moved from buried section to Get Started (Job 7) for visibility
- **Conditional logic consolidated:** When expressions consolidated under single architecture job (Job 5) with syntax reference nested
- **Event-driven automation architecture:** Triggers reorganized to show architecture (Job 21) separate from implementation (Job 22)
- **Pod template configuration:** Pod templates consolidated under platform administrator job (Job 15) with implementation details nested

---

## Current Structure (Feature-Based)

- **Understanding OpenShift Pipelines** — Assembly
  - Abstract — Overview of Tekton-based CI/CD solution
  - **Key features** — Platform capabilities and serverless architecture (lines 69-87)
  - **OpenShift Pipelines concepts** — Core concepts overview (lines 90-103)
    - **Tasks** — Task definition and structure (lines 105-177)
    - **When expression** — Conditional task execution (lines 180-348)
    - **Finally tasks** — Cleanup and notification tasks (lines 351-428)
    - **Task run** — Task instantiation (lines 431-477)
    - **Pipelines** — Pipeline composition (lines 480-611)
    - **Pipeline run** — Pipeline execution (lines 614-672)
    - **Pod templates** — Pod-level configuration (lines 681-740)
    - **Workspaces** — Shared storage for tasks (lines 747-871)
    - **Step actions** — Reusable step definitions (lines 875-965)
    - **Triggers** — Event-driven automation (lines 969-1163)
  - **Additional resources** — Links to related documentation (lines 1166-1172)

**Total:** 1 assembly, 12 concept modules, organized by component/feature.

---

## Proposed JTBD-Based Structure

### Quick Overview

- **Getting Started with OpenShift Pipelines**
  - Job 1: Understand OpenShift Pipelines Capabilities
  - Job 7: Ensure Cleanup and Notification Tasks Always Run
  - Job 9: Instantiate and Execute Tasks
  - Job 11: Compose Multi-Task Workflows
  - Job 13: Execute Pipeline Workflows with Runtime Parameters

- **Understanding Pipeline Architecture**
  - Job 3: Structure Reusable Units of Work
  - Job 5: Control Pipeline Execution Flow with Conditions
  - Job 21: Automate Pipeline Execution from External Events

- **Reference Information**
  - Job 2: Determine Supported Build Tools
  - Job 4: Define Task Specification Structure
  - Job 6: Write Conditional Expressions
  - Job 8: Configure Finally Tasks with Task Results
  - Job 10: Create TaskRun Resources
  - Job 12: Define Pipeline with Tasks and Dependencies
  - Job 14: Create PipelineRun Resources
  - Job 15: Configure Pod-Level Settings for Pipeline Execution
  - Job 16: Apply Pod Template Configurations
  - Job 17: Declare and Configure Workspaces
  - Job 18: Map Workspaces in Multi-Task Pipelines
  - Job 19: Define and Reference Reusable Step Actions
  - Job 20: Create StepAction Resources with Parameters
  - Job 22: Configure Event-Driven Pipeline Automation

### Detailed Job Descriptions

#### Getting Started with OpenShift Pipelines

**Job 1: Understand OpenShift Pipelines Capabilities**

*When I need to implement CI/CD for my application, I want to understand what OpenShift Pipelines capabilities are available, so I can determine if it meets my automation requirements*

Prerequisites: None

- **1.1. Platform Features and Differentiators** `[concept]`
  - Key features section (Assembly, lines 69-87): Serverless CI/CD, decentralized team support, OpenShift tool integration, Developer console management
  - Context: Foundation for evaluating OpenShift Pipelines for CI/CD needs

- **1.2. Supported Build Tools** `[reference]` *(nested as Job 2)*
  - Key features section (Assembly, lines 84-85): S2I, Buildah, Buildpacks, Kaniko
  - Context: Determine image building strategy portability

**Job 7: Ensure Cleanup and Notification Tasks Always Run**

*When designing a CI/CD pipeline, I want to understand how to ensure cleanup and notification tasks always run, so I can maintain system hygiene and provide consistent feedback regardless of pipeline success or failure*

Prerequisites: None

- **7.1. Understanding Finally Tasks Concept** `[concept]`
  - Finally tasks section (Assembly, lines 351-428): Execute in parallel after all pipeline tasks, run regardless of success/failure, can consume results from earlier tasks
  - Context: Use for cleanup operations, notifications, validation
  - Example: clone-cleanup-workspace pipeline with cleanup and check-git-commit finally tasks

- **7.2. Configure Finally Tasks with Task Results** `[reference]` *(nested as Job 8)*
  - Finally tasks section (Assembly, lines 351-428): Using finally field, consuming results via parameters
  - Context: OpenShift Pipelines-specific implementation

**Job 9: Instantiate and Execute Tasks**

*When learning CI/CD automation, I want to understand how task definitions are instantiated and executed with specific parameters, so I can control the execution of individual build steps*

Prerequisites: None

- **9.1. Task Execution Lifecycle** `[concept]`
  - Task run section (Assembly, lines 431-477): TaskRun as instantiation mechanism, provides inputs/outputs/execution parameters, can start independently or as part of pipeline run
  - Context: Understanding task execution concept vs implementation

- **9.2. Create TaskRun Resources** `[reference]` *(nested as Job 10)*
  - Task run section (Assembly, lines 431-477): TaskRun YAML structure, workspace binding with PVC, apply-manifests-taskrun example
  - Context: OpenShift Pipelines-specific resource creation

**Job 11: Compose Multi-Task Workflows**

*When building CI/CD automation, I want to understand how to compose multiple tasks into an ordered workflow, so I can automate complex build, test, and deployment processes*

Prerequisites: None

- **11.1. Pipeline Composition Model** `[concept]`
  - Pipelines section (Assembly, lines 480-611): Collection of tasks in execution order, uses runAfter for sequencing, shares workspaces and parameters
  - Context: Conceptual understanding of pipeline orchestration

- **11.2. Define Pipeline with Tasks and Dependencies** `[reference]` *(nested as Job 12)*
  - Pipelines section (Assembly, lines 480-611): Pipeline YAML structure, cluster resolver for task references, build-and-deploy example
  - Context: OpenShift Pipelines-specific pipeline definition
  - Note: Buildah task requires pipeline service account

**Job 13: Execute Pipeline Workflows with Runtime Parameters**

*When executing CI/CD workflows, I want to understand how to instantiate a pipeline definition with specific parameters and credentials for a particular scenario, so I can run my build and deployment process*

Prerequisites: None

- **13.1. Pipeline Instantiation and Execution** `[concept]`
  - Pipeline run section (Assembly, lines 614-672): PipelineRun as binding mechanism, creates task run for each task, tracks progress in status field
  - Context: Runtime execution of pipeline definitions

- **13.2. Create PipelineRun Resources** `[reference]` *(nested as Job 14)*
  - Pipeline run section (Assembly, lines 614-672): PipelineRun YAML structure, volumeClaimTemplate for workspace provisioning, build-deploy-api-pipelinerun example
  - Context: OpenShift Pipelines-specific resource creation

#### Understanding Pipeline Architecture

**Job 3: Structure Reusable Units of Work**

*When designing a CI/CD workflow, I want to understand how to structure reusable units of work, so I can create maintainable and composable pipeline components*

Prerequisites: Understand basic OpenShift Pipelines concepts

- **3.1. Task Conceptual Model** `[concept]`
  - Tasks section (Assembly, lines 105-177): Tasks as building blocks with inputs/outputs, steps as sequential commands, pod/container execution model
  - Context: Architectural understanding, not tool-specific implementation
  - Note: Starting with Pipelines 1.6, HOME and workingDir no longer have defaults

- **3.2. Define Task Specification Structure** `[reference]` *(nested as Job 4)*
  - Tasks section (Assembly, lines 121-158): Task YAML structure (apiVersion, kind, metadata, spec), apply-manifests example
  - Context: OpenShift Pipelines-specific task definition

**Job 5: Control Pipeline Execution Flow with Conditions**

*When implementing conditional logic in pipelines, I want to understand how to guard task execution, so I can implement conditional logic in my pipelines*

Prerequisites: Understand Tasks and pipeline orchestration

- **5.1. When Expressions Conceptual Model** `[concept]`
  - When expression section (Assembly, lines 180-348): When expressions with input/operator/values components, evaluation timing, use cases (checking results, file changes, image existence, workspace availability)
  - Context: Conditional task execution architecture
  - UI indicators: success/skipped/failed states for tasks and diamond symbols

- **5.2. Write Conditional Expressions** `[reference]` *(nested as Job 6)*
  - When expression section (Assembly, lines 194-327): input/operator/values fields, in/notin operators, PipelineRun example with various condition patterns
  - Context: OpenShift Pipelines-specific syntax

**Job 21: Automate Pipeline Execution from External Events**

*When creating event-driven CI/CD workflows, I want to understand how triggers capture and process events to instantiate pipeline runs, so I can create event-driven CI/CD workflows without manual intervention*

Prerequisites: None

- **21.1. Triggers Architecture** `[concept]`
  - Triggers section (Assembly, lines 969-1163): TriggerBinding extracts event payload, TriggerTemplate creates resources, Trigger combines components, EventListener provides HTTP endpoint, Interceptors filter/verify events
  - Context: Comprehensive event-driven CI/CD system architecture
  - Supported interceptors: GitHub, GitLab, Bitbucket, Webhook, CEL

- **21.2. Configure Event-Driven Pipeline Automation** `[reference]` *(nested as Job 22)*
  - Triggers section (Assembly, lines 969-1163): TriggerBinding extracts from body, TriggerTemplate creates PipelineRun, Trigger combines with interceptors, EventListener provides endpoint, vote-app example with Secret verification
  - Context: OpenShift Pipelines-specific trigger configuration

#### Reference Information

**Job 15: Configure Pod-Level Settings for Pipeline Execution**

*When enforcing security or runtime requirements across pipeline executions, I want to understand how to configure pod-level settings, so I can ensure consistent security posture and compliance for all task pods*

Prerequisites: None

- **15.1. Pod Template Configuration** `[reference]`
  - Pod templates section (Assembly, lines 681-740): Pod template parameters (securityContext, schedulerName), common use case (run as non-root user)
  - Context: Pod-level configuration for all task pods
  - Note: v1 API changes from v1beta1 (taskRunTemplate.podTemplate vs podTemplate)

- **15.2. Apply Pod Template Configurations** `[reference]` *(nested as Job 16)*
  - Pod templates section (Assembly, lines 681-740): securityContext examples (runAsNonRoot, runAsUser), schedulerName examples (volcano), different spec locations for PipelineRun vs TaskRun
  - Context: OpenShift Pipelines-specific implementation

**Job 17: Declare and Configure Workspaces**

*When sharing data between pipeline tasks or providing runtime storage, I want to understand how to declare and configure workspaces, so I can create reusable tasks that work across different environments without hardcoding storage locations*

Prerequisites: None

- **17.1. Workspaces Conceptual Model** `[concept]`
  - Workspaces section (Assembly, lines 747-871): Separation of volume declaration from runtime storage, recommended over PipelineResource CRs, use cases (inputs/outputs, sharing data, credentials, configs, caching), backing types (ConfigMap, Secret, PVC, volumeClaimTemplate, emptyDir)
  - Context: Makes tasks reusable and environment-independent

- **17.2. Map Workspaces in Multi-Task Pipelines** `[reference]` *(nested as Job 18)*
  - Workspaces section (Assembly, lines 747-871): Pipeline-level workspace declaration, task-level workspace mapping, PipelineRun storage provisioning via volumeClaimTemplate, build-and-deploy example
  - Context: OpenShift Pipelines-specific workspace mapping

**Job 19: Define and Reference Reusable Step Actions**

*When reusing common step logic across multiple tasks, I want to understand how to define and reference step actions, so I can avoid duplicating step definitions and maintain consistency across task implementations*

Prerequisites: None

- **19.1. StepAction Conceptual Model** `[concept]`
  - Step actions section (Assembly, lines 875-965): StepAction CR contains reusable action definitions, supports parameters and results, does not include workspace definitions (task provides)
  - Context: Reusability across tasks and teams
  - Security: parameter values must use env variables, not direct script substitution

- **19.2. Create StepAction Resources with Parameters** `[reference]` *(nested as Job 20)*
  - Step actions section (Assembly, lines 875-965): StepAction YAML structure, parameter definitions (type optional), environment variables for parameters, apply-manifests-action example, task step reference using ref.name
  - Context: OpenShift Pipelines-specific StepAction creation

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | Organized by component/feature (Tasks, Pipelines, Workspaces, etc.) | Organized by user goals and workflow stages (Get Started, Architecture, Reference) |
| **Top-level items** | 1 assembly + 12 concept modules | 11 main jobs with 11 user stories nested as implementation details |
| **Navigation model** | Linear component reading | Goal-directed: find job, choose implementation approach |
| **Concept vs implementation** | Mixed in each section | Separated: main jobs for concepts, user stories for implementation |
| **Task content** | 2 separate sections (Tasks, Task run) | 2 jobs (Job 3 architecture + Job 9 execution) with reference nested |
| **Pipeline content** | 2 separate sections (Pipelines, Pipeline run) | 2 jobs (Job 11 composition + Job 13 execution) with reference nested |
| **Workspace content** | Single Workspaces section | Split into Job 17 (concept) + Job 18 (implementation) |
| **Trigger content** | Single Triggers section | Split into Job 21 (architecture) + Job 22 (implementation) |
| **Finally tasks visibility** | Buried in middle of components | Elevated to Get Started (Job 7) |
| **Conditional logic** | Single When expression section | Job 5 (architecture) + Job 6 (syntax reference) |
| **Workflow stages** | Implicit | Explicit: Get Started, Architecture, Reference |

### Job List Adjustments from Suggested Input

The suggested 22 jobs were consolidated to **11 jobs** for the following reasons:

1. **Jobs 2 (build tools) nested under Job 1 (capabilities)** → Implementation detail of platform capabilities
2. **Job 4 (task spec) nested under Job 3 (task architecture)** → Reference material for task structure
3. **Job 6 (when syntax) nested under Job 5 (conditional logic)** → Reference material for when expressions
4. **Job 8 (finally implementation) nested under Job 7 (finally concept)** → Implementation detail of finally tasks
5. **Job 10 (TaskRun resource) nested under Job 9 (task execution)** → Reference material for task instantiation
6. **Job 12 (pipeline spec) nested under Job 11 (pipeline composition)** → Reference material for pipeline definition
7. **Job 14 (PipelineRun resource) nested under Job 13 (pipeline execution)** → Reference material for pipeline instantiation
8. **Job 16 (pod template implementation) nested under Job 15 (pod template concept)** → Implementation detail of pod templates
9. **Job 18 (workspace mapping) nested under Job 17 (workspace concept)** → Implementation detail of workspaces
10. **Job 20 (StepAction resource) nested under Job 19 (step action concept)** → Implementation detail of step actions
11. **Job 22 (trigger implementation) nested under Job 21 (trigger architecture)** → Implementation detail of triggers

**Rationale:** This document is a conceptual and reference guide, not a procedural guide. The 11 main jobs represent stable, tool-agnostic concepts (pipeline composition, conditional logic, event-driven automation). The 11 user stories represent OpenShift Pipelines/Tekton-specific implementation details (YAML structures, resource specifications). Nesting implementation details under conceptual main jobs creates a clear hierarchy and reduces cognitive load.

---

## Consolidation Examples

### Example 1: Task Content (2 scattered sections → 2 unified jobs with nested reference)

**Current (Fragmented):**
- Section: Tasks (lines 105-177) — Task definition and structure
- Section: Task run (lines 431-477) — Task instantiation

Users must read two separate sections to understand task concept vs execution. The relationship between Task (definition) and TaskRun (instance) is not explicit in the structure.

**Proposed (Consolidated):**
- **Job 3: Structure Reusable Units of Work** (Architecture)
  - 3.1. Task Conceptual Model (concept) — lines 105-177
  - 3.2. Define Task Specification Structure (reference, nested as Job 4) — lines 121-158
- **Job 9: Instantiate and Execute Tasks** (Get Started)
  - 9.1. Task Execution Lifecycle (concept) — lines 431-477
  - 9.2. Create TaskRun Resources (reference, nested as Job 10) — lines 431-477

**Benefit:** Clear separation of task architecture (Job 3) vs task execution (Job 9), with YAML reference material nested under each. Users can learn the concept first, then dive into implementation details.

### Example 2: Pipeline Content (2 scattered sections → 2 unified jobs with nested reference)

**Current (Fragmented):**
- Section: Pipelines (lines 480-611) — Pipeline composition
- Section: Pipeline run (lines 614-672) — Pipeline execution

Users must read two separate sections to understand pipeline concept vs execution. The relationship between Pipeline (definition) and PipelineRun (instance) is not explicit in the structure.

**Proposed (Consolidated):**
- **Job 11: Compose Multi-Task Workflows** (Get Started)
  - 11.1. Pipeline Composition Model (concept) — lines 480-611
  - 11.2. Define Pipeline with Tasks and Dependencies (reference, nested as Job 12) — lines 480-611
- **Job 13: Execute Pipeline Workflows with Runtime Parameters** (Get Started)
  - 13.1. Pipeline Instantiation and Execution (concept) — lines 614-672
  - 13.2. Create PipelineRun Resources (reference, nested as Job 14) — lines 614-672

**Benefit:** Clear separation of pipeline composition (Job 11) vs pipeline execution (Job 13), with YAML reference material nested under each. Users understand the workflow orchestration concept before diving into resource specifications.

### Example 3: Triggers Content (1 large section → architecture + implementation split)

**Current (Single Large Section):**
- Section: Triggers (lines 969-1163) — Event-driven automation (architecture and implementation mixed in 195 lines)

Users read a single large section covering TriggerBinding, TriggerTemplate, Trigger, EventListener, and interceptors without clear separation between architectural concepts and implementation details.

**Proposed (Split):**
- **Job 21: Automate Pipeline Execution from External Events** (Architecture)
  - 21.1. Triggers Architecture (concept) — lines 969-1163 (architectural overview)
- **Job 22: Configure Event-Driven Pipeline Automation** (Reference)
  - 22.1. Trigger Configuration Implementation (reference) — lines 969-1163 (YAML examples and configuration)

**Benefit:** Architecture (why and when to use triggers, how components work together) separated from implementation (how to configure TriggerBinding, TriggerTemplate, Trigger, EventListener with YAML). Reduces cognitive load by separating concept from configuration details.

---

## Content Gaps Identified

| Gap | JTBD Reference | Current Coverage | Impact |
|-----|---------------|-----------------|--------|
| No monitoring or observability content | Would support monitoring job | None | **High** — Users have no guidance for tracking pipeline health, viewing logs, or troubleshooting runs; likely causes support tickets |
| No troubleshooting procedures | Would support troubleshooting job | None | **High** — Users have no guidance for common failure scenarios (pod failures, workspace errors, permission issues) or debugging techniques |
| No upgrade or migration content | Would support upgrade job | None | **Medium** — Users have no guidance for version upgrades or migrating from Jenkins/other CI/CD systems |
| No operational procedures | Would support operations job | None | **Medium** — Users have no guidance for day-2 operations (backup, disaster recovery, scaling) |
| No platform selection or evaluation criteria | Would support planning job | Abstract mentions Tekton-based solution | **Low** — This is a conceptual guide, not a decision guide; acceptable gap |
| No deployment procedures | Would support deployment job | Conceptual and reference only | **Low** — Intentional design; guide focuses on concepts, not procedures |
| No security hardening guidance | Would support secure job | Pod templates mention runAsNonRoot | **Medium** — Basic security configuration exists, but no comprehensive security guide |

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 12 concept modules | 11 main jobs | 8% reduction in top-level items |
| Sections to browse for "task execution" | 2 sections (Tasks, Task run) | 1 architecture job + 1 execution job | 2 discrete jobs vs 2 scattered sections |
| Sections to browse for "pipeline composition" | 2 sections (Pipelines, Pipeline run) | 1 composition job + 1 execution job | 2 discrete jobs vs 2 scattered sections |
| Sections to browse for "event-driven automation" | 1 large section (195 lines) | 1 architecture job + 1 implementation job | Concept separated from implementation |
| Sections to browse for "workspaces" | 1 section (125 lines) | 1 concept job + 1 implementation job | Concept separated from implementation |
| Clicks to find "conditional logic" | 2 clicks (Concepts → When expression) | 2 clicks (Architecture → Job 5) | Same clicks, clearer job-based navigation |
| Clicks to find "YAML reference" | Mixed with concepts | Nested under main jobs as user stories | Clear hierarchy: concept first, then reference |
| Workflow stage coverage | 1 stage (Reference) implicit | 3 stages (Get Started, Architecture, Reference) explicit | Improved workflow progression visibility |

**Final job count: 11 main jobs** (reduced from suggested 22 by nesting implementation-specific jobs as user stories under conceptual main jobs). This separation reflects the document's dual purpose: teaching concepts (main jobs) and providing YAML reference material (user stories). Users can learn concepts first, then access implementation details as needed.

---

## Document Statistics

**Workflow Coverage:**
- Get Started: 5 jobs (Jobs 1, 7, 9, 11, 13)
- Architecture: 3 jobs (Jobs 3, 5, 21)
- Reference: 14 user stories nested under main jobs (Jobs 2, 4, 6, 8, 10, 12, 14, 15, 16, 17, 18, 19, 20, 22)
- Plan: Gap identified
- Deploy: Not applicable (conceptual guide)
- Monitor: Gap identified
- Troubleshoot: Gap identified
- Operate: Gap identified

**Content Analysis:**
- Main Jobs: 11 (conceptual, stable goals)
- User Stories: 11 (implementation-specific, nested under main jobs)
- Source Sections: 12 concept modules in current structure
- Platform Variations: OpenShift Pipelines/Tekton specific
- Document Type: Conceptual and reference guide (no procedures)

**Navigation Improvements:**
- 8% reduction in top-level items (12 → 11)
- Clear concept-to-implementation hierarchy
- Explicit workflow stage progression (Get Started → Architecture → Reference)
- Better visibility for critical jobs (Finally tasks elevated to Get Started)

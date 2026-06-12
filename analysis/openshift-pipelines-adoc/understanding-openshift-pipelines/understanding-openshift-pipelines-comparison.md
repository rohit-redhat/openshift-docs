# Understanding OpenShift Pipelines - TOC Comparison

**Current Feature-Based vs. Proposed JTBD-Based Structure**

**Analysis Date:** 2026-06-11
**JTBD Records:** 22
**Main Jobs:** 11 core jobs (11 user stories as implementation details)
**Coverage:** Conceptual and reference document

---

## Current Structure (Feature-Based)

Understanding OpenShift Pipelines
- **Abstract** — Overview of Tekton-based CI/CD solution
- **Key features** — Platform capabilities and serverless architecture
- **OpenShift Pipelines concepts** — Core concepts overview
  - **Tasks** — Task definition and structure
  - **When expression** — Conditional task execution
  - **Finally tasks** — Cleanup and notification tasks
  - **Task run** — Task instantiation
  - **Pipelines** — Pipeline composition
  - **Pipeline run** — Pipeline execution
  - **Pod templates** — Pod-level configuration
  - **Workspaces** — Shared storage for tasks
  - **Step actions** — Reusable step definitions
  - **Triggers** — Event-driven automation
- **Additional resources** — Links to related documentation

**Total:** 1 assembly, 12 concept modules, organized by component/feature

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
  → Lines 69-87: Key features
    Source: Assembly, Key features section
  - Serverless CI/CD system
  - Decentralized team support for microservices
  - Integration with OpenShift tools (S2I, Buildah, Buildpacks, Kaniko)
  - Developer console management

**Job 7: Ensure Cleanup and Notification Tasks Always Run**

*When designing a CI/CD pipeline, I want to understand how to ensure cleanup and notification tasks always run, so I can maintain system hygiene and provide consistent feedback regardless of pipeline success or failure*

Prerequisites: None

- **7.1. Understanding Finally Tasks Concept** `[concept]`
  → Lines 351-428: Finally tasks
    Source: Assembly, Finally tasks section
  - Finally tasks execute in parallel after all pipeline tasks complete
  - Run regardless of success or failure
  - Can consume results from earlier tasks
  - Context: Use for cleanup operations, notifications, validation

**Job 9: Instantiate and Execute Tasks**

*When learning CI/CD automation, I want to understand how task definitions are instantiated and executed with specific parameters, so I can control the execution of individual build steps*

Prerequisites: None

- **9.1. Task Execution Lifecycle** `[concept]`
  → Lines 431-477: Task run
    Source: Assembly, Task run section
  - TaskRun as instantiation mechanism
  - Provides specific inputs, outputs, execution parameters
  - Can start independently or as part of pipeline run
  - Context: Understanding the concept vs OpenShift-specific implementation

**Job 11: Compose Multi-Task Workflows**

*When building CI/CD automation, I want to understand how to compose multiple tasks into an ordered workflow, so I can automate complex build, test, and deployment processes*

Prerequisites: None

- **11.1. Pipeline Composition Model** `[concept]`
  → Lines 480-611: Pipelines
    Source: Assembly, Pipelines section
  - Collection of tasks in specific execution order
  - Uses runAfter for task sequencing
  - Shares workspaces and parameters across tasks
  - Context: Conceptual understanding of pipeline orchestration

**Job 13: Execute Pipeline Workflows with Runtime Parameters**

*When executing CI/CD workflows, I want to understand how to instantiate a pipeline definition with specific parameters and credentials for a particular scenario, so I can run my build and deployment process*

Prerequisites: None

- **13.1. Pipeline Instantiation and Execution** `[concept]`
  → Lines 614-672: Pipeline run
    Source: Assembly, Pipeline run section
  - PipelineRun as binding mechanism for pipelines, workspaces, credentials, parameters
  - Creates task run for each pipeline task
  - Tracks progress in status field
  - Context: Runtime execution of pipeline definitions

#### Understanding Pipeline Architecture

**Job 3: Structure Reusable Units of Work**

*When designing a CI/CD workflow, I want to understand how to structure reusable units of work, so I can create maintainable and composable pipeline components*

Prerequisites: Understand basic OpenShift Pipelines concepts

- **3.1. Task Conceptual Model** `[concept]`
  → Lines 105-177: Tasks
    Source: Assembly, Tasks section
  - Tasks as building blocks with inputs/outputs
  - Steps as sequential commands
  - Pod/container execution model
  - Context: Architectural understanding, not tool-specific implementation

**Job 5: Control Pipeline Execution Flow with Conditions**

*When implementing conditional logic in pipelines, I want to understand how to guard task execution, so I can implement conditional logic in my pipelines*

Prerequisites: Understand Tasks and pipeline orchestration

- **5.1. When Expressions Conceptual Model** `[concept]`
  → Lines 180-348: When expression
    Source: Assembly, When expression section
  - When expressions with input/operator/values components
  - Evaluation timing and use cases
  - Context: Checking results, file changes, image existence, workspace availability

**Job 21: Automate Pipeline Execution from External Events**

*When creating event-driven CI/CD workflows, I want to understand how triggers capture and process events to instantiate pipeline runs, so I can create event-driven CI/CD workflows without manual intervention*

Prerequisites: None

- **21.1. Triggers Architecture** `[concept]`
  → Lines 969-1163: Triggers
    Source: Assembly, Triggers section
  - TriggerBinding extracts event payload
  - TriggerTemplate creates resources
  - Trigger combines binding/template/interceptors
  - EventListener provides HTTP endpoint
  - Interceptors filter/verify events (GitHub, GitLab, Bitbucket, Webhook, CEL)
  - Context: Comprehensive event-driven CI/CD system architecture

#### Reference Information

**Job 2: Determine Supported Build Tools**

*When building container images in CI/CD pipeline, I want to know what build tools are supported, so I can choose the right image building strategy for my project*

Prerequisites: None

- **2.1. Build Tool Options** `[reference]`
  → Lines 84-85: Key features
    Source: Assembly, Key features section
  - S2I, Buildah, Buildpacks, Kaniko
  - Portability across OpenShift platforms

**Job 4: Define Task Specification Structure**

*When creating a Task definition, I want to understand the Task specification structure and required fields, so I can correctly define my pipeline tasks*

Prerequisites: None

- **4.1. Task YAML Structure** `[reference]`
  → Lines 121-158: Tasks
    Source: Assembly, Tasks section
  - apiVersion, kind, metadata, spec fields
  - apply-manifests example

**Job 6: Write Conditional Expressions**

*When skipping tasks based on parameter values or task results, I want to understand the when expression syntax and operators, so I can write correct conditional expressions*

Prerequisites: None

- **6.1. When Expression Syntax** `[reference]`
  → Lines 194-327: When expression
    Source: Assembly, When expression section
  - input/operator/values fields
  - in/notin operators
  - Parameters and results in conditions
  - PipelineRun example with various condition patterns

**Job 8: Configure Finally Tasks with Task Results**

*When implementing cleanup operations in OpenShift Pipelines, I want to configure finally tasks that consume results from earlier tasks, so I can perform context-aware cleanup and validation*

Prerequisites: Understanding of OpenShift Pipelines task concept, YAML syntax

- **8.1. Finally Task Implementation** `[reference]`
  → Lines 351-428: Finally tasks
    Source: Assembly, Finally tasks section
  - Using finally field
  - Consuming results via parameters
  - clone-cleanup-workspace example

**Job 10: Create TaskRun Resources**

*When executing a task in OpenShift Pipelines, I want to create a TaskRun resource with the required workspace and parameters, so I can run the task with my specific configuration*

Prerequisites: Task definition exists, Workspace configuration available

- **10.1. TaskRun Resource Configuration** `[reference]`
  → Lines 431-477: Task run
    Source: Assembly, Task run section
  - TaskRun YAML structure
  - Workspace binding with PersistentVolumeClaim
  - apply-manifests-taskrun example

**Job 12: Define Pipeline with Tasks and Dependencies**

*When defining a pipeline in OpenShift Pipelines, I want to specify tasks with workspaces, parameters, and execution order using runAfter, so I can create a build-and-deploy workflow*

Prerequisites: Understanding of YAML syntax, Tasks available in cluster/namespace

- **12.1. Pipeline Specification** `[reference]`
  → Lines 480-611: Pipelines
    Source: Assembly, Pipelines section
  - Pipeline YAML structure
  - Cluster resolver for task references
  - runAfter for sequencing
  - build-and-deploy pipeline example
  - Context: Buildah task requires pipeline service account

**Job 14: Create PipelineRun Resources**

*When running a pipeline in OpenShift Pipelines, I want to create a PipelineRun resource with parameter values and workspace volume claims, so I can execute my build-and-deploy workflow for a specific application*

Prerequisites: Pipeline definition exists, Storage class available

- **14.1. PipelineRun Configuration** `[reference]`
  → Lines 614-672: Pipeline run
    Source: Assembly, Pipeline run section
  - PipelineRun YAML structure
  - volumeClaimTemplate for workspace provisioning
  - build-deploy-api-pipelinerun example

**Job 15: Configure Pod-Level Settings for Pipeline Execution**

*When enforcing security or runtime requirements across pipeline executions, I want to understand how to configure pod-level settings, so I can ensure consistent security posture and compliance for all task pods*

Prerequisites: None

- **15.1. Pod Template Configuration** `[reference]`
  → Lines 681-740: Pod templates
    Source: Assembly, Pod templates section
  - Pod template parameters (securityContext, schedulerName)
  - PipelineRun vs TaskRun spec locations
  - Common use case: run as non-root user
  - Context: v1 API changes from v1beta1

**Job 16: Apply Pod Template Configurations**

*When running tasks as specific user or with custom scheduler settings, I want to apply pod template configurations to pipeline runs, so I can meet organizational security or scheduling requirements*

Prerequisites: Understanding of Kubernetes Pod specifications, Access to PipelineRun or TaskRun definitions

- **16.1. Pod Template Implementation** `[reference]`
  → Lines 681-740: Pod templates
    Source: Assembly, Pod templates section
  - securityContext examples (runAsNonRoot, runAsUser)
  - schedulerName examples (volcano)
  - Different spec locations for PipelineRun vs TaskRun

**Job 17: Declare and Configure Workspaces**

*When sharing data between pipeline tasks or providing runtime storage, I want to understand how to declare and configure workspaces, so I can create reusable tasks that work across different environments without hardcoding storage locations*

Prerequisites: None

- **17.1. Workspaces Conceptual Model** `[concept]`
  → Lines 747-871: Workspaces
    Source: Assembly, Workspaces section
  - Separation of volume declaration from runtime storage
  - Recommended over PipelineResource CRs
  - Use cases: inputs/outputs, sharing data, credentials, configs, caching
  - Backing types: ConfigMap, Secret, PVC, volumeClaimTemplate, emptyDir
  - Context: Makes tasks reusable and environment-independent

**Job 18: Map Workspaces in Multi-Task Pipelines**

*When building a multi-task pipeline that needs shared storage, I want to declare a workspace in the pipeline and map it to tasks, so I can pass data from one task to another without managing storage directly*

Prerequisites: Understanding of pipeline and task structure, Knowledge of workspace use cases

- **18.1. Workspace Mapping Implementation** `[reference]`
  → Lines 747-871: Workspaces
    Source: Assembly, Workspaces section
  - Pipeline-level workspace declaration
  - Task-level workspace mapping
  - PipelineRun storage provisioning via volumeClaimTemplate
  - build-and-deploy pipeline example

**Job 19: Define and Reference Reusable Step Actions**

*When reusing common step logic across multiple tasks, I want to understand how to define and reference step actions, so I can avoid duplicating step definitions and maintain consistency across task implementations*

Prerequisites: None

- **19.1. StepAction Conceptual Model** `[concept]`
  → Lines 875-965: Step actions
    Source: Assembly, Step actions section
  - StepAction CR contains reusable action definitions
  - Supports parameters and results
  - Does not include workspace definitions (task provides)
  - Security: parameter values must use env variables, not direct script substitution
  - Context: Reusability across tasks and teams

**Job 20: Create StepAction Resources with Parameters**

*When sharing step implementation across tasks or referencing external step definitions, I want to create a StepAction resource with parameters and results, so I can invoke the same action from multiple tasks without code duplication*

Prerequisites: Understanding of task and step structure, Knowledge of parameter and result passing

- **20.1. StepAction Implementation** `[reference]`
  → Lines 875-965: Step actions
    Source: Assembly, Step actions section
  - StepAction YAML structure
  - Parameter definitions (type optional)
  - Environment variables for parameters
  - apply-manifests-action example
  - Task step reference using ref.name

**Job 22: Configure Event-Driven Pipeline Automation**

*When automating pipeline execution from Git push events, I want to extract repository information and automatically create a pipeline run with the correct parameters, so I can deploy the latest changes without manual pipeline triggering*

Prerequisites: Understanding of TriggerBinding and TriggerTemplate, Webhook configured, EventListener deployed

- **22.1. Trigger Configuration Implementation** `[reference]`
  → Lines 969-1163: Triggers
    Source: Assembly, Triggers section
  - TriggerBinding extracts from body (repository.url, repository.name, head_commit.id)
  - TriggerTemplate creates PipelineRun with extracted params
  - Trigger combines binding/template with GitHub interceptor
  - EventListener provides HTTP endpoint
  - vote-app trigger example with Secret for verification

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | Organized by component/feature (Tasks, Pipelines, Workspaces, etc.) | Organized by user goals and workflow stages |
| **Top-level items** | 1 assembly + 12 concept modules | 11 main jobs with 11 user stories as implementation details |
| **Navigation model** | Linear reading through components | Goal-directed: find your job, choose implementation approach |
| **Task-specific content** | Scattered across Tasks, TaskRun sections | Consolidated under Job 3 (architecture) + Jobs 4, 10 (reference) |
| **Pipeline-specific content** | Scattered across Pipelines, PipelineRun sections | Consolidated under Job 11 (architecture) + Jobs 12, 14 (reference) |
| **Workspace content** | Single Workspaces section | Split into Job 17 (concept) + Job 18 (implementation) |
| **Trigger content** | Single Triggers section | Split into Job 21 (architecture) + Job 22 (implementation) |
| **Learning path** | Component-by-component | Workflow-based: Get Started → Architecture → Reference |

### Job List Adjustments from Suggested Input

The 22 JTBD records were organized into **11 main jobs** with **11 user stories** (implementation-specific jobs nested as related content):

1. **Jobs 1 and 2**: Job 2 (build tools) is a related job nested under Job 1 (capabilities) as reference material
2. **Jobs 3 and 4**: Job 4 (task spec) is a user story nested under Job 3 (task architecture) as reference
3. **Jobs 5 and 6**: Job 6 (when syntax) is a user story nested under Job 5 (conditional logic) as reference
4. **Jobs 7 and 8**: Job 8 (finally implementation) is a user story nested under Job 7 (finally concept) as reference
5. **Jobs 9 and 10**: Job 10 (TaskRun resource) is a user story nested under Job 9 (task execution) as reference
6. **Jobs 11 and 12**: Job 12 (pipeline spec) is a user story nested under Job 11 (pipeline composition) as reference
7. **Jobs 13 and 14**: Job 14 (PipelineRun resource) is a user story nested under Job 13 (pipeline execution) as reference
8. **Jobs 15 and 16**: Job 16 (pod template implementation) is a user story nested under Job 15 (pod template concept) as reference
9. **Jobs 17 and 18**: Job 18 (workspace mapping) is a user story nested under Job 17 (workspace concept) as reference
10. **Jobs 19 and 20**: Job 20 (StepAction resource) is a user story nested under Job 19 (step action concept) as reference
11. **Jobs 21 and 22**: Job 22 (trigger implementation) is a user story nested under Job 21 (trigger architecture) as reference

**Rationale:** This document is a conceptual and reference guide. The main jobs represent stable, tool-agnostic concepts (pipeline composition, conditional logic, event-driven automation). The user stories represent OpenShift Pipelines/Tekton-specific implementation details (YAML structures, resource specifications).

---

## Consolidation Examples

### Example 1: Task Content (2 scattered sections → 1 unified architecture job)

**Current (Fragmented):**
- Section: Tasks (lines 105-177) — Task definition and structure
- Section: Task run (lines 431-477) — Task instantiation

Users must read two separate sections to understand task concept vs execution.

**Proposed (Consolidated):**
- **Job 3: Structure Reusable Units of Work** (architecture)
  - 3.1. Task Conceptual Model (concept) — lines 105-177
- **Job 4: Define Task Specification Structure** (reference, nested under Job 3)
  - 4.1. Task YAML Structure (reference) — lines 121-158
- **Job 9: Instantiate and Execute Tasks** (Get Started)
  - 9.1. Task Execution Lifecycle (concept) — lines 431-477
- **Job 10: Create TaskRun Resources** (reference, nested under Job 9)
  - 10.1. TaskRun Resource Configuration (reference) — lines 431-477

**Benefit:** Clear separation of architecture (Job 3) vs execution (Job 9), with implementation details nested as reference material.

### Example 2: Pipeline Content (2 scattered sections → 1 unified architecture job)

**Current (Fragmented):**
- Section: Pipelines (lines 480-611) — Pipeline composition
- Section: Pipeline run (lines 614-672) — Pipeline execution

Users must read two separate sections to understand pipeline concept vs execution.

**Proposed (Consolidated):**
- **Job 11: Compose Multi-Task Workflows** (architecture)
  - 11.1. Pipeline Composition Model (concept) — lines 480-611
- **Job 12: Define Pipeline with Tasks and Dependencies** (reference, nested under Job 11)
  - 12.1. Pipeline Specification (reference) — lines 480-611
- **Job 13: Execute Pipeline Workflows with Runtime Parameters** (Get Started)
  - 13.1. Pipeline Instantiation and Execution (concept) — lines 614-672
- **Job 14: Create PipelineRun Resources** (reference, nested under Job 13)
  - 14.1. PipelineRun Configuration (reference) — lines 614-672

**Benefit:** Clear separation of composition (Job 11) vs execution (Job 13), with implementation details nested as reference material.

### Example 3: Workspaces Content (1 section → concept + implementation split)

**Current (Single Section):**
- Section: Workspaces (lines 747-871) — Workspace declaration and configuration (concept and implementation mixed)

Users read a single large section covering both concept and implementation.

**Proposed (Split):**
- **Job 17: Declare and Configure Workspaces** (reference)
  - 17.1. Workspaces Conceptual Model (concept) — lines 747-871
- **Job 18: Map Workspaces in Multi-Task Pipelines** (reference, nested under Job 17)
  - 18.1. Workspace Mapping Implementation (reference) — lines 747-871

**Benefit:** Concept (why and when to use workspaces) separated from implementation (how to map them in pipelines).

---

## Content Gaps Identified

| Gap | JTBD Reference | Current Coverage | Impact |
|-----|---------------|-----------------|--------|
| No monitoring or observability content | Would support monitoring job | None | **High** — Users have no guidance for tracking pipeline health, viewing logs, or troubleshooting runs |
| No troubleshooting procedures | Would support troubleshooting job | None | **High** — Users have no guidance for common failure scenarios or debugging techniques |
| No upgrade or migration content | Would support upgrade job | None | **Medium** — Users have no guidance for version upgrades or migrating from other CI/CD systems |
| No platform selection or evaluation criteria | Would support planning job | Abstract mentions Tekton-based solution | **Low** — This is a conceptual guide, not a decision guide |
| No deployment procedures | Would support deployment job | Conceptual and reference only | **Low** — Intentional design; guide focuses on concepts, not procedures |
| No operational procedures | Would support operations job | None | **Medium** — Users have no guidance for day-2 operations like backup, disaster recovery |

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 12 concept modules | 11 main jobs | 8% reduction |
| Sections to browse for "task execution" | 2 sections (Tasks, Task run) | 1 architecture job + 1 execution job with nested reference | 2 discrete jobs vs 2 scattered sections |
| Sections to browse for "pipeline composition" | 2 sections (Pipelines, Pipeline run) | 1 architecture job + 1 execution job with nested reference | 2 discrete jobs vs 2 scattered sections |
| Sections to browse for "event-driven automation" | 1 section (Triggers) | 1 architecture job + 1 implementation job with nested reference | Concept separated from implementation |
| Sections to browse for "workspaces" | 1 section (Workspaces) | 1 concept job + 1 implementation job with nested reference | Concept separated from implementation |
| Clicks to find "conditional logic" | 2 clicks (OpenShift Pipelines concepts → When expression) | 2 clicks (Understanding Pipeline Architecture → Job 5) | Same number of clicks, clearer job-based navigation |
| Workflow stage coverage | 1 stage (Reference) | 3 stages (Get Started, Architecture, Reference) | Better workflow progression |

**Final job count: 11 main jobs** (reduced from suggested 22 by nesting implementation-specific jobs as user stories under conceptual main jobs). This document is a conceptual and reference guide, so the main jobs represent stable concepts while user stories represent OpenShift Pipelines-specific implementation details.

---

## Workflow Coverage Comparison

| Stage | Current | Proposed | Gap Status |
|-------|---------|----------|------------|
| Get Started | ⚠️ Scattered | ✅ Jobs 1, 7, 9, 11, 13 | Improved - consolidated |
| Plan | ❌ Missing | ❌ Missing | Gap remains |
| Architecture | ⚠️ Implicit in modules | ✅ Jobs 3, 5, 21 | Improved - explicit architecture section |
| Configure | ❌ Missing | ❌ Missing | Not applicable - conceptual guide |
| Deploy | ❌ Missing | ❌ Missing | Not applicable - conceptual guide |
| Monitor | ❌ Missing | ❌ Missing | Gap remains |
| Troubleshoot | ❌ Missing | ❌ Missing | Gap remains |
| Reference | ✅ All modules | ✅ Jobs 2, 4, 6, 8, 10, 12, 14, 15, 16, 17, 18, 19, 20, 22 | Reorganized by parent job |

### Coverage Summary

**Current structure gaps:** Plan, Configure, Deploy, Monitor, Troubleshoot, Operate
**Proposed structure gaps:** Plan, Configure, Deploy, Monitor, Troubleshoot, Operate
**Gaps addressed by restructure:** Architecture (now explicit), Get Started (now consolidated)

**Note:** This document is intentionally a conceptual and reference guide, not a procedural guide. The gaps in Configure, Deploy, and Operate are expected.

### Recommendations for Gap Closure

| Gap | Recommendation | Priority |
|-----|----------------|----------|
| Monitor | Link to observability guide or add basic pipeline run checks | High |
| Troubleshoot | Add common failure scenarios and debugging techniques | High |
| Plan | Add platform evaluation criteria and comparison to other CI/CD tools | Low |
| Upgrade | Add version upgrade procedures if applicable | Medium |
| Operate | Link to operational guide for backup, disaster recovery | Medium |

---

## Success Criteria

**A good TOC comparison:**

- Users can immediately see main goals (11 main jobs vs 12 scattered modules)
- Users can find jobs by what they need to accomplish (workflow stages) vs browsing components
- Users can see it's simpler: 11 jobs vs 12 modules, with clear nesting
- Stakeholders understand the proposed improvement: concept vs implementation separation
- Content mappers know what to extract: line references provided for all content
- Structure follows natural workflow progression: Get Started → Architecture → Reference
- No persona gates: jobs are accessible to all users with appropriate permissions
- Prerequisites stated as knowledge/permissions, not job titles
- Gaps clearly marked with impact ratings and recommendations

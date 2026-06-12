# Understanding OpenShift Pipelines
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** This guide helps users understand the core concepts, components, and architecture of OpenShift Pipelines to design and implement CI/CD automation workflows.

**Personas:** Developer, CI/CD engineer, Platform administrator

**Main Jobs:** 11 core jobs across 4 workflow stages

---

## Quick Navigation

**I want to:**
- Learn what OpenShift Pipelines can do → Job 1 (Get Started)
- Know what build tools are supported → Job 2 (Reference)
- Understand how to structure pipeline components → Job 3 (Architecture)
- Design conditional pipeline logic → Job 5 (Architecture)
- Ensure cleanup tasks always run → Job 7 (Get Started)
- Execute a task with specific parameters → Job 9 (Get Started)
- Build a multi-task workflow → Job 11 (Get Started)
- Configure pod-level security settings → Job 15 (Reference)
- Share data between pipeline tasks → Job 17 (Reference)
- Reuse common step logic → Job 19 (Reference)
- Automate pipeline execution from events → Job 21 (Architecture)

---

# Table of Contents

## Getting Started with OpenShift Pipelines

### Job 1: Understand OpenShift Pipelines Capabilities
*When I need to implement CI/CD for my application*

**Personas:** Developer

#### Platform Features and Differentiators

→ Lines 69-87: Key features
  Source: Assembly, Key features section

- Serverless CI/CD system
- Support for decentralized teams on microservices
- Integration with OpenShift tools (S2I, Buildah, Buildpacks, Kaniko)
- Developer console management

### Job 7: Ensure Cleanup and Notification Tasks Always Run
*When designing a CI/CD pipeline*

**Personas:** CI/CD engineer

#### Understanding Finally Tasks Concept

→ Lines 351-428: Finally tasks
  Source: Assembly, Finally tasks section

- Finally tasks execute in parallel after all pipeline tasks complete
- Run regardless of success or failure
- Can consume results from earlier tasks
- Use cases: cleanup operations, notifications, validation

**Examples:**
- Clone-cleanup-workspace pipeline with cleanup and check-git-commit finally tasks
- Consuming task results in finally tasks via parameters

### Job 9: Instantiate and Execute Tasks
*When learning CI/CD automation*

**Personas:** Developer

#### Task Execution Lifecycle

→ Lines 431-477: Task run
  Source: Assembly, Task run section

**Concept: TaskRun as instantiation mechanism**
- TaskRun creates an instance of a task definition
- Provides specific inputs, outputs, and execution parameters
- Can start independently or as part of pipeline run
- Automatically created by PipelineRun for each task

**OpenShift Pipelines Implementation:**
- Creating TaskRun resource with workspace and parameters
- Binding workspaces using PersistentVolumeClaim
- Configuring service account

### Job 11: Compose Multi-Task Workflows
*When building CI/CD automation*

**Personas:** CI/CD engineer

#### Pipeline Composition Model

→ Lines 480-611: Pipelines
  Source: Assembly, Pipelines section

**Concept: Pipeline orchestration**
- Collection of tasks in specific execution order
- Constructs complex workflows for build, deployment, delivery
- Uses runAfter for task sequencing
- Shares workspaces and parameters across tasks

**OpenShift Pipelines Implementation:**
- Build-and-deploy pipeline example
- Cluster resolver for referencing tasks from openshift-pipelines namespace
- Workspace and parameter definition at pipeline level

### Job 13: Execute Pipeline Workflows with Runtime Parameters
*When executing CI/CD workflows*

**Personas:** Developer

#### Pipeline Instantiation and Execution

→ Lines 614-672: Pipeline run
  Source: Assembly, Pipeline run section

**Concept: PipelineRun as binding mechanism**
- Binds pipeline to workspaces, credentials, parameter values
- Creates task run for each pipeline task
- Tracks progress in status field
- Specific to a scenario/execution instance

**OpenShift Pipelines Implementation:**
- Creating PipelineRun resource with parameter values
- VolumeClaimTemplate for dynamic workspace provisioning
- Monitoring execution progress via status field

## Understanding Pipeline Architecture

### Job 3: Structure Reusable Units of Work
*When designing a CI/CD workflow*

**Personas:** CI/CD engineer

**Prerequisites:** Understand basic OpenShift Pipelines concepts

#### Task Conceptual Model

→ Lines 105-177: Tasks
  Source: Assembly, Tasks section

**Concept: Tasks as building blocks**
- Function of inputs and outputs
- Sequentially executed steps
- Reusable across many pipelines
- Each task runs as a pod; steps as containers within pod

**Task Specification Structure:**
- apiVersion, kind, metadata, spec
- Workspaces, parameters, steps definitions
- apply-manifests task example

**Note:** Starting with Pipelines 1.6, HOME and workingDir no longer have defaults

### Job 5: Control Pipeline Execution Flow with Conditions
*When implementing conditional logic in pipelines*

**Personas:** CI/CD engineer

**Prerequisites:** Understand Tasks and pipeline orchestration

#### When Expressions Conceptual Model

→ Lines 180-348: When expression
  Source: Assembly, When expression section

**Concept: Conditional task execution**
- Guard task execution with specific criteria
- Works in regular tasks and finally section
- Three components: input, operator, values
- Evaluation happens before task runs

**Use Cases:**
- Check result of preceding task
- Verify file changes in Git repository
- Confirm image exists in registry
- Validate optional workspace availability

**When Expression Syntax:**
- Input: static inputs, parameters, task results, execution status
- Operator: in or notin
- Values: array of strings (static or variables)
- Example: guarded-pr pipeline with create-file, check-file, echo-file-exists tasks

**UI Indicators:**
- Success: task and diamond appear in success state
- Skipped: task and diamond appear in skipped state
- Failed: task and diamond appear in failed state

### Job 21: Automate Pipeline Execution from External Events
*When creating event-driven CI/CD workflows*

**Personas:** CI/CD engineer

#### Triggers Architecture

→ Lines 969-1163: Triggers
  Source: Assembly, Triggers section

**Concept: Event-driven CI/CD system**
- Captures external events (Git push, pull requests)
- Processes event data to instantiate pipeline runs
- Decoupled, reusable trigger definitions

**Main Components:**

**TriggerBinding: Extract event payload**
- Extracts fields from event (repository URL, name, revision)
- Stores as parameters for TriggerTemplate
- Example: vote-app binding extracting Git information

**TriggerTemplate: Define resource creation**
- Standard for creating resources from parameterized data
- Creates PipelineRun with extracted parameters
- Example: vote-app template creating build-deploy pipeline run

**Trigger: Combine binding, template, interceptors**
- Connects TriggerBinding and TriggerTemplate
- Optional interceptors for event processing
- Vote-trigger example with GitHub interceptor

**Interceptors: Event processing**
- Filter payload, verify events, test conditions
- Platform-specific: GitHub, GitLab, Bitbucket, Webhook, CEL
- Use secrets for event verification
- Example: GitHub interceptor filtering push events

**EventListener: HTTP endpoint**
- Listens for incoming HTTP-based events with JSON payload
- Performs lightweight event processing
- References Trigger resource
- Example: vote-app EventListener

## Reference Information

### Job 2: Determine Supported Build Tools
*When building container images in CI/CD pipeline*

**Personas:** Developer

**Parent Job:** Job 1 (Understand OpenShift Pipelines Capabilities)

#### Build Tool Options

→ Lines 84-85: Key features
  Source: Assembly, Key features section

**Supported image build tools:**
- Source-to-Image (S2I)
- Buildah
- Buildpacks
- Kaniko

**Portability:** Tools work across any OpenShift platform

### Job 4: Define Task Specification Structure
*When creating a Task definition*

**Personas:** Developer

**Parent Job:** Job 3 (Structure Reusable Units of Work)

#### Task YAML Structure

→ Lines 121-158: Tasks
  Source: Assembly, Tasks section

**Required fields:**
- apiVersion: tekton.dev/v1
- kind: Task
- metadata.name: unique task identifier
- spec: parameters, steps, workspace definitions

**Example:** apply-manifests task with workspace, parameters, steps

### Job 6: Write Conditional Expressions
*When skipping tasks based on conditions*

**Personas:** Developer

**Parent Job:** Job 5 (Control Pipeline Execution Flow with Conditions)

#### When Expression Syntax

→ Lines 194-327: When expression
  Source: Assembly, When expression section

**Syntax components:**
- input/operator/values fields
- in/notin operators
- Parameters and results in conditions

**Example:** PipelineRun with when expressions checking path parameter, task results, execution status

### Job 8: Configure Finally Tasks with Task Results
*When implementing cleanup operations in OpenShift Pipelines*

**Personas:** Developer

**Parent Job:** Job 7 (Ensure Cleanup and Notification Tasks Always Run)

**Prerequisites:** Understanding of OpenShift Pipelines task concept, YAML syntax

#### Finally Task Implementation

→ Lines 351-428: Finally tasks
  Source: Assembly, Finally tasks section

**Implementation details:**
- Define finally tasks using finally field
- Reference tasks via taskRef
- Consume results from earlier tasks via parameters
- Use taskSpec for embedded task definitions

**Example:** clone-cleanup-workspace pipeline with cleanup-workspace and check-git-commit finally tasks

### Job 10: Create TaskRun Resources
*When executing a task in OpenShift Pipelines*

**Personas:** Developer

**Parent Job:** Job 9 (Instantiate and Execute Tasks)

**Prerequisites:** Task definition exists, Workspace configuration available

#### TaskRun Resource Configuration

→ Lines 431-477: Task run
  Source: Assembly, Task run section

**TaskRun specification:**
- apiVersion: tekton.dev/v1
- kind: TaskRun
- metadata.name: unique identifier
- spec: taskRef, workspaces, serviceAccountName

**Workspace binding:**
- persistentVolumeClaim with claimName
- Example: apply-manifests-taskrun

### Job 12: Define Pipeline with Tasks and Dependencies
*When defining a pipeline in OpenShift Pipelines*

**Personas:** Developer

**Parent Job:** Job 11 (Compose Multi-Task Workflows)

**Prerequisites:** Understanding of YAML syntax, Tasks available in cluster/namespace

#### Pipeline Specification

→ Lines 480-611: Pipelines
  Source: Assembly, Pipelines section

**Pipeline fields:**
- apiVersion: tekton.dev/v1
- kind: Pipeline
- metadata.name: unique identifier
- spec.workspaces: shared workspaces
- spec.params: pipeline parameters
- spec.tasks: task definitions with taskRef, runAfter, workspaces, params

**Task resolution:**
- Cluster resolver for referencing tasks from openshift-pipelines namespace
- Parameters: kind, name, namespace

**Example:** build-and-deploy pipeline with fetch-repository, build-image, apply-manifests, update-deployment tasks

**Note:** Buildah task requires pipeline service account with sufficient permissions

### Job 14: Create PipelineRun Resources
*When running a pipeline in OpenShift Pipelines*

**Personas:** Developer

**Parent Job:** Job 13 (Execute Pipeline Workflows with Runtime Parameters)

**Prerequisites:** Pipeline definition exists, Storage class available for volume claim

#### PipelineRun Configuration

→ Lines 614-672: Pipeline run
  Source: Assembly, Pipeline run section

**PipelineRun specification:**
- apiVersion: tekton.dev/v1
- kind: PipelineRun
- metadata.name: unique identifier
- spec.pipelineRef.name: pipeline reference
- spec.params: parameter values
- spec.workspaces: workspace provisioning

**Workspace provisioning:**
- volumeClaimTemplate for dynamic PVC creation
- accessModes: ReadWriteOnce
- storage requests

**Monitoring:**
- status field tracks progress
- Example: build-deploy-api-pipelinerun

### Job 15: Configure Pod-Level Settings for Pipeline Execution
*When enforcing security or runtime requirements across pipeline executions*

**Personas:** Platform administrator

#### Pod Template Configuration

→ Lines 681-740: Pod templates
  Source: Assembly, Pod templates section

**Concept: Pod template parameters**
- Define pod-level settings for all task pods
- Available Pod CR parameters can be used
- Common use case: run as non-root user

**PipelineRun pod template:**
- Location: taskRunTemplate.podTemplate spec
- Example: securityContext with runAsNonRoot, runAsUser

**TaskRun pod template:**
- Location: podTemplate spec
- Example: schedulerName (volcano), securityContext

**Note:** v1beta1 API defined podTemplate directly in spec; v1 API requires taskRunTemplate

### Job 16: Apply Pod Template Configurations
*When running tasks as specific user or with custom scheduler*

**Personas:** CI/CD engineer

**Parent Job:** Job 15 (Configure Pod-Level Settings for Pipeline Execution)

**Prerequisites:** Understanding of Kubernetes Pod specifications, Access to PipelineRun or TaskRun definitions

#### Pod Template Implementation

→ Lines 681-740: Pod templates
  Source: Assembly, Pod templates section

**Configuration options:**
- securityContext: runAsNonRoot, runAsUser
- schedulerName: custom scheduler (e.g., volcano)

**Spec locations:**
- PipelineRun: taskRunTemplate.podTemplate
- TaskRun: podTemplate

**Examples:**
- Running as non-root user (runAsUser: 1001)
- Using custom scheduler

### Job 17: Declare and Configure Workspaces
*When sharing data between pipeline tasks or providing runtime storage*

**Personas:** Developer

#### Workspaces Conceptual Model

→ Lines 747-871: Workspaces
  Source: Assembly, Workspaces section

**Concept: Separation of volume declaration from runtime storage**
- Declare filesystem requirements at task/pipeline level
- Provide specific storage volumes at runtime
- Makes tasks reusable and environment-independent

**Note:** Workspaces recommended over PipelineResource CRs (difficult to debug, limited scope)

**Use Cases:**
- Store task inputs and outputs
- Share data among tasks
- Mount credentials from secrets
- Mount configurations from config maps
- Mount common tools
- Cache build artifacts

**Backing types:**
- Read-only config map or secret
- Existing persistent volume claim
- Volume claim from template
- emptyDir (discarded after task run)

**Pipeline workspace declaration:**
- spec.workspaces at pipeline level
- tasks.workspaces maps to pipeline workspace
- Example: build-and-deploy pipeline with shared-workspace

**PipelineRun workspace provisioning:**
- volumeClaimTemplate for dynamic PVC creation
- Example: build-deploy-api-pipelinerun with 500Mi storage

### Job 18: Map Workspaces in Multi-Task Pipelines
*When building a multi-task pipeline that needs shared storage*

**Personas:** Developer

**Parent Job:** Job 17 (Declare and Configure Workspaces)

**Prerequisites:** Understanding of pipeline and task structure, Knowledge of workspace use cases

#### Workspace Mapping Implementation

→ Lines 747-871: Workspaces
  Source: Assembly, Workspaces section

**Pipeline-level workspace declaration:**
- spec.workspaces with name
- Example: shared-workspace in build-and-deploy pipeline

**Task-level workspace mapping:**
- tasks.workspaces with name and workspace reference
- Example: build-image task maps source workspace to shared-workspace

**Data flow:**
- Pipeline declares workspace (shared-workspace)
- Tasks map to pipeline workspace (source → shared-workspace)
- PipelineRun provides storage (volumeClaimTemplate)

**Example:** build-image and apply-manifests tasks sharing source workspace

### Job 19: Define and Reference Reusable Step Actions
*When reusing common step logic across multiple tasks*

**Personas:** CI/CD engineer

#### StepAction Conceptual Model

→ Lines 875-965: Step actions
  Source: Assembly, Step actions section

**Concept: Reusable step definitions**
- StepAction CR contains action definitions
- Can be referenced from task steps
- Supports parameters and results
- Does not include workspace definitions (task provides)

**Security:** Parameter values cannot be used directly in scripts; use env variables

**StepAction structure:**
- apiVersion: tekton.dev/v1
- kind: StepAction
- metadata.name: unique identifier
- spec.params: parameter definitions
- spec.results: result definitions
- spec.image, env, workingDir, script

**Example:** apply-manifests-action with working_dir, manifest_dir parameters and output result

### Job 20: Create StepAction Resources with Parameters
*When sharing step implementation across tasks or referencing external step definitions*

**Personas:** CI/CD engineer

**Parent Job:** Job 19 (Define and Reference Reusable Step Actions)

**Prerequisites:** Understanding of task and step structure, Knowledge of parameter and result passing

#### StepAction Implementation

→ Lines 875-965: Step actions
  Source: Assembly, Step actions section

**StepAction resource creation:**
- Define parameters with type (optional)
- Define results with description
- Use environment variables for parameter values
- Script contains reusable logic

**Task step reference:**
- ref.name points to StepAction
- params pass values from task to step action
- Results automatically become step results

**Example:**
- apply-manifests-action StepAction
- apply-manifests-with-action task references action
- display_result step accesses apply step results

**Note:** Type specification for parameters is optional

### Job 22: Configure Event-Driven Pipeline Automation
*When automating pipeline execution from Git push events*

**Personas:** Developer

**Parent Job:** Job 21 (Automate Pipeline Execution from External Events)

**Prerequisites:** Understanding of TriggerBinding and TriggerTemplate, Webhook configured in Git repository, EventListener deployed

#### Trigger Configuration Implementation

→ Lines 969-1163: Triggers
  Source: Assembly, Triggers section

**TriggerBinding implementation:**
- Extract fields from event body (repository.url, repository.name, head_commit.id)
- Define params with name and value using $(body.field.path) syntax

**TriggerTemplate implementation:**
- Define params with name, description, default
- resourcetemplates section creates PipelineRun
- Use $(tt.params.name) to reference trigger template parameters
- Generate unique names with $(uid)

**Trigger implementation:**
- Combine bindings.ref and template.ref
- Configure interceptors (GitHub, GitLab, Bitbucket, Webhook, CEL)
- GitHub interceptor: secretRef, eventTypes (push)
- Create Secret with secretToken for verification

**EventListener implementation:**
- Define triggers.triggerRef
- Provides HTTP endpoint for webhook
- Uses serviceAccountName for permissions

**Example:** vote-app trigger system with TriggerBinding, TriggerTemplate, Trigger, EventListener, and github-secret

---

## Workflow Coverage

| Stage | Coverage | Jobs | Notes |
|-------|----------|------|-------|
| Get Started | ✅ | Jobs 1, 7, 9, 11, 13 | Platform overview, execution concepts |
| Architecture | ✅ | Jobs 3, 5, 21 | Task composition, conditional logic, event automation |
| Reference | ✅ | Jobs 2, 4, 6, 8, 10, 12, 14, 15, 16, 17, 18, 19, 20, 22 | Specifications, configurations, implementation details |
| Plan | ❌ | - | No platform selection or evaluation content |
| Deploy | ❌ | - | No deployment procedures (conceptual guide only) |
| Monitor | ❌ | - | No observability or monitoring content |
| Troubleshoot | ❌ | - | No troubleshooting content |
| Operate | ❌ | - | No operational procedures |

### Gaps Identified

| Stage | Gap | Recommendation |
|-------|-----|----------------|
| Monitor | No observability content | Link to monitoring guide or add basic pipeline run checks |
| Troubleshoot | No troubleshooting | Add common failure scenarios and debugging techniques |
| Deploy | No deployment procedures | This is intentional - guide focuses on concepts and reference |

---

## Navigation Guide

### By User Journey

**Developer learning OpenShift Pipelines:**
1. Job 1: Understand platform capabilities
2. Job 3: Learn task structure
3. Job 11: Understand pipeline composition
4. Job 13: Execute pipeline workflows
5. Job 17: Share data between tasks

**CI/CD engineer designing workflows:**
1. Job 3: Structure reusable task components
2. Job 5: Implement conditional logic
3. Job 7: Ensure cleanup tasks run
4. Job 11: Compose multi-task workflows
5. Job 19: Define reusable step actions
6. Job 21: Automate from external events

**Platform administrator configuring security:**
1. Job 15: Configure pod-level security settings
2. Job 16: Apply pod templates
3. Job 17: Declare workspaces

---

## Document Statistics

**Workflow Coverage:**
- Get Started: 5 jobs
- Architecture: 3 jobs
- Reference: 14 jobs
- Plan: Gap identified
- Deploy: Not applicable (conceptual guide)
- Monitor: Gap identified
- Troubleshoot: Gap identified
- Operate: Gap identified

**Main Jobs:** 22 (11 conceptual, 11 implementation-specific)
**Source Sections:** 12 concept modules
**Platform Variations:** OpenShift Pipelines/Tekton specific
**Document Type:** Conceptual and reference guide (no procedures)

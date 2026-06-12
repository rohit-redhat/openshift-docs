# About OpenShift Pipelines
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** Enable platform engineers and DevOps engineers to understand OpenShift Pipelines concepts and determine if it meets their CI/CD automation needs.

**Personas:** Platform engineer, DevOps engineer

**Main Jobs:** 3 core jobs across 1 workflow stage (Get Started)

---

## Quick Navigation

**I want to:**
- Understand what OpenShift Pipelines is -> Job 1 (Get Started)
- Learn key features and capabilities -> Job 1.1 (Get Started)
- Understand core concepts (tasks, pipelines, workspaces) -> Job 2 (Get Started)
- Learn how tasks work -> Job 2.1 (Get Started)
- Understand conditional execution -> Job 2.2 (Get Started)
- Learn about cleanup tasks -> Job 2.3 (Get Started)
- Understand pipeline orchestration -> Job 2.5 (Get Started)
- Learn about data sharing with workspaces -> Job 2.8 (Get Started)
- Understand event-driven automation -> Job 3 (Get Started)

---

# Table of Contents

## Evaluate the Platform

### Job 1: Evaluate OpenShift Pipelines for Your Needs
*When evaluating CI/CD solutions for Kubernetes-based applications*

**Personas:** Platform engineer

**Objective:** Determine if OpenShift Pipelines fits your automation needs by understanding its cloud-native approach and Tekton foundation.

#### 1.1 Understand What OpenShift Pipelines Is

**Context:** OpenShift Pipelines is a cloud-native CI/CD solution based on Kubernetes resources using Tekton building blocks. It provides portable pipeline definitions across Kubernetes distributions.

- **Overview:** Product definition and Tekton integration
  -> Lines 58-79: About OpenShift Pipelines

**Key Points:**
- Cloud-native CI/CD solution
- Based on Kubernetes resources and Tekton
- Standard CRDs for portable pipelines
- Separate release cadence from OpenShift Container Platform

**Related:** Understand key features (Job 1.1)

---

#### 1.2 Understand Key Features
*For platform engineers evaluating architectural fit*

**Objective:** Assess whether OpenShift Pipelines meets architectural requirements including serverless execution, decentralization support, and OpenShift integration.

**Features Overview:**

| Feature | Benefit |
|---------|---------|
| Serverless CI/CD | Runs pipelines with dependencies in isolated containers |
| Decentralized teams | Supports microservice-based architectures |
| Standard pipeline definitions | Easy to extend and integrate with OpenShift tools |
| Portable builds | Use S2I, Buildah, Buildpacks, Kaniko across platforms |
| Developer console integration | Create resources, view logs, manage pipelines |

-> Lines 76-86: Key features

**Related:** Understand core concepts (Job 2)

---

## Understand Core Concepts

### Job 2: Understand OpenShift Pipelines Core Concepts
*When learning about OpenShift Pipelines to design effective CI/CD workflows*

**Personas:** DevOps engineer

**Requires:**
- Understand what OpenShift Pipelines is (Job 1)

**Objective:** Learn the fundamental building blocks (tasks, pipelines, workspaces, triggers) and their relationships to design maintainable CI/CD workflows.

-> Lines 96-101: OpenShift Pipelines concepts overview

**Core Concepts:**
- Tasks - Reusable units of work
- Pipelines - Orchestration of tasks
- Task Runs & Pipeline Runs - Execution instances
- Workspaces - Shared data between tasks
- Step Actions - Reusable step definitions
- Triggers - Event-driven automation

---

#### 2.1 Understand How Tasks Work
*For DevOps engineers designing modular pipeline components*

**Objective:** Learn how Tasks define reusable units of work with sequentially executed steps.

**Task Fundamentals:**

- **Building Blocks:** Tasks consist of sequentially executed steps
- **Reusability:** Tasks can be used across multiple pipelines
- **Execution:** Each task runs as a pod, each step as a container
- **Data Sharing:** Steps share volumes (config maps, secrets, caches)

**Example Structure:**
```yaml
apiVersion: tekton.dev/v1
kind: Task
metadata:
  name: apply-manifests
spec:
  workspaces:
  - name: source
  params:
    - name: manifest_dir
  steps:
    - name: apply
      image: registry/cli:latest
      command: ["/bin/bash", "-c"]
```

-> Lines 112-177: Tasks

**Key Fields:**
- `apiVersion`: v1
- `kind`: Task
- `spec`: Parameters, steps, workspaces

**Note:** Starting with OpenShift Pipelines 1.6, HOME and workingDir no longer have default values.

**Related:** Understand task runs (Job 2.4), pipelines (Job 2.5)

---

#### 2.2 Understand Conditional Execution with When Expressions
*For DevOps engineers implementing branching and guarding logic*

**Objective:** Learn how when expressions control task execution based on criteria to implement conditional pipeline flows.

**When Expression Components:**

| Component | Purpose | Example Values |
|-----------|---------|----------------|
| `input` | Static inputs or variables | `$(params.path)`, `$(tasks.check-file.results.exists)` |
| `operator` | Relationship to values | `in`, `notin` |
| `values` | Array of string values | `["README.md"]`, `["yes"]` |

**Evaluation Rules:**
- Expression evaluates `True` -> Task runs
- Expression evaluates `False` -> Task skips

**Use Cases:**
- Check if preceding task result matches expectation
- Verify if file changed in recent commits
- Confirm image exists in registry
- Check if optional workspace is available

-> Lines 187-349: When expression with comprehensive example

**Related:** Understand finally tasks (Job 2.3), tasks (Job 2.1)

---

#### 2.3 Understand Finally Tasks for Cleanup
*For DevOps engineers ensuring cleanup and notifications*

**Objective:** Learn how finally tasks always run regardless of pipeline success or failure to ensure consistent cleanup and post-execution actions.

**Finally Tasks Characteristics:**

- **Always execute:** Run regardless of pipeline success/failure
- **Parallel execution:** All finally tasks run in parallel after pipeline tasks complete
- **Result consumption:** Can consume results from any pipeline task
- **Use cases:** Cleanup, notifications, logging

**Example Pattern:**
```yaml
spec:
  tasks:
    - name: clone-app-repo
      # ... task definition
  finally:
    - name: cleanup
      taskRef:
        name: cleanup-workspace
    - name: check-git-commit
      params:
        - name: commit
          value: $(tasks.clone-app-repo.results.commit)
```

-> Lines 358-428: Finally tasks with clone-cleanup-workspace example

**Related:** Understand when expressions (Job 2.2), tasks (Job 2.1)

---

#### 2.4 Understand Task Runs
*For DevOps engineers executing and debugging individual tasks*

**Objective:** Learn how TaskRun resources instantiate tasks with specific inputs, outputs, and execution parameters.

**TaskRun Fundamentals:**

- **Instantiation:** Creates task execution with specific parameters
- **Standalone or pipeline:** Can run independently or as part of pipeline
- **Step execution:** Runs task steps in order until success or failure
- **Automatic creation:** PipelineRun creates TaskRun for each pipeline task

**Example Structure:**
```yaml
apiVersion: tekton.dev/v1
kind: TaskRun
metadata:
  name: apply-manifests-taskrun
spec:
  taskRunTemplate:
    serviceAccountName: pipeline
  taskRef:
    kind: Task
    name: apply-manifests
  workspaces:
  - name: source
    persistentVolumeClaim:
      claimName: source-pvc
```

-> Lines 437-477: Task run

**Related:** Understand tasks (Job 2.1), pipeline runs (Job 2.6), workspaces (Job 2.8)

---

#### 2.5 Understand Pipeline Orchestration
*For DevOps engineers automating build, deployment, and delivery processes*

**Objective:** Learn how Pipelines orchestrate multiple tasks in specific execution order with shared resources.

**Pipeline Fundamentals:**

- **Task collection:** Arranges tasks in specific execution order
- **Complex workflows:** Automates build, deployment, delivery
- **Required components:** At least one Task resource
- **Optional components:** Conditions, Workspaces, Parameters, Resources

**Execution Control:**
- Use `runAfter` to define task dependencies
- Tasks without dependencies run in parallel
- Pipeline completes when all tasks succeed or one fails

**Example: build-and-deploy Pipeline**

**Tasks:**
1. `fetch-repository` - Clone Git repository
2. `build-image` - Build with Buildah (runs after fetch)
3. `apply-manifests` - Apply Kubernetes manifests (runs after build)
4. `update-deployment` - Update deployment (runs after apply)

-> Lines 486-611: Pipelines with complete build-and-deploy example

**Note:** Buildah task requires `pipeline` service account with proper permissions.

**Related:** Understand pipeline runs (Job 2.6), workspaces (Job 2.8), task runs (Job 2.4)

---

#### 2.6 Understand Pipeline Runs
*For DevOps engineers executing CI/CD workflows*

**Objective:** Learn how PipelineRun resources bind pipelines to workspaces, parameters, and credentials for specific scenarios.

**PipelineRun Fundamentals:**

- **Binding:** Connects pipeline with workspaces, credentials, parameters
- **Running instance:** Represents pipeline execution
- **Task run creation:** Creates TaskRun for each pipeline task
- **Status tracking:** Monitors progress for auditing

**Example Structure:**
```yaml
apiVersion: tekton.dev/v1
kind: PipelineRun
metadata:
  name: build-deploy-api-pipelinerun
spec:
  pipelineRef:
    name: build-and-deploy
  params:
  - name: deployment-name
    value: vote-api
  workspaces:
  - name: shared-workspace
    volumeClaimTemplate:
      spec:
        accessModes:
          - ReadWriteOnce
        resources:
          requests:
            storage: 500Mi
```

-> Lines 620-671: Pipeline run

**Related:** Understand pipelines (Job 2.5), workspaces (Job 2.8), task runs (Job 2.4)

---

#### 2.7 Understand Pod Templates for Security Configuration
*For platform engineers controlling pod-level execution parameters*

**Objective:** Learn how pod templates set security contexts, user IDs, and pod parameters for task execution.

**Pod Template Capabilities:**

- **Security contexts:** runAsNonRoot, runAsUser settings
- **Pod parameters:** Any `Pod` CR parameter available
- **Scope:** Applied to all pods created during pipeline/task run
- **Location:** 
  - PipelineRun: `taskRunTemplate.podTemplate`
  - TaskRun: `podTemplate`

**Example Use Case: Run as Non-Root**

**PipelineRun:**
```yaml
spec:
  taskRunTemplate:
    podTemplate:
      securityContext:
        runAsNonRoot: true
        runAsUser: 1001
```

**TaskRun:**
```yaml
spec:
  podTemplate:
    schedulerName: volcano
    securityContext:
      runAsNonRoot: true
      runAsUser: 1001
```

-> Lines 686-739: Pod templates

**Note:** In v1 API, PipelineRun uses `taskRunTemplate.podTemplate` (not direct `podTemplate` like v1beta1).

**Related:** Understand pipeline runs (Job 2.6), task runs (Job 2.4)

---

#### 2.8 Understand Workspaces for Data Sharing
*For DevOps engineers creating flexible and reusable pipeline components*

**Objective:** Learn how workspaces declare filesystem requirements at runtime without specifying storage implementation.

**Workspace Benefits:**

- **Separation of concerns:** Declare volume needs, specify storage at runtime
- **Task reusability:** Tasks work across different environments
- **Flexibility:** Change storage without rewriting tasks
- **Multiple uses:**
  - Store task inputs and outputs
  - Share data among tasks
  - Mount credentials from secrets
  - Mount configurations from config maps
  - Cache build artifacts

**Storage Options:**

| Option | Use Case | Lifecycle |
|--------|----------|-----------|
| Read-only config map/secret | Configuration, credentials | Persistent |
| Existing PVC | Shared data between runs | Persistent |
| PVC from volume claim template | Per-run isolated storage | Created on-demand |
| emptyDir | Temporary workspace | Discarded after run |

**Example: Shared Workspace Pattern**

**Pipeline declares workspace:**
```yaml
spec:
  workspaces:
  - name: shared-workspace
```

**Tasks use workspace:**
```yaml
tasks:
- name: build-image
  workspaces:
  - name: source
    workspace: shared-workspace
- name: apply-manifests
  workspaces:
  - name: source
    workspace: shared-workspace
```

**PipelineRun provides storage:**
```yaml
workspaces:
- name: shared-workspace
  volumeClaimTemplate:
    spec:
      resources:
        requests:
          storage: 500Mi
```

-> Lines 753-871: Workspaces with build-and-deploy example

**Note:** Workspaces replace deprecated PipelineResource CRs.

**Related:** Understand tasks (Job 2.1), pipelines (Job 2.5), pipeline runs (Job 2.6)

---

#### 2.9 Understand Step Actions for Reusability
*For DevOps engineers avoiding duplication across tasks*

**Objective:** Learn how StepAction resources define shareable actions that steps can reference.

**StepAction Fundamentals:**

- **Reusable actions:** Define step logic once, reference from multiple tasks
- **External sources:** Use resolvers to reference actions from external sources
- **Parameters and results:** StepAction defines params, step provides values
- **Workspace expectations:** Task provides mounted source tree (typically via workspace)

**Security Note:** StepAction does not support parameter values in `script` field. Use `env:` section for environment variables containing parameter values.

**Example Pattern:**

**StepAction definition:**
```yaml
apiVersion: tekton.dev/v1
kind: StepAction
metadata:
  name: apply-manifests-action
spec:
  params:
  - name: manifest_dir
  env:
  - name: MANIFEST_DIR
    value: $(params.manifest_dir)
  script: |
      oc apply -f "$MANIFEST_DIR"
```

**Task using StepAction:**
```yaml
steps:
- name: apply
  ref:
    name: apply-manifests-action
  params:
  - name: manifest_dir
    value: $(params.manifest_dir)
```

-> Lines 880-960: Step actions

**Related:** Understand tasks (Job 2.1)

---

## Understand Automation

### Job 3: Understand Triggers for Event-Driven Automation
*When implementing automated CI/CD workflows*

**Personas:** DevOps engineer

**Requires:**
- Understand pipelines (Job 2.5)
- Understand pipeline runs (Job 2.6)

**Objective:** Learn how Triggers capture external events (Git pull requests, webhooks) and automatically instantiate pipeline runs to create event-driven automation.

**Triggers Architecture:**

Triggers consist of four main components working together:

#### 3.1 TriggerBinding - Extract Event Data

**Purpose:** Extract fields from event payload and store as parameters.

**Example:**
```yaml
apiVersion: triggers.tekton.dev/v1
kind: TriggerBinding
metadata:
  name: vote-app
spec:
  params:
  - name: git-repo-url
    value: $(body.repository.url)
  - name: git-repo-name
    value: $(body.repository.name)
  - name: git-revision
    value: $(body.head_commit.id)
```

-> Lines 1002-1023: TriggerBinding

---

#### 3.2 TriggerTemplate - Create Pipeline Resources

**Purpose:** Define how parameterized data from TriggerBinding creates pipeline resources.

**Example:**
```yaml
apiVersion: triggers.tekton.dev/v1
kind: TriggerTemplate
metadata:
  name: vote-app
spec:
  params:
  - name: git-repo-url
  - name: git-revision
  - name: git-repo-name
  resourcetemplates:
  - apiVersion: tekton.dev/v1
    kind: PipelineRun
    metadata:
      name: build-deploy-$(tt.params.git-repo-name)-$(uid)
    spec:
      pipelineRef:
        name: build-and-deploy
      params:
      - name: git-url
        value: $(tt.params.git-repo-url)
```

-> Lines 1025-1082: TriggerTemplate

---

#### 3.3 Trigger - Connect Components with Interceptors

**Purpose:** Combine TriggerBinding and TriggerTemplate with optional event processing.

**Interceptor Capabilities:**
- Filter event payload
- Verify events using secrets
- Define and test trigger conditions
- Process events before TriggerBinding

**Example:**
```yaml
apiVersion: triggers.tekton.dev/v1
kind: Trigger
metadata:
  name: vote-trigger
spec:
  interceptors:
    - ref:
        name: "github"
      params:
        - name: "secretRef"
          value:
            secretName: github-secret
        - name: "eventTypes"
          value: ["push"]
  bindings:
    - ref: vote-app
  template:
     ref: vote-app
```

-> Lines 1084-1140: Trigger with GitHub interceptor

---

#### 3.4 EventListener - Provide Event Endpoint

**Purpose:** Provide HTTP endpoint that listens for events with JSON payload and triggers pipeline runs.

**Interceptor Types Supported:**
- Webhook Interceptors
- GitHub Interceptors
- GitLab Interceptors
- Bitbucket Interceptors
- Common Expression Language (CEL) Interceptors

**Example:**
```yaml
apiVersion: triggers.tekton.dev/v1
kind: EventListener
metadata:
  name: vote-app
spec:
  taskRunTemplate:
    serviceAccountName: pipeline
  triggers:
    - triggerRef: vote-trigger
```

-> Lines 1142-1173: EventListener

**Complete Flow:**
1. EventListener receives HTTP event
2. Interceptors process/filter event
3. TriggerBinding extracts parameters
4. TriggerTemplate creates PipelineRun
5. Pipeline executes with event data

**Related:** Understand pipelines (Job 2.5), pipeline runs (Job 2.6)

---

## Workflow Coverage

This guide covers **Get Started** phase exclusively:

| Phase | Jobs Covered | Coverage |
|-------|--------------|----------|
| **Get Started** | 3 main jobs, 10 user stories | ✓ Complete |
| Upgrade | - | Not applicable (conceptual guide) |
| Develop | - | See "Creating CI/CD pipelines" guide |
| Deploy | - | See "Creating CI/CD pipelines" guide |
| Observe | - | See "Observability in OpenShift Pipelines" guide |
| Secure | - | See "Securing OpenShift Pipelines" guide |

**Gaps Identified:**
- No procedural content (this is a reference guide)
- Implementation details in other guides (Creating pipelines, Observability, Security)

**Next Steps:**
- After understanding concepts (this guide), proceed to "Creating CI/CD solutions for applications using OpenShift Pipelines"
- For advanced topics: Pipelines as Code, Tekton Results, Tekton Chains

---

## Document Statistics

**Source:** `about-combined.adoc` (1,172 lines)

**Records:**
- Total JTBD records: 13
- Main jobs: 3
- User stories: 10
- Procedures: 0

**Personas:**
- Platform engineer: 4 records
- DevOps engineer: 9 records

**Job Types:**
- Core functional jobs: 13
- Related jobs: 0
- Consumption jobs: 0
- Emotional jobs: 0

**Coverage:**
- Assemblies: 2
  - About OpenShift Pipelines
  - Understanding OpenShift Pipelines
- Modules: 12 CONCEPT modules
- Line coverage: ~81% (950 content lines / 1,172 total)

---

## Additional Resources

**Related Documentation:**
- Installing OpenShift Pipelines
- Creating CI/CD solutions for applications using OpenShift Pipelines
- Pipelines as Code
- Using Tekton Results for observability
- Using Tekton Chains for supply chain security

**External Resources:**
- Tekton documentation
- Kubernetes pod documentation
- OpenShift routes documentation

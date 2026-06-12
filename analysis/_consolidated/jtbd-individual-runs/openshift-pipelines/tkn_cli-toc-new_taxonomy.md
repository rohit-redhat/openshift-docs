# Pipelines CLI (tkn) Reference
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** Enable CLI users to install, configure, and operate OpenShift Pipelines using the tkn command-line tool.

**Personas:** 
- OpenShift Pipelines user
- Linux/RHEL/Windows/macOS system administrator
- CLI user
- Pipeline operator
- Pipeline developer
- DevOps engineer
- Platform engineer

**Main Jobs:** 10 core jobs across 5 workflow stages (Get Started, Configure, Operate, Deploy, Monitor, Reference)

---

## Quick Navigation

**I want to:**
- Install the tkn CLI → Job 1 (Get Started)
- Enable command completion → Job 2 (Configure)
- Manage pipelines → Job 4 (Operate)
- Execute pipelines → Job 4 (Operate)
- Monitor pipeline runs → Job 5 (Monitor)
- Build reusable tasks → Job 6 (Operate)
- Test tasks independently → Job 7 (Operate)
- Configure pipeline inputs/outputs → Job 8 (Configure)
- Set up event-driven pipelines → Job 9 (Configure)
- Find tasks from Tekton Hub → Job 10 (Get Started)

---

# Table of Contents

## Getting Started with tkn

### Job 1: Install the tkn CLI Tool
*When I need to manage OpenShift Pipelines from a terminal*

**Personas:** OpenShift Pipelines user, Linux/RHEL/Windows/macOS system administrator
**Requires:** Platform-specific installation method knowledge

#### Installation Methods by Platform

**For Linux (tar.gz archive):**
- **When:** Using Linux distributions (x86_64, s390x, ppc64le, or arm64)
  → Lines 91-137: Installing the Red Hat OpenShift Pipelines CLI on Linux
  - Download platform-specific archive
  - Extract binaries
  - Add to PATH environment variable

**For Linux (RPM package):**
- **When:** Using RHEL 8 with system package management
  → Lines 140-230: Installing the Red Hat OpenShift Pipelines CLI on Linux using an RPM
  - Requires: Active OpenShift subscription, root/sudo privileges
  - Register with Red Hat Subscription Manager
  - Attach subscription pool
  - Enable architecture-specific repository
  - Install openshift-pipelines-client package

**For Windows (zip archive):**
- **When:** Using Windows terminal
  → Lines 233-265: Installing the Red Hat OpenShift Pipelines CLI on Windows
  - Download Windows CLI archive
  - Extract with ZIP program
  - Add to PATH environment variable

**For macOS (tar.gz archive):**
- **When:** Using macOS (Intel or Apple Silicon)
  → Lines 268-306: Installing the Red Hat OpenShift Pipelines CLI on macOS
  - Download architecture-specific archive (amd64 or arm64)
  - Extract binaries
  - Add to PATH environment variable

**Expected Outcomes:**
- tkn CLI installed on local system
- tkn command available in PATH
- Ability to execute tkn commands from terminal

---

### Job 3: Verify tkn Installation
*When I need to set up the tkn CLI for the first time*

**Personas:** Pipeline operator
**Prerequisites:** tkn CLI installed

#### Verification Steps

**Check CLI availability:**
→ Lines 400-431: Utility commands
- Run `tkn` to display all options
- Run `tkn version` to verify correct version
- Confirm installation is accessible

**Expected Outcomes:**
- Confirm tkn is installed and accessible
- Understand available tkn commands
- Verify correct version is installed

---

## Configure Your CLI Environment

### Job 2: Configure the tkn CLI for Optimal Usage
*When I need to work more efficiently with the tkn CLI*

**Personas:** CLI user
**Prerequisites:** tkn CLI installed
**Why:** Tab completion reduces typing errors and speeds up command execution

#### Configuration Options

**Enable tab completion (bash or zsh):**
→ Lines 329-363: Enabling tab completion
- Requires: bash-completion installed on local system
- **Task:** Save completion code
  - Run `tkn completion bash > tkn_bash_completion`
- **Task:** Install completion code
  - Option A: System-wide → Copy to `/etc/bash_completion.d/`
  - Option B: User-local → Source from `.bashrc`

**Generate completion code for interactive use:**
→ Lines 414-421: Utility commands (completion)
- Print completion code for bash or zsh
- Evaluate code for interactive completion

**Expected Outcomes:**
- CLI is configured for optimal usage
- Tab completion is enabled
- Command execution is more efficient
- Commands are automatically completed when pressing Tab

---

### Job 8: Configure Pipeline Inputs and Outputs
*When I need to configure pipeline resources*

**Personas:** Pipeline operator
**Prerequisites:** tkn CLI installed, Understanding of resource types, Access to namespace
**Note:** Pipeline resources define inputs/outputs like git repositories, images, and storage

#### Resource Management Tasks

**Create new pipeline resources:**
→ Lines 753-762: Pipeline resource management commands (resource create)
- Interactive command prompts for resource details
- Define resource type (git, image, storage)
- Configure resource values

**View available resources:**
→ Lines 782-789: Pipeline resource management commands (resource list)
- List all pipeline resources in namespace
- Identify resource names for pipeline use

**Inspect resource configuration:**
→ Lines 773-780: Pipeline resource management commands (resource describe)
- View resource details
- Understand resource type and values
- Verify resource setup

**Clean up obsolete resources:**
→ Lines 764-771: Pipeline resource management commands (resource delete)
- Delete specified resource by name
- Free resource definitions

**Expected Outcomes:**
- Create pipeline resources
- List available resources
- Inspect resource configurations
- Delete obsolete resources

---

### Job 9: Configure Event-Driven CI/CD
*When I am implementing event-driven pipeline automation*

**Personas:** DevOps engineer, Platform engineer
**Prerequisites:** tkn CLI installed, Tekton Triggers installed, Understanding of trigger concepts
**Why:** Webhooks and event listeners enable automated pipeline execution based on external events

#### Trigger Resource Management

**Set up event listeners (webhook endpoints):**
→ Lines 806-848: Trigger management commands (eventlistener)
- Create webhook endpoints
- List configured listeners
- View listener details
- Monitor incoming events with logs
- Delete obsolete listeners

**Configure trigger bindings (parameter mappings):**
→ Lines 850-883: Trigger management commands (triggerbinding)
- Define parameter mappings from webhook payload
- Extract event field data
- Bind event fields to pipeline parameters
- List and manage bindings

**Define trigger templates (pipeline/task creation):**
→ Lines 885-917: Trigger management commands (triggertemplate)
- Specify which pipelines or tasks to create
- Define resource creation logic
- List available templates
- View template details

**Manage cluster-wide bindings (for Platform Engineers):**
→ Lines 918-951: Trigger management commands (clustertriggerbinding)
- Define reusable parameter mappings cluster-wide
- Share bindings across all namespaces
- Requires: Cluster admin permissions

**Expected Outcomes:**
- Create and configure event listeners
- Define trigger bindings for event data
- Set up trigger templates
- Manage cluster-level triggers
- Enable webhook-based automation

---

## Operate & Manage Pipelines

### Job 4: Manage CI/CD Pipelines
*When I am managing CI/CD workflows*

**Personas:** Pipeline operator
**Prerequisites:** tkn CLI installed, OpenShift Pipelines installed, Cluster access configured
**Note:** Core operational job for pipeline lifecycle management

#### Pipeline Operations

**List available pipelines:**
→ Lines 475-482: Pipelines management commands (pipeline list)
- View all available pipelines
- Identify pipeline names for execution

**Inspect pipeline configuration:**
→ Lines 466-473: Pipelines management commands (pipeline describe)
- View complete pipeline definition
- Understand pipeline structure
- Review task composition
- Inspect parameters and workspaces

**Execute a pipeline:**
→ Lines 493-500: Pipelines management commands (pipeline start)
- Start a pipeline to create pipeline run
- Trigger automated workflows
- Begin CI/CD process
- Requires: Pipeline exists, Required resources configured

**Monitor pipeline execution:**
→ Lines 484-491: Pipelines management commands (pipeline logs)
- Stream live logs with `-f` flag
- Watch real-time execution progress
- Identify failures quickly
- Debug pipeline issues

**Clean up pipelines:**
→ Lines 456-464: Pipelines management commands (pipeline delete)
- Delete pipeline from namespace
- Remove obsolete or test pipelines
- Requires: Permission to delete pipelines

**Expected Outcomes:**
- Create and deploy pipelines
- List and inspect pipeline configurations
- Start pipeline executions
- Delete obsolete pipelines
- View pipeline execution logs

---

### Job 5: Manage Pipeline Executions
*When I am operating CI/CD pipeline runs*

**Personas:** Pipeline operator
**Prerequisites:** tkn CLI installed, Access to pipeline runs
**Note:** Pipeline runs are execution instances of pipeline definitions

#### Pipeline Run Operations

**List execution history:**
→ Lines 572-579: Pipeline run commands (pipelinerun list)
- View execution history
- Identify run status
- Find specific executions

**Inspect run details:**
→ Lines 563-570: Pipeline run commands (pipelinerun describe)
- View complete run status
- See task execution details
- Review parameters and results
- Identify failure points

**View execution logs:**
→ Lines 581-589: Pipeline run commands (pipelinerun logs)
- Display logs with all tasks and steps (use `-a` flag)
- Debug task failures
- Verify step outputs
- Audit execution activity

**Cancel running executions:**
→ Lines 527-534: Pipeline run commands (pipelinerun cancel)
- Stop running pipeline execution
- Free cluster resources
- Terminate failed or incorrect runs

**Clean up old executions:**
→ Lines 536-561: Pipeline run commands (pipelinerun delete)
- Delete specific runs by name
- Use `--keep N` to retain most recent runs
- Use `--all` to delete all completed runs
- Note: v1.6+ does not delete running executions

**Expected Outcomes:**
- List active and completed runs
- Inspect run details and status
- Cancel running executions
- Delete old or failed runs
- View execution logs

---

### Job 6: Build Reusable CI/CD Components
*When I am building reusable task definitions*

**Personas:** Pipeline developer
**Prerequisites:** tkn CLI installed, Access to namespace, Understanding of task concepts
**Note:** Tasks are reusable units of work within pipelines

#### Task Management Operations

**List available tasks:**
→ Lines 632-639: Task management commands (task list)
- View available task catalog
- Identify task names
- Find reusable components

**Inspect task specifications:**
→ Lines 623-630: Task management commands (task describe)
- View complete task definition
- Understand task steps
- Review parameters and inputs
- Inspect workspace requirements

**Test task independently:**
→ Lines 641-648: Task management commands (task start)
- Execute task standalone
- Validate task functionality
- Specify service account with `-s` flag
- Test task with parameters
- Verify task outputs

**Clean up unused tasks:**
→ Lines 614-621: Task management commands (task delete)
- Delete tasks from namespace
- Remove obsolete or test tasks
- Supports deleting multiple tasks in one command

**Expected Outcomes:**
- Create and deploy task definitions
- List available tasks
- Inspect task specifications
- Execute tasks for testing
- Remove obsolete tasks

---

### Job 7: Manage Task Executions
*When I am testing and troubleshooting tasks*

**Personas:** Pipeline developer
**Prerequisites:** tkn CLI installed, Access to task runs
**Note:** Task runs are execution instances of task definitions

#### Task Run Operations

**List task execution history:**
→ Lines 709-716: Task run commands (taskrun list)
- View execution history
- Identify run status
- Find specific executions

**Inspect task run details:**
→ Lines 700-707: Task run commands (taskrun describe)
- View complete run status
- See step execution details
- Review results and outputs
- Identify failure points

**Monitor task execution:**
→ Lines 719-727: Task run commands (taskrun logs)
- Display live logs with `-f` flag
- Watch real-time execution
- Debug step failures
- View output and errors

**Cancel running tasks:**
→ Lines 675-682: Task run commands (taskrun cancel)
- Stop running task execution
- Free cluster resources
- Terminate failed or incorrect runs

**Clean up test executions:**
→ Lines 684-698: Task run commands (taskrun delete)
- Delete specific runs by name
- Use `--keep N` to retain most recent runs
- Maintain clean execution history

**Expected Outcomes:**
- List task executions
- Inspect run details
- Cancel running tasks
- Delete old test runs
- View execution logs

---

## Discover & Install Resources

### Job 10: Discover and Install Tasks from Tekton Hub
*When I am building pipelines and need reusable community tasks*

**Personas:** Pipeline developer
**Prerequisites:** tkn CLI installed, Internet access to Tekton Hub, Understanding of task concepts
**Note:** Hub provides catalog of reusable Tekton resources

#### Hub Interaction Operations

**Search for tasks:**
→ Lines 1033-1040: Hub interaction commands (hub search)
- Find relevant tasks by name, kind, or tags
- Discover community resources
- Filter by categories
- Identify task candidates

**Review task details:**
→ Lines 1006-1013: Hub interaction commands (hub info)
- View task description
- Understand parameters
- See usage examples
- Check version information

**Get task manifest:**
→ Lines 997-1004: Hub interaction commands (hub get)
- Review task YAML definition
- Understand task implementation
- Verify task compatibility
- Assess task requirements

**Install task to cluster:**
→ Lines 1015-1022: Hub interaction commands (hub install)
- Deploy task to namespace
- Install specific version
- Make task available for pipelines
- Requires: Permission to create tasks

**Upgrade installed tasks:**
→ Lines 1042-1049: Hub interaction commands (hub upgrade)
- Update to newer version
- Get latest features
- Apply bug fixes

**Downgrade to previous version:**
→ Lines 988-995: Hub interaction commands (hub downgrade)
- Roll back to earlier version
- Fix breaking changes
- Restore stable functionality

**Reinstall tasks:**
→ Lines 1024-1031: Hub interaction commands (hub reinstall)
- Reset task to clean state
- Repair corrupted task
- Fix installation issues

**Expected Outcomes:**
- Search for reusable tasks
- Install tasks from catalog
- View task documentation
- Upgrade installed tasks
- Manage task versions

---

## Appendices

### A. Installation Method Comparison Matrix

| Platform | Method | Package Format | Prerequisites | Notes |
|----------|--------|----------------|---------------|-------|
| Linux (generic) | Archive | tar.gz | None | Supports x86_64, s390x, ppc64le, arm64 |
| RHEL 8 | Package Manager | RPM | Active subscription, root/sudo | Managed by yum/dnf |
| Windows | Archive | zip | ZIP extraction program | Simple installation |
| macOS | Archive | tar.gz | None | Supports Intel (amd64) and Apple Silicon (arm64) |

**Choose based on:**
- **Linux tar.gz:** Generic Linux distributions, no subscription required
- **RHEL RPM:** RHEL 8 systems, prefer package management, automated updates
- **Windows zip:** Windows systems, command prompt or PowerShell
- **macOS tar.gz:** macOS systems, both Intel and ARM architectures

---

### B. CLI Tools by Workflow

| Workflow | Primary Commands | Purpose |
|----------|-----------------|---------|
| Installation | Platform-specific installers | Install tkn binary |
| Configuration | `tkn completion` | Enable tab completion |
| Pipeline Lifecycle | `tkn pipeline` | Create, list, start, delete, describe, view logs |
| Pipeline Run Lifecycle | `tkn pipelinerun` | List, describe, cancel, delete, view logs |
| Task Development | `tkn task` | Create, list, start, delete, describe |
| Task Run Testing | `tkn taskrun` | List, describe, cancel, delete, view logs |
| Resource Configuration | `tkn resource` | Create, list, delete, describe |
| Event-Driven Automation | `tkn eventlistener`, `tkn triggerbinding`, `tkn triggertemplate`, `tkn clustertriggerbinding` | Configure webhooks and triggers |
| Hub Discovery | `tkn hub` | Search, install, upgrade, downgrade, get, info |

---

### C. Workflow Coverage Analysis

| Stage | Coverage | Jobs | Notes |
|-------|----------|------|-------|
| Get Started | ✅ | Jobs 1, 3, 10 | Installation, verification, hub discovery |
| Configure | ✅ | Jobs 2, 8, 9 | CLI configuration, pipeline resources, triggers |
| Operate | ✅ | Jobs 4, 5, 6, 7 | Manage pipelines, runs, tasks, task runs |
| Deploy | ✅ | Embedded in Jobs 4, 6 | Start pipelines, start tasks |
| Monitor | ✅ | Embedded in Jobs 5, 7 | View logs, describe runs |
| Reference | ✅ | All jobs | Command reference throughout |
| Troubleshoot | ⚠️ Limited | Via logs and describe commands | Basic troubleshooting with logs and status |
| Upgrade | ❌ | - | No tkn CLI upgrade content |
| Extend | ⚠️ Limited | Job 10 | Hub installation enables extension |

### Gaps Identified

| Stage | Gap | Recommendation |
|-------|-----|----------------|
| Upgrade | No tkn CLI upgrade procedures | Add section on upgrading tkn binary versions |
| Troubleshoot | Limited troubleshooting guidance | Add common error scenarios and resolutions |
| Administer | No cluster-level admin tasks | Consider adding operator installation prerequisites |

---

## Navigation Guide

### By User Journey

**New CLI User Journey (Getting Started):**
1. Job 1: Install the tkn CLI Tool
2. Job 3: Verify tkn Installation
3. Job 2: Configure the tkn CLI for Optimal Usage

**Pipeline Operator Journey (Managing Pipelines):**
1. Job 4: Manage CI/CD Pipelines (list, describe, start)
2. Job 5: Manage Pipeline Executions (monitor, logs, delete)

**Pipeline Developer Journey (Building Reusable Components):**
1. Job 10: Discover and Install Tasks from Tekton Hub (search, install)
2. Job 6: Build Reusable CI/CD Components (create, describe tasks)
3. Job 7: Manage Task Executions (test, debug, clean up)

**DevOps Engineer Journey (Event-Driven Pipelines):**
1. Job 9: Configure Event-Driven CI/CD (event listeners, bindings, templates)
2. Job 4: Manage CI/CD Pipelines (verify automated execution)

**Platform Engineer Journey (Infrastructure Setup):**
1. Job 1: Install the tkn CLI Tool (RPM method for RHEL)
2. Job 8: Configure Pipeline Inputs and Outputs (pipeline resources)
3. Job 9: Configure Event-Driven CI/CD (cluster trigger bindings)

---

## Document Statistics

**Workflow Coverage:**
- Get Started: 3 jobs
- Configure: 3 jobs
- Operate: 4 jobs
- Deploy: Embedded in Operate jobs
- Monitor: Embedded in Operate jobs
- Reference: Throughout all jobs
- Troubleshoot: Limited (via logs/describe)
- Upgrade: Gap identified
- Extend: Limited (via Hub)

**Main Jobs:** 10
**User Stories/Paths:** 39 user stories across all jobs
**Source Sections:** 49 total JTBD records
**Platform Variations:** 4 (Linux tar.gz, RHEL RPM, Windows, macOS)
**Trigger Resource Types:** 4 (EventListener, TriggerBinding, TriggerTemplate, ClusterTriggerBinding)
**Hub Operations:** 7 (search, info, get, install, reinstall, upgrade, downgrade)

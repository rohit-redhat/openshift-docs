# Pipelines CLI (tkn) Reference - TOC Comparison

**Current Feature-Based vs. Proposed JTBD-Based Structure**

**Analysis Date:** 2026-06-12
**JTBD Records:** 49 total records
**Main Jobs:** 10 (consolidated from user stories and procedures)
**Coverage:** Standard schema (no research extensions)

---

## Current Structure (Feature-Based)

Pipelines CLI (tkn) reference
  - Installing tkn
    - Installing the Red Hat OpenShift Pipelines CLI on Linux
    - Installing the Red Hat OpenShift Pipelines CLI on Linux using an RPM
    - Installing the Red Hat OpenShift Pipelines CLI on Windows
    - Installing the Red Hat OpenShift Pipelines CLI on macOS
  - Configuring tkn
    - Enabling tab completion
  - Basic tkn commands
    - Utility commands
    - Pipelines management commands
    - Pipeline run commands
    - Task management commands
    - Task run commands
    - Pipeline resource management commands
    - Trigger management commands
    - Hub interaction commands

---

## Proposed JTBD-Based Structure

### Getting Started with tkn

**Job 1: Install the tkn CLI Tool**
*When I need to manage OpenShift Pipelines from a terminal*

Personas: OpenShift Pipelines user, Linux/RHEL/Windows/macOS system administrator

Installation Methods by Platform:
- For Linux (tar.gz archive)
  → Lines 91-137: Installing the Red Hat OpenShift Pipelines CLI on Linux
  Source: Installing tkn assembly

- For Linux (RPM package)
  → Lines 140-230: Installing the Red Hat OpenShift Pipelines CLI on Linux using an RPM
  Source: Installing tkn assembly
  Requires: Active OpenShift subscription, root/sudo privileges

- For Windows (zip archive)
  → Lines 233-265: Installing the Red Hat OpenShift Pipelines CLI on Windows
  Source: Installing tkn assembly

- For macOS (tar.gz archive)
  → Lines 268-306: Installing the Red Hat OpenShift Pipelines CLI on macOS
  Source: Installing tkn assembly
  Supports: Intel (amd64) and Apple Silicon (arm64)

**Job 3: Verify tkn Installation**
*When I need to set up the tkn CLI for the first time*

Personas: Pipeline operator

Verification Steps:
- Check CLI availability and version
  → Lines 400-431: Utility commands
  Source: Basic tkn commands, Utility commands module

**Job 10: Discover and Install Tasks from Tekton Hub**
*When I am building pipelines and need reusable community tasks*

Personas: Pipeline developer

Hub Interaction Operations:
- Search for tasks
  → Lines 1033-1040: Hub interaction commands (hub search)

- Review task details
  → Lines 1006-1013: Hub interaction commands (hub info)

- Get task manifest
  → Lines 997-1004: Hub interaction commands (hub get)

- Install task to cluster
  → Lines 1015-1022: Hub interaction commands (hub install)

- Upgrade, downgrade, and reinstall tasks
  → Lines 988-995, 1024-1031, 1042-1049: Hub interaction commands
  Source: Basic tkn commands, Hub interaction commands module

---

### Configure Your CLI Environment

**Job 2: Configure the tkn CLI for Optimal Usage**
*When I need to work more efficiently with the tkn CLI*

Personas: CLI user

Configuration Options:
- Enable tab completion (bash or zsh)
  → Lines 329-363: Enabling tab completion
  Source: Configuring tkn assembly
  Requires: bash-completion installed on local system

- Generate completion code for interactive use
  → Lines 414-421: Utility commands (completion)
  Source: Basic tkn commands, Utility commands module

**Job 8: Configure Pipeline Inputs and Outputs**
*When I need to configure pipeline resources*

Personas: Pipeline operator

Resource Management Tasks:
- Create, list, describe, and delete pipeline resources
  → Lines 739-791: Pipeline resource management commands
  Source: Basic tkn commands, Pipeline resource management module

**Job 9: Configure Event-Driven CI/CD**
*When I am implementing event-driven pipeline automation*

Personas: DevOps engineer, Platform engineer

Trigger Resource Management:
- Set up event listeners (webhook endpoints)
  → Lines 806-848: Trigger management commands (eventlistener)
  Source: Basic tkn commands, Trigger management module

- Configure trigger bindings (parameter mappings)
  → Lines 850-883: Trigger management commands (triggerbinding)

- Define trigger templates (pipeline/task creation)
  → Lines 885-917: Trigger management commands (triggertemplate)

- Manage cluster-wide bindings
  → Lines 918-951: Trigger management commands (clustertriggerbinding)
  Requires: Cluster admin permissions

---

### Operate & Manage Pipelines

**Job 4: Manage CI/CD Pipelines**
*When I am managing CI/CD workflows*

Personas: Pipeline operator

Pipeline Operations:
- List, describe, start, monitor, and delete pipelines
  → Lines 442-502: Pipelines management commands
  Source: Basic tkn commands, Pipeline management module

**Job 5: Manage Pipeline Executions**
*When I am operating CI/CD pipeline runs*

Personas: Pipeline operator

Pipeline Run Operations:
- List, describe, view logs, cancel, and delete pipeline runs
  → Lines 512-590: Pipeline run commands
  Source: Basic tkn commands, Pipeline run module
  Note: v1.6+ does not delete running executions with `--all` flag

**Job 6: Build Reusable CI/CD Components**
*When I am building reusable task definitions*

Personas: Pipeline developer

Task Management Operations:
- List, describe, start, and delete tasks
  → Lines 600-650: Task management commands
  Source: Basic tkn commands, Task management module

**Job 7: Manage Task Executions**
*When I am testing and troubleshooting tasks*

Personas: Pipeline developer

Task Run Operations:
- List, describe, view logs, cancel, and delete task runs
  → Lines 661-729: Task run commands
  Source: Basic tkn commands, Task run module

---

## Key Differences

### Current Structure (Feature-Based)

**Organized By:** Installation methods, then command categories (utility, pipeline, task, resource, trigger, hub)
**Navigation:** 9 top-level sections
**User Journey:** Linear reading, starting with installation, then learning all command categories
**Format:** Reference-oriented, command-by-command documentation
**Persona Guidance:** Minimal, implied by installation platform

### Proposed Structure (JTBD-Based)

**Organized By:** User workflow stages (Getting Started, Configure, Operate), then job goals within each stage
**Navigation:** 10 main jobs organized by workflow stage
**User Journey:** Goal-directed, choose your job based on what you're trying to accomplish
**Format:** Outcome-oriented, organized by what users want to achieve
**Persona Guidance:** Explicit, showing which personas perform which jobs

---

## Hierarchy Levels Explanation

The proposed structure uses a 3-tier hierarchy:

### Level 1: Main Jobs (~10 total)
- Stable, outcome-focused goals that remain constant over time
- Organized by workflow stage (Get Started, Configure, Operate)
- Clean, professional titles using [Verb] + [Object] format
- Examples: "Install the tkn CLI Tool", "Manage CI/CD Pipelines"

### Level 2: User Stories (nested under main jobs)
- Persona-specific or platform-specific implementation paths
- Show different approaches to accomplish the main job
- Format: "For [Persona]: [Approach]" or "Option A/B/C"
- Examples: "For Linux (tar.gz archive)", "For RHEL (RPM package)"

### Level 3: Procedures (references to source)
- Line numbers and section names from evidence
- Brief descriptions of steps or commands
- Link to specific commands or procedures
- Examples: "→ Lines 442-502: Pipelines management commands"

---

## Example: Content Consolidation

### Example 1: Pipeline Resource Operations

**Current (Scattered):**
- Pipeline resource management commands
  - resource (help command)
  - resource create
  - resource delete
  - resource describe
  - resource list

**Proposed (Consolidated by Goal):**
Job 8: Configure Pipeline Inputs and Outputs
  - Create new pipeline resources
  - View available resources
  - Inspect resource configuration
  - Clean up obsolete resources

**Benefit:** One job consolidates all resource operations, organized by what users want to achieve (create, view, inspect, clean up) rather than listing individual commands.

---

### Example 2: Task and Task Run Operations

**Current (Separated):**
- Task management commands (task delete, describe, list, start)
- Task run commands (taskrun cancel, delete, describe, list, logs)

**Proposed (Consolidated by Workflow):**
Job 6: Build Reusable CI/CD Components
  - List, describe, start, delete tasks

Job 7: Manage Task Executions
  - List, describe, monitor, cancel, clean up task runs

**Benefit:** Separates task definition management (Job 6) from execution management (Job 7), matching the workflow of building components vs. testing and troubleshooting them.

---

### Example 3: Hub Operations Consolidation

**Current (Individual Commands):**
- hub (help)
- hub downgrade
- hub get
- hub info
- hub install
- hub reinstall
- hub search
- hub upgrade

**Proposed (Workflow-Oriented):**
Job 10: Discover and Install Tasks from Tekton Hub
  - Search for tasks
  - Review task details (info, get manifest)
  - Install task to cluster
  - Manage versions (upgrade, downgrade, reinstall)

**Benefit:** Organizes hub commands by discovery → evaluation → installation → version management workflow, rather than alphabetical command listing.

---

## Navigation Improvement Metrics

**Current Structure:**
- Browse 9 top-level sections to find content
- Linear navigation through command categories
- Must understand command structure (pipeline vs pipelinerun, task vs taskrun)

**Proposed Structure:**
- Navigate 10 main jobs organized by workflow stage
- Goal-directed navigation ("I want to install tkn" → Job 1)
- Persona paths shown within each job

**Reduction:** 10% fewer top-level navigation items (10 jobs vs 9 sections)
**Benefit:** 
- Find content in 2-3 clicks (workflow stage → job → persona path) vs. 3-5 clicks (installation/configuration/commands → category → specific command → scroll for options)
- Clear workflow progression (Get Started → Configure → Operate)
- Explicit persona guidance for platform-specific tasks

---

## Workflow Coverage Comparison

| Stage | Current | Proposed | Gap Status |
|-------|---------|----------|------------|
| Get Started | ✅ Installing tkn | ✅ Jobs 1, 3, 10 | Expanded with verification and hub discovery |
| Configure | ✅ Configuring tkn | ✅ Jobs 2, 8, 9 | Expanded with resources and triggers |
| Operate | ✅ Pipeline/Task commands | ✅ Jobs 4, 5, 6, 7 | Reorganized by operations vs. executions |
| Deploy | ⚠️ Embedded in commands | ✅ Embedded in Jobs 4, 6 | Made explicit (pipeline start, task start) |
| Monitor | ⚠️ Embedded in log commands | ✅ Embedded in Jobs 5, 7 | Made explicit (logs, describe) |
| Reference | ✅ All command sections | ✅ Throughout all jobs | Reorganized by workflow |
| Troubleshoot | ⚠️ Via logs/describe | ⚠️ Via logs/describe | Remains limited |
| Upgrade | ❌ Missing | ❌ Missing | Gap remains |
| Extend | ⚠️ Hub commands only | ⚠️ Job 10 | Remains limited to Hub operations |

### Coverage Summary

**Current structure strengths:**
- Comprehensive command reference
- Clear installation paths
- All command categories covered

**Current structure gaps:**
- No tkn CLI upgrade content
- Limited troubleshooting guidance
- Workflow progression not explicit

**Proposed structure improvements:**
- Explicit workflow progression (Get Started → Configure → Operate)
- Persona-specific guidance integrated
- Goal-oriented navigation (jobs match user intent)

**Proposed structure gaps (same as current):**
- No tkn CLI upgrade procedures
- Limited troubleshooting content
- No cluster-level admin prerequisites

### Recommendations for Gap Closure

| Gap | Recommendation | Priority |
|-----|----------------|----------|
| Upgrade | Add section on upgrading tkn binary versions | Medium |
| Troubleshoot | Add common error scenarios and resolutions | High |
| Administer | Add prerequisites section for operator installation | Low |
| Hub Extension | Add guidance on creating custom hub catalogs | Low |

---

## Document Statistics

### Current Structure
- Top-level sections: 9
- Command categories: 8 (utility, pipeline, pipelinerun, task, taskrun, resource, trigger, hub)
- Platform installation variations: 4 (Linux tar.gz, RHEL RPM, Windows, macOS)
- Total source sections: 49 (from JTBD analysis)

### Proposed Structure
- Main jobs: 10
- User stories/paths: 39 (persona/platform variations)
- Workflow stages covered: 6 (Get Started, Configure, Operate, Deploy, Monitor, Reference)
- Platform installation variations: 4 (same as current)
- Trigger resource types: 4 (EventListener, TriggerBinding, TriggerTemplate, ClusterTriggerBinding)
- Hub operations: 7 (search, info, get, install, reinstall, upgrade, downgrade)

### Consolidation Metrics
- Sections consolidated: 49 source sections → 10 main jobs
- Consolidation ratio: ~5:1 (5 user stories per main job on average)
- Workflow stages explicitly represented: 6

---

## Conclusion

The proposed JTBD-based structure reorganizes the tkn CLI reference from a command-centric reference to a goal-oriented workflow guide. Key improvements:

1. **Workflow Progression:** Clear Get Started → Configure → Operate flow
2. **Goal-Oriented Navigation:** Users navigate by job goals, not command categories
3. **Persona Integration:** Platform-specific and role-specific paths are explicit
4. **Consolidation:** Related operations grouped by user goals (e.g., all resource operations in one job)
5. **Workflow Visibility:** Deploy and Monitor stages made explicit (previously embedded in log/start commands)

The structure maintains all current content while reorganizing for improved discoverability and workflow alignment. Both structures share the same gaps (upgrade procedures, advanced troubleshooting), which should be addressed in future content development regardless of structure choice.

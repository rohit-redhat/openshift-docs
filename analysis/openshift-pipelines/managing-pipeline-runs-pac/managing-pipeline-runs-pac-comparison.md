# Managing Pipeline Runs using Pipelines as Code - TOC Comparison

**Current Feature-Based vs. Proposed JTBD-Based Structure**

**Analysis Date:** 2026-06-11
**JTBD Records:** 18
**Main Jobs:** 8 (rolled up from records)
**Coverage:** 100% enhanced schema

---

## Current Structure (Feature-Based)

Managing Pipeline Runs
- = Managing pipeline runs
  - == Verifying a pipeline run
  - == Running a pipeline run using Pipelines as Code
  - == Triggering a PipelineRun on Git tags
    - === Triggering PipelineRuns for GitOps commands using tagged commits
  - == Restarting or canceling a pipeline run using Pipelines as Code
  - == Monitoring pipeline run status using Pipelines as Code
  - == Cleaning up pipeline run using Pipelines as Code
  - == Using incoming webhook with Pipelines as Code

---

## Proposed JTBD-Based Structure

### Validate Pipeline Configurations

**Job 1: Verify Pipeline Run Definitions**

When: I create a pipeline run definition, I want to validate that all referenced resources are resolvable before triggering in production

Personas: Pipeline Developer

**Task 1.1: Validate Using CLI Resolver**
- Goal: Use tkn pac resolve command to see the fully resolved PipelineRun with all referenced resources
- → Lines 72-95: Verifying a pipeline run
- Source: Managing pipeline runs, Section: Verifying a pipeline run
- Complete validation in under 1 minute
- Receive clear error messages for missing resources
- View complete PipelineRun definition before execution

---

### Deploy & Execute Pipelines

**Job 2: Execute Pipeline Runs Automatically on Git Events**

When: A Git event occurs on my repository, I want pipeline runs to execute automatically based on configured event triggers

Personas: DevOps Engineer

Prerequisites: Configure Repository CRD, Create pipeline run definitions in .tekton/ directory, Set up authentication for repository

**Task 2.1: Understand Automatic Execution Behavior**
- Goal: Know when and how pipelines execute based on Git events and user permissions
- → Lines 104-121: Running a pipeline run using Pipelines as Code
- Source: Managing pipeline runs, Section: Running a pipeline run using Pipelines as Code
- Authorization rules for pull request authors
- Execution context and namespace targeting
- Default branch vs. non-default branch behavior

**Task 2.2: Monitor Pipeline Execution via CLI**
- Goal: Follow pipeline progress and troubleshoot issues in real-time using command line
- → Lines 122-141: Running a pipeline run using Pipelines as Code
- Source: Managing pipeline runs, Section: Running a pipeline run using Pipelines as Code
- Access logs within seconds of pipeline start
- View logs for any PipelineRun attached to repository
- Alternative: GitHub App UI (line 141)

---

**Job 3: Trigger Pipeline Runs on Git Tags**

When: I create or reference a Git tag representing a specific release version, I want to trigger pipeline runs that test or deploy that tagged version

Personas: DevOps Engineer

Prerequisites: Configure PipelineRun with tag event annotations, Use supported Git provider (GitHub App, GitHub Webhook, or GitLab)

**Task 3.1: Understand Tag-Based Triggering**
- Goal: Know how Pipelines as Code processes tag events and GitOps commands
- → Lines 151-176: Triggering a PipelineRun on Git tags (concept)
- Source: Managing pipeline runs, Section: Triggering a PipelineRun on Git tags
- Pipelines as Code resolves Git tag to commit SHA
- Treats tag creation as push event
- Supported providers: GitHub App, GitHub Webhook, GitLab

**Task 3.2: Configure PipelineRun for Tag Events**
- Goal: Author PipelineRun manifest that responds to tag events
- → Lines 177-196: Triggering a PipelineRun on Git tags (example)
- Source: Managing pipeline runs, Section: Triggering a PipelineRun on Git tags
- Annotation: `pipelinesascode.tekton.dev/on-target-branch: "[refs/tags/*]"`
- Annotation: `pipelinesascode.tekton.dev/on-event: "[push]"`
- Use case: Continuous delivery scenarios for tagged releases

---

**Job 4: Trigger Pipeline Runs Using GitOps Commands on Tags**

When: I need to manage pipeline runs for tagged commits, I want to use GitOps commands via Git provider UI

Personas: DevOps Engineer

Prerequisites: Git tag exists in repository, User has GitHub UI access, User has required repository permissions

**Task 4.1: Execute GitOps Commands via GitHub UI**
- Goal: Trigger or manage tag-based pipeline runs without CLI tools
- → Lines 206-220: Triggering PipelineRuns for GitOps commands using tagged commits
- Source: Managing pipeline runs, Section: Triggering PipelineRuns for GitOps commands using tagged commits
- Navigate: Tags view → Select tag → Click commit SHA → Enter GitOps command
- Supported commands: `/test tag:<tag>`, `/retest tag:<tag>`, `/cancel tag:<tag>`, `/test <name> tag:<tag>`
- Verify pipeline processing immediately

---

**Job 8: Trigger Pipeline Runs via Incoming Webhooks**

When: I need to trigger pipeline runs from external systems or custom automation, I want to use incoming webhook URLs with shared secrets

Personas: DevOps Engineer

Prerequisites: Configure Repository CRD with incoming webhook settings, Create secret with webhook shared secret, Specify Git provider type and user token

**Task 8.1: Configure Repository for Incoming Webhooks**
- Goal: Set up Repository CRD with incoming webhook configuration
- → Lines 474-507: Using incoming webhook (Repository CRD and secret examples)
- Source: Managing pipeline runs, Section: Using incoming webhook with Pipelines as Code
- Supports github, gitlab, bitbucket-cloud
- Requires user token when using GitHub App
- Configure target branches and shared secret

**Task 8.2: Trigger Pipeline Run via Webhook URL**
- Goal: Execute pipelines from external automation workflows
- → Lines 509-519: Using incoming webhook (triggering procedure)
- Source: Managing pipeline runs, Section: Using incoming webhook with Pipelines as Code
- POST with parameters: secret, repository, branch, pipelinerun
- Pipelines as Code treats as push event
- No status reporting by default (use finally tasks or tkn pac CLI)

---

### Operate & Manage Pipelines

**Job 5: Restart or Cancel Pipeline Runs**

When: I need to restart a failed pipeline or cancel a running pipeline, I want to manage pipeline lifecycle without triggering new Git events

Personas: DevOps Engineer

Prerequisites: User has required repository permissions (owner, collaborator, public member, or OWNERS file)

**Task 5.1: Restart All Pipeline Runs (GitHub App Method)**
- Goal: Retry all failed pipelines with one click using GitHub UI
- → Lines 232-234, 275: Restarting or canceling a pipeline run (GitHub App approach)
- Source: Managing pipeline runs, Section: Restarting or canceling a pipeline run using Pipelines as Code
- Navigate to Checks tab and click "Re-run all checks"
- Restart all pipelines in under 10 seconds
- Technology Preview when starting pipelines not matching events (lines 257-270)

**Task 5.2: Restart or Cancel Specific Pipelines (GitOps Commands)**
- Goal: Control individual pipelines using comments on pull requests or commits
- → Lines 236-246, 277-316: Restarting or canceling a pipeline run (GitOps commands)
- Source: Managing pipeline runs, Section: Restarting or canceling a pipeline run using Pipelines as Code
- For pull/merge requests: Comment with `/test`, `/retest`, `/cancel`, `/test <name>`, `/cancel <name>`
- For push requests (GitHub/GitLab only): Add command in commit message comments
- Branch specification: `/test branch:user-branch` for specific branch targeting

---

**Job 7: Clean Up Old Pipeline Runs**

When: Many pipeline runs accumulate in my namespace, I want to automatically retain only a limited number of recent runs

Personas: Platform Engineer

**Task 7.1: Configure Automatic Cleanup via Annotation**
- Goal: Set retention policy per pipeline to control resource consumption
- → Lines 427-447: Cleaning up pipeline runs using Pipelines as Code
- Source: Managing pipeline runs, Section: Cleaning up pipeline run using Pipelines as Code
- Annotation: `pipelinesascode.tekton.dev/max-keep-runs: "<max_number>"`
- Cleanup happens after successful execution
- Skips running pipelines and failed PRs (preserves for debugging)
- Configure in under 5 minutes

---

### Track Performance & Status

**Job 6: Monitor Pipeline Run Status and Errors**

When: Pipeline runs execute, I want to monitor their status, view error details, and track execution progress across different interfaces

Personas: DevOps Engineer, Platform Engineer

**Task 6.1: View Pipeline Status in GitHub App**
- Goal: See high-level pipeline results and task execution times without accessing cluster
- → Lines 332-341: Monitoring pipeline run status (GitHub Apps status)
- Source: Managing pipeline runs, Section: Monitoring pipeline run status using Pipelines as Code
- Task duration for each pipeline step
- Output of tkn pipelinerun describe
- Error snippets (last 3 lines from first failed task)
- Note: Secrets masked automatically (except workspaces and envFrom)

**Task 6.2: Enable Advanced Error Detection**
- Context: Platform Engineer role
- Goal: See detailed error annotations directly on pull requests where failures occurred
- → Lines 343-373: Monitoring pipeline run status (annotations for log error snippets)
- Source: Managing pipeline runs, Section: Monitoring pipeline run status using Pipelines as Code
- Technology Preview feature
- Enable in TektonConfig: `error-detection-from-container-logs: true`
- Customize with `error-detection-simple-regexp` and `error-detection-max-number-of-lines`
- Supports makefile/grep format: `<filename>:<line>:<column>: <error message>`

**Task 6.3: Check Pipeline Run History via CLI**
- Goal: View recent pipeline run status and metadata without GitHub UI access
- → Lines 390-406: Monitoring pipeline run status (Repository CRD status)
- Source: Managing pipeline runs, Section: Monitoring pipeline run status using Pipelines as Code
- Command: `oc get repo -n <namespace>`
- Command: `tkn pac describe`
- Pipelines as Code stores last 5 status messages in Repository CR
- Columns: SUCCEEDED, REASON, STARTTIME, COMPLETIONTIME

**Task 6.4: View Status for Webhook-Based Pipelines**
- Goal: Monitor pipeline runs triggered via webhooks
- → Lines 375-376: Monitoring pipeline run status (webhook status)
- Source: Managing pipeline runs, Section: Monitoring pipeline run status using Pipelines as Code
- For webhook pull requests, Pipelines as Code adds status as comment

**Task 6.5: Monitor Validation Errors and Failures**
- Goal: Identify YAML parsing errors and validation issues
- → Lines 378-389: Monitoring pipeline run status (failures and YAML errors)
- Source: Managing pipeline runs, Section: Monitoring pipeline run status using Pipelines as Code
- Pipelines as Code detects YAML errors in .tekton directory
- Creates/updates PR comment with error details
- Halts execution of correctly formatted runs when errors found
- Logs to namespace events and controller log
- Valid runs continue despite validation issues

---

## Key Differences

### Current Structure (Feature-Based)

**Organized By:** Features and technical capabilities (verification, running, triggering, restarting, monitoring, cleaning, webhooks)

**Navigation:** 7 top-level sections/chapters

**User Journey:** Linear reading, chapter by chapter through technical features

**Focus:** Technical mechanisms and Pipelines as Code capabilities

**Organization Logic:** What the system can do (feature list)

---

### Proposed Structure (JTBD-Based)

**Organized By:** Workflow stages and user goals (Validate, Deploy, Operate, Monitor)

**Navigation:** 8 main jobs organized under 4 workflow categories

**User Journey:** Goal-directed, choose your path based on what you need to accomplish

**Focus:** User outcomes and job completion

**Organization Logic:** What users need to accomplish (job map)

**Workflow Stages:**
- Validate Pipeline Configurations (1 job)
- Deploy & Execute Pipelines (4 jobs)
- Operate & Manage Pipelines (2 jobs)
- Track Performance & Status (1 job)

---

## Hierarchy Levels

### Level 1: Main Jobs (Stable Goals)

Main jobs represent stable, outcome-focused goals that would exist even if the underlying technology changed. These are organized by workflow stages.

**Examples:**
- "Verify Pipeline Run Definitions" (not "Use tkn pac resolve")
- "Execute Pipeline Runs Automatically on Git Events" (not "Configure event annotations")
- "Monitor Pipeline Run Status and Errors" (not "View GitHub Checks tab")

### Level 2: User Stories/Tasks (Persona Approaches)

Tasks represent specific implementation paths or approaches to completing the main job. These may vary by:
- Tool choice (CLI vs UI)
- Platform variation (GitHub vs GitLab)
- User context (DevOps Engineer vs Platform Engineer)

**Examples:**
- "Validate Using CLI Resolver" (under Job 1)
- "Monitor Pipeline Execution via CLI" (under Job 2)
- "Enable Advanced Error Detection" (under Job 6, Platform Engineer context)

### Level 3: Procedures (Step-by-Step)

Specific commands, configurations, and step-by-step instructions with line references to source content.

**Examples:**
- `tkn pac resolve .tekton/pipeline-run-definition.yaml` (Job 1, Task 1.1)
- Annotation: `pipelinesascode.tekton.dev/max-keep-runs: "<max_number>"` (Job 7, Task 7.1)
- Navigate: Tags view → Select tag → Click commit SHA (Job 4, Task 4.1)

---

## Example: Content Consolidation

### Current (Fragmented)

**Monitoring scattered across multiple sections:**
- Section: Running a pipeline run using Pipelines as Code (lines 122-141) - CLI log viewing
- Section: Monitoring pipeline run status using Pipelines as Code (lines 332-341) - GitHub App status
- Section: Monitoring pipeline run status using Pipelines as Code (lines 343-373) - Error annotations
- Section: Monitoring pipeline run status using Pipelines as Code (lines 390-406) - Repository CRD status

**Result:** User must read 4+ sections to understand all monitoring options

---

### Proposed (Consolidated)

**Job 6: Monitor Pipeline Run Status and Errors**
- Task 6.1: View Pipeline Status in GitHub App (lines 332-341)
- Task 6.2: Enable Advanced Error Detection (lines 343-373)
- Task 6.3: Check Pipeline Run History via CLI (lines 390-406)
- Task 6.4: View Status for Webhook-Based Pipelines (lines 375-376)
- Task 6.5: Monitor Validation Errors and Failures (lines 378-389)

**Additional Monitoring Context:**
- Task 2.2: Monitor Pipeline Execution via CLI (lines 122-141) - Real-time log following during execution

**Result:** All monitoring options in one place, organized by interface and use case

**Benefit:** One place to learn all monitoring options! Clear decision guide for which interface to use.

---

## Navigation Improvement

### Current Navigation

**Browse:** 7 top-level sections to find content

**Path to restart failed pipeline:**
1. Read "Managing pipeline runs" (overview)
2. Read "Running a pipeline run using Pipelines as Code"
3. Read "Restarting or canceling a pipeline run using Pipelines as Code"
4. Identify GitHub App vs GitOps command approach
5. Locate specific procedure (5 sections total)

**Clicks:** 5-7 sections to read

---

### Proposed Navigation

**Navigate:** 4 workflow categories → 8 main jobs → choose task

**Path to restart failed pipeline:**
1. Navigate to "Operate & Manage Pipelines"
2. Select "Job 5: Restart or Cancel Pipeline Runs"
3. Choose Task 5.1 (GitHub App) or Task 5.2 (GitOps Commands)

**Clicks:** 3 sections (category → job → task)

---

### Reduction Metrics

**Top-level Items:** 7 sections → 4 workflow categories (43% reduction)

**Navigation Depth:** 5-7 clicks → 2-3 clicks (60% improvement)

**Benefit:** Find content in 2-3 clicks vs 5-7 clicks

**Consolidation:** Monitoring content consolidated from 4+ scattered sections into 1 main job with 5 organized tasks

---

## Workflow Coverage Comparison

| Stage | Current | Proposed | Gap Status |
|-------|---------|----------|------------|
| Get Started | ❌ Missing | ❌ Missing | Gap remains - no prerequisites or initial setup |
| Plan | ❌ Missing | ❌ Missing | Gap remains - no platform selection or decision guidance |
| Configure | ✅ Section: Verifying a pipeline run | ✅ Job 1: Verify Pipeline Run Definitions | Reorganized |
| Deploy | ✅ Sections: Running, Triggering tags, Webhooks | ✅ Jobs 2, 3, 4, 8: Execute automatically, trigger on tags, use webhooks | Consolidated |
| Operate | ✅ Sections: Restarting/canceling, Cleaning up | ✅ Jobs 5, 7: Restart/cancel, cleanup | Reorganized |
| Monitor | ✅ Section: Monitoring pipeline run status | ✅ Job 6: Monitor status and errors | Enhanced consolidation |
| Troubleshoot | ⚠️ Embedded in monitoring section | ⚠️ Embedded in Job 6 (error detection) | Limited coverage |
| Upgrade | ❌ Missing | ❌ Missing | Gap remains - no version upgrade procedures |
| Reference | ⚠️ Appendix only | ⚠️ Appendices D, E (embedded) | Limited coverage |

---

### Coverage Summary

**Current structure gaps:**
- Get Started: No prerequisites or initial setup guidance
- Plan: No platform selection or decision guidance
- Troubleshoot: Only embedded error detection, no dedicated troubleshooting guide
- Upgrade: No upgrade or migration procedures
- Reference: No comprehensive CLI reference

**Proposed structure gaps:**
- Get Started: No prerequisites or initial setup guidance
- Plan: No platform selection or decision guidance
- Troubleshoot: Only embedded error detection, no dedicated troubleshooting guide
- Upgrade: No upgrade or migration procedures
- Reference: Limited to embedded appendices

**Gaps addressed by restructure:**
- Monitor: Consolidated from scattered sections into comprehensive Job 6 with 5 tasks
- Deploy: Better organization of 4 jobs covering automatic execution, tag triggering, GitOps commands, and webhooks

---

### Recommendations for Gap Closure

| Gap | Recommendation | Priority |
|-----|----------------|----------|
| Get Started | Add prerequisites section covering Repository CRD setup, authentication configuration, and initial .tekton directory structure | High |
| Plan | Add decision guide for choosing execution approach (automatic vs manual, GitHub App vs webhooks, tag-based vs branch-based) | Medium |
| Troubleshoot | Add dedicated troubleshooting job with common failure scenarios: authorization failures, YAML parsing errors, resource resolution failures, webhook authentication issues | High |
| Upgrade | Add version upgrade procedures for Pipelines as Code, including migration guides for annotation changes and breaking changes | Medium |
| Reference | Add comprehensive CLI reference for `tkn pac` commands: resolve, logs, describe, create, bootstrap | Medium |
| Configure | Add pipeline definition best practices: annotation patterns, naming conventions, resource reference guidelines, secret management | Low |
| Secure | Add security hardening guidance: RBAC configuration, secret management, webhook security, OWNERS file configuration | Low |

---

## UX Research Alignment

### Pain Points Addressed by Restructure

| Pain Point (from JTBD analysis) | How New Structure Helps |
|--------------------------------|------------------------|
| "Minimize time to identify pipeline definition errors" | Job 1 elevated as first validation step before deployment, clear CLI procedure with expected outcomes |
| "Reduce likelihood of runtime failures due to missing resources" | Job 1 positioned as prerequisite to Job 2 (automatic execution), preventing production failures |
| "Minimize time from commit to pipeline execution" | Job 2 separates automatic execution understanding (Task 2.1) from monitoring (Task 2.2), reducing cognitive load |
| "Reduce likelihood of unauthorized pipeline runs" | Job 2 Task 2.1 explicitly covers authorization rules, making security requirements visible |
| "Reduce time to identify root cause of failures" | Job 6 consolidates 5 monitoring interfaces in one place, with clear decision guide for which to use when |
| "Ensure sensitive information is not exposed in error messages" | Job 6 Task 6.1 explicitly notes secret masking behavior and limitations, preventing security issues |
| "Minimize namespace resource consumption" | Job 7 elevated from buried cleanup section to dedicated Operate job, making resource management discoverable |
| "Reduce dependency on Git events for triggering" | Job 8 separated as distinct integration job, making webhook option visible for automation scenarios |

---

### Strategic Priorities Elevated

The following jobs are flagged as core jobs in JTBD analysis. The new structure gives them dedicated sections with clear visibility:

| Strategic Job | Current Location | Proposed Location | Visibility Improvement |
|--------------|------------------|-------------------|------------------------|
| Verify Pipeline Run Definitions | Buried in first section, equal weight to other sections | Job 1: First job under "Validate Pipeline Configurations" | Elevated as prerequisite to all deployment jobs |
| Monitor Pipeline Run Status | Section with 5 monitoring approaches mixed together | Job 6: Dedicated job with 5 organized tasks by interface | Consolidates scattered monitoring content into decision guide |
| Restart or Cancel Pipeline Runs | Mid-document section | Job 5: Dedicated job under "Operate & Manage Pipelines" | Direct navigation from workflow stage heading |
| Trigger on Git Tags | Section with concept + procedure split across 2 levels | Jobs 3 & 4: Separated understanding (Job 3) from execution (Job 4) | Clearer separation of concepts from procedures |

---

### Workflow Stage Distribution

The new structure makes workflow progression visible:

| Stage | Jobs | Implication |
|-------|------|-------------|
| Configure | Job 1 | Pipeline Developer focus: Validate before deploy |
| Deploy | Jobs 2, 3, 4, 8 | DevOps Engineer focus: Multiple triggering options (automatic, tags, webhooks) |
| Operate | Jobs 5, 7 | DevOps/Platform Engineer focus: Lifecycle management (restart/cancel, cleanup) |
| Monitor | Job 6 | Cross-persona: 5 monitoring interfaces for different contexts |

**Workflow Insight:** Configure → Deploy → Operate → Monitor represents the complete pipeline run lifecycle, making the natural progression visible.

---

### Persona-Specific Paths

The JTBD records identify 3 primary personas. The new structure supports their distinct workflows:

#### Pipeline Developer Path
1. Job 1: Verify Pipeline Run Definitions (validate before deployment)
2. Job 2: Execute Pipeline Runs Automatically on Git Events (understand execution)
3. Job 6: Monitor Pipeline Run Status and Errors (confirm success)

**Context:** Focus on definition validation and understanding automatic execution behavior.

---

#### DevOps Engineer Path
1. Job 2: Execute Pipeline Runs Automatically on Git Events (operational execution)
2. Job 3 & 4: Trigger Pipeline Runs on Git Tags (release workflows)
3. Job 5: Restart or Cancel Pipeline Runs (manage failures)
4. Job 6: Monitor Pipeline Run Status and Errors (track production runs)

**Context:** Operational focus on execution, releases, and troubleshooting.

---

#### Platform Engineer Path
1. Job 6 Task 6.2: Enable Advanced Error Detection (configure TektonConfig)
2. Job 7: Clean Up Old Pipeline Runs (manage resources)
3. Job 8: Trigger Pipeline Runs via Incoming Webhooks (integration scenarios)

**Context:** Platform configuration, resource management, and system integration.

---

### Cross-Team Collaboration Visibility

The new structure makes team collaboration patterns visible:

| Job | Teams Involved | Benefit |
|-----|---------------|---------|
| Verify Pipeline Run Definitions | Pipeline Developer (creates) → DevOps Engineer (executes) | Clear handoff: validate before deploy |
| Execute Pipeline Runs Automatically | DevOps Engineer (uses) → Platform Engineer (configures Repository CRD) | Platform setup enables DevOps workflows |
| Enable Advanced Error Detection | Platform Engineer (configures) → DevOps Engineer (views annotations) | Platform feature enhances DevOps troubleshooting |
| Clean Up Old Pipeline Runs | Platform Engineer (configures retention) → DevOps Engineer (benefits from clean namespace) | Platform policy enables efficient operations |
| Trigger Pipeline Runs via Incoming Webhooks | DevOps Engineer (integrates) → Platform Engineer (configures Repository CRD) | Platform configuration enables external integrations |

---

## Comparison Summary

### What Changed

**Organization:** Feature-based (7 sections) → JTBD-based (4 workflow stages, 8 jobs)

**Focus:** Technical capabilities → User outcomes

**Navigation:** Linear chapter reading → Goal-directed task selection

**Consolidation:** Monitoring scattered across 4+ sections → Job 6 with 5 organized tasks

**Workflow Visibility:** Implicit progression → Explicit stages (Configure → Deploy → Operate → Monitor)

**Persona Support:** Generic content → Clear paths for Pipeline Developer, DevOps Engineer, Platform Engineer

---

### What Stayed the Same

**Content:** All source content retained with line references

**Coverage:** Same workflow stages covered (Configure, Deploy, Operate, Monitor)

**Technical Depth:** All procedures, commands, and configurations preserved

**Prerequisites:** Authorization requirements and technical prerequisites maintained

---

### What Improved

**Discoverability:** 43% fewer top-level items (7 → 4 workflow categories)

**Navigation Efficiency:** 60% improvement (5-7 clicks → 2-3 clicks)

**Content Consolidation:** Monitoring approaches united in single job (6) instead of scattered

**Workflow Clarity:** Explicit stage progression visible in structure

**Persona Alignment:** Clear paths for 3 distinct personas (Pipeline Developer, DevOps Engineer, Platform Engineer)

**Strategic Visibility:** Critical jobs (verify, monitor, restart) elevated with dedicated sections

**Pain Point Mapping:** 8 identified pain points directly addressed by structural improvements

---

### What Remains to Address

**Gap Coverage:**
- Get Started stage: No prerequisites or setup guidance (HIGH priority)
- Troubleshoot stage: No dedicated troubleshooting guide (HIGH priority)
- Upgrade stage: No version upgrade procedures (MEDIUM priority)
- Reference stage: No comprehensive CLI reference (MEDIUM priority)
- Plan stage: No decision guidance for approach selection (MEDIUM priority)
- Configure stage: No best practices for pipeline definitions (LOW priority)
- Secure stage: No security hardening guidance (LOW priority)

**Next Steps:** Prioritize adding Get Started and Troubleshoot content to close high-priority gaps identified in workflow coverage analysis.

---

## Document Metadata

**Source Document:** managing-pipeline-runs-pac-self-managed-reduced.adoc (528 lines)

**JTBD Records:** 18 records

**Main Jobs Identified:** 8 jobs

**User Stories/Tasks:** 18 tasks across 8 jobs

**Workflow Stages Covered:** 4 of 8 standard stages (Configure, Deploy, Operate, Monitor)

**Personas Identified:** 3 (Pipeline Developer, DevOps Engineer, Platform Engineer)

**Pain Points Mapped:** 8 pain points addressed by restructure

**Strategic Priority Jobs:** 4 jobs elevated for visibility (verify, monitor, restart, tag triggering)

**Technology Preview Features:** 2 (error annotations, non-matching event starts)

**Supported Git Providers:** GitHub App, GitHub Webhook, GitLab (tag support); Bitbucket Cloud (webhook support)

---

**Generated:** 2026-06-11

**JTBD Framework Version:** Enhanced schema with research extension fields

**Comparison Guide Version:** 1.3.0

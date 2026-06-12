# Pipelines as Code
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** Enable platform teams and developers to implement GitOps-driven CI/CD pipelines that automatically trigger from Git events, manage pipeline definitions as code, and integrate seamlessly with GitHub, GitLab, and Bitbucket repositories.

**Personas:** 
- Platform Administrator
- DevOps Engineer
- Application Developer

**Main Jobs:** 18 core jobs across 8 workflow stages

---

## Quick Navigation

**I want to:**
- Understand what Pipelines as Code offers -> Job 1 (Getting Started)
- Install PaC on my OpenShift cluster -> Job 2 (Installation & Setup)
- Set up GitHub App integration -> Job 4 (GitHub Integration)
- Configure GitLab or Bitbucket integration -> Jobs 8-10 (Git Provider Integration)
- Connect my Git repository to PaC -> Job 5 (Repository Configuration)
- Create pipeline runs that trigger on Git events -> Job 11 (Creating Pipeline Runs)
- Use remote tasks from Tekton Hub -> Job 13 (Pipeline Definition)
- Control when pipelines run (events, paths, labels) -> Job 14 (Event Management)
- Run pipelines on Git tags -> Job 15 (Tag-Based Pipelines)
- Restart or cancel a running pipeline -> Job 16 (Pipeline Control)
- Monitor pipeline execution and status -> Job 17 (Monitoring)
- Use tkn pac CLI commands -> Job 18 (Command Line Tools)

---

# Table of Contents

## Getting Started

### Job 1: Understand Pipelines as Code Capabilities
*When I need to implement GitOps-driven CI/CD for my applications*

**Personas:** Platform Administrator, DevOps Engineer

**Why:** Understanding PaC's architecture and key features helps determine if it meets automation requirements and supports your Git provider

#### 1.1 Evaluate Core Concepts
**Goal:** Understand how PaC implements GitOps for Tekton pipelines.

- **Task:** Review PaC architecture and workflow
  → Lines 59-69: About Pipelines as Code
  - GitOps-driven pipeline execution
  - Pipeline definitions stored in Git
  - Automatic triggering on Git events

- **Task:** Understand Repository CR and .tekton directory structure
  → Lines 91-118: Pipelines as Code concepts
  - Repository CR connects Git repos to namespaces
  - .tekton directory stores pipeline run definitions
  - PaC resolver fetches and processes pipeline files

#### 1.2 Review Key Features
**Goal:** Assess whether PaC supports required CI/CD workflow requirements.

- **Task:** Evaluate feature capabilities
  → Lines 70-84: Key features
  - Pull request status checks
  - Automatic task resolution from remote sources
  - Git event filtering and matching
  - Support for GitHub, GitLab, Bitbucket

---

## Installation & Setup

### Job 2: Install Pipelines as Code
*When I need to enable Pipelines as Code functionality on my OpenShift cluster*

**Personas:** Platform Administrator

**Requires:** 
- OpenShift Pipelines Operator installed
- Cluster administrator access

**Timing:** BEFORE Job 3 (Customize Configuration) - PaC must be installed first

#### 2.1 Install via OpenShift Pipelines Operator
**Goal:** Deploy PaC in the openshift-pipelines namespace.

- **Task:** Install using default TektonConfig settings
  → Lines 196-234: Installing Pipelines as Code
  - PaC installed automatically by default
  - Deployed in openshift-pipelines namespace

- **Alternative:** Disable default installation
  → Lines 204-234: Installing Pipelines as Code
  - Set `enable: false` in TektonConfig for controlled deployment

#### 2.2 Install PaC CLI Tool
**Goal:** Enable local management and repository bootstrapping.

- **Task:** Install tkn pac CLI for your platform
  → Lines 276-334: Installing Pipelines as Code CLI
  - Download from OpenShift Pipelines downloads page
  - Available for Linux, macOS, Windows
  - Required for bootstrap and management operations

---

### Job 3: Customize Pipelines as Code Configuration
*When I need to adjust PaC settings for organizational policies and requirements*

**Personas:** Platform Administrator

**Requires:** PaC installed on cluster

#### 3.1 Configure Core PaC Settings
**Goal:** Customize PaC behavior through TektonConfig parameters.

- **Task:** Configure application name, remote tasks, and webhook behavior
  → Lines 342-397: Customizing Pipelines as Code configuration
  - Set application name for status reporting
  - Enable/disable remote task resolution
  - Configure hub catalog URL
  - Adjust error detection settings

#### 3.2 Configure Additional PaC Controllers (Advanced)
**Goal:** Support multiple GitHub Apps or GitHub instances.

- **Task:** Deploy additional PaC controller instances
  → Lines 406-442: Configuring additional PaC controllers
  - Create separate controller for each GitHub organization
  - Configure independent GitHub App per controller
  - Create dedicated secrets for each instance

---

## GitHub Integration

### Job 4: Configure GitHub App Integration
*When I need to integrate Pipelines as Code with GitHub repositories*

**Personas:** Platform Administrator

**Requires:**
- tkn pac CLI installed (for automated method)
- Cluster administrator access
- GitHub account with app creation permissions

#### 4.1 For Automated Setup: Use CLI Bootstrap
**Goal:** Minimize manual configuration steps with automated GitHub App creation.

- **Task:** Run tkn pac bootstrap command
  → Lines 570-612: Configure a GitHub App using CLI
  - Interactive CLI wizard creates GitHub App
  - Automatically configures webhook and permissions
  - Stores credentials in cluster secret

#### 4.2 For Web Console Setup: Use Administrator Perspective
**Goal:** Set up GitHub App integration through guided UI.

- **Task:** Create GitHub App via OpenShift web console
  → Lines 621-657: Create GitHub App in administrator perspective
  - Navigate to Pipelines > Pipelines as Code
  - Click Setup GitHub App
  - Follow wizard to complete configuration

#### 4.3 For Advanced Scenarios: Manual Configuration
**Goal:** Enable fine-grained control for additional controllers or GitHub Enterprise.

- **Task:** Create GitHub App manually with custom settings
  → Lines 666-767: Configure GitHub App manually
  - Register new GitHub App with specific permissions
  - Generate and store webhook secret
  - Create Kubernetes secret with app credentials
  - Install app on target repositories

---

## Repository Configuration

### Job 5: Create Repository Custom Resource
*When I want to connect a Git repository to Pipelines as Code*

**Personas:** Application Developer, Platform Administrator

**Requires:**
- PaC configured for Git provider (GitHub App, webhook, etc.)
- Target namespace created

**Why:** Repository CR enables PaC to match Git events to the correct namespace and process pipeline definitions

#### 5.1 Define Basic Repository CR
**Goal:** Connect a Git repository to a specific namespace.

- **Task:** Create Repository CR manifest
  → Lines 1911-1939: Creating Repository CR
  - Specify Git repository URL
  - Map to target namespace
  - Reference Git provider credentials

#### 5.2 Configure Global Repository Defaults (Optional)
**Goal:** Apply common configuration across all repositories.

- **Task:** Create global Repository CR in openshift-pipelines namespace
  → Lines 1948-2000: Creating global Repository CR
  - Technology Preview feature
  - Define default Git provider settings
  - Set common secrets and parameters

---

### Job 6: Configure Repository Settings
*When I need to control pipeline execution behavior and security*

**Personas:** Platform Administrator, Application Developer

**Requires:** Repository CR created

#### 6.1 Set Concurrency Limits
**Goal:** Prevent excessive resource consumption from simultaneous pipeline runs.

- **Task:** Configure concurrency limits in Repository CR
  → Lines 2008-2031: Setting concurrency limits
  - Limit concurrent pipeline runs per repository
  - Queue additional runs automatically
  - Prevent cluster resource exhaustion

#### 6.2 Configure Pipeline Provenance (Security)
**Goal:** Ensure only reviewed pipeline definitions execute.

- **Task:** Set pipelinerun_provenance to use default branch
  → Lines 2040-2064: Changing source branch
  - Prevents malicious pipeline definitions from executing
  - Enforces review process for pipeline changes
  - Uses main/default branch pipeline definitions

#### 6.3 Define Custom Parameters (Optional)
**Goal:** Pass administrator-managed values without modifying pipeline definitions.

- **Task:** Configure custom parameter expansion
  → Lines 2073-2140: Custom parameter expansion
  - Inject environment-specific values
  - Support different configurations per environment
  - Centralize configuration management

---

### Job 7: Configure Token Scoping for Multi-Repository Access
*When my pipeline needs to access multiple repositories*

**Personas:** DevOps Engineer, Application Developer

**Requires:**
- GitHub App configured
- Repository CR created

**Why:** Enables fetching tasks or code from private repositories outside the main repository

#### 7.1 Configure Repository-Level Token Scoping
**Goal:** Grant access to additional repositories for a specific Repository CR.

- **Task:** Add extra-permissions annotation to Repository CR
  → Lines 776-865: Scope GitHub token to additional repositories
  - Use `pipelinesascode.tekton.dev/extra-permissions` annotation
  - Specify repositories and organizations
  - Enable access to private remote tasks

#### 7.2 Configure Global Token Scoping (Advanced)
**Goal:** Apply token scoping across all repositories.

- **Task:** Set global scoping in TektonConfig
  → Lines 866-895: Global token scoping
  - Configure secret scanning settings
  - Apply scoping to all Repository CRs
  - Centralize cross-repository access

---

## Git Provider Integration

### Job 8: Integrate with GitHub Webhooks (Alternative Method)
*When I cannot create a GitHub App*

**Personas:** Platform Administrator

**Requires:**
- PaC installed
- GitHub personal access token

**Why:** Provides PaC integration when GitHub App creation is not available

- **Task:** Configure GitHub webhook integration
  → Lines 904-1132: Use PaC with GitHub Webhook
  - Create webhook in GitHub repository settings
  - Store personal access token in secret
  - Configure Repository CR with webhook details
  - Enable pipeline status reporting

---

### Job 9: Integrate with GitLab
*When my organization uses GitLab*

**Personas:** Platform Administrator

**Requires:**
- PaC installed
- GitLab personal access token

- **Task:** Configure GitLab webhook integration
  → Lines 1141-1339: Use PaC with GitLab
  - Create webhook in GitLab project settings
  - Store access token in secret
  - Configure Repository CR for GitLab
  - Enable merge request status reporting

---

### Job 10: Integrate with Bitbucket
*When my organization uses Bitbucket Cloud or Bitbucket Data Center*

**Personas:** Platform Administrator

**Requires:**
- PaC installed
- Bitbucket app password or personal access token

#### 10.1 For Bitbucket Cloud
**Goal:** Enable PaC integration with Bitbucket Cloud repositories.

- **Task:** Configure Bitbucket Cloud webhook
  → Lines 1348-1588: Use PaC with Bitbucket Cloud
  - Create webhook in Bitbucket repository
  - Store app password in secret
  - Configure Repository CR for Bitbucket Cloud
  - Enable pull request status reporting

#### 10.2 For Bitbucket Data Center (Self-Hosted)
**Goal:** Enable PaC integration with self-hosted Bitbucket repositories.

- **Task:** Configure Bitbucket Data Center webhook
  → Lines 1598-1738: Use PaC with Bitbucket Data Center
  - Create webhook in Bitbucket repository
  - Store personal access token in secret
  - Configure Repository CR for Bitbucket Data Center
  - Enable pull request status reporting

---

### Job 11: Configure Custom Certificates
*When my Git repository uses custom certificates*

**Personas:** Platform Administrator

**Requires:** OpenShift Pipelines Operator installed

**Why:** Enables PaC to connect to privately signed or self-hosted Git providers

- **Task:** Configure PaC to trust custom certificates
  → Lines 1747-1758: Configure custom certificates
  - Add custom CA certificates
  - Configure cluster proxy settings
  - Ensure secure communication with private Git servers

---

## Creating Pipeline Runs

### Job 12: Create Pipeline Run Definitions
*When I need to create pipeline runs triggered by Git events*

**Personas:** Application Developer

**Requires:**
- PaC configured with Git provider
- Repository CR created
- .tekton directory in repository

**Why:** Enables automated CI/CD workflow execution in response to Git events

#### 12.1 Define Core Pipeline Run Structure
**Goal:** Create pipeline run definitions in .tekton directory.

- **Task:** Author pipeline run YAML files
  → Lines 2216-2377: Creating a pipeline run
  - Define pipeline tasks
  - Configure workspaces and volumes
  - Specify parameters and resources

- **Task:** Configure automatic Git authentication for private repos
  → Lines 1767-1821: Private repository support
  - PaC automatically creates git-clone secrets
  - Reference git_auth_secret in pipeline runs
  - Enable seamless private repository access

---

### Job 13: Use Dynamic Variables and Remote Tasks
*When I need reusable pipeline definitions*

**Personas:** Application Developer

**Requires:** Pipeline run definition created

#### 13.1 Use Dynamic Variables
**Goal:** Create context-aware, reusable pipeline definitions.

- **Task:** Reference dynamic variables for commit and repository information
  → Lines 2387-2454: Dynamic variables
  - Use `{{repo_url}}` for repository URL
  - Use `{{revision}}` for commit SHA
  - Use `{{git_auth_secret}}` for authentication
  - Enable template-based pipeline definitions

#### 13.2 Reference Remote Tasks with PaC Resolver
**Goal:** Avoid duplicating task definitions across repositories.

- **Task:** Use PaC resolver annotations to reference remote tasks
  → Lines 2463-2644: PaC resolver annotations
  - Reference tasks from Tekton Hub
  - Reference tasks from HTTP URLs
  - Reference tasks from other Git repositories
  - Use local task files in .tekton directory

#### 13.3 Verify Pipeline Run Configuration (Before Commit)
**Goal:** Catch errors before committing to Git.

- **Task:** Test pipeline run locally with tkn pac resolve
  → Lines 3130-3153: Verifying a pipeline run
  - Verify resolver processes definitions correctly
  - Test dynamic variable substitution
  - Catch missing task references early

---

## Event Management

### Job 14: Control Pipeline Execution with Event Matching
*When I need to control when each pipeline run executes*

**Personas:** Application Developer

**Requires:** Pipeline run definition created

**Why:** Ensures pipelines run only for relevant events and minimize unnecessary executions

#### 14.1 Match Git Events with Annotations
**Goal:** Configure pipeline runs to trigger on specific Git events.

- **Task:** Add event matching annotations
  → Lines 2653-2870: Annotations for matching events
  - Match pull request events with `on-event`
  - Match push events to specific branches
  - Match comment events (e.g., `/test`, `/retest`)
  - Use CEL expressions for advanced matching

#### 14.2 Filter Events by Changed Files or Labels
**Goal:** Avoid running pipelines for irrelevant changes.

- **Task:** Add filtering annotations
  → Lines 2879-2983: Annotations for filtering events
  - Filter by changed file paths
  - Exclude specific paths
  - Filter by pull request labels
  - Reduce unnecessary pipeline runs

#### 14.3 Enable Automatic Cancellation (Technology Preview)
**Goal:** Prevent excessive resource consumption from rapid commits.

- **Task:** Configure automatic cancellation of older runs
  → Lines 2992-3044: Annotations for cancellation-in-progress
  - Cancel previous runs when new commit arrives
  - Ensure latest commits are tested first
  - Reduce pipeline run queue length

---

### Job 15: Trigger Pipeline Runs on Git Tags
*When I create or reference a Git tag for a release*

**Personas:** DevOps Engineer

**Requires:**
- Pipeline run configured for tag events
- GitHub App or GitLab webhook configured

**Why:** Enables version-based testing and deployment for release workflows

- **Task:** Configure tag event triggering
  → Lines 3209-3279: Triggering PipelineRun on Git tags
  - Use tag event annotations
  - Trigger on tag creation or reference
  - Support release and versioning workflows
  - Use GitOps commands on tagged commits

---

## Pipeline Execution & Control

### Job 16: Manage Pipeline Run Lifecycle
*When I need to retry failed pipelines or cancel running pipelines*

**Personas:** Application Developer

**Requires:**
- Pipeline run exists
- Appropriate repository permissions

**Why:** Enables pipeline control without requiring new commits

#### 16.1 Run Pipelines Automatically
**Goal:** Execute CI/CD workflows without manual intervention.

- **Task:** Trigger pipeline runs from Git events
  → Lines 3162-3200: Running a pipeline run
  - Automatic triggering on matched events
  - No manual intervention required
  - Continuous integration execution

#### 16.2 Restart or Cancel Pipelines
**Goal:** Control pipeline execution through comments or GitHub App features.

- **Task:** Use GitOps commands to manage pipeline runs
  → Lines 3287-3375: Restarting or canceling pipeline run
  - Use `/retest` comment to restart
  - Use `/cancel` comment to cancel
  - Use GitHub App "Re-run all checks" feature
  - Enable quick pipeline retries without new commits

#### 16.3 Trigger Pipelines Programmatically (Advanced)
**Goal:** Integrate PaC with external systems.

- **Task:** Use incoming webhooks with shared secret
  → Lines 3515-3577: Using incoming webhook
  - Configure Repository CR with incoming webhook
  - Call webhook URL from external systems
  - Enable programmatic triggering
  - Ensure secure webhook access

---

## Monitoring & Operations

### Job 17: Monitor Pipeline Run Status
*When pipeline runs execute*

**Personas:** Application Developer, DevOps Engineer

**Requires:** Pipeline run created and running

**Why:** Enables quick identification of failures and progress tracking

#### 17.1 View Status Across Multiple Channels
**Goal:** Track pipeline execution through various interfaces.

- **Task:** Monitor pipeline run status
  → Lines 3384-3468: Monitoring pipeline run status
  - View status in GitHub Checks tab
  - Review log error snippets in PR comments
  - Check Repository CR status field
  - Review Kubernetes events for detailed logs

#### 17.2 Clean Up Pipeline Runs
**Goal:** Manage storage and keep namespace tidy.

- **Task:** Configure automatic cleanup policy
  → Lines 3485-3506: Cleaning up pipeline runs
  - Use `pipelinesascode.tekton.dev/max-keep-runs` annotation
  - Set retention limits per pipeline
  - Automatically delete old runs
  - Reduce storage usage

---

## Command Line Tools

### Job 18: Use Pipelines as Code CLI
*When I need to manage Pipelines as Code from the command line*

**Personas:** DevOps Engineer, Platform Administrator

**Requires:** tkn pac CLI installed

**Why:** Enables scripting, automation, and quick access to PaC functions

#### 18.1 Perform Common CLI Operations
**Goal:** Execute PaC operations from command line.

- **Task:** Use tkn pac commands
  → Lines 3660-3904: PaC command reference
  - `tkn pac bootstrap` - Set up GitHub App
  - `tkn pac create repository` - Create Repository CR
  - `tkn pac resolve` - Verify pipeline runs locally
  - `tkn pac list` - List repositories
  - `tkn pac logs` - View pipeline run logs

#### 18.2 Troubleshoot with Logging Configuration (Advanced)
**Goal:** Get detailed diagnostic information for troubleshooting.

- **Task:** Configure PaC logging levels
  → Lines 3914-4061: Configuring PaC logging
  - Adjust log levels via TektonConfig CR
  - Configure component-specific logging
  - Review PaC controller logs
  - Filter logs by namespace
  → Lines 4070-4082: Splitting logs by namespace

---

## Appendices

### A. Git Provider Comparison Matrix

| Provider | Integration Method | Required Credentials | Status Reporting | Notes |
|----------|-------------------|---------------------|------------------|-------|
| GitHub | GitHub App (recommended) | App ID, App Private Key, Webhook Secret | GitHub Checks | Full feature support |
| GitHub | Webhook | Personal Access Token, Webhook Secret | Commit status | Alternative when App not available |
| GitLab | Webhook | Personal Access Token | Merge Request status | Webhook-based integration |
| Bitbucket Cloud | Webhook | App Password | Pull Request status | Cloud-hosted only |
| Bitbucket Data Center | Webhook | Personal Access Token | Pull Request status | Self-hosted instances |

### B. Integration Method Decision Guide

**Choose GitHub App when:**
- You have permissions to create GitHub Apps
- You want the best user experience (GitHub Checks tab)
- You need fine-grained repository permissions
- You're setting up new repositories

**Choose Webhook integration when:**
- You cannot create a GitHub App
- You're using GitLab or Bitbucket
- You need simpler setup for testing
- You have limited GitHub permissions

### C. Event Matching Quick Reference

| Annotation | Purpose | Example |
|------------|---------|---------|
| `pipelinesascode.tekton.dev/on-event` | Match Git events | `"[pull_request, push]"` |
| `pipelinesascode.tekton.dev/on-target-branch` | Filter by branch | `"[main, release-*]"` |
| `pipelinesascode.tekton.dev/on-cel-expression` | Advanced matching | CEL expression |
| `pipelinesascode.tekton.dev/task-**` | Reference remote tasks | URL or Tekton Hub reference |
| `pipelinesascode.tekton.dev/max-keep-runs` | Retention policy | `"5"` |

### D. Workflow Coverage Analysis

| Stage | Coverage | Jobs | Notes |
|-------|----------|------|-------|
| Get Started | ✅ | Job 1 | Core concepts and capabilities |
| Configure | ✅ | Jobs 2-3, 5-7, 11 | Installation, Git providers, Repository CR |
| Secure | ✅ | Jobs 6.2, 7, 11 | Pipeline provenance, token scoping, certificates |
| Deploy | ✅ | Jobs 12-15 | Pipeline run creation, events, tags |
| Monitor | ✅ | Job 17 | Pipeline status tracking |
| Operate | ✅ | Jobs 6.1, 16, 17.2 | Concurrency, lifecycle, cleanup |
| Troubleshoot | ✅ | Job 18.2 | Logging configuration |
| Reference | ✅ | Job 18 | CLI commands |

**Gaps Identified:** None - All major workflow stages are covered.

---

## Navigation Guide

### By User Journey

**Platform Administrator getting started:**
1. Job 1: Understand Pipelines as Code capabilities
2. Job 2: Install Pipelines as Code
3. Job 3: Customize PaC configuration
4. Job 4: Configure GitHub App integration
5. Job 5: Create Repository CR for first repository

**Platform Administrator integrating GitLab:**
1. Job 1: Understand Pipelines as Code capabilities
2. Job 2: Install Pipelines as Code
3. Job 9: Integrate with GitLab
4. Job 5: Create Repository CR

**Application Developer creating pipelines:**
1. Job 12: Create pipeline run definitions
2. Job 13: Use dynamic variables and remote tasks
3. Job 14: Control pipeline execution with event matching
4. Job 16: Run pipelines automatically
5. Job 17: Monitor pipeline run status

**DevOps Engineer managing releases:**
1. Job 15: Trigger pipeline runs on Git tags
2. Job 16: Manage pipeline run lifecycle
3. Job 17: Monitor pipeline run status
4. Job 18: Use PaC CLI for automation

**Platform Administrator securing pipelines:**
1. Job 6.2: Configure pipeline provenance
2. Job 7: Configure token scoping
3. Job 11: Configure custom certificates
4. Job 6.1: Set concurrency limits

---

## Document Statistics

**Workflow Coverage:**
- Get Started: 1 job
- Installation & Setup: 2 jobs
- GitHub Integration: 1 job (with 3 approaches)
- Repository Configuration: 3 jobs
- Git Provider Integration: 4 jobs
- Creating Pipeline Runs: 2 jobs
- Event Management: 2 jobs
- Pipeline Execution & Control: 1 job (with 3 approaches)
- Monitoring & Operations: 1 job
- Command Line Tools: 1 job

**Main Jobs:** 18
**User Stories/Themed Sections:** 39
**Source Line References:** 37 distinct sections
**Git Provider Variations:** 5 (GitHub App, GitHub Webhook, GitLab, Bitbucket Cloud, Bitbucket Data Center)

---

*Generated from JTBD analysis of pac-combined.adoc*

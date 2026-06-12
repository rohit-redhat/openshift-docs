# Remote Pipelines, Tasks, and Resolvers
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** Help users retrieve and reference remote pipeline resources from catalogs, registries, Git repositories, and cluster namespaces using Tekton resolvers.

**Personas:** Developer, Platform Administrator, CI/CD Engineer

**Main Jobs:** 12 core jobs across 5 workflow stages (Define, Configure, Execute, Reference, Plan)

---

## Quick Navigation

**I want to:**
- Understand how resolvers work → Job 1 (Define)
- Use public catalog tasks → Job 2 (Configure - Hub resolver)
- Use OCI bundle tasks → Job 3 (Configure - Bundles resolver)
- Use tasks from public Git repos → Job 4 (Configure - Git anonymous)
- Use tasks from private Git repos → Job 5 (Configure - Git authenticated)
- Use tasks from web servers → Job 6 (Configure - HTTP resolver)
- Use tasks from other namespaces → Job 7 (Configure - Cluster resolver)
- Access standard OpenShift Pipelines tasks → Job 8 (Reference)
- Access community integration tasks → Job 9 (Reference)
- Use reusable step actions → Job 10 (Reference)
- Choose task versioning strategy → Job 11 (Plan)

---

# Table of Contents

## Understand Resolvers

### Job 1: Understand How Resolvers Retrieve Remote Resources
*When building CI/CD pipelines, I want to understand how resolvers retrieve remote pipeline and task definitions, so I can reuse existing pipelines and tasks without copying their definitions.*

**Personas:** Developer

→ Lines 62-81: Specifying remote pipelines, tasks, and step actions using resolvers  
Source: Introduction

**Why:** Minimize duplication of pipeline and task definitions, ensure ability to reuse from multiple sources

**Core concepts covered:**
- What resolvers are and why they matter
- Five resolver types: Hub, Bundles, Git, HTTP, Cluster
- How resolvers integrate with pipelineRef, taskRef, and step.ref
- Benefits of remote resource reuse

---

## Configure Resolvers

### Job 2: Configure Hub Resolver for Public Catalogs
*When creating pipelines, I want to fetch pipeline and task definitions from public catalogs like Artifact Hub or Tekton Hub, so I can leverage community-maintained resources without reinventing solutions.*

**Personas:** Platform Administrator (configure), Developer (use)

**Timing:** Configure BEFORE Job 8 (Use standard tasks) - resolvers must be enabled

#### 2.1 Understand Hub Resolver Capabilities

→ Lines 89-104: About Hub resolver  
Source: Section on Hub resolver

**Key capabilities:**
- Access Artifact Hub (recommended) or Tekton Hub catalogs
- Reference tasks by catalog name, type, and version
- Support for self-hosted catalog instances

#### 2.2 Configure Hub Resolver Settings

→ Lines 114-161: Configuring the hub resolver  
Source: Hub resolver configuration section

**Configuration tasks:**
- **Task:** Set default catalog type (artifact or tekton)
- **Task:** Specify default Tekton Hub catalog name
- **Task:** Specify default Artifact Hub catalog name  
- **Task:** Configure Artifact Hub API endpoint
- **Task:** Configure Tekton Hub API endpoint (for self-hosted instances)

**Configuration location:** TektonConfig custom resource under `pipeline.hub-resolver-config`

#### 2.3 Reference Catalog Resources in Pipelines

→ Lines 170-338: Specifying using hub resolver  
Source: Hub resolver usage examples

**For PipelineRuns:**
- **Task:** Reference pipeline with `resolver: hub`
- **Task:** Specify catalog, type (artifact/tekton), kind, name, version parameters

**For TaskRuns:**
- **Task:** Reference task with `resolver: hub`
- **Task:** Specify catalog, kind, name, version

**For Step Actions:**
- **Task:** Reference step action in task definition with `resolver: hub`

---

### Job 3: Configure Bundles Resolver for OCI Registries
*When managing pipeline resources, I want to fetch pipeline and task definitions from OCI bundles stored in container registries, so I can version and distribute resources using existing registry infrastructure.*

**Personas:** Platform Administrator (configure), CI/CD Engineer (publish bundles), Developer (use)

**Requires:** OCI-compatible registry, service account with registry pull credentials

#### 3.1 Understand Bundles Resolver Capabilities

→ Lines 347-352: About Bundles resolver  
Source: Bundles resolver introduction

**Key capabilities:**
- Fetch resources from OCI images (bundles)
- Reuse existing registry infrastructure and authentication
- Version resources alongside container images

#### 3.2 Configure Bundles Resolver Settings

→ Lines 361-392: Configuring the bundles resolver  
Source: Bundles resolver configuration section

**Configuration tasks:**
- **Task:** Set default service account for registry authentication
- **Task:** Set default resource kind (Task or Pipeline)
- **Task:** Configure service account with registry pull secrets

**Configuration location:** TektonConfig custom resource under `pipeline.bundles-resolver-config`

#### 3.3 Reference OCI Bundle Resources in Pipelines

→ Lines 401-546: Specifying using bundles resolver  
Source: Bundles resolver usage examples

**For PipelineRuns:**
- **Task:** Reference pipeline with `resolver: bundles`
- **Task:** Specify bundle (fully qualified image name), name, kind parameters
- **Task:** Override service account if needed

**For TaskRuns:**
- **Task:** Reference task with `resolver: bundles`
- **Task:** Specify bundle, name, kind

**For Step Actions:**
- **Task:** Reference step action with `resolver: bundles`

---

### Job 4: Configure Git Resolver for Anonymous Access
*When fetching resources from Git, I want to use anonymous cloning to retrieve pipeline and task definitions from public repositories, so I can use open-source resources without managing credentials.*

**Personas:** Platform Administrator (configure), Developer (use)

**Requires:** Access to public Git repository containing YAML pipeline/task definitions

#### 4.1 Understand Git Resolver (Anonymous) Capabilities

→ Lines 555-560: About Git resolver with anonymous cloning  
Source: Git anonymous resolver introduction

**Key capabilities:**
- Clone from public Git repositories without authentication
- Reference specific branches, tags, or commit SHAs
- Pin to specific file paths within repository

#### 4.2 Configure Git Resolver for Anonymous Access

→ Lines 569-601: Configuring the Git resolver for anonymous cloning  
Source: Git anonymous resolver configuration section

**Configuration tasks:**
- **Task:** Set default repository URL
- **Task:** Set default revision (branch/tag)
- **Task:** Configure fetch timeout (max 1 minute)

**Configuration location:** TektonConfig custom resource under `pipeline.git-resolver-config`

#### 4.3 Reference Git Resources Using Anonymous Cloning

→ Lines 610-756: Specifying using Git resolver for anonymous cloning  
Source: Git anonymous resolver usage examples

**For PipelineRuns:**
- **Task:** Reference pipeline with `resolver: git`
- **Task:** Specify url, revision (branch/tag/SHA), pathInRepo parameters

**For TaskRuns:**
- **Task:** Reference task with `resolver: git`
- **Task:** Specify repository location and file path

**For Step Actions:**
- **Task:** Reference step action with `resolver: git`

**Important:** Cannot use `url` and `repo` parameters together

---

### Job 5: Configure Git Resolver for Authenticated SCM APIs
*When accessing private Git repositories, I want to use authenticated SCM APIs to fetch pipeline and task definitions, so I can use organization-internal resources securely.*

**Personas:** Platform Administrator (configure), CI/CD Engineer (use private resources)

**Requires:** SCM API token with read permissions, access to private Git repository

**Why:** Minimize exposure of internal pipeline definitions, ensure secure credential management

#### 5.1 Understand Git Resolver (Authenticated) Capabilities

→ Lines 765-770: About Git resolver with authenticated SCM API  
Source: Git authenticated resolver introduction

**Key capabilities:**
- Access private repositories using SCM provider APIs
- Support GitHub, GitLab, Gitea, Bitbucket
- Secure token-based authentication

#### 5.2 Configure Single Git Provider

→ Lines 779-843: Configuring the Git resolver for authenticated API  
Source: Git authenticated resolver configuration section

**Configuration tasks:**
- **Task:** Create secret with SCM API token
- **Task:** Set SCM type (github, gitlab, gitea, bitbucket, gitbucket)
- **Task:** Set server URL for enterprise instances
- **Task:** Configure API token secret reference (name, key, namespace)
- **Task:** Set default organization

**Configuration location:** TektonConfig custom resource under `pipeline.git-resolver-config`

#### 5.3 Configure Multiple Git Providers

→ Lines 852-921: Configuring many Git providers  
Source: Multi-provider configuration section

**Configuration tasks:**
- **Task:** Use prefix keys (e.g., `test1.scm-type`) for each provider
- **Task:** Configure unique settings per provider
- **Task:** Designate default configuration (unprefixed keys)

**Important:** Cannot use '.' character in configKey values

#### 5.4 Reference Private Git Resources Using SCM API

→ Lines 931-1094: Specifying using Git resolver with authenticated SCM API  
Source: Git authenticated resolver usage examples

**For PipelineRuns:**
- **Task:** Reference pipeline with `resolver: git`
- **Task:** Specify org, repo, revision, pathInRepo parameters

**For TaskRuns:**
- **Task:** Reference task with `resolver: git`
- **Task:** Specify organization, repository, file path

**Important:** Uses authenticated API, not git clone. Cannot combine `url` and `repo` parameters.

#### 5.5 Select Provider Configuration in Multi-Provider Setup

→ Lines 1103-1135: Specifying many Git providers  
Source: Provider selection examples

**For any resource:**
- **Task:** Pass configKey parameter to select specific provider configuration
- **Task:** Use value 'default' or omit to use default configuration

#### 5.6 Override Git Resolver Configuration Inline

→ Lines 1144-1215: Overriding Git resolver configuration  
Source: Configuration override examples

**For ad-hoc access:**
- **Task:** Override token, tokenKey, scmType, serverURL parameters in resource spec
- **Task:** Store inline credentials in TaskRun/PipelineRun spec

**Warning:** Use with caution - credentials visible in resource spec

---

### Job 6: Configure HTTP Resolver for Web-Hosted Resources
*When fetching resources from HTTP endpoints, I want to retrieve pipeline and task definitions from remote URLs, so I can use resources hosted on web servers or CDNs without Git infrastructure.*

**Personas:** Platform Administrator (configure), Developer (use)

**Requires:** HTTP/HTTPS URL hosting YAML file, URL accessible from cluster

#### 6.1 Understand HTTP Resolver Capabilities

→ Lines 1224-1229: About HTTP resolver  
Source: HTTP resolver introduction

**Key capabilities:**
- Fetch resources from any HTTP/HTTPS URL
- No Git or registry infrastructure required
- Simple resource hosting on web servers or CDNs

#### 6.2 Configure HTTP Resolver Settings

→ Lines 1238-1267: Configuring the HTTP resolver  
Source: HTTP resolver configuration section

**Configuration tasks:**
- **Task:** Configure fetch timeout (default 1 minute)

**Configuration location:** TektonConfig custom resource under `pipeline.http-resolver-config`

#### 6.3 Reference HTTP Resources in Pipelines

→ Lines 1276-1388: Specifying using HTTP resolver  
Source: HTTP resolver usage examples

**For PipelineRuns:**
- **Task:** Reference pipeline with `resolver: http`
- **Task:** Specify fully qualified HTTP/HTTPS URL

**For TaskRuns:**
- **Task:** Reference task with `resolver: http`
- **Task:** Specify URL pointing to valid YAML file

**For Step Actions:**
- **Task:** Reference step action with `resolver: http`

---

### Job 7: Configure Cluster Resolver for Cross-Namespace Resources
*When reusing resources across namespaces, I want to reference pipeline and task definitions from other namespaces on the same cluster, so I can centralize standard tasks without duplicating definitions.*

**Personas:** Platform Administrator (configure), Developer (use)

**Requires:** Resource exists in target namespace, RBAC permissions to access target namespace

**Why:** Minimize duplication of task definitions across namespaces, reduce maintenance burden

#### 7.1 Understand Cluster Resolver Capabilities

→ Lines 1397-1402: About Cluster resolver  
Source: Cluster resolver introduction

**Key capabilities:**
- Reference resources from other cluster namespaces
- Access standard tasks in openshift-pipelines namespace
- Share centralized task definitions across teams

#### 7.2 Configure Cluster Resolver Settings

→ Lines 1411-1446: Configuring the cluster resolver  
Source: Cluster resolver configuration section

**Configuration tasks:**
- **Task:** Set default resource kind (Task, Pipeline, StepAction)
- **Task:** Set default namespace
- **Task:** Configure allowed namespaces (whitelist)
- **Task:** Configure blocked namespaces (blacklist)

**Configuration location:** TektonConfig custom resource under `pipeline.cluster-resolver-config`

**Security:** Namespace restrictions enforce access control boundaries

#### 7.3 Reference Cluster Resources in Pipelines

→ Lines 1455-1594: Specifying using cluster resolver  
Source: Cluster resolver usage examples

**For PipelineRuns:**
- **Task:** Reference pipeline with `resolver: cluster`
- **Task:** Specify name, namespace, kind parameters

**For TaskRuns:**
- **Task:** Reference task with `resolver: cluster`
- **Task:** Specify resource name and namespace

**For Step Actions:**
- **Task:** Reference step action with `resolver: cluster`

---

## Discover and Use Resources

### Job 8: Access Standard OpenShift Pipelines Tasks
*When building pipelines, I want to discover and use standard tasks provided by OpenShift Pipelines, so I can leverage pre-built, tested tasks for common operations like building images, cloning Git repos, and running CLI tools.*

**Personas:** Developer, CI/CD Engineer

**Requires:** OpenShift Pipelines installed, cluster resolver configured

→ Lines 1604-2800: Tasks provided in the OpenShift Pipelines namespace  
Source: Standard tasks reference section

#### 8.1 Image Building and Container Operations

**buildah** - Build container images using Buildah
- Parameters: IMAGE, BUILDER_IMAGE, STORAGE_DRIVER, DOCKERFILE, CONTEXT, TLSVERIFY, FORMAT, BUILD_EXTRA_ARGS, PUSH_EXTRA_ARGS, SKIP_PUSH
- Workspaces: source, sslcertdir, dockerconfig
- Results: IMAGE_DIGEST, IMAGE_URL

**s2i-dotnet** - Build .NET Core applications  
**s2i-go** - Build Go applications  
**s2i-java** - Build Java applications  
**s2i-nodejs** - Build Node.js applications  
**s2i-perl** - Build Perl applications  
**s2i-php** - Build PHP applications  
**s2i-python** - Build Python applications  
**s2i-ruby** - Build Ruby applications

**skopeo-copy** - Copy container images between registries
- Parameters: srcImageURL, destImageURL, srcTLSverify, destTLSverify
- Workspaces: images-url

#### 8.2 Git Operations

**git-cli** - Run arbitrary Git commands
- Parameters: BASE_IMAGE, GIT_USER_NAME, GIT_USER_EMAIL, GIT_SCRIPT, USER_HOME, VERBOSE
- Workspaces: source, input, ssh-directory, basic-auth, ssl-ca-directory

**git-clone** - Clone Git repository
- Parameters: url, revision, refspec, submodules, depth, sslVerify, crtFileName, subdirectory, sparseCheckoutDirectories, deleteExisting, httpProxy, httpsProxy, noProxy, verbose, gitInitImage, userHome
- Workspaces: output, ssh-directory, basic-auth, ssl-ca-directory
- Results: commit, url, committer-date

#### 8.3 OpenShift and Kubernetes Operations

**openshift-client** - Run OpenShift oc commands
- Parameters: SCRIPT, VERSION, ARGS
- Workspaces: manifest-dir, kubeconfig-dir

**kn** - Run Knative kn CLI commands
- Parameters: kn-image, ARGS
- Workspaces: kubeconfig

**kn-apply** - Apply Knative service YAML
- Parameters: ARGS, kn-image
- Workspaces: kubeconfig

#### 8.4 Build Tools

**maven** - Run Maven goals
- Parameters: GOALS, MAVEN_MIRROR_URL, SERVER_USER, SERVER_PASSWORD, PROXY_USER, PROXY_PASSWORD, PROXY_PORT, PROXY_HOST, PROXY_NON_PROXY_HOSTS, PROXY_PROTOCOL, CONTEXT_DIR
- Workspaces: source, maven-settings

#### 8.5 Tekton and Pipeline Operations

**tkn** - Run Tekton tkn CLI commands
- Parameters: ARGS, tkn-image
- Workspaces: kubeconfig

**opc** - Run OpenShift Pipelines opc CLI commands (Tech Preview)
- Parameters: SCRIPT, ARGS, OPC_VERSION
- Workspaces: kubeconfig

---

### Job 9: Access Community Tasks for Tool Integrations
*When integrating with third-party tools, I want to use community-maintained tasks for tools like Argo CD, Helm, Jib, and Jenkins, so I can extend pipelines without writing custom integration logic.*

**Personas:** CI/CD Engineer, Developer

**Requires:** OpenShift Pipelines installed with community tasks, understanding of target tool

→ Lines 2809-3244: Community tasks provided in the OpenShift Pipelines namespace  
Source: Community tasks reference section

#### 9.1 Continuous Deployment

**argocd-task-sync-and-wait** - Sync and wait for Argo CD application
- Parameters: application-name, flags, revision, argocd-version
- Results: Argo CD application status

#### 9.2 Package Management

**helm-upgrade-from-repo** - Deploy Helm chart from repository
- Parameters: helm_repo, chart_name, release_version, release_name, release_namespace, overwrite_values, helm_image, upgrade_extra_params
- Workspaces: source

**helm-upgrade-from-source** - Deploy Helm chart from source
- Parameters: charts_dir, release_version, release_name, release_namespace, overwrite_values, helm_image, upgrade_extra_params
- Workspaces: source

#### 9.3 Java Build Tools

**jib-maven** - Build container image with Jib Maven plugin
- Parameters: DIRECTORY, MAVEN_IMAGE, CACHE, INSECUREREGISTRY
- Workspaces: source, sslcertdir
- Results: IMAGE_DIGEST

#### 9.4 Kubernetes Configuration

**kubeconfig-creator** - Create Kubeconfig file from cluster and user information
- Parameters: name, clusterUrl, username, caCrt, clientCrt, clientKey, namespace
- Workspaces: output
- Results: kubeconfig path

#### 9.5 Pull Request Operations

**pull-request** - Interact with pull requests
- Parameters: mode (upload/download), pr-url, provider, secret-key-ref, file-path, repo-full-name, insecure-skip-tls-verify
- Workspaces: output, input, pr

#### 9.6 CI System Integration

**trigger-jenkins-job** - Trigger Jenkins job execution
- Parameters: JENKINS_HOST_URL, JOB_NAME, JOB_PARAMS, JENKINS_SECRETS
- Workspaces: custom-workspace
- Results: jenkins_build_url

---

### Job 10: Reference Step Actions for Reusable Steps
*When creating reusable task steps, I want to use standard StepAction definitions like git-clone and cache operations, so I can compose tasks from tested, reusable step actions.*

**Personas:** Developer

**Requires:** OpenShift Pipelines installed, understanding of StepAction concept

→ Lines 3253-3509: Step action definitions provided with OpenShift Pipelines  
Source: StepActions reference section

#### 10.1 Git Operations

**git-clone** - Clone Git repository as a step action
- Parameters: output-path, url, revision, refspec, submodules, depth, sslVerify, crtFileName, subdirectory, sparseCheckoutDirectories, deleteExisting, httpProxy, httpsProxy, noProxy, verbose, gitInitImage, userHome
- Results: commit, url, committer-date

**Use case:** Embed git-clone logic within task step definitions for maximum flexibility

#### 10.2 Caching Operations (Tech Preview)

**cache-upload** - Upload artifacts to cache
- Parameters: patterns, source, cacheKey, workingdir, hashType, verbose
- **Cache backend:** OCI registry (Tekton Results required)

**cache-fetch** - Fetch artifacts from cache
- Parameters: patterns, target, cacheKey, workingdir, verbose
- **Cache backend:** OCI registry (Tekton Results required)

**Use case:** Implement build caching strategies to speed up pipeline executions

---

## Plan Task Versioning Strategy

### Job 11: Choose Task Versioning Strategy for Production Pipelines
*When choosing between task versions, I want to understand the differences between non-versioned and versioned tasks, so I can decide whether to use stable versioned tasks or auto-updating non-versioned tasks.*

**Personas:** Platform Administrator, CI/CD Engineer

**Requires:** Understanding of OpenShift Pipelines operator upgrade process

→ Lines 3518-3576: About non-versioned and versioned tasks and step actions  
Source: Task versioning strategy section

#### 11.1 Understand Non-Versioned Tasks

**Characteristics:**
- Auto-update with OpenShift Pipelines operator upgrades
- Receive security patches and bug fixes automatically
- Example: `buildah`, `git-clone`, `openshift-client`

**Trade-offs:**
- **Benefit:** Always have latest features and fixes
- **Risk:** Breaking changes may occur during operator upgrades
- **Use case:** Development environments, non-critical pipelines

#### 11.2 Understand Versioned Tasks

**Characteristics:**
- Persist across minor operator versions
- Require explicit version changes
- Example: `buildah-1-18-0`, `git-clone-0-9`

**Trade-offs:**
- **Benefit:** Stable, predictable behavior across upgrades
- **Risk:** May miss security patches without manual updates
- **Use case:** Production environments, critical pipelines

#### 11.3 Choose Strategy Based on Environment

**Decision matrix:**

| Environment | Recommendation | Rationale |
|-------------|----------------|-----------|
| Development/Test | Non-versioned tasks | Get latest features, fast feedback on breaking changes |
| Staging | Versioned tasks + testing | Test operator upgrades before production |
| Production | Versioned tasks | Stability and predictability prioritized |
| Experimental/POC | Non-versioned tasks | Maximize access to new capabilities |

**Hybrid approach:**
- Use versioned tasks for core pipeline stages (build, deploy)
- Use non-versioned tasks for non-critical stages (notifications, cleanup)
- Test non-versioned tasks in staging before adopting in production

---

## Appendices

### A. Resolver Selection Decision Matrix

| Resolver | Best For | Authentication | Infrastructure | Versioning |
|----------|----------|----------------|----------------|------------|
| **Hub** | Public catalog tasks | None | No additional infra | Catalog versions |
| **Bundles** | Private OCI-based distribution | Registry credentials | OCI registry | Image tags/digests |
| **Git (anonymous)** | Public Git repositories | None | Git repository | Branch/tag/SHA |
| **Git (authenticated)** | Private Git repositories | SCM API token | Git provider + secrets | Branch/tag/SHA |
| **HTTP** | Simple web-hosted resources | None (URL-based) | Web server/CDN | URL-based versioning |
| **Cluster** | Cross-namespace sharing | RBAC | None (cluster-local) | Resource versions |

**Choose based on:**
- **Hub resolver:** Using community tasks from Artifact Hub or Tekton Hub
- **Bundles resolver:** Organization uses OCI registries, need private distribution
- **Git resolver (anonymous):** Public open-source tasks, need version control
- **Git resolver (authenticated):** Private internal tasks, enterprise Git instances
- **HTTP resolver:** Simple hosting, no Git/registry infrastructure
- **Cluster resolver:** Sharing tasks across namespaces, centralizing standard tasks

---

### B. Resolver Configuration Quick Reference

| Resolver | TektonConfig Section | Key Configuration Parameters |
|----------|---------------------|------------------------------|
| Hub | `pipeline.hub-resolver-config` | default-type, default-tekton-hub-catalog, default-artifact-hub-task-catalog |
| Bundles | `pipeline.bundles-resolver-config` | default-service-account, default-kind |
| Git (anonymous) | `pipeline.git-resolver-config` | default-url, default-revision, fetch-timeout |
| Git (authenticated) | `pipeline.git-resolver-config` | scm-type, server-url, api-token-secret-name, default-org |
| HTTP | `pipeline.http-resolver-config` | fetch-timeout |
| Cluster | `pipeline.cluster-resolver-config` | default-namespace, default-kind, allowed-namespaces, blocked-namespaces |

**Global constraints:**
- All resolvers have 1-minute maximum timeout
- Git resolver timeout cannot exceed 1 minute

---

### C. Workflow Coverage Analysis

| Stage | Coverage | Jobs | Notes |
|-------|----------|------|-------|
| **Define** | ✅ | Job 1 | Resolver concepts and architecture |
| **Configure** | ✅ | Jobs 2-7 | All 5 resolver types + 2 Git modes |
| **Execute** | ✅ | Embedded in Jobs 2-7 | Usage examples within configuration jobs |
| **Reference** | ✅ | Jobs 8-10 | Standard tasks, community tasks, step actions |
| **Plan** | ✅ | Job 11 | Task versioning strategy |
| **Monitor** | ❌ | - | No resolver performance monitoring content |
| **Troubleshoot** | ❌ | - | No resolver troubleshooting procedures |
| **Secure** | ⚠️ Limited | Job 5, Job 7 | Authentication and namespace access controls |
| **Upgrade** | ⚠️ Limited | Job 11 | Task versioning during upgrades |

### Gaps Identified

| Stage | Gap | Recommendation |
|-------|-----|----------------|
| Monitor | No resolver observability | Add section on monitoring resolver performance, timeout metrics |
| Troubleshoot | No resolver debugging | Add common resolver errors and resolution procedures |
| Secure | Limited security guidance | Expand secret management, RBAC best practices for resolvers |

---

## Navigation Guide

### By User Journey

**Developer using public catalog tasks:**
1. Job 1: Understand how resolvers work
2. Job 2: Configure Hub resolver
3. Job 8: Browse standard OpenShift Pipelines tasks
4. Reference tasks in your PipelineRuns/TaskRuns

**Platform Administrator setting up private task distribution:**
1. Job 1: Understand resolver architecture
2. Job 3: Configure Bundles resolver OR Job 5: Configure Git resolver (authenticated)
3. Set up RBAC and credentials
4. Job 11: Choose versioning strategy for production

**CI/CD Engineer integrating third-party tools:**
1. Job 9: Access community tasks (Argo CD, Helm, Jenkins)
2. Job 5: Configure Git resolver for private integrations (if needed)
3. Combine standard and community tasks in pipelines

**Developer sharing tasks across namespaces:**
1. Job 7: Configure Cluster resolver
2. Create centralized task namespace
3. Reference tasks from openshift-pipelines or custom namespaces

---

## Document Statistics

**Workflow Coverage:**
- Define: 1 job
- Configure: 6 jobs (Resolvers 2-7)
- Execute: Embedded in configuration jobs
- Reference: 3 jobs (Tasks, Community, StepActions)
- Plan: 1 job (Versioning strategy)
- Monitor: Gap identified
- Troubleshoot: Gap identified

**Main Jobs:** 11  
**Resolver Types Covered:** 5 (Hub, Bundles, Git, HTTP, Cluster)  
**Git Resolver Modes:** 2 (Anonymous, Authenticated)  
**Standard Tasks:** 17 tasks  
**Community Tasks:** 7 tasks  
**Step Actions:** 3 (git-clone, cache-upload, cache-fetch)  
**Source Sections:** 26 JTBD records consolidated into 11 main jobs  

**Consolidations Made:**
- Hub resolver: Configure + Use → Job 2 (3 records → 1 job with 3 sub-sections)
- Bundles resolver: Configure + Use → Job 3 (3 records → 1 job with 3 sub-sections)
- Git anonymous: Configure + Use → Job 4 (3 records → 1 job with 3 sub-sections)
- Git authenticated: Configure + Multi-provider + Use + Override → Job 5 (6 records → 1 job with 6 sub-sections)
- HTTP resolver: Configure + Use → Job 6 (3 records → 1 job with 3 sub-sections)
- Cluster resolver: Configure + Use → Job 7 (3 records → 1 job with 3 sub-sections)

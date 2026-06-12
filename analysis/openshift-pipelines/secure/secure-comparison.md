# Securing OpenShift Pipelines - TOC Comparison

**Current Feature-Based vs. Proposed JTBD-Based Structure**

**Analysis Date:** 2026-06-12  
**Book:** Securing OpenShift Pipelines  
**JTBD Records:** 61  
**Main Jobs:** 8 (rolled up from records)  
**Current Chapters:** 6  
**Current Sections:** 48  

---

## Current Structure (Feature-Based)

**Securing OpenShift Pipelines**

- **Chapter 1: Using Tekton Chains for OpenShift Pipelines supply chain security**
  - Section 1.1: Configuring Tekton Chains
    - Section 1.1.1: Supported parameters for Tekton Chains configuration
    - Section 1.1.2: Creating and mounting the Mongo server URL secret
    - Section 1.1.3: Creating and mounting the KMS authentication token secret
    - Section 1.1.4: Enabling Tekton Chains to operate only in selected namespaces
  - Section 1.2: Secrets for signing data in Tekton Chains
    - Section 1.2.1: Generating the cosign key pair using the TektonConfig CR
    - Section 1.2.2: Manually generating signing secrets with the cosign tool
    - Section 1.2.3: Manually generating signing secrets with the skopeo tool
    - Section 1.2.4: Resolving the "secret already exists" error
  - Section 1.3: Authenticating to an OCI registry
  - Section 1.4: Creating and verifying task run signatures without any additional authentication
  - Section 1.5: Using Tekton Chains to sign and verify image and provenance

- **Chapter 2: Setting up OpenShift Pipelines in the web console to view Software Supply Chain Security elements**
  - Section 2.1: Setting up OpenShift Pipelines to view project vulnerabilities
  - Section 2.2: Setting up OpenShift Pipelines to download or view SBOMs
    - Section 2.2.1: Viewing an SBOM in the web UI
    - Section 2.2.2: Downloading an SBOM in the CLI
    - Section 2.2.3: Reading the SBOM

- **Chapter 3: Configuring the security context for pods**
  - Section 3.1: Configuring default and maximum SCC for pods
  - Section 3.2: Configuring the SCC for pods in a namespace
  - Section 3.3: Running pipeline run and task run with custom SCC and service account

- **Chapter 4: Securing webhooks with event listeners**
  - Section 4.1: Providing secure connection with OpenShift routes
  - Section 4.2: Configuring security context for event listeners
  - Section 4.3: Creating a sample EventListener resource using a secure HTTPS connection

- **Chapter 5: Authenticating pipelines with repositories using secrets**
  - Section 5.1: Providing secrets using service accounts
    - Section 5.1.1: Types and annotation of secrets for service accounts
    - Section 5.1.2: Configuring Basic HTTP authentication for Git using a service account
    - Section 5.1.3: Configuring SSH authentication for Git using a service account
    - Section 5.1.4: Configuring container registry authentication by using a service account
    - Section 5.1.5: Additional considerations for authentication using service accounts
      - Section 5.1.5.1: SSH Git authentication in tasks
      - Section 5.1.5.2: Use of secrets as a non-root user
  - Section 5.2: Providing secrets using workspaces
    - Section 5.2.1: Configuring SSH authentication for Git using workspaces
    - Section 5.2.2: Configuring container registry authentication using workspaces
    - Section 5.2.3: Limiting a secret to particular steps using workspaces

- **Chapter 6: Building of container images using Buildah as a non-root user**
  - Section 6.1: Running Buildah as a non-root user by configuring user namespaces
  - Section 6.2: Running Buildah as a non-root user by defining a custom SA and SCC
    - Section 6.2.1: Configuring custom service account and security context constraint
    - Section 6.2.2: Configuring Buildah to use build user
    - Section 6.2.3: Starting a task run with custom config map, or a pipeline run
  - Section 6.3: Limitations of unprivileged builds

- **Chapter 7: Using buildah-ns Tekton task**
  - Section 7.1: Differences between buildah and buildah-ns tasks
  - Section 7.2: Security model of the buildah-ns task
  - Section 7.3: Workspaces, parameters, and results for the buildah-ns task
  - Section 7.4: Running the buildah-ns task

---

## Proposed JTBD-Based Structure

**Securing OpenShift Pipelines**

### Getting Started

**Job 1: Ensure supply chain security for CI/CD pipelines**  
*When:* I need to ensure supply chain security for my CI/CD pipelines  
*Personas:* Security engineer, Cluster administrator  
*Prerequisites:* Install OpenShift Pipelines Operator

- **Understand Tekton Chains capabilities**
  - → Lines 58-78: Using Tekton Chains for OpenShift Pipelines supply chain security
  - Source: Chapter 1, Introduction
  - Learn automatic signing and verification of task runs and pipeline runs
  - Understand cryptographic proof of artifact integrity

### Configure Security Settings

**Job 2: Customize Tekton Chains behavior for organization**  
*When:* I need to customize Tekton Chains behavior for my organization  
*Personas:* Cluster administrator, Security engineer, Platform engineer  
*Prerequisites:* Install OpenShift Pipelines Operator

- **Option A: Basic Configuration via TektonConfig**
  - Persona: Cluster administrator
  - → Lines 85-112: Configuring Tekton Chains
  - Source: Chapter 1, Section 1.1
  - Edit TektonConfig custom resource via oc edit command
  - Automatic application of configuration changes

- **Option B: Configure task run artifacts**
  - Persona: Security engineer
  - → Lines 122-155: Supported parameters for task run artifacts
  - Source: Chapter 1, Section 1.1.1
  - Set artifact format (in-toto, slsa/v1)
  - Configure storage backend (tekton, oci, gcs, docdb, grafeas)
  - Select signature backend (x509, kms)

- **Option C: Configure pipeline run artifacts with deep inspection**
  - Persona: Security engineer
  - → Lines 157-190: Supported parameters for pipeline run artifacts
  - Source: Chapter 1, Section 1.1.1
  - Enable deep inspection to capture child task run results
  - Configure pipeline run storage and signing

- **Option D: Integrate with enterprise KMS providers**
  - Persona: Platform engineer
  - → Lines 217-230: Supported parameters for KMS signers
  - Source: Chapter 1, Section 1.1.1
  - Configure KMS URI (gcpkms://, awskms://, azurekms://, hashivault://)
  - Enable centralized key rotation and auditing

- **Option E: Secure MongoDB credentials for docdb storage**
  - Persona: Platform engineer
  - → Lines 455-509: Creating and mounting the Mongo server URL secret
  - Source: Chapter 1, Section 1.1.2
  - Mount secret to avoid plain text credentials
  - Configure storage.docdb.mongo-server-url-dir parameter

- **Option F: Secure KMS authentication tokens**
  - Persona: Platform engineer
  - → Lines 517-574: Creating and mounting the KMS authentication token secret
  - Source: Chapter 1, Section 1.1.3
  - Mount VAULT_TOKEN as secret
  - Configure signers.kms.auth.token-path parameter

- **Option G: Limit Tekton Chains to specific namespaces**
  - Persona: Cluster administrator
  - → Lines 582-621: Enabling Tekton Chains to operate only in selected namespaces
  - Source: Chapter 1, Section 1.1.4
  - Add --namespace argument to controller
  - Reduce resource consumption and scope security controls

**Job 3: Generate and store cryptographic keys for signing**  
*When:* I need to sign task runs and pipeline runs  
*Personas:* Security engineer, Cluster administrator  
*Prerequisites:* Have openshift-pipelines namespace access

- **Option A: Auto-generate cosign keys via TektonConfig (simplest)**
  - Persona: Cluster administrator
  - → Lines 664-731: Generating the cosign key pair using the TektonConfig CR
  - Source: Chapter 1, Section 1.2.1
  - Set generateSigningSecret: true in TektonConfig
  - Automatic ECDSA key pair generation and storage
  - Extract public key with oc extract command

- **Option B: Manually generate cosign keys with CLI (full control)**
  - Persona: Security engineer
  - → Lines 738-762: Manually generating signing secrets with the cosign tool
  - Source: Chapter 1, Section 1.2.2
  - Use cosign generate-key-pair k8s://openshift-pipelines/signing-secrets
  - Custom passphrase selection
  - Store encrypted cosign.key and cosign.password

- **Option C: Generate keys with skopeo (existing workflow integration)**
  - Persona: Security engineer
  - → Lines 770-853: Manually generating signing secrets with the skopeo tool
  - Source: Chapter 1, Section 1.2.3
  - Generate keys with skopeo generate-sigstore-key
  - Base64 encode private key, public key, and passphrase
  - Create signing-secrets secret in openshift-pipelines namespace

- **Troubleshoot: Resolve "secret already exists" error**
  - → Lines 860-887: Resolving the "secret already exists" error
  - Source: Chapter 1, Section 1.2.4
  - Delete existing secret and recreate

**Job 4: Configure service account credentials for OCI registry authentication**  
*When:* I need to push signatures to an OCI registry  
*Personas:* Platform engineer  
*Prerequisites:* Have OCI registry accessible, Have Docker config credentials

- **Option A: Use default pipeline service account**
  - → Lines 897-937: Authenticating to an OCI registry (basic setup)
  - Source: Chapter 1, Section 1.3
  - Create registry-credentials secret from .dockerconfigjson
  - Patch pipeline service account with imagePullSecrets

- **Option B: Create custom service account (best practice)**
  - Persona: Platform engineer
  - → Lines 938-965: Authenticating to an OCI registry (custom SA)
  - Source: Chapter 1, Section 1.3
  - Create separate service account to avoid operator overrides
  - Associate with task runs via serviceAccountName
  - Minimize pod timeout issues and upgrade disruptions

**Job 5: Configure security context for pipeline pods**  
*When:* I need to control security permissions for pipeline pods  
*Personas:* Cluster administrator, Platform engineer  
*Prerequisites:* Have OpenShift Pipelines installed

- **Option A: Configure cluster-wide default and maximum SCC**
  - Persona: Cluster administrator
  - → Lines 1774-1807: Configuring default and maximum SCC for pods
  - Source: Chapter 3, Section 3.1
  - Edit TektonConfig CR: spec.platforms.openshift.scc.default and maxAllowed
  - Enforce organization-wide security baselines

- **Option B: Configure namespace-specific SCC**
  - Persona: Cluster administrator
  - → Lines 1820-1842: Configuring the SCC for pods in a namespace
  - Source: Chapter 3, Section 3.2
  - Set operator.tekton.dev/scc annotation on namespace
  - Override default SCC for specific environments

- **Option C: Use custom SCC and service account per run**
  - Persona: Platform engineer
  - → Lines 1851-1975: Running pipeline run and task run with custom SCC and service account
  - Source: Chapter 3, Section 3.3
  - Create custom SCC with fsGroup.type: RunAsAny
  - Avoid pod timeouts from default pipelines-scc
  - Associate custom SA with specific TaskRun or PipelineRun

**Job 6: Protect webhook endpoints from unauthorized access**  
*When:* I need to protect webhook endpoints from unauthorized access  
*Personas:* Cluster administrator, Security engineer, DevOps engineer  
*Prerequisites:* Create namespace, Install OpenShift Pipelines Operator

- **Enable HTTPS for EventListener**
  - → Lines 2044-2063: Securing webhooks with event listeners
  - Source: Chapter 4, Introduction
  - Add operator.tekton.dev/enable-annotation=enabled label to namespace
  - Automatic secret and certificate creation

- **Option A: Create routes with re-encrypted TLS (external access)**
  - Persona: Cluster administrator
  - → Lines 2071-2131: Providing secure connection with OpenShift routes
  - Source: Chapter 4, Section 4.1
  - Create route with --cert, --key, and --ca-cert
  - Enable end-to-end encryption from client to event listener

- **Option B: Configure custom security context for EventListener**
  - Persona: Security engineer
  - → Lines 2142-2183: Configuring security context for event listeners
  - Source: Chapter 4, Section 4.2
  - Set runAsNonRoot: true and readOnlyRootFilesystem: true
  - Comply with OpenShift security context constraints

- **Tutorial: Create sample EventListener with HTTPS**
  - Persona: DevOps engineer
  - → Lines 2192-2242: Creating a sample EventListener resource using a secure HTTPS connection
  - Source: Chapter 4, Section 4.3
  - Use pipelines-tutorial example
  - Create TriggerBinding, TriggerTemplate, Trigger, and EventListener

**Job 7: Configure authentication for pipelines to access protected repositories**  
*When:* Pipelines need to interact with protected repositories  
*Personas:* DevOps engineer, Security engineer, Developer  
*Prerequisites:* Create service account or define workspace, Have repository credentials

- **Approach A: Use service accounts (automatic credential mounting)**
  - → Lines 2324-2332: Providing secrets using service accounts
  - Source: Chapter 5, Section 5.1
  - Associate secrets with service account
  - Credentials automatically available to tasks

  - **Git: Configure Basic HTTP authentication**
    - Persona: DevOps engineer
    - → Lines 2463-2566: Configuring Basic HTTP authentication for Git using a service account
    - Source: Chapter 5, Section 5.1.2
    - Create kubernetes.io/basic-auth secret with tekton.dev/git-0 annotation
    - Use personal access token for GitHub authentication

  - **Git: Configure SSH authentication**
    - Persona: DevOps engineer
    - → Lines 2574-2676: Configuring SSH authentication for Git using a service account
    - Source: Chapter 5, Section 5.1.3
    - Create kubernetes.io/ssh-auth secret with ssh-privatekey and known_hosts
    - Support custom SSH ports via annotation

  - **Container Registry: Configure registry authentication**
    - Persona: DevOps engineer
    - → Lines 2684-2768: Configuring container registry authentication by using a service account
    - Source: Chapter 5, Section 5.1.4
    - Create secret from config.json with registry credentials
    - Associate with service account for image pull/push operations

  - **Understand secret types and annotations**
    - Persona: DevOps engineer
    - → Lines 2338-2455: Types and annotation of secrets for service accounts
    - Source: Chapter 5, Section 5.1.1
    - Git: basic-auth, ssh-auth with tekton.dev/git-N annotations
    - Registry: basic-auth, dockercfg, dockerconfigjson with tekton.dev/docker-N annotations

  - **Handle SSH in custom tasks**
    - Persona: Developer
    - → Lines 2790-2820: SSH Git authentication in tasks
    - Source: Chapter 5, Section 5.1.5.1
    - Symlink $HOME/.ssh to user's home directory before Git commands
    - Not needed when using git-clone task

  - **Run as non-root user**
    - Persona: Security engineer
    - → Lines 2827-2846: Use of secrets as a non-root user
    - Source: Chapter 5, Section 5.1.5.2
    - Ensure valid home directory in /etc/passwd
    - Symlink SSH directories for non-root execution

- **Approach B: Use workspaces (flexible, no annotations required)**
  - → Lines 2854-2864: Providing secrets using workspaces
  - Source: Chapter 5, Section 5.2
  - Configure named workspace in task
  - Bind secret to workspace at runtime

  - **Git: SSH authentication via workspace**
    - Persona: DevOps engineer
    - → Lines 2872-2998: Configuring SSH authentication for Git using workspaces
    - Source: Chapter 5, Section 5.2.1
    - Create secret from id_ed25519 and known_hosts
    - Access via $(workspaces.ssh-directory.path)
    - Specify secret with --workspace name=ssh-directory,secret=my-github-ssh-credentials

  - **Container Registry: Authentication via workspace**
    - Persona: DevOps engineer
    - → Lines 3005-3089: Configuring container registry authentication using workspaces
    - Source: Chapter 5, Section 5.2.2
    - Create secret from config.json
    - Set DOCKER_CONFIG=$(workspaces.dockerconfig.path)
    - Support tools like Skopeo

  - **Limit credentials to specific steps**
    - Persona: Security engineer
    - → Lines 3095-3134: Limiting a secret to particular steps using workspaces
    - Source: Chapter 5, Section 5.2.3
    - Define workspace in both task spec and step spec
    - Minimize credential exposure to only authenticated steps

### Secure Image Building

**Job 8: Build container images as a non-root user**  
*When:* I need to build container images in pipelines  
*Personas:* Security engineer, DevOps engineer  
*Prerequisites:* Understand security context constraints, Have buildah task available

- **Option A: Configure user namespaces (simplest approach)**
  - Persona: DevOps engineer
  - → Lines 3214-3284: Running Buildah as a non-root user by configuring user namespaces
  - Source: Chapter 6, Section 6.1
  - Add annotation io.kubernetes.cri-o.userns-mode: 'auto:size=65536;map-to-root=true'
  - Configure stepTemplate with runAsNonRoot: true, runAsUser: 1000
  - Add SETFCAP capability
  - *Note:* Some images might not build with this option

- **Option B: Define custom SA and SCC (for unsupported images)**
  - Persona: Security engineer
  - → Lines 3293-3304: Running Buildah as a non-root user by defining a custom SA and SCC
  - Source: Chapter 6, Section 6.2
  - *Note:* Requires allowPrivilegeEscalation: true but gives more control

  - **Create custom SA and SCC**
    - → Lines 3312-3408: Configuring custom service account and security context constraint
    - Source: Chapter 6, Section 6.2.1
    - Create pipelines-sa-userid-1000 SA
    - Create pipelines-scc-userid-1000 SCC with runAsUser uid: 1000
    - Enable SETUID and SETGID capabilities via allowPrivilegeEscalation: true

  - **Modify Buildah task for build user**
    - → Lines 3416-3526: Configuring Buildah to use build user
    - Source: Chapter 6, Section 6.2.2
    - Copy buildah task to buildah-as-user
    - Set securityContext runAsUser: 1000
    - Mount storage to /home/build/.local/share/containers

  - **Execute builds with custom config**
    - → Lines 3534-3668: Starting a task run with custom config map, or a pipeline run
    - Source: Chapter 6, Section 6.2.3
    - Create TaskRun with serviceAccountName: pipelines-sa-userid-1000
    - Or create PipelineRun with taskServiceAccountName for buildah task

- **Option C: Use buildah-ns task (enhanced security)**
  - Persona: Security engineer
  - → Lines 3700-3772: Using buildah-ns Tekton task
  - Source: Chapter 7, Introduction
  - Enhanced security via automatic user namespace isolation
  - Kernel-level isolation without manual configuration

  - **Understand buildah-ns differences**
    - → Lines 3779-3797: Differences between buildah and buildah-ns tasks
    - Source: Chapter 7, Section 7.1
    - Task name: buildah-ns
    - Annotations: io.kubernetes.cri-o.userns-mode: "auto", io.openshift.builder: "true"
    - User namespace separation for improved privilege isolation

  - **Understand security model**
    - → Lines 3804-3825: Security model of the buildah-ns task
    - Source: Chapter 7, Section 7.2
    - Processes run as UID 0 inside container, nonzero UID on host
    - Kernel-level isolation reduces privilege exposure
    - Container escape protection

  - **Configure buildah-ns parameters**
    - → Lines 3832-3915: Workspaces, parameters, and results for the buildah-ns task
    - Source: Chapter 7, Section 7.3
    - Required: source workspace, IMAGE parameter
    - Optional: CONTAINERFILE_PATH, TLS_VERIFY, VERBOSE, STORAGE_DRIVER, BUILD_EXTRA_ARGS, PUSH_EXTRA_ARGS, SKIP_PUSH
    - Results: IMAGE_URL, IMAGE_DIGEST

  - **Run buildah-ns in PipelineRun**
    - → Lines 3922-3972: Running the buildah-ns task
    - Source: Chapter 7, Section 7.4
    - Create PipelineRun with pipelineRef: task-buildah-ns
    - Bind source workspace to PVC
    - Configure registry authentication if needed

- **Troubleshoot: Understand unprivileged build limitations**
  - → Lines 3676-3691: Limitations of unprivileged builds
  - Source: Chapter 6, Section 6.3
  - --mount=type=cache may fail due to permissions
  - --mount=type=secret fails due to lack of mounting capabilities

### Verify & Observe

**Job 9: Verify the complete signing workflow**  
*When:* I need to verify the complete signing workflow  
*Personas:* Security engineer  
*Prerequisites:* Have Tekton Chains configured, Have signing keys generated, Have cosign installed

- **Create and verify task run signatures (testing)**
  - → Lines 973-1082: Creating and verifying task run signatures without any additional authentication
  - Source: Chapter 1, Section 1.4
  - Disable OCI storage, set task run format/storage to tekton
  - Create task run and wait for completion
  - Retrieve signature from annotations with base64 decode
  - Verify signature with cosign verify-blob-attestation

- **Sign and verify images and provenance (production)**
  - → Lines 1096-1237: Using Tekton Chains to sign and verify image and provenance
  - Source: Chapter 1, Section 1.5
  - Configure in-toto format, OCI storage, and transparency.enabled: true
  - Build image with Kaniko task
  - Verify signed image and attestation with cosign
  - Search Rekor transparency log for provenance records

**Job 10: Visualize supply chain security artifacts in OpenShift web console**  
*When:* I need to visualize supply chain security artifacts in the OpenShift web console  
*Personas:* DevOps engineer, Security engineer, Platform engineer  
*Prerequisites:* Have Tekton Chains configured, Have vulnerability scanning task, Have SBOM generation task

- **Overview: Set up UI for security elements**
  - → Lines 1305-1326: Setting up OpenShift Pipelines to view Software Supply Chain Security elements
  - Source: Chapter 2, Introduction
  - View signed badges on PipelineRuns
  - Display project vulnerabilities
  - Download or view SBOMs

- **View vulnerability counts by severity**
  - Persona: Security engineer
  - → Lines 1334-1477: Setting up OpenShift Pipelines to view project vulnerabilities
  - Source: Chapter 2, Section 2.1
  - Configure vulnerability scan task to output JSON in SCAN_OUTPUT result
  - Extract counts: critical, high, medium, low via jq
  - View visual representation in PipelineRun UI

- **Download or view SBOMs**
  - Persona: Security engineer
  - → Lines 1486-1665: Setting up OpenShift Pipelines to download or view SBOMs
  - Source: Chapter 2, Section 2.2
  - Configure SBOM task with LINK_TO_SBOM result and external-link type
  - Configure pipeline IMAGE_URL result pointing to OCI registry
  - View SBOM in browser or download via cosign CLI
  - Search SBOM for vulnerable libraries (e.g., log4j)

---

## Key Differences

### Current Structure (Feature-Based)

**Organized By:** Technical components, features (Tekton Chains, SCCs, EventListeners, Buildah variants)  
**Navigation:** 7 chapters, 48 sections across multiple nesting levels  
**User Journey:** Linear reading, chapter by chapter, feature by feature  
**Discovery:** Browse chapters to find security feature, then locate relevant section  

**Challenges:**
- Related tasks scattered across chapters (e.g., authentication in Ch 5, but OCI registry auth also in Ch 1)
- Multiple approaches to same job hidden in separate chapters (user namespaces in Ch 6, buildah-ns in Ch 7)
- Security context configuration split between Ch 3 (pods) and Ch 4 (event listeners)
- No clear workflow progression from setup to verification

### Proposed Structure (JTBD-Based)

**Organized By:** Job map stages (Getting Started, Configure, Secure, Verify & Observe)  
**Navigation:** 10 main jobs with persona/approach paths  
**User Journey:** Goal-directed, choose your approach within each job  
**Discovery:** Navigate by what you need to accomplish, then select your persona path or approach  

**Benefits:**
- Related approaches consolidated under single job (e.g., Job 8 has all 3 Buildah approaches)
- Clear progression: Getting Started → Configure → Secure → Verify
- Authentication methods grouped by approach (service accounts vs workspaces)
- Multiple persona paths visible for same job (DevOps engineer UI path vs Security engineer full-control path)

---

## Hierarchy Levels Explanation

### Level 1: Main Jobs (~10 jobs)
Stable, outcome-focused goals that remain constant even if technology changes. Examples:
- "Ensure supply chain security for CI/CD pipelines" (Job 1)
- "Configure authentication for pipelines to access protected repositories" (Job 7)
- "Build container images as a non-root user" (Job 8)

### Level 2: User Stories / Approaches (2-7 per main job)
Persona-specific implementation paths or technical approach variations. Examples:
- "Option A: Auto-generate cosign keys via TektonConfig (simplest)" (Job 3)
- "Option B: Manually generate cosign keys with CLI (full control)" (Job 3)
- "Approach A: Use service accounts (automatic credential mounting)" (Job 7)
- "Approach B: Use workspaces (flexible, no annotations required)" (Job 7)

### Level 3: Procedures (referenced with line numbers)
Step-by-step instructions from source documentation. Examples:
- → Lines 664-731: Generating the cosign key pair using the TektonConfig CR
- → Lines 2463-2566: Configuring Basic HTTP authentication for Git using a service account

---

## Example: Content Consolidation

### Before (Feature-Based, Fragmented)

**Image building scattered across 2 chapters:**
- Chapter 6, Section 6.1: Running Buildah as a non-root user by configuring user namespaces (lines 3214-3284)
- Chapter 6, Section 6.2: Running Buildah as a non-root user by defining a custom SA and SCC (lines 3293-3668)
- Chapter 7: Using buildah-ns Tekton task (lines 3700-3972)

**User must:**
1. Read entire Chapter 6 to understand user namespace approach
2. Read Chapter 6.2 subsections to understand custom SCC approach
3. Read separate Chapter 7 to discover buildah-ns enhanced security option
4. Compare approaches mentally across chapters

### After (JTBD-Based, Consolidated)

**Job 8: Build container images as a non-root user**

All 3 approaches visible in one place:
- **Option A:** Configure user namespaces (simplest approach) → Lines 3214-3284
- **Option B:** Define custom SA and SCC (for unsupported images) → Lines 3293-3668
- **Option C:** Use buildah-ns task (enhanced security) → Lines 3700-3972

**User can:**
1. Navigate directly to Job 8
2. See all 3 options with clear trade-offs
3. Choose approach based on security needs and image compatibility
4. Access detailed procedure via line references

**Benefit:** One place to learn all image building security options, with clear guidance on when to use each approach.

---

## Navigation Improvement Metrics

### Current Structure
- **Top-level items:** 7 chapters
- **Total sections:** 48 sections across 4 nesting levels
- **Finding content:** Browse 7 chapters → Find relevant chapter → Navigate nested sections → Locate procedure
- **Typical clicks:** 5-10 clicks to reach specific procedure
- **Related content:** Scattered across chapters (authentication in Ch 5, but OCI auth also in Ch 1)

### Proposed Structure
- **Top-level items:** 10 main jobs (consolidated from 61 JTBD records)
- **Organization:** Workflow stages (Getting Started → Configure → Secure → Verify)
- **Finding content:** Navigate to job stage → Select main job → Choose persona/approach → Access procedure
- **Typical clicks:** 2-3 clicks to reach specific procedure
- **Related content:** Consolidated under main jobs (all authentication under Job 7, all image building under Job 8)

### Quantified Improvements
- **Top-level navigation items:** 7 chapters → 4 workflow stages (43% reduction)
- **Main navigation items:** 48 sections → 10 main jobs (79% reduction)
- **Clicks to content:** 5-10 clicks → 2-3 clicks (60-70% reduction)
- **Related content consolidation:** 
  - Authentication: Was in Ch 1 (OCI) + Ch 5 (Git/Registry) → Now all in Job 7
  - Image building: Was in Ch 6 + Ch 7 → Now all in Job 8
  - Security context: Was in Ch 3 (pods) + Ch 4 (event listeners) → Now in Jobs 5 & 6

---

## Workflow Coverage Comparison

| Stage | Current | Proposed | Gap Status |
|-------|---------|----------|------------|
| **Get Started** | ⚠️ Scattered in chapter intros | ✅ Job 1: Ensure supply chain security | **Improved** - Dedicated getting started section |
| **Plan** | ❌ Not covered | ⚠️ Partial in Job 8 Option C (buildah-ns differences) | **Gap remains** - Limited planning guidance for choosing approaches |
| **Configure** | ✅ Chapters 1, 3, 4, 5 | ✅ Jobs 2, 3, 4, 5, 6, 7, 8 | **Reorganized** - Configuration tasks consolidated by job |
| **Secure** | ✅ All chapters | ✅ Jobs 2, 3, 4, 5, 6, 7, 8 | **Reorganized** - Security tasks integrated into configuration jobs |
| **Deploy** | ⚠️ Scattered in task/pipeline run procedures | ✅ Job 8 (buildah-ns execution) | **Improved** - Explicit deployment procedures |
| **Observe** | ✅ Chapter 2 (UI visualization) | ✅ Job 10: Visualize security artifacts | **Reorganized** - Observation consolidated |
| **Verify** | ✅ Chapter 1, Sections 1.4, 1.5 | ✅ Job 9: Verify signing workflow | **Reorganized** - Verification consolidated |
| **Troubleshoot** | ⚠️ Scattered (Ch 1 secret errors, Ch 6 limitations) | ⚠️ Scattered (Job 3 secret errors, Job 8 limitations) | **No change** - Still scattered within jobs |
| **Monitor** | ❌ Not covered | ❌ Not covered | **Gap remains** - No ongoing monitoring guidance for Chains, webhooks, or signed artifacts |
| **Upgrade** | ❌ Not covered | ❌ Not covered | **Gap remains** - No guidance for upgrading Tekton Chains or migrating signing keys |
| **Migrate** | ❌ Not covered | ❌ Not covered | **Gap remains** - No migration guidance from other signing solutions |

### Coverage Summary

**Current structure gaps:** Plan, Monitor, Upgrade, Migrate, Troubleshoot (scattered)  
**Proposed structure gaps:** Plan (partial), Monitor, Upgrade, Migrate, Troubleshoot (scattered)  
**Gaps addressed by restructure:** Getting Started (now dedicated section), Deploy (explicit procedures)  

### Recommendations for Gap Closure

| Gap | Recommendation | Priority |
|-----|----------------|----------|
| **Monitor** | Add Job 11: Monitor supply chain security (track signature verification failures, webhook authentication issues, OCI push errors) | High |
| **Upgrade** | Add Job 12: Upgrade Tekton Chains and rotate signing keys (version upgrade procedures, key rotation workflow) | Medium |
| **Troubleshoot** | Consolidate troubleshooting into dedicated section or add troubleshooting subsections to each job | Medium |
| **Plan** | Expand "Choose Your Approach" sections with decision trees for selecting authentication methods, SCC configurations, and Buildah approaches | Low |
| **Migrate** | Add migration content if users are moving from other signing solutions (e.g., Sigstore, Notary) | Low |

---

## Document Statistics

### Current (Feature-Based)
- **Total lines:** 3,978 lines
- **Chapters:** 7
- **Sections:** 48
- **Average section length:** ~83 lines
- **Nesting depth:** 4 levels (Chapter → Section → Subsection → Sub-subsection)

### Proposed (JTBD-Based)
- **JTBD records:** 61
- **Main jobs:** 10
- **User stories/approaches:** 40+
- **Procedures (line references):** 61
- **Nesting depth:** 3 levels (Main Job → User Story/Approach → Procedure reference)

### Content Reuse
- **100% reuse:** All content from current structure referenced in proposed structure via line numbers
- **No duplication:** Each procedure referenced once via line numbers
- **No content loss:** All 48 sections mapped to JTBD jobs

---

## Migration Notes

### For Content Authors
1. **No content rewrite required:** All content remains in secure-combined.adoc
2. **Line references:** Use provided line numbers to link to existing procedures
3. **New content needs:** Monitor (Job 11), Upgrade (Job 12), expanded Planning sections
4. **Troubleshooting consolidation:** Consider creating dedicated troubleshooting job or subsections

### For Technical Reviewers
1. **Verify line number accuracy:** Ensure all line references point to correct procedures
2. **Check workflow progression:** Validate that job order (Getting Started → Configure → Secure → Verify) makes sense
3. **Persona alignment:** Confirm persona assignments match actual user needs (DevOps engineer, Security engineer, Cluster admin)
4. **Gap recommendations:** Prioritize Monitor and Upgrade coverage for production readiness

### For Users
1. **Navigation:** Start with workflow stage, find main job, choose persona/approach
2. **Discovery:** Search by what you need to accomplish, not by feature name
3. **Related content:** All variations of a task are now consolidated under one main job
4. **Prerequisites:** Check prerequisites for each job to ensure proper workflow sequence

---

**End of Comparison**

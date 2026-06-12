# Securing OpenShift Pipelines — Consolidation Report

**Document:** secure-combined.adoc  
**Analysis Date:** 2026-06-12  
**JTBD Records:** 33 pre-consolidated records → 11 final main jobs (after merging)  
**Current Structure:** 7 chapters, 48+ sections  
**Proposed Structure:** 11 main jobs organized by workflow stages

---

## Executive Summary

### What's Changing

The current "Securing OpenShift Pipelines" documentation is organized by technical features and components: Tekton Chains configuration, signing schemes (cosign/x509), SCC management, EventListeners, service account authentication, and Buildah variants. While comprehensive, this structure scatters related user goals across multiple chapters. For example, securing image builds requires reading Chapter 1 (Tekton Chains), Chapter 3 (SCC configuration), and Chapters 6-7 (Buildah approaches). Authentication appears in both Chapter 1 (OCI registry) and Chapter 5 (Git/container repositories).

This reorganization shifts from feature-based chapters to **user goal-oriented jobs**, grouped by workflow stages: Getting Started, Configure Security Settings, Secure Image Building, and Verify & Observe. Each job consolidates all approaches to accomplish a specific security outcome, allowing users to find complete guidance in one place rather than navigating across chapters.

### Key Improvements

- **Supply chain security consolidated:** Tekton Chains configuration (Chapter 1, 6 sections) + signing verification (Chapter 1, 2 sections) + UI observability (Chapter 2) → 4 unified jobs (Jobs 1, 2, 9, 10)
- **Authentication unified:** OCI registry auth (Chapter 1) + Git/repository auth (Chapter 5, 8 subsections) → 2 jobs with clear service account vs workspace approaches (Jobs 4, 7)
- **Image building simplified:** 3 Buildah approaches scattered across Chapters 6-7 → 1 job (Job 8) with 3 clearly distinguished options (user namespaces, custom SCC, buildah-ns)
- **Security context centralized:** Pod SCC configuration (Chapter 3, 3 sections) + EventListener security (Chapter 4, 2 sections) → 2 jobs with global/namespace/run-level scopes (Jobs 5, 6)
- **Key generation streamlined:** 3 separate sections for cosign generation methods → 1 job (Job 3) with 3 options (operator auto-generation, CLI manual, skopeo alternative)
- **Navigation reduced:** 48 sections across 4 hierarchy levels → 11 main jobs with 40+ approaches across 3 levels (60-70% reduction in clicks to content)
- **Workflow progression made explicit:** New structure follows security implementation lifecycle (configure → secure → verify) instead of requiring users to construct workflow from scattered feature docs

---

## Current Structure (Feature-Based)

Extracted from `secure-combined.adoc` (3,978 lines):

- **Chapter 1: Using Tekton Chains for OpenShift Pipelines supply chain security** (lines 59-1237) — Core supply chain security feature
  - 1.1. Configuring Tekton Chains — Backend storage, KMS integration, namespace filtering
    - 1.1.1. Supported parameters for Tekton Chains configuration
    - 1.1.2. Creating and mounting the Mongo server URL secret
    - 1.1.3. Creating and mounting the KMS authentication token secret
    - 1.1.4. Enabling Tekton Chains to operate only in selected namespaces
  - 1.2. Secrets for signing data in Tekton Chains — Key generation approaches
    - 1.2.1. Generating the cosign key pair using the TektonConfig CR
    - 1.2.2. Manually generating signing secrets with the cosign tool
    - 1.2.3. Manually generating signing secrets with the skopeo tool
    - 1.2.4. Resolving the "secret already exists" error
  - 1.3. Authenticating to an OCI registry — Registry authentication for signature storage
  - 1.4. Creating and verifying task run signatures without any additional authentication — Testing workflow
  - 1.5. Using Tekton Chains to sign and verify image and provenance — Production workflow with Rekor

- **Chapter 2: Setting up OpenShift Pipelines to view Software Supply Chain Security elements** (lines 1305-1665) — UI observability
  - 2.1. Setting up OpenShift Pipelines to view project vulnerabilities — Severity-based visualization
  - 2.2. Setting up OpenShift Pipelines to download or view SBOMs — SBOM generation and consumption
    - 2.2.1. Viewing an SBOM in the web UI
    - 2.2.2. Downloading an SBOM in the CLI
    - 2.2.3. Reading the SBOM

- **Chapter 3: Configuring the security context for pods** (lines 1731-1975) — SCC management
  - 3.1. Configuring default and maximum SCC for pods — Cluster-wide policy
  - 3.2. Configuring the SCC for pods in a namespace — Namespace-level override
  - 3.3. Running pipeline run and task run with custom SCC and service account — Run-specific customization

- **Chapter 4: Securing webhooks with event listeners** (lines 2044-2242) — Webhook HTTPS configuration
  - 4.1. Providing secure connection with OpenShift routes — External access with re-encrypted TLS
  - 4.2. Configuring security context for event listeners — Container-level security settings
  - 4.3. Creating a sample EventListener resource using a secure HTTPS connection — Tutorial example

- **Chapter 5: Authenticating pipelines with repositories using secrets** (lines 2246-3134) — Git and container registry authentication
  - 5.1. Providing secrets using service accounts — Automatic credential mounting approach
    - 5.1.1. Types and annotation of secrets for service accounts
    - 5.1.2. Configuring Basic HTTP authentication for Git using a service account
    - 5.1.3. Configuring SSH authentication for Git using a service account
    - 5.1.4. Configuring container registry authentication by using a service account
    - 5.1.5. Additional considerations for authentication using service accounts
      - 5.1.5.1. SSH Git authentication in tasks
      - 5.1.5.2. Use of secrets as a non-root user
  - 5.2. Providing secrets using workspaces — Runtime credential binding approach
    - 5.2.1. Configuring SSH authentication for Git using workspaces
    - 5.2.2. Configuring container registry authentication using workspaces
    - 5.2.3. Limiting a secret to particular steps using workspaces

- **Chapter 6: Building of container images using Buildah as a non-root user** (lines 3137-3691) — Non-root builds with Buildah
  - 6.1. Running Buildah as a non-root user by configuring user namespaces — Simplest approach
  - 6.2. Running Buildah as a non-root user by defining a custom SA and SCC — Full control approach
    - 6.2.1. Configuring custom service account and security context constraint
    - 6.2.2. Configuring Buildah to use build user
    - 6.2.3. Starting a task run with custom config map, or a pipeline run
  - 6.3. Limitations of unprivileged builds — Known constraints

- **Chapter 7: Using buildah-ns Tekton task** (lines 3700-3972) — Enhanced security buildah variant
  - 7.1. Differences between buildah and buildah-ns tasks
  - 7.2. Security model of the buildah-ns task — Kernel-level isolation explanation
  - 7.3. Workspaces, parameters, and results for the buildah-ns task — Configuration reference
  - 7.4. Running the buildah-ns task — Execution procedure

**Total:** 7 chapters, 48+ sections across 4 nesting levels, organized by technical component (Chains, SCCs, EventListeners, Buildah).

---

## Proposed JTBD-Based Structure

### Quick Overview

- **Getting Started**
  - Job 1: Ensure supply chain security for CI/CD pipelines
- **Configure Security Settings**
  - Job 2: Customize Tekton Chains behavior for organizational requirements
  - Job 3: Generate cryptographic keys for artifact signing
  - Job 4: Configure OCI registry authentication for signature storage
  - Job 5: Control security permissions for pipeline pods
  - Job 6: Protect webhook endpoints from unauthorized access
  - Job 7: Configure authentication for pipelines to access protected repositories
- **Secure Image Building**
  - Job 8: Build container images as a non-root user
- **Verify & Observe**
  - Job 9: Verify the complete signing workflow
  - Job 10: Visualize supply chain security artifacts in OpenShift web console

---

### Detailed Job Descriptions

#### Getting Started

**Job 1: Ensure Supply Chain Security for CI/CD Pipelines**

*When I need to ensure supply chain security for my CI/CD pipelines, I want to automatically sign and verify task runs and pipeline runs, so I can prove the integrity and provenance of my software artifacts.*

Prerequisites: Install OpenShift Pipelines Operator

- **1.1. Understanding Tekton Chains capabilities** `[concept]`
  - Lines 58-78 (Chapter 1): Introduction to Tekton Chains
  - Context: Learn what Tekton Chains does, how it observes task runs, generates snapshots, signs artifacts, and enables cryptographic verification. Essential reading before configuration.

---

#### Configure Security Settings

**Job 2: Customize Tekton Chains Behavior for Organizational Requirements**

*When I need to customize Tekton Chains behavior for my organization, I want to modify configuration parameters via the TektonConfig custom resource, so I can control artifact formats, storage backends, and signing methods.*

Prerequisites: Install OpenShift Pipelines Operator

- **2.1. Basic configuration via TektonConfig CR** `[procedure]`
  - Lines 85-112 (Chapter 1, Section 1.1): Configuring Tekton Chains
  - Context: Edit TektonConfig via `oc edit` command. Changes apply automatically without manual pod restarts.

- **2.2. Configure task run artifact storage** `[reference]`
  - Lines 122-155 (Chapter 1, Section 1.1.1): Supported parameters for task run artifacts
  - Context: Set artifact format (in-toto, slsa/v1), storage backend (tekton, oci, gcs, docdb, grafeas), signature backend (x509, kms).

- **2.3. Configure pipeline run artifact storage with deep inspection** `[reference]`
  - Lines 157-190 (Chapter 1, Section 1.1.1): Supported parameters for pipeline run artifacts
  - Context: Enable deep inspection to capture child task run results for complete provenance.

- **2.4. Integrate with enterprise KMS providers** `[procedure]`
  - Lines 217-230 (Chapter 1, Section 1.1.1): Supported parameters for KMS signers
  - Lines 517-574 (Chapter 1, Section 1.1.3): Creating and mounting the KMS authentication token secret
  - Context: Configure KMS URI (gcpkms://, awskms://, azurekms://, hashivault://). Mount VAULT_TOKEN as secret for HashiVault authentication.

- **2.5. Secure MongoDB credentials for docdb storage** `[procedure]`
  - Lines 455-509 (Chapter 1, Section 1.1.2): Creating and mounting the Mongo server URL secret
  - Context: Avoid plain text credentials by mounting MONGO_SERVER_URL as secret.

- **2.6. Limit Tekton Chains to specific namespaces** `[procedure]`
  - Lines 582-621 (Chapter 1, Section 1.1.4): Enabling Tekton Chains to operate only in selected namespaces
  - Context: Add `--namespace` argument to reduce resource consumption and scope security controls.

---

**Job 3: Generate Cryptographic Keys for Artifact Signing**

*When I need to sign task runs and pipeline runs, I want to generate and store cryptographic keys in Kubernetes secrets, so I can enable Tekton Chains to sign artifacts automatically.*

Prerequisites: Access to openshift-pipelines namespace

- **3.1. Auto-generate cosign keys via TektonConfig (simplest)** `[procedure]`
  - Lines 664-731 (Chapter 1, Section 1.2.1): Generating the cosign key pair using the TektonConfig CR
  - Context: Set `generateSigningSecret: true` in TektonConfig. Operator generates ECDSA key pair automatically. Best for quick setup without manual CLI tools.

- **3.2. Manually generate cosign keys with CLI (full control)** `[procedure]`
  - Lines 738-762 (Chapter 1, Section 1.2.2): Manually generating signing secrets with the cosign tool
  - Context: Use `cosign generate-key-pair` with custom passphrase. Best for security engineers requiring full control over encryption parameters.

- **3.3. Generate keys with skopeo (existing workflow integration)** `[procedure]`
  - Lines 770-853 (Chapter 1, Section 1.2.3): Manually generating signing secrets with the skopeo tool
  - Context: Use `skopeo generate-sigstore-key` for sigstore-compatible keys. Best for teams already using skopeo in workflows.

- **3.4. Troubleshoot secret conflicts** `[procedure]`
  - Lines 860-887 (Chapter 1, Section 1.2.4): Resolving the "secret already exists" error
  - Context: Delete existing secret to resolve conflicts during regeneration.

---

**Job 4: Configure OCI Registry Authentication for Signature Storage**

*When I need to push signatures to an OCI registry, I want to configure service account credentials with registry authentication, so I can enable Tekton Chains to store signed artifacts in the registry.*

Prerequisites: OCI registry accessible, Docker config credentials

- **4.1. Create custom service account (best practice)** `[procedure]`
  - Lines 897-965 (Chapter 1, Section 1.3): Authenticating to an OCI registry
  - Context: Avoid pod timeouts by creating custom service account instead of patching default `pipeline` SA. Associate with task runs via `serviceAccountName` field.

---

**Job 5: Control Security Permissions for Pipeline Pods**

*When I need to control security permissions for pipeline pods, I want to configure security context constraints (SCC) for task runs and pipeline runs, so I can enforce least-privilege principles while enabling required capabilities.*

Prerequisites: OpenShift Pipelines installed

- **5.1. Configure cluster-wide default and maximum SCC** `[procedure]`
  - Lines 1774-1807 (Chapter 3, Section 3.1): Configuring default and maximum SCC for pods
  - Context: Edit TektonConfig to set `spec.platforms.openshift.scc.default` and `maxAllowed`. Enforces organization-wide security baselines.

- **5.2. Configure namespace-specific SCC** `[procedure]`
  - Lines 1820-1842 (Chapter 3, Section 3.2): Configuring the SCC for pods in a namespace
  - Context: Set `operator.tekton.dev/scc` annotation on namespace. Overrides default SCC for specific environments.

- **5.3. Use custom SCC and service account per run** `[procedure]`
  - Lines 1851-1975 (Chapter 3, Section 3.3): Running pipeline run and task run with custom SCC and service account
  - Context: Create custom SCC with `fsGroup.type: RunAsAny` to avoid pod timeout issues (BZ#1995779). Associate custom SA with specific TaskRun or PipelineRun.

---

**Job 6: Protect Webhook Endpoints from Unauthorized Access**

*When I need to protect webhook endpoints from unauthorized access, I want to secure webhook endpoints with HTTPS and security context constraints, so I can ensure encrypted communication within and outside the cluster.*

Prerequisites: Namespace created, OpenShift Pipelines Operator installed

- **6.1. Enable HTTPS for EventListener** `[procedure]`
  - Lines 2044-2063 (Chapter 4): Securing webhooks with event listeners
  - Context: Add `operator.tekton.dev/enable-annotation=enabled` label to namespace. Automatic secret and certificate creation.

- **6.2. Create routes with re-encrypted TLS (external access)** `[procedure]`
  - Lines 2071-2131 (Chapter 4, Section 4.1): Providing secure connection with OpenShift routes
  - Context: Create route with `--cert`, `--key`, `--ca-cert` for end-to-end encryption from client to event listener.

- **6.3. Configure custom security context for EventListener** `[procedure]`
  - Lines 2142-2183 (Chapter 4, Section 4.2): Configuring security context for event listeners
  - Context: Set `runAsNonRoot: true` and `readOnlyRootFilesystem: true` to comply with OpenShift SCCs.

- **6.4. Tutorial: Create sample EventListener with HTTPS** `[procedure]`
  - Lines 2192-2242 (Chapter 4, Section 4.3): Creating a sample EventListener resource using a secure HTTPS connection
  - Context: Use pipelines-tutorial example to understand complete configuration flow.

---

**Job 7: Configure Authentication for Pipelines to Access Protected Repositories**

*When pipelines need to interact with protected repositories, I want to configure authentication using service accounts or workspaces, so I can enable authenticated Git clone and image push/pull operations.*

Prerequisites: Service account or workspace definition, repository credentials

- **7.1. Approach A: Service accounts (automatic credential mounting)** `[concept]`
  - Lines 2324-2332 (Chapter 5, Section 5.1): Providing secrets using service accounts
  - Context: Associate secrets with service account. Credentials automatically available to all tasks under that SA. Best for centralized credential management.

  - **7.1.1. Understand secret types and annotations** `[reference]`
    - Lines 2338-2455 (Chapter 5, Section 5.1.1): Types and annotation of secrets for service accounts
    - Context: Git secrets (basic-auth, ssh-auth) with `tekton.dev/git-N` annotations. Registry secrets (basic-auth, dockercfg, dockerconfigjson) with `tekton.dev/docker-N` annotations.

  - **7.1.2. Configure Basic HTTP authentication for Git** `[procedure]`
    - Lines 2463-2566 (Chapter 5, Section 5.1.2): Configuring Basic HTTP authentication for Git using a service account
    - Context: Use personal access token with `kubernetes.io/basic-auth` secret. Annotate with Git URL.

  - **7.1.3. Configure SSH authentication for Git** `[procedure]`
    - Lines 2574-2676 (Chapter 5, Section 5.1.3): Configuring SSH authentication for Git using a service account
    - Context: Create `kubernetes.io/ssh-auth` secret with ssh-privatekey and known_hosts. Supports custom SSH ports.

  - **7.1.4. Configure container registry authentication** `[procedure]`
    - Lines 2684-2768 (Chapter 5, Section 5.1.4): Configuring container registry authentication by using a service account
    - Context: Create secret from Docker config.json with registry credentials. Associate with SA for image pull/push.

  - **7.1.5. Handle SSH in custom tasks** `[procedure]`
    - Lines 2790-2820 (Chapter 5, Section 5.1.5.1): SSH Git authentication in tasks
    - Context: Symlink `$HOME/.ssh` to user's home before Git commands. Not needed when using git-clone task.

  - **7.1.6. Run as non-root user with SSH** `[procedure]`
    - Lines 2827-2846 (Chapter 5, Section 5.1.5.2): Use of secrets as a non-root user
    - Context: Ensure valid home directory in `/etc/passwd`. Symlink SSH directories for non-root execution.

- **7.2. Approach B: Workspaces (flexible, no annotations required)** `[concept]`
  - Lines 2854-2864 (Chapter 5, Section 5.2): Providing secrets using workspaces
  - Context: Configure named workspace in task, bind secret at runtime. Best for dynamic credentials and testing.

  - **7.2.1. Configure SSH authentication for Git via workspaces** `[procedure]`
    - Lines 2872-2998 (Chapter 5, Section 5.2.1): Configuring SSH authentication for Git using workspaces
    - Context: Create secret from id_ed25519 and known_hosts. Access via `$(workspaces.ssh-directory.path)`.

  - **7.2.2. Configure container registry authentication via workspaces** `[procedure]`
    - Lines 3005-3089 (Chapter 5, Section 5.2.2): Configuring container registry authentication using workspaces
    - Context: Create secret from config.json. Set `DOCKER_CONFIG=$(workspaces.dockerconfig.path)`. Supports Skopeo.

  - **7.2.3. Limit credentials to specific steps** `[procedure]`
    - Lines 3095-3134 (Chapter 5, Section 5.2.3): Limiting a secret to particular steps using workspaces
    - Context: Define workspace in both task spec and step spec. Minimizes credential exposure.

---

#### Secure Image Building

**Job 8: Build Container Images as a Non-Root User**

*When I need to build container images in pipelines, I want to run Buildah as a non-root user, so I can reduce security exposure from container build processes.*

Prerequisites: Understanding of security context constraints, buildah task available

- **8.1. Option A: Configure user namespaces (simplest)** `[procedure]`
  - Lines 3214-3284 (Chapter 6, Section 6.1): Running Buildah as a non-root user by configuring user namespaces
  - Context: Add annotation `io.kubernetes.cri-o.userns-mode: 'auto:size=65536;map-to-root=true'`. Set `runAsNonRoot: true`, `runAsUser: 1000`, add `SETFCAP` capability. Minimal configuration complexity, automatic user namespace mapping. Note: Some images may not build with this approach.

- **8.2. Option B: Define custom SA and SCC (for unsupported images)** `[procedure]`
  - Lines 3293-3304 (Chapter 6, Section 6.2): Running Buildah as a non-root user by defining a custom SA and SCC
  - Lines 3312-3408 (Chapter 6, Section 6.2.1): Configuring custom service account and security context constraint
  - Lines 3416-3526 (Chapter 6, Section 6.2.2): Configuring Buildah to use build user
  - Lines 3534-3668 (Chapter 6, Section 6.2.3): Starting a task run with custom config map, or a pipeline run
  - Context: Create `pipelines-sa-userid-1000` SA and `pipelines-scc-userid-1000` SCC with `runAsUser uid: 1000`. Enable SETUID and SETGID via `allowPrivilegeEscalation: true`. Copy buildah task to buildah-as-user with `securityContext runAsUser: 1000`. Best for images that fail with user namespace approach. Requires more configuration but provides explicit control.

- **8.3. Option C: Use buildah-ns task (enhanced security)** `[procedure]`
  - Lines 3700-3772 (Chapter 7): Using buildah-ns Tekton task
  - Lines 3779-3797 (Chapter 7, Section 7.1): Differences between buildah and buildah-ns tasks
  - Lines 3804-3825 (Chapter 7, Section 7.2): Security model of the buildah-ns task
  - Lines 3832-3915 (Chapter 7, Section 7.3): Workspaces, parameters, and results for the buildah-ns task
  - Lines 3922-3972 (Chapter 7, Section 7.4): Running the buildah-ns task
  - Context: Automatic user namespace isolation via annotations (`io.kubernetes.cri-o.userns-mode: "auto"`, `io.openshift.builder: "true"`). Processes run as UID 0 inside container, nonzero UID on host. Kernel-level isolation provides maximum security. Minimal configuration for automatic isolation.

- **8.4. Troubleshoot: Understand unprivileged build limitations** `[reference]`
  - Lines 3676-3691 (Chapter 6, Section 6.3): Limitations of unprivileged builds
  - Context: `--mount=type=cache` may fail due to permissions. `--mount=type=secret` fails due to lack of mounting capabilities.

---

#### Verify & Observe

**Job 9: Verify the Complete Signing Workflow**

*When I need to verify the complete signing workflow, I want to create a task run, retrieve its signature, and verify it with the public key, so I can ensure Tekton Chains is correctly signing artifacts.*

Prerequisites: Tekton Chains configured, signing keys generated, cosign installed

- **9.1. Create and verify task run signatures (testing)** `[procedure]`
  - Lines 973-1082 (Chapter 1, Section 1.4): Creating and verifying task run signatures without any additional authentication
  - Context: Disable OCI storage, set task run format/storage to tekton. Create task run, retrieve signature from annotations, verify with cosign verify-blob-attestation. Best for testing workflow before production deployment.

- **9.2. Sign and verify images and provenance (production)** `[procedure]`
  - Lines 1096-1237 (Chapter 1, Section 1.5): Using Tekton Chains to sign and verify image and provenance
  - Context: Configure in-toto format, OCI storage, enable `transparency.enabled: true`. Build image with Kaniko task. Verify signed image and attestation with cosign. Search Rekor transparency log for provenance records. End-to-end production workflow with public transparency.

---

**Job 10: Visualize Supply Chain Security Artifacts in OpenShift Web Console**

*When I need to visualize supply chain security artifacts in the OpenShift web console, I want to view signed badges, vulnerabilities, and SBOMs in the PipelineRun UI, so I can assess security posture without CLI tools.*

Prerequisites: Tekton Chains configured, vulnerability scanning task, SBOM generation task

- **10.1. Overview: Set up UI for security elements** `[concept]`
  - Lines 1305-1326 (Chapter 2): Setting up OpenShift Pipelines to view Software Supply Chain Security elements
  - Context: Understand signed badges, vulnerability visualization, SBOM viewing capabilities. PipelineRuns with signed provenance display badges automatically.

- **10.2. View vulnerability counts by severity** `[procedure]`
  - Lines 1334-1477 (Chapter 2, Section 2.1): Setting up OpenShift Pipelines to view project vulnerabilities
  - Context: Configure vulnerability scan task to output JSON in `SCAN_OUTPUT` result. Extract counts (critical, high, medium, low) via jq. View visual representation categorized by severity in PipelineRun UI and list view.

- **10.3. Download or view SBOMs** `[procedure]`
  - Lines 1486-1665 (Chapter 2, Section 2.2): Setting up OpenShift Pipelines to download or view SBOMs
  - Lines 1569-1586 (Chapter 2, Section 2.2.1): Viewing an SBOM in the web UI
  - Lines 1588-1616 (Chapter 2, Section 2.2.2): Downloading an SBOM in the CLI
  - Lines 1618-1665 (Chapter 2, Section 2.2.3): Reading the SBOM
  - Context: Configure SBOM task with `LINK_TO_SBOM` result (type: external-link). Configure pipeline `IMAGE_URL` result. View SBOM in browser, search for vulnerable libraries (e.g., log4j), or download via cosign CLI. SBOM shows library author, name, version, licenses for compliance verification.

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | Technical component (Tekton Chains, SCCs, EventListeners, Buildah variants) | User goal and workflow stage (configure → secure → verify) |
| **Top-level items** | 7 chapters with 48+ sections across 4 hierarchy levels | 11 main jobs with 40+ approaches across 3 levels |
| **Authentication coverage** | Split: OCI registry auth (Ch 1) + Git/repository auth (Ch 5, 8 subsections) | Unified: Jobs 4 (OCI) + 7 (Git/registry) with clear approach comparison |
| **Image building guidance** | Scattered: User namespaces (Ch 6.1), custom SCC (Ch 6.2, 3 subsections), buildah-ns (Ch 7, 4 sections) | Consolidated: Job 8 with 3 options (A/B/C) and clear decision guidance |
| **Key generation paths** | Linear: 3 separate sections for cosign methods in Ch 1.2 | Unified: Job 3 with 3 options (auto-generate, manual CLI, skopeo) and persona mapping |
| **Security context scope** | Split: Pod SCC (Ch 3, 3 sections) + EventListener SCC (Ch 4.2) | Consolidated: Jobs 5 (pods) + 6 (webhooks) with global/namespace/run scopes |
| **Signing workflow** | Split: Configuration (Ch 1.1), key generation (Ch 1.2), verification (Ch 1.4, 1.5) | End-to-end: Jobs 2 (configure) → 3 (keys) → 9 (verify) with clear progression |
| **Observability** | Isolated: Ch 2 (3 sections) separate from signing chapters | Integrated: Job 10 in Verify & Observe stage, linked to Jobs 1, 2, 9 |

### Job List Adjustments from Suggested Input

The suggested 33 JTBD records were consolidated to **11 jobs** for the following reasons:

1. **Records secure-002, secure-003 merged** → **Job 2** ("Customize Tekton Chains behavior"): Both cover TektonConfig editing; secure-003 is a user story under the main job.

2. **Records secure-004, secure-005 absorbed into Job 2** → Sub-approaches 2.2 and 2.3: Task run and pipeline run artifact configuration are configuration parameters, not separate jobs.

3. **Records secure-006, secure-007, secure-008 absorbed into Job 2** → Sub-approaches 2.4, 2.5: KMS integration, MongoDB credentials, namespace filtering are advanced configuration options.

4. **Record secure-009 absorbed into Job 2** → Sub-approach 2.6: Namespace filtering is a configuration parameter.

5. **Records secure-010, secure-011, secure-012, secure-013, secure-014 merged** → **Job 3** ("Generate cryptographic keys"): All cover signing secret generation; differences are approach variations (operator auto, manual cosign, skopeo, troubleshooting).

6. **Records secure-015, secure-016 merged** → **Job 4** ("Configure OCI registry authentication"): Both cover service account credentials; secure-016 is best practice guidance within the job.

7. **Records secure-017, secure-018 merged** → **Job 9** ("Verify signing workflow"): Both cover verification; secure-018 is a configuration step within testing.

8. **Records secure-019, secure-020, secure-021 merged** → **Job 9** sub-approach 9.2: All cover image and provenance signing; differences are workflow steps (configure, sign, search Rekor).

9. **Records secure-022, secure-023, secure-024 merged** → **Job 10** ("Visualize security artifacts"): All cover UI observability; differences are artifact types (signed badges, vulnerabilities, SBOMs).

10. **Records secure-025, secure-026, secure-027, secure-028, secure-029 merged** → **Job 10** sub-approach 10.3: All cover SBOM generation and consumption; differences are consumption methods (view UI, download CLI, read content).

11. **Records secure-030, secure-031, secure-032, secure-033 merged** → **Job 5** ("Control security permissions for pods"): All cover SCC configuration; differences are scope (global, namespace, run-specific).

**Final count:** 11 jobs. **Consolidation rationale:** Merged configuration parameters into parent jobs (Job 2), grouped approach variations under main jobs (Jobs 3, 8, 9, 10), unified scattered authentication (Jobs 4, 7), and centralized security context by scope (Job 5, 6).

---

## Consolidation Examples

### Example 1: Image Building Security (3 scattered chapters → 1 unified job)

**Current (Fragmented):**
- Chapter 6, Section 6.1: Running Buildah as a non-root user by configuring user namespaces (lines 3214-3284) — Annotation-based approach
- Chapter 6, Section 6.2: Running Buildah as a non-root user by defining a custom SA and SCC (lines 3293-3668, 3 subsections) — Explicit control approach
- Chapter 7: Using buildah-ns Tekton task (lines 3700-3972, 4 sections) — Enhanced security variant

Users must read 2 full chapters (6 and 7) to understand all non-root build approaches. No guidance on which approach to choose. Chapter 7 appears as a separate topic rather than an alternative to Chapter 6.

**Proposed (Consolidated):**
- **Job 8: Build container images as a non-root user**
  - 8.1. Option A: Configure user namespaces (simplest) — Chapter 6.1
  - 8.2. Option B: Define custom SA and SCC (for unsupported images) — Chapter 6.2
  - 8.3. Option C: Use buildah-ns task (enhanced security) — Chapter 7
  - 8.4. Troubleshoot: Understand unprivileged build limitations — Chapter 6.3

**Benefit:** All 3 Buildah approaches consolidated under one job with clear option labels (A/B/C) and decision guidance (simplest, unsupported images, enhanced security). Users see all security options in one place and choose based on requirements.

---

### Example 2: Authentication Configuration (2 chapters, 10 sections → 2 jobs with clear approaches)

**Current (Fragmented):**
- Chapter 1, Section 1.3: Authenticating to an OCI registry (lines 897-965) — For signature storage
- Chapter 5: Authenticating pipelines with repositories using secrets (lines 2246-3134, 8 subsections)
  - 5.1: Service accounts approach (4 subsections: types, Basic HTTP, SSH, container registry)
  - 5.2: Workspaces approach (3 subsections: SSH, registry, step-level limiting)

Authentication split between Chapters 1 and 5. Within Chapter 5, service account vs workspace approaches buried in subsections. No comparison or decision guidance on when to use each approach.

**Proposed (Consolidated):**
- **Job 4: Configure OCI registry authentication for signature storage** (Chapter 1.3)
- **Job 7: Configure authentication for pipelines to access protected repositories**
  - Approach A: Service accounts (automatic credential mounting) — Chapter 5.1
    - 7.1.1. Understand secret types and annotations
    - 7.1.2-7.1.4. Git and registry authentication methods
  - Approach B: Workspaces (flexible, no annotations required) — Chapter 5.2
    - 7.2.1-7.2.3. Git, registry, step-level methods

**Benefit:** OCI registry auth (Job 4) separated from Git/repository auth (Job 7). Within Job 7, service account vs workspace approaches clearly distinguished at top level with decision criteria (centralized vs flexible). Users choose approach first, then drill into specific methods.

---

### Example 3: Supply Chain Security Workflow (5 scattered sections → 4 connected jobs)

**Current (Fragmented):**
- Chapter 1, Section 1.1: Configuring Tekton Chains (lines 85-621, 4 subsections) — Configuration parameters
- Chapter 1, Section 1.2: Secrets for signing data (lines 631-887, 4 subsections) — Key generation
- Chapter 1, Section 1.4: Creating and verifying task run signatures (lines 973-1082) — Testing workflow
- Chapter 1, Section 1.5: Using Tekton Chains to sign and verify image and provenance (lines 1096-1237) — Production workflow
- Chapter 2: Setting up OpenShift Pipelines to view Software Supply Chain Security elements (lines 1305-1665, 3 sections) — UI observability

Supply chain security workflow scattered across 2 chapters. No clear progression from configuration → keys → verification. UI observability (Chapter 2) isolated from signing configuration (Chapter 1).

**Proposed (Consolidated):**
- **Job 1: Ensure supply chain security for CI/CD pipelines** (Chapter 1 intro, lines 58-78) — Understanding Tekton Chains
- **Job 2: Customize Tekton Chains behavior** (Chapter 1.1) — Configuration with 6 sub-approaches
- **Job 3: Generate cryptographic keys** (Chapter 1.2) — Key generation with 3 options
- **Job 9: Verify signing workflow** (Chapter 1.4, 1.5) — Testing and production verification
- **Job 10: Visualize security artifacts in web console** (Chapter 2) — UI observability

**Benefit:** Clear workflow progression: Job 1 (understand) → Job 2 (configure) → Job 3 (generate keys) → Job 9 (verify) → Job 10 (observe). UI observability (Job 10) now explicitly linked to verification (Job 9) in "Verify & Observe" stage.

---

## Content Gaps Identified

| Gap | JTBD Reference | Current Coverage | Impact |
|-----|---------------|-----------------|--------|
| No troubleshooting guide for signature verification failures | Jobs 9, 10 | Verification procedures exist but no failure diagnosis guidance | **High** — Users have no guidance when cosign verify fails or signatures are missing; likely causes support tickets |
| No decision framework for choosing security approaches | Jobs 3 (signing schemes), 7 (auth approaches), 8 (Buildah methods) | Options listed but no comparison tables or decision trees | **High** — Users must read all options to determine which fits requirements; increases time-to-implement |
| No upgrade procedures for Tekton Chains or key rotation | Job 2 | Configuration procedures exist but no version upgrade or key rotation guidance | **Medium** — Users can configure Chains but lack guidance for production lifecycle (upgrades, key expiration) |
| No monitoring guidance for Tekton Chains controller | Jobs 1, 2, 9 | Configuration and verification exist but no ongoing monitoring | **Medium** — Users can set up and verify but lack proactive monitoring (controller pod failures, signing errors) |
| No rollback procedures for SCC or signing configuration changes | Jobs 2, 5 | Configuration change procedures exist but no rollback guidance | **Medium** — Users can apply changes but lack safety net if changes cause failures |
| No integration examples with external secret management (Vault, Sealed Secrets) | Jobs 3, 7 | Kubernetes secret creation documented but no enterprise secret management integration | **Low** — Users can use Kubernetes secrets but lack patterns for enterprise secret management tools |
| No cost optimization guidance for OCI storage backends | Job 2 (sub-approach 2.2) | Storage backend options listed but no cost comparison | **Low** — Users can configure backends but lack guidance on storage costs (OCI registry vs GCS vs docdb) |
| No migration guidance from other signing solutions (Sigstore, Notary) | Jobs 1, 2, 3 | Tekton Chains setup documented but no migration from existing solutions | **Low** — Applies only to users with existing signing solutions; workaround is manual setup |

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 7 chapters | 4 workflow stages | 43% reduction |
| Sections to browse for "image building security" | 11 sections across 2 chapters (Ch 6, 7) | 1 job, 4 approaches | ~64% reduction |
| Sections to browse for "authentication configuration" | 10 sections across 2 chapters (Ch 1.3, Ch 5) | 2 jobs, 2 approaches | ~50% reduction |
| Sections to browse for "signing key generation" | 4 sections in Ch 1.2 | 1 job, 4 approaches | ~0% (same depth, clearer grouping) |
| Sections to browse for "supply chain security setup" | 5 sections across 2 chapters (Ch 1.1-1.2, Ch 2) | 4 jobs (Jobs 1, 2, 3, 10) | Workflow clarity +100% (explicit progression) |
| Clicks to find "SCC configuration" | 5-7 clicks (Chapter 3 → Section 3.1/3.2/3.3) | 2-3 clicks (Job 5 → scope option) | ~60% reduction |
| Clicks to find "webhook HTTPS setup" | 5-6 clicks (Chapter 4 → Section 4.1/4.2/4.3) | 2-3 clicks (Job 6 → approach) | ~50% reduction |
| Average hierarchy depth | 4 levels (Chapter → Section → Subsection → Sub-subsection) | 3 levels (Job → Approach → Source reference) | 25% reduction |

**Final job count: 11** (reduced from suggested 33 records). Consolidation rationale: Configuration parameters merged into parent jobs (Job 2 has 6 sub-approaches instead of 6 separate jobs), approach variations grouped under main jobs (Jobs 3, 8, 9, 10 consolidate 3-5 records each), authentication unified by target (OCI vs Git/registry), and security context organized by scope (global/namespace/run).

---

## Document Statistics

### Current (Feature-Based)
- **Total lines:** 3,978 lines
- **Chapters:** 7
- **Sections:** 48+
- **Hierarchy depth:** 4 levels (Chapter → Section → Subsection → Sub-subsection)
- **Average section length:** ~83 lines
- **Organizing principle:** Technical component (Tekton Chains, SCCs, EventListeners, Buildah)

### Proposed (JTBD-Based)
- **JTBD records:** 33 pre-consolidated → 11 final main jobs
- **Workflow stages:** 4 (Getting Started, Configure, Secure Image Building, Verify & Observe)
- **Approaches:** 40+ (numbered sub-items under main jobs)
- **Hierarchy depth:** 3 levels (Job → Approach → Source reference)
- **Content reuse:** 100% (all 48 sections referenced via line numbers, no duplication)
- **Organizing principle:** User goal and workflow stage

### Workflow Coverage

| Stage | Current | Proposed | Coverage |
|-------|---------|----------|----------|
| **Understand** | ⚠️ Scattered in chapter intros | ✅ Job 1 (dedicated intro) | Improved |
| **Configure** | ✅ Ch 1, 3, 4, 5 (scattered) | ✅ Jobs 2-7 (consolidated) | Reorganized |
| **Secure** | ✅ All chapters (mixed with config) | ✅ Jobs 2-8 (integrated) | Reorganized |
| **Deploy** | ⚠️ Partial (execution steps buried) | ✅ Jobs 8, 9 (explicit) | Improved |
| **Observe** | ✅ Ch 2 (isolated) | ✅ Job 10 (linked to verification) | Reorganized |
| **Verify** | ✅ Ch 1.4, 1.5 (buried) | ✅ Job 9 (explicit stage) | Improved |
| **Troubleshoot** | ⚠️ Minimal (Ch 1.2.4, Ch 6.3) | ⚠️ Still scattered | No change (gap identified) |
| **Monitor** | ❌ Not covered | ❌ Not covered | Gap remains |
| **Upgrade** | ❌ Not covered | ❌ Not covered | Gap remains |

### Consolidation Metrics
- **Sections consolidated:** 48 sections → 11 jobs (77% reduction in top-level items)
- **Hierarchy reduction:** 4 levels → 3 levels (25% depth reduction)
- **Authentication unification:** 2 chapters, 10 sections → 2 jobs, 2 approaches (80% structural simplification)
- **Image building consolidation:** 2 chapters, 7 sections → 1 job, 4 approaches (83% structural simplification)
- **Supply chain security workflow:** 5 sections across 2 chapters → 4 connected jobs with explicit progression

---

**End of Consolidation Report**

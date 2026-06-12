# Securing OpenShift Pipelines
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** Enable cluster administrators and security engineers to implement comprehensive supply chain security, authentication, and access controls for OpenShift Pipelines.

**Personas:** Security engineer, Cluster administrator, Platform engineer, DevOps engineer

**Main Jobs:** 11 core jobs across 5 workflow stages

---

## Quick Navigation

**I want to:**
- Automatically sign and verify pipeline artifacts → Job 1 (Secure)
- Configure Tekton Chains for my organization → Job 2 (Configure)
- Generate signing keys for artifact attestation → Job 3 (Secure)
- Authenticate pipelines to OCI registries → Job 4 (Configure)
- Verify that my signing workflow is working → Job 5 (Secure)
- Sign and verify container images and provenance → Job 6 (Secure)
- View security artifacts in the OpenShift UI → Job 7 (Observe)
- Control pod security permissions → Job 8 (Secure)
- Secure webhook endpoints with HTTPS → Job 9 (Secure)
- Authenticate pipelines to Git and container registries → Job 10 (Secure)
- Build container images as non-root user → Job 11 (Secure)

---

# Table of Contents

## Implement Supply Chain Security

### Job 1: Ensure Supply Chain Security for CI/CD Pipelines
*When I need to prove the integrity and provenance of software artifacts*

**Personas:** Security engineer
**Why:** Minimize risk of supply chain attacks and enable compliance with security policies

#### Understanding Tekton Chains

→ Lines 58-78: Using Tekton Chains for OpenShift Pipelines supply chain security
  Source: Introduction

**What Tekton Chains does:**
- Automatically observes all task run executions
- Takes snapshots of task runs after completion
- Converts snapshots to standard payload formats (in-toto, SLSA)
- Signs and stores artifacts with cryptographic proof
- Enables verification of artifact integrity

**Benefits:**
- Cryptographic proof of artifact integrity
- Automated signing without manual intervention
- Compliance with SLSA specification
- Reduced manual verification effort

---

### Job 2: Customize Tekton Chains for Organizational Requirements
*When I need to control artifact formats, storage backends, and signing methods*

**Personas:** Cluster administrator, Security engineer, Platform engineer

#### 2.1 Configure Tekton Chains via TektonConfig CR (The "Standard" Configuration)
**Goal:** Modify Tekton Chains behavior through the operator-managed custom resource.

→ Lines 85-112: Configuring Tekton Chains
  Source: Chapter 1, Configuration

- **Task:** Edit TektonConfig custom resource
  ```bash
  oc edit TektonConfig config
  ```
- **Benefit:** Changes apply automatically without manual pod restarts
- **Note:** Operator automatically propagates configuration changes

#### 2.2 Configure Task Run Artifact Storage (The "Task-Level" Setup)
**Goal:** Control how task run signatures are stored and formatted.

→ Lines 122-155: Supported parameters for task run artifacts
  Source: Chapter 1, Configuration parameters

**Configuration options:**
- **Format:** `artifacts.taskrun.format`
  - Options: `in-toto`, `slsa/v1`
  - Recommendation: Use `slsa/v1` for SLSA compliance
  
- **Storage backend:** `artifacts.taskrun.storage`
  - Options: `tekton`, `oci`, `gcs`, `docdb`, `grafeas`
  - Recommendation: Use `oci` for production (registry-based), `tekton` for testing (annotation-based)
  
- **Signature backend:** `artifacts.taskrun.signer`
  - Options: `x509`, `kms`
  - Recommendation: Use `kms` for enterprise key management, `x509` for simpler setups

**Desired outcomes:**
- Task run artifacts comply with SLSA specification
- Reduced storage costs through appropriate backend selection
- Minimal integration effort with existing security infrastructure

#### 2.3 Configure Pipeline Run Artifact Storage (The "Pipeline-Level" Setup)
**Goal:** Record provenance for entire pipeline runs including child task runs.

→ Lines 157-190: Supported parameters for pipeline run artifacts
  Source: Chapter 1, Configuration parameters

**Configuration options:**
- **Deep inspection:** `artifacts.pipelinerun.enable-deep-inspection`
  - `true`: Records results of child task runs (complete provenance)
  - `false`: Records only pipeline run results (minimal provenance)
  - Recommendation: Enable for audit and compliance requirements

**Benefits:**
- Complete provenance capture for complex pipelines
- Reduced audit effort through full execution history
- Minimal risk of missing critical execution data

#### 2.4 Integrate with Enterprise Key Management Systems (The "KMS" Setup)
**Goal:** Leverage cloud provider KMS for centralized key management.

→ Lines 217-230: Supported parameters for KMS signers
  Source: Chapter 1, KMS configuration

**Configuration:**
- **KMS URI:** `signers.kms.kmsref`
  - Supported schemes: `gcpkms://`, `awskms://`, `azurekms://`, `hashivault://`

→ Lines 517-574: Creating and mounting the KMS authentication token secret
  Source: Chapter 2, KMS authentication

- **Task:** Create secret with KMS authentication token
- **Task:** Mount secret on Tekton Chains controller
- **Task:** Set `signers.kms.auth.token-path` to token file path

**Benefits:**
- Centralized key management across organization
- Automated key rotation capabilities
- Reduced risk of key exposure
- Minimal manual key management effort

#### 2.5 Secure MongoDB Connection for DocDB Storage (The "DocDB" Setup)
**Goal:** Use MongoDB for artifact storage without exposing credentials.

→ Lines 455-509: Creating and mounting the Mongo server URL secret
  Source: Chapter 2, DocDB configuration

- **Task:** Create secret with `MONGO_SERVER_URL`
- **Task:** Mount secret on Tekton Chains controller
- **Task:** Configure `storage.docdb.mongo-server-url` parameter
- **Why:** Plain text credentials in configuration are insecure for production

#### 2.6 Limit Tekton Chains to Selected Namespaces (Granular Control)
**Goal:** Reduce resource consumption and scope security controls.

→ Lines 582-621: Enabling Tekton Chains to operate only in selected namespaces
  Source: Chapter 2, Namespace filtering

- **Task:** Add `--namespace=<namespace>` argument to Tekton Chains controller
- **Benefits:**
  - Reduced resource consumption by limiting watched namespaces
  - Security controls apply only where needed
  - Minimal blast radius of misconfiguration

---

### Job 3: Generate Cryptographic Keys for Artifact Signing
*When I need to enable Tekton Chains to sign task runs and pipeline runs*

**Personas:** Security engineer, Cluster administrator
**Requires:** Access to `openshift-pipelines` namespace

→ Lines 631-656: Secrets for signing data in Tekton Chains
  Source: Chapter 3, Introduction

**Context:** Tekton Chains requires a private key and password stored in the `signing-secrets` secret in the `openshift-pipelines` namespace.

#### 3.1 Choose Signing Scheme
**Goal:** Select between cosign and x509 based on requirements.

**Signing scheme comparison:**

| Scheme | Use Case | Key Type | Tools Required |
|--------|----------|----------|----------------|
| cosign | Modern container signing, Sigstore integration | ECDSA | cosign or skopeo |
| x509 | Traditional PKI, enterprise CA integration | RSA/ECDSA | openssl |

**Recommendation:** Use cosign for container-focused pipelines; use x509 for PKI integration.

#### 3.2 Generate Cosign Keys Automatically (Operator Method)
**Goal:** Quickly provision cosign keys without CLI tools.

→ Lines 664-731: Generating the cosign key pair using the TektonConfig CR
  Source: Chapter 3, Cosign automatic generation

**For cluster administrators:**

- **Task:** Set `generateSigningSecret: true` in TektonConfig CR
  ```bash
  oc edit TektonConfig config
  ```
  Update:
  ```yaml
  spec:
    chain:
      generateSigningSecret: true
  ```

- **Task:** Extract public key for verification
  ```bash
  oc get secret signing-secrets -n openshift-pipelines -o jsonpath='{.data.cosign\.pub}' | base64 -d
  ```

**Benefits:**
- Key generation completes in under 2 minutes
- No manual cosign CLI usage required
- Keys stored in correct secret location automatically

#### 3.3 Generate Cosign Keys Manually (CLI Method)
**Goal:** Maintain full control over key generation parameters.

→ Lines 738-762: Manually generating signing secrets with the cosign tool
  Source: Chapter 3, Cosign manual generation

**For security engineers:**

- **Task:** Generate cosign key pair with custom passphrase
  ```bash
  cosign generate-key-pair k8s://openshift-pipelines/signing-secrets
  ```
- **Benefits:**
  - Maximum control over encryption parameters
  - Custom passphrase selection
  - Minimal dependency on operator-generated keys

#### 3.4 Generate Cosign Keys with Skopeo (Alternative Method)
**Goal:** Use skopeo for sigstore-compatible key generation.

→ Lines 770-853: Manually generating signing secrets with the skopeo tool
  Source: Chapter 3, Skopeo key generation

**For security engineers:**

- **Task:** Generate key pair with skopeo
  ```bash
  skopeo generate-sigstore-key --output-prefix <mykey>
  ```
- **Task:** Base64 encode private and public keys
- **Task:** Create Kubernetes secret with encoded keys
  ```bash
  oc create secret generic signing-secrets \
    --from-literal=cosign.key=<base64_private_key> \
    --from-literal=cosign.pub=<base64_public_key> \
    -n openshift-pipelines
  ```

**Benefits:**
- Integration with existing skopeo workflows
- Keys compatible with cosign signing scheme
- Minimal migration effort from skopeo usage

#### 3.5 Troubleshoot Secret Conflicts
**Goal:** Resolve "secret already exists" errors.

→ Lines 860-887: Resolving the 'secret already exists' error
  Source: Chapter 3, Troubleshooting

- **Task:** Delete existing secret
  ```bash
  oc delete secret signing-secrets -n openshift-pipelines
  ```
- **Task:** Recreate secret with new keys

---

### Job 4: Configure OCI Registry Authentication for Signature Storage
*When I need to push signed artifacts to an OCI registry*

**Personas:** Platform engineer
**Requires:** OCI registry accessible, Docker config credentials

→ Lines 897-965: Authenticating to an OCI registry
  Source: Chapter 4, OCI authentication

**Context:** Tekton Chains controller uses the service account that starts task runs to push signatures to registries.

#### 4.1 Create Custom Service Account (Best Practice)
**Goal:** Avoid pod timeouts and operator overrides of the default service account.

**For platform engineers:**

- **Task:** Create custom service account
  ```bash
  oc create serviceaccount <service-account-name> -n <namespace>
  ```

- **Task:** Create Kubernetes secret with registry credentials
  ```bash
  oc create secret docker-registry <secret-name> \
    --docker-server=<registry-url> \
    --docker-username=<username> \
    --docker-password=<token>
  ```

- **Task:** Patch service account with `imagePullSecrets`
  ```bash
  oc patch serviceaccount <service-account-name> -n <namespace> \
    -p '{"imagePullSecrets":[{"name":"<secret-name>"}]}'
  ```

- **Task:** Configure task runs or pipeline runs to use custom service account
  ```yaml
  spec:
    serviceAccountName: <service-account-name>
  ```

**Benefits:**
- Elimination of pod timeout issues
- Service account has correct permissions
- Minimal disruption from operator upgrades

#### 4.2 Assign Appropriate Security Context Constraint
**Goal:** Ensure service account has required SCC for pod execution.

→ Lines 938-964: Authenticating to an OCI registry (SCC context)
  Source: Chapter 4, SCC configuration

- **Task:** Assign `pipelines-scc` or custom SCC to service account
- **Why:** Default service account may be overridden by operator; custom SA provides stability

---

### Job 5: Verify Signing Workflow Without Additional Authentication
*When I need to validate that Tekton Chains is correctly signing artifacts*

**Personas:** Security engineer
**Requires:** Tekton Chains configured, signing keys generated, cosign installed

→ Lines 973-1082: Creating and verifying task run signatures without any additional authentication
  Source: Chapter 5, Signing verification

#### 5.1 Configure Tekton Backend Storage for Testing
**Goal:** Store signatures as annotations for easy retrieval.

→ Lines 996-1013: Configure backend storage
  Source: Chapter 5, Backend configuration

- **Task:** Edit TektonConfig to use tekton storage
  ```yaml
  artifacts.oci.storage: ""
  artifacts.taskrun.format: tekton
  artifacts.taskrun.storage: tekton
  ```

**Benefits:**
- Signatures accessible via Kubernetes API
- Minimal external storage dependencies
- Quick signature retrieval for testing

#### 5.2 Create and Sign a Task Run (Execution Step)
**Goal:** Generate a signed task run for verification.

- **Task:** Create a simple task run
- **Verification:** Tekton Chains automatically signs the task run after completion

#### 5.3 Retrieve Signature and Payload (Confirmation Step)
**Goal:** Extract the signature from task run annotations.

- **Task:** Retrieve signature annotation
  ```bash
  oc get taskrun <taskrun-name> -o jsonpath='{.metadata.annotations.chains\.tekton\.dev/signature-taskrun-<uuid>}'
  ```
- **Task:** Retrieve payload annotation
  ```bash
  oc get taskrun <taskrun-name> -o jsonpath='{.metadata.annotations.chains\.tekton\.dev/payload-taskrun-<uuid>}'
  ```

#### 5.4 Verify Signature with Cosign (Validation Step)
**Goal:** Cryptographically verify the task run signature.

- **Task:** Verify signature using cosign and public key
  ```bash
  cosign verify-blob --key k8s://openshift-pipelines/signing-secrets \
    --signature <signature> <payload>
  ```

**Benefits:**
- Minimal time to validate signing workflow
- Signatures are cryptographically valid
- Reduced risk of signing misconfiguration
- Confidence in supply chain security

---

### Job 6: Sign and Verify Container Images and Provenance
*When I need to prove image integrity and build provenance for compliance*

**Personas:** Security engineer
**Requires:** Tekton Chains configured, signing keys generated, OCI registry authentication configured

→ Lines 1096-1237: Using Tekton Chains to sign and verify image and provenance
  Source: Chapter 6, Image and provenance signing

#### 6.1 Configure Tekton Chains for Image and Provenance Signing
**Goal:** Set artifact format and storage for OCI images and attestations.

→ Lines 1137-1151: Configure Chains for image signing
  Source: Chapter 6, Chains configuration

- **Task:** Set task run format to `in-toto` or `slsa/v1`
- **Task:** Set task run storage to `oci`
- **Task:** Enable transparency log upload to Rekor
  ```bash
  oc patch configmap chains-config -n openshift-pipelines \
    -p='{"data":{"transparency.enabled": "true"}}'
  ```

**Benefits:**
- Provenance is publicly verifiable via Rekor
- End-to-end build provenance is signed
- Transparency log integration enabled

#### 6.2 Build Image with Kaniko Task (Execution Step)
**Goal:** Create an OCI image that Tekton Chains will automatically sign.

- **Task:** Create task run using Kaniko task
- **Task:** Specify target image URL with `IMAGE_URL` parameter
- **Verification:** Tekton Chains signs image and provenance after build completes

**Note:** Task must emit `IMAGE_URL` result for Chains to detect the image.

#### 6.3 Verify Signed Image (Validation Step)
**Goal:** Confirm image signature is valid.

- **Task:** Verify image signature with cosign
  ```bash
  cosign verify --key k8s://openshift-pipelines/signing-secrets <image-url>
  ```

#### 6.4 Verify Signed Provenance Attestation (Validation Step)
**Goal:** Confirm provenance attestation is valid.

- **Task:** Verify attestation with cosign
  ```bash
  cosign verify-attestation --key k8s://openshift-pipelines/signing-secrets \
    --type slsaprovenance <image-url>
  ```

#### 6.5 Search Rekor for Public Provenance Records (Transparency Step)
**Goal:** Prove build provenance is publicly auditable.

→ Lines 1209-1237: Find provenance in Rekor
  Source: Chapter 6, Rekor search

- **Task:** Get image digest
  ```bash
  cosign triangulate <image-url>
  ```

- **Task:** Search Rekor by image digest
  ```bash
  rekor-cli search --sha <image-digest>
  ```

- **Task:** Retrieve attestation record
  ```bash
  rekor-cli get --uuid <uuid> --format json
  ```

**Benefits:**
- Minimal time to find provenance records
- Attestation is discoverable in transparency log
- Third-party verification of builds is enabled
- Tamper-proof audit trail created

---

## Observe Supply Chain Security

### Job 7: Visualize Security Artifacts in OpenShift Web Console
*When I need to assess security posture without CLI tools*

**Personas:** DevOps engineer, Security engineer
**Requires:** Tekton Chains configured, vulnerability scanning task, SBOM generation task

→ Lines 1305-1326: Setting up OpenShift Pipelines to view Software Supply Chain Security elements
  Source: Chapter 7, UI visibility

**Context:** OpenShift web console displays signed badges, vulnerabilities, and SBOMs for pipeline runs.

#### 7.1 View Signed Pipeline Run Badges (Visual Indicator)
**Goal:** Quickly identify pipeline runs that meet Tekton Chains signing requirements.

**What you see:**
- Signed badge appears next to pipeline run names when provenance is signed
- Badge visible in both Administrator and Developer perspectives

**Benefits:**
- Immediate visual confirmation of signed artifacts
- Reduced friction in security review workflows

#### 7.2 View Vulnerability Scan Results by Severity (Risk Assessment)
**Goal:** Prioritize security remediation based on vulnerability severity.

→ Lines 1334-1477: Setting up OpenShift Pipelines to view project vulnerabilities
  Source: Chapter 7, Vulnerability visibility

**For security engineers:**

- **Task:** Configure vulnerability scan task to output severity counts
  ```bash
  jq -rce '{vulnerabilities:{ 
    critical: (.result.summary.CRITICAL), 
    high: (.result.summary.IMPORTANT), 
    medium: (.result.summary.MODERATE), 
    low: (.result.summary.LOW) 
  }}'
  ```

- **Task:** Store output in `SCAN_OUTPUT` result of type `external-link`

- **Task:** Reference `SCAN_OUTPUT` in pipeline configuration

**What you see:**
- Visual representation of vulnerabilities by severity (critical, high, medium, low)
- Vulnerability counts in PipelineRun details page
- Vulnerability column in pipeline run list view

**Benefits:**
- Minimal time to identify critical vulnerabilities
- Visual prioritization by severity
- Reduced manual parsing of scan results
- Vulnerability data accessible to all stakeholders

#### 7.3 View or Download Software Bill of Materials (SBOM Analysis)
**Goal:** Understand software composition for compliance and risk assessment.

→ Lines 1486-1665: Setting up OpenShift Pipelines to download or view SBOMs
  Source: Chapter 7, SBOM visibility

**For DevOps engineers:**

- **Task:** Configure SBOM generation task to output SBOM link
  ```yaml
  results:
    - name: LINK_TO_SBOM
      type: external-link
      value: $(SBOM_URL)
  ```

- **Task:** Configure pipeline to emit `IMAGE_URL` result

**For security engineers viewing SBOMs:**

→ Lines 1569-1586: Viewing an SBOM in the web UI
  Source: Chapter 7, SBOM web viewing

- **Task:** Navigate to Activity → PipelineRuns tab
- **Task:** Select View SBOM link
- **Task:** Search SBOM for vulnerable libraries (e.g., log4j)

**Benefits:**
- Minimal time to access SBOM data
- In-browser vulnerability assessment
- Reduced need for CLI tools
- Transparency into software composition

→ Lines 1588-1616: Downloading an SBOM in the CLI
  Source: Chapter 7, SBOM CLI download

**For platform engineers:**

- **Task:** Download SBOM via cosign CLI
  ```bash
  cosign download sbom <image-url>
  ```

**Benefits:**
- Automated SBOM processing for compliance workflows
- Machine-readable SBOM data

→ Lines 1618-1665: Reading the SBOM
  Source: Chapter 7, SBOM interpretation

**SBOM contents:**
- Library author or publisher
- Library name
- Library version
- Library licenses

**Use cases:**
- Verify dependencies are safely-sourced
- Confirm libraries are updated
- Ensure license compliance
- Assess risk from outdated or vulnerable libraries

---

## Secure Pipeline Execution

### Job 8: Control Security Permissions for Pipeline Pods
*When I need to enforce least-privilege principles for task and pipeline runs*

**Personas:** Cluster administrator, Security engineer
**Requires:** OpenShift Pipelines installed

→ Lines 1731-1766: Configuring the security context for pods
  Source: Chapter 8, Security context configuration

**Context:** The default service account for pipeline pods is `pipeline` with SCC `pipelines-scc`. Cluster administrators can configure security context constraints (SCC) globally, per-namespace, or per-run.

#### 8.1 Configure Default and Maximum SCC Globally (Cluster-Wide Policy)
**Goal:** Enforce organization-wide security baselines for all pipelines.

→ Lines 1774-1807: Configuring default and maximum SCC for pods
  Source: Chapter 8, Global SCC configuration

**For cluster administrators:**

- **Task:** Edit TektonConfig custom resource
  ```yaml
  spec:
    platforms:
      openshift:
        scc:
          default: <default-scc-name>
          maxAllowed: <max-scc-name>
  ```

**Benefits:**
- Consistent security policies across namespaces
- Minimal risk of overly permissive SCCs
- Centralized security control
- Reduced per-namespace configuration effort

#### 8.2 Configure SCC for Specific Namespace (Namespace Policy)
**Goal:** Override default SCC for pipelines in specific environments.

→ Lines 1820-1842: Configuring the SCC for pods in a namespace
  Source: Chapter 8, Namespace SCC configuration

**For cluster administrators:**

- **Task:** Annotate namespace with desired SCC
  ```bash
  oc annotate namespace <namespace> \
    operator.tekton.dev/scc=<scc-name>
  ```

**Constraints:** SCC must not exceed `maxAllowed` configured in TektonConfig

**Benefits:**
- Namespace-level security customization
- SCC enforcement within maximum allowed
- Minimal per-pipeline configuration

#### 8.3 Run Pipeline with Custom SCC and Service Account (Run-Specific Policy)
**Goal:** Avoid pod timeouts and enable specific capabilities for individual runs.

→ Lines 1851-1975: Running pipeline run and task run with custom SCC and service account
  Source: Chapter 8, Custom SCC configuration

**Context:** Default `pipelines-scc` has `fsGroup.type: MustRunAs` which can cause pod timeouts (BZ#1995779).

**For platform engineers:**

- **Task:** Create custom SCC with `fsGroup.type: RunAsAny`
  ```yaml
  allowPrivilegeEscalation: false
  fsGroup:
    type: RunAsAny
  ```

- **Task:** Create custom service account
  ```bash
  oc create serviceaccount <custom-sa> -n <namespace>
  ```

- **Task:** Create ClusterRole and RoleBinding to associate SCC with service account

- **Task:** Configure pipeline run or task run to use custom service account
  ```yaml
  spec:
    serviceAccountName: <custom-sa>
  ```

**Benefits:**
- Elimination of pod timeout errors
- SCC appropriate for workload requirements
- Minimal upgrade disruption
- Stable pipeline execution

---

### Job 9: Secure Webhook Endpoints with Event Listeners
*When I need to protect webhook endpoints from unauthorized access*

**Personas:** Cluster administrator, Security engineer, DevOps engineer
**Requires:** Create namespace, Install OpenShift Pipelines Operator

→ Lines 2044-2063: Securing webhooks with event listeners
  Source: Chapter 9, Webhook security

**Context:** Enable HTTPS for event listeners to ensure secure communication within and outside the cluster.

#### 9.1 Enable HTTPS for Event Listeners (Label-Based Activation)
**Goal:** Enable HTTPS with automatic certificate generation.

- **Task:** Add label to namespace
  ```bash
  oc label namespace <namespace> \
    operator.tekton.dev/enable-annotation=enabled
  ```

**Benefits:**
- Minimal risk of webhook data interception
- Encrypted connections to event listeners
- Both internal and external secure access enabled

#### 9.2 Expose Webhooks Externally with Routes (External Access)
**Goal:** Maintain end-to-end encryption from client to event listener.

→ Lines 2071-2131: Providing secure connection with OpenShift routes
  Source: Chapter 9, Route configuration

**For cluster administrators:**

- **Task:** Create route with `reencrypt` TLS termination
  ```bash
  oc create route reencrypt --service=<eventlistener-service> \
    --cert=tls.crt --key=tls.key --ca-cert=ca.crt
  ```

**Benefits:**
- End-to-end encryption for webhook traffic
- Minimal certificate management complexity
- Secure external access to event listeners

#### 9.3 Configure Security Context for Event Listeners (Privilege Restriction)
**Goal:** Ensure event listener containers run with restricted privileges.

→ Lines 2142-2183: Configuring security context for event listeners
  Source: Chapter 9, Security context configuration

**For security engineers:**

- **Task:** Configure EventListener CR with security context
  ```yaml
  spec:
    podTemplate:
      securityContext:
        runAsNonRoot: true
        seccompProfile:
          type: RuntimeDefault
      containers:
        - securityContext:
            allowPrivilegeEscalation: false
            readOnlyRootFilesystem: true
            capabilities:
              drop:
                - ALL
  ```

**Benefits:**
- Event listeners run as non-root users
- Minimal attack surface through read-only filesystems
- Compliance with OpenShift security context constraints

#### 9.4 Create Sample Secure EventListener (Quick Start)
**Goal:** Understand complete configuration flow for secure webhooks.

→ Lines 2192-2242: Creating a sample EventListener resource using a secure HTTPS connection
  Source: Chapter 9, Example configuration

**For DevOps engineers:**

- **Task:** Create TriggerBinding, TriggerTemplate, and Trigger resources
- **Task:** Create EventListener with HTTPS label
  ```yaml
  metadata:
    labels:
      operator.tekton.dev/enable-annotation: enabled
  ```

**Benefits:**
- Minimal time to get working secure webhook example
- Reduced likelihood of misconfiguration
- Understanding of label-based HTTPS enablement

---

### Job 10: Authenticate Pipelines to Git and Container Repositories
*When pipelines need to interact with protected repositories*

**Personas:** DevOps engineer, Security engineer
**Requires:** Service account or workspace, repository credentials

→ Lines 2246-2316: Authenticating pipelines with repositories using secrets
  Source: Chapter 10, Repository authentication

**Context:** Pipelines use secrets for authenticated access to Git and container repositories during execution.

#### Approach A: Using Service Accounts (Automatic Credential Mounting)

**Best for:** Centralized credential management, minimal per-task configuration

**Personas:** DevOps engineer, Security engineer

→ Lines 2324-2332: Providing secrets using service accounts
  Source: Chapter 10, Service account approach

**How it works:**
- Associate secrets with service accounts
- Credentials automatically available to tasks running under that service account
- No manual credential passing in task definitions

##### A.1 Understand Secret Types and Annotations
**Goal:** Correctly specify which repositories each secret applies to.

→ Lines 2338-2455: Types and annotation of secrets for service accounts
  Source: Chapter 10, Secret types

**Secret types for Git:**
- `kubernetes.io/basic-auth` (username + password/token)
- `kubernetes.io/ssh-auth` (SSH private key + known_hosts)

**Secret types for container registries:**
- `kubernetes.io/basic-auth`
- `kubernetes.io/dockercfg`
- `kubernetes.io/dockerconfigjson`

**Annotations:**
- `tekton.dev/git-0`, `tekton.dev/git-1`, ... (for Git URLs)
- `tekton.dev/docker-0`, `tekton.dev/docker-1`, ... (for registry URLs)

**Benefits:**
- Minimal authentication failures from incorrect secret types
- Proper secret-to-repository mapping
- Support for multiple repositories

##### A.2 Configure Basic HTTP Authentication for Git
**Goal:** Enable password-protected Git repository access with personal access tokens.

→ Lines 2463-2566: Configuring Basic HTTP authentication for Git using a service account
  Source: Chapter 10, Basic HTTP Git auth

- **Task:** Create secret with username and token
  ```bash
  oc create secret generic <secret-name> \
    --type=kubernetes.io/basic-auth \
    --from-literal=username=<username> \
    --from-literal=password=<token>
  ```

- **Task:** Annotate secret with Git URL
  ```bash
  oc annotate secret <secret-name> \
    tekton.dev/git-0=https://github.com
  ```

- **Task:** Associate secret with service account
  ```bash
  oc patch serviceaccount <sa-name> \
    -p '{"secrets":[{"name":"<secret-name>"}]}'
  ```

- **Task:** Configure TaskRun or PipelineRun with service account
  ```yaml
  spec:
    serviceAccountName: <sa-name>
  ```

**Benefits:**
- Authenticated Git clone operations in pipelines
- Minimal credential exposure in pipeline definitions
- GitHub personal access token authentication support

##### A.3 Configure SSH Authentication for Git
**Goal:** Enable secure Git repository access using SSH private keys.

→ Lines 2574-2676: Configuring SSH authentication for Git using a service account
  Source: Chapter 10, SSH Git auth

- **Task:** Create secret with SSH private key and known_hosts
  ```bash
  oc create secret generic <secret-name> \
    --type=kubernetes.io/ssh-auth \
    --from-file=ssh-privatekey=<private-key-file> \
    --from-file=known_hosts=<known-hosts-file>
  ```

- **Task:** Annotate secret with Git URL (supports custom ports)
  ```bash
  oc annotate secret <secret-name> \
    tekton.dev/git-0=github.com:2222
  ```

- **Task:** Associate secret with service account and configure run

**Benefits:**
- SSH-based Git clone operations in pipelines
- Minimal risk of man-in-the-middle attacks via known_hosts
- Custom SSH port support

##### A.4 Configure Container Registry Authentication
**Goal:** Enable authenticated image pull and push operations.

→ Lines 2684-2768: Configuring container registry authentication by using a service account
  Source: Chapter 10, Registry auth

- **Task:** Create secret from Docker config.json
  ```bash
  oc create secret generic <secret-name> \
    --from-file=.dockerconfigjson=<path-to-config.json> \
    --type=kubernetes.io/dockerconfigjson
  ```

- **Task:** Annotate secret with registry URL
  ```bash
  oc annotate secret <secret-name> \
    tekton.dev/docker-0=quay.io
  ```

- **Task:** Associate secret with service account and configure run

**Benefits:**
- Authenticated image pull and push operations
- Minimal credential exposure
- Support for multiple container registries

##### A.5 Handle SSH Authentication in Custom Tasks
**Goal:** Ensure Git finds SSH authentication files when running custom commands.

→ Lines 2790-2820: SSH Git authentication in tasks
  Source: Chapter 10, SSH in tasks

- **Task:** Symlink SSH directories in task steps
  ```bash
  ln -s $HOME/.ssh /root/.ssh
  ```

**Why:** Git ignores `$HOME` variable and uses `/etc/passwd` entry, requiring symlink for authentication to work.

**Note:** Not required when using `git-clone` task from Tekton Hub.

##### A.6 Run Tasks as Non-Root User with SSH Authentication
**Goal:** Enable SSH authentication without root privileges.

→ Lines 2827-2846: Use of secrets as a non-root user
  Source: Chapter 10, Non-root SSH

- **Task:** Ensure valid home directory in `/etc/passwd`
- **Task:** Symlink `$HOME` to actual home directory
- **Note:** Platform may randomize user/group IDs for security

**Benefits:**
- SSH authentication for non-root task execution
- Minimal privilege escalation risks

---

#### Approach B: Using Workspaces (Runtime Credential Binding)

**Best for:** Flexible credential passing per task run, avoiding service account coupling

**Personas:** DevOps engineer, Security engineer

→ Lines 2854-2864: Providing secrets using workspaces
  Source: Chapter 10, Workspace approach

**How it works:**
- Define named workspace in task
- Bind secret to workspace at runtime
- No annotations required on secrets

**Benefits:**
- Minimal annotation management overhead
- Flexible credential passing per task run
- Reduced coupling between secrets and service accounts

##### B.1 Configure SSH Authentication for Git via Workspaces
**Goal:** Pass Git credentials at task runtime without service account annotations.

→ Lines 2872-2998: Configuring SSH authentication for Git using workspaces
  Source: Chapter 10, SSH workspace

- **Task:** Create secret from `.ssh` directory
  ```bash
  oc create secret generic <secret-name> \
    --from-file=id_ed25519=<private-key> \
    --from-file=known_hosts=<known-hosts>
  ```

- **Task:** Define `ssh-directory` workspace in task
  ```yaml
  workspaces:
    - name: ssh-directory
  ```

- **Task:** Access workspace in task steps
  ```bash
  cp -R $(workspaces.ssh-directory.path) $HOME/.ssh
  chmod 400 $HOME/.ssh/id_ed25519
  ```

- **Task:** Run task with workspace secret binding
  ```bash
  tkn task start <task-name> \
    --workspace name=ssh-directory,secret=<secret-name>
  ```

**Benefits:**
- Workspace-based SSH authentication for Git
- Minimal service account annotation requirements
- Runtime credential selection per task invocation

##### B.2 Configure Container Registry Authentication via Workspaces
**Goal:** Pass Docker credentials at task runtime without service account annotations.

→ Lines 3005-3089: Configuring container registry authentication using workspaces
  Source: Chapter 10, Registry workspace

- **Task:** Create secret from `config.json`
  ```bash
  oc create secret generic <secret-name> \
    --from-file=config.json=<path-to-config.json>
  ```

- **Task:** Define `dockerconfig` workspace in task
  ```yaml
  workspaces:
    - name: dockerconfig
  ```

- **Task:** Set `DOCKER_CONFIG` environment variable to workspace path
  ```yaml
  env:
    - name: DOCKER_CONFIG
      value: $(workspaces.dockerconfig.path)
  ```

- **Task:** Run task with workspace secret binding
  ```bash
  tkn task start <task-name> \
    --workspace name=dockerconfig,secret=<secret-name>
  ```

**Benefits:**
- Workspace-based registry authentication
- Support for tools like Skopeo that use `DOCKER_CONFIG`

##### B.3 Limit Secret Access to Specific Steps
**Goal:** Minimize credential exposure to only steps requiring authentication.

→ Lines 3095-3134: Limiting a secret to particular steps using workspaces
  Source: Chapter 10, Step-level workspace

- **Task:** Define workspace in task spec
- **Task:** Define workspace in specific step spec (not all steps)
- **Result:** Only steps with workspace definition can access credentials

**Benefits:**
- Minimal credential exposure to unnecessary steps
- Only authenticated steps access secrets
- Reduced attack surface within multi-step tasks

---

### Job 11: Build Container Images as Non-Root User with Buildah
*When I need to reduce security exposure from container build processes*

**Personas:** Security engineer, DevOps engineer
**Requires:** Understanding of security context constraints, buildah task available

→ Lines 3137-3207: Building of container images using Buildah as a non-root user
  Source: Chapter 11, Non-root Buildah builds

**Context:** Running pipelines as root can expose container processes and the host to malicious resources. Running Buildah as non-root user reduces this exposure.

#### Approach A: User Namespaces (Simplest Method)

**Best for:** Minimizing configuration complexity, automatic user mapping

**Personas:** DevOps engineer

→ Lines 3214-3284: Running Buildah as a non-root user by configuring user namespaces
  Source: Chapter 11, User namespace method

##### A.1 Configure User Namespaces with Annotations
**Goal:** Enable unprivileged builds without custom service accounts or SCCs.

- **Task:** Copy buildah task from `openshift-pipelines` namespace to custom task

- **Task:** Add annotation to task metadata
  ```yaml
  metadata:
    annotations:
      io.kubernetes.cri-o.userns-mode: "auto:size=65536;map-to-root=true"
  ```

- **Task:** Configure stepTemplate with security context
  ```yaml
  stepTemplate:
    securityContext:
      runAsNonRoot: true
      runAsUser: 1000
      capabilities:
        add:
          - SETFCAP
  ```

**Benefits:**
- Minimal configuration complexity
- Automatic user namespace mapping
- Reduced need for custom SCCs

---

#### Approach B: Custom Service Account and SCC (Explicit Control Method)

**Best for:** Images that fail with user namespaces, requiring explicit privilege controls

**Personas:** Security engineer

→ Lines 3293-3304: Running Buildah as a non-root user by defining a custom SA and SCC
  Source: Chapter 11, SA and SCC method

**Context:** User namespace configuration may not work for all images. Custom SA and SCC provide more control.

##### B.1 Create Custom Service Account and Security Context Constraint
**Goal:** Reduce dependency on default pipeline SA while enabling required capabilities.

→ Lines 3312-3408: Configuring custom service account and security context constraint
  Source: Chapter 11, SA and SCC configuration

- **Task:** Create custom service account
  ```bash
  oc create serviceaccount pipelines-sa-userid-1000 -n <namespace>
  ```

- **Task:** Create custom SCC with user ID restriction
  ```yaml
  apiVersion: security.openshift.io/v1
  kind: SecurityContextConstraints
  metadata:
    name: pipelines-scc-userid-1000
  allowPrivilegeEscalation: true
  runAsUser:
    type: MustRunAs
    uid: 1000
  supplementalGroups:
    type: RunAsAny
  fsGroup:
    type: RunAsAny
  seLinuxContext:
    type: RunAsAny
  capabilities:
    allowedCapabilities:
      - SETUID
      - SETGID
  ```

- **Task:** Create ClusterRole referencing SCC

- **Task:** Create RoleBinding to associate SCC with service account

**Benefits:**
- Minimal dependency on default pipeline service account
- Pods run as specific non-root user ID 1000
- SETUID and SETGID capabilities enabled for Buildah

##### B.2 Configure Buildah Task to Use Build User
**Goal:** Modify Buildah task to run as user ID 1000 with proper volume mounts.

→ Lines 3416-3526: Configuring Buildah to use build user
  Source: Chapter 11, Buildah user configuration

- **Task:** Copy buildah task to `buildah-as-user` task

- **Task:** Add security context to steps
  ```yaml
  securityContext:
    runAsUser: 1000
  ```

- **Task:** Add user verification command
  ```bash
  echo "Running as USER=$(id)"
  ```

- **Task:** Configure volume mount for build user home
  ```yaml
  volumeMounts:
    - name: varlibcontainers
      mountPath: /home/build/.local/share/containers
  ```

**Benefits:**
- Buildah runs as build user with ID 1000
- Storage mounted to correct user home directory
- Task execution as non-root confirmed via logging

##### B.3 Execute Builds with Custom Service Account
**Goal:** Run image builds as user ID 1000 with proper authentication.

→ Lines 3534-3668: Starting a task run with custom config map, or a pipeline run
  Source: Chapter 11, Task and pipeline run execution

**For TaskRun:**

- **Task:** Create TaskRun with custom service account
  ```yaml
  spec:
    serviceAccountName: pipelines-sa-userid-1000
    taskRef:
      name: buildah-as-user
  ```

**For PipelineRun:**

- **Task:** Create PipelineRun with task-specific service account
  ```yaml
  spec:
    taskServiceAccountName:
      buildah: pipelines-sa-userid-1000
  ```

**Benefits:**
- Buildah builds execute with custom service account
- Integration with pipeline workflows
- Support for both standalone TaskRun and PipelineRun

##### B.4 Understand Limitations of Unprivileged Builds
**Goal:** Diagnose build failures due to known unprivileged constraints.

→ Lines 3676-3691: Limitations of unprivileged builds
  Source: Chapter 11, Build limitations

**Known limitations:**
- `--mount=type=cache` may fail due to permissions
- `--mount=type=secret` fails due to lack of mounting capabilities

**Benefits:**
- Minimal time diagnosing unprivileged build failures
- Understanding of Dockerfile features requiring additional capabilities
- Identification of workarounds for unsupported mount options

---

#### Approach C: buildah-ns Task (Maximum Security Method)

**Best for:** Maximum security through kernel-level isolation, no container runtime daemons

**Personas:** Security engineer

→ Lines 3700-3772: Using buildah-ns Tekton task
  Source: Chapter 11, buildah-ns introduction

**Context:** The `buildah-ns` task uses user namespace isolation for enhanced security at the kernel level.

##### C.1 Understand buildah-ns vs buildah Differences
**Goal:** Select the task with appropriate security model.

→ Lines 3779-3797: Differences between buildah and buildah-ns tasks
  Source: Chapter 11, buildah-ns comparison

**Key differences:**

| Feature | buildah | buildah-ns |
|---------|---------|------------|
| Task name | `buildah` | `buildah-ns` |
| User namespace | Manual config | Automatic via annotation |
| Annotation | None | `io.kubernetes.cri-o.userns-mode: auto` |
| Builder annotation | None | `io.openshift.builder: true` |
| UID mapping | Manual | Automatic kernel-level |

**Benefits:**
- Automatic user namespace mapping
- Minimal configuration for maximum security

##### C.2 Understand buildah-ns Security Model
**Goal:** Verify how UID mapping provides kernel-level isolation.

→ Lines 3804-3825: Security model of the buildah-ns task
  Source: Chapter 11, buildah-ns security model

**Security model:**
- **Inside container:** Processes run as UID 0 (root)
- **Outside container:** Same processes run as non-zero UID on host

**Advantages:**
- Kernel-level isolation between containers
- Reduced privilege exposure on host system
- Container escape protection through UID mapping

**Benefits:**
- Processes appear as root inside container but non-root on host
- Minimal kernel-level privilege exposure
- Reduced impact of container escape vulnerabilities

##### C.3 Configure buildah-ns Task Execution
**Goal:** Provide correct inputs and retrieve build outputs.

→ Lines 3832-3915: Workspaces, parameters, and results for the buildah-ns task
  Source: Chapter 11, buildah-ns configuration

**Required:**
- **Workspace:** `source` (with Containerfile or Dockerfile)
- **Parameter:** `IMAGE` (target image name and tag)

**Optional parameters:**
- `CONTAINERFILE_PATH` (default: `./Dockerfile`)
- `TLS_VERIFY` (default: `true`)
- `VERBOSE` (default: `false`)
- `SUBDIRECTORY` (default: `.`)
- `STORAGE_DRIVER` (default: `overlay`)
- `BUILD_EXTRA_ARGS` (default: `""`)
- `PUSH_EXTRA_ARGS` (default: `""`)
- `SKIP_PUSH` (default: `false`)

**Results:**
- `IMAGE_URL` (fully qualified image name)
- `IMAGE_DIGEST` (image digest)

**Benefits:**
- Minimal configuration errors
- Understanding of required vs optional parameters
- Retrieval of fully qualified image name and digest

##### C.4 Execute buildah-ns Task
**Goal:** Build images with user namespace security.

→ Lines 3922-3972: Running the buildah-ns task
  Source: Chapter 11, buildah-ns execution

- **Task:** Create PipelineRun with buildah-ns task
  ```yaml
  spec:
    pipelineRef:
      name: task-buildah-ns
    params:
      - name: IMAGE
        value: <image-url>
      - name: TLS_VERIFY
        value: "true"
    workspaces:
      - name: source
        persistentVolumeClaim:
          claimName: <pvc-name>
  ```

- **Task:** Configure registry authentication if pushing to protected registry
  - Create Kubernetes secret with registry credentials
  - Link secret to service account

**Benefits:**
- buildah-ns task executes successfully
- Authenticated registry push if required
- Minimal manual configuration per build

---

## Appendices

### A. Signing Scheme Comparison

| Scheme | Key Type | Best For | Tools Required | Integration |
|--------|----------|----------|----------------|-------------|
| cosign | ECDSA | Modern container signing, Sigstore integration | cosign or skopeo | Rekor transparency log |
| x509 | RSA/ECDSA | Traditional PKI, enterprise CA integration | openssl | Enterprise CA systems |

### B. Storage Backend Comparison

| Backend | Best For | Accessibility | Production Ready | Authentication Required |
|---------|----------|---------------|------------------|-------------------------|
| `tekton` | Testing, development | Kubernetes API (annotations) | No | No |
| `oci` | Production | OCI registry | Yes | Yes (registry credentials) |
| `gcs` | Google Cloud | Google Cloud Storage | Yes | Yes (GCP credentials) |
| `docdb` | MongoDB integration | MongoDB | Yes | Yes (MongoDB credentials) |
| `grafeas` | Grafeas-based systems | Grafeas API | Yes | Yes (Grafeas credentials) |

### C. Service Account vs Workspace Authentication Decision Guide

| Factor | Service Account | Workspace |
|--------|----------------|-----------|
| **Credential management** | Centralized | Per-task runtime |
| **Annotation requirement** | Required | Not required |
| **Flexibility** | All tasks under SA use same creds | Different creds per task invocation |
| **Coupling** | Tightly coupled to SA | Loosely coupled |
| **Best for** | Standard workflows, consistent credentials | Dynamic credentials, testing |
| **Configuration complexity** | Higher (annotations, SA patching) | Lower (runtime binding) |

### D. Buildah Non-Root Methods Comparison

| Method | Complexity | SCC Required | When to Use |
|--------|------------|--------------|-------------|
| User namespaces (A) | Low | No custom SCC | Default choice, works for most images |
| Custom SA + SCC (B) | High | Yes (custom SCC) | User namespace fails, need explicit control |
| buildah-ns task (C) | Low | No custom SCC | Maximum security, automatic isolation |

**Recommendation:** Try user namespaces first; use custom SA + SCC if images fail; use buildah-ns for maximum security.

---

## Navigation Guide

### By User Journey

**Security Engineer implementing full supply chain security:**
1. Job 1: Understand Tekton Chains capabilities
2. Job 2: Configure Tekton Chains for organization
3. Job 3: Generate signing keys
4. Job 4: Configure OCI registry authentication
5. Job 5: Verify signing workflow
6. Job 6: Sign and verify images and provenance
7. Job 7: Enable UI visibility for security artifacts

**Cluster Administrator securing pipeline execution:**
1. Job 8: Configure security context constraints for pods
2. Job 9: Secure webhook endpoints with HTTPS
3. Job 10: Configure repository authentication
4. Job 11: Enable non-root container builds

**DevOps Engineer setting up authenticated pipelines:**
1. Job 10: Configure Git and registry authentication
   - Choose service account or workspace approach
   - Configure basic HTTP or SSH for Git
   - Configure registry authentication
2. Job 9: Create secure event listeners for webhooks
3. Job 11: Build container images securely

**Platform Engineer integrating with KMS:**
1. Job 2.4: Integrate Tekton Chains with enterprise KMS
2. Job 3: Generate signing keys (or use KMS-managed keys)
3. Job 4: Configure OCI registry authentication
4. Job 6: Sign and verify images with KMS-backed signatures

---

## Workflow Coverage

| Stage | Coverage | Jobs | Notes |
|-------|----------|------|-------|
| Plan | ⚠️ Limited | Job 11 (buildah comparison) | Minimal planning content; mostly execution-focused |
| Configure | ✅ | Jobs 2, 4 | Tekton Chains, OCI registry, KMS integration |
| Secure | ✅ | Jobs 1, 3, 5, 6, 8, 9, 10, 11 | Core focus: signing, authentication, access control |
| Deploy | ⚠️ Limited | Job 11 (buildah execution) | Limited deployment content; focus is on security configuration |
| Observe | ✅ | Job 7 | UI visibility for vulnerabilities, SBOMs, signed badges |
| Troubleshoot | ⚠️ Limited | Job 3 (secret conflicts), Job 11 (build limitations) | Minimal troubleshooting content |
| Upgrade | ❌ | - | No upgrade or migration content |
| Reference | ❌ | - | No dedicated reference material |

### Gaps Identified

| Stage | Gap | Recommendation |
|-------|-----|----------------|
| Plan | No decision framework for security architecture | Add "Choosing Security Approach" section with decision matrices |
| Troubleshoot | Limited troubleshooting for signature verification failures | Add "Troubleshooting Signature Verification" section |
| Upgrade | No upgrade procedures for Tekton Chains | Add "Upgrading Tekton Chains" section with version compatibility |
| Reference | No CLI command reference or API reference | Add "Command Reference" and "API Reference" appendices |
| Monitor | No observability for Tekton Chains controller | Add "Monitoring Tekton Chains" section with metrics and logs |

---

## Document Statistics

**Workflow Coverage:**
- Plan: 1 job (limited)
- Configure: 2 jobs
- Secure: 8 jobs (primary focus)
- Deploy: 1 job (limited)
- Observe: 1 job
- Troubleshoot: 2 jobs (limited)

**Main Jobs:** 11
**User Stories/Sections:** 50+ themed sections
**Source Sections:** 61 referenced
**Source Document Lines:** 3,972

**Personas:**
- Security engineer: 8 jobs
- Cluster administrator: 4 jobs
- Platform engineer: 3 jobs
- DevOps engineer: 7 jobs

**Document Focus:**
- Supply chain security: 54%
- Authentication and access control: 36%
- Pod security and non-root builds: 10%

---

# Understanding the Tekton Results Retention Policy
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** Configure and understand retention policies for Tekton Results and Records in the pipeline database.

**Personas:** Cluster administrator

**Main Jobs:** 4 core jobs across 2 workflow stages (Configure, Reference)

---

## Quick Navigation

**I want to:**
- Understand how retention policies work → Job 1 (Configure)
- Set default retention for all results → Job 2 (Configure)
- Create policies for specific namespaces or labels → Job 3 (Configure)
- Look up field definitions and defaults → Job 4 (Reference)

---

# Table of Contents

## Set Up & Configure

### Job 1: Understand Retention Policy Architecture
*When I need to manage how long pipeline results are kept*

**Personas:** Cluster administrator

#### Understanding the System

→ Lines 63-67: Abstract - Retention Policy Agent overview
  Source: Assembly header
  - How the Retention Policy Agent manages database pruning
  - Global defaults vs fine-grained rules
  - Configuration via config map

→ Lines 68-136: Sample YAML configuration
  Source: Assembly body
  - Complete TektonConfig example with retention settings
  - Basic structure: defaultRetention, policies, runAt

---

### Job 2: Configure Global Retention Defaults
*When I need to set default retention periods for all results*

**Personas:** Cluster administrator

**Requires:** Understanding of retention policy architecture

#### Configuration Fields

→ Lines 114-136: Config map field definitions
  Source: Field reference table
  - `runAt`: Cron schedule for pruning job (default: every Sunday at 7:07 a.m.)
  - `defaultRetention`: Fallback retention period (default: 30d)
  - `maxRetention`: Deprecated backward compatibility field
  - `policies`: Fine-grained policy list

→ Lines 68-112: Sample TektonConfig with global settings
  Source: YAML example
  - Setting `defaultRetention: 30m`
  - Configuring `runAt: '*/1 * * * *'` cron schedule
  - Using duration strings (30d, 24h) or numbers (days)

---

### Job 3: Define Fine-Grained Retention Policies
*When I need different retention periods for specific results*

**Personas:** Cluster administrator

**Requires:** Understanding of retention policy architecture, global defaults configured

**Why:** Optimize storage costs while retaining critical results longer

#### 3.1 Understanding Policy Selectors `[concept]`
**Goal:** Learn how to target specific results with policies

→ Lines 143-177: Fine-grained retention policies concept
  Source: Module op-fine-grained-retention-policies
  - Policy evaluation order (first match wins)
  - Selector fields: matchNamespaces, matchLabels, matchAnnotations, matchStatuses
  - AND logic across all selector types
  - Omitting selectors to match all results for that criterion

**Policy field reference table (lines 150-177):**
- `name`: Descriptive policy name
- `selector`: Criteria for matching Results (AND logic)
- `matchNamespaces`: List of target namespaces
- `matchLabels`: Map of label keys and possible values
- `matchAnnotations`: Map of annotation keys and possible values
- `matchStatuses`: List of final statuses (Succeeded, Failed, Cancelled, Running, Pending)
- `retention`: Retention period for matches

#### 3.2 Implementing Multi-Policy Strategies `[procedure]`
**Goal:** Configure multiple policies with correct precedence

→ Lines 178-217: Example ConfigMap with multiple policies
  Source: YAML example
  - Policy 1: retain-critical-failures-long-term (180d for production failures with high criticality)
  - Policy 2: retain-annotated-for-debug (14d for debug annotation)
  - Policy 3: default-production-policy (60d for all production namespaces)
  - Policy 4: short-term-ci-retention (7d for CI namespace)

→ Lines 219-226: Policy application examples
  Source: Scenario descriptions
  - How policies match: namespace + label + status combinations
  - Precedence demonstration (first matching policy wins)
  - Fallback to defaultRetention when no policy matches

**Example scenarios:**
- Failed Result in production with label `criticality: high` → 180 days (Policy 1)
- Any Result with annotation `debug/retain: "true"` → 14 days (Policy 2)
- Results in production/prod-east namespaces → 60 days (Policy 3)
- Results in CI namespace → 7 days (Policy 4)
- All other Results → 30 days (defaultRetention)

---

## Reference

### Job 4: Reference Retention Configuration Fields
*When I need to understand available retention configuration options*

**Personas:** Cluster administrator

#### Configuration Field Reference `[reference]`

→ Lines 114-136: Config map field table
  Source: Field definitions table
  - Complete field descriptions with defaults
  - Deprecated field warnings (maxRetention)
  - Cron format requirements for runAt
  - Duration string formats (30d, 24h) vs numbers

---

## Workflow Coverage

| Stage | Coverage | Jobs | Notes |
|-------|----------|------|-------|
| Configure | ✅ | Jobs 1, 2, 3 | Retention policy setup and fine-grained rules |
| Reference | ✅ | Job 4 | Field definitions and defaults |
| Monitor | ❌ | - | No observability for retention policy execution |
| Troubleshoot | ❌ | - | No troubleshooting content for retention issues |
| Upgrade | ❌ | - | No version upgrade or migration content |

### Gaps Identified

| Stage | Gap | Recommendation |
|-------|-----|----------------|
| Monitor | No visibility into pruning job execution or results | Add section on viewing pruning logs or cron job status |
| Troubleshoot | No guidance for common retention policy issues | Add troubleshooting section for policy matching failures, pruning errors |
| Upgrade | No migration guidance for maxRetention deprecation | Add migration steps from maxRetention to defaultRetention |

---

## Navigation Guide

### By User Journey

**Cluster Administrator setting up retention for the first time:**
1. Job 1: Understand Retention Policy Architecture
2. Job 2: Configure Global Retention Defaults
3. Job 3: Define Fine-Grained Retention Policies (if needed)
4. Job 4: Reference field definitions as needed

**Cluster Administrator optimizing storage costs:**
1. Job 3: Define Fine-Grained Retention Policies (Section 3.2)
2. Job 4: Reference field definitions for policy selectors

---

## Document Statistics

**Workflow Coverage:**
- Configure: 3 jobs
- Reference: 1 job
- Monitor: Gap identified
- Troubleshoot: Gap identified
- Upgrade: Gap identified

**Main Jobs:** 4
**User Stories/Paths:** 2 (policy understanding, policy implementation)
**Source Sections:** 5 (abstract, YAML examples, concept module, field table, scenarios)
**Total Lines:** 227 (small, focused document)

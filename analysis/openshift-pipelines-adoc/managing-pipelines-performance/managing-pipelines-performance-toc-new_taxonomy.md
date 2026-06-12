# Managing OpenShift Pipelines Performance
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** Help platform teams understand, plan, and optimize OpenShift Pipelines performance for high-concurrency workloads.

**Personas:** Platform Administrator, DevOps Engineer, Performance Engineer, CI/CD Engineer

**Main Jobs:** 2 core jobs across 3 workflow stages (Plan, Monitor, Optimize)

---

## Quick Navigation

**I want to:**
- Understand performance limits for concurrent pipelines → Job 1 (Plan)
- Fix slow or failing pipeline runs → Job 2 (Optimize)
- Scale cluster infrastructure for pipelines → Job 2 (Optimize)
- Enable high-availability mode → Job 2 (Optimize)
- Tune HA controller parameters → Job 2 (Optimize)

---

# Table of Contents

## Plan Capacity

### Job 1: Understand Performance Characteristics and Limitations
*When running a large number of concurrent pipeline tasks*

**Personas:** Platform Administrator, DevOps Engineer, CI/CD Engineer

**Why:** Setting realistic expectations for concurrent execution prevents unexpected failures and enables proper capacity planning

#### 1.1 Reference Performance Data

**Goal:** Establish baseline expectations based on Red Hat testing results.

→ Lines 64-76: Assembly abstract
  Source: Introduction

- **Test configuration:** 3-node OpenShift cluster on AWS m6a.2xlarge nodes
- **Concurrent pipeline limit:** Up to 60 simple test pipelines without significant failures
- **Performance degradation indicators:**
  - Increased failed pipeline runs
  - Higher average pipeline run duration
  - Increased pod creation latency
  - Deeper work queue depth
  - More pending pods
- **Version tested:** OpenShift Pipelines 1.13 (no significant difference from 1.12)
- **Note:** Results depend on test configuration; your performance may vary

---

## Optimize Performance

### Job 2: Improve Pipeline Performance Through Infrastructure and Configuration
*When experiencing slowness or recurrent failures of pipeline runs*

**Personas:** Platform Administrator, Performance Engineer, DevOps Engineer

**Timing:** AFTER Job 1 - understanding baseline performance helps identify appropriate optimizations

**Why:** Degraded performance impacts CI/CD velocity and team productivity; optimization requires infrastructure scaling AND controller configuration

#### 2.1 Monitor and Scale Infrastructure

**Goal:** Ensure adequate cluster capacity for concurrent pipeline execution.

**For Platform Administrator: Monitor node resource usage**

→ Lines 90-91: Resource monitoring approach
  Source: Section "Improving OpenShift Pipelines performance"

- **Task:** Monitor CPU and memory usage of cluster nodes running Pipelines
- **Task:** Identify resource capacity constraints
- **Validation:** High resource usage indicates need for scaling

**For Platform Administrator: Increase cluster nodes**

→ Lines 90-91: Infrastructure scaling
  Source: Section "Improving OpenShift Pipelines performance"

- **Task:** Add nodes to OpenShift cluster when resource usage is high
- **Outcome:** Provide adequate resources for concurrent pipeline execution
- **Note:** Prerequisite for high-availability configuration

#### 2.2 Enable High-Availability Mode (Recommended)

**Goal:** Reduce pipeline execution times and pod creation latency through distributed Tekton controller architecture.

**For Platform Administrator: Configure TektonConfig CR**

→ Lines 92-100: High-availability configuration
  Source: Section "Improving OpenShift Pipelines performance"

- **Task:** Set `pipeline.performance.disable-ha` to `false`
- **Task:** Set `pipeline.performance.buckets` to number between 5-10
- **Task:** Set `pipeline.performance.replicas` to number >2 and ≤buckets value
- **Outcome:** Significantly reduced pipeline execution times (confirmed in Red Hat testing)
- **Outcome:** Reduced delay from TaskRun creation to pod start

**For Performance Engineer: Tune HA parameters for optimal throughput**

→ Lines 94-100: Performance tuning
  Source: Section "Improving OpenShift Pipelines performance"

- **Task:** Experiment with different buckets values (5-10 range)
- **Task:** Experiment with different replicas values (>2, ≤buckets)
- **Task:** Monitor CPU and memory usage during tuning
- **Validation:** Check for resource exhaustion on nodes
- **Outcome:** Higher numbers generally beneficial but require resource monitoring
- **Note:** Optimal settings vary by workload; testing recommended

---

## Appendices

### A. Configuration Quick Reference

| Parameter | Setting | Notes |
|-----------|---------|-------|
| `pipeline.performance.disable-ha` | `false` | Enables high-availability mode |
| `pipeline.performance.buckets` | `5-10` | Number of work distribution buckets |
| `pipeline.performance.replicas` | `>2 and ≤buckets` | Number of controller replicas |

### B. Workflow Coverage Analysis

| Stage | Coverage | Jobs | Notes |
|-------|----------|------|-------|
| Plan | ✅ | Job 1 | Performance characteristics reference data |
| Monitor | ✅ | Job 2 (partial) | Resource monitoring for capacity planning |
| Optimize | ✅ | Job 2 | Infrastructure scaling and HA configuration |
| Configure | ✅ | Job 2 (partial) | TektonConfig CR configuration |
| Get Started | ❌ | - | No initial setup/installation content |
| Deploy | ❌ | - | No pipeline creation/deployment content |
| Troubleshoot | ❌ | - | No diagnostic or failure resolution content |
| Reference | ⚠️ Limited | Appendix A | Basic parameter reference only |

### C. Gaps Identified

| Stage | Gap | Recommendation |
|-------|-----|----------------|
| Get Started | No installation/prerequisites | Link to OpenShift Pipelines installation guide |
| Deploy | No pipeline creation | Link to pipeline creation/Pipelines as Code guides |
| Troubleshoot | No diagnostic procedures | Add section on diagnosing performance bottlenecks |
| Reference | Limited parameter docs | Link to full TektonConfig CR performance tuning reference |
| Monitor | No metrics collection | Add section on exposing/querying pipeline performance metrics |

---

## Navigation Guide

### By User Journey

**Platform Administrator planning pipeline capacity:**
1. Job 1: Review reference performance data (60 concurrent pipelines baseline)
2. Job 2.1: Monitor current node resource usage
3. Job 2.1: Scale infrastructure if resources constrained
4. Job 2.2: Enable high-availability mode for improved throughput

**Performance Engineer optimizing existing deployment:**
1. Job 1: Understand baseline performance characteristics
2. Job 2.2: Enable high-availability mode on TektonConfig CR
3. Job 2.2: Tune buckets and replicas parameters for workload
4. Job 2.1: Monitor CPU/memory during optimization

**DevOps Engineer troubleshooting slow pipelines:**
1. Job 1: Compare current performance to reference baseline
2. Job 2.1: Check node resource utilization
3. Job 2.2: Consider enabling HA mode for performance improvement

---

## Document Statistics

**Workflow Coverage:**
- Plan: 1 job
- Monitor: 1 job (partial)
- Optimize: 1 job
- Configure: 1 job (partial)
- Get Started: Gap identified
- Deploy: Gap identified
- Troubleshoot: Gap identified
- Reference: Limited coverage

**Main Jobs:** 2
**User Stories/Paths:** 4
**Source Sections:** 2 (Assembly abstract + 1 concept module)
**Platform/Tool Variations:** None (single configuration approach)

**Key Metrics:**
- Document length: 108 lines (reduced)
- Personas identified: 4
- Prerequisites extracted: 2
- Related jobs identified: 4
- Desired outcomes: 11

# JTBD-Oriented Table of Contents

## Document: Understanding the Tekton Results retention policy

**Generation Date:** 2026-06-12  
**Variant:** self-managed

---

## Proposed Structure

### Managing Tekton Results retention

**Job 1: Understand how Tekton Results retention works** [concept]
- Overview of Retention Policy Agent
- How retention policies work
- Configuration overview
- Config map structure and location
- Retention period formats (days, duration strings)

**Job 2: Configure basic retention settings** [procedure]
- Prerequisites
- Steps to configure the tekton-results-config-results-retention-policy config map
- Setting defaultRetention value
- Configuring the runAt cron schedule
- Verifying the configuration
- (Optional) Additional resources

**Job 3: Understand fine-grained retention policies** [concept]
- What are fine-grained retention policies
- How policy evaluation works (order and precedence)
- Policy structure overview
- Selector types and AND logic
- When to use fine-grained policies vs. default retention

**Reference: Retention policy configuration fields** [reference]
- runAt field
- defaultRetention field
- maxRetention field (deprecated)
- policies field

**Reference: Fine-grained policy selector fields** [reference]
- name field
- selector field
- matchNamespaces
- matchLabels
- matchAnnotations
- matchStatuses
- retention field

**Job 4: Create namespace-based retention policies** [procedure]
- Prerequisites
- Steps to create a namespace-specific retention policy
- Defining matchNamespaces selectors
- Setting namespace-specific retention periods
- Handling multiple namespaces
- Verifying namespace policy application
- (Optional) Example: Different retention for production vs. CI namespaces

**Job 5: Create status and label-based retention policies** [procedure]
- Prerequisites
- Steps to create label-based retention policies
- Steps to create status-based retention policies
- Combining multiple selectors (labels, statuses, namespaces)
- Common use cases:
  - Retaining failed pipeline runs longer
  - Debug annotation-based retention
  - Critical workload retention
- Understanding selector AND logic
- Policy precedence and ordering
- Verifying advanced policy application

---

## TOC Design Rationale

### Job Grouping
All jobs are grouped under a single logical domain: "Managing Tekton Results retention". The jobs follow a learning progression from understanding basics → configuring basics → understanding advanced features → implementing advanced configurations.

### Job Sequence
1. **Jobs 1-2:** Foundation (understand → configure basic settings)
2. **Jobs 3:** Advanced concepts (understand fine-grained policies)
3. **Reference sections:** Supporting material for configuration fields
4. **Jobs 4-5:** Advanced implementation (specific policy types)

This sequence ensures users understand the fundamentals before attempting advanced configurations.

### Content Type Distribution
- **Concepts (2):** Jobs 1 and 3 provide understanding
- **Procedures (3):** Jobs 2, 4, and 5 provide actionable steps
- **Reference (2):** Supporting tables for configuration and policy fields

### Key Improvements Over Current Structure
1. **Task-oriented:** Each job directly addresses a user goal
2. **Clear progression:** From basic to advanced, from understanding to doing
3. **Procedural gaps filled:** The current doc lacks step-by-step procedures; proposed structure adds three procedure modules
4. **Better separation:** Reference material (field tables) is clearly separated from concepts and procedures
5. **Logical grouping:** Related policy types (namespace vs. label/status) are presented as distinct jobs

### Cross-references
- Job 2 should reference the "Retention policy configuration fields" reference
- Jobs 4-5 should reference the "Fine-grained policy selector fields" reference
- Job 3 should cross-reference Jobs 4-5 as practical implementations

### Additional Resources Opportunities
- Link to Tekton Results documentation
- Link to cron schedule syntax reference
- Link to Kubernetes label and annotation best practices
- Link to troubleshooting retention policy issues

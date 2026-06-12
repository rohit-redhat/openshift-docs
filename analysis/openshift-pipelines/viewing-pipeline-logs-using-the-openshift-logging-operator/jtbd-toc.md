# JTBD-Oriented Table of Contents
## Document: viewing-pipeline-logs-using-the-openshift-logging-operator

### Proposed Structure

**Main Job 1: View pipeline logs for troubleshooting and audits**

- Understanding pipeline log storage and the pod dependency problem [concept]
- Viewing pipeline logs using the Elasticsearch Kibana stack [concept]

**Main Job 2: Access and analyze pipeline logs in Kibana**

- Viewing pipeline logs in the Kibana web console [procedure]
  - Prerequisites: Required Operators and access
  - Creating an index pattern in Kibana [procedure]
  - Filtering pipeline-related logs [procedure]
  - Viewing log messages [procedure]

---

### Consolidation Analysis

**Main Jobs Identified (after "Why?" ladder test):**

1. **View pipeline logs for troubleshooting and audits** - This is the core user goal. Jobs 1, 2, and 3 from the extraction all relate to this fundamental need.

2. **Access and analyze pipeline logs in Kibana** - This is the implementation approach. Jobs 4-7 are all tasks supporting this goal.

**Jobs Consolidated:**

- Job 1 (troubleshooting/audits), Job 2 (avoid resource waste), and Job 3 (use Kibana) → consolidated into Main Job 1
  - Rationale: These three represent the problem (needing logs), the constraint (resource efficiency), and the solution (Kibana). They answer "why" to the same ultimate goal: viewing logs for operational purposes.

- Jobs 4-7 → grouped under Main Job 2 as sequential tasks
  - Rationale: These are procedural steps that answer "how" to achieve the goal, not independent jobs. They fail the "Why?" ladder test as standalone jobs.

**Topic Type Distribution:**
- Concepts: 2 approaches
- Procedures: 4 approaches (1 parent procedure with 3 sub-tasks)
- References: 0 approaches

**Structural Improvements:**

1. **Clear problem-solution narrative**: Starts with the problem (pod-dependent logs, resource waste) and immediately presents the solution (Kibana stack)

2. **Logical task grouping**: All Kibana configuration steps are grouped under a single procedural workflow rather than scattered

3. **Prerequisites elevation**: Prerequisites are called out explicitly for the procedural section

4. **Removed redundancy**: The original structure had some conceptual overlap in the abstract. The new structure separates the "what/why" (concept) from the "how" (procedure).

**User Journey Alignment:**

The proposed structure follows the natural user journey:
1. Understand the problem and solution → Concept
2. Decide to use Kibana → Concept
3. Set up and use Kibana → Procedure with clear sub-steps

This aligns with how users would actually approach the task: understanding before doing.

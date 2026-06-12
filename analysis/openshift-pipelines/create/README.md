# JTBD Analysis: Creating CI/CD Pipelines (OpenShift Pipelines)

**Analysis Date:** 2026-06-12  
**Book:** create  
**Distro:** openshift-pipelines  
**Workflow:** Complete 4-step JTBD analysis

---

## Summary

This directory contains a complete Jobs-to-be-Done (JTBD) analysis of the "Creating CI/CD pipelines" book from the OpenShift Pipelines documentation. The analysis transformed 5 feature-based assemblies into 9 outcome-focused main jobs organized across 6 workflow stages.

### Key Metrics

- **Source Content**: 5 assemblies, 6,639 lines (combined)
- **JTBD Records**: 50 total
  - Main jobs: 9
  - User stories: 41
- **Personas**: 7 identified
- **Workflow Stages**: 6 covered
- **Navigation Improvement**: 44% reduction in top-level items

---

## Output Files

### Step 1: Analysis

| File | Description | Size |
|------|-------------|------|
| `create-jtbd.jsonl` | JTBD records in JSON Lines format (50 records) | 58 KB |
| `create-jtbd.csv` | JTBD records in CSV format (spreadsheet-compatible) | 48 KB |
| `create-combined.adoc` | Concatenated reduced content from all 5 assemblies | 237 KB |
| `create-include-graph.json` | Module include graph with types and paths (61 modules) | 19 KB |
| `create-topicmap.json` | Topic map structure extracted from source | 768 B |
| `*-reduced.adoc` | Individual reduced assembly files (5 files) | 236 KB total |

### Step 2: TOC Generation

| File | Description | Size |
|------|-------------|------|
| `create-toc-new_taxonomy.md` | JTBD-oriented Table of Contents | 28 KB (765 lines) |

**Features:**
- 9 main jobs organized by 6 workflow stages
- Quick Navigation section with "I want to..." links
- Decision matrices for resolvers and entitlement methods
- Complete workflow coverage analysis
- Navigation guide by user journey
- Document statistics

### Step 3: Comparison

| File | Description | Size |
|------|-------------|------|
| `create-comparison.md` | Current vs. Proposed structure comparison | 38 KB (803 lines) |

**Features:**
- Side-by-side structure comparison
- Hierarchy level mapping
- 3 concrete consolidation examples
- Navigation improvement metrics (85% scatter reduction for triggers)
- Workflow coverage comparison table
- Benefits analysis

### Step 4: Consolidation

| File | Description | Size |
|------|-------------|------|
| `create-consolidation-report.md` | Stakeholder-facing consolidation report | 36 KB (629 lines) |

**Features:**
- Executive summary with key improvements
- Detailed job descriptions for all 9 jobs
- 3 before/after consolidation examples
- 8 content gaps identified with impact ratings
- Navigation improvement summary with metrics
- Complete document statistics

---

## Main Jobs Identified

### Organized by Workflow Stage

#### Build Pipeline Workflows

1. **Create customized CI/CD solution using pipelines**
   - Personas: Application developer, Pipeline developer
   - Approaches: Project setup, task creation, pipeline assembly, image mirroring, execution, triggers, multi-namespace config

2. **Create CI/CD pipelines for my application (Developer Console)**
   - Personas: Application developer, Cluster administrator
   - Approaches: Pipeline builder (UI), From Git (template), GitHub repository integration

4. **Reuse existing pipeline and task definitions from various sources**
   - Personas: Pipeline developer, Platform engineer
   - Approaches: Hub resolver, Bundles resolver, Git resolver (anon/auth), HTTP resolver, Cluster resolver

5. **Modify existing pipeline configuration**
   - Personas: Application developer
   - Approaches: Edit pipelines, Delete pipelines

#### Execute and Monitor

3. **Start pipeline with configured resources**
   - Personas: Application developer
   - Approaches: Pipelines view, Topology view, credential configuration

8. **View consolidated execution statistics**
   - Personas: Platform administrator, Application developer
   - Approaches: All pipelines together, Specific pipeline metrics

#### Govern and Secure

6. **Provide reusable pipeline patterns (Administrator)**
   - Personas: Cluster administrator
   - Approaches: Create templates in openshift namespace

7. **Control pipeline execution with manual approval gates**
   - Personas: Platform administrator, DevOps engineer, Pipeline approver
   - Approaches: Enable controller, configure approval tasks, approve via web console, approve via CLI

#### Manage Resources

9. **Use Red Hat entitlements in pipelines**
   - Personas: Pipeline developer, Platform engineer
   - Approaches: Manual secret copying, Shared Resources CSI driver

---

## Personas

1. **Application developer** (primary) - Creates and runs pipelines for applications
2. **Pipeline developer** - Designs reusable pipeline components
3. **Platform engineer** - Manages platform-level pipeline infrastructure
4. **Platform administrator** - Analyzes org-wide pipeline performance
5. **Cluster administrator** - Provides templates and infrastructure
6. **DevOps engineer** - Configures deployment governance
7. **Pipeline approver** - Authorizes critical deployments

---

## Workflow Stages Covered

| Stage | Jobs | Coverage |
|-------|------|----------|
| **Build Pipeline Workflows** | 1, 2, 4, 5 | ✅ Complete |
| **Execute and Monitor** | 3, 8 | ✅ Complete |
| **Govern and Secure** | 6, 7 | ✅ Complete |
| **Manage Resources** | 9 | ✅ Complete |
| **Modify and Update** | 5 | ✅ Complete |
| **Troubleshoot** | — | ⚠️ Gap identified |

---

## Key Improvements

### Navigation Efficiency

- **Top-level items**: 5 assemblies → 9 jobs (44% reduction)
- **Navigation depth**: 3-4 levels → 2-3 levels (25-33% reduction)
- **Scatter reduction**:
  - Triggers: 7 sections → 1 subsection (85% reduction)
  - Resolver comparison: 5 sections → 1 job (80% faster)
  - Approval gates: Separate assembly → unified workflow progression

### User Experience

- **Workflow-driven**: Organized by stages users progress through
- **Outcome-focused**: Jobs describe what users want to accomplish, not features
- **Context-aware**: Prerequisites and timing surfaced upfront
- **Decision support**: Comparison matrices for choosing approaches
- **Reduced context switching**: Related approaches grouped together

---

## Content Gaps Identified

| Gap | Impact | Recommendation |
|-----|--------|----------------|
| Troubleshooting failed pipeline runs | High | Add dedicated troubleshooting job |
| Quickstart/Getting Started | High | Add "Get Started" main job |
| Pipeline rollback procedures | Medium | Add to execution/monitoring jobs |
| Performance optimization guidance | Medium | Expand monitoring job with optimization |
| Security best practices | Medium | Add to secure jobs |
| Multi-cluster pipeline patterns | Low | Add to configure jobs |
| Cost management | Low | Add to resource management |
| Disaster recovery | Low | Add to operate jobs |

---

## Usage

### For Documentation Writers

1. **Review JTBD records**: `create-jtbd.csv` (spreadsheet-friendly)
2. **Understand proposed structure**: `create-toc-new_taxonomy.md`
3. **See before/after**: `create-comparison.md`
4. **Identify gaps**: `create-consolidation-report.md` (Section 7)

### For Product Managers

1. **Executive summary**: `create-consolidation-report.md` (Section 2)
2. **User journey improvements**: `create-comparison.md` (Section 7)
3. **Content gaps with priorities**: `create-consolidation-report.md` (Section 7)

### For UX Researchers

1. **Persona breakdown**: `create-consolidation-report.md` (Section 10)
2. **Job statements**: `create-jtbd.jsonl` (searchable)
3. **Desired outcomes**: Extract from JSONL records

---

## Methodology

This analysis followed the JTBD Workflow for Topic Map Repositories using:

1. **Analysis**: Parse topic map, reduce assemblies, extract JTBD records following Ulwick's ODI framework
2. **TOC Generation**: Organize by workflow stages with clean job titles
3. **Comparison**: Side-by-side current vs. proposed structure
4. **Consolidation**: Stakeholder-facing report with metrics and examples

**Tools used:**
- `asciidoctor-reducer` for resolving includes
- JTBD extraction with LLM (Claude Sonnet 4.5)
- Chunked processing for large documents (6,639 lines)

---

## Next Steps

### Recommended Actions

1. **Review consolidation report** with documentation team leads
2. **Prioritize content gaps** identified in Section 7 of consolidation report
3. **Create prototypes** for top 2-3 jobs to validate structure
4. **Gather user feedback** on proposed navigation
5. **Plan migration** from feature-based to JTBD-based organization

### Quick Wins

- **Consolidate trigger content** (85% scatter reduction)
- **Add resolver comparison matrix** (80% faster decision-making)
- **Create troubleshooting job** (highest-impact gap)
- **Add quickstart guide** (high-impact gap for new users)

---

## Contact

For questions about this analysis or the JTBD methodology, refer to:
- JTBD methodology: `/Users/roparmar/.claude/plugins/cache/ccs-ai-agentic-workflow/jtbd-tools/1.3.0/reference/methodology.md`
- TOC guidelines: `/Users/roparmar/.claude/plugins/cache/ccs-ai-agentic-workflow/jtbd-tools/1.3.0/reference/toc-guidelines.md`
- Comparison guidelines: `/Users/roparmar/.claude/plugins/cache/ccs-ai-agentic-workflow/jtbd-tools/1.3.0/reference/comparison-guide.md`
- Consolidation guidelines: `/Users/roparmar/.claude/plugins/cache/ccs-ai-agentic-workflow/jtbd-tools/1.3.0/reference/consolidation-guide.md`

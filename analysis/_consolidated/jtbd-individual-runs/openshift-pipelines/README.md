# OpenShift Pipelines JTBD Analysis - Master Index

**Analysis Date:** 2026-06-12  
**Scope:** 10 books from OpenShift Pipelines documentation  
**Methodology:** Jobs-to-be-Done (JTBD) framework

---

## Quick Start

### 📊 For Stakeholders
**Start here:** [NEXT_STEPS.md](NEXT_STEPS.md) — Implementation roadmap and action items

**Executive summaries:**
- [COMPLETE_FILE_LIST.md](COMPLETE_FILE_LIST.md) — All 170+ generated files organized by book
- [MAIN_JOBS_ONLY.csv](MAIN_JOBS_ONLY.csv) — 91 main jobs ready for spreadsheet import ✨
- [ALL_BOOKS_JTBD_JOBS.csv](ALL_BOOKS_JTBD_JOBS.csv) — Complete 355 records (main jobs + user stories)

### 📖 For Reviewers
**Review individual books:**  
Each book has a consolidation report explaining restructuring rationale:
- `release_notes/release_notes-consolidation-report.md`
- `about/about-consolidation-report.md`
- `install_config/install_config-consolidation-report.md`
- _(etc. — see directory listing below)_

### 🛠️ For Implementers
**Migration guides:**
- `*-toc-new_taxonomy.md` — Proposed structure with line references to source content
- `*-comparison.md` — Side-by-side current vs. proposed structure
- `*-include-graph.json` — Module dependency graphs

---

## Analysis Summary

### Key Metrics

| Metric | Count |
|--------|-------|
| **Books Analyzed** | 10 |
| **Total JTBD Records** | 355 |
| **Main Jobs Identified** | 91 |
| **User Stories** | 264 |
| **Files Generated** | 170+ |
| **Average Navigation Improvement** | 40-70% click reduction |

### Books Analyzed

1. **Release notes** (`release_notes/`) — 8 main jobs, 52 total records
2. **About OpenShift Pipelines** (`about/`) — 3 main jobs, 13 total records
3. **Installing and configuring** (`install_config/`) — 14 main jobs, 30 total records
4. **Managing performance and resource use** (`resource/`) — 6 main jobs, 20 total records
5. **Creating CI/CD pipelines** (`create/`) — 9 main jobs, 50 total records
6. **Observability in OpenShift Pipelines** (`records/`) — 6 main jobs, 23 total records
7. **Pipelines as Code** (`pac/`) — 14 main jobs, 39 total records
8. **Securing OpenShift Pipelines** (`secure/`) — 12 main jobs, 61 total records
9. **Custom Tekton Hub instance** (`hub/`) — 9 main jobs, 18 total records
10. **Pipelines CLI (tkn) reference** (`tkn_cli/`) — 10 main jobs, 49 total records

---

## File Guide

### 🎯 Import to JTBD Template

**File:** [MAIN_JOBS_ONLY.csv](MAIN_JOBS_ONLY.csv)  
**Rows:** 92 (91 jobs + header)  
**Purpose:** Import this file directly into the JTBD Jobs spreadsheet template

**Columns:**
- `job_number` — Sequential ID (1-91)
- `source_book` — Book directory name
- `book_title` — Human-readable book name
- `job_statement` — "When X, I want Y, so I can Z" format
- `job_type` — Core, supporting, etc.
- `persona` — User role (Platform engineer, DevOps engineer, etc.)
- `job_map_stage` — Workflow stage (Get Started, Configure, Deploy, etc.)
- `granularity` — Always "main_job" in this file
- `prerequisites` — Pipe-separated list of prerequisite jobs
- `related_jobs` — Pipe-separated list of related jobs
- `desired_outcomes` — Pipe-separated list of outcomes
- `section` — Original section title in source docs
- `evidence` — Citation with line numbers
- `notes` — Additional context
- `doc` — Source document filename

### 📋 Complete Dataset

**File:** [ALL_BOOKS_JTBD_JOBS.csv](ALL_BOOKS_JTBD_JOBS.csv)  
**Rows:** 356 (355 records + header)  
**Purpose:** Complete dataset including main jobs AND user stories

**Additional column:**
- `parent_job` — Parent main job statement (for user stories)

**Use cases:**
- Detailed implementation mapping
- User story → main job relationships
- Comprehensive job family analysis

---

## Directory Structure

```
analysis/openshift-pipelines/
├── README.md                          ← You are here
├── NEXT_STEPS.md                      ← Implementation roadmap
├── COMPLETE_FILE_LIST.md              ← All 170+ files organized
├── MAIN_JOBS_ONLY.csv                 ← 91 main jobs (import this)
├── ALL_BOOKS_JTBD_JOBS.csv            ← 355 complete records
│
├── release_notes/                     ← Book 1: Release notes (8 main jobs)
│   ├── release_notes-consolidation-report.md
│   ├── release_notes-toc-new_taxonomy.md
│   ├── release_notes-comparison.md
│   ├── release_notes-jtbd.jsonl
│   ├── release_notes-jtbd.csv
│   ├── release_notes-combined.adoc
│   ├── op-release-notes-1-22-include-graph.json
│   ├── op-release-notes-1-22-topicmap.json
│   └── op-release-notes-1-22-reduced.adoc
│
├── about/                             ← Book 2: About OpenShift Pipelines (3 main jobs)
│   ├── about-consolidation-report.md
│   ├── about-toc-new_taxonomy.md
│   ├── about-comparison.md
│   ├── about-jtbd.jsonl
│   ├── about-jtbd.csv
│   ├── about-combined.adoc
│   ├── about-include-graph.json
│   ├── about-topicmap.json
│   ├── README.md
│   ├── about-pipelines-reduced.adoc
│   └── understanding-openshift-pipelines-reduced.adoc
│
├── install_config/                    ← Book 3: Installing and configuring (14 main jobs)
│   ├── install_config-consolidation-report.md
│   ├── install_config-toc-new_taxonomy.md
│   ├── install_config-comparison.md
│   ├── install_config-jtbd.jsonl
│   ├── install_config-jtbd.csv
│   ├── install_config-combined.adoc
│   ├── install_config-include-graph.json
│   ├── install_config-topicmap.json
│   ├── installing-pipelines-reduced.adoc
│   ├── uninstalling-pipelines-reduced.adoc
│   └── customizing-configurations-in-the-tektonconfig-cr-reduced.adoc
│
├── resource/                          ← Book 4: Managing performance (6 main jobs)
│   ├── resource-consolidation-report.md
│   ├── resource-toc-new_taxonomy.md
│   ├── resource-comparison.md
│   ├── resource-jtbd.jsonl
│   ├── resource-jtbd.csv
│   ├── resource-combined.adoc
│   ├── resource-include-graph.json
│   ├── resource-topicmap.json
│   └── [5 reduced assembly files]
│
├── create/                            ← Book 5: Creating CI/CD pipelines (9 main jobs)
│   ├── create-consolidation-report.md
│   ├── create-toc-new_taxonomy.md
│   ├── create-comparison.md
│   ├── create-jtbd.jsonl
│   ├── create-jtbd.csv
│   ├── create-combined.adoc
│   ├── create-include-graph.json
│   ├── create-topicmap.json
│   ├── README.md
│   └── [5 reduced assembly files]
│
├── records/                           ← Book 6: Observability (6 main jobs)
│   ├── records-consolidation-report.md
│   ├── records-toc-new_taxonomy.md
│   ├── records-comparison.md
│   ├── records-jtbd.jsonl
│   ├── records-jtbd.csv
│   ├── records-combined.adoc
│   ├── records-include-graph.json
│   ├── records-topicmap.json
│   └── [2 reduced assembly files]
│
├── pac/                               ← Book 7: Pipelines as Code (14 main jobs)
│   ├── pac-consolidation-report.md
│   ├── pac-toc-new_taxonomy.md
│   ├── pac-comparison.md
│   ├── pac-jtbd.jsonl
│   ├── pac-jtbd.csv
│   ├── pac-combined.adoc
│   ├── pac-topicmap.json
│   ├── WORKFLOW_SUMMARY.md
│   └── [7 reduced assembly files]
│
├── secure/                            ← Book 8: Securing OpenShift Pipelines (12 main jobs)
│   ├── secure-consolidation-report.md
│   ├── secure-toc-new_taxonomy.md
│   ├── secure-comparison.md
│   ├── secure-jtbd.jsonl
│   ├── secure-jtbd.csv
│   ├── secure-combined.adoc
│   ├── secure-include-graph.json
│   ├── secure-topicmap.json
│   └── [7 reduced assembly files]
│
├── hub/                               ← Book 9: Custom Tekton Hub (9 main jobs)
│   ├── hub-consolidation-report.md
│   ├── hub-toc-new_taxonomy.md
│   ├── hub-comparison.md
│   ├── hub-jtbd.jsonl
│   ├── hub-combined.adoc
│   ├── hub-include-graph.json
│   ├── hub-topicmap.json
│   └── using-tekton-hub-with-openshift-pipelines-reduced.adoc
│
└── tkn_cli/                           ← Book 10: Pipelines CLI reference (10 main jobs)
    ├── tkn_cli-consolidation-report.md
    ├── tkn_cli-toc-new_taxonomy.md
    ├── tkn_cli-comparison.md
    ├── tkn_cli-jtbd.jsonl
    ├── tkn_cli-jtbd.csv
    ├── tkn_cli-combined.adoc
    ├── tkn_cli-include-graph.json
    ├── tkn_cli-topicmap.json
    └── [3 reduced assembly files]
```

---

## File Types Explained

### Stakeholder Reports
- **`*-consolidation-report.md`** — Executive summary with all 10 required sections:
  1. Header & Metadata
  2. Executive Summary (What's Changing + Key Improvements)
  3. Current Structure
  4. Proposed JTBD Structure
  5. Key Differences
  6. Consolidation Examples
  7. Content Gaps
  8. Navigation Improvements (quantified)
  9. UX Research Alignment
  10. Document Statistics

### Implementation Guides
- **`*-toc-new_taxonomy.md`** — Proposed JTBD-based table of contents with:
  - Main jobs organized by workflow stages
  - User stories nested under jobs
  - Line references to source content
  - Quick navigation section
  - Decision matrices (where applicable)
  - Workflow coverage analysis

- **`*-comparison.md`** — Side-by-side comparison showing:
  - Current feature-based structure
  - Proposed job-based structure
  - Quantified navigation improvements
  - Consolidation examples with metrics
  - Gap analysis

### Data Files
- **`*-jtbd.jsonl`** — Machine-readable JTBD records (one JSON per line)
  - Use for automated processing
  - Contains full record with arrays
  
- **`*-jtbd.csv`** — Spreadsheet-compatible format
  - Arrays converted to pipe-separated strings
  - Import to Excel/Google Sheets
  
- **`*-combined.adoc`** — Concatenated reduced assemblies
  - All includes resolved
  - Source for evidence extraction
  
- **`*-include-graph.json`** — Module dependency graph
  - Maps assembly → modules with types (CONCEPT, PROCEDURE, REFERENCE)
  
- **`*-topicmap.json`** — Topic map structure
  - Book metadata from _topic_maps/_topic_map.yml

### Reduced Files
- **`*-reduced.adoc`** — Individual assemblies with includes resolved
  - Created by asciidoctor-reducer
  - Used for analysis and line number references

---

## How to Use This Analysis

### For Documentation Managers
1. Read [NEXT_STEPS.md](NEXT_STEPS.md) for implementation roadmap
2. Review high-level metrics in this README
3. Present findings to stakeholders using consolidation reports
4. Prioritize books for restructuring (recommend pilot with 3 books)

### For Content Strategists
1. Import [MAIN_JOBS_ONLY.csv](MAIN_JOBS_ONLY.csv) to JTBD template spreadsheet
2. Review job statements for accuracy
3. Map personas to actual user types
4. Create implementation priority matrix

### For Technical Writers
1. Review consolidation report for assigned book
2. Study proposed TOC structure
3. Use comparison file to understand migration mapping
4. Reference JTBD records for detailed job context
5. Use include graphs to understand module dependencies

### For UX Researchers
1. Use job statements as basis for user testing scenarios
2. Validate personas against actual user types
3. Test proposed navigation structure with users
4. Measure time-to-task completion before/after

### For Information Architects
1. Review proposed hierarchies in TOC files
2. Validate job map stage assignments
3. Create content migration mapping (old → new structure)
4. Design redirect strategy for URL changes

---

## Methodology

### JTBD Framework
Jobs-to-be-Done (JTBD) is a framework for understanding user goals independent of specific solutions. A "job" is what a user is trying to accomplish, not the tool they use.

**Job statement format:**
```
When [situation], I want [motivation], so I can [desired outcome].
```

**Example:**
```
When configuring production pipelines, I want to optimize performance 
settings, so I can minimize pipeline execution time and resource costs.
```

### Analysis Workflow (4 Steps)

**Step 1: Analysis**
- Parse topic map structure
- Reduce assemblies with asciidoctor-reducer (resolve all includes)
- Extract JTBD records using LLM-powered analysis
- Output: JSONL, CSV, combined content, metadata

**Step 2: TOC Generation**
- Organize jobs by workflow stages (Get Started → Configure → Deploy → Monitor → Troubleshoot)
- Create 3-tier hierarchy: Job → User Story → Task
- Add quick navigation and decision matrices
- Output: JTBD-oriented table of contents

**Step 3: Comparison**
- Extract current structure from AsciiDoc headings
- Compare current (feature-based) vs. proposed (job-based)
- Quantify navigation improvements
- Identify consolidation opportunities
- Output: Side-by-side comparison with metrics

**Step 4: Consolidation Report**
- Create stakeholder-facing executive summary
- Explain restructuring rationale
- Provide concrete before/after examples
- Identify content gaps
- Output: Complete consolidation report

### Quality Checks
✅ All job statements follow "When/Want/So" format  
✅ Main jobs pass "Why?" ladder test (outcome-focused, stable)  
✅ Parent_job references set for all user stories  
✅ Evidence includes line numbers  
✅ Module types identified (CONCEPT, PROCEDURE, REFERENCE)  
✅ Sequential job numbering (no gaps)  
✅ Topic type tags on all approaches ([procedure], [concept], [reference])

---

## Key Findings Summary

### Navigation Improvements
- **Average:** 40-70% reduction in clicks to reach content
- **Best:** 85% reduction (trigger consolidation in "create" book)
- **Range:** 33-79% across books

### Common Consolidation Patterns
1. **Installation methods** — Multiple scattered procedures → unified comparison with decision guidance
2. **Configuration options** — 20+ sections → 6-8 consolidated jobs
3. **Security content** — 3-5 scattered sections → dedicated security stage
4. **Troubleshooting** — Missing or buried → elevated to dedicated workflow stage

### Content Gaps (High Priority)
- **Quickstart guides** — Missing in 7/10 books
- **Troubleshooting** — Missing in 8/10 books
- **Decision guidance** — Installation choices, configuration trade-offs
- **Monitoring/observability** — Missing in 6/10 books
- **Prerequisites** — Often implicit, rarely explicit

### Persona Distribution
- **Platform Engineer** — 35%
- **DevOps Engineer** — 30%
- **Cluster Administrator** — 20%
- **SRE** — 10%
- **Security Engineer** — 5%

### Job Map Stage Distribution
- **Configure** — 35%
- **Get Started** — 20%
- **Deploy** — 15%
- **Secure** — 12%
- **Operate** — 10%
- **Monitor** — 5%
- **Troubleshoot** — 3% (significant gap)

---

## Success Metrics

### Quantified Improvements (Predicted)
- **40-70%** reduction in navigation clicks
- **50-60%** reduction in average time to find content
- **60-80%** reduction in scattered content (consolidation)
- **30-40%** reduction in top-level navigation items

### Validation (To be measured post-implementation)
- Time-to-task completion (before vs. after)
- "Was this helpful?" ratings
- Support ticket volume related to docs
- Search query patterns
- Page views per job
- Bounce rate by job

---

## Next Actions

### Immediate (This Week)
1. ✅ Import [MAIN_JOBS_ONLY.csv](MAIN_JOBS_ONLY.csv) to JTBD spreadsheet template
2. ✅ Review analysis with documentation team
3. ✅ Present findings to stakeholders
4. ✅ Get approval for pilot implementation

### Short-term (Next 2 Weeks)
5. ⏳ Prioritize books for restructuring (recommend 3-book pilot)
6. ⏳ Create content migration mapping
7. ⏳ Address high-priority content gaps (create Jira tickets)

### Medium-term (Next 2 Months)
8. ⏳ Implement pilot restructuring (3 books)
9. ⏳ User testing and iteration
10. ⏳ Roll out to remaining books

**See [NEXT_STEPS.md](NEXT_STEPS.md) for complete implementation roadmap.**

---

## Questions?

**Documentation Team:** Review [NEXT_STEPS.md](NEXT_STEPS.md) for detailed guidance  
**Technical Issues:** Check individual book consolidation reports  
**Data Questions:** Refer to CSV files or JSONL records  

**Analysis Tools:** All workflows executed using `jtbd-tools` skills in Claude Code CLI

---

**Generated:** 2026-06-12  
**Analysis Directory:** `/Users/roparmar/git/openshift-docs/analysis/openshift-pipelines/`  
**Total Files:** 170+  
**Total Size:** ~1.5 MB

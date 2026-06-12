# OpenShift Pipelines JTBD Analysis - Consolidated Export

**Export Date:** 2026-06-12  
**Source:** `/Users/roparmar/git/openshift-docs/analysis/openshift-pipelines/`  
**Export Location:** `/Users/roparmar/git/openshift-docs/analysis/_consolidated/jtbd-individual-runs/openshift-pipelines/`

---

## Export Summary

**Total Files Exported:** 55 files (2.0 MB)
- **CSV files:** 11
- **Markdown files:** 34
- **JSONL files:** 10

---

## Quick Start

### 📊 For Immediate Use

**1. Import to JTBD Spreadsheet Template**
- File: [MAIN_JOBS_ONLY.csv](MAIN_JOBS_ONLY.csv)
- Contains: 91 main jobs ready for import
- Action: Import directly to Jobs tab of your JTBD template

**2. Review Implementation Plan**
- File: [NEXT_STEPS.md](NEXT_STEPS.md)
- Contains: 12-week implementation roadmap with action items
- Action: Share with documentation team

**3. Present to Stakeholders**
- File: [EXECUTIVE_SUMMARY.md](EXECUTIVE_SUMMARY.md)
- Contains: One-page overview with key findings and business impact
- Action: Use for stakeholder presentation

---

## Files in This Export

### 📋 Master Documents (6 files)

1. **MAIN_JOBS_ONLY.csv** (76K)
   - 91 main jobs across all 10 books
   - Ready for spreadsheet import
   - Columns: job_number, source_book, book_title, job_statement, persona, job_map_stage, etc.

2. **ALL_BOOKS_JTBD_JOBS.csv** (310K)
   - 355 complete records (91 main jobs + 264 user stories)
   - Includes parent_job relationships
   - Use for detailed implementation mapping

3. **NEXT_STEPS.md** (14K)
   - Complete implementation roadmap
   - Week-by-week action items
   - Risk mitigation, success metrics, resource requirements

4. **EXECUTIVE_SUMMARY.md** (11K)
   - Stakeholder-facing one-pager
   - Key findings, business impact, decisions needed
   - Quick reference for management

5. **README.md** (17K)
   - Master index for all analysis files
   - How-to guide by role
   - Methodology overview

6. **COMPLETE_FILE_LIST.md** (12K)
   - Comprehensive list of all 170+ generated files
   - Organized by book
   - File type explanations

---

### 📖 Per-Book Reports (30 files, 10 books × 3 reports)

Each of the 10 books has 3 key deliverables:

#### Consolidation Reports (10 files)
Stakeholder-facing executive summaries with:
- Current vs. proposed structure
- Before/after consolidation examples
- Content gaps with impact ratings
- Quantified navigation improvements

Files:
- `about-consolidation-report.md`
- `create-consolidation-report.md`
- `hub-consolidation-report.md`
- `install_config-consolidation-report.md`
- `pac-consolidation-report.md`
- `records-consolidation-report.md`
- `release_notes-consolidation-report.md`
- `resource-consolidation-report.md`
- `secure-consolidation-report.md`
- `tkn_cli-consolidation-report.md`

#### TOC Files (10 files)
Proposed JTBD-based table of contents with:
- Jobs organized by workflow stages
- Line references to source content
- Quick navigation sections
- Decision matrices

Files:
- `about-toc-new_taxonomy.md`
- `create-toc-new_taxonomy.md`
- `hub-toc-new_taxonomy.md`
- `install_config-toc-new_taxonomy.md`
- `pac-toc-new_taxonomy.md`
- `records-toc-new_taxonomy.md`
- `release_notes-toc-new_taxonomy.md`
- `resource-toc-new_taxonomy.md`
- `secure-toc-new_taxonomy.md`
- `tkn_cli-toc-new_taxonomy.md`

#### Comparison Files (10 files)
Side-by-side current vs. proposed structure with:
- Quantified navigation improvements
- Consolidation metrics
- Migration guidance

Files:
- `about-comparison.md`
- `create-comparison.md`
- `hub-comparison.md`
- `install_config-comparison.md`
- `pac-comparison.md`
- `records-comparison.md`
- `release_notes-comparison.md`
- `resource-comparison.md`
- `secure-comparison.md`
- `tkn_cli-comparison.md`

---

### 📊 JTBD Data Files (19 files)

#### JSONL Format (10 files)
Machine-readable format (one JSON object per line):
- `about-jtbd.jsonl`
- `create-jtbd.jsonl`
- `hub-jtbd.jsonl`
- `install_config-jtbd.jsonl`
- `pac-jtbd.jsonl`
- `records-jtbd.jsonl`
- `release_notes-jtbd.jsonl`
- `resource-jtbd.jsonl`
- `secure-jtbd.jsonl`
- `tkn_cli-jtbd.jsonl`

#### CSV Format (9 files)
Spreadsheet-compatible format:
- `about-jtbd.csv`
- `create-jtbd.csv`
- `install_config-jtbd.csv`
- `pac-jtbd.csv`
- `records-jtbd.csv`
- `release_notes-jtbd.csv`
- `resource-jtbd.csv`
- `secure-jtbd.csv`
- `tkn_cli-jtbd.csv`

**Note:** hub-jtbd.csv was not found in source (only JSONL available)

---

## Books Included

| # | Book Name | Directory | Main Jobs | Total Records |
|---|-----------|-----------|-----------|---------------|
| 1 | Release notes | release_notes | 8 | 52 |
| 2 | About OpenShift Pipelines | about | 3 | 13 |
| 3 | Installing and configuring | install_config | 14 | 30 |
| 4 | Managing performance and resource use | resource | 6 | 20 |
| 5 | Creating CI/CD pipelines | create | 9 | 50 |
| 6 | Observability in OpenShift Pipelines | records | 6 | 23 |
| 7 | Pipelines as Code | pac | 14 | 39 |
| 8 | Securing OpenShift Pipelines | secure | 12 | 61 |
| 9 | Custom Tekton Hub instance | hub | 9 | 18 |
| 10 | Pipelines CLI (tkn) reference | tkn_cli | 10 | 49 |
| **TOTAL** | **10 books** | | **91** | **355** |

---

## Key Findings

### Navigation Improvements
- **Average:** 40-70% reduction in clicks to reach content
- **Best:** 85% reduction (trigger consolidation in create book)
- **Range:** 33-79% across books

### Top Consolidation Wins
1. **Trigger configuration** (create book): 85% reduction (7 sections → 1 job)
2. **Database navigation** (hub book): 75% reduction (4 sections → 3 sequential jobs)
3. **Main navigation** (secure book): 79% reduction (48 sections → 10 jobs)
4. **Installation methods** (install_config): 50% reduction (duplicate procedures → unified comparison)

### Content Gaps (High Priority)
- Quickstart guides (missing in 7/10 books)
- Troubleshooting content (missing in 8/10 books)
- Decision guidance (installation, configuration trade-offs)
- Monitoring/observability (missing in 6/10 books)

---

## How to Use This Export

### For Documentation Managers
1. Start with [EXECUTIVE_SUMMARY.md](EXECUTIVE_SUMMARY.md)
2. Review [NEXT_STEPS.md](NEXT_STEPS.md) for implementation roadmap
3. Present findings to stakeholders
4. Import [MAIN_JOBS_ONLY.csv](MAIN_JOBS_ONLY.csv) to JTBD template

### For Content Strategists
1. Import [MAIN_JOBS_ONLY.csv](MAIN_JOBS_ONLY.csv) to spreadsheet
2. Review job statements and personas
3. Prioritize books for restructuring
4. Create implementation priority matrix

### For Technical Writers
1. Review consolidation report for assigned book
2. Study TOC file for proposed structure
3. Use comparison file for migration mapping
4. Reference JTBD CSV/JSONL for detailed context

### For UX Researchers
1. Use job statements for user testing scenarios
2. Validate personas against actual users
3. Test proposed navigation with users
4. Measure time-to-task completion

---

## Recommended Next Actions

### This Week
- [ ] Import [MAIN_JOBS_ONLY.csv](MAIN_JOBS_ONLY.csv) to JTBD Jobs spreadsheet template
- [ ] Review [EXECUTIVE_SUMMARY.md](EXECUTIVE_SUMMARY.md) for stakeholder presentation
- [ ] Read 2-3 consolidation reports to understand analysis depth
- [ ] Schedule stakeholder review meeting (1 hour)

### Next 2 Weeks
- [ ] Prioritize books for restructuring (recommend 3-book pilot)
- [ ] Create content migration mapping
- [ ] Address high-priority content gaps (create Jira tickets)
- [ ] Allocate writer resources

### Next 2 Months
- [ ] Implement pilot restructuring (3 books)
- [ ] User testing and iteration
- [ ] Begin rollout to remaining books

**Complete roadmap:** See [NEXT_STEPS.md](NEXT_STEPS.md)

---

## File Sizes

### Master Documents
- MAIN_JOBS_ONLY.csv: 76K
- ALL_BOOKS_JTBD_JOBS.csv: 310K
- NEXT_STEPS.md: 14K
- EXECUTIVE_SUMMARY.md: 11K
- README.md: 17K
- COMPLETE_FILE_LIST.md: 12K

### Per-Book Averages
- Consolidation report: ~30K
- TOC file: ~25K
- Comparison file: ~25K
- JTBD JSONL: ~30K
- JTBD CSV: ~25K

**Total Export Size:** 2.0 MB

---

## Source Information

**Original Analysis Directory:**  
`/Users/roparmar/git/openshift-docs/analysis/openshift-pipelines/`

**Original File Count:** 170+ files across 20 directories

**What's Not Included in This Export:**
- Individual reduced assembly files (`.adoc`)
- Combined assembly files
- Include graphs (`.json`)
- Topic map files (`.json`)
- Historical/partial run directories

**To access full analysis:** See original directory above

---

## Analysis Methodology

### JTBD Framework
Jobs-to-be-Done focuses on user goals independent of specific solutions.

**Job Statement Format:**
```
When [situation], I want [motivation], so I can [desired outcome].
```

### 4-Step Workflow
1. **Analysis** — Extract JTBD records from documentation
2. **TOC Generation** — Organize jobs by workflow stages
3. **Comparison** — Compare current vs. proposed structure
4. **Consolidation** — Create stakeholder reports

### Quality Checks
✅ All job statements follow "When/Want/So" format  
✅ Main jobs pass "Why?" ladder test  
✅ Parent_job references set for user stories  
✅ Evidence includes line numbers  
✅ Sequential job numbering  

---

## Success Metrics

### Predicted Improvements
- 40-70% reduction in navigation clicks
- 50-60% reduction in time to find content
- 30-40% reduction in top-level navigation items

### To Be Measured (Post-Implementation)
- Time-to-task completion (before vs. after)
- "Was this helpful?" ratings
- Support ticket volume
- Page views per job
- Bounce rate by job

---

## Questions?

**Implementation:** See [NEXT_STEPS.md](NEXT_STEPS.md)  
**Overview:** See [README.md](README.md)  
**Business Case:** See [EXECUTIVE_SUMMARY.md](EXECUTIVE_SUMMARY.md)  
**Technical Details:** See individual book reports

---

**Export Generated:** 2026-06-12  
**Analysis Tool:** JTBD workflow automation (Claude Code)  
**Maintained By:** Documentation Team

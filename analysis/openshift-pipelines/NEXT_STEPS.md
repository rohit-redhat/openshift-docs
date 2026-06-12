# Next Steps: OpenShift Pipelines JTBD Analysis Implementation

**Generated:** 2026-06-12  
**Analysis Scope:** 10 books, 355 JTBD records, 91 main jobs

---

## Immediate Actions (Week 1)

### 1. Review and Validate Analysis Artifacts

**Priority:** HIGH  
**Owner:** Documentation team lead + 2 reviewers

**Tasks:**
- [ ] Review the main jobs CSV ([MAIN_JOBS_ONLY.csv](MAIN_JOBS_ONLY.csv)) for accuracy
- [ ] Spot-check 10-15 job statements against source documentation
- [ ] Validate persona assignments match actual user types
- [ ] Review job_map_stage assignments for workflow accuracy
- [ ] Check for duplicate or overlapping main jobs across books

**Deliverable:** Validation report with corrections needed

**Files to review:**
- `MAIN_JOBS_ONLY.csv` — 91 main jobs (start here)
- Individual `*-consolidation-report.md` files per book

---

### 2. Import Data to JTBD Jobs Template

**Priority:** HIGH  
**Owner:** Content strategist

**Tasks:**
- [ ] Open the JTBD Jobs template spreadsheet
- [ ] Import `MAIN_JOBS_ONLY.csv` into the Jobs tab
- [ ] Map CSV columns to template columns (if different)
- [ ] Add any template-specific columns (priority, status, implementation date)
- [ ] Color-code by source book for visual organization
- [ ] Create filters for persona, job_map_stage, and book

**Files:**
- Source: `/Users/roparmar/git/openshift-docs/analysis/openshift-pipelines/MAIN_JOBS_ONLY.csv`
- Target: Google Sheets JTBD Jobs template

**Note:** If column names don't match the template exactly, create a mapping document.

---

### 3. Present Findings to Stakeholders

**Priority:** HIGH  
**Owner:** Documentation manager

**Tasks:**
- [ ] Schedule 1-hour stakeholder review meeting
- [ ] Prepare executive summary deck (use consolidation reports)
- [ ] Present key metrics:
  - 355 total JTBD records across 10 books
  - 91 main jobs identified
  - Average 40-60% navigation improvement potential
  - Content gaps identified (8-10 per book)
- [ ] Share access to analysis files
- [ ] Get approval to proceed with implementation planning

**Key slides to include:**
1. Analysis methodology and scope
2. Main jobs by book (bar chart)
3. Top 3 consolidation examples with metrics
4. High-impact content gaps summary
5. Proposed next steps timeline

**Supporting documents:**
- `COMPLETE_FILE_LIST.md` — Overview of all deliverables
- Individual `*-consolidation-report.md` files per book

---

## Planning Phase (Weeks 2-3)

### 4. Prioritize Books for Restructuring

**Priority:** HIGH  
**Owner:** Content strategist + UX researcher

**Tasks:**
- [ ] Review quantified navigation improvements per book
- [ ] Analyze user analytics (if available) to identify high-traffic books
- [ ] Survey or interview 5-10 users about pain points
- [ ] Create prioritization matrix: (Impact × Traffic) / Effort
- [ ] Recommend implementation order (suggest 3-book pilot)

**Recommended pilot candidates:**
- **pac** (Pipelines as Code): 50-60% navigation improvement, 18 main jobs, high user engagement
- **create** (Creating CI/CD pipelines): 44% reduction, foundational content
- **secure** (Securing OpenShift Pipelines): 79% reduction, critical for compliance users

**Deliverable:** Prioritized implementation roadmap with timeline

---

### 5. Address High-Priority Content Gaps

**Priority:** MEDIUM-HIGH  
**Owner:** Technical writers (assign by domain)

**Tasks:**
- [ ] Compile all "High impact" gaps from consolidation reports (grep for "**High:**")
- [ ] Create Jira tickets for each gap with:
  - Gap description
  - Affected personas
  - Recommended content type (quickstart, troubleshooting, etc.)
  - Target book and job placement
- [ ] Assign to subject matter experts for review
- [ ] Estimate effort (small/medium/large)
- [ ] Add to documentation backlog

**Common high-priority gaps across books:**
- Quickstart guides (missing in 7/10 books)
- Troubleshooting content (missing in 8/10 books)
- Decision guidance (installation choices, configuration trade-offs)
- Monitoring/observability (missing in 6/10 books)

**Deliverable:** Gap closure plan with assigned owners and due dates

---

### 6. Create Content Migration Mapping

**Priority:** MEDIUM  
**Owner:** Information architect

**Tasks:**
- [ ] For pilot books, map every existing section to proposed job structure
- [ ] Identify content that belongs to multiple jobs (reuse vs. duplicate)
- [ ] Flag content with no clear job mapping (candidates for deprecation)
- [ ] Document redirect strategy (old URLs → new structure)
- [ ] Create content reuse strategy (xrefs, snippets, conditional includes)

**Deliverable:** Migration mapping spreadsheet with:
- Old section path → New job location
- Action: Move / Copy / Deprecate / Merge
- Dependencies and blockers

**Reference files:**
- `*-comparison.md` — Current vs proposed structure
- `*-toc-new_taxonomy.md` — Proposed structure with line references

---

## Implementation Phase (Weeks 4-12)

### 7. Pilot Implementation (3 Books)

**Priority:** HIGH  
**Owner:** Documentation team (3-4 writers)

**Timeline:** 6-8 weeks

**Phase 1: Content Preparation (Weeks 4-6)**
- [ ] Create new assembly files using job-based structure
- [ ] Migrate existing modules to new assemblies (use mapping from step 6)
- [ ] Write new content for high-priority gaps
- [ ] Update topic maps for pilot books
- [ ] Review with SMEs

**Phase 2: Technical Review (Week 7)**
- [ ] Technical accuracy review by product team
- [ ] UX review for navigation and scannability
- [ ] Accessibility review (headings, alt text, etc.)
- [ ] Legal review (if required)

**Phase 3: User Testing (Week 8)**
- [ ] Recruit 5-8 users per persona (platform engineer, DevOps engineer, SRE)
- [ ] Task-based testing: "Find how to install Pipelines as Code with OAuth"
- [ ] Measure time-to-task completion vs. old structure
- [ ] Collect qualitative feedback on job-based organization
- [ ] Document findings and iterate

**Phase 4: Publish & Monitor (Week 9)**
- [ ] Merge pilot book restructuring
- [ ] Set up analytics to track:
  - Time on page
  - Bounce rate
  - Search query patterns
  - Page navigation paths
- [ ] Monitor support tickets for confusion/issues
- [ ] Collect user feedback via in-doc surveys

**Deliverable:** Pilot restructuring complete with metrics baseline

---

### 8. Iterate Based on Pilot Results

**Priority:** HIGH  
**Owner:** Content strategist + UX researcher

**Tasks:**
- [ ] Analyze user testing results from pilot
- [ ] Review analytics data (4 weeks post-launch minimum)
- [ ] Compare predicted navigation improvements vs. actual
- [ ] Identify patterns: What worked? What didn't?
- [ ] Update JTBD template and process based on learnings
- [ ] Refine job statements that tested poorly
- [ ] Document best practices for remaining books

**Success criteria:**
- ≥40% reduction in time-to-task completion
- ≥30% increase in "Was this helpful?" positive ratings
- ≤10% increase in support tickets related to pilot books
- Qualitative feedback: users find job-based structure intuitive

**Deliverable:** Iteration report with recommendations for remaining books

---

### 9. Roll Out to Remaining Books

**Priority:** MEDIUM  
**Owner:** Documentation team

**Timeline:** 6-12 weeks (depending on capacity)

**Recommended rollout order (after pilot):**
1. **install_config** — Foundational, 14 main jobs, high traffic
2. **tkn_cli** — Reference content, 10 main jobs, clear consolidation wins
3. **resource** — Performance-focused, 6 main jobs, smaller scope
4. **records** — Observability, 6 main jobs, smaller scope
5. **hub** — Tekton Hub, 9 main jobs, niche audience (lower priority)
6. **about** — Conceptual, 3 main jobs, smallest scope
7. **release_notes** — Special case, may keep chronological structure

**Per-book process:**
1. Review JTBD analysis artifacts
2. Apply learnings from pilot
3. Migrate content using established process
4. SME review → UX review → Publish
5. Monitor for 2 weeks before starting next book

**Deliverable:** All 10 books restructured using JTBD framework

---

## Optimization Phase (Weeks 13+)

### 10. Continuous Improvement

**Priority:** ONGOING  
**Owner:** Documentation team lead

**Tasks:**
- [ ] Quarterly review of analytics per book
- [ ] Bi-annual user research to validate job statements
- [ ] Update JTBD records when product changes significantly
- [ ] Add new jobs as features are released
- [ ] Deprecate jobs when features are removed
- [ ] Run annual JTBD re-analysis to catch drift

**Metrics to track:**
- Page views per main job
- Average time on page
- Bounce rate by job
- Search terms leading to each job
- Support ticket references to documentation jobs

**Deliverable:** Quarterly documentation health report

---

## Supporting Activities

### 11. Training & Enablement

**Priority:** MEDIUM  
**Owner:** Documentation manager

**Tasks:**
- [ ] Create JTBD writing guide for docs team
- [ ] Run 2-hour workshop on JTBD methodology
- [ ] Document job statement writing best practices
- [ ] Create templates for new job-based assemblies
- [ ] Add JTBD principles to documentation style guide
- [ ] Train support team on new structure (navigation guidance)

**Deliverable:** JTBD documentation guide and team training complete

---

### 12. Cross-Product Application

**Priority:** LOW (Future consideration)

**Tasks:**
- [ ] Share analysis methodology with other product docs teams
- [ ] Identify other products that could benefit from JTBD restructuring
- [ ] Create reusable JTBD analysis workflow/scripts
- [ ] Contribute improvements back to jtbd-tools skills

**Potential candidates:**
- OpenShift Builds (similar CI/CD domain)
- OpenShift GitOps (related workflow automation)
- OpenShift Serverless (Knative-based, similar to Tekton)

---

## Risk Mitigation

### Potential Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| **User confusion during transition** | High | Implement redirects, add "Previously located at" notices, gradual rollout |
| **SEO impact from URL changes** | Medium | Maintain old URLs as redirects, update sitemap, notify search engines |
| **Resource constraints (writers)** | Medium | Pilot with 3 books first, iterate, extend timeline if needed |
| **Stakeholder resistance to change** | Medium | Present data-driven findings, show user testing results, start with pilot |
| **Technical debt in old modules** | Low | Opportunity to refactor during migration, flag for cleanup |
| **Job statements become outdated** | Low | Include review cycle in maintenance plan, update quarterly |

---

## Success Metrics

### Short-term (3 months post-pilot)
- [ ] 40-60% reduction in average clicks to reach content
- [ ] 30% increase in "Was this helpful?" positive ratings
- [ ] ≤10% increase in documentation-related support tickets
- [ ] Pilot books migrated and published

### Medium-term (6 months)
- [ ] 7/10 books restructured
- [ ] Analytics show improved engagement (time on page, reduced bounce)
- [ ] User testing validates job-based navigation
- [ ] Content gaps for pilot books closed (80%+)

### Long-term (12 months)
- [ ] All 10 books restructured
- [ ] Documentation satisfaction scores increase by ≥20%
- [ ] Support ticket volume related to "can't find documentation" decreases by ≥30%
- [ ] Annual user research confirms job statements align with real work

---

## Resources & Artifacts

### Analysis Files (All in `/Users/roparmar/git/openshift-docs/analysis/openshift-pipelines/`)

**Executive Summaries:**
- `COMPLETE_FILE_LIST.md` — Overview of all 170+ generated files
- `MAIN_JOBS_ONLY.csv` — 91 main jobs ready for import (start here)
- `ALL_BOOKS_JTBD_JOBS.csv` — All 355 records (main jobs + user stories)

**Per-Book Deliverables (for each of 10 books):**
- `*-consolidation-report.md` — Stakeholder-facing report (read this first)
- `*-toc-new_taxonomy.md` — Proposed JTBD-based structure
- `*-comparison.md` — Current vs. proposed comparison with metrics
- `*-jtbd.jsonl` — Machine-readable JTBD records
- `*-jtbd.csv` — Spreadsheet-compatible records

**Implementation Guides:**
- Individual consolidation reports explain restructuring rationale
- TOC files show exact line-number mappings to source content
- Include graphs show module dependencies

### Key Contacts (To be filled in)

- **Documentation Manager:** [Name]
- **Content Strategist:** [Name]
- **Information Architect:** [Name]
- **UX Researcher:** [Name]
- **Product Manager:** [Name]
- **Engineering SME (Pipelines):** [Name]
- **Engineering SME (Tekton):** [Name]

---

## Questions & Decisions Needed

### Open Questions
1. **Timeline:** What is the target completion date for full rollout?
2. **Resources:** How many writers can be dedicated to this effort?
3. **Tooling:** Do we have analytics in place to measure impact?
4. **User testing:** Can we recruit users for testing? Budget available?
5. **SEO:** Who owns redirect strategy and search engine notification?
6. **Localization:** How does restructuring impact translated docs?

### Decisions Needed (Week 1)
- [ ] Approve pilot approach (3 books) vs. full rollout
- [ ] Select pilot books (recommend: pac, create, secure)
- [ ] Allocate writer resources (3-4 writers for 6-8 weeks)
- [ ] Budget for user research/testing ($5k-10k recommended)
- [ ] Approve content gap closure as part of project or separate backlog

---

## Appendix: Book Summaries

### Quick Reference: Main Jobs by Book

| Book | Main Jobs | User Stories | Key Findings |
|------|-----------|--------------|--------------|
| **release_notes** | 8 | 44 | 60-70% click reduction; consolidate security/performance scattered content |
| **about** | 3 | 10 | 60-70% navigation improvement; need quickstart guide |
| **install_config** | 14 | 16 | 50% click reduction; consolidate 3 installation/pruning approaches |
| **resource** | 6 | 14 | 33-67% click reduction; missing monitoring/troubleshooting |
| **create** | 9 | 41 | 44% top-level reduction; 85% trigger consolidation win |
| **records** | 6 | 17 | 50-70% click reduction; high-impact RBAC gap |
| **pac** | 14 | 27 | 50-60% click reduction; unify 5 Git provider sections |
| **secure** | 12 | 50+ | 79% main navigation reduction; consolidate image building |
| **hub** | 9 | 9 | 75% database navigation reduction; missing monitoring |
| **tkn_cli** | 10 | 39 | 40% click reduction; consolidate 4 installation methods |

### File Size Summary
- Total analysis output: ~1.5 MB across 170+ files
- Average per-book deliverables: 11-16 files
- CSV files ready for import: 2 (main jobs only + all records)

---

**Document Owner:** Documentation Team  
**Last Updated:** 2026-06-12  
**Next Review:** After pilot completion (Week 9)

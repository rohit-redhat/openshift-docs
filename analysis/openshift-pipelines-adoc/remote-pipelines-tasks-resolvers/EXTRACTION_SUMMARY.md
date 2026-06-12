# JTBD Extraction Summary: Remote Pipelines, Tasks, and Resolvers

## Document Information
- **Source Document**: remote-pipelines-tasks-resolvers-self-managed-reduced.adoc
- **Lines**: 3,581
- **Topic**: Using resolvers to fetch remote pipelines, tasks, and step actions from various sources
- **Output Directory**: `/Users/roparmar/git/openshift-docs/analysis/openshift-pipelines-adoc/remote-pipelines-tasks-resolvers/`

## Extraction Results

### Total Records: 26

- **Main Jobs**: 11
- **User Stories**: 15
- **Procedures**: 0 (reference content not extracted as standalone jobs)

### Main Jobs Identified

1. **Understand resolver concepts** - Understanding how resolvers retrieve remote resources
2. **Fetch from public catalogs** - Using Hub resolver for Artifact Hub/Tekton Hub
3. **Fetch from OCI bundles** - Using Bundles resolver for registry-based distribution
4. **Fetch via anonymous Git** - Using Git resolver for public repositories
5. **Fetch via authenticated Git** - Using Git resolver with SCM APIs for private repos
6. **Fetch via HTTP** - Using HTTP resolver for URL-based resources
7. **Reference cluster resources** - Using Cluster resolver for cross-namespace access
8. **Use standard tasks** - Discovering and using OpenShift Pipelines standard tasks
9. **Use community tasks** - Using community-maintained integration tasks
10. **Use step actions** - Composing tasks from reusable step actions
11. **Choose task versioning** - Understanding versioned vs non-versioned task strategy

### Job Map Coverage

| Stage | Jobs Count | Examples |
|-------|------------|----------|
| **Define** | 1 | Understanding resolver concepts |
| **Configure** | 9 | Configuring each resolver type, multiple providers |
| **Execute** | 10 | Specifying resources using each resolver |
| **Secure** | 2 | Authenticated Git access configuration and usage |
| **Reference** | 4 | Accessing standard tasks, community tasks, step actions |
| **Plan** | 1 | Choosing task versioning strategy |

### Personas Identified

1. **Developer** - Creating pipelines, referencing remote resources (14 jobs)
2. **Platform Administrator** - Configuring resolvers, managing access (9 jobs)
3. **CI/CD Engineer** - Managing pipeline resources, integrations (3 jobs)

### Resolver Coverage

| Resolver Type | Main Job | Config Story | Usage Story | Notes |
|---------------|----------|--------------|-------------|-------|
| **Hub** | ✓ | ✓ | ✓ | Artifact Hub (preferred), Tekton Hub (deprecated) |
| **Bundles** | ✓ | ✓ | ✓ | OCI image-based distribution |
| **Git (Anonymous)** | ✓ | ✓ | ✓ | Public repository access |
| **Git (Authenticated)** | ✓ | ✓ | ✓ | Private repos via SCM API; multiple provider support |
| **HTTP** | ✓ | ✓ | ✓ | URL-based fetching |
| **Cluster** | ✓ | ✓ | ✓ | Cross-namespace access |

### Special Coverage Areas

#### Git Resolver Advanced Features
- Multiple provider configuration (user story)
- Provider selection via configKey (user story)
- Inline parameter override (user story)

#### Reference Material
- Standard tasks reference (buildah, git-clone, maven, s2i-*, skopeo, tkn, opc, etc.)
- Community tasks reference (Argo CD, Helm, Jib, Jenkins integration)
- Step actions reference (git-clone, cache-fetch, cache-upload)
- Versioning strategy (non-versioned vs versioned tasks)

## Output Files

1. **remote-pipelines-tasks-resolvers-include-graph.json** (6.2K)
   - Include graph with 25 modules
   - Structured hierarchy showing assembly and included modules

2. **remote-pipelines-tasks-resolvers-jtbd.jsonl** (29K)
   - 26 JTBD records in JSON Lines format
   - Full schema compliance with validation fields

3. **remote-pipelines-tasks-resolvers-jtbd.csv** (23K)
   - Same 26 records in CSV format
   - Easier for spreadsheet analysis

## Key Insights

### Desired Outcomes Focus
- **Minimize**: Configuration complexity, credential management, duplication, timeout issues
- **Reduce**: Security risks, maintenance burden, dependency on external systems
- **Ensure**: Reproducibility, consistent versioning, secure access, reusability

### Prerequisites Patterns
- Cluster admin permissions (for configuration jobs)
- Access to TektonConfig CR (for resolver configuration)
- Knowledge of resource location (for usage jobs)
- Authentication credentials (for private resource access)

### Related Jobs Patterns
- Configuration jobs relate to usage jobs
- Different resolvers offer alternative approaches to same goal
- Standard/community tasks relate to cluster resolver usage

## Methodology Compliance

✓ Job statements follow "When/Want/So" format
✓ Main jobs are technology-agnostic and stable
✓ User stories are implementation-specific
✓ Personas aligned with roles in documentation
✓ Prerequisites explicitly stated
✓ Related jobs capture workflow relationships
✓ Desired outcomes use ODI-style phrasing
✓ Evidence includes document and line references
✓ Job map stages appropriate for resolver workflow

## Notable Aspects

1. **Resolver Symmetry**: Each resolver follows same pattern - concept, config, usage
2. **Git Resolver Depth**: Most complex with anonymous/authenticated variants and multi-provider support
3. **Reference Material**: Large reference sections (tasks, community tasks, step actions) captured as main jobs
4. **Versioning Strategy**: Important planning consideration captured as standalone main job
5. **Security Focus**: Authenticated access, namespace controls, credential management prominent throughout

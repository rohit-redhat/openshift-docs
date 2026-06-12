import re
import json
import os

assemblies = {
    "creating-applications-with-cicd-pipelines": {
        "path": "/Users/roparmar/git/openshift-docs/create/creating-applications-with-cicd-pipelines.adoc",
        "topic": "Creating CI/CD solutions for applications using OpenShift Pipelines"
    },
    "working-with-pipelines-web-console": {
        "path": "/Users/roparmar/git/openshift-docs/create/working-with-pipelines-web-console.adoc",
        "topic": "Working with OpenShift Pipelines in the web console"
    },
    "remote-pipelines-tasks-resolvers": {
        "path": "/Users/roparmar/git/openshift-docs/create/remote-pipelines-tasks-resolvers.adoc",
        "topic": "Specifying remote pipelines and tasks using resolvers"
    },
    "using-manual-approval": {
        "path": "/Users/roparmar/git/openshift-docs/create/using-manual-approval.adoc",
        "topic": "Using manual approval in OpenShift Pipelines"
    },
    "using-rh-entitlements-pipelines": {
        "path": "/Users/roparmar/git/openshift-docs/create/using-rh-entitlements-pipelines.adoc",
        "topic": "Using Red Hat entitlements in pipelines"
    }
}

include_graph = []
include_pattern = re.compile(r'include::(.+?\.adoc)\[leveloffset=([^\]]+)\]')

for assembly_name, assembly_data in assemblies.items():
    with open(assembly_data["path"], 'r') as f:
        content = f.read()
        
    for match in include_pattern.finditer(content):
        module_path = match.group(1)
        leveloffset = match.group(2)
        
        # Extract module filename
        module_file = os.path.basename(module_path)
        
        # Determine module type
        if module_file.startswith('con-'):
            module_type = 'CONCEPT'
        elif module_file.startswith('proc-'):
            module_type = 'PROCEDURE'
        elif module_file.startswith('ref-'):
            module_type = 'REFERENCE'
        elif module_file.startswith('snip-'):
            module_type = 'SNIPPET'
        else:
            module_type = 'UNKNOWN'
        
        include_graph.append({
            "assembly": assembly_name,
            "assembly_topic": assembly_data["topic"],
            "module_path": module_path,
            "module_file": module_file,
            "module_type": module_type,
            "leveloffset": leveloffset
        })

# Save to JSON
with open('/Users/roparmar/git/openshift-docs/analysis/openshift-pipelines/create/create-include-graph.json', 'w') as f:
    json.dump(include_graph, f, indent=2)

print(f"Include graph built: {len(include_graph)} modules across {len(assemblies)} assemblies")

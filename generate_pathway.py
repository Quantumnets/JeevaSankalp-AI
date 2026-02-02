import networkx as nx

G = nx.read_gpickle("data/updated_memory_graph.gpickle")

for node in G.nodes(data=True):
    if node[1].get("type") == "MEMORY":
        score = node[1]["health_score"]

        if score < 80:
            plan = "Apply compost, grow legumes, reduce chemicals."
        else:
            plan = "Maintain practices, add crop rotation."

print("Regenerative Pathway:")
print(plan)
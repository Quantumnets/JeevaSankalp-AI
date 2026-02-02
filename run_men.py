import networkx as nx

G = nx.read_gpickle("data/memory_graph.gpickle")

for node in G.nodes(data=True):
    if node[1].get("type") == "MEMORY":
        node[1]["health_score"] = (
            node[1]["organic_carbon"] * 50 +
            node[1]["moisture"] * 2
        )

nx.write_gpickle(G, "data/updated_memory_graph.gpickle")
print("Memory updated using MEN logic.")
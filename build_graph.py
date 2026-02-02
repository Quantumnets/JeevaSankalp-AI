import json
import networkx as nx

with open("data/input.json") as f:
    data = json.load(f)

G = nx.Graph()

land_node = data["land_id"]
G.add_node(land_node, type="LAND")
G.add_node("MEMORY_1", type="MEMORY", **data)
G.add_edge(land_node, "MEMORY_1", relation="HAS_MEMORY")

nx.write_gpickle(G, "data/memory_graph.gpickle")
print("Memory graph created.")
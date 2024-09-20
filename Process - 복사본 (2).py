import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes
nodes = [
    "(1.1) News Ranking",
    "(1.2) News URL",
    "(1.3) Extracted articles",
    "(1.4.1) News Title & Date",
    "(1.4.2) Articles' Contents",
    "(1.5) Translate"
]
G.add_nodes_from(nodes)

# Add edges
edges = [
    ("(1.1) News Ranking", "(1.2) News URL"),
    ("(1.2) News URL", "(1.3) Extracted articles"),
    ("(1.3) Extracted articles", "(1.4.1) News Title & Date"),
    ("(1.3) Extracted articles", "(1.4.2) Articles' Contents"),
    ("(1.4.1) News Title & Date", "(1.5) Translate"),
    ("(1.4.2) Articles' Contents", "(1.5) Translate")
]
G.add_edges_from(edges)

# Define node positions
node_positions = {
    "(1.1) News Ranking": (1, 3),
    "(1.2) News URL": (2, 3),
    "(1.3) Extracted articles": (3, 3),
    "(1.4.1) News Title & Date": (4, 4),
    "(1.4.2) Articles' Contents": (4, 2),
    "(1.5) Translate": (5, 3)
}

# Draw nodes
nx.draw_networkx_nodes(G, node_positions, node_color="skyblue", node_size=2000, alpha=0.7)

# Draw edges
nx.draw_networkx_edges(G, node_positions, width=2, alpha=0.5, edge_color="gray", arrowsize=20)

# Draw labels
nx.draw_networkx_labels(G, node_positions, font_size=10, font_weight="bold")

plt.title("News Processing Workflow")
plt.axis("off")  # Turn off axis
plt.tight_layout()  # Adjust layout
plt.show()


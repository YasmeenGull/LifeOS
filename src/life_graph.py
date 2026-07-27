import os
import networkx as nx
import matplotlib.pyplot as plt


def build_life_graph(df):
    """
    Build a directed graph from consecutive activities.
    """

    graph = nx.DiGraph()

    activities = df["activity"].tolist()

    for i in range(len(activities) - 1):

        source = activities[i]
        destination = activities[i + 1]

        if graph.has_edge(source, destination):
            graph[source][destination]["weight"] += 1
        else:
            graph.add_edge(source, destination, weight=1)

    return graph


def print_graph(graph):

    print("\n========== LIFE GRAPH ==========\n")

    if graph.number_of_edges() == 0:
        print("No transitions found.")
        return

    for source, destination, data in graph.edges(data=True):

        print(
            f"{source} ---> {destination} "
            f"(Transitions: {data['weight']})"
        )


def graph_summary(graph):

    print("\n========== GRAPH SUMMARY ==========\n")

    print("Nodes :", graph.number_of_nodes())
    print("Edges :", graph.number_of_edges())


def top_transitions(graph, top_n=5):

    print("\n========== TOP TRANSITIONS ==========\n")

    edges = sorted(
        graph.edges(data=True),
        key=lambda x: x[2]["weight"],
        reverse=True
    )

    if len(edges) == 0:
        print("No transitions.")
        return

    for source, destination, data in edges[:top_n]:

        print(
            f"{source} -> {destination}"
            f" ({data['weight']} transitions)"
        )


def save_graph(graph):

    os.makedirs("output", exist_ok=True)

    path = "output/life_graph.graphml"

    nx.write_graphml(graph, path)

    print(f"\nGraph saved to: {path}")


def draw_graph(graph):

    plt.figure(figsize=(10, 7))

    pos = nx.spring_layout(graph, seed=42)

    nx.draw_networkx_nodes(graph, pos)

    nx.draw_networkx_edges(graph, pos)

    nx.draw_networkx_labels(graph, pos)

    edge_labels = nx.get_edge_attributes(graph, "weight")

    nx.draw_networkx_edge_labels(
        graph,
        pos,
        edge_labels=edge_labels
    )

    plt.title("Life Graph")

    plt.axis("off")

    plt.show()
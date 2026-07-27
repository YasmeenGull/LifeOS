from entropy import behavioral_entropy
from context_switch import calculate_context_switch_cost
from life_graph import (
    build_life_graph,
    graph_summary,
    top_transitions
)
from sequence_mining import recurring_loops


def behavioral_engine(df):
    """
    Complete Behavioral Analysis Engine.
    """

    report = {}

    # Behavioral Entropy
    report["entropy"] = behavioral_entropy(
        df,
        "activity"
    )

    # Context Switching
    report["context_switch"] = calculate_context_switch_cost(df)

    # Life Graph
    graph = build_life_graph(df)

    report["nodes"] = graph.number_of_nodes()
    report["edges"] = graph.number_of_edges()

    # Distraction Loops
    loops = recurring_loops(df)

    report["loops"] = loops

    return report


def print_report(report):

    print("\n")
    print("=" * 60)
    print("LIFEOS BEHAVIORAL ENGINE REPORT")
    print("=" * 60)

    print(f"\nBehavioral Entropy : {report['entropy']} bits")

    print(
        f"Context Switch Cost : "
        f"{report['context_switch']:.2f}"
    )

    print(
        f"Life Graph Nodes : {report['nodes']}"
    )

    print(
        f"Life Graph Edges : {report['edges']}"
    )

    print("\nRecurring Loops")

    if len(report["loops"]) == 0:

        print("None")

    else:

        for sequence, frequency in report["loops"].items():

            print(
                " -> ".join(sequence),
                f"({frequency} times)"
            )

    print("=" * 60)
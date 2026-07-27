import os


def generate_report(
    entropy_score,
    context_cost,
    graph,
    loops,
    filename="output/behavior_report.txt"
):
    """
    Generate a behavioral analysis report.
    """

    os.makedirs("output", exist_ok=True)

    with open(filename, "w", encoding="utf-8") as report:

        report.write("=" * 60 + "\n")
        report.write("LIFEOS BEHAVIORAL REPORT\n")
        report.write("=" * 60 + "\n\n")

        report.write(f"Behavioral Entropy : {entropy_score:.4f}\n")
        report.write(f"Context Switch Cost : {context_cost:.2f}\n\n")

        report.write("Life Graph Summary\n")
        report.write("----------------------------\n")
        report.write(f"Nodes : {graph.number_of_nodes()}\n")
        report.write(f"Edges : {graph.number_of_edges()}\n\n")

        report.write("Recurring Loops\n")
        report.write("----------------------------\n")

        if len(loops) == 0:

            report.write("No recurring loops detected.\n")

        else:

            for sequence, frequency in loops.items():

                report.write(
                    " -> ".join(sequence)
                    + f" ({frequency} times)\n"
                )

    print(f"\nReport saved to {filename}")
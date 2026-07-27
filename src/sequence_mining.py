from collections import Counter


def extract_sequences(df, activity_column="activity", length=3):
    """
    Extract sequences of consecutive activities.
    """

    activities = df[activity_column].tolist()

    sequences = []

    for i in range(len(activities) - length + 1):

        sequence = tuple(activities[i:i + length])

        sequences.append(sequence)

    return sequences


def count_sequences(sequences):
    """
    Count occurrence of every sequence.
    """

    return Counter(sequences)


def recurring_loops(df, activity_column="activity", length=3, minimum_frequency=2):
    """
    Return only recurring sequences.
    """

    sequences = extract_sequences(
        df,
        activity_column,
        length
    )

    counts = count_sequences(sequences)

    loops = {}

    for sequence, frequency in counts.items():

        if frequency >= minimum_frequency:
            loops[sequence] = frequency

    return loops


def print_loops(loops):

    print("\n========== DISTRACTION LOOPS ==========\n")

    if len(loops) == 0:

        print("No recurring loops detected.")

        return

    for sequence, frequency in loops.items():

        print(
            " -> ".join(sequence),
            f"({frequency} times)"
        )
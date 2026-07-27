import math
import pandas as pd


def calculate_activity_probability(dataframe, activity_column):
    """
    Calculate probability of each activity.
    """

    activity_counts = dataframe[activity_column].value_counts()

    total_activities = activity_counts.sum()

    probabilities = activity_counts / total_activities

    return probabilities


def calculate_entropy(probabilities):
    """
    Calculate Shannon Entropy.
    """

    entropy = 0

    for probability in probabilities:

        entropy -= probability * math.log2(probability)

    return round(entropy, 4)


def behavioral_entropy(dataframe, activity_column):
    """
    Complete Behavioral Entropy Pipeline.
    """

    probabilities = calculate_activity_probability(
        dataframe,
        activity_column
    )

    entropy_score = calculate_entropy(probabilities)

    return entropy_score


def print_entropy(entropy_score):
    """
    Print entropy in a professional format.
    """

    print("\nBehavioral Entropy")
    print("--------------------------")
    print(f"Entropy Score : {entropy_score} bits")
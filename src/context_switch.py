import pandas as pd


def count_context_switches(dataframe, activity_column="activity"):
    """
    Count the number of times the activity changes.
    """

    activities = dataframe[activity_column].tolist()

    switches = 0

    for i in range(1, len(activities)):

        if activities[i] != activities[i - 1]:
            switches += 1

    return switches


def calculate_context_switch_cost(
    dataframe,
    activity_column="activity",
    cost_per_switch=0.5
):
    """
    Calculate total context switching cost.
    """

    switches = count_context_switches(
        dataframe,
        activity_column
    )

    total_cost = switches * cost_per_switch

    return total_cost


def print_context_switch_report(
    dataframe,
    activity_column="activity"
):
    """
    Print Context Switching Report.
    """

    switches = count_context_switches(
        dataframe,
        activity_column
    )

    cost = calculate_context_switch_cost(
        dataframe,
        activity_column
    )

    print("\n========== CONTEXT SWITCH REPORT ==========")
    print(f"Total Switches : {switches}")
    print(f"Estimated Cost : {cost:.2f}")
import os
import pandas as pd


FILE_NAME = "output/feedback.csv"


def save_feedback(action, responded):
    """
    Save intervention feedback.
    """

    os.makedirs("output", exist_ok=True)

    new_data = pd.DataFrame(
        {
            "Action": [action],
            "Responded": [responded]
        }
    )

    if os.path.exists(FILE_NAME):

        old_data = pd.read_csv(FILE_NAME)

        new_data = pd.concat(
            [old_data, new_data],
            ignore_index=True
        )

    new_data.to_csv(
        FILE_NAME,
        index=False
    )


def response_rate():
    """
    Calculate response rate.
    """

    if not os.path.exists(FILE_NAME):
        return 0

    data = pd.read_csv(FILE_NAME)

    total = len(data)

    responded = data["Responded"].sum()

    return round(
        (responded / total) * 100,
        2
    )


def ignore_rate():
    """
    Calculate ignore rate.
    """

    if not os.path.exists(FILE_NAME):
        return 0

    data = pd.read_csv(FILE_NAME)

    total = len(data)

    ignored = total - data["Responded"].sum()

    return round(
        (ignored / total) * 100,
        2
    )


def print_feedback_report():
    """
    Print feedback statistics.
    """

    print("\n========== FEEDBACK ==========\n")

    print(
        f"Response Rate : {response_rate()}%"
    )

    print(
        f"Ignore Rate   : {ignore_rate()}%"
    )
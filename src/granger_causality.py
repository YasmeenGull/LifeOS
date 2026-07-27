import pandas as pd
from sklearn.preprocessing import LabelEncoder
from statsmodels.tsa.stattools import grangercausalitytests


def prepare_granger_data(dataframe):
    """
    Convert activity names into numeric values.
    """

    encoder = LabelEncoder()

    df = dataframe.copy()

    df["activity"] = encoder.fit_transform(df["activity"])

    return df


def perform_granger_test(dataframe, max_lag=2):
    """
    Perform Granger Causality Test.
    """

    print("\n========== GRANGER CAUSALITY ==========\n")

    try:

        data = dataframe[["activity", "duration"]]

        results = grangercausalitytests(
            data,
            maxlag=max_lag,
            verbose=False
        )

        print("Granger Causality completed successfully.")

        return results

    except Exception as error:

        print("Error:", error)

        return None


def print_granger_summary(results):
    """
    Print p-values for each lag.
    """

    if results is None:
        return

    print("\nP-Values\n")

    for lag in results:

        p_value = results[lag][0]["ssr_ftest"][1]

        print(f"Lag {lag}: {p_value:.4f}")
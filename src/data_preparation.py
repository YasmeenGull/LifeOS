import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


def prepare_features(dataframe):

    dataframe = dataframe.copy()

    category_encoder = LabelEncoder()

    dataframe["category"] = category_encoder.fit_transform(
        dataframe["category"]
    )

    X = dataframe[
        [
            "duration",
            "category"
        ]
    ]

    y = dataframe["activity"]

    return X, y


def split_dataset(
    X,
    y,
    test_size=0.20,
    random_state=42
):
    """
    Split data into training and testing sets.
    """

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state
    )

    return X_train, X_test, y_train, y_test


def print_dataset_information(
    X_train,
    X_test
):

    print("\n========== DATASET ==========\n")

    print("Training Samples :", len(X_train))

    print("Testing Samples  :", len(X_test))
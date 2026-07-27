import numpy as np
from hmmlearn import hmm


def train_hmm(dataframe):
    """
    Train a Hidden Markov Model using activities.
    """

    observations = dataframe["activity"].values.reshape(-1, 1)

    model = hmm.CategoricalHMM(
        n_components=3,
        random_state=42,
        n_iter=100
    )

    model.fit(observations)

    return model


def predict_states(model, dataframe):
    """
    Predict hidden states.
    """

    observations = dataframe["activity"].values.reshape(-1, 1)

    states = model.predict(observations)

    return states


def print_states(states):

    print("\n========== HIDDEN STATES ==========\n")

    for index, state in enumerate(states):

        print(f"Activity {index + 1} --> State {state}")
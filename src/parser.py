import pandas as pd


def read_screen_time(file_path):

    dataframe = pd.read_csv(file_path)

    return dataframe


def read_browser_history(file_path):

    dataframe = pd.read_csv(file_path)

    return dataframe


def read_mood_sleep(file_path):

    dataframe = pd.read_csv(file_path)

    return dataframe
import pandas as pd


def read_screen_time(file_path):

    dataframe = pd.read_csv(file_path)

    dataframe["source"] = "Screen Time"

    return dataframe


def read_browser_history(file_path):

    dataframe = pd.read_csv(file_path)

    dataframe["source"] = "Browser History"

    return dataframe


def read_mood_sleep(file_path):

    dataframe = pd.read_csv(file_path)

    dataframe["source"] = "Mood Sleep"

    return dataframe
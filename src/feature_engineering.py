import pandas as pd


def create_time_bucket(dataframe, column_name):

    dataframe[column_name] = pd.to_datetime(dataframe[column_name])

    dataframe["Hour"] = dataframe[column_name].dt.hour

    dataframe["TimeBucket"] = pd.cut(

        dataframe["Hour"],

        bins=[0,6,12,18,24],

        labels=["Night","Morning","Afternoon","Evening"],

        include_lowest=True

    )

    return dataframe
import pandas as pd


def create_time_bucket(df, column):

    df[column] = pd.to_datetime(df[column])

    df["Hour"] = df[column].dt.hour

    def bucket(hour):

        if hour < 6:
            return "Night"

        elif hour < 12:
            return "Morning"

        elif hour < 18:
            return "Afternoon"

        return "Evening"

    df["TimeBucket"] = df["Hour"].apply(bucket)

    return df
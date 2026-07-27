def remove_duplicates(dataframe):

    dataframe = dataframe.drop_duplicates()

    return dataframe


def remove_missing_values(dataframe):

    dataframe = dataframe.dropna()

    return dataframe


def validate_data(dataframe):

    dataframe = remove_duplicates(dataframe)

    dataframe = remove_missing_values(dataframe)

    return dataframe
def remove_duplicates(df):

    return df.drop_duplicates()


def remove_missing(df):

    return df.fillna("Unknown")


def validate_data(df):

    df = remove_duplicates(df)

    df = remove_missing(df)

    return df
import os
import pandas as pd
import streamlit as st


FEEDBACK_FILE = "output/dashboard_feedback.csv"


def save_feedback(name, rating, comments):

    os.makedirs("output", exist_ok=True)

    feedback = pd.DataFrame({

        "Name": [name],

        "Rating": [rating],

        "Comments": [comments]

    })

    if os.path.exists(FEEDBACK_FILE):

        old = pd.read_csv(FEEDBACK_FILE)

        feedback = pd.concat(

            [old, feedback],

            ignore_index=True

        )

    feedback.to_csv(

        FEEDBACK_FILE,

        index=False

    )


def feedback_form():

    st.header("📝 User Feedback")

    name = st.text_input("Name")

    rating = st.slider(

        "Dashboard Rating",

        1,

        5,

        5

    )

    comments = st.text_area(

        "Suggestions"

    )

    if st.button("Submit Feedback"):

        save_feedback(

            name,

            rating,

            comments

        )

        st.success(

            "Feedback submitted successfully!"
        )
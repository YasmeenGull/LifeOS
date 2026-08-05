import plotly.express as px
import pandas as pd
import streamlit as st


def discipline_chart():

    data = pd.DataFrame({

        "Day": [

            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri",
            "Sat",
            "Sun"

        ],

        "Score": [

            74,
            79,
            82,
            84,
            87,
            90,
            91

        ]

    })

    fig = px.line(

        data,

        x="Day",

        y="Score",

        markers=True,

        title="Discipline Score Trend"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )


def debt_chart():

    data = pd.DataFrame({

        "Day":[

            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri",
            "Sat",
            "Sun"

        ],

        "Debt":[

            16,
            15,
            13,
            11,
            10,
            8,
            7

        ]

    })

    fig = px.bar(

        data,

        x="Day",

        y="Debt",

        color="Debt",

        title="Behavioral Debt Trend"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )


def entropy_chart():

    data = pd.DataFrame({

        "Day":[

            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri",
            "Sat",
            "Sun"

        ],

        "Entropy":[

            0.91,
            0.88,
            0.84,
            0.80,
            0.78,
            0.75,
            0.71

        ]

    })

    fig = px.area(

        data,

        x="Day",

        y="Entropy",

        title="Behavioral Entropy Trend"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )
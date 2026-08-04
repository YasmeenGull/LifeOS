import streamlit as st


def setup_page():
    st.set_page_config(
        page_title="LifeOS Dashboard",
        page_icon="🧠",
        layout="wide",
        initial_sidebar_state="expanded"
    )


def sidebar():

    st.sidebar.title("🧠 LifeOS")

    st.sidebar.markdown("---")

    page = st.sidebar.radio(

        "Navigation",

        [

            "Dashboard",

            "Life Graph",

            "Goal Alignment",

            "Simulation"

        ]

    )

    st.sidebar.markdown("---")

    st.sidebar.success("Tynovate Internship 2026")

    return page
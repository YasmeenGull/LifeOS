import streamlit as st

from src.dashboard.layout import setup_page
from src.dashboard.layout import sidebar
from src.dashboard.metrics import show_metrics


setup_page()

page = sidebar()

st.title("🧠 LifeOS Dashboard")

st.write(
    "Welcome to the LifeOS Behavioral Analytics Dashboard."
)

st.markdown("---")

if page == "Dashboard":

    st.header("Dashboard")

    show_metrics()

elif page == "Life Graph":

    st.header("Life Graph")

    st.info("Life Graph visualization will appear here.")

elif page == "Goal Alignment":

    st.header("Goal Alignment")

    st.info("Goal Alignment engine will appear here.")

elif page == "Simulation":

    st.header("30-Day Simulation")

    st.info("Simulation results will appear here.")
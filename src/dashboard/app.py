import streamlit as st

from src.dashboard.layout import setup_page
from src.dashboard.layout import sidebar
from src.dashboard.metrics import show_metrics
from src.dashboard.charts import discipline_chart
from src.dashboard.charts import debt_chart
from src.dashboard.charts import entropy_chart
from src.dashboard.goal_alignment import show_goal_alignment
from src.dashboard.simulation import show_simulation
from src.dashboard.feedback import feedback_form


setup_page()

page = sidebar()
st.markdown("---")

if page == "Dashboard":

    st.title("🧠 LifeOS Behavioral Dashboard")
    st.write(
    "Welcome to the LifeOS Behavioral Analytics Dashboard."
)

    tab1, tab2 = st.tabs([
        "📊 Metrics",
        "📈 Analytics"
    ])

    with tab1:
        show_metrics()

    with tab2:
        discipline_chart()
        debt_chart()
        entropy_chart()
    


elif page == "Life Graph":

    
    discipline_chart()

    debt_chart()

    entropy_chart()

elif page == "Goal Alignment":

    show_goal_alignment()

elif page == "Simulation":

    show_simulation()
    
elif page == "Feedback":

    feedback_form()
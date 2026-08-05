import streamlit as st

from src.discipline_score import DisciplineScoreEngine
from src.behavioral_debt import BehavioralDebt


def get_entropy():
    """
    Temporary entropy value.
    Replace with the real behavioral engine in a later update.
    """
    return 0.82


def get_discipline_score():
    engine = DisciplineScoreEngine(
        focus_ratio=85,
        recovery_time=80,
        sleep_consistency=90
    )

    return engine.calculate_score()


def get_behavioral_debt():
    debt = BehavioralDebt()

    debt.accumulate(
        context_switch_cost=4,
        late_night_usage=3,
        distraction_count=2
    )

    return debt.debt


def show_metrics():

    entropy = get_entropy()

    score = get_discipline_score()

    behavioral_debt = get_behavioral_debt()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🧠 Behavioral Entropy",
            round(entropy, 2)
        )

    with col2:
        st.metric(
            "🎯 Discipline Score",
            score
        )

    with col3:
        st.metric(
            "⚠ Behavioral Debt",
            round(behavioral_debt, 2)
        )
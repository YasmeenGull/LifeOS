import streamlit as st


class GoalAlignmentEngine:

    def __init__(

        self,

        goal_name,

        target_hours,

        completed_hours,

        remaining_days

    ):

        self.goal_name = goal_name

        self.target_hours = target_hours

        self.completed_hours = completed_hours

        self.remaining_days = remaining_days


    def remaining_hours(self):

        return max(

            self.target_hours -

            self.completed_hours,

            0

        )


    def daily_required(self):

        if self.remaining_days == 0:

            return 0

        return round(

            self.remaining_hours()

            /

            self.remaining_days,

            2

        )


    def alignment_percentage(self):

        return round(

            (

                self.completed_hours

                /

                self.target_hours

            )

            *

            100,

            2

        )


def show_goal_alignment():

    st.header("🎯 Goal Alignment")

    goal = GoalAlignmentEngine(

        goal_name="AI Internship",

        target_hours=150,

        completed_hours=95,

        remaining_days=22

    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(

            "Target Hours",

            goal.target_hours

        )

        st.metric(

            "Completed Hours",

            goal.completed_hours

        )

        st.metric(

            "Remaining Hours",

            goal.remaining_hours()

        )

    with col2:

        st.metric(

            "Days Left",

            goal.remaining_days

        )

        st.metric(

            "Daily Required",

            goal.daily_required()

        )

        st.metric(

            "Goal Alignment",

            f"{goal.alignment_percentage()} %"

        )

    st.progress(

        goal.alignment_percentage()

        /

        100

    )
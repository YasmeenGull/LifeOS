import pandas as pd
import plotly.express as px
import streamlit as st


class ProductivitySimulation:

    def __init__(

        self,

        current_productivity,

        optimized_productivity,

        days=30

    ):

        self.current = current_productivity

        self.optimized = optimized_productivity

        self.days = days

    def simulate(self):

        current_values = []
        optimized_values = []

        current = self.current
        optimized = self.optimized

        for day in range(1, self.days + 1):

            current += 0.5
            optimized += 1.2

            current_values.append(current)
            optimized_values.append(optimized)

        dataframe = pd.DataFrame({

            "Day": range(1, self.days + 1),

            "Current Pattern": current_values,

            "Optimized Pattern": optimized_values

        })

        return dataframe


def show_simulation():

    st.header("🚀 30-Day Productivity Simulation")

    simulator = ProductivitySimulation(

        current_productivity=65,

        optimized_productivity=65,

        days=30

    )

    dataframe = simulator.simulate()

    fig = px.line(

        dataframe,

        x="Day",

        y=[

            "Current Pattern",

            "Optimized Pattern"

        ],

        markers=True,

        title="30-Day Productivity Forecast"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.success(

        f"Projected Productivity (Current): {round(dataframe['Current Pattern'].iloc[-1],2)}"

    )

    st.success(

        f"Projected Productivity (Optimized): {round(dataframe['Optimized Pattern'].iloc[-1],2)}"

    )
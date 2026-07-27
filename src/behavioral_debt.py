class BehavioralDebt:

    def __init__(self):
        self.debt = 0.0

    def accumulate(
        self,
        context_switch_cost,
        late_night_usage,
        distraction_count
    ):

        self.debt += (
            context_switch_cost
            + late_night_usage
            + distraction_count
        )

        return round(self.debt, 2)

    def decay(self, decay_rate=0.10):

        self.debt *= (1 - decay_rate)

        return round(self.debt, 2)


def print_behavioral_debt(debt):

    print("\n========== BEHAVIORAL DEBT ==========")
    print(f"Current Debt : {debt:.2f}")

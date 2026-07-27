class DisciplineScoreEngine:
    """
    Calculates the Discipline Score.
    """

    def __init__(self, focus_ratio, recovery_time, sleep_consistency):

        self.focus_ratio = focus_ratio
        self.recovery_time = recovery_time
        self.sleep_consistency = sleep_consistency

    def calculate_score(self):

        score = (
            self.focus_ratio * 0.50
            + self.recovery_time * 0.25
            + self.sleep_consistency * 0.25
        )

        return round(score, 2)


def print_score(score):

    print("\n========== DISCIPLINE SCORE ==========")
    print(f"Score : {score}/100")


# ---------- TEMPORARY TEST ----------
if __name__ == "__main__":

    engine = DisciplineScoreEngine(
        focus_ratio=85,
        recovery_time=80,
        sleep_consistency=90
    )

    score = engine.calculate_score()

    print_score(score)
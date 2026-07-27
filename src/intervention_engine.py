from notification import (
    distraction_alert,
    study_break_alert,
    late_night_alert
)

from contextual_bandit import LinUCB

from feedback import (
    save_feedback,
    print_feedback_report
)


bandit = LinUCB()


def run_intervention(trigger):
    """
    Run the appropriate intervention.
    """

    action = bandit.choose_action(trigger)

    print("\n========== INTERVENTION ==========\n")

    print("Trigger :", trigger)
    print("Action  :", action)

    if action == "FOCUS":

        distraction_alert()

    elif action == "BREAK":

        study_break_alert()

    elif action == "SLEEP":

        late_night_alert()

    return action


def update_intervention(action, responded):
    """
    Update reward and feedback.
    """

    reward = 1 if responded else 0

    bandit.update_reward(
        action,
        reward
    )

    save_feedback(
        action,
        responded
    )


def print_intervention_report():
    """
    Print complete intervention report.
    """

    bandit.print_statistics()

    print_feedback_report()
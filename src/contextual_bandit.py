import numpy as np


class LinUCB:
    """
    Simple LinUCB Contextual Bandit.
    """

    def __init__(self):

        self.actions = [
            "BREAK",
            "FOCUS",
            "SLEEP"
        ]

        self.counts = {
            action: 0
            for action in self.actions
        }

        self.rewards = {
            action: 0
            for action in self.actions
        }


    def choose_action(self, trigger):
        """
        Select an intervention based on the trigger.
        """

        if trigger == "DISTRACTION":
            return "FOCUS"

        elif trigger == "LONG_STUDY":
            return "BREAK"

        elif trigger == "LATE_NIGHT":
            return "SLEEP"

        return "FOCUS"


    def update_reward(
        self,
        action,
        reward
    ):
        """
        Update reward statistics.
        """

        self.counts[action] += 1
        self.rewards[action] += reward


    def print_statistics(self):
        """
        Display action statistics.
        """

        print("\n========== LINUCB ==========\n")

        for action in self.actions:

            print(
                f"{action} | "
                f"Count: {self.counts[action]} | "
                f"Reward: {self.rewards[action]}"
            )
import unittest

from src.behavioral_debt import BehavioralDebt


class TestBehavioralDebt(unittest.TestCase):

    def test_accumulate(self):

        debt = BehavioralDebt()

        result = debt.accumulate(

            context_switch_cost=10,

            late_night_usage=5,

            distraction_count=2

        )

        self.assertEqual(result, 17)

    def test_decay(self):

        debt = BehavioralDebt()

        debt.accumulate(

            context_switch_cost=20,

            late_night_usage=10,

            distraction_count=10

        )

        result = debt.decay()

        self.assertEqual(result, 36)


if __name__ == "__main__":

    unittest.main()
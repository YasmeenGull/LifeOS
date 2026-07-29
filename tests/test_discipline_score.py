import unittest

from src.discipline_score import DisciplineScoreEngine


class TestDisciplineScore(unittest.TestCase):

    def test_score(self):

        engine = DisciplineScoreEngine(

            focus_ratio=80,

            recovery_time=90,

            sleep_consistency=70

        )

        score = engine.calculate_score()

        self.assertGreaterEqual(score, 0)

        self.assertLessEqual(score, 100)


if __name__ == "__main__":

    unittest.main()
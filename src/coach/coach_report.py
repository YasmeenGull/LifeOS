from anthropic import APIError

from src.coach.anthropic_client import AnthropicCoachClient
from src.coach.fallback_report import FallbackCoachReport
from src.monitoring.logger import get_logger


class WeeklyCoachReport:
    """Generate weekly behavioral coaching reports."""

    def __init__(self):
        self.logger = get_logger("lifeos.coach")
        self.client = AnthropicCoachClient()
        self.fallback = FallbackCoachReport()

    def generate(
        self,
        entropy,
        discipline_score,
        behavioral_debt,
        focus_ratio,
        recovery_time,
    ):
        """Generate an AI report or use the local fallback."""

        self.logger.info("Generating weekly coach report.")

        prompt = f"""
You are the LifeOS Behavioral Coach.

Generate a professional weekly behavioral coaching report.

Behavioral metrics:

- Entropy: {entropy}
- Discipline Score: {discipline_score}/100
- Behavioral Debt: {behavioral_debt}
- Focus Ratio: {focus_ratio}%
- Recovery Time: {recovery_time}%

Include:

1. Weekly summary
2. Behavioral strengths
3. Areas for improvement
4. Three practical recommendations
5. One goal for next week

Keep the report concise, professional and actionable.
"""

        try:
            report = self.client.generate_response(prompt)

            self.logger.info(
                "Weekly coach report generated successfully."
            )

            return report

        except APIError as error:
            self.logger.warning(
                "Anthropic API unavailable. Using local fallback: %s",
                error,
            )

            return self._generate_fallback(
                entropy,
                discipline_score,
                behavioral_debt,
                focus_ratio,
                recovery_time,
            )

        except Exception as error:
            self.logger.error(
                "Unexpected coach service error. Using fallback: %s",
                error,
            )

            return self._generate_fallback(
                entropy,
                discipline_score,
                behavioral_debt,
                focus_ratio,
                recovery_time,
            )

    def _generate_fallback(
        self,
        entropy,
        discipline_score,
        behavioral_debt,
        focus_ratio,
        recovery_time,
    ):
        """Generate a local report when the LLM is unavailable."""

        self.logger.info("Generating local fallback coach report.")

        return self.fallback.generate(
            entropy=entropy,
            discipline_score=discipline_score,
            behavioral_debt=behavioral_debt,
            focus_ratio=focus_ratio,
            recovery_time=recovery_time,
        )
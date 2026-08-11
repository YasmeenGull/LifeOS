class FallbackCoachReport:
    """Generates a local coaching report when the LLM is unavailable."""

    @staticmethod
    def generate(
        entropy,
        discipline_score,
        behavioral_debt,
        focus_ratio,
        recovery_time
    ):
        recommendations = []

        if discipline_score < 60:
            recommendations.append(
                "Create a consistent daily study routine."
            )
        elif discipline_score < 80:
            recommendations.append(
                "Maintain a more consistent focus schedule."
            )
        else:
            recommendations.append(
                "Continue maintaining your strong discipline."
            )

        if focus_ratio < 70:
            recommendations.append(
                "Reduce distractions and increase focused work sessions."
            )
        else:
            recommendations.append(
                "Continue protecting your focused work periods."
            )

        if behavioral_debt > 30:
            recommendations.append(
                "Reduce context switching and unnecessary interruptions."
            )
        else:
            recommendations.append(
                "Keep behavioral interruptions under control."
            )

        return f"""
========== LIFEOS WEEKLY COACH REPORT ==========

Mode: Local Demo Mode

WEEKLY SUMMARY
Your current discipline score is {discipline_score}/100
with a focus ratio of {focus_ratio}%.

BEHAVIORAL METRICS
• Behavioral Entropy: {entropy}
• Discipline Score: {discipline_score}
• Behavioral Debt: {behavioral_debt}
• Focus Ratio: {focus_ratio}%
• Recovery Time: {recovery_time}%

RECOMMENDATIONS
1. {recommendations[0]}
2. {recommendations[1]}
3. {recommendations[2]}

NEXT WEEK GOAL
Improve consistency while reducing unnecessary context switching.

Note:
Anthropic LLM generation was unavailable, so LifeOS generated
this report using its local fallback coaching engine.
"""
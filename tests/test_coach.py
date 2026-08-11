from src.coach.prompt_builder import build_weekly_coach_prompt


def test_weekly_coach_prompt():

    prompt = build_weekly_coach_prompt(
        entropy=0.45,
        discipline_score=82,
        behavioral_debt=18,
        focus_ratio=78,
        recovery_time=85
    )

    assert "Behavioral Entropy" in prompt
    assert "Discipline Score" in prompt
    assert "Behavioral Debt" in prompt
    assert "Recommendations" in prompt
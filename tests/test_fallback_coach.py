from src.coach.fallback_report import FallbackCoachReport


def test_fallback_coach_report():
    report = FallbackCoachReport.generate(
        entropy=0.45,
        discipline_score=82,
        behavioral_debt=18,
        focus_ratio=78,
        recovery_time=85
    )

    assert report is not None
    assert isinstance(report, str)
    assert "LIFEOS WEEKLY COACH REPORT" in report
    assert "82" in report
    assert "78" in report
    assert "18" in report
from src.monitoring.health import HealthMonitor


def test_health_monitor():
    result = HealthMonitor().check()

    assert result["status"] == "healthy"
    assert result["service"] == "LifeOS"
    assert "timestamp" in result
    
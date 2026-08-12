from datetime import datetime, timezone


class HealthMonitor:
    """Provides basic LifeOS system health information."""

    def check(self) -> dict:
        return {
            "status": "healthy",
            "service": "LifeOS",
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
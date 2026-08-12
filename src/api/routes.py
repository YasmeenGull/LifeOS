from fastapi import APIRouter

from src.api.database import (
    insert_log,
    insert_goal,
    get_logs,
    get_goals,
)
from src.api.schemas import ActivityLog, Goal
from src.coach.coach_report import WeeklyCoachReport
from src.discipline_score import DisciplineScoreEngine
from src.monitoring.health import HealthMonitor
from src.monitoring.logger import get_logger


router = APIRouter()

logger = get_logger("lifeos.api")


@router.post("/log")
def create_log(log: ActivityLog):
    """Create a new behavioral activity log."""

    logger.info(
        "Creating activity log: activity=%s, duration=%s, category=%s",
        log.activity,
        log.duration,
        log.category,
    )

    insert_log(
        activity=log.activity,
        duration=log.duration,
        category=log.category,
    )

    logger.info("Activity log created successfully.")

    return {
        "message": "Log created successfully."
    }


@router.get("/logs")
def read_logs():
    """Return all behavioral activity logs."""

    logger.info("Fetching behavioral logs.")

    logs = get_logs()

    logger.info("Behavioral logs retrieved successfully.")

    return {
        "logs": logs
    }


@router.post("/goals")
def create_goal(goal: Goal):
    """Create a new behavioral goal."""

    logger.info(
        "Creating goal: goal=%s, target=%s",
        goal.goal,
        goal.target,
    )

    insert_goal(
        goal.goal,
        goal.target,
    )

    logger.info("Goal created successfully.")

    return {
        "message": "Goal added successfully."
    }


@router.get("/")
def home():
    """Return LifeOS API status."""

    logger.info("API home endpoint requested.")

    return {
        "message": "LifeOS API is running successfully."
    }


@router.get("/goals")
def read_goals():
    """Return all behavioral goals."""

    logger.info("Fetching behavioral goals.")

    goals = get_goals()

    logger.info("Behavioral goals retrieved successfully.")

    return {
        "goals": goals
    }


@router.get("/score")
def get_score():
    """Calculate and return the current discipline score."""

    logger.info("Calculating discipline score.")

    engine = DisciplineScoreEngine(
        focus_ratio=85,
        recovery_time=80,
        sleep_consistency=90,
    )

    score = engine.calculate_score()

    logger.info(
        "Discipline score calculated successfully: %s",
        score,
    )

    return {
        "discipline_score": score
    }


@router.get("/debt")
def get_debt():
    """Return the current behavioral debt."""

    logger.info("Fetching behavioral debt.")

    debt = 9

    logger.info(
        "Behavioral debt retrieved successfully: %s",
        debt,
    )

    return {
        "behavioral_debt": debt
    }


@router.get("/coach/weekly")
def weekly_coach_report(
    entropy: float = 0.45,
    discipline_score: float = 82,
    behavioral_debt: float = 18,
    focus_ratio: float = 78,
    recovery_time: float = 85,
):
    """Generate a weekly LifeOS behavioral coach report."""

    logger.info("Weekly coach endpoint requested.")

    coach = WeeklyCoachReport()

    report = coach.generate(
        entropy=entropy,
        discipline_score=discipline_score,
        behavioral_debt=behavioral_debt,
        focus_ratio=focus_ratio,
        recovery_time=recovery_time,
    )

    logger.info("Weekly coach report generated successfully.")

    return {
        "status": "success",
        "report": report,
    }


@router.get("/health")
def health_check():
    """Return LifeOS service health status."""

    logger.info("Health check requested.")

    monitor = HealthMonitor()

    result = monitor.check()

    logger.info(
        "Health check completed successfully: %s",
        result["status"],
    )

    return result
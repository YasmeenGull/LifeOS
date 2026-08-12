from fastapi import APIRouter
from src.discipline_score import DisciplineScoreEngine
from src.api.schemas import ActivityLog
from src.api.database import insert_log
from src.api.schemas import Goal
from src.coach.coach_report import WeeklyCoachReport
from src.monitoring.health import HealthMonitor

from src.api.database import (
    insert_log,
    insert_goal,
    get_logs,
    get_goals
)

router = APIRouter()


@router.post("/log")
def create_log(log: ActivityLog):

    insert_log(
        activity=log.activity,
        duration=log.duration,
        category=log.category
    )

    return {
        "message": "Log created successfully."
    }
@router.get("/logs")
def read_logs():

    logs = get_logs()

    return {

        "logs": logs

    }
@router.post("/goals")
def create_goal(goal: Goal):

    insert_goal(

        goal.goal,

        goal.target

    )

    return {

        "message": "Goal added successfully."

    }


@router.get("/")
def home():

    return {
        "message": "LifeOS API is running successfully."
    }
@router.get("/goals")
def read_goals():

    goals = get_goals()

    return {

        "goals": goals

    }

@router.get("/score")
def get_score():

    engine = DisciplineScoreEngine(

        focus_ratio=85,

        recovery_time=80,

        sleep_consistency=90

    )

    score = engine.calculate_score()

    return {
        "discipline_score": score
    }


@router.get("/debt")
def get_debt():

    return {
        "behavioral_debt": 9
    }

@router.get("/coach/weekly")
def weekly_coach_report(
    entropy: float = 0.45,
    discipline_score: float = 82,
    behavioral_debt: float = 18,
    focus_ratio: float = 78,
    recovery_time: float = 85
):
    """Generate a weekly LifeOS behavioral coach report."""

    coach = WeeklyCoachReport()

    report = coach.generate(
        entropy=entropy,
        discipline_score=discipline_score,
        behavioral_debt=behavioral_debt,
        focus_ratio=focus_ratio,
        recovery_time=recovery_time
    )

    return {
        "status": "success",
        "report": report
    }
    
@router.get("/health")
def health_check():
    """Return LifeOS service health status."""

    monitor = HealthMonitor()

    return monitor.check()
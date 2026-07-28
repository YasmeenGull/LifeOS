from fastapi import APIRouter
from src.discipline_score import DisciplineScoreEngine
from src.api.schemas import ActivityLog
from src.api.database import insert_log
from src.api.schemas import Goal

from src.api.database import (
    insert_goal,
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
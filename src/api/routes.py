from fastapi import APIRouter
from src.discipline_score import DisciplineScoreEngine
from src.api.schemas import ActivityLog
from src.api.database import insert_log

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


@router.get("/")
def home():

    return {
        "message": "LifeOS API is running successfully."
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
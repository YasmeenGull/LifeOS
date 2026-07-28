from pydantic import BaseModel


class ActivityLog(BaseModel):

    activity: str

    duration: int

    category: str
class Goal(BaseModel):

        goal: str

        target: int
from pydantic import BaseModel, Field


class ActivityLog(BaseModel):
    activity: str
    duration: int = Field(gt=0)
    category: str


class Goal(BaseModel):
    name: str
    target: int = Field(gt=0)
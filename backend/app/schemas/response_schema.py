from pydantic import BaseModel
from typing import List
from datetime import datetime


class AnalysisResponse(BaseModel):
    possible_conditions: List[str]
    recommended_tests: List[str]
    risk_level: str
    confidence_score: float
    doctor_review_recommended: bool
    disclaimer: str


# This is optional but recommended if you return DB data
class PredictionResponse(AnalysisResponse):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True   # For SQLAlchemy (Pydantic v2)

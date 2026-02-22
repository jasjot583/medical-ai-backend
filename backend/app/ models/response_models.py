from pydantic import BaseModel
from typing import List

class AnalysisResponse(BaseModel):
    possible_conditions: List[str]
    recommended_tests: List[str]
    risk_level: str
    confidence_score: float
    doctor_review_recommended: bool
    disclaimer: str
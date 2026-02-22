from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.symptom_schema import SymptomRequest
from app.schemas.response_schema import AnalysisResponse
from app.services.analysis_service import analyze_and_store

router = APIRouter()


@router.post("/analyze", response_model=AnalysisResponse)
def analyze(data: SymptomRequest, db: Session = Depends(get_db)):
    return analyze_and_store(data.symptoms, db)

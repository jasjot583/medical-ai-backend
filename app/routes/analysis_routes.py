from fastapi import APIRouter
from app.schemas.symptom_schema import SymptomRequest

router = APIRouter()

@router.post("/analyze-symptoms")
def analyze_symptoms(request: SymptomRequest):
    return {
        "received_symptoms": request.symptoms,
        "message": "Analysis logic will be added here"
    }
print("ROUTES FILE LOADED")

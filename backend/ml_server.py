from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Medical AI ML Service")


# Request Schema
class SymptomRequest(BaseModel):
    symptoms: List[str]


# Health Check Route
@app.get("/")
def health_check():
    return {"status": "ML Server Running"}


# Prediction Route
@app.post("/predict")
def predict(data: SymptomRequest):

    symptoms = [s.lower() for s in data.symptoms]

    # Dummy ML logic (replace later with real model)
    if "fatigue" in symptoms and "frequent urination" in symptoms:
        result = {
            "possible_conditions": ["Diabetes"],
            "recommended_tests": ["HbA1c", "Fasting Blood Sugar"],
            "risk_level": "High",
            "confidence_score": 0.85,
            "doctor_review_recommended": True,
            "disclaimer": "This is an AI-generated report. Please consult a doctor."
        }

    elif "bone pain" in symptoms:
        result = {
            "possible_conditions": ["Vitamin D Deficiency"],
            "recommended_tests": ["Vitamin D Blood Test"],
            "risk_level": "Medium",
            "confidence_score": 0.75,
            "doctor_review_recommended": False,
            "disclaimer": "This is an AI-generated report. Please consult a doctor."
        }

    else:
        result = {
            "possible_conditions": ["General Checkup Recommended"],
            "recommended_tests": ["Complete Blood Count (CBC)"],
            "risk_level": "Low",
            "confidence_score": 0.40,
            "doctor_review_recommended": True,
            "disclaimer": "Low confidence prediction. Doctor review recommended."
        }

    return result

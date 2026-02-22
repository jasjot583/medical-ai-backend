from app.services.ml_service import call_ml_service
from app.models.prediction_model import Prediction


def analyze_and_store(symptoms: list[str], db):

    # Call ML microservice
    ml_result = call_ml_service(symptoms)

    confidence = ml_result.get("confidence_score", 0)

    # Enforce doctor review rule
    if confidence < 0.5:
        ml_result["doctor_review_recommended"] = True
    else:
        ml_result["doctor_review_recommended"] = ml_result.get(
            "doctor_review_recommended", False
        )

    # Save to DB
    prediction = Prediction(
        symptoms=symptoms,
        disease=ml_result.get("possible_conditions", ["Unknown"])[0],
        confidence=confidence,
        risk_level=ml_result.get("risk_level", "Unknown"),
    )

    db.add(prediction)
    db.commit()
    db.refresh(prediction)

    return ml_result

from sqlalchemy import Column, Integer, String, Float, DateTime, JSON
from datetime import datetime
from app.database import Base

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    symptoms = Column(JSON)
    disease = Column(String)
    confidence = Column(Float)
    risk_level = Column(String)
    pubmed_results = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)

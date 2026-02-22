from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.routes.analysis_routes import router as analysis_router
from app.database import engine, Base
from app.models.prediction_model import Prediction
import logging

app = FastAPI()

# Create database tables automatically
Base.metadata.create_all(bind=engine)

# Include Routes
app.include_router(analysis_router)

# Root endpoint
@app.get("/")
def root():
    return {"message": "Medical AI Backend Running"}

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "Backend running successfully"}

# Logging setup
logging.basicConfig(level=logging.INFO)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logging.info(f"Incoming request: {request.method} {request.url}")
    response = await call_next(request)
    logging.info(f"Response status: {response.status_code}")
    return response

# Global Exception Handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "message": "Something went wrong. Please try again later."
        }
    )
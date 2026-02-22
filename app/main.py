from fastapi import FastAPI
from app.routes.analysis_routes import router as analysis_router

app = FastAPI()

app.include_router(analysis_router)

@app.get("/")
def root():
    return {"message": "Medical AI Backend Running"}

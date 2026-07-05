from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import database

app = FastAPI(title="GhostWriter Detector API")

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    try:
        await database.command("ping")
        db_status = "connected"
    except Exception:
        db_status = "not connected"

    return {
        "status": "ok",
        "message": "Backend is running",
        "database": db_status,
    }
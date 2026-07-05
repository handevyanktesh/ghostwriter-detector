from fastapi import FastAPI

app = FastAPI(title="GhostWriter Detector API")

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Backend is running"}
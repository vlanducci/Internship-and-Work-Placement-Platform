from fastapi import FastAPI

app = FastAPI(
  title="Internship and Work Placement Platform API",
  version="0.1.0",
)

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/api/test")
def test_connection():
  return {
    "message": "Frontend successfully connected to FastAPI"
  }
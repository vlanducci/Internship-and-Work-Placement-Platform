# main.py
# Creates the FastAPI application and defines test endpoints to verify that the backend is running and the frontend can communicate with it.

from fastapi import FastAPI

# Initialises the FastAPI application with its title and version.
app = FastAPI(
  title="Internship and Work Placement Platform API",
  version="0.1.0",
)

# Defines a health-check endpoint to confirm that the backend is running.
@app.get("/health")
def health_check():
  return {"status": "healthy"}

# Defines a test endpoint to verify communication between Next.js and FastAPI.
@app.get("/api/test")
def test_connection():
  return {
    "message": "Frontend successfully connected to FastAPI"
  }
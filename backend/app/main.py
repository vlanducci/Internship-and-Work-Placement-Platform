from fastapi import FastAPI

app = FastAPI(
  title="Internship and Work Placement Platform API",
  version="0.1.0",
)

@app.get("/health")
def health_check():
  return {"status": "healthy"}
# main.py
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

# Load .env file
load_dotenv()

# Initialize FastAPI app
app = FastAPI(title="AI Scrum Master")

# Allow frontend (Angular) to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this later to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get database URL from environment
DATABASE_URL = os.getenv("DATABASE_URL")

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Health check route
@app.get("/health")
def health_check():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return {"status": "ok", "message": "Database connection successful!"}
    except Exception as e:
        return {"status": "fail", "error": str(e)}
    
@app.get("/standup/latest")
def latest_standup():
    return {"summary": "<b>Yesterday:</b> Fixed bugs<br><b>Today:</b> Deploying updates<br><b>Blockers:</b> None"}


# Root route
@app.get("/")
def root():
    return {"message": "Welcome to AI Scrum Master API"}

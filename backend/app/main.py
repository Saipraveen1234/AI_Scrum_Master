import os
from dotenv import load_dotenv 
from sqlalchemy import create_engine
from sqlalchemy.sql import text

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 1. Load the .env file
load_dotenv() 

# 2. Load the DATABASE_URL from the environment
DATABASE_URL = os.getenv("DATABASE_URL")

# 2. Load the DATABASE_URL from the environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Test the connection (Health Check)
try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("Database connection successful!")
        
except Exception as e:
    print(f"Database connection failed: {e}")
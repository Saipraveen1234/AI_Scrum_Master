from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    role = Column(String(50), default="developer")

    standups = relationship("StandupEntry", back_populates="user")


class StandupEntry(Base):
    __tablename__ = "standup_entries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    yesterday = Column(Text)
    today = Column(Text)
    blockers = Column(Text)
    date = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="standups")


class StandupSummary(Base):
    __tablename__ = "standup_summaries"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, default=datetime.utcnow)
    summary_text = Column(Text)

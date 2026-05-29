from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Enum as SAEnum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from app.core.database import Base


class SolutionStatus(str, enum.Enum):
    PENDING = "pending"
    ACCEPTED = "AC"
    WRONG_ANSWER = "WA"
    COMPILE_ERROR = "CE"
    RUNTIME_ERROR = "RE"
    TIME_LIMIT_EXCEEDED = "TLE"
    MEMORY_LIMIT_EXCEEDED = "MLE"
    OTHER = "OT"


class UserSolution(Base):
    __tablename__ = "user_solutions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    problem_id = Column(Integer, ForeignKey("problems.id"), nullable=False)
    code = Column(Text, nullable=False)
    status = Column(SAEnum(SolutionStatus), default=SolutionStatus.PENDING)
    score = Column(Integer, nullable=True)
    time_used = Column(Integer, nullable=True)  # ms
    memory_used = Column(Integer, nullable=True)  # KB
    submitted_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="solutions")
    problem = relationship("Problem", back_populates="solutions")

from sqlalchemy import Column, Integer, String, Text, Boolean, Float, Enum as SAEnum
from sqlalchemy.orm import relationship
import enum
from app.core.database import Base


class ProblemType(str, enum.Enum):
    CSP_REAL = "csp_real"
    EXERCISE = "exercise"


class Problem(Base):
    __tablename__ = "problems"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    difficulty = Column(Integer, nullable=False)  # 1-5
    time_limit = Column(Integer, default=1000)  # ms
    memory_limit = Column(Integer, default=256)  # MB
    template_code = Column(Text, nullable=True)
    solution_code = Column(Text, nullable=True)
    problem_type = Column(SAEnum(ProblemType), default=ProblemType.EXERCISE)
    is_public = Column(Boolean, default=True)

    solutions = relationship("UserSolution", back_populates="problem")

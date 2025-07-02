from sqlalchemy import Column, Integer, Text, String, CheckConstraint
from sqlalchemy.orm import relationship

from src.db.core.database import Base

class Question(Base):

    """
        Modelo ORM para representar una pregunta en la base de datos

        Atributos:
            - question_id: Identificador único de la pregunta
            - description: Texto completo de la pregunta
            - difficult: Nivel de dificultad de la pregunta ('Easy', 'Medium', 'Hard')
            - options: Lista de opciones asociadas a esta pregunta
    """

    __tablename__ = "questions"

    question_id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(Text, nullable=False)
    difficult = Column(String, nullable=False)

    __table_args__ = (
        CheckConstraint("difficult IN ('Easy', 'Medium', 'Hard')", name="difficult_check"),
    )

    options = relationship("Option", back_populates="question", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<Question(question_id={self.question_id}, description={self.description}, difficult={self.difficult})>"

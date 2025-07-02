from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from src.db.core.database import Base

class Option(Base):

    """
        Modelo ORM para representar una opción en la base de datos

        Atributos:
            - options_id: Identificador único de la opción
            - question_id: Identificador de clave foránea de la pregunta asociada
            - content: Texto de la opción
            - is_correct: Verificación de que la opción es correcta con respecto a la pregunta
    """

    __tablename__ = "options"

    options_id = Column(Integer, primary_key=True, autoincrement=True)
    question_id = Column(Integer, ForeignKey("questions.question_id", ondelete="CASCADE"), nullable=False)
    content = Column(Text, nullable=False)
    is_correct = Column(Boolean, nullable=False)

    question = relationship("Question", back_populates="options")

    def __repr__(self) -> str:
        return f"<Option(options_id={self.options_id}, question_id={self.question_id}, content={self.content}, is_correct={self.is_correct})>"

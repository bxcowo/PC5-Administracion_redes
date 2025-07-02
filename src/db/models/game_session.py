from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.sql import func

from src.db.core.database import Base

class GameSession(Base):

    """
        Modelo ORM para representar una sesión de juego en la base de datos

        Atributos:
            - game_id: Identificador único de la sesión
            - player_name: Nombre del jugador de la sesión guardada
            - total_score: Puntuación total registrada
            - correct_answers: Numero de preguntas correctas de la sesión
            - incorrect_answers: Número de preguntas incorrectas de la sesión
            - game_date: Fecha de realización del juegor registrada
    """

    __tablename__ = "game_sessions"

    game_id = Column(Integer, primary_key=True, autoincrement=True)
    player_name = Column(String, nullable=False)
    total_score = Column(Integer, nullable=False)
    correct_answers = Column(Integer, nullable=False)
    incorrect_answers = Column(Integer, nullable=False)
    game_date = Column(DateTime, nullable=False, default=func.now())

    def __repr__(self) -> str:
        return f"<GameSession(game_id={self.game_id}), player_name={self.player_name}, total_score={self.total_score}>"

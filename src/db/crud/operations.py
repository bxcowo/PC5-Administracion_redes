from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from typing import List

from sqlalchemy.orm.strategy_options import joinedload

from src.db.models.question import Question
from src.db.models.game_session import GameSession

def get_questions(db: Session) -> List[Question]:

    """
        Parametros:
            - db: Sesión activa de operaciones con la base de datos

        Obtención de preguntas solicitadas para nueva sesión de juego mediante SQL asegurandose de obtener 4 de tipo Easy, 3 de tipo Medium y 3 de tipo Hard.
    """

    questions_easy = (
        db.query(Question)
        .options(joinedload(Question.options))
        .filter(Question.difficult == "Easy")
        .order_by(func.random())
        .limit(4)
        .all()
    )

    questions_medium = (
        db.query(Question)
        .options(joinedload(Question.options))
        .filter(Question.difficult == "Medium")
        .order_by(func.random())
        .limit(3)
        .all()
    )

    questions_hard = (
        db.query(Question)
        .options(joinedload(Question.options))
        .filter(Question.difficult == "Hard")
        .order_by(func.random())
        .limit(3)
        .all()
    )

    return questions_easy + questions_medium + questions_hard


def create_game_session(db: Session, player_name: str, score: int, correct_answer: int, incorrect_answer: int) -> GameSession:

    """
        Parametros:
            - db: Sesión activa de operaciones con la base de datos
            - player_name: Nombre del jugador obtenido del
            - score: Puntuación total a guardar
            - correct_answer: Número de preguntas correctamente respondidas
            - incorrect_answer: Número de preguntas correctamente respondidas

        Se encarga de realizar las operaciones necesarias para almacenar los datos de una nueva entrada de una sesión de juego en la base de datos mediante SQL.
    """

    save_session = GameSession(
        player_name = player_name,
        total_score = score,
        correct_answers = correct_answer,
        incorrect_answers = incorrect_answer
    )

    db.add(save_session)
    db.commit()
    db.refresh(save_session)

    return save_session


def get_top_three(db: Session) -> List[GameSession]:

   """
        Parametros:
            - db: Sesión activa de operaciones con la base de datos

        Obtiene las 3 puntuaciones más altas de la base de datos mediante operaciones SQL
   """

   top_scores = (
       db.query(GameSession)
       .order_by(desc(GameSession.total_score))
       .limit(3)
       .all()
   )

   return top_scores

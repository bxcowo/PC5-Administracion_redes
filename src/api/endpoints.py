from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from src.db.core.database import get_db
from src.db.crud.operations import get_questions, get_top_three, create_game_session
from schemas import GameSessionRequest, QuestionResponse, GameSessionResponse

# Creacion de router para la creación de endpoints adecuados
router = APIRouter()

@router.get("/questions", response_model=List[QuestionResponse])
def get_trivia_questions(db: Session = Depends(get_db)):
    """
        Obtiene 10 preguntas de forma aleatoria definidas para el juego de trivia con la condición de obtener:
        - 4 preguntas de dificultad "Easy"
        - 3 preguntas de dificultad "Medium"
        - 3 preguntas de dificultad "Hard"
    """

    questions = get_questions(db)
    return questions

@router.get("/top_scores", response_model=List[GameSessionResponse])
def get_leaderboard(db: Session = Depends(get_db)):

    """
        Obtiene las 3 primeras puntuaciones con el puntaje más alto dentro de la base de datos
    """

    scores = get_top_three(db)
    return scores


@router.post("/game_session", response_model=GameSessionResponse, status_code=201)
def record_game_session(game_data: GameSessionRequest, db: Session = Depends(get_db)):

    """
        Permite guardar las sesiones de juego de algun usuario siempre y cuando este haya terminado la sesión de juego
        correctamente, para este se necesitan completar un objeto GameSessionRequest
    """

    session = create_game_session(
        db,
        player_name=game_data.player_name,
        score=game_data.total_score,
        correct_answer=game_data.correct_answers,
        incorrect_answer=game_data.incorrect_answers
    )
    return session

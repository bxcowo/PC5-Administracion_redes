from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

# Declaración de modelos pydantic para requests y responses del aplicativo FastAPI

class OptionResponse(BaseModel):
    """
        Clase response para la representación de las opciones pertenecientes a sus respectivas preguntas:
            - options_id: Identificador único de las opciones
            - content: Mensaje de la opción
            - is_correct: Flag para saber si la opción es la correcta
    """

    options_id: int
    content: str
    is_correct: bool

    model_config = ConfigDict(from_attributes=True)


class QuestionResponse(BaseModel):
    """
        Clase response para la representación de las preguntas extraidas de la base de datos:
            - question_id: Identificador único de las preguntas
            - description: Mensaje de la pregunta
            - difficult: Categoría de dificultad ('Easy', 'Medium', 'Hard')
            - options: Lista de opciones asociadas a la pregunta
    """

    question_id: int
    description: str
    difficult: str
    options: List[OptionResponse]

    model_config = ConfigDict(from_attributes=True)


class GameSessionRequest(BaseModel):
    """
        Clase request para el guardado de los juegos realizados por los usuarios una vez completado en su totalidad:
            - player_name: Nombre del jugador
            - total_score: Puntuación total final
            - correct_answers: Número de respuestas correctas
            - incorrect_answers: Número de respuestas incorrectas
    """

    player_name: str
    total_score: int
    correct_answers: int
    incorrect_answers: int


class GameSessionResponse(BaseModel):
    """
        Clase response como confirmación del guardado adecuado de las sesiones de juego en la base de datos:
            - game_id: Identificador único en la base de datos de los juegos
            - player_name: Nombre del jugador registrado
            - total_score: Puntuación total registrada
            - correct_answers: Número de respuestas correctas registradas
            - incorrect_answers: Número de respuestas incorrectas registradas
    """

    game_id: int
    player_name: str
    total_score: int
    correct_answers: int
    incorrect_answers: int
    game_date: datetime

    model_config = ConfigDict(from_attributes=True)

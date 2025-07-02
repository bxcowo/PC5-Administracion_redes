import pytest

from game_objects.question import Question
from game_objects.quiz import Quiz

def test_question_correct_answer():
    question = Question(
        description="¿Cuál es la capital del Perú?",
        difficult="Medium",
        options=[
            "Buenos Aires",
            "Bogotá",
            "Lima",
            "Quito"
        ],
        correct_answer=3
    )

    assert question.is_correct(3)


def test_question_incorrect_answer():
    question = Question(
        description="¿Cuál es la capital del Perú?",
        difficult="Medium",
        options=[
            "Buenos Aires",
            "Bogotá",
            "Lima",
            "Quito"
        ],
        correct_answer=3
    )

    assert not question.is_correct(1)


def test_question_invalid_answer():
    question = Question(
        description="¿Cuál es la capital del Perú?",
        difficult="Medium",
        options=[
            "Buenos Aires",
            "Bogotá",
            "Lima",
            "Quito"
        ],
        correct_answer=3
    )

    assert not question.is_correct("")


def test_question_attributes():
    question = Question(
        description="¿Cuál es la capital del Perú?",
        difficult="Medium",
        options=[
            "Buenos Aires",
            "Bogotá",
            "Lima",
            "Quito"
        ],
        correct_answer=3
    )

    assert question.description == "¿Cuál es la capital del Perú?"
    assert question.difficult == "Medium"
    assert question.options == [
        "Buenos Aires",
        "Bogotá",
        "Lima",
        "Quito"
    ]
    assert question.correct_answer == 3


def test_quiz_correct_answer_update():
    question = Question(
           description="¿Cuál es la capital del Perú?",
           difficult="Medium",
           options=[
               "Buenos Aires",
               "Bogotá",
               "Lima",
               "Quito"
           ],
           correct_answer=3
       )

    quiz = Quiz()
    quiz.load_question(question)

    question = quiz.get_question()
    quiz.update_score(3)

    assert quiz.num_correct == 1 and quiz.score == 5


def test_quiz_incorrect_answer_update():
    question = Question(
           description="¿Cuál es la capital del Perú?",
           difficult="Medium",
           options=[
               "Buenos Aires",
               "Bogotá",
               "Lima",
               "Quito"
           ],
           correct_answer=3
       )

    quiz = Quiz()
    quiz.load_question(question)

    question = quiz.get_question()
    quiz.update_score(1)

    assert quiz.num_incorrect == 1 and quiz.score != 5


def test_quiz_invalid_answer_update():
    question = Question(
           description="¿Cuál es la capital del Perú?",
           difficult="Medium",
           options=[
               "Buenos Aires",
               "Bogotá",
               "Lima",
               "Quito"
           ],
           correct_answer=3
       )

    quiz = Quiz()
    quiz.load_question(question)

    question = quiz.get_question()
    quiz.update_score("")

    assert quiz.num_incorrect == 1 and quiz.score == 0

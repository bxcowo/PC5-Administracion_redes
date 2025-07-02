from fastapi.testclient import TestClient

from src.api.app import app

client = TestClient(app)

def test_get_trivia_questions_correct_return():
    response = client.get("/questions")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 10


def test_get_trivia_questions_correct_distribution():
    response = client.get("/questions")

    assert response.status_code == 200

    questions = response.json()

    preguntas_easy = sum(1 for i in questions if i.get("difficult") == "Easy")
    preguntas_medium = sum(1 for i in questions if i.get("difficult") == "Medium")
    preguntas_hard = sum(1 for i in questions if i.get("difficult") == "Hard")

    assert preguntas_easy == 4
    assert preguntas_medium == 3
    assert preguntas_hard == 3


def test_get_trivia_correct_sub_structure():
    response = client.get("/questions")

    assert response.status_code == 200

    questions = response.json()

    for question in questions:
        assert "question_id" in question
        assert isinstance(question["question_id"], int)
        assert "description" in question
        assert isinstance(question["description"], str)
        assert "difficult" in question
        assert isinstance(question["difficult"], str)
        assert "options" in question
        assert isinstance(question["options"], list)
        assert len(question["options"]) == 4
        for option in question["options"]:
            assert "options_id" in option
            assert isinstance(option["options_id"], int)
            assert "content" in option
            assert isinstance(option["content"], str)
            assert "is_correct" in option
            assert isinstance(option["is_correct"], bool)


def test_correct_post_game_session():
    response = client.post(
        "/game_session",
        json={
            "player_name": "aaa",
            "total_score": 30,
            "correct_answers": 3,
            "incorrect_answers": 7
        }
    )

    ideal_response = {
        "player_name": "bbb",
        "total_score": 30,
        "correct_answers": 3,
        "incorrect_answers": 7
    }

    assert response.status_code == 201
    assert set(ideal_response).issubset((set(response.json())))


def test_incorrect_post_game_session():
    response = client.post(
        "/game_session",
        json={
            "player_name": "joa",
            "total_score": 30,
            "correct_answers": 3,
            "incorrect_answers": 7
        }
    )

    true_response = response.json()

    ideal_response = {
        "player_name": "eli",
        "total_score": 20,
        "correct_answers": 4,
        "incorrect_answers": 6
    }

    assert response.status_code == 201
    assert ideal_response["player_name"] is not true_response["player_name"]
    assert ideal_response["total_score"] is not true_response["total_score"]
    assert ideal_response["correct_answers"] is not true_response["correct_answers"]
    assert ideal_response["incorrect_answers"] is not true_response["incorrect_answers"]


def test_get_leaderboard_correct_return():
    response = client.get("/top_scores")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 3


def test_get_leaderboard_sub_structure():
    response = client.get("/top_scores")

    assert response.status_code == 200

    scores = response.json()

    for score in scores:
        assert "game_id" in score
        assert isinstance(score["game_id"], int)
        assert "player_name" in score
        assert isinstance(score["player_name"], str)
        assert "total_score" in score
        assert isinstance(score["total_score"], int)
        assert "correct_answers" in score
        assert isinstance(score["correct_answers"], int)
        assert "incorrect_answers" in score
        assert isinstance(score["incorrect_answers"], int)
        assert "game_date" in score
        assert isinstance(score["game_date"], str)

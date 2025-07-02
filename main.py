import requests
import os
import sys
from typing import List, Dict, Any

from game_objects.question import Question
from game_objects.quiz import Quiz


BASE_URL = "http://localhost:8000/"


def clear():

    """
        Limpia por completo la terminal
    """

    os.system('clear')


def mostrar_menu() -> int:

    """
        Función de aparición de menu de juego con múltiples opciones de elección del jugador
    """

    clear()
    print("""

     ______   ______   ______   ______   ______   ______   ______   ______   ______   ______   ______
    /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/
    /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/

    __________.__                                 .__    .___
    \______   \__| ____   _______  __ ____   ____ |__| __| _/____  ______
     |    |  _/  |/ __ \ /    \  \/ // __ \ /    \|  |/ __ |/  _ \/  ___/
     |    |   \  \  ___/|   |  \   /\  ___/|   |  \  / /_/ (  <_> )___ \.
     |______  /__|\___  >___|  /\_/  \___  >___|  /__\____ |\____/____  >
            \/        \/     \/          \/     \/        \/          \/
           .__      __         .__      .__         __________          __  .__
    _____  |  |   _/  |________|__|__  _|__|____    \______   \___.__._/  |_|  |__   ____   ____
    \__  \ |  |   \   __\_  __ \  \  \/ /  \__  \    |     ___<   |  |\   __\  |  \ /  _ \ /    \.
     / __ \|  |__  |  |  |  | \/  |\   /|  |/ __ \_  |    |    \___  | |  | |   Y  (  <_> )   |  \.
    (____  /____/  |__|  |__|  |__| \_/ |__(____  /  |____|    / ____| |__| |___|  /\____/|___|  /
         \/                                     \/             \/                \/            \/

     ______   ______   ______   ______   ______   ______   ______   ______   ______   ______   ______
    /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/
    /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/


        """)
    print("1. Comenzar un nuevo juego")
    print("2. Ver primeros puestos")
    print("3. Salir")

    while True:
        try:
            choice = int(input("\n====> "))
            if 1 <= choice <= 3:
                return choice
            else:
                print("Porfavor ingresa un valor entre 1 y 3")
        except ValueError:
            print("Porfavor ingrese un valor válido")


def comenzar_juego():

    """
        Comienza una partida del juego de trivia
    """

    clear()
    print("Comenzando un nuevo juego...\n")

    try:
        response = requests.get(f"{BASE_URL}/questions")
        if response.status_code == 200:
            questions = response.json()
            jugar(questions)
        else:
            print(f"Error al recibir las preguntas: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error de conexión: {e}")

    input("Presione [Enter] para regresar al menú...")


def jugar(questions: List[Dict[str, Any]]):

    """
        Corre el juego de trivia por completo.
    """

    clear()

    quiz = Quiz()

    for elem in questions:
        correct_index = 0
        list_options = []
        for i in range(len(elem['options'])):
            list_options.append(elem['options'][i]['content'])
            if elem['options'][i]['is_correct']:
                correct_index = i

        qst = Question(
            description=elem['description'],
            difficult=elem['difficult'],
            options=list_options,
            correct_answer=correct_index
        )

        quiz.load_question(qst)


    print(
        """

         ______   ______   ______   ______   ______   ______
        /_____/  /_____/  /_____/  /_____/  /_____/  /_____/
        /_____/  /_____/  /_____/  /_____/  /_____/  /_____/


        __________              .__
        \______   \ ____   ____ |  | _____    ______
         |       _// __ \ / ___\|  | \__  \  /  ___/
         |    |   \  ___// /_/  >  |__/ __ \_\___ \.
         |____|_  /\___  >___  /|____(____  /____  >
                \/     \/_____/           \/     \/

         ______   ______   ______   ______   ______   ______
        /_____/  /_____/  /_____/  /_____/  /_____/  /_____/
        /_____/  /_____/  /_____/  /_____/  /_____/  /_____/


        1. Las rondas constan de 10 preguntas: 4 de dificultad Fácil (1 pto.), 3 de dificultad Media (5 pto.) y 3 de dificultad Difícil (10 pto.)
        2. Las partidas de juego solo guardarán una vez concluidas las 10 preguntas
        3. No hay tiempo límite, así que tómate tu tiempo


        """
    )

    input("Presione [Enter] para continuar...")
    clear()

    while not quiz.is_over():
        curr_question = quiz.get_question()
        print(
            f"""
            {quiz.current_index}.- {curr_question.description}:
               1. {curr_question.options[0]}
               2. {curr_question.options[1]}
               3. {curr_question.options[2]}
               4. {curr_question.options[3]}
            """
        )

        while True:
            try:
                answer = int(input("\n              Tu respuesta: "))
                if 1 <= answer <= len(curr_question.options):
                    quiz.update_score(answer - 1)
                    break
                else:
                    print(f"Por favor ingresa un valor entre 1 y {len(curr_question.options)}")
            except ValueError:
                print("Por favor ingresa un valor válido")

        print()

    clear()

    print(
        """

     ______   ______   ______   ______   ______   ______   ______   ______
    /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/
    /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/


    __________                    .__   __              .___
    \______   \ ____   ________ __|  |_/  |______     __| _/____  ______
     |       _// __ \ /  ___/  |  \  |\   __\__  \   / __ |/  _ \/  ___/
     |    |   \  ___/ \___ \|  |  /  |_|  |  / __ \_/ /_/ (  <_> )___ \.
     |____|_  /\___  >____  >____/|____/__| (____  /\____ |\____/____  >
           \/     \/     \/                     \/      \/          \/

     ______   ______   ______   ______   ______   ______   ______   ______
    /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/
    /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/


        """
    )
    print(f"Puntaje total: {quiz.score}")
    print(f"Respuestas correctas: {quiz.num_correct}")
    print(f"Respuestas incorrectas: {quiz.num_incorrect}")

    # Submit score to API
    player_name = input("\nEscribe tu nombre para registrar tu puntaje: ")
    try:
        score_response = requests.post(
            f"{BASE_URL}/game_session",
            json={"player_name": player_name, "total_score": quiz.score, "correct_answers": quiz.num_correct, "incorrect_answers": quiz.num_incorrect}
        )
        if score_response.status_code == 201:
            print("¡Puntaje guardado correctamente!")
        else:
            print(f"Error al enviar resultado: {score_response.status_code}")
    except requests.RequestException as e:
        print(f"Error de conexión: {e}")

def mostrar_leaderboard():

    """
        Muestra el top 3 de sesiones de juego de la base de datos
    """

    clear()

    print(
        """

         ______   ______   ______   ______   ______   ______   ______   ______   ______
        /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/
        /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/


        .____                      .___          ___.                          .___
        |    |    ____  _____    __| _/__________\_ |__   _________ _______  __| _/
        |    |  _/ __ \ \__  \  / __ |/ __ \_  __ \ __ \ /  _ \__ \ \_  __ \/ __ |
        |    |__\  ___/ / __ \_/ /_/ \  ___/|  | \/ \_\ (  <_> ) __ \|  | \/ /_/ |
        |_______ \___  >____  /\____ |\___  >__|  |___  /\____(____  /__|  \____ |
                \/   \/     \/      \/    \/          \/           \/           \/


         ______   ______   ______   ______   ______   ______   ______   ______   ______
        /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/
        /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/


        """
    )

    try:
        response = requests.get(f"{BASE_URL}/top_scores")
        if response.status_code == 200:
            leaderboard = response.json()

            if not leaderboard:
                print("Aún no hay puntajes!")
            else:
                for i in range(len(leaderboard)):
                    print(
                        f"""
                        >> {i + 1}° Puesto << - Nombre: {leaderboard[i]['player_name']} - Puntaje: {leaderboard[i]['total_score']} //// {leaderboard[i]['game_date']}
                        """
                    )

        else:
            print(f"Error al obtener el leaderboard: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error de conexión: {e}")

    input("Presione [Enter] para regresar al menú principial...")
    clear()

def main():

    """
        Función de inicialización de juego de trivia
    """

    while True:
        num = mostrar_menu()

        if num == 1:
            comenzar_juego()
        elif num == 2:
            mostrar_leaderboard()
        elif num == 3:
            print("¡Muchas gracias por jugar!")
            sys.exit(0)

if __name__ == "__main__":
    main()

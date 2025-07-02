from game_objects.question import Question

class Quiz:

    """
    Clase de definición de objeto de juego como Quiz:
        - questions: Lista de preguntas asociadas a dicho quiz
        - current_index: Índice actual de la lista de preguntas
        - score: Puntuación total obtenida
        - num_correct: Número de preguntas respondida correctamente
        - num_incorrect: Número de preguntas respondida incorrectamente
    """

    def __init__(self) -> None:
        self.questions: list[Question] = []
        self.current_index: int = 0
        self.score: int = 0
        self.num_correct: int = 0
        self.num_incorrect: int = 0


    def load_question(self, question: Question) -> None:

        """
            Parametros:
                - question: Objeto del tipo Question

            Añade a la lista de preguntas (questions) una instancia de un objeto de tipo Question
        """
        if type(question) is Question:
            self.questions.append(question)


    def get_question(self) -> Question:

        """
            Devuelve la pregunta asociada con el indice actual guardado
        """

        result = self.questions[self.current_index]
        self.current_index += 1
        return result


    def update_score(self, answer: int) -> None:

        """
            Parametro:
                - answer: Respuesta enviada por el usuario

            Función que valida la respuesta dada con la pregunta actual y permite actualizar el puntaje total guardado
        """

        if self.questions[self.current_index - 1].is_correct(answer):
            self.num_correct += 1
            self.score += self.questions[self.current_index - 1].give_rewards()
        else:
            self.num_incorrect += 1


    def is_over(self) -> bool:

        """
            Flag que permite saber si es que se recorrió por completo la lista de preguntas almacenada
        """

        return self.current_index == len(self.questions)

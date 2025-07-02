class Question:

    """
        Clase de definición de objeto de juego como Question:
            - description: Texto de la pregunta
            - difficult: Dificultad de la pregunta (Easy, Medium o Hard)
            - options: Lista de opciones asignada a la pregunta
            - correct_answer: Indice de la opción correcta
    """

    def __init__(self, description: str, difficult: str, options: list[str], correct_answer: int) -> None:
        self.description = description
        self.difficult = difficult
        self.options = options
        self.correct_answer = correct_answer


    def is_correct(self, answer: int) -> bool:

        """
            Parametros:
                - answer: Respuesta enviada por el usuario

            Devuelve un valor booleano de confirmación si su respuesta coincide con aquella obtenia en la base de datos
        """

        if type(answer) != int:
            return False
        return self.correct_answer == answer


    def give_rewards(self) -> int:

        """
            Devuelve el valor de la recompensa asignada a la pregunta dependiendo de su dificultad dada
        """

        match self.difficult:
            case "Easy":
                return 1
            case "Medium":
                return 5
            case "Hard":
                return 10
            case _:
                return 0

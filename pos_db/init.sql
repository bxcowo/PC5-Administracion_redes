-- Inicializacion de la tabla Questions
CREATE TABLE Questions (
    question_id serial NOT NULL,
    description text NOT NULL,
    difficult varchar(6) NOT NULL,
    CONSTRAINT questions_pk PRIMARY KEY (question_id),
    CONSTRAINT difficult_check CHECK (difficult IN ('Easy', 'Medium', 'Hard'))
);

-- Inicializacion de la tabla Options
CREATE TABLE Options (
    options_id serial NOT NULL,
    question_id integer NOT NULL,
    content text NOT NULL,
    is_correct boolean NOT NULL,
    CONSTRAINT options_pk PRIMARY KEY (options_id),
    CONSTRAINT options_fk_questions FOREIGN KEY (question_id) REFERENCES Questions (question_id) ON DELETE CASCADE
);

-- Inicializacion de la tabla de registros de juegos Game_Sessions
CREATE TABLE Game_Sessions (
    game_id serial NOT NULL,
    player_name varchar(3) NOT NULL,
    total_score integer NOT NULL,
    correct_answers integer NOT NULL,
    incorrect_answers integer NOT NULL,
    game_date timestamp NOT NULL,
    CONSTRAINT game_sessions_pk PRIMARY KEY (game_id)
);

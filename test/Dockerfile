FROM python:3.10-slim

WORKDIR /app

COPY ./src/requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install pytest httpx pytest-cov

COPY ./src ./src
COPY ./test ./test
COPY ./game_objects ./game_objects

CMD ["pytest", "test/", "-v", "--cov=src", "--cov=game_objects"]

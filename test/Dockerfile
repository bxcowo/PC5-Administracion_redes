FROM python:3.10-slim

WORKDIR /app

COPY ./src/requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install pytest httpx

COPY ./src ./src
COPY ./test ./test

CMD ["pytest", "test/", "-v"]

FROM python:3.10-slim

WORKDIR /app

COPY ./src/requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./src ./src

CMD [ "uvicorn", "src.api.app:app", "--host", "0.0.0.0", "--reload", "--port", "8000" ]

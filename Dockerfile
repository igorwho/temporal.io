FROM python:3.12-slim

RUN pip install --no-cache poetry

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && poetry install --no-root

COPY . .

EXPOSE 7233 9092

ENV KAFKA_BROKER=localhost:9092
ENV TEMPORAL_SERVER=localhost:7233

CMD ["poetry", "run", "python", "app/main.py"]

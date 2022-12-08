FROM python:3.9-slim-buster as base
WORKDIR /code
COPY . /code
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install
RUN poetry env info
RUN poetry run pytest

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]

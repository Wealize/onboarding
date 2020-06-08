FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

RUN pip install 'poetry==1.0.5'
COPY poetry.lock pyproject.toml ./
RUN poetry install

COPY . .

CMD ["poetry", "run", "cli.py"]

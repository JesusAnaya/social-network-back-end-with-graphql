FROM python:3.8-slim
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

# Install pipenv and compilation dependencies
RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

RUN mkdir /code
WORKDIR /code

# Install python dependencies in /.venv
COPY Pipfile Pipfile.lock /code/

RUN pipenv install --deploy --system

COPY ./web_service /code/

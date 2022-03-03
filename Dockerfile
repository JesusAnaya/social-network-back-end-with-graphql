FROM python:3.8-slim
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

# Install pipenv and compilation dependencies
RUN pip install pipenv
RUN apt-get update
RUN apt-get install -y --no-install-recommends gcc
RUN apt-get install -y libtiff5-dev libjpeg62-turbo-dev libopenjp2-7-dev zlib1g-dev
RUN apt-get install -y libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk
RUN apt-get install -y libharfbuzz-dev libfribidi-dev libxcb1-dev

RUN mkdir /code
WORKDIR /code

# Install python dependencies in /.venv
COPY Pipfile Pipfile.lock /code/

RUN pipenv install --deploy --system

COPY . /code/

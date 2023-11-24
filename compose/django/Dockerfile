ARG PYTHON_VERSION=3.10-slim-bullseye

# buasca a versão do python definida e nomeia como python
FROM python:${PYTHON_VERSION} as python

FROM python as python-build-stage

ARG BUILD_ENVIROMENT=requirements

RUN apt-get && apt-get 

# pega o arquivo da raiz do projeot e joga pra dentro do container
COPY ./requirements.txt .

# serve como o pip install que instala de diferentes locais
RUN pip wheel --wheel-dir /usr/src/app/wheels \ 
    -r ${BUILD_ENVIROMENT}.txt


FROM python as python-run-stage

ARG BUILD_ENVIROMENT=local
ARG APP_HOME=/home/app

ENV PYTHONNUNBUFFERED 1
env BUILD_ENV ${BUILD_ENVIROMENT}

workdir ${APP_HOME}


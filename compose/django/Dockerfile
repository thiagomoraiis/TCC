ARG PYTHON_VERSION=3.10-slim-bullseye

FROM python:${PYTHON_VERSION} as python

FROM python as python-build-stage

ARG BUILD_ENVIRONMENT=requirements

RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    git \
    libpq-dev


COPY ./requirements.txt .

RUN pip wheel --wheel-dir /usr/src/app/wheels \
    -r ${BUILD_ENVIRONMENT}.txt

FROM python as python-run-stage

ARG BUILD_ENVIRONMENT=requirements
ARG APP_HOME=/home/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWHITEBYTECODE 1
ENV BUILD_ENV ${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

RUN addgroup --system django \
    && adduser --system --ingroup django django

RUN apt-get update && apt-get install --no-install-recommends -y \
    libpq-dev \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

COPY --from=python-build=stage /usr/src/app/wheels /wheels/

RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
    && rm -rf /wheels/

RUN pip install drf_yasg


COPY --chown=django:django ./compose/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start


COPY --chown=django:django . ${APP_HOME}


RUN chown django:django ${APP_HOME}

RUN mkdir django:django ${APP_HOME}/staticfiles
RUN chown django:django ${APP_HOME}/staticfiles

WORKDIR ${APP_HOME}
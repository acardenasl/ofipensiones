# syntax=docker/dockerfile:1

FROM docker.io/library/python:3.12-slim AS webstatic

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app

COPY --from=webapp . /app

RUN uv sync --frozen --no-cache --no-dev --compile-bytecode

RUN /app/.venv/bin/python ofipensiones/manage.py collectstatic

FROM nginx:1.27

COPY nginx.conf /etc/nginx/nginx.conf

COPY --from=webstatic /static/ /staticfiles

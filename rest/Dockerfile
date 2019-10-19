FROM python:3.6.8-alpine AS base

FROM base AS builder

RUN apk add --no-cache --upgrade --virtual build-deps gcc python3-dev musl-dev libxml2-dev libxslt-dev postgresql-dev && \
    pip install -U pip pipenv && \
    rm -rf /var/cache/apk/*

WORKDIR /rest
COPY . ./
RUN pipenv install

EXPOSE 5000
CMD ["pipenv", "run", "flask", "run", "-h", "0.0.0.0"]

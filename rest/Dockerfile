FROM python:3.7.3-alpine AS base

FROM base AS builder

RUN apk add --no-cache --upgrade gcc python3-dev musl-dev libxml2-dev libxslt-dev && \
    pip install -U pip pipenv && \
    rm -rf /var/cache/apk/*

WORKDIR /wheels
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pipenv lock -r > requirements.txt && pip wheel -r requirements.txt

FROM base

WORKDIR /rest
COPY . ./
COPY --from=builder /wheels /wheels
RUN pip install -r /wheels/requirements.txt -f /wheels && \
    rm -rf /wheels && \
    rm -rf /root/.cache

EXPOSE 5000
CMD ["flask", "run"]

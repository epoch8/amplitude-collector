FROM python:3.11 AS builder

RUN mkdir /app
WORKDIR /app

RUN --mount=type=cache,target=/root/.cache pip install --upgrade pip
RUN pip install --upgrade pip poetry

COPY pyproject.toml poetry.lock ./

RUN --mount=type=cache,target=/root/.cache poetry lock --no-update
RUN poetry export --with dev -f requirements.txt --without-hashes -o requirements.txt

###############################################################################

FROM python:3.11

RUN mkdir /app
WORKDIR /app

RUN --mount=type=cache,target=/root/.cache pip install --upgrade pip

COPY --from=builder /app/requirements.txt .
RUN --mount=type=cache,target=/root/.cache pip install -r requirements.txt

COPY . /app

EXPOSE 8000

LABEL org.opencontainers.image.source https://github.com/epoch8/amplitude-collector

CMD ["uvicorn", "src.app:app", "--host=0.0.0.0", "--proxy-headers", "--workers=4"]

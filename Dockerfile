FROM python:3.9

RUN --mount=type=cache,target=/root/.cache pip install --upgrade pip

RUN mkdir /app
WORKDIR /app

COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache pip install -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["uvicorn", "src.app:app", "--host=0.0.0.0"]

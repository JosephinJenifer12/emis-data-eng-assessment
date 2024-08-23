FROM python:3.12-slim-bookworm
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

COPY ./data ./data
COPY ./src ./src

CMD python3 ./src/runner.py
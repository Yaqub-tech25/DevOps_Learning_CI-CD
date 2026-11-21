FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY Assignment-01-CI/app ./app
COPY Assignment-02-CD/main.py ./main.py

USER 10001:10001

CMD ["python", "main.py"]

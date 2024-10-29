FROM python:3.11-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh

COPY . .

EXPOSE 8000
CMD ["./wait-for-it.sh", "gifted_29_db:5432", "--", \
    "sh", "-c", "\
    docker plugin install grafana/loki-docker-driver:latest --alias loki --grant-all-permissions && \
    python manage.py migrate && \
    python manage.py csu && \
    python manage.py team_create && \
    python manage.py runserver 0.0.0.0:8000"]


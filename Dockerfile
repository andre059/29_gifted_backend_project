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
CMD ["./wait-for-it.sh", "${GIFTED_29_DB_HOST}:${GIFTED_29_DB_PORT}", "--", \
    "sh", "-c", "\
    python manage.py migrate && \
    python manage.py csu && \
    python manage.py team_create && \
    python manage.py runserver 0.0.0.0:${GIFTED_29_APP_PORT}"]

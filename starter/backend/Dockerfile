FROM python:3.10-slim

ENV FLASK_RUN_HOST=0.0.0.0

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libpcre3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY Pipfile* /app/

RUN pip install --no-cache-dir \
    flask==2.2.3 \
    flask-cors==3.0.10 \
    uwsgi==2.0.21

COPY . /app

RUN useradd -m -u 1000 app && chown -R app:app /app
USER app

CMD ["uwsgi", "--http", ":5000", "--master", "--enable-threads", "-s", "/tmp/app.sock", "--manage-script-name", "--mount", "/=app:app"]
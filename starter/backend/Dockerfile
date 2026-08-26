FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY Pipfile* /app/

RUN pip install --no-cache-dir \
    flask==2.2.3 \
    flask-cors==3.0.10 \
    werkzeug==2.2.2 \
    uwsgi==2.0.21

COPY . /app

EXPOSE 5000

CMD ["uwsgi", "--http", ":5000", "--master", "--enable-threads", "--module", "movies.movies_api:app"]
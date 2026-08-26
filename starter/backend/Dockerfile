FROM python:3.10-slim

WORKDIR /app

COPY Pipfile* /app/

RUN pip install --no-cache-dir \
    flask==2.2.3 \
    flask-cors==3.0.10 \
    uwsgi==2.0.21

COPY . /app

EXPOSE 5000

CMD ["uwsgi", "--http", ":5000", "--master", "--enable-threads", "--module", "movies.movies_api:app"]
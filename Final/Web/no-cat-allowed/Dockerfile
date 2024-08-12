FROM python:3.9-slim

RUN apt-get update && apt-get install -y nginx iputils-ping && rm -rf /var/lib/apt/lists/*

ADD /app /app

# Set permissions to read-only for the /app directory
RUN chmod -R 444 /app

RUN pip install Flask gunicorn bcrypt

USER nobody

CMD gunicorn --chdir /app app:app -b 0.0.0.0:10103

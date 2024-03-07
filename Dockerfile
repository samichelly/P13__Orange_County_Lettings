FROM python:3.11.5 as base

RUN apt-get update && apt-get install -y nginx
RUN python3 -m pip install --upgrade pip

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

# ARG SECRET_KEY="fp$9^593hsriajg$_%=5trot9g!1qa@ew(o-1#@=&4%=hp46(s"
# ENV SECRET_KEY=${SECRET_KEY}

# ARG SENTRY_DSN="https://6fe579278b0124ad6cd5b6f6027ebfa0@o4506610879954944.ingest.sentry.io/4506666483187712"
# ENV SENTRY_DSN=${SENTRY_DSN}

EXPOSE 8000

COPY nginx/conf/nginx.conf /etc/nginx/nginx.conf
COPY docker-entrypoint.sh /docker-entrypoint.sh

RUN chmod +x /docker-entrypoint.sh

CMD ["/docker-entrypoint.sh"]



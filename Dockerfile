FROM python:3.11.5 as base

RUN apt-get update && apt-get install -y nginx
RUN python3 -m pip install --upgrade pip

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

# ARG SECRET_KEY=["insert_your_SECRET_KEY"]
# ENV SECRET_KEY=${SECRET_KEY}

# ARG SENTRY_DSN=["insert_your_SENTRY_DSN"]
# ENV SENTRY_DSN=${SENTRY_DSN}

EXPOSE 8000

COPY nginx/conf/nginx.conf /etc/nginx/nginx.conf
COPY docker-entrypoint.sh /docker-entrypoint.sh

RUN chmod +x /docker-entrypoint.sh

CMD ["/docker-entrypoint.sh"]



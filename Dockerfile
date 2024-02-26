FROM python:3.11.5 as base

RUN apt-get update && apt-get install -y nginx
RUN python3 -m pip install --upgrade pip

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

COPY nginx/conf/nginx.conf /etc/nginx/nginx.conf
COPY docker-entrypoint.sh /docker-entrypoint.sh

RUN chmod +x /docker-entrypoint.sh

CMD ["/docker-entrypoint.sh"]



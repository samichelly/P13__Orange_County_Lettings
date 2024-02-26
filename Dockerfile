# Utilisation de l'image de base avec Python
FROM python:3.11.5 as base

RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# Installation de NGINX
RUN apt-get update && apt-get install -y nginx

# Installation des dépendances Python
RUN python3 -m pip install --upgrade pip

# Création d'un répertoire de travail
WORKDIR /app

# Copie du code source
COPY . .

# Installation des dépendances Python
RUN pip install -r requirements.txt
# RUN --mount=type=cache,target=/root/.cache/pip \
#     --mount=type=bind,source=requirements.txt,target=requirements.txt \
#     python -m pip install -r requirements.txt

# Exposition du port 8000 pour Gunicorn (par défaut)
EXPOSE 8000

# Configuration de NGINX pour servir les fichiers statiques et rediriger les requêtes vers Gunicorn
COPY nginx/conf/nginx.conf /etc/nginx/nginx.conf

COPY docker-entrypoint.sh /docker-entrypoint.sh

RUN chmod +x /docker-entrypoint.sh

CMD ["/docker-entrypoint.sh"]





# # syntax=docker/dockerfile:1

# # Comments are provided throughout this file to help you get started.
# # If you need more help, visit the Dockerfile reference guide at
# # https://docs.docker.com/go/dockerfile-reference/

# # Want to help us make this template better? Share your feedback here: https://forms.gle/ybq9Krt8jtBL3iCk7

# ARG PYTHON_VERSION=3.11.5
# FROM python:${PYTHON_VERSION}-slim as base

# # Prevents Python from writing pyc files.
# ENV PYTHONDONTWRITEBYTECODE=1

# # Keeps Python from buffering stdout and stderr to avoid situations where
# # the application crashes without emitting any logs due to buffering.
# ENV PYTHONUNBUFFERED=1

# WORKDIR /app

# # Create a non-privileged user that the app will run under.
# # See https://docs.docker.com/go/dockerfile-user-best-practices/
# ARG UID=10001
# RUN adduser \
#     --disabled-password \
#     --gecos "" \
#     --home "/" \
#     --shell "/sbin/nologin" \
#     --no-create-home \
#     --uid "${UID}" \
#     appuser

# # AJOUT
# RUN apt-get update && apt-get install -y nginx

# # Download dependencies as a separate step to take advantage of Docker's caching.
# # Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# # Leverage a bind mount to requirements.txt to avoid having to copy them into
# # into this layer.
# RUN --mount=type=cache,target=/root/.cache/pip \
#     --mount=type=bind,source=requirements.txt,target=requirements.txt \
#     python -m pip install -r requirements.txt

# # AJOUT
# EXPOSE 8000

# # Switch to the non-privileged user to run the application.
# USER appuser

# COPY gunicorn_config.py /app
# # COPY nginx/conf/nginx.conf /app


# # AJOUT
# COPY nginx/conf/nginx.conf /etc/nginx/nginx.conf /app


# # # AJOUT
# # # Copie du script de démarrage
# # COPY docker-entrypoint.sh /docker-entrypoint.sh


# # Copy the source code into the container.
# COPY . .

# # Expose the port that the application listens on.
# EXPOSE 8000

# # Run the application.
# CMD (gunicorn 'oc_lettings_site.wsgi' --bind=0.0.0.0:8000)


# # # AJOUT
# # # Autoriser l'exécution du script de démarrage
# # RUN chmod +x /docker-entrypoint.sh
# # # Commande par défaut pour exécuter le script de démarrage
# # CMD ["/docker-entrypoint.sh"]

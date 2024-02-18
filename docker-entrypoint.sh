#!/bin/bash

# Démarrer Gunicorn
gunicorn 'oc_lettings_site.wsgi' --bind=0.0.0.0:8000 &

# Démarrer NGINX en mode non démon
nginx -g "daemon off;"

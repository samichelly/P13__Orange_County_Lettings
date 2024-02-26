#!/bin/bash

# Run Gunicorn
gunicorn 'oc_lettings_site.wsgi' --bind=0.0.0.0:8000 &

# Run NGINX
nginx -g "daemon off;"

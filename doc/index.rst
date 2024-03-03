.. P13_OCL documentation master file, created by
   sphinx-quickstart on Tue Feb 27 16:00:39 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to P13_OCL's documentation!
===================================

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Contents:



===========
Description
===========
This project is a website to manage the activities of Orange Country Lettings.

============
Installation
============
Make sure you have Python installed on your machine.

Create and activate a virtual environment with the following commands:

For Linux and Mac :

   ``python -m venv venv``

   ``source venv/bin/activate``

   ``pip install -r requirements.txt``

For Windows :

   ``python -m venv venv``

   ``venv\Scripts\activate``

   ``pip install -r requirements.txt``

===========
Quickstart
===========

----------------
Test Environment
----------------

Create .env file to add SENTRY_DSN key and SECRET_KEY key, see the following example

   ``SENTRY_DSN=["insert_your_SENTRY_DSN"]``
   ``SECRET_KEY=["insert_your_SECRET_KEY"]``

Set ``DEBUG = True`` in settings.py

   ``python manage.py runserver``

Go to http://127.0.0.1:8000/

------------------------
Docker Local Environment
------------------------


Make sure you have the following in place before you begin deployment:

- An environment with Docker installed.
- A Docker Hub account with the necessary credentials.
  
In the Dockerfile, uncomment the following lines and insert your personnal keys

   ``# ARG SECRET_KEY=["insert_your_SECRET_KEY"]``

   ``# ENV SECRET_KEY=${SECRET_KEY}``

   ``# ARG SENTRY_DSN=["insert_your_SENTRY_DSN"]``

   ``# ENV SENTRY_DSN=${SENTRY_DSN}``


Set ``DEBUG = False`` in settings.py

   ``docker build -t [image Docker name] .``

   ``docker run -d -p 8000:8000 -p 8080:80 --name [container Docker name] [image Docker name]``

Go to http://127.0.0.1:8000/

To stop and remove container, run the following commands

   ``docker stop [container Docker name]``
   
   ``docker rm [container Docker name]``


======================================
Technologies and Programming languages
======================================
Python==3.11.5

Django==5.0.1

gunicorn==21.2.0

nginx==1.24.0

sentry-sdk==1.40.0


*Services*
   Docker

   CircleCI

   Render

   Sentry

===================
Models and Database
===================
Database : SQLite3

**Class Address**

Fields:
- number: PositiveIntegerField, representing the street number.
- street: CharField, representing the street name.
- city: CharField, representing the city name.
- state: CharField, representing the state abbreviation.
- zip_code: PositiveIntegerField, representing the ZIP code.
- country_iso_code: CharField, representing the ISO code of the country.


**Class Lettings**

Fields:

- title: CharField, representing the title of the letting.
- address: OneToOneField, representing the address associated with the letting.


**Class Profiles**

Fields:
- user: OneToOneField, representing the associated user.
- favorite_city: CharField, representing the user's favorite city.


======================
Interfaces Description
======================

**Views**

The oc_letting_site application views manage the logic for processing HTTP requests and generate the appropriate responses:

- index: The main view that displays the home page of the site.
- profile: Displays details of a user profile.
- letting: Shows the details of a rental.

To use these views, refer to the appropriate URLs.

**URLs**

- /: Corresponds to the index view.
- /profiles/: Displays the list of profiles.
- /lettings/: Displays the list of lettings.
- /profiles/<str:username>/: Corresponds to the profile view.
- /lettings/<int:letting_id>/: Corresponds to the letting view.


===========
Deployement
===========

To deploy and manage the oc_letting_site application in production, you can follow the following steps:

-------------
Prerequisites
-------------

- Set ``DEBUG = True`` in settings.py
- Give an access at your remote repository to CircleCI
- Connect CircleCI with Render with your personnal hook
- Add your environment variables (SECRET_KEY and SENTRY_DSN) in Render

-----------------------------------
Automate the pipeline with CircleCI
-----------------------------------

When you push changes to the main/master branch of your remote repository, CircleCI is configured to automatically trigger the deployment process.

In the .circleci/config.yml file, the steps are defined to create a Docker image, publish it to Docker Hub and then deploy it to the server. This process includes:

- Installation of dependencies.
- Running testing and coverage verification.
- Build and publish the Docker image if the tests pass.
- Deployement to Render

----------------------
Deployment with Render
----------------------

Deploy the last commit

When the site is live, go to https://p13-ocl-render.onrender.com


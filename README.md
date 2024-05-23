# PROJECT_13__OC_Lettings

## Project Description

Orange County Lettings is a web application designed for managing rental listings and profiles. This project provides a platform where users can view various profiles and rental locations.

## Table of Contents

- [Development Local](#development-local)
  - [Prerequisites](#prerequisites)
  - [Cloning the Repository](#cloning-the-repository)
  - [Creating the Virtual Environment](#creating-the-virtual-environment)
  - [Running the Site](#running-the-site)
  - [Linting](#linting)
  - [Unit Tests](#unit-tests)
  - [Database](#database)
  - [Admin Panel](#admin-panel)

## Development Local

### Prerequisites

- GitHub account with read access to this repository
- Git CLI
- SQLite3 CLI
- Python interpreter, version 3.6 or higher

In the rest of the local development documentation, it is assumed that the `python` command in your OS shell runs the above Python interpreter (unless a virtual environment is activated).

### Cloning the Repository

- Navigate to the desired directory:
  ```bash
  cd /path/to/put/project/in
  ```
- Clone the repository:
  ```bash
  git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git
  ```

### Creating the Virtual Environment

- Navigate to the project directory:
  ```bash
  cd /path/to/Python-OC-Lettings-FR
  ```
- Create a virtual environment:
  ```bash
  python -m venv venv
  ```
- (If the previous step gives errors about a missing package on Ubuntu, run:)
  ```bash
  apt-get install python3-venv
  ```
- Activate the virtual environment:
  ```bash
  source venv/bin/activate
  ```
- Confirm that the `python` command runs the Python interpreter in the virtual environment:
  ```bash
  which python
  ```
- Confirm that the Python interpreter version is 3.6 or higher:
  ```bash
  python --version
  ```
- Confirm that the `pip` command runs the pip executable in the virtual environment:
  ```bash
  which pip
  ```
- To deactivate the virtual environment, run:
  ```bash
  deactivate
  ```

### Running the Site

- Navigate to the project directory:
  ```bash
  cd /path/to/Python-OC-Lettings-FR
  ```
- Activate the virtual environment:
  ```bash
  source venv/bin/activate
  ```
- Install the required packages:
  ```bash
  pip install --requirement requirements.txt
  ```
- Run the Django development server:
  ```bash
  python manage.py runserver
  ```
- Open `http://localhost:8000` in a browser.
- Confirm that the site works and you can navigate (you should see several profiles and locations).

### Linting

- Navigate to the project directory:
  ```bash
  cd /path/to/Python-OC-Lettings-FR
  ```
- Activate the virtual environment:
  ```bash
  source venv/bin/activate
  ```
- Run flake8:
  ```bash
  flake8
  ```

### Unit Tests

- Navigate to the project directory:
  ```bash
  cd /path/to/Python-OC-Lettings-FR
  ```
- Activate the virtual environment:
  ```bash
  source venv/bin/activate
  ```
- Run pytest:
  ```bash
  pytest
  ```

### Database

- Navigate to the project directory:
  ```bash
  cd /path/to/Python-OC-Lettings-FR
  ```
- Open a SQLite3 shell:
  ```bash
  sqlite3
  ```
- Connect to the database:
  ```sqlite
  .open oc-lettings-site.sqlite3
  ```
- List the tables in the database:
  ```sqlite
  .tables
  ```
- Show the columns in the profiles table:
  ```sqlite
  pragma table_info(Python-OC-Lettings-FR_profile);
  ```
- Query the profiles table:
  ```sqlite
  select user_id, favorite_city from Python-OC-Lettings-FR_profile where favorite_city like 'B%';
  ```
- Quit SQLite3:
  ```sqlite
  .quit
  ```

### Admin Panel

- Open `http://localhost:8000/admin` in a browser.
- Log in with the following credentials:
  - Username: `admin`
  - Password: `Abc1234!`

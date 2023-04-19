#!/bin/bash

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
flask --app flaskr init-db
pip install -e .
pip list
flask --app flaskr run --debug

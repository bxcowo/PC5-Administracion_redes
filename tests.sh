#!/bin/bash
docker-compose up --build -d

# Setup Python environment
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt

# See tests results
docker logs tests

./clean.sh

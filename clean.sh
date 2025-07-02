#!/bin/bash

docker-compose down -v
rm -rf .venv
find . -type d -name "__pycache__" -exec rm -rf {} +

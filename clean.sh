#!/bin/bash

docker-compose down -v --remove-orphans
rm -rf .venv
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -type d -name ".pytest_cache" -exec rm -rf {} +
find . -type f -name ".coverage" -exec rm -rf {} +

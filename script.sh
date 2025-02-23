#!/usr/bin/env bash

docker compose build
docker rollout -f docker-compose.yml flask_app
docker compose restart nginx
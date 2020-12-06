#!/bin/bash
docker-compose -f /home/ubuntu/backend-arqui/docker-compose.production.yml build
docker-compose -f /home/ubuntu/backend-arqui/docker-compose.production.yml up -d
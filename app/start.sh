#!/bin/bash
docker-compose -f /home/ubuntu/backend-arqui/docker-compose.prod.yml build
docker-compose -f /home/ubuntu/backend-arqui/docker-compose.prod.yml up -d
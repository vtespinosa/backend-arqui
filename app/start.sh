#!/bin/bash
docker-compose -f /home/ubuntu/we-chat/docker-compose.production.yml build
docker-compose -f /home/ubuntu/we-chat/docker-compose.production.yml up -d
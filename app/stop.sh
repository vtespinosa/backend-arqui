#!/bin/bash
docker-compose -f /home/ubuntu/we-chat/docker-compose.production.yml down
docker stop $(docker ps -a -q)
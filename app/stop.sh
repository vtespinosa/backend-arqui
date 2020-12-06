#!/bin/bash
docker-compose -f /home/ubuntu/backend-arqui/docker-compose.production.yml down
docker stop $(docker ps -a -q)
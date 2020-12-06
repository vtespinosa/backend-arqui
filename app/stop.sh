#!/bin/bash
docker-compose -f /home/ubuntu/backend-arqui/docker-compose.prod.yml down
docker stop $(docker ps -a -q)
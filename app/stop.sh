#!/bin/bash
sudo docker-compose -f /home/ubuntu/backend-arqui/docker-compose.prod.yml down
# sudo docker stop $(docker ps -a -q)
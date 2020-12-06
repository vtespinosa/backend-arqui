#!/bin/bash
sudo docker-compose -f /home/ubuntu/backend-arqui/docker-compose.prod.yml build
sudo docker-compose -f /home/ubuntu/backend-arqui/docker-compose.prod.yml up -d
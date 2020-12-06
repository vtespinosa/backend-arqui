#!/bin/bash
pwd=$( aws ecr get-login-password )
sudo docker container stop $(docker container ls -aq)
sudo docker login -u AWS -p $pwd https://066234982609.dkr.ecr.us-east-1.amazonaws.com/we-chat
sudo docker pull 066234982609.dkr.ecr.us-east-1.amazonaws.com/we-chat
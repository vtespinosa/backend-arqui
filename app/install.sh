#!/bin/bash
pwd=$( aws ecr get-login-password )
docker container stop $(docker container ls -aq)
docker login -u AWS -p $pwd https://066234982609.dkr.ecr.us-east-1.amazonaws.com/we-chat
docker pull 066234982609.dkr.ecr.us-east-1.amazonaws.com/we-chat
#!/bin/bash

# For Macbook M1 --platform linux/amd64
export DOCKER_DEFAULT_PLATFORM=linux/amd64

# Setup env variables
if [ ! -f ".env" ]; then
    cp .env.sample .env
    echo "Create new .env file from .env.sample"
fi



# Build and run containers
docker-compose down --remove-orphans

docker-compose --env-file .env up mariadb -d --build --remove-orphans 

# WAIT for DB: Start!
(
   while ! docker exec mariadb mysqladmin --user=root --password=password --host "127.0.0.1" ping --silent &> /dev/null ; do 
   echo "Waiting for db..."; sleep 5; done; echo "=== DB wait done! ===";
)
# WAIT for DB: Done!

docker-compose --env-file .env up api -d --build --remove-orphans

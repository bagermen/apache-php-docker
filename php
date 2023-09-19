#!/bin/sh
docker exec -it $(docker ps -f name=apachephp_phpserver --quiet) php $@
# Docker: PHP + Apache stack
This repository consists of configuration of PHP and Apache ready for development usage

## How to start
* Install Docker
* Init swarm mode

    `docker swarm init`

* Copy **.env.dist** to **.env** and change variables to your needs
* Use **deploy.py** to start and stop stack

## Variables list
|Variable|Descriptin|
-|-
XDEBUG_CONFIG|xdebug configuration
HOST_PORT|localhost port at which site is be available at
HOST_PROJECT_DIR|Path to your web project

## Todo
add memcached, mysql, postgresql set up
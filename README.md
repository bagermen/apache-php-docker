#  LAMP stack built with Docker Swarm

![Landing Page](https://i.ibb.co/yQqfn3f/Screenshot-1.png)


A basic LAMP stack environment built witth Docker Swarm. It consists of following libraries:

* PHP
* Memcached
* Apache
* MySQL

##  Installation

* Clone this repository into your computer
* Init swarm mode `docker swarm init`
* Copy **.env.dist** to **.env** and change variables to suit your needs
* Use **deploy.py** to start and stop the stack (use -h for help)

```shell
git clone https://github.com/bagermen/apache-php-docker.git
cd apache-php-docker/
cp .env.dist .env
// modify .env as needed
python deploy.py
// visit localhost
```

Your LAMP stack is ready now. You can access it via `http://localhost:8080`.
> Note. Port is defined with `HOST_PORT` variable at `.env` file

##  Configuration and Usage

### General Information
This Docker Stack is build for local development and not for production usage.

### Configuration
This package comes with default configuration options. You can modify them by creating `.env` file in your root directory.
To make it easy, just copy the content from `.env.dist` file and update the environment variable values as per your need.

### Configuration Variables
There are following configuration variables available and you can customize them by overwritting `.env` file.

|Variable|Descriptin|
-|-
HOST_PORT|Host port at which the stack is available at
HOST_PROJECT_DIR|Path to your project
DOCUMENTROOT|Apache DOCUMENTROOT
PHP_IMAGE|PHP image to be used in the stack
MY_IMAGE|MySQL image to be used in the stack
APACHE_CONF|Path to `httpd.conf`
PHP_INI|Path to `php.ini`
PHP_FPM|Path to `php-fpm.conf`
MY_CNF|Path to `my.cnf`
MY_CFG|Path to `root_password`
XDEBUG_CONFIG|Xdebug configuration
DATABASE|Default database name
DATABASE_USER|Default database user
DATABASE_PASSWORD|Default database user password
DATABASE_PORT|Host port at which database is abailable at

### XDebug Notes
Default xdebug port is __9001__. You can change it in XDEBUG_CONFIG variable.

Note that Docker can connect to the port at following IP addesses __only__:

- 127.0.0.1 (IPv4)
- '' (IPv6)

VSCode could have following configuration in _launch.json_
```json
{
    "name": "Start Xdebug",
    "type": "php",
    "request": "launch",
    "port": 9001,
    "hostname": "::",
    "pathMappings": {
        "/var/www/html": "${workspaceRoot}/htdocs"
    }
}
```

If you intend debugging code from WSL2 (Windows Subsystem for Linux), you have to do remote port forwarding from WSL to Windows host.
VSCode configuration is following in _launch.json_
```json
{
    "name": "WSL Xdebug",
    "type": "php",
    "request": "launch",
    "port": 9001,
    "hostname": "::",
    "preLaunchTask": "WSL - Xdebug Start",
    "postDebugTask": "WSL - Xdebug Stop",
    "pathMappings": {
        "/var/www/html": "${workspaceRoot}/htdocs"
    }
}
```

Corresponding tasks configuration in _tasks.json_
```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "WSL - Xdebug Start",
            "type": "shell",
            "command": "sshpass -p \"PASSWORD\" ssh -f -N -M -S /tmp/ssh-xdebug -R 9001:localhost:9001 USER@host.docker.internal"
        },
        {
            "label": "WSL - Xdebug Stop",
            "type": "shell",
            "command": "ssh -S /tmp/ssh-xdebug -O exit USER@host.docker.internal"
        }
    ]
}
```
where

- __USER__ is the active Windows User
- __PASSWORD__ is the User's Password

Read article ["Step Debugging"](https://xdebug.org/docs/step_debug) for more details
## PHP

### [PHP Images](https://hub.docker.com/repository/docker/besogon1/php)
* besogon1/php:8.1.9-fpm-alpine-ext
* besogon1/php:8-fpm-alpine-ext
* besogon1/php:7-fpm-alpine-ext

#### Extensions

* mysqli
* pdo_mysql
* pdo_pgsql
* memcached
* igbinary
* intl
* zip
* soap
* sodium
* gd
* xdebug

> Note. If you want to install more extensions, you have to create custom PHP image and use it instead of provided ones.


## Contributing
We are happy if you want to create a pull request or help people with their issues. If you want to create a PR, please remember that this stack is not built for production usage, and changes should good for general purpose and not overspecialized.

Thank you!

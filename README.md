#  LAMP stack built with Docker Swarm

![Landing Page](https://i.ibb.co/yQqfn3f/Screenshot-1.png)


A basic LAMP stack environment built using Docker Swarm. It consists of the following:

* PHP
* Memcached
* Apache
* MySQL

##  Installation

* Clone this repository on your local computer
* Init swarm mode `docker swarm init`
* Copy **.env.dist** to **.env** and change variables to your needs
* Use **deploy.py** to start and stop stack (use -h for help)

```shell
git clone https://github.com/bagermen/apache-php-docker.git
cd apache-php-docker/
cp .env.dist .env
// modify .env as needed
python deploy.py
// visit localhost
```

Your LAMP stack is now ready. You can access it via `http://localhost:8080`.
> Note. Port is defined with `HOST_PORT` variable at `.env` file

##  Configuration and Usage

### General Information
This Docker Stack is build for local development and not for production usage.

### Configuration
This package comes with default configuration options. You can modify them by creating `.env` file in your root directory.
To make it easy, just copy the content from `.env.dist` file and update the environment variable values as per your need.

### Configuration Variables
There are following configuration variables available and you can customize them by overwritting in your own `.env` file.

|Variable|Descriptin|
-|-
HOST_PORT|Host port at which the stack is available at
HOST_PROJECT_DIR|Path to your project
APACHE_CONF|Path to `httpd.conf`
PHP_INI|Path to `php.ini`
PHP_FPM|Path to `php-fpm.conf`
MY_CNF|Path to `my.cnf`
XDEBUG_CONFIG|Xdebug configuration
XDEBUG_PORT|Host port at which Xdebug is available at
DATABASE|Default database name
DATABASE_USER|Default database user
DATABASE_PASSWORD|Default database user password
DATABASE_PORT|Host port at which database is abailable at


## PHP

#### Extensions

By default following extensions are installed.
* ctype
* curl
* date
* dom
* fileinfo
* filter
* ftp
* gd
* hash
* iconv
* igbinary
* intl
* json
* libxml
* mbstring
* mcrypt
* memcached
* mysqli
* mysqlnd
* openssl
* pcre
* PDO
* pdo_mysql
* pdo_pgsql
* pdo_sqlite
* Phar
* posix
* readline
* Reflection
* session
* SimpleXML
* soap
* sodium
* SPL
* sqlite3
* standard
* tokenizer
* xdebug
* xml
* xmlreader
* xmlwriter
* zip
* zlib

> Note. If you want to install more extensions, you have to create custom PHP image and use it instead of provided one.


## Contributing
We are happy if you want to create a pull request or help people with their issues. If you want to create a PR, please remember that this stack is not built for production usage, and changes should good for general purpose and not overspecialized.

Thank you!

FROM php:7-fpm-alpine

ARG TIMEZONE=Europe/Moscow

# Install additional packages
RUN set -ex \
    && apk --no-cache add \
    postgresql-dev \
    tzdata \
    autoconf \
    gcc \
    g++ \
    make

# Set timezone
RUN ln -snf /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && echo ${TIMEZONE} > /etc/timezone \
    && printf '[PHP]\ndate.timezone = "%s"\n', ${TIMEZONE} > ${PHP_INI_DIR}/conf.d/tzone.ini


# Install mysql support
RUN docker-php-ext-install pdo_mysql

# Install postgresql support
RUN docker-php-ext-install pdo_pgsql

# Install xdebug
RUN pecl install xdebug \
    && docker-php-ext-enable xdebug \
    && echo "xdebug.remote_port=9001" >> ${PHP_INI_DIR}/conf.d/docker-php-ext-xdebug.ini

# Copy pool configuration
COPY conf/php-fpm.conf "/usr/local/etc/php-fpm.conf"

# Copy development configuration
COPY conf/php.ini "${PHP_INI_DIR}/php.ini"

EXPOSE 9001
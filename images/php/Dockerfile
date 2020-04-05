
FROM php:7-fpm-alpine

ARG TIMEZONE=Europe/Moscow

# Install additional packages
RUN set -ex \
    && apk --update --no-cache add \
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


# Install PHP Extensions: igbinary & memcached
# @see https://stackoverflow.com/questions/40894385/how-can-i-install-the-php-memcached-extension-on-dockers-php7-alpine-image
RUN apk add --no-cache --update libmemcached-libs zlib
RUN set -xe && \
    cd /tmp/ && \
    apk add --no-cache --update --virtual .phpize-deps $PHPIZE_DEPS && \
    apk add --no-cache --update --virtual .memcached-deps zlib-dev libmemcached-dev cyrus-sasl-dev && \
# Install igbinary (memcached's deps)
    pecl install igbinary && \
# Install memcached
    ( \
        pecl install --nobuild memcached && \
        cd "$(pecl config-get temp_dir)/memcached" && \
        phpize && \
        ./configure --enable-memcached-igbinary && \
        make -j$(nproc) && \
        make install && \
        cd /tmp/ \
    ) && \
# Enable PHP extensions
    docker-php-ext-enable igbinary memcached && \
    rm -rf /tmp/* && \
    apk del .memcached-deps .phpize-deps

# Copy pool configuration (not required at swarm mode)
# COPY conf/php-fpm.conf "/usr/local/etc/php-fpm.conf"

# Copy development configuration (not required at swarm mode)
# COPY conf/php.ini "${PHP_INI_DIR}/php.ini"

EXPOSE 9001
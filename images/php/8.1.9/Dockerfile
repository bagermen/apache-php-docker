
FROM php:8.1.9-fpm-alpine

ARG TIMEZONE=Europe/Moscow

# Install additional packages
RUN set -ex \
    && apk add --update --no-cache \
    tzdata

# Set timezone
RUN ln -snf /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && echo ${TIMEZONE} > /etc/timezone \
    && printf '[PHP]\ndate.timezone = "%s"\n', ${TIMEZONE} > ${PHP_INI_DIR}/conf.d/tzone.ini

# gd, libsodium, intl, zip, soap, postgresql, mysql, mysqli support
RUN apk add --update --no-cache \
        libpq \
        libsodium freetype libjpeg-turbo libpng \
        libintl icu-libs zip libzip libxml2 && \
    apk add --no-cache --update --virtual .db postgresql-dev && \
    apk add --update --no-cache --virtual .gd_libsodium libsodium-dev freetype-dev libjpeg-turbo-dev libpng-dev && \
    apk add --no-cache --update --virtual .intl_zip_soap icu-dev libzip-dev libxml2-dev && \
    docker-php-ext-configure gd --with-freetype=/usr/include/ --with-jpeg=/usr/include/ && \
    docker-php-ext-install -j"$(nproc)" gd intl zip soap pdo pdo_pgsql pdo_mysql mysqli bcmath opcache && \
    apk del .gd_libsodium && \
    apk del .intl_zip_soap && \
    apk del .db

# Install xdebug, memcached, igbinary
RUN set -xe && \
    apk add --no-cache --update --virtual .phpize-deps $PHPIZE_DEPS && \
    # Install xdebug
    apk add --no-cache --update --virtual .xdebug-deps linux-headers && \
    pecl install xdebug && \
    docker-php-ext-enable xdebug && \
    echo "xdebug.client_host=host.docker.internal" >> ${PHP_INI_DIR}/conf.d/docker-php-ext-xdebug.ini && \
    echo "xdebug.mode=develop,debug" >> ${PHP_INI_DIR}/conf.d/docker-php-ext-xdebug.ini && \
    apk del .xdebug-deps && \
# Install PHP Extensions: igbinary & memcached
# @see https://stackoverflow.com/questions/40894385/how-can-i-install-the-php-memcached-extension-on-dockers-php7-alpine-image
    cd /tmp/ && \
    apk add --no-cache --update libmemcached-libs zlib libsasl && \
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
    # Install redis
    ( \
        pecl install --nobuild redis && \
        cd "$(pecl config-get temp_dir)/redis" && \
        phpize && \
        ./configure --enable-redis-igbinary && \
        make -j$(nproc) && \
        make install && \
        cd /tmp/ \
    ) && \
    # Enable PHP extensions
    docker-php-ext-enable igbinary memcached redis && \
    rm -rf /tmp/* && \
    apk del .memcached-deps .phpize-deps
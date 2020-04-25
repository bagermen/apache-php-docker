<?php
// Test Memcached service
$memcached = new Memcached('my_pool');
$memcached->addServer('memcached', 11211);
$memcached->setOption(Memcached::OPT_SERIALIZER, Memcached::SERIALIZER_IGBINARY);

$memcached->set('saved_str', 'Memcached works');

echo $memcached->get('saved_str');
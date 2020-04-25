<?php
// Test MySQL connection
$dsn = 'mysql:dbname=database;host=database';
$user = 'root';
$password = 'mW9PjVrNWIP0U7VTkBOvM2BFFr8=';

try {
    $dbh = new PDO($dsn, $user, $password);
    echo 'MySQL connection is successful';
} catch (PDOException $e) {
    echo 'Can\'t connect to the database: ' . $e->getMessage();
}
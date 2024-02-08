<?php
// Test PostgreSQL connection
$dsn = 'pgsql:dbname=postgres;host=postgres_database;port=5432';
$user = 'postgres';
$password = 'mW9PjVrNWIP0U7VTkBOvM2BFFr8=';

try {
    $dbh = new PDO($dsn, $user, $password);
    $res = $dbh->query("SELECT version();");

    if ($res) {
        echo "PostgreSQL version: {$res->fetchColumn()}";
    }
} catch (PDOException $e) {
    echo 'Can\'t connect to the database: ' . $e->getMessage();
}
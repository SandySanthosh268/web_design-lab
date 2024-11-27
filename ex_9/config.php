<?php
$host = 'localhost';
$db = 'todo_db';
$user = 'root'; // Default username
$pass = 'sandy@268';     // Default password for XAMPP

try {
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}
?>

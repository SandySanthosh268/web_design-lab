<?php
// db.php
$host = "localhost";
$user = "root"; // Change if using a different username
$password = "sandy@268"; // Change if you have set a password
$database = "user_auth_db";

$conn = new mysqli($host, $user, $password, $database);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>

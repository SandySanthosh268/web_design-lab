<?php
include 'session.php';

if (!isset($_SESSION['user_id'])) {
    header("Location: login.php");
    exit;
}

echo "<h1>Welcome, " . $_SESSION['username'] . "!</h1>";
echo "<a href='logout.php'>Logout</a>";
?>

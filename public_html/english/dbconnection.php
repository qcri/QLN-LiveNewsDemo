<?php
$servername = "localhost";
$username = "demouser1";
$password = "76wxaGNUlaOT7fl2";
$dbname = "reactapp";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
$conn->set_charset('utf8mb4');       // object oriented style
mysqli_set_charset($conn, 'utf8mb4');  // procedural style

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
?>

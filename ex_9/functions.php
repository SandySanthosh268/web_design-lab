<?php
require 'config.php';

// Create a new task
function createTask($task) {
    global $pdo;
    $stmt = $pdo->prepare("INSERT INTO todos (task) VALUES (:task)");
    $stmt->execute(['task' => $task]);
}

// Read all tasks
function getTasks() {
    global $pdo;
    $stmt = $pdo->query("SELECT * FROM todos ORDER BY created_at DESC");
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

// Update task status
function updateTask($id, $status) {
    global $pdo;
    $stmt = $pdo->prepare("UPDATE todos SET status = :status WHERE id = :id");
    $stmt->execute(['status' => $status, 'id' => $id]);
}

// Delete a task
function deleteTask($id) {
    global $pdo;
    $stmt = $pdo->prepare("DELETE FROM todos WHERE id = :id");
    $stmt->execute(['id' => $id]);
}
?>

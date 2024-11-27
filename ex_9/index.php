<?php
require 'functions.php';

// Handle Create
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['task'])) {
    createTask($_POST['task']);
    header('Location: index.php');
    exit;
}

// Handle Update
if (isset($_GET['update'])) {
    updateTask($_GET['id'], $_GET['status']);
    header('Location: index.php');
    exit;
}

// Handle Delete
if (isset($_GET['delete'])) {
    deleteTask($_GET['id']);
    header('Location: index.php');
    exit;
}

// Fetch Tasks
$tasks = getTasks();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>To-Do List</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: center; }
        th { background-color: #f4f4f4; }
        form { margin-bottom: 20px; }
    </style>
</head>
<body>
    <h1>To-Do List</h1>
    <form method="POST">
        <input type="text" name="task" placeholder="Enter new task" required>
        <button type="submit">Add Task</button>
    </form>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Task</th>
                <th>Status</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($tasks as $task): ?>
                <tr>
                    <td><?= $task['id'] ?></td>
                    <td><?= htmlspecialchars($task['task']) ?></td>
                    <td><?= $task['status'] ?></td>
                    <td>
                        <a href="?update&id=<?= $task['id'] ?>&status=completed">Mark Completed</a> |
                        <a href="?delete&id=<?= $task['id'] ?>">Delete</a>
                    </td>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
</body>
</html>

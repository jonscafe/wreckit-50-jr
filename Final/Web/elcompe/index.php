<?php
ini_set("error_reporting", 1);
include "flag.php";

$message = "";
$messageColor = "";

if (isset($_GET['source'])) {
    highlight_file(__FILE__);
    exit();
}

if (isset($_GET['inputsecret'])) {
    $sec = $_GET['inputsecret'];

    if (preg_match('/^[1-9]\d*e[+-]?\d+$/i', $sec)) {
        $message = "Correct! Here's your flag: $flag";
        $messageColor = "green";
    } elseif ($sec == '0' || $sec == '0.0' || strtolower($sec) == '0e0') {
        $message = "not that ez you f00l";
        $messageColor = "red";
    } else {
        $message = "Incorrect secret.";
        $messageColor = "red";
    }
}
?>

<html>
<head>
    <title>el Compe</title>
    <style>
        body {
            background-color: #282c34;
            color: #61dafb;
            font-family: 'Palatino Linotype', 'Book Antiqua', Palatino, serif;
            text-align: center;
            padding: 50px;
        }
        h1 {
            font-size: 3em;
            margin-bottom: 0.5em;
        }
        form {
            background: #20232a;
            padding: 20px;
            border-radius: 10px;
            display: inline-block;
        }
        label {
            font-size: 1.5em;
        }
        input[type="text"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            font-size: 1.2em;
        }
        input[type="submit"] {
            background: #61dafb;
            border: none;
            padding: 10px 20px;
            font-size: 1.2em;
            color: #20232a;
            cursor: pointer;
            border-radius: 5px;
        }
        input[type="submit"]:hover {
            background: #21a1f1;
        }
        p {
            font-size: 1.2em;
        }
        .message {
            font-size: 1.5em;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h1>welcome to el compe's hideout</h1>
    <form method="GET" action="">
        <label for="inputsecret">enter the secret:</label><br>
        <input type="text" id="inputsecret" name="inputsecret"><br><br>
        <input type="submit" value="Submit">
    </form>
    <p>Hint: View the source code.</p>
    <p>Hint: All zeros are equals</p>
    <?php if (!empty($message)): ?>
        <p class="message" style="color: <?= $messageColor ?>;"><?= $message ?></p>
    <?php endif; ?>
</body>
</html>

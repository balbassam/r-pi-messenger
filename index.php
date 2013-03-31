<!--Allow the page to render on a cellphone-->
<meta name="HandheldFriendly" content="true" />
<meta name="viewport" content="width=device-width, height=device-height, user-scalable=no" />

<html>
<head>
<!--Fill the width of the page-->
<style type="text/css">
.inputArea {width:100%;}
</style>
</head>
<!--BEGIN of rendered data-->
<body>
<!--Form which posts data to the same page-->
<form action="." method="POST">
<!--input box for the question-->
<textarea class="inputArea" rows="10" autofocus style="resize:none" name="question"></textarea><br>
<!--submit button-->
<input class="inputArea" type="submit" class="commentarea" value="Submit question"/>
</form>

<?php
//BEGIN of PHP code
    // Was there data passed in?
    if (isset($_POST["question"]) && !empty($_POST["question"]) ) {

        // Grab data that was passed in
        $data = $_POST["question"];

        // Display that data in its own paragraph
        echo "Your question was<p>";
        echo "<font color='green'>" . htmlspecialchars($data) . "</font></p>";
        
        // Open messages file to append to.
        $file = fopen("Messages.txt", "a");

        // Strip all non-printable characters from data before writing to file
        $data = preg_replace('/[^[:print:]]/', '', $data);

        // Append the data in its own line then close the file
        fwrite($file, $data . "\n");
        fclose($file);

        // Make the LCD blink if it wasn't already blinking
        if (!exec("ps aux | grep blinkServer.py | grep -v grep")) {
            exec('sudo /home/pi/Server/blinkServer.py > /dev/null &');
        }
        
        // If the program to display messages isn't running then make it run
        if (!exec("ps aux | grep server.py | grep -v grep")) {
            exec('sudo /home/pi/Server/server.py > /dev/null &');
        }
    }
    // If there wasn't any data passed in
    else {
        // Then ask the user to enter a question
        echo "Please enter a question in the box above";
    }
// END of PHP code
?>
</body>
<!--END of rendered data-->
</html>

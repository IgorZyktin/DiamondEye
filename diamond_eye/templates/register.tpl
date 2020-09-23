<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link type="text/css" href="/static/styles.css" rel="stylesheet">
    <script src="/static/scripts.js"></script>
    <title>{{ title }}</title>
</head>
<body>

<div class="wrapper">
    <div class="register">
        <form method="post">
            <p>What is your name?</p>
            % if error:
                <div class="error"><p>{{error}}</p></div>
            %end
            <input id="user_name" type="text" name="user_name"
                   maxlength="128"/>
            <p>This is required, but used only to count statistics.
                Type random gibberish if you don't care.</p>
            <input type="submit" class="btn active w-100"/>
        </form>
    </div>
</div>
</body>
</html>




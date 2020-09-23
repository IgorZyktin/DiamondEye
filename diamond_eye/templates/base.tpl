<!DOCTYPE html>
<!--suppress HtmlUnknownTarget -->
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link type="text/css" href="/static/styles.css" rel="stylesheet">
    <script src="/static/scripts.js"></script>
    <title>{{ title }}</title>
</head>
<body>

<div class="header_base">
    <div><a href="/index" class="btn">User name: {{ user_name }}</a></div>
    <div><a href="/index" class="btn">Version: {{ version }}</a></div>
    <div>
        <a href="#" id="save_btn"
           class="btn{{' not_saved' if not_saved else ''}} active"
           onclick="saveState()">Save state
        </a>
    </div>
    <div>
        <a href="#" class="btn active" onclick="refreshState()">Refresh state</a>
    </div>
    <div>
        <a href="/upload" class="btn active">Upload images</a>
    </div>

    <div>
        <a href="mailto:nicord@yandex.ru" class="btn active">Mail me</a>
    </div>
</div>

<hr>

<div class="header_query">
    <div>
        <label for="query"></label><input id="query" type="search">
    </div>

    <div>
        <label for="images_at_once"></label><select id="images_at_once">
            <option {{ 'selected' if at_once == '10' else '' }} value="10">10 per page</option>
            <option {{ 'selected' if at_once == '20' else '' }} value="20">20 per page</option>
            <option {{ 'selected' if at_once == '50' else '' }} value="50">50 per page</option>
            <option {{ 'selected' if at_once == '100' else '' }} value="100">100 per page</option>
            <option {{ 'selected' if at_once == '150' else '' }} value="150">150 per page</option>
        </select>
    </div>

    <div>
        <a href="#" class="btn active" onclick="goSearch()">Search</a>
    </div>
</div>

<hr>

<div class="content">
    {{!base}}
</div>

</body>
</html>
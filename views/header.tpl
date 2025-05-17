%import datetime
<!-- Copyright (C) {{datetime.datetime.now().year}} {{module.band_name}} //-->

<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <link rel="shortcut icon" href="/content/shortcut-icon.png" type="image/x-icon">
    <link rel="apple-touch-icon" href="/content/apple-touch-icon.png">

%for sheet in ['normalize', 'layout', 'navigation', module_name]:
    <link rel="stylesheet" type="text/css" href="/static/{{sheet}}.css">
%end

    <script src="https://code.jquery.com/jquery-3.6.3.slim.min.js"></script>
%for script in ['collapse', 'expire', 'main', 'embed-cookie-banner/embed-handler']:
    <script src="/static/{{script}}.js"></script>
%end

%title = [module.band_name.upper()]
%if module_name in ['feed', 'impressum', 'contact']:
    %title.append(module.genre)
%else:
    %title.append(module.base_title)
%end
%title.append('Official Homepage')
%title = ' - '.join(title)
    <title>{{title}}</title>
%url = '' if module_name == 'feed' else module_name
%url = 'imprint' if module_name == 'impressum' else module_name
%if url == 'feed':
    <link rel="canonical" href="https://www.{{module.domain}}">
    <meta property="og:url" content="https://www.{{module.domain}}">
%else:
    <link rel="canonical" href="https://www.{{module.domain}}/{{url}}">
    <meta property="og:url" content="https://www.{{module.domain}}/{{url}}">
%end
    <meta name="title" content="{{module.title}}">
    <meta name="description" content="{{module.description[module_name]}}">
    <meta name="keywords" content="{{', '.join(module.keywords)}}"> <!-- but google ignores this anyway //-->
    <meta name="robots" content="index,follow">
    <meta property="og:title" content="{{module.title}}">
    <meta property="og:image" content="/content/logo_inverted.png">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="{{module.title}}">
    <meta property="og:description" content="{{module.description[module_name]}}">
    <meta name="HandheldFriendly" content="true">
    <meta name="format-detection" content="telephone=yes">
</head>

<body>
%include('navigation')

    <div id="content">

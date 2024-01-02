%import datetime
<!-- Copyright (C) {{datetime.datetime.now().year}} {{module.band_name}} //-->

<!DOCTYPE html>
<html lang="de" style="background-image: url('{{module.server.path.get_static_url('/content/background.jpg')}}');">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="shortcut icon" href="{{module.server.path.get_static_url('/content/shortcut-icon.png')}}" type="image/x-icon">
    <link rel="apple-touch-icon" href="{{module.server.path.get_static_url('/content/apple-touch-icon.png')}}">

%for css in ['normalize', 'layout', 'navigation', module_name]:
    %url = module.server.path.get_static_url('/' + css + '.css')
    <link rel="stylesheet" type="text/css" href="{{url}}">
%end

    <script src="https://code.jquery.com/jquery-3.6.3.slim.min.js"></script>
    <script src="{{module.server.path.get_static_url('/collapse.js')}}"></script>

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
    <link rel="canonical" href="https://www.{{module.domain}}/{{url}}">
    <meta name="title" content="{{module.title}}">
    <meta name="description" content="{{module.description}}">
    <meta name="keywords" content="{{', '.join(module.keywords)}}"> <!-- but google ignores this anyway //-->
    <meta name="robots" content="index,follow">
    <meta property="og:title" content="{{module.title}}">
    <meta property="og:site_name" content="{{module.title}}">
    <meta property="og:description" content="{{module.description}}">
    <meta property="og:url" content="https://www.{{module.domain}}">
    <meta name="HandheldFriendly" content="true">
    <meta name="format-detection" content="telephone=yes">
</head>

<body>
%include('navigation')

    <div id="content">

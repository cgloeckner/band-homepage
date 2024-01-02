%include('header', module_name='feed')

<img class="title" alt="{{module.band_name}} Foto" src="{{module.server.path.get_static_url('/content/titles/feed.jpg')}}">

<div class="feed">

    <img class="large-logo" alt="{{module.band_name}}" src="{{module.server.path.get_static_url('/content/logo_inverted.png')}}">

    <h1>{{module.title}}</h1>

    <div class="elements">

%for key, value in module.data.items():
    %if module.data[key]['type'] == 'youtube':
        %include('feed/youtube', data=value)
    %end
%end
    </div>

</div>

%include('footer')
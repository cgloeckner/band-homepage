%include('header', module_name='feed')

<img class="title" alt="{{module.band_name}} Foto" src="{{get_static_url('/content/titles/feed.jpg')}}">

<div class="feed">

    <img class="large-logo" alt="{{module.band_name}}" src="{{get_static_url('/content/logo_inverted.png')}}">

    <h1>{{module.title}}</h1>

    <div class="elements">

%for key in data:
    %if data[key]['type'] == 'youtube':
        %include('feed/youtube', data=data[key])
    %end
%end
    </div>

</div>

%include('footer')
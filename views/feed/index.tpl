%include('header', module_name='feed')

<img class="title" alt="{{module.band_name}} Foto" src="/content/titles/feed.jpg">

<div class="feed">

    <img class="large-logo" alt="{{module.band_name}}" src="/content/logo_inverted.png">

    <h1>{{module.title}}</h1>

    <div class="reviews center">
%for source, quote in module.data['quotes'].items():
        <blockquote>
             <div class="quote">"{{quote}}"</div>
             <div class="source">&mdash; {{source}}</div>
        </blockquote>
%end
    </div>

    <div class="elements">
%for key, value in module.data['links'].items():
    %if value['type'] == 'youtube-short':
        %include('feed/youtube-short', data=value)
    %end
    %if value['type'] == 'youtube':
        %include('feed/youtube', data=value)
    %end
    %if value['type'] == 'bandcamp':
        %include('feed/bandcamp', data=value)
    %end
    %if value['type'] == 'thumbnail':
        %include('feed/html', data=value)
    %end
%end
    </div>

</div>

%include('footer')
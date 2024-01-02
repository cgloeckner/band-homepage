%include('header', module_name='releases')

<img class="title" alt="{{module.band_name}} Foto" src="{{module.server.path.get_static_url('/content/titles/releases.jpg')}}">

<div class="releases">

<h1 class="shifted">{{module.base_title}}</h1>

    <div class="container">
%for item in module.data:
    %include('releases/item', item=item)
%end
    </div>

</div>

%include('footer')

%include('header', module_name='lineup')

<img class="title" alt="{{module.band_name}} Foto" src="{{module.server.get_static_url('/content/titles/lineup.jpg')}}">

<div class="lineup">

<h1 class="shifted">{{module.base_title}}</h1>

<h2 class="center">Aktuelle Besetzung</h2>

<div class="overview">
%for key, value in module.data:
    %include('lineup/member', key=key, data=value)
%end
</div>

<h2 class="center">Biografie</h2>

<h3>Gründung</h3>
<p>...
</p>

</div>

%include('footer')
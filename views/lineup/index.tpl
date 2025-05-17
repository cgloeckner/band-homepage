%include('header', module_name='lineup')

<img class="title" alt="{{module.band_name}} Foto" src="/content/titles/lineup.jpg">

<div class="lineup">

<h1 class="shifted">{{module.base_title}}</h1>

<h2 class="center">Aktuelle Besetzung</h2>

<div class="overview">
%for key, value in module.data.items():
    %include('lineup/member', key=key, data=value)
%end
</div>

{{!module.biography}}

</div>

%include('footer')
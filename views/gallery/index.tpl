%include('header', module_name='gallery')

<img class="title" alt="{{module.band_name}} Foto" src="/content/titles/gallery.jpg">

<div class="gallery">

<h1 class="shifted">{{module.base_title}}</h1>

    <div class="container">
%for file in module.data:
    %include('gallery/thumbnail', file=file)
%end
    </div>

    <p class="center">Die Urheberrechte der Bilder liegen bei den jeweiligen Fotografen. Wir bedanken uns für die
        Genehmigung zur Nutzung.</p>

</div>

%include('footer')

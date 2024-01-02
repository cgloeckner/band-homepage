%include('header', module_name='merch')

<img class="title" alt="{{module.band_name}} Foto" src="{{get_static_url('/content/titles/merch.jpg')}}">

<div class="merch">

<h1 class="shifted">{{module.base_title}}</h1>

<p class="center card">Merch könnt ihr bei unseren Konzerten oder per Post erhalten.<br>
    Alle Preise inkl. MwSt., ggf. zzgl. Versandkosten.<br>
    <br>
    Alle CDs sind außerdem digital verfügbar
    <a class="listen" href="" target="_blank">
        <img class="icon" alt="Spotify Link" src="https://open.spotifycdn.com/cdn/images/favicon.0f31d2ea.ico">
    </a>
    <br>
    <br>
    <b>Anfragen / Bestellungen an:</b><br>
    <a href="mailto:{{merch_email}}">{{merch_email}}</a>
</p>

%for category in data:
    %include('merch/category', category=category, data=data[category])
%end

</div>

%include('footer')

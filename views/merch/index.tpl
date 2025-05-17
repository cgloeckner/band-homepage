%include('header', module_name='merch')

<img class="title" alt="{{module.band_name}} Foto" src="/content/titles/merch.jpg">

<div class="merch">

<h1 class="shifted">{{module.base_title}}</h1>

%if module.merch is None:
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
%merch_email = module.server.email.get_merch_email()
    <a href="mailto:{{merch_email}}">{{merch_email}}</a>
</p>

    %for category, value in module.data.items():
        %include('merch/category', category=category, data=value)
    %end
%else:
    <p class="center card">Merch könnt ihr bei unseren Konzerten oder per Post erhalten.<br>
    <br>
    <b>Mehr Infos:</b><br>
    &#x1F449; <a href="{{module.merch['url']}}" target="_blank">{{module.merch['title']}}</a> &#x1F448;<br>
    <br>
    <b>Anfragen / Bestellungen gerne auch an:</b><br>
%merch_email = module.server.email.get_merch_email()
    <a href="mailto:{{merch_email}}">{{merch_email}}</a>
%end

</div>

%include('footer')

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
<div class="center card">
    <p class="center">Merch könnt ihr bei unseren Konzerten oder per Post erhalten.</p>
    
    <b>Anfragen / Bestellungen gerne an</b>
    <p class="center">
%merch_email = module.server.email.get_merch_email()
    <a href="mailto:{{merch_email}}">{{merch_email}}</a>
    </p>

    oder hier
    <p class="center">
    &#x1F310; <a class="underlined" href="{{module.merch['url']}}" target="_blank">{{module.merch['title']}}</a>
    </p>
%end

</div>

%include('footer')

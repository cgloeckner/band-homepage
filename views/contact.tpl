%include('header', module_name='contact')

<div class="contact">

<br>
<br>
<br>
<br>

<h1>Kontakt</h1>

<div class="emails">

%for category in module.contact:
    <h2 class="center">{{category['title']}}</h2>
    <p class="center card">
        <b>{{category['name']}}</b><br>
        <a href="mailto:{{category['email']}}">{{category['email']}}</a>
    </p>

%end
</div>

<h2 class="center">Electronic Press Kit (EPK)</h2>

<div class="center card">
    <p>In unserem EPK befindet sich eine Fülle von Informationen für Presse, Blogs, Redaktionen, Veranstalter:innen, Labels, Vertriebe und andere Geschäftspartner:innen.</p>
    <p><a href="{{module.epk.get_url()}}">💾 {{module.epk.get_filename()}} (ca. {{module.epk.get_size()}})</a></p>
</div>

<h2 class="center">Stage Rider</h2>

<div class="center card">
    <p>Unser Stage Rider dient zur Orientierung von Veranstalter:innen und Livetechniker:innen in Vorbereitung auf Konzerte. Darin werden Idealbedingungen beschrieben. Abweichungen sind nach Rücksprache möglich.</p>
    <p><a href="{{module.rider.get_url()}}" target="_blank">💾 {{module.rider.get_filename()}} (ca. {{module.rider.get_size()}})</a></p>
</div>

</div>

%include('footer')

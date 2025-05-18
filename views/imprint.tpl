%include('header', module_name='impressum')

<div class="impressum">

<br>
<br>
<br>
<br>

<h1>Impressum</h1>

<h2 class="center">{{module.band_name}}</h2>

<p class="center card">
    <b>Vertreten durch: </b><br>
%for line in module.represented_by:
    {{line}}<br />
%end
    <br>
    <b>Kontakt:</b><br>
    Telefon: {{module.phone}}<br>
%contact_email = module.server.email.get_contact_email()
    E-Mail: <a href="mailto:{{contact_email}}">{{contact_email}}</a><br>
</p>

<h2 class="center">Datenschutz</h2>

<p class="center card">
    Wir verfolgen keine Besucheraktivitäten und nutzen keine Analysetools.<br>
    Wir verlangen keine Registrierung und erheben keine Kontaktdaten.<br>
    <br>
    Die eingebetteten Player erfordern Cookies. Wenn Sie allen Cookies auf dieser Website zustimmen, werden diese verwendet, um die Player funktionsfähig zu machen. Wenn Sie nur essenzielle Cookies akzeptieren, werden alle eingebetteten Player deaktiviert.<br>
    <br>
    Technisch bedingt speichern wir Ihre Entscheidung in einem Cookie.<br>
</p>

</div>

%include('footer')
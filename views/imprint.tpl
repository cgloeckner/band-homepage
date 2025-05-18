%include('header', module_name='impressum')

<div class="impressum">

<br>
<br>
<br>
<br>

<h1>Impressum</h1>

<p class="center"><a class="underlined" href="#privacy">Zur Datenschutzerklärung</a></p>

<div class="center card">
    <p>Angaben gemäß § 5 Digitale-Dienste-Gesetz (DDG)</p>

    <h2 class="center">{{module.band_name}}</h2>

    <b>Vertreten durch</b>
    <p class="center">
%for line in module.represented_by:
    {{line}}<br />
%end
    </p>

    <b>Kontakt</b>
    <p class="center">
    Telefon: <a href="tel:{{module.phone}}">{{module.phone}}</a><br>
%contact_email = module.server.email.get_contact_email()
    E-Mail: <a href="mailto:{{contact_email}}">{{contact_email}}</a><br>
    </p>

    <b>Haftung für Inhalte</b>
    <p>Die Inhalte dieser Seite wurden mit größter Sorgfalt erstellt. Für die Richtigkeit, Vollständigkeit und Aktualität der Inhalte kann jedoch keine Gewähr übernommen werden.</p>

    <b>Haftung für Links</b>
    <p>Trotz sorgfältiger inhaltlicher Kontrolle übernehmen wir keine Haftung für die Inhalte externer Links. Für den Inhalt verlinkter Seiten sind ausschließlich deren Betreiber verantwortlich.</p>

    <b>Urheberrecht</b>
    <p>Die durch den Seitenbetreiber erstellten Inhalte und Werke auf diesen Seiten unterliegen dem deutschen Urheberrecht. Beiträge Dritter sind als solche gekennzeichnet.</p>
</div>

<a name="privacy"></a>
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
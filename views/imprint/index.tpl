%include('header', module_name='impressum')

<div class="impressum">

<br>
<br>
<br>
<br>

<h1>Impressum</h1>

Angaben gemäß § 5 TMG

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

%include('imprint/disclaimer')

</div>

%include('footer')
%include('header', module_name='contact')

<div class="contact">

<br>
<br>
<br>
<br>

<h1>Kontakt</h1>

<div class="emails">

%for category in module.contacts:
    <h2>{{category['title']}}</h2>
    <p class="center card">
        <b>{{category['name']}}</b><br>
        <a href="mailto:{{category['email']}}">{{category['email']}}</a>
    </p>

%end
</div>

</div>

%include('footer')

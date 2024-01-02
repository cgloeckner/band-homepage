%include('header', module_name='shows')

<img class="title" alt="{{module.band_name}} Foto" src="{{module.server.path.get_static_url('/content/titles/shows.jpg')}}">

<div class="shows">

<h1 class="shifted">{{module.base_title}}</h1>

<p class="center card">Unser Standort: {{module.location}}
    <br>
    <br>
    <b>Konzertanfragen an:</b><br>
%booking_email = module.server.email.get_booking_email()
    <a href="mailto:{{booking_email}}">{{booking_email}}</a>
</p>

%years_desc = sorted(module.data.keys(), key=lambda v: -v)
%for index, year in enumerate(years_desc):
    <div class="list toggle">
        <span onClick="toggleCollapse('shows_{{year}}');">
            <h2><span id="shows_{{year}}_button">&#9662;</span> {{year}}</h2>
        </span>
        <div id="shows_{{year}}_container">
        %include('shows/list', data=module.data[year])
        </div>
    </div>
%end

</div>

%include('footer')

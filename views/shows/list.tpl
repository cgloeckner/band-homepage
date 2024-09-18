%for index, show in enumerate(data):
    %alt = '' if index % 2 == 0 else 'alternate'
        <p class="{{alt}}">
            {{show['date'].strftime('%d.%m.%y')}} &mdash; <b>{{show['title']}}</b>
    %if 'description' in show and show['description'] != '':
            <br>
            <i>{{show['description']}}</i>
    %end
    %if 'location' in show and show['location'] != '':
            <br>
            ({{show['location']}})
    %end
        </p>
%end

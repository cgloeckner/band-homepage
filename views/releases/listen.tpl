%if 'listen' in item:
    %for key in item['listen']:
        %if key == 'spotify':
            %spotify_button_url = module.social_icons['spotify']
                        <a class="listen" href="https://open.spotify.com/intl-de/album/{{item['listen']['spotify']}}" target="_blank">
                            <img class="icon" alt="Spotify Link" src="{{spotify_button_url}}">
                        </a>
        %end
    %end
%end
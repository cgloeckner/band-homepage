%if 'listen' in item:
    %for key, value in item['listen'].items():
        %include('releases/' + key, value=value)
    %end
%end
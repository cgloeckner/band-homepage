%expire_flag = ''
%if 'expire' in data:
    %expire_at = data['expire'].strftime('%Y-%m-%d')
    %expire_flag = f' class=may_expire expire={expire_at}'
%end
        <embed
            src="https://www.youtube-nocookie.com/embed/{{data['target']}}"
            wmode="transparent"
            type="video/mp4"
            width="400" height="250"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            allowfullscreen
            title="YouTube Video Player"
            {{expire_flag}}
        >

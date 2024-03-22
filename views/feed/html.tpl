%expire_flag = ''
%if 'expire' in data:
    %expire_at = data['expire'].strftime('%Y-%m-%d')
    %expire_flag = f' class=may_expire expire={expire_at}'
%end
        <a href="{{data['target']}}" target="_blank" {{expire_flag}}>
            <img class="thumbnail" src="{{data['url']}}" />
        </a>

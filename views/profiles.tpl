<div class="social-profiles">
    %for type in module.profiles:
        %profile_url = module.profiles[type]
        %button_icon = module.social_icons[type]
    <a href="{{profile_url}}" target="_blank">
        <img class="icon" alt="{{type.title()}} Link" src="{{button_icon}}">
    </a>
    %end
</div>

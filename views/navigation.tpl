    <a href="/">
        <img class="navi-logo" alt="{{module.band_name}}" src="{{module.server.get_static_url('/content/logo_inverted.png')}}">
    </a>

    <div class="navigation">
        <div class="icon">&#x2261;</div>

        <div class="elements">
            <a href="/" title="News, Videos">Feed</a>
%if 'releases' in module.navigation:
            <a href="/releases" title="CDs, Artwork, Tracklists">Releases</a>
%end
%if 'lineup' in module.navigation:
            <a href="/lineup" title="Lineup, Biografie">Lineup</a>
%end
%if 'shows' in module.navigation:
            <a href="/shows" title="Live Shows">Shows</a>
%end
%if 'gallery' in module.navigation:
            <a href="/gallery" title="Live Fotos">Gallery</a>
%end
%if 'merch' in module.navigation:
            <a href="/merch" title="Merchandise">Merch</a>
%end
        </div>
    </div>

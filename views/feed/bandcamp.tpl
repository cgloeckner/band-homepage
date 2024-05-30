%base_url = module.profiles['bandcamp']
        <iframe style="border: 0; width: 400px; height: 274px;"
                src="https://bandcamp.com/EmbeddedPlayer/album=3853137783/size=large/bgcol=333333/linkcol=ffffff/artwork=small/transparent=true/"
                seamless>
            <a href="{{base_url}}/album/{{value['url']}}">{{value['title']}}</a>
        </iframe>
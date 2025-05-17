        <div class="release">
            <img class="preview" alt="{{item['title']}}" src="/content/cds/' + item['thumbnail'] + '.jpg">
            <div class="column">
                <div class="title"><h2>{{item['title']}}</h2></div>
                <div class="description">{{item['year']}} | {{item['type']}}
%include('releases/listen', item=item)
%if 'label' in item:
                    | {{item['label']}}
%end
                </div>
                <div class="tracklist"><b>Tracklist:</b>
                    <ol>
%for track in item['tracks']:
                        <li>{{track}}</li>
%end
                    </ol>
                </div>
%if 'bandcamp' in item['listen']:
    %base_url = module.profiles['bandcamp']
    %album_uri = item['listen']['bandcamp']
            <iframe style="border: 0; width: 100%; height: 42px;"
                    src="https://bandcamp.com/EmbeddedPlayer/album=3853137783/size=small/bgcol=333333/linkcol=ffffff/transparent=true/"
                    seamless>
                <a href="{{base_url}}/album/{{album_uri}}">{{item['title']}}</a>
            </iframe>
%end
            </div>
        </div>
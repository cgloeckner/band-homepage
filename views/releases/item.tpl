        <div class="release">
            <img class="preview" alt="{{item['title']}}" src="{{module.server.path.get_static_url('/content/cds/' + item['thumbnail'] + '.jpg')}}">
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
            </div>
        </div>
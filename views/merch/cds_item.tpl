            <div class="item">
                <img class="preview" alt="{{item['title']}}" src="{{module.server.path.get_static_url('/content/cds/' + item['thumbnail'] + '.jpg')}}">
                <span class="title">{{item['title']}}</span>
                <span class="description">{{item['year']}} | {{item['type']}}
%include('releases/listen', item=item)
                </span>
%include('merch/price', price=item['price'])
            </div>

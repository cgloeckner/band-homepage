            <div class="item">
                <img class="preview" alt="{{item['title']}}" src="/content/cloths/' + item['tag'] + '.png">
                <span class="title">{{item['title']}}</span>
                <span class="description">{{item['description']}}</span>
%include('merch/price', price=item['price'])
            </div>

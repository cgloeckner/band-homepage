%import datetime

    </div>

    <p class="footer center">
        &copy; {{datetime.datetime.now().year}} {{module.band_name.upper()}} |
            <a href="/contact">Kontakt</a> |
            <a href="{{module.server.get_presskit_url()}}">Press Kit</a> |
            <a href="/imprint">Impressum</a> |
            <a href="/imprint#privacy">Datenschutz</a>
        <a class="scroll-up" href="#top" title="Scroll">^</a>
    </p>

</body>

</html>

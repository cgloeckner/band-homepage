# band-homepage
Engine for band homepages of
- [Kali Yuga](https://www.kali-yuga.de)
- [Laser Scope](https://www.laser-scope.de)

## Example `/etc/caddy/Caddyfile`

```yaml
static.example.com {
        encode zstd gzip

        root * /opt/band-homepage/views/static

        file_server
}

www.example.com {
        encode zstd gzip

        root * /opt/band-homepage/.build

        # handle a few files
        handle /robots.txt {
                file_server
        }
        handle /sitemap.xml {
                file_server
        }

        # handle all html files
        @html_files {
                path *.html
        }
        file_server @html_files

        # redirect everything else to *.html
        @notRoot {
                not path /
                not path /robots.txt /sitemap.xml
        }
        rewrite @notRoot /{http.request.uri.path}.html

        # handle / as index.html
        route {
                file_server

                @root {
                        path /
                }

                file_server @root {
                        index index.html
                }
        }

        log {
                output file /var/log/caddy/band-homepage.log
        }
}
```
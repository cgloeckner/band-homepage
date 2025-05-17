# band-homepage
Engine for band homepage [Laser Scope](https://www.laser-scope.de)

## Example `/etc/caddy/Caddyfile`

```yaml
www.example.com {
        encode zstd gzip

        log {
                output log /var/log/caddy/band-homepage.log
        }
}

www.example.com {
        encode zstd gzip
        
        root * /path/to/www
        file_server
 
        try_files {path}.html {path} /index.html
}


example.com {
        redir https://www.example.com{uri} permanent
}
```
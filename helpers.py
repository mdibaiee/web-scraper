from urllib.parse import urlparse, urlunparse, urljoin

def to_absolute(url, host):
    if url == '/': return host

    if url[0:2] == '//':
        url = urlparse(host).scheme + ':' + url

    p = urlparse(url)
    if not (p.scheme in ['http', 'https', '']): return None

    if not p.netloc:
        p = urlparse(urljoin(host, url))

    return p
        


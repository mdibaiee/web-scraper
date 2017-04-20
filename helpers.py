from urllib.parse import urlparse, urlunparse, urljoin
import os
from csv import DictWriter

def to_absolute(url, host):
    if url == '/': return host

    if url[0:2] == '//':
        url = urlparse(host).scheme + ':' + url

    p = urlparse(url)
    if not (p.scheme in ['http', 'https', '']): return None

    if not p.netloc:
        p = urlparse(urljoin(host, url))

    return p
        
def write_results(main, data, first=False):
    with open(os.path.join('results', main.netloc, 'texts.csv'), 'w' if first else 'a') as f:
            w = DictWriter(f, fieldnames=['page', 'tag', 'text', 'link', 'image'])

            if first:
                w.writeheader()

            w.writerows(data)


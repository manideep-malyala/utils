from urllib.parse import urlparse

def is_valid_url(url: str) -> bool:
    r = urlparse(url)
    return r.scheme in {"http", "https"} and bool(r.netloc)

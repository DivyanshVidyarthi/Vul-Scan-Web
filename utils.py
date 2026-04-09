from urllib.parse import urlparse

def get_domain(url):
    return urlparse(url).netloc


def is_same_domain(url1, url2):
    return get_domain(url1) == get_domain(url2)

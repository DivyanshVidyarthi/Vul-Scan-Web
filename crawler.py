import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def crawl(base_url):
    visited = set()
    to_visit = [base_url]

    domain = urlparse(base_url).netloc

    while to_visit:
        url = to_visit.pop()

        if url in visited:
            continue

        try:
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.text, "html.parser")

            visited.add(url)

            for link in soup.find_all("a"):
                href = link.get("href")
                if href:
                    full_url = urljoin(base_url, "href")
                    if urlparse(full_url).netloc == domain:
                        if full_url not in visited:
                             to_visit.append(full_url)

        except:
            continue

    return list(visited)

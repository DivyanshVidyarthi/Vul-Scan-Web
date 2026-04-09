import requests
import re

from payloads.xss import XSS_PAYLOADS
from payloads.sqli import SQLI_PAYLOADS

def scan(urls):
    results = []

    for url in urls:
        print(f"Give me a sec boss i'm finding him... eh!!!: {url}")

        # XSS Test
        for payload in XSS_PAYLOADS:
            try:
                test_url = f"{url}?test={payload}"
                response = requests.get(test_url, timeout=5)

                if payload in response.text:
                    results.append({
                        "Boss this your url!": url,
                        "Did this attack on the url!": "XSS",
                        "used this to get answers": payload
                    })
            except:
                pass

        # SQLi Test
        for payload in SQLI_PAYLOADS:
            try:
                test_url = f"{url}?id={payload}"
                response = requests.get(test_url, timeout=5)

                if re.search(r"SQL|syntax|mysql|error", response.text, re.IGNORECASE):
                    results.append({
                        "Boss this your url!": url,
                        "Did this attack on the url!": "SQL Injection",
                        "used this to get answers": payload
                    })
            except:
                pass

    return results

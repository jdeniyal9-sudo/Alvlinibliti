import requests

def detect_tech(domain):

    try:

        r = requests.get(
            "https://" + domain,
            timeout=5
        )

        headers = str(r.headers).lower()

        tech = []

        if "cloudflare" in headers:
            tech.append("Cloudflare")

        if "nginx" in headers:
            tech.append("Nginx")

        if "apache" in headers:
            tech.append("Apache")

        if "wordpress" in r.text.lower():
            tech.append("WordPress")

        return {
            "technologies": tech
        }

    except Exception as e:

        return {
            "tech_error": str(e)
        }

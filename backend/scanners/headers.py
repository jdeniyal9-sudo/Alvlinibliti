import requests

def scan_headers(domain):

    try:

        url = "https://" + domain

        r = requests.get(url, timeout=5)

        return {
            "server": r.headers.get("Server"),
            "content_security_policy":
                r.headers.get("Content-Security-Policy"),

            "x_frame_options":
                r.headers.get("X-Frame-Options"),

            "strict_transport_security":
                r.headers.get("Strict-Transport-Security")
        }

    except Exception as e:

        return {
            "headers_error": str(e)
        }

from flask import Flask, jsonify

from scanners.dns import get_dns
from scanners.headers import get_headers
from scanners.tech import detect_tech
from scanners.whois_scan import get_whois

app = Flask(__name__)

@app.route("/scan/<domain>")
def scan(domain):

    result = {
        "domain": domain,
        "dns": get_dns(domain),
        "headers": get_headers(domain),
        "technology": detect_tech(domain),
        "whois": get_whois(domain)
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, jsonify
from flask_cors import CORS

from scanners.ssl import scan_ssl
from scanners.headers import scan_headers
from scanners.whois_scan import get_whois
from scanners.tech import detect_tech
from scanners.dns import scan_dns
from scanners.iplookup import get_ip
from scanners.ports import scan_ports

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({
        "message": "Recon Scanner API Running"
    })


@app.route("/scan/<domain>")
def scan(domain):

    result = {
        "domain": domain
    }

    # SSL
    try:
        result["ssl"] = scan_ssl(domain)
    except Exception as e:
        result["ssl"] = {"error": str(e)}

    # Headers
    try:
        result["headers"] = scan_headers(domain)
    except Exception as e:
        result["headers"] = {"error": str(e)}

    # WHOIS
    try:
        result["whois"] = get_whois(domain)
    except Exception as e:
        result["whois"] = {"error": str(e)}

    # DNS
    try:
        result["dns"] = scan_dns(domain)
    except Exception as e:
        result["dns"] = {"error": str(e)}

    # IP Lookup
    try:
        result["ip"] = get_ip(domain)
    except Exception as e:
        result["ip"] = {"error": str(e)}

    # Ports
    try:
        result["ports"] = scan_ports(domain)
    except Exception as e:
        result["ports"] = {"error": str(e)}

    # Technology Detection
    try:
        result["tech"] = detect_tech(domain)
    except Exception as e:
        result["tech"] = {"error": str(e)}

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

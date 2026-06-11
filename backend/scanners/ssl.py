import ssl
import socket
import whois
import dns.resolver


def scan_ssl(domain):

    result = {}

    # SSL CHECK
    try:
        ctx = ssl.create_default_context()

        with socket.create_connection((domain, 443)) as sock:
            with ctx.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()

        result["ssl"] = {
            "issuer": str(cert.get("issuer")),
            "expires": cert.get("notAfter")
        }

    except Exception as e:
        result["ssl_error"] = str(e)

    # DNS CHECK
    try:
        answers = dns.resolver.resolve(domain, "NS")

        result["name_servers"] = [
            str(rdata) for rdata in answers
        ]

    except Exception as e:
        result["dns_error"] = str(e)

    # WHOIS CHECK
    try:
        w = whois.whois(domain)

        result["whois"] = {
            "registrar": str(w.registrar),
            "creation_date": str(w.creation_date),
            "expiration_date": str(w.expiration_date)
        }

    except Exception as e:
        result["whois_error"] = str(e)

    return result

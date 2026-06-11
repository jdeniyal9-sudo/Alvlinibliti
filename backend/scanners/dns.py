import dns.resolver

def scan_dns(domain):
    result = {}

    try:
        a_records = dns.resolver.resolve(domain, 'A')
        result["A"] = [str(r) for r in a_records]
    except:
        result["A"] = []

    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        result["MX"] = [str(r.exchange) for r in mx_records]
    except:
        result["MX"] = []

    try:
        ns_records = dns.resolver.resolve(domain, 'NS')
        result["NS"] = [str(r) for r in ns_records]
    except:
        result["NS"] = []

    return result

import dns.resolver

def get_dns(domain):

    result = {}

    try:

        a_records = dns.resolver.resolve(domain, "A")

        result["A"] = [
            str(r) for r in a_records
        ]

    except:
        result["A"] = []

    try:

        mx_records = dns.resolver.resolve(domain, "MX")

        result["MX"] = [
            str(r.exchange)
            for r in mx_records
        ]

    except:
        result["MX"] = []

    return result

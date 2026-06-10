import dns.resolver

def get_dns(domain):

    records = {}

    for record_type in ['A', 'MX', 'NS']:

        try:
            answers = dns.resolver.resolve(domain, record_type)

            records[record_type] = [str(r) for r in answers]

        except Exception as e:
            records[record_type] = str(e)

    return records

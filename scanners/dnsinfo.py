import dns.resolver

def dns_lookup(domain):
    records = ['A', 'MX', 'NS']

    for record in records:
        try:
            answers = dns.resolver.resolve(domain, record)

            print(f"\n{record} Records:")
            for data in answers:
                print(data)

        except:
            pass

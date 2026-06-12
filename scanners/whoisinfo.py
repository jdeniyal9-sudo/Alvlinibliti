import whois

def whois_lookup(domain):
    try:
        data = whois.whois(domain)

        print("Domain :", data.domain_name)
        print("Registrar :", data.registrar)
        print("Creation :", data.creation_date)

    except Exception as e:
        print(e)

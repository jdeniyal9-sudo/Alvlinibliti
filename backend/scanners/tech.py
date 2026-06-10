import builtwith

def detect_tech(domain):
    try:
        return builtwith.parse(f"https://{domain}")

    except Exception as e:
        return {"error": str(e)}

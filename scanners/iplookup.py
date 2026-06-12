import requests

def ip_lookup(target):
    try:
        data = requests.get(f"http://ip-api.com/json/{target}").json()

        print("Country :", data.get("country"))
        print("City :", data.get("city"))
        print("ISP :", data.get("isp"))

    except Exception as e:
        print(e)

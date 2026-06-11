import socket

def get_ip(domain):

    try:
        ip = socket.gethostbyname(domain)

        return {
            "ip": ip
        }

    except Exception as e:
        return {
            "ip_error": str(e)
        }

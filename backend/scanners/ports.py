import socket

def scan_ports(domain):

    ports = [21, 22, 80, 443, 3306, 8080]

    open_ports = []

    for port in ports:

        s = socket.socket()

        s.settimeout(1)

        result = s.connect_ex((domain, port))

        if result == 0:
            open_ports.append(port)

        s.close()

    return open_ports

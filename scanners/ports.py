import nmap

def port_scan(target):
    scanner = nmap.PortScanner()
    scanner.scan(target, '1-1000')

    for host in scanner.all_hosts():
        print(f"\nHost : {host}")

        for proto in scanner[host].all_protocols():
            ports = scanner[host][proto].keys()

            for port in ports:
                state = scanner[host][proto][port]['state']
                print(f"Port {port} : {state}")

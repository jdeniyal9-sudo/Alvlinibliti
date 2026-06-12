from scanners.dnsinfo import dns_lookup
from scanners.ports import port_scan
from scanners.sslscan import ssl_info
from scanners.whoisinfo import whois_lookup
from scanners.iplookup import ip_lookup

from colorama import Fore, init
init()

banner = f"""{Fore.GREEN}

██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║
██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║
██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝

"""

print(banner)

target = input(Fore.CYAN + "TARGET DOMAIN/IP : ")

print(Fore.YELLOW + "\n[+] WHOIS")
whois_lookup(target)

print(Fore.YELLOW + "\n[+] DNS INFO")
dns_lookup(target)

print(Fore.YELLOW + "\n[+] PORT SCAN")
port_scan(target)

print(Fore.YELLOW + "\n[+] SSL INFO")
ssl_info(target)

print(Fore.YELLOW + "\n[+] IP LOOKUP")
ip_lookup(target)

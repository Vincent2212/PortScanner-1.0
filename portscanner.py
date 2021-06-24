# PortScanner 1.3
import requests
import sys
url = "https://ports.yougetsignal.com/check-port.php"
how_many = int(input("Ports: "))
ip = input("Enter a IP or URL: ")
open_ports = []
if not ip:
    print("No value given.")
    sys.exit()
print(f"Checking ports on {ip}...")

for x in range(1, how_many + 1):
    data = {
        "MIME Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "remoteAddress": ip,
        "portNumber": x,
    }
    response = requests.post(url, data=data).text
    if 'src="/img/flag_green.gif' in response:
        open_ports.append(x)
        
    elif "Invalid remote address." in response:
        print("Invalid IP or url.")
        break

if len(open_ports) == 0:
    print(f"Found {len(open_ports)} open ports on {ip}")
    sys.exit()

print(f"Found {len(open_ports)} open ports on {ip}\n{open_ports}")

import requests
url = "https://ports.yougetsignal.com/check-port.php"
how_many = int(input("How many ports to check? ")) # Enter a range starting from 1
ip = input("Enter a IP Address: ")

for x in range(1, how_many):
    data = {
        "MIME Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "remoteAddress": ip,
        "portNumber": x,
    }
    response = requests.post(url, data=data).text
    if 'src="/img/flag_green.gif' in response:
        print(f"Port {x} is open on {ip}")
        break
    else:
        print(f"Port {x} is closed")

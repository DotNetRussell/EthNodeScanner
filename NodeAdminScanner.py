import json
import requests
import sys

def check_node_health(ip):
    url = f"http://{ip}:8545"
    headers = {'Content-Type': 'application/json'}
    payload = json.dumps({"jsonrpc": "2.0", "method": "admin_peers", "params": [], "id": 1})

    try:
        response = requests.post(url, headers=headers, data=payload, timeout=2)
        if response.status_code == 200 and response.json().get('result'):
            return True
    except requests.RequestException:
        pass
    return False

def main(filename):
    with open(filename, 'r') as file:
        ips = file.readlines()

    for ip in ips:
        ip = ip.strip()
        if check_node_health(ip):
            print(f"{ip} is up and allows admin commands")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python NodeHealthChecker.py <filename>")
        sys.exit(1)
    main(sys.argv[1])

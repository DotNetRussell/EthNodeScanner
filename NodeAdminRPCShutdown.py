import json
import requests
import sys

def shutdown_node(ip):
    url = f"http://{ip}:8545"
    headers = {'Content-Type': 'application/json'}
    payload = json.dumps({"jsonrpc": "2.0", "method": "admin_stopRPC", "params": [], "id": 1})

    try:
        requests.post(url, headers=headers, data=payload, timeout=2)
    except requests.RequestException:
        pass

def check_node_down(ip):
    url = f"http://{ip}:8545"
    headers = {'Content-Type': 'application/json'}
    payload = json.dumps({"jsonrpc": "2.0", "method": "admin_peers", "params": [], "id": 1})

    try:
        requests.post(url, headers=headers, data=payload, timeout=2)
        return False
    except requests.RequestException:
        return True

def main(filename):
    with open(filename, 'r') as file:
        ips = file.readlines()

    for ip in ips:
        ip = ip.strip()
        shutdown_node(ip)
        if check_node_down(ip):
            print(f"Server taken down: {ip}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python NodeShutdownExecutor.py <filename>")
        sys.exit(1)
    main(sys.argv[1])

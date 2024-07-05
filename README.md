# Node Management Scripts

This repository contains two Python scripts designed for managing Ethereum nodes. The scripts perform the following tasks:

1. **NodeAdminScanner.py**: Checks if a list of Ethereum nodes are up and allows admin commands.
2. **NodeAdminRPCShutdown.py**: Sends a shutdown command to a list of Ethereum nodes and checks if they have been taken down.

## Prerequisites

- Python 3.x
- `requests` library

You can install the `requests` library using pip:

```bash
pip install requests
```

## Usage

Both scripts require a file containing a list of IP addresses (one per line) as an argument. The port is assumed to be `8545`.

### NodeAdminScanner.py

This script checks if the nodes are up and allow admin commands.

#### Usage

```bash
python NodeAdminScanner.py <filename>
```

#### Example

```bash
python NodeAdminScanner.py ip_list.txt
```

### NodeAdminRPCShutdown.py

This script sends the `admin_stopRPC` command to the nodes and then checks if they have been taken down.

#### Usage

```bash
python NodeAdminRPCShutdown.py <filename>
```

#### Example

```bash
python NodeAdminRPCShutdown.py ip_list.txt
```

## File Format

The input file should contain a list of IP addresses, one per line. Example:

```
82.97.241.226
82.97.241.240
82.97.241.67
213.171.8.55
81.200.158.168
82.97.241.146
82.97.241.204
213.171.3.109
158.160.91.76
82.97.241.192
82.97.241.164
158.160.72.216
91.186.197.52
178.20.236.12
213.171.12.218
82.97.241.34
213.171.9.77
83.222.9.72
213.171.9.77
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributions

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.

---

This README provides a detailed overview of the two scripts, their usage, and examples. Feel free to customize it further as per your needs.

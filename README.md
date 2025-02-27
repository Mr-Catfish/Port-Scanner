# Python Port Scanner

A simple Python port scanner that allows you to ping a target IP address and scan a range of ports for availability. The script can be used to check whether specific ports are open on a target machine or server. It includes an IP ping feature to verify if the target is reachable before scanning for open ports.

## Features:
- Pings the target IP to check if it's reachable.
- Allows scanning of a single port or a range of ports.
- Configurable timeout for port scan attempts.
- Works on both Windows and Linux/macOS.

## Usage:
1. Input the target IP address.
2. Ping the target IP to ensure it is reachable.
3. Choose whether to scan a single port or a range of ports.
4. The script will output the status (open/closed) of the ports.

## Requirements:
- Python 3.x
- `subprocess` (for pinging the IP)
- `socket` (for port scanning)

## How to Run:
1. Clone the repository:
   ```bash
   git clone https://github.com/Mr-Catfish/port-scanner.git

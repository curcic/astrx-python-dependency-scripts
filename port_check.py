import socket
import sys

if len(sys.argv) != 3:
    sys.exit(1)

ip_address = sys.argv[1]
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((ip_address, port))
    print(f'Port {port} is open on {ip_address}')
except Exception as e:
    print(f'Error connecting to {ip_address}:{port}: {e}')

s.close()

#!/bin/python3

import sys
import socket
from datetime import datetime

# Define our target.
if (len(sys.argv) == 2):
    # Translate hostname to IPV4.
    target_host = socket.gethostbyname(sys.argv[1])

else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip>")
    sys.exit()

# Add a pretty banner.
print("-" * 50)
print(f"Scanning target: {target_host}")
print(f"Time started: {str(datetime.now())}")
print("-" * 50)

try:
    for target_port in range(50, 85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target_host, target_port))
        if (result == 0):
            print(f"Port {target_port} is open")
        s.close()

except KeyboardInterrupt:
    print("\n Exiting program.")
    sys.exit()

except socket.gaierror:
    print("Hostanme could not be resolved.")
    sys.exit()

except socket.error:
    print("Could not connect to the server.")
    sys.exit()

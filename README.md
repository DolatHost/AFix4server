#  A Simple Fix portscan & DDOS Abuse on Ubunto

In Hetzner's cloud servers and vps other datacenters, when you have not set up a firewall, if you have not observed the security of the installed codes, a port scan or DDOS may be performed from inside the server, which leads to blocking the server.
To fix abuses and open your server, you must do something and inform the data center so that they can unblock it.
This script will automatically do the following:

# 1) Enable UFW Ubuntu Firewall
# 2) Close the server's private IPs
# 3) Blocking Too many requests in the firewall

installation:

git clone https://github.com/DolatHost/AFix4server.git
cd security && python3 security.py

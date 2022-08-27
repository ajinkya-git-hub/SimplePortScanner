#! /bin/python3

import sys
import socket
from datetime import datetime
import platform


#define our target

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPV4
	
else:
	print("Invalid amount of arguments.")
	print("Syntax: ./scanner.py <IP>")
	
#Adding a Banner
print("- -" * 50)
print("Scanner developed by AJ")
print("Scanning Target " +target)
print("Time Started: " +str(datetime.now()))
print("- -" * 50)

victim_os = platform.system()
print("Victim OS is: ",victim_os)

try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) #Returns an error indicator
		if result == 0:
			print("Port {} is open".format(port))
		s.close()	
		
except KeyboardInterrupt:
	print("\n Exiting the Program")
	sys.exit()
	
except socket.gaierror:
	print("Host could not be resolved...")
	sys.exit()

except socket.error:
	print("Could not connect to server!!!!!")
	sys.exit()
	
	
			
	

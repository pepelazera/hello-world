from urllib import error
import urllib.request

try:
    site = urllib.request.urlopen("http://www.pudim.com.br")
except error.URLError:
    print("O site pudim não está acessível no momento.")
else:
    print("Consegui acessar o site pudim com sucesso!")
    print(site.read()) # Lê o conteúdo html do site que eu acessar.
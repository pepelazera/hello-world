import requests

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
print(requisicao)
print(requisicao.json())

dicreq = requisicao.json()
print(dicreq["BTCBRL"]["bid"])
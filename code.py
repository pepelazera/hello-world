import requests

link = "https://2c5437cd-b54f-4f1a-9234-afce88194d6a-00-1h5udmfi0md6w.riker.replit.dev/pegarvendas"

requisicao = requests.get(link)

print(requisicao)
print(requisicao.json())

dicionario = requisicao.json()
print(dicionario["total_vendas"])

# Os códgios {200, 404, 400, 401, 500} indicam se a busca deu certo, errado ou então se o que você quer acessar é confidencial.
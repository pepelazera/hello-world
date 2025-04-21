pessoas = {'nome': 'Gustavo', 'sexo': 'Masculino', 'idade': 22}
pessoas['nome'] = 'Pedro' #modifica o nome do dicionário
del pessoas['sexo'] #apaga o sexo do dicionário
for k, v in pessoas.items():
    print(f'{k} = {v}')
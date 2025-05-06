def voto(): # Dentro dessa função temos o cálculo das idades sendo feito sem a importação da biblioteca datetime;
    from datetime import date
    atual = date.today().year
    print('-'*30) # O print foi usado somente para questões estéticas dentro da função, e também para manter uma organização.
    nascimento = int(input('Em que ano você nasceu ? '))
    calculoidade = atual - nascimento
    if calculoidade < 16: # Foram usados um 'if' e dois 'elif' para construir esse código com facilidade;
        print(f'Com {calculoidade} anos: NÃO VOTA.')
    elif calculoidade == 16 or calculoidade == 17 or calculoidade > 65:
        print(f'Com {calculoidade} anos: Voto opcional.')
    else:
        print(f'Com {calculoidade} anos: VOTO OBRIGATÓRIO.')


voto()
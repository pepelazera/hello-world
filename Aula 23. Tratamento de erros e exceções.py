try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except (ValueError, TypeError):
    print("Tivemos um problema com os tipos de dados que você digitou.")
except ZeroDivisionError:
    print("Não é possível fazer uma divisão por zero.")
except KeyboardInterrupt:
    print("O usuário preferiu não informar os dados.")
except Exception as erro:
    print(f"O err encontrado foi {r:.1f}")
else:
    print(f"O resultado é {r:.1f}") # Nesse caso, o else está sendo utilizado para não mostrar mensagem de erro no código, somente o que eu escrevi
finally:
    print(f"Volte sempre! Muito obrigado!")
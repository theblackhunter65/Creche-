print("Bem Vindo ao exercício de Python ")

while True:
    num1 = float(input("Digite o  primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro  número: "))
    lista = [num1, num2, num3]
    print(f"O maior número é {max(lista)}")
    print(f"A lista de números é {lista}")
    print(f"O menor número é {min(lista)}")
    print(f"A soma dos números é {sum(lista)}")
    print(f"A lista em ordem crescente é {sorted(lista)}")
    resposta = input("Deseja continuar? (S/N): ")
    if resposta.upper() == "N":
        break
    print("Obrigado por usar o programa!")
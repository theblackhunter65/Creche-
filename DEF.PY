valor_minimo = []
valor_maximo = []
valor_medio = []
validacao_de_dados = []
def validacao():
    while True:
        print("=======>>>>>>Sistema de Validação<<<<<<<<=======")
        print("Digite a opção desejada: ")
        print("1 - Digite os números")
        print("2 - Verificar dados e dar a validação de numeros")
        print("3 - Sair")
        opcao = input("Opção: ")
        if opcao == "1":
                valor_minimo.append(float(input("Digite o valor mínimo: ")))
                valor_maximo.append(float(input("Digite o valor máximo: ")))
                valor_medio.append(float(input("Digite o valor médio: ")))
                validacao_de_dados.append("Validado")
        elif opcao == "2":
            if len(valor_minimo) == len(valor_maximo) == len(valor_medio) ==len(validacao_de_dados):
                print("=======>>>>>>Validação de Dados<<<<<<<<=======")
            for i in range(len(valor_minimo)):
                if valor_minimo[i] < valor_medio[i] < valor_maximo[i]:
                    print(f"O valor {valor_medio[i]} está dentro do intervalo {valor_minimo[i]} - {valor_maximo[i]}")
                else:
                    print(f"O valor {valor_medio[i]} está fora do intervalo {valor_minimo[i]} - {valor_maximo[i]}")
           
                for z in range(len(valor_maximo)):
                    print(f"O valor máximo {valor_maximo[z]} é maior que o valor médio {valor_medio} e é maior que valor menor {valor_minimo}")
                else:
                    print("Os dados não estão completos para validação.")
                    for f in range(len(valor_minimo)):
                        print(f"O valor mínimo {valor_minimo[f]} é menor que o valor médio {valor_medio} e o valor maior {valor_minimo}")
                    else:
                        print("Os dados não estão completos para validação.")
        
        elif opcao == "3":
            print("=======>>>>>>SAIR<<<<<<<<=======")
            print("Obrigado por utilizar o sistema de validação")
            break

        else:
            print("Opção Inválida")

validacao()
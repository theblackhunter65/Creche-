print("Solicite o nome e a idade de 5 membros da família e utilize um loop for para iterar sobre esses membros determine quem é o mais velho, o do meio e o mais novo e apresente os resultados em uma lista formatada, com nomes e idades.")
nome1 = input("Digite o nome do primeiro membro da família: ")
idade1 = int(input("Digite a idade do primeiro membro da família: "))
nome2 = input("Digite o nome do segundo membro da família: ")
idade2 = int(input("Digite a idade do segundo membro da família: "))
nome3 = input("Digite o nome do terceiro membro da família: ")
idade3 = int(input("Digite a idade do terceiro membro da família: "))
nome4 = input("Digite o nome do quarto membro da família: ")
idade4 = int(input("Digite a idade do quarto membro da família: "))
nome5 = input("Digite o nome do quinto membro da família: ")
idade5 = int(input("Digite a idade do quinto membro da família: "))
idade_maior = idade1
idade_menor = idade1
idade_medio = idade1
idade_maior2 = idade2
idade_menor2 = idade2
idade_medio2 = idade2
idade_maior3 = idade3
idade_menor3 = idade3
idade_medio3 = idade3
idade_maior4 = idade4
idade_menor4 = idade4
idade_medio4 = idade4
idade_maior5 = idade5
idade_menor5 = idade5
idade_medio5 = idade5
nome_maior = nome1
nome_menor = nome1
nome_medio = nome1
nome_maior2 = nome2
nome_menor2 = nome2
nome_medio2 = nome2
nome_maior3 = nome3
nome_menor3 = nome3
nome_medio3 = nome3
nome_maior4 = nome4
nome_menor4 = nome4
nome_medio4 = nome4
nome_maior5 = nome5
nome_menor5 = nome5
nome_medio5 = nome5
for i in range(1,6):
    if idade1 > idade_maior:
        idade_maior = idade1
        nome_maior = nome1
    elif idade2 > idade_maior:
        idade_maior = idade2
        nome_maior = nome2
    elif idade3 > idade_maior:
        idade_maior = idade3
        nome_maior = nome3
    elif idade4 >  idade_maior:
        idade_maior = idade4
        nome_maior = nome4
    elif idade5 > idade_maior:
        idade_maior = idade5
        nome_maior = nome5
    elif idade1 > idade_medio:
        idade_medio = idade1
        nome_medio = nome1
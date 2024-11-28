print("Bem Vindo ao exercício de Python ")

# Solicitando 5 números para a lista
numeros = []
for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)
    # Mostrando o maior número da lista
    maior = max(numeros)
    print(f"O maior número da lista é: {maior}")
    # Mostrando o menor número da lista
    menor = min(numeros)
    print(f"O menor número da lista é: {menor}")
    # Mostrando a soma dos números da lista
    soma = sum(numeros)
    print(f"A soma dos números da lista é: {soma}")
    # Mostrando a média dos números da lista
    media = soma / len(numeros)
    print(f"A média dos números da lista é: {media}")
    # Mostrando a lista de números em ordem crescente
    numeros_ordenados_crescente = sorted(numeros)
    print(f"A lista de números em ordem crescente é: {numeros_ordenados_crescente}")
    # Mostrando a lista de números em ordem decrescente
    numeros_ordenados_decrescente = sorted(numeros, reverse=True)
    print(f"A lista de números em ordem decrescente é: {numeros_ordenados_decrescente}")
    print("A lista de números é: ", numeros)
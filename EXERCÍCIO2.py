while True:
    lista = []
    
    for _ in range(4):
        num = int(input("Digite um número de 0 a 100: "))
        

        while num < 0 or num > 100:
            print("Número inválido, tente novamente!")
            num = int(input("Digite um número de 0 a 100: "))
        
        lista.append(num)
    

    media = sum(lista) / len(lista)
    menor = min(lista)
    maior = max(lista)
    
   
    print(f"Você digitou os números: {lista}")
    print(f"A média dos números é: {media}")
    print(f"O menor número é: {menor}")
    print(f"O maior número é: {maior}")

    resposta = input("Deseja fazer o programa novamente? (S/N): ")
    if resposta.upper() == "N":
        print("Fim do programa")
        break

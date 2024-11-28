num = int(input("Digite um número entre 0 e 100: "))
while num < 0 or num > 100:
    num = int(input("Número invalido, por favor digite um número entre 0 e 100 "))
    print("O número digitado foi:", num)
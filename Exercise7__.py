print("Faça um sistema de de numeros crescente de um numero negativo  até 10 ")
num = int(input("Digite um numero negativo: "))
while num <= 0:
    num = int(input("Digite um numero negativo: "))
    for i in range(num, 11):
        print(i)
    break
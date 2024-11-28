print("Bem vindo !")
num1=float (input("Digite um número: "))
num2 =float(input("Digite o segundo número: "))
num3 =float (input("Digite o terceiro número: "))
num4 =float (input("Ditete o quarto número: "))
num5 =float (input("Ditete o cinco número: "))
lista = [num1,num2,num3,num4,num5]
print(lista)
if num1 > num2 and num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
    print("O maior número é:", num1)
elif num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:
    print("O maior número é:", num2)
elif num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5:
    print("O maior número é:", num3)
elif num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5:
    print("O maior número é:", num4)
elif num5 > num1 and num5 > num2 and num5 > num3 and num5 and num5 > num4:
    print("O maior número é:", num5)
else:
    print("Os números são iguais")

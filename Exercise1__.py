tabuada = 1
print("Bem vindo ao sistema de tabuada de multiplicação onde o usuario digita e calcula")
while tabuada<=10:
    num = int(input("Digite um número para calcular a tabuada: "))
    result = num * tabuada
    print(f"A tabuada de {num} é: {num} x {tabuada}")
    print(f"{num} * {tabuada}= {result}")
    tabuada += 1
flag = 1
while flag == 1:
    print("Olá seja bem vindo ao sistema de cálculo de área e valor de terreno")
    comprimento = float(input("Escolha um valor para o comprimento :"))
    while comprimento <= 0:
        print("Comprimento invalido, por favor escolha um valor maior que zero")
        comprimento = float(input("Escolha um valor para o comprimento :"))
    largura = float (input("Escolha um valor para a largura :"))
    while largura <= 0:
        print("Largura invalida, por favor escolha um valor maior que zero")
        largura = float(input("Escolha um valor para a largura :"))
        print("Obrigado por usar o sistema de cálculo de área e valor de terreno")
    area = comprimento * largura
    print("O valor da área do terreno é : ", area)
    while area <= 0:
        print("Área invalida, por favor escolha um valor maior que zero")
        area = comprimento * largura
        print("Obrigado por usar o sistema de cálculo de área e valor de terreno")
    valor = float(input("Escolha um valor em reais "))
    while valor <= 0:
        print("Valor invalido, por favor escolha um valor maior que zero")
        valor = float(input("Escolha um valor em reais "))
        print("O valor do terreno é : ", valor)
        print("Obrigado por usar o sistema de cálculo de área e valor de terreno")
    preco = area * (valor)
    while preco <= 0:
        print("Preço invalido, por favor escolha um valor maior que zero")
        preco = area * (valor)
        print("Obrigado por usar o sistema de cálculo de área e valor de terreno")
        print("O valor do terreno é : ", preco)
    print("O valor do terreno é : ", preco,"reais")
    if preco <= 50000:
        desconto = preco * 0.95
        print("O valor do desconto em 5 por cento de desconto ",desconto,"em reais")
    if preco > 50000 and preco <=100000:
        desconto = preco * 0.90
        print("O valor do desconto em 10 por cento de desconto ",desconto)
    if preco > 100000:
        desconto = preco * 0.85
        print("O valor do desconto em 15 por cento de desconto ",desconto)
    print("Você quer fazer de novo")
    flag = int(input("1 para sim e 2 para não "))

print('SAINDOO...')
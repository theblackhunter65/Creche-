print('Bem Vindo ao sistema de conversor de temperatura Celsius ou Fahrenheit')
while True:
    print('Escolha uma opção:')
    print('1 - Converter de Celsius para Fahrenheit')
    print('2 - Converter de Fahrenheit para Celsius')
    print('3 - Sair do sistema')
    opcao = input('Digite a opção escolhida: ')
    if opcao == '1':
        celsius = float(input("Digite a temperatuara em Celsius"))
        fahrenheit = (celsius * 9/5) + 32
        print(f'{celsius}°C é igual a {fahrenheit}°F')
    elif opcao == '2':
        fahrenheit = float(input("Digite a temperatura em Fahrenheit"))
        celsius = (fahrenheit / 32) *5/9
        print(f'{fahrenheit}°F é igual a {celsius}°C')
    elif opcao == '3':
        print('Obrigado por usar o sistema de conversor de temperatura')
        break
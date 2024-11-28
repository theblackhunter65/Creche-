print("Bem ao sistema de contagem de  vogais ")
name = input("Digite um nome ")
name = name.lower()
contagem = 0
for letra in name:
    if letra in 'aeiou':
        contagem += 1
        print(f"O nome {name} tem {contagem} vogais")
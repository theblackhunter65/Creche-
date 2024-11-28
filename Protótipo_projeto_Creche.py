# Sistema de Login e Senha
usuarios = {"admin": "1234"}  # Dicionário com usuários e senhas

# Armazenamento de dados
cadastros_professores = []
cadastros_alunos = []
relatorio_administrativo = {}
relatorio_academico = {}

# Função de Login
def login():
    print("=== Sistema de Login ===")
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    if usuario in usuarios and usuarios[usuario] == senha:
        print("Login realizado com sucesso!\n")
        return True
    else:
        print("Usuário ou senha incorretos! Tente novamente.\n")
        return False

# Função para cadastro de professor
def cadastrar_professor():
    print("Cadastro de Professor")
    nome = input("Nome do Professor: ")
    idade = int(input("Idade do Professor: "))
    email = input("Email do Professor: ")
    salario = input("Salário do Professor: ")
    telefone = input("Telefone do Professor: ")
    cadastros_professores.append({
        "nome": nome,
        "idade": idade,
        "email": email,
        "salario": salario,
        "telefone": telefone
    })
    print("Professor cadastrado com sucesso!\n")

# Função para cadastro de aluno
def cadastrar_aluno():
    print("Cadastro de Aluno")
    nome = input("Nome do Aluno: ")
    idade = int(input("Idade do Aluno: "))
    matricula = int(input("Matrícula do Aluno: "))
    email = input("Email do Aluno: ")
    sala = input("Número e letra da sala: ")
    cadastros_alunos.append({
        "nome": nome,
        "idade": idade,
        "matricula": matricula,
        "email": email,
        "sala": sala
    })
    print("Aluno cadastrado com sucesso!\n")

# Função para cadastro de relatório administrativo
def cadastrar_relatorio_administrativo():
    print("Cadastro de Relatório Administrativo")
    nome_creche = input("Nome da Creche Rural: ")
    diretor = input("Nome do Diretor: ")
    transporte = input("Nome do Transporte: ")
    valor = input("Valor da Creche: ")
    qtd_criancas = input("Quantidade de crianças: ")
    frequencia = input("Frequência dos alunos: ")
    manutencao = input("Custo de Manutenções: ")
    relatorio_administrativo.update({
        "nome_creche": nome_creche,
        "diretor": diretor,
        "transporte": transporte,
        "valor": valor,
        "qtd_criancas": qtd_criancas,
        "frequencia": frequencia,
        "manutencao": manutencao
    })
    print("Relatório administrativo cadastrado com sucesso!\n")

# Função para cadastro de relatório acadêmico
def cadastrar_relatorio_academico():
    print("Cadastro de Relatório Acadêmico")
    nome_instituicao = input("Nome da Creche: ")
    recurso = input("Quantidade de recurso limitado: ")
    relatorio_academico.update({
        "nome_instituicao": nome_instituicao,
        "recurso": recurso
    })
    print("Relatório acadêmico cadastrado com sucesso!\n")

# Loop para tentativa de login até sucesso
while not login():
    print("Tente novamente.")

# Menu principal
while True:
    print("MENU:")
    print("Digite a opção desejada:")
    print("1 - Cadastro")
    print("2 - Relatórios")
    print("3 - Sair")
    opc = int(input("Escolha uma opção:"))
    
    if opc == 1:
        while True:
            print("Realizar cadastro")
            print("1 - Professor") 
            print("2 - Alunos")
            print("3 - Voltar")
            opc1 = int(input("Qual a sua opção: "))

            if opc1 == 1:
                cadastrar_professor()
            elif opc1 == 2:
                cadastrar_aluno()
            elif opc1 == 3:
                print("Voltando ao menu principal...\n")
                break
            else:
                print("Opção inválida!")

    elif opc == 2:
        while True:
            print("Apresentar relatórios")
            print("1 - Administrativo")
            print("2 - Acadêmico")
            print("3 - Voltar")
            opc2 = int(input("Qual a sua opção: "))

            if opc2 == 1:
                cadastrar_relatorio_administrativo()
            elif opc2 == 2:
                cadastrar_relatorio_academico()
            elif opc2 == 3:
                print("Voltando ao menu principal...\n")
                break
            else:
                print("Opção inválida!")

    elif opc == 3:
        print("Saindo... Até logo!")
        break
    else:
        print("Opção inválida! Tente novamente.")

# Sistema de Login e Gerenciamento da Creche

# Usuários cadastrados
os_usuarios = {"admin": "1234"}

# Armazenamento de dados
cadastros_professores = []
cadastros_alunos = []
cadastro_do_diretor = []
cadastro_do_secretario = []
cadastro_do_zelador = []
relatorio_administrativo = {}
relatorio_academico = {}

# Funções auxiliares de validação
def validar_inteiro(valor):
    try:
        return int(valor)
    except ValueError:
        return None

def validar_float(valor):
    try:
        return float(valor)
    except ValueError:
        return None

def validar_email(email):
    return "@" in email and "." in email

def validar_entrada(mensagem, tipo):
    while True:
        entrada = input(mensagem)
        if tipo == "int" and entrada.isdigit():
            return int(entrada)
        elif tipo == "float":
            valor = validar_float(entrada)
            if valor is not None:
                return valor
        elif tipo == "email" and validar_email(entrada):
            return entrada
        elif tipo == "nome" and entrada.isalpha():
            return entrada
        elif tipo == "telefone" and entrada.isdigit() and len(entrada) >= 8:
            return entrada
        elif tipo == "cpf" and entrada.isdigit() and len(entrada) == 11:
            return entrada
        print("Entrada inválida. Tente novamente.")

# Função de login
def login():
    print("----===>>Sistema de Login <<===---")
    usuario = input("Digite o seu usuário: ")
    senha = input("Digite a sua senha: ")
    if usuario in os_usuarios and os_usuarios[usuario] == senha:
        print("Bem-vindo ao sistema da creche!")
        return True
    else:
        print("Usuário ou senha inválidos.")
        return False

# Funções de cadastro
def cadastrar_diretor():
    print("\nCadastro do Diretor")
    nome = validar_entrada("Digite o nome do diretor: ", "nome")
    idade = validar_entrada("Digite a idade do diretor: ", "int")
    telefone = validar_entrada("Digite o telefone do diretor: ", "telefone")
    email = validar_entrada("Digite o e-mail do diretor: ", "email")
    cpf = validar_entrada("Digite o CPF do diretor (11 dígitos): ", "cpf")
    cadastro_do_diretor.append({
        "nome": nome,
        "idade": idade,
        "telefone": telefone,
        "email": email,
        "cpf": cpf
    })
    print("Diretor cadastrado com sucesso!")

def cadastrar_professor():
    print("\nCadastro de Professor")
    nome = validar_entrada("Digite o nome do professor: ", "nome")
    idade = validar_entrada("Digite a idade do professor: ", "int")
    salario = validar_entrada("Digite o salário do professor: ", "float")
    telefone = validar_entrada("Digite o telefone do professor: ", "telefone")
    email = validar_entrada("Digite o e-mail do professor: ", "email")
    cpf = validar_entrada("Digite o CPF do professor (11 dígitos): ", "cpf")
    cadastros_professores.append({
        "nome": nome,
        "idade": idade,
        "salario": salario,
        "telefone": telefone,
        "email": email,
        "cpf": cpf
    })
    print("Professor cadastrado com sucesso!")

def cadastrar_aluno():
    print("\nCadastro de Aluno")
    nome = validar_entrada("Digite o nome do aluno: ", "nome")
    idade = validar_entrada("Digite a idade do aluno: ", "int")
    telefone = validar_entrada("Digite o telefone do aluno: ", "telefone")
    email = validar_entrada("Digite o e-mail do aluno: ", "email")
    cpf = validar_entrada("Digite o CPF do aluno (11 dígitos): ", "cpf")
    cadastros_alunos.append({
        "nome": nome,
        "idade": idade,
        "telefone": telefone,
        "email": email,
        "cpf": cpf
    })
    print("Aluno cadastrado com sucesso!")

# Função de relatórios
def cadastrar_relatorio_administrativo():
    print("\nCadastro do Relatório Administrativo")
    nome_creche = validar_entrada("Digite o nome da creche: ", "nome")
    endereco = input("Digite o endereço da creche: ")  # Pode ser texto alfanumérico
    telefone = validar_entrada("Digite o telefone da creche: ", "telefone")
    email = validar_entrada("Digite o e-mail da creche: ", "email")
    despesas = validar_entrada("Digite o valor das despesas da creche: ", "float")
    relatorio_administrativo.update({
        "nome_creche": nome_creche,
        "endereco": endereco,
        "telefone": telefone,
        "email": email,
        "despesas": despesas
    })
    print("Relatório administrativo cadastrado com sucesso!")

def cadastrar_relatorio_academico():
    print("\nCadastro do Relatório Acadêmico")
    nome_aluno = validar_entrada("Digite o nome do aluno: ", "nome")
    idade_aluno = validar_entrada("Digite a idade do aluno: ", "int")
    numero_sala = validar_entrada("Digite o número da sala: ", "int")
    turma = validar_entrada("Digite o nome da turma: ", "nome")
    relatorio_academico.update({
        "nome_aluno": nome_aluno,
        "idade_aluno": idade_aluno,
        "numero_sala": numero_sala,
        "turma": turma
    })
    print("Relatório acadêmico cadastrado com sucesso!")

# Menu principal
while not login():
    print("Tente novamente.")

while True:
    print("\n=======>> Menu <<=======")
    print("1 - Cadastro")
    print("2 - Relatórios")
    print("3 - Sair")
    opc = validar_entrada("Escolha uma opção: ", "int")

    if opc == 1:
        print("\n=======>> Cadastro <<=======")
        print("1 - Cadastro de Diretor")
        print("2 - Cadastro de Professor")
        print("3 - Cadastro de Aluno")
        print("4 - Voltar")
        opc1 = validar_entrada("Escolha uma opção: ", "int")
        if opc1 == 1:
            cadastrar_diretor()
        elif opc1 == 2:
            cadastrar_professor()
        elif opc1 == 3:
            cadastrar_aluno()
        elif opc1 == 4:
            continue
        else:
            print("Opção inválida.")

    elif opc == 2:
        print("\n=======>> Relatórios <<=======")
        print("1 - Relatório Administrativo")
        print("2 - Relatório Acadêmico")
        print("3 - Voltar")
        opc2 = validar_entrada("Escolha uma opção: ", "int")
        if opc2 == 1:
            cadastrar_relatorio_administrativo()
        elif opc2 == 2:
            cadastrar_relatorio_academico()
        elif opc2 == 3:
            continue
        else:
            print("Opção inválida.")

    elif opc == 3:
        print("Saindo... Até logo!")
        break

    else:
        print("Opção inválida!")

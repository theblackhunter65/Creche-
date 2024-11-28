f1=1
while(f1==1):
    print("MENU:")
    print("Digite a opção desejada:")
    print("1 - Cadastro")
    print("2 - Relatórios")
    print("3 - Sair")
    opc=int(input("Escolha uma opção:"))
    if opc==1:
        f3 = 1
        while f3 == 1:
            print("Realizar cadastro")
            print("1 - Professor") 
            print("2 - Alunos")
            print("3 - Voltar")

            opc1=int(input("Qual a sua opcão :"))

            if(opc1==1):
                print("Realizar cadastro do professor")
                nome_professor=input("Nome do Professor: ")
                idade_professor=int(input("Idade do Professor: "))
                email_do_professor = input("Coloque o email do professor ? :")
                print("Email do Professor: ", email_do_professor)
                salario_professor=input("Salário do Professor: ")
                telefone_do_professor = int(input("Telefone do professor:"))
                print("Professor cadastrado com sucesso!")
            elif (opc1==2):
                print("Realizar cadastro do aluno")
                nome_aluno = input("Nome do Aluno: ")
                idade_aluno = int(input("Idade do Aluno: "))
                matricula_aluno = int(input("Matrícula do Aluno: "))
                email_do_aluno = input("Coloque o email do aluno ? :")
                numero_da_sala = input("Qual é o número da sala e letra da sala de aula ")
                print("Aluno cadastrado com sucesso!")
            elif (opc1==3):
                print("3- Voltar")
                f3 = 0
            else:
                print("Saindo....")
    elif opc ==2:
       f3 = 1
    while f3 == 1:
            print("Aprensentar relatórios")
            print("1-Administrativo")
            print("2-Acadêmico")
            print("3-Voltar")

            opc2=int(input("Qual a sua opção:"))

            if opc2 == 1:
                print("Relatório administrativo")
                nome_da_creche = input("Qual o nome da creche rural ? :")
                print("A nossa creche está localizada em Minas Gerais")
                nome_do_diretor = input("Qual o nome do diretor da creche rural ?")
                print("professores, auxiliares, cozinheiros,segurança")
                nome_do_transporte = input("Qual o nome da do transporte")
                print("Os nossos funcionários são excelentes e são bem capacitados")
                valor_da_creche_rural = input("O valor da creche")
                print("O valor da creche rural é de R$ ", valor_da_creche_rural)
                print("A visão da nossa creche é trazer uma segurança aos país que não podem cuidar das suas crianças por causa do trabalho.")
                quantidades_de_criancas_matriculadas = input("Quantas crianças tem na creche ?: ")
                print("A nossa creche tem ", quantidades_de_criancas_matriculadas)
                O_Numero_de_frequencia_das_criancas_matriculadas = input("A frequência dos alunos da creche rural é qual ? :")
                print("A frequência dos alunos da creche rural é de ",  O_Numero_de_frequencia_das_criancas_matriculadas)
                custo_de_reformas_das_manutencoes=input(" Qual é custo de reformas das manutenções da creche rural ? :")
                print("O custo de reformas das manutenções da creche rural é de R$")
                print("A nossa creche rural é uma das melhores da região ! ")
                print("Temos as melhores subvenções públicas, doações e mensalidades ")
                print("A nossa gestão financeira da creche é uma das melhores do estado de Minas Gerais")
            elif opc2 == 2:
                print("Relatório acadêmico")
                nome_da_instituicao = input("Nome da Creche ?:")
                print(f"A creche {nome_da_instituicao} está localizada na área rural de Minas Gerais.")
                print("A nossa creche rural tem uma das melhores notas de aprovação da região!")
                print("Nossa preparação  para a vida rural é formação pode incluir aspectos práticos, como noções de agricultura e sustentabilidade, preparando as crianças para a realidade do campo.")
                recurso_limitado = input("Digite  a quantidade de recurso limitado da creche:")
                print("A nossa creche rural tem um recurso limitado de R$ ", recurso_limitado)
                print("Recursos limitados: Pode haver falta de professores especializados ou materiais pedagógicos, o que exige soluções criativas para oferecer uma educação de qualidade.")
                print("Soluções apoio da prefeitura")
            elif opc2 == 3:
                print("3- Voltar")
                f3 =0
            elif opc == 3:  # Sair do programa
                print("Saindo... Até logo!")
                f1 = 0

else:
    print("Opção inválida! Tente novamente.")
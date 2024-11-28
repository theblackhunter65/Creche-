import mysql.connector
from tkinter import *
from tkinter import messagebox
from fpdf import FPDF
from datetime import datetime

def connectar_banco():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="DAVI3592043&%3/",
            database="creche"
            )
    except mysql.connector.Error as err:
        messagebox.showerror("Erro de Conexão", f"Erro: {err}")
        return None

db = connectar_banco()
if db is None:
    exit()

cursor = db.cursor()

def criar_tabelas():
    cursor.execute("""
    Create table if  NOT EXISTS creche_info(
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome Varchar(100) NOT NULL,
        rua VARCHAR(100) NOT NULL,
        numero VARCHAR(10) NOT NULL,
        bairro VARCHAR(100) NOT NULL,
        cidade VARCHAR(100) NOT NULL,
        estado VARCHAR(100) NOT NULL,
        cep VARCHAR(10) NOT NULL   
    );             
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id_aluno INT PRIMARY KEY AUTO_INCREMENT,
        nome VARCHAR(100),
        registro VARCHAR(15) UNIQUE NOT NULL,
        cpf VARCHAR(14) UNIQUE NOT NULL,
        idade INT,
        telefone_dos_responsaveis VARCHAR(15),
        email VARCHAR(100),
        email_validado BOOLEAN DEFAULT 0,
        senha VARCHAR(100),
        senha_validada BOOLEAN DEFAULT 0
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS professores (
    id_professor INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    idade INT,
    registro VARCHAR(15),
    cpf VARCHAR(14),
    id_endereco INT,
    id_sala INT,
    email VARCHAR(100) UNIQUE NOT NULL,
    email_validado BOOLEAN DEFAULT 0,
    telefone VARCHAR(14),
    salario DECIMAL(10, 3) NOT NULL,
    senha_validada BOOLEAN DEFAULT 0
    );
    """)

    criar_tabelas()

def obter_info_creche(tipo):
    cursor.execute(f"SELECT nome,rua,numero,bairro,cidade,estado,cep      FROM creche_info LIMIT 1")
    return cursor.fetchone()

def validar_cpf(tipo):
    cpf = entry_cpf.get() if tipo == 'aluno' else entry_cpf_prof.get()
    tabela = 'alunos' if tipo == 'aluno' else 'professores'

    cursor.execute(f"SELECT cpf FROM {tabela} WHERE cpf = %", (cpf))
    resultado = cursor.fetchone()

    if len(cpf) !=14 or not cpf.replace('.','').replace('-','').isdigit   ():
        messagebox.showerror("ERRO", "CPF invalido")
        return False
    
    elif resultado:
        messagebox.showerror("ERRO", "CPF ja cadastrado")
        return False
    else:
        messagebox.showinfo()
        return True

def validar_email(tipo):
    email = entry_email.get() if tipo == 'aluno 'else entry_email.get    ()
    tabela = 'alunos' if tipo == 'aluno' else 'professores'

    if "@" not in email or "." not in email:
        messagebox.showerror("ERRO", "E-mail inváido")
        return False
        
    cursor.execute(f"Select email FROM {tabela} Where email = %s",(email,))
    resultado = cursor.fetchone()

    if resultado:
        messagebox.showerror("ERRO", "E-mail já cadastrado")
        return False
    else:
        messagebox.showinfo("Sucesso", "E-mail válido")
        return True

def validar_nome(tipo):
    nome = entry_nome.get() if tipo == 'aluno' else entry_nome_prof.get()

    if len(nome) < 3 or len(nome) >50:
        messagebox.showerror("ERRO", "Nome inválido")
        return False

    tabela = 'alunos' if tipo == 'aluno' else  entry_idade_prof.get      ()
    cursor.execute(f"SELECT nome FROM {tabela} WHERE nome = %s", (nome,))
    resultado = cursor.fetchone()
    if resultado:
        messagebox.showerror("ERRO", "Nome já cadastrado")
        return False
    else:
        messagebox.showinfo("Sucesso", "Nome válido")
        return True

def validar_idade(tipo):
    idade = entry_idade.get() if tipo == 'aluno' else entry_idade_prof.get()
    if not idade.isdigit() and (0 < int(idade) < 100):
        messagebox.showerror("ERRO", "Idade inválida")  
        return False
    return True

def cadastrar(tipo):
    if validar_cpf(tipo) and validar_email(tipo) and validar_nome(tipo) and validar_idade(tipo):
        nome = entry_nome.get() if tipo == 'aluno' else entry_nome_prof.get()
        email = entry_email.get() if tipo == 'aluno' else entry_email_prof.get()
        idade = entry_idade.get() if tipo == 'aluno' else (entry_idade_prof())
        cpf = entry_cpf.get() if tipo == 'aluno' else entry_cpf_prof()
        registro = entry_registro.get() if tipo == 'aluno' else (entry_registro_prof.get())
        tabela = 'alunos' if tipo == 'aluno' else 'professores'

        # Insere no Banco
        if tipo == 'professor':
            salario = float(entry_salario.get()) if entry_salario.get() else 0.0
            cursor.execute(f"INSERT INTO {tabela} nome (nome, email, cpf, idade, registro, salario ) VALUES (%s, %s,%s, %s, %s, %s)",
                           (nome, email, cpf, idade, registro, salario))
        else:
            cursor.execute(f"INSERT INTO {tabela} (nome, email, cpf, idade,registro,telefone_dos_responsaveis) VALUES (%s, %s, %s, %s, %s)",
                               (nome, email, cpf, idade, registro))
        db.commit()
        messagebox.showinfo("Sucesso", f"{tipo.capitalize()}Cadastro realizado com sucesso")
        limpar_campos(tipo)

def limpar_campos(tipo):
    if tipo == 'aluno':
        entry_nome.delete(0,END)
        entry_email.delete(0,END)
        entry_cpf.delete(0,END)
        entry_idade.delete(0,END)
        entry_registro.delete(0, END)
        entry_telefone.delete(0, END)
    else:
        entry_nome_prof.delete(0,END)
        entry_email_prof.delete(0,END)
        entry_cpf_prof.delete(0,END)
        entry_idade_prof.delete(0,END)
        entry_registro_prof.delete(0, END)
        entry_telefone.delete(0,END)

def gerar_pdf():
    # Gera o PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 15)
    pdf.cell(200, 10, txt = "Relatório de Alunos", ln = True, align = 'C')
    pdf.ln(10)

    # Adicione as irformações da creche no PDF
    creche_info = obter_info_creche()
    if creche_info:
       if creche_info:
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Informações da Creche:", ln=True, align='L')
        pdf.cell(200, 10, txt=f"Nome: {creche_info[0]}", ln=True)
        pdf.cell(200, 10, txt=f"Endereço: {creche_info[1]}, {creche_info[2]}", ln=True)
        pdf.cell(200, 10, txt=f"Bairro: {creche_info[3]}, Cidade: {creche_info[4]}, Estado: {creche_info[5]}, CEP: {creche_info[6]}", ln=True)
        pdf.ln(10)
    
    # Dados dos alunos
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Alunos:", ln=True, align='L')
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    for aluno in alunos:
        pdf.cell(200, 10, txt=f"ID: {aluno[0]}, Nome: {aluno[1]}, Registro: {aluno[2]}, CPF: {aluno[3]}, Idade: {aluno[4]}, Email: {aluno[6]}, Telefone dos Responsáveis: {aluno[5]}", ln=True)
    
    pdf.ln(10)

    # Dados dos professores
    pdf.cell(200, 10, txt="Professores:", ln=True, align='L')
    cursor.execute("SELECT * FROM professores")
    professores = cursor.fetchall()
    for professor in professores:
        pdf.cell(200, 10, txt=f"ID: {professor[0]}, Nome: {professor[1]}, Registro: {professor[3]}, CPF: {professor[4]}, Idade: {professor[2]}, Email: {professor[5]}, Salário: R${professor[8]}", ln=True)
    
    pdf.output("Relatorio.pdf")
    messagebox.showinfo("Sucesso", "PDF gerado com sucesso!")

# Interface Gráfica
root = Tk()
root.title("Sistema de Cadastro")

# Frame para Alunos
frame_aluno = LabelFrame(root, text="Cadastro de Alunos", padx=10, pady=10)
frame_aluno.grid(row=0, column=0, padx=10, pady=10)

Label(frame_aluno, text="Nome:").grid(row=0, column=0)
entry_nome = Entry(frame_aluno)
entry_nome.grid(row=0, column=1)

Label(frame_aluno, text="Email:").grid(row=1, column=0)
entry_email = Entry(frame_aluno)
entry_email.grid(row=1, column=1)

Label(frame_aluno, text="Idade:").grid(row=2, column=0)
entry_idade = Entry(frame_aluno)
entry_idade.grid(row=2, column=1)

Label(frame_aluno, text="CPF:").grid(row=3, column=0)
entry_cpf = Entry(frame_aluno)
entry_cpf.grid(row=3, column=1)

Label(frame_aluno, text="Registro:").grid(row=4, column=0)
entry_registro = Entry(frame_aluno)
entry_registro.grid(row=4, column=1)

Label(frame_aluno, text="Telefone dos Responsáveis:").grid(row=5, column=0)
entry_telefone = Entry(frame_aluno)
entry_telefone.grid(row=5, column=1)

Button(frame_aluno, text="Cadastrar Aluno", command=lambda: cadastrar("aluno")).grid(row=6, columnspan=2, pady=10)

# Frame para Professores
frame_professor = LabelFrame(root, text="Cadastro de Professores", padx=10, pady=10)
frame_professor.grid(row=1, column=0, padx=10, pady=10)

Label(frame_professor, text="Nome:").grid(row=0, column=0)
entry_nome_prof = Entry(frame_professor)
entry_nome_prof.grid(row=0, column=1)

Label(frame_professor, text="Email:").grid(row=1, column=0)
entry_email_prof = Entry(frame_professor)
entry_email_prof.grid(row=1, column=1)

Label(frame_professor, text="Idade:").grid(row=2, column=0)
entry_idade_prof = Entry(frame_professor)
entry_idade_prof.grid(row=2, column=1)

Label(frame_professor, text="CPF:").grid(row=3, column=0)
entry_cpf_prof = Entry(frame_professor)
entry_cpf_prof.grid(row=3, column=1)

Label(frame_professor, text="Registro:").grid(row=4, column=0)
entry_registro_prof = Entry(frame_professor)
entry_registro_prof.grid(row=4, column=1)

Label(frame_professor, text="Salário:").grid(row=5, column=0)
entry_salario = Entry(frame_professor)
entry_salario.grid(row=5, column=1)

Button(frame_professor, text="Cadastrar Professor", command=lambda: cadastrar("professor")).grid(row=6, columnspan=2, pady=10)

# Botão para gerar PDF
Button(root, text="Gerar Relatório PDF", command=gerar_pdf).grid(row=2, column=0, pady=10)

root.mainloop()
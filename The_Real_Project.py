# Sistema de gerenciamento de creche
import mysql.connector       # Para conexão com MySQL/MariaDB
from tkinter import Tk, Label, Entry, Button, LabelFrame  # GUI básica
from tkinter import messagebox  # Janelas de alerta/mensagens
from fpdf import FPDF       # Gerar PDFs 
import re                    # Expressões regulares (validação de dados)
import os                    # Operações de sistema (arquivos, pastas)

def connectar_banco():
    try:
        # Usar variável de ambiente para a senha do MySQL
        senha = os.getenv("MYSQL_PASSWORD", "DAVI3592043&%3/")  # Valor padrão para testes
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password=senha,
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
    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS creche_info (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
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
        db.commit()
    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Falha ao criar tabelas: {err}")

criar_tabelas()

def obter_info_creche():
    try:
        cursor.execute("SELECT nome, rua, numero, bairro, cidade, estado, cep FROM creche_info LIMIT 1")
        return cursor.fetchone()
    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Falha ao obter informações da creche: {err}")
        return None

def formatar_cpf(event=None):
    cpf = entry_cpf.get().replace('.', '').replace('-', '')
    if cpf.isdigit():
        if len(cpf) > 11:
            cpf = cpf[:11]
        formatted = ''
        for i, char in enumerate(cpf):
            if i in [3, 6]:
                formatted += '.'
            elif i == 9:
                formatted += '-'
            formatted += char
        entry_cpf.delete(0, END)
        entry_cpf.insert(0, formatted)

def formatar_cpf_prof(event=None):
    cpf = entry_cpf_prof.get().replace('.', '').replace('-', '')
    if cpf.isdigit():
        if len(cpf) > 11:
            cpf = cpf[:11]
        formatted = ''
        for i, char in enumerate(cpf):
            if i in [3, 6]:
                formatted += '.'
            elif i == 9:
                formatted += '-'
            formatted += char
        entry_cpf_prof.delete(0, END)
        entry_cpf_prof.insert(0, formatted)

def formatar_telefone(event=None):
    telefone = entry_telefone.get().replace('(', '').replace(')', '').replace('-', '')
    if telefone.isdigit():
        if len(telefone) > 11:
            telefone = telefone[:11]
        formatted = ''
        for i, char in enumerate(telefone):
            if i == 0:
                formatted += '('
            elif i == 2:
                formatted += ')'
            elif i == 7:
                formatted += '-'
            formatted += char
        entry_telefone.delete(0, END)
        entry_telefone.insert(0, formatted)

def validar_cpf(tipo):
    cpf = entry_cpf.get() if tipo == 'aluno' else entry_cpf_prof.get()
    tabela = 'alunos' if tipo == 'aluno' else 'professores'

    if len(cpf) != 14 or not cpf.replace('.', '').replace('-', '').isdigit():
        messagebox.showerror("Erro", "CPF inválido")
        return False
    
    try:
        cursor.execute(f"SELECT cpf FROM {tabela} WHERE cpf = %s", (cpf,))
        if cursor.fetchone():
            messagebox.showerror("Erro", "CPF já cadastrado")
            return False
        return True
    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Falha ao validar CPF: {err}")
        return False

def validar_email(tipo):
    email = entry_email.get() if tipo == 'aluno' else entry_email_prof.get()
    tabela = 'alunos' if tipo == 'aluno' else 'professores'

    padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(padrao, email):
        messagebox.showerror("Erro", "E-mail inválido")
        return False
        
    try:
        cursor.execute(f"SELECT email FROM {tabela} WHERE email = %s", (email,))
        if cursor.fetchone():
            messagebox.showerror("Erro", "E-mail já cadastrado")
            return False
        return True
    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Falha ao validar e-mail: {err}")
        return False

def validar_nome(tipo):
    nome = entry_nome.get() if tipo == 'aluno' else entry_nome_prof.get()
    tabela = 'alunos' if tipo == 'aluno' else 'professores'

    if len(nome) < 3 or len(nome) > 50:
        messagebox.showerror("Erro", "Nome inválido")
        return False

    try:
        cursor.execute(f"SELECT nome FROM {tabela} WHERE nome = %s", (nome,))
        if cursor.fetchone():
            messagebox.showerror("Erro", "Nome já cadastrado")
            return False
        return True
    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Falha ao validar nome: {err}")
        return False

def validar_idade(tipo):
    idade = entry_idade.get() if tipo == 'aluno' else entry_idade_prof.get()
    if not idade.isdigit() or not (0 < int(idade) < 100):
        messagebox.showerror("Erro", "Idade inválida")  
        return False
    return True

def validar_registro(tipo):
    registro = entry_registro.get() if tipo == 'aluno' else entry_registro_prof.get()
    tabela = 'alunos' if tipo == 'aluno' else 'professores'

    if len(registro) < 5 or len(registro) > 15:
        messagebox.showerror("Erro", "Registro inválido (deve ter entre 5 e 15 caracteres)")
        return False

    try:
        cursor.execute(f"SELECT registro FROM {tabela} WHERE registro = %s", (registro,))
        if cursor.fetchone():
            messagebox.showerror("Erro", "Registro já cadastrado")
            return False
        return True
    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Falha ao validar registro: {err}")
        return False

def validar_telefone():
    telefone = entry_telefone.get()
    if len(telefone) != 14 or not telefone.replace('(', '').replace(')', '').replace('-', '').isdigit():
        messagebox.showerror("Erro", "Telefone inválido (formato: (XX)XXXXX-XXXX)")
        return False
    return True

def validar_salario():
    salario = entry_salario.get()
    try:
        salario = float(salario) if salario else 0.0
        if salario < 0:
            messagebox.showerror("Erro", "Salário não pode ser negativo")
            return False
        return True
    except ValueError:
        messagebox.showerror("Erro", "Salário inválido (deve ser um número)")
        return False

def cadastrar(tipo):
    # Validações específicas por tipo
    if tipo == 'aluno':
        if not (validar_cpf(tipo) and validar_email(tipo) and validar_nome(tipo) and validar_idade(tipo) and validar_registro(tipo) and validar_telefone()):
            return
    else:
        if not (validar_cpf(tipo) and validar_email(tipo) and validar_nome(tipo) and validar_idade(tipo) and validar_registro(tipo) and validar_salario()):
            return

    nome = entry_nome.get() if tipo == 'aluno' else entry_nome_prof.get()
    email = entry_email.get() if tipo == 'aluno' else entry_email_prof.get()
    idade = entry_idade.get() if tipo == 'aluno' else entry_idade_prof.get()
    cpf = entry_cpf.get() if tipo == 'aluno' else entry_cpf_prof.get()
    registro = entry_registro.get() if tipo == 'aluno' else entry_registro_prof.get()
    tabela = 'alunos' if tipo == 'aluno' else 'professores'

    try:
        if tipo == 'professor':
            salario = float(entry_salario.get()) if entry_salario.get() else 0.0
            cursor.execute(
                f"INSERT INTO {tabela} (nome, email, cpf, idade, registro, salario) VALUES (%s, %s, %s, %s, %s, %s)",
                (nome, email, cpf, idade, registro, salario)
            )
        else:
            telefone = entry_telefone.get()
            cursor.execute(
                f"INSERT INTO {tabela} (nome, email, cpf, idade, registro, telefone_dos_responsaveis) VALUES (%s, %s, %s, %s, %s, %s)",
                (nome, email, cpf, idade, telefone)
            )
        db.commit()
        messagebox.showinfo("Sucesso", f"{tipo.capitalize()} cadastrado com sucesso")
        limpar_campos(tipo)
    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Falha ao cadastrar: {err}")

def limpar_campos(tipo):
    if tipo == 'aluno':
        entry_nome.delete(0, END)
        entry_email.delete(0, END)
        entry_cpf.delete(0, END)
        entry_idade.delete(0, END)
        entry_registro.delete(0, END)
        entry_telefone.delete(0, END)
    else:
        entry_nome_prof.delete(0, END)
        entry_email_prof.delete(0, END)
        entry_cpf_prof.delete(0, END)
        entry_idade_prof.delete(0, END)
        entry_registro_prof.delete(0, END)
        entry_salario.delete(0, END)

def gerar_pdf():
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=15)
        pdf.cell(200, 10, txt="Relatório de Alunos", ln=True, align='C')
        pdf.ln(10)

        creche_info = obter_info_creche()
        if creche_info:
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt="Informações da Creche:", ln=True, align='L')
            pdf.cell(200, 10, txt=f"Nome: {creche_info[0]}", ln=True)
            pdf.cell(200, 10, txt=f"Endereço: {creche_info[1]}, {creche_info[2]}", ln=True)
            pdf.cell(200, 10, txt=f"Bairro: {creche_info[3]}, Cidade: {creche_info[4]}, Estado: {creche_info[5]}, CEP: {creche_info[6]}", ln=True)
            pdf.ln(10)
        
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Alunos:", ln=True, align='L')
        cursor.execute("SELECT * FROM alunos")
        for aluno in cursor.fetchall():
            pdf.cell(200, 10, txt=f"ID: {aluno[0]}, Nome: {aluno[1]}, Registro: {aluno[2]}, CPF: {aluno[3]}, Idade: {aluno[4]}, Email: {aluno[6]}, Telefone: {aluno[5]}", ln=True)
        
        pdf.ln(10)
        pdf.cell(200, 10, txt="Professores:", ln=True, align='L')
        cursor.execute("SELECT * FROM professores")
        for professor in cursor.fetchall():
            pdf.cell(200, 10, txt=f"ID: {professor[0]}, Nome: {professor[1]}, Registro: {professor[3]}, CPF: {professor[4]}, Idade: {professor[2]}, Email: {professor[7]}, Salário: R${professor[10]}", ln=True)
        
        pdf.output("Relatorio.pdf")
        messagebox.showinfo("Sucesso", "PDF gerado com sucesso!")
    except Exception as err:
        messagebox.showerror("Erro", f"Falha ao gerar PDF: {err}")

# Interface Gráfica
root = Tk()
root.title("Sistema de Cadastro")
root.geometry("600x700")
root.resizable(False, False)

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
entry_cpf.bind("<KeyRelease>", formatar_cpf)

Label(frame_aluno, text="Registro:").grid(row=4, column=0)
entry_registro = Entry(frame_aluno)
entry_registro.grid(row=4, column=1)

Label(frame_aluno, text="Telefone dos Responsáveis:").grid(row=5, column=0)
entry_telefone = Entry(frame_aluno)
entry_telefone.grid(row=5, column=1)
entry_telefone.bind("<KeyRelease>", formatar_telefone)

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
entry_cpf_prof.bind("<KeyRelease>", formatar_cpf_prof)

Label(frame_professor, text="Registro:").grid(row=4, column=0)
entry_registro_prof = Entry(frame_professor)
entry_registro_prof.grid(row=4, column=1)

Label(frame_professor, text="Salário:").grid(row=5, column=0)
entry_salario = Entry(frame_professor)
entry_salario.grid(row=5, column=1)

Button(frame_professor, text="Cadastrar Professor", command=lambda: cadastrar("professor")).grid(row=6, columnspan=2, pady=10)

# Botão para gerar PDF
Button(root, text="Gerar Relatório PDF", command=gerar_pdf).grid(row=2, column=0, pady=10)

# Fechar conexão ao encerrar
root.protocol("WM_DELETE_WINDOW", lambda: [db.close(), root.destroy()])

root.mainloop()

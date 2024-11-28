import mysql.connector
from tkinter import *
from tkinter import messagebox
from fpdf import FPDF
from datetime import datetime

# Conexão com o banco de dados 
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DAVI3592043&%3/",  # Insira sua senha correta aqui
    database="creche"
)

cursor = db.cursor()

# Funções de validação
def validar_cpf(tipo):
    cpf = entry_cpf.get() if tipo == 'aluno' else entry_cpf_prof.get()
    tabela = 'alunos' if tipo == 'aluno' else 'professores'
    
    cursor.execute(f"SELECT cpf FROM {tabela} WHERE cpf = %s", (cpf,))
    resultado = cursor.fetchone()

    if len(cpf) != 11 or not cpf.isdigit():
        messagebox.showerror("ERRO", "CPF inválido")
        return False
        
    elif resultado:
        messagebox.showerror("ERRO", "CPF já cadastrado")
        return False
    else:
        messagebox.showinfo("Sucesso", "CPF válido")
        return True

def validar_email(tipo):
    email = entry_email.get() if tipo == 'aluno' else entry_email_prof.get()
    tabela = 'alunos' if tipo == 'aluno' else 'professores'
    
    if "@" not in email or "." not in email:
        messagebox.showerror("ERRO", "E-mail inválido")
        return False

    cursor.execute(f"SELECT email FROM {tabela} WHERE email = %s", (email,))
    resultado = cursor.fetchone()
    
    if resultado:
        messagebox.showerror("ERRO", "E-mail já cadastrado")
        return False
    else:
        messagebox.showinfo("Sucesso", "E-mail válido")
        return True

def validar_nome(tipo):
    nome = entry_nome.get() if tipo == 'aluno' else entry_nome_prof.get()
    
    if len(nome) < 3 or len(nome) > 50:
        messagebox.showerror("ERRO", "Nome inválido")
        return False
    
    tabela = 'alunos' if tipo == 'aluno' else 'professores'
    cursor.execute(f"SELECT nome FROM {tabela} WHERE nome = %s", (nome,))
    resultado = cursor.fetchone()

    if resultado:
        messagebox.showerror("ERRO", "Nome já cadastrado")
        return False
    else:
        messagebox.showinfo("Sucesso", "Nome válido")
        return True

def validar_data(tipo):
    data = entry_data.get() if tipo == 'aluno' else entry_data_prof.get()
    try:
        datetime.strptime(data, "%d/%m/%Y")
        messagebox.showinfo("Sucesso", "Data Válida")
        return True
    except ValueError:
        messagebox.showerror("ERRO", "Data Inválida")
        return False

# Função para cadastrar no banco de dados
def cadastrar(tipo):
    if validar_cpf(tipo) and validar_email(tipo) and validar_nome(tipo) and validar_data(tipo):
        nome = entry_nome.get() if tipo == 'aluno' else entry_nome_prof.get()
        email = entry_email.get() if tipo == 'aluno' else entry_email_prof.get()
        data = entry_data.get() if tipo == 'aluno' else entry_data_prof.get()
        cpf = entry_cpf.get() if tipo == 'aluno' else entry_cpf_prof.get()
        salario = float(entry_salario.get()) if tipo == 'professor' and entry_salario.get() else 0.0
        tabela = 'alunos' if tipo == 'aluno' else 'professores'

        # Converte a data para o formato 'AAAA-MM-DD'
        data_formatada = datetime.strptime(data, "%d/%m/%Y").strftime("%Y-%m-%d")

        # Insere no banco com o salário, se for um professor
        if tipo == 'professor':
            cursor.execute(f"INSERT INTO {tabela} (nome, email, data_nascimento, cpf, salario) VALUES (%s, %s, %s, %s, %s)", 
                           (nome, email, data_formatada, cpf, salario))
        else:
            cursor.execute(f"INSERT INTO {tabela} (nome, email, data_nascimento, cpf) VALUES (%s, %s, %s, %s)", 
                           (nome, email, data_formatada, cpf))
        db.commit()
        messagebox.showinfo("Sucesso", f"{tipo.capitalize()} cadastrado com sucesso")
        limpar_campos(tipo)

def limpar_campos(tipo):
    if tipo == 'aluno':
        entry_nome.delete(0, END)
        entry_email.delete(0, END)
        entry_data.delete(0, END)
        entry_cpf.delete(0, END)
    else:
        entry_nome_prof.delete(0, END)
        entry_email_prof.delete(0, END)
        entry_data_prof.delete(0, END)
        entry_cpf_prof.delete(0, END)
        entry_salario.delete(0, END)

# Função para gerar o PDF
def gerar_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    pdf.cell(200, 10, txt="Relatório de Alunos e Professores", ln=True, align='C')
    pdf.ln(10)
    
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Alunos:", ln=True, align='L')
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    for aluno in alunos:
        pdf.cell(200, 10, txt=f"Nome: {aluno[1]}, Email: {aluno[2]}, CPF: {aluno[3]}", ln=True)
    pdf.ln(10)

    pdf.cell(200, 10, txt="Professores:", ln=True, align='L')
    cursor.execute("SELECT * FROM professores")
    professores = cursor.fetchall()
    for professor in professores:
        pdf.cell(200, 10, txt=f"Nome: {professor[1]}, Email: {professor[2]}, CPF: {professor[3]}", ln=True)
    
    pdf.output("relatorio.pdf")
    messagebox.showinfo("Sucesso", "Relatório gerado com sucesso")

# Interface gráfica
root = Tk()
root.title("Cadastro de Alunos e Professores")

# Interface para Alunos
Label(root, text="Cadastrar Aluno").grid(row=0, columnspan=2, pady=10)
Label(root, text="Nome:").grid(row=1, column=0)
entry_nome = Entry(root)
entry_nome.grid(row=1, column=1)

Label(root, text="CPF:").grid(row=2, column=0)
entry_cpf = Entry(root)
entry_cpf.grid(row=2, column=1)

Label(root, text="Email:").grid(row=3, column=0)
entry_email = Entry(root)
entry_email.grid(row=3, column=1)

Label(root, text="Data de Nascimento:").grid(row=4, column=0)
entry_data = Entry(root)
entry_data.grid(row=4, column=1)

Button(root, text="Cadastrar Aluno", command=lambda: cadastrar('aluno')).grid(row=5, column=0, columnspan=2, pady=10)

# Interface para Professores
Label(root, text="Cadastrar Professor").grid(row=6, columnspan=2, pady=10)
Label(root, text="Nome:").grid(row=7, column=0)
entry_nome_prof = Entry(root)
entry_nome_prof.grid(row=7, column=1)

Label(root, text="CPF:").grid(row=8, column=0)
entry_cpf_prof = Entry(root)
entry_cpf_prof.grid(row=8, column=1)

Label(root, text="Email:").grid(row=9, column=0)
entry_email_prof = Entry(root)
entry_email_prof.grid(row=9, column=1)

Label(root, text="Data de Nascimento:").grid(row=10, column=0)
entry_data_prof = Entry(root)
entry_data_prof.grid(row=10, column=1)

# Adiciona o campo Salário para professores
Label(root, text="Salário:").grid(row=11, column=0)
entry_salario = Entry(root)
entry_salario.grid(row=11, column=1)

Button(root, text="Cadastrar Professor", command=lambda: cadastrar('professor')).grid(row=12, column=0, columnspan=2, pady=10)

# Botão para gerar o PDF
Button(root, text="Gerar PDF", command=gerar_pdf).grid(row=13, column=0, columnspan=2, pady=10)

root.mainloop()

# Fechar a conexão ao finalizar
cursor.close()
db.close()
import mysql.connector  # Corrigido para importar o módulo correto
from tkinter import *
from tkinter import messagebox
from fpdf import FPDF
from datetime import datetime


# Conexão com o banco de dados
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DAVI3592043&%3/",
    database="creche"
)

cursor = db.cursor()

# Funções de validação
def validar_cpf(tipo):
    cpf = entry_cpf.get().replace('.', '').replace('-', '')
    if len(cpf) != 11 or not cpf.isdigit():
        messagebox.showerror("Erro", "CPF inválido")
        return False

    tabela = 'alunos' if tipo == 'aluno' else 'professores'
    cursor.execute(f"SELECT cpf FROM {tabela} WHERE cpf = %s", (cpf,))
    resultado = cursor.fetchone()

    if resultado:
        messagebox.showerror("Erro", "CPF já cadastrado")
        return False
    else:
        messagebox.showinfo("Sucesso", "CPF válido")
        return True

def validar_email(tipo):
    email = entry_email.get()
    if "@" not in email:
        messagebox.showerror("Erro", "Email inválido")
        return False

    tabela = 'alunos' if tipo == 'aluno' else 'professores'
    cursor.execute(f"SELECT email FROM {tabela} WHERE email = %s", (email,))
    resultado = cursor.fetchone()

    if resultado:
        messagebox.showerror("Erro", "E-mail já cadastrado")
        return False
    else:
        messagebox.showinfo("Sucesso", "E-mail válido")
        return True

def validar_nome(tipo):
    nome = entry_nome.get()
    if len(nome) < 3 or len(nome) > 50:
        messagebox.showerror("Erro", "Nome inválido")
        return False

    tabela = 'alunos' if tipo == 'aluno' else 'professores'
    cursor.execute(f"SELECT nome FROM {tabela} WHERE nome = %s", (nome,))
    resultado = cursor.fetchone()

    if resultado:
        messagebox.showerror("Erro", "Nome já cadastrado")
        return False
    else:
        messagebox.showinfo("Sucesso", "Nome válido")
        return True

def validar_data(tipo):
    data = entry_data.get()
    
    # Verifica se a data está no formato DD/MM/AAAA
    try:
        datetime.strptime(data, "%d/%m/%Y")  # Tenta converter a string em um objeto datetime
    except ValueError:
        messagebox.showerror("Erro", "Data inválida. Utilize o formato DD/MM/AAAA.")
        return False

    messagebox.showinfo("Sucesso", "Data de nascimento válida")
    return True

def cadastrar(tipo):
    if (validar_cpf(tipo) and validar_email(tipo) and validar_nome(tipo) and validar_data(tipo)):
        nome = entry_nome.get()
        cpf = entry_cpf.get().replace('.', '').replace('-', '')
        email = entry_email.get()
        data_nascimento = entry_data.get()  # Este campo pode ser ajustado para armazenar no banco se necessário

        tabela = 'alunos' if tipo == 'aluno' else 'professores'
        cursor.execute(f"INSERT INTO {tabela} (nome, cpf, email) VALUES (%s, %s, %s)", (nome, cpf, email))
        db.commit()
        messagebox.showinfo("Sucesso", f"{tipo.capitalize()} cadastrado com sucesso!")
        limpar_campos()

def limpar_campos():
    entry_nome.delete(0, END)
    entry_cpf.delete(0, END)
    entry_email.delete(0, END)
    entry_data.delete(0, END)

def gerar_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    cursor.execute("SELECT nome, cpf, email FROM alunos")
    alunos = cursor.fetchall()

    pdf.cell(200, 10, txt="Lista de Alunos", ln=True, align='C')
    pdf.ln(10)

    for aluno in alunos:
        pdf.cell(200, 10, txt=f"Nome: {aluno[0]}, CPF: {aluno[1]}, Email: {aluno[2]}", ln=True)

    cursor.execute("SELECT nome, cpf, email FROM professores")
    professores = cursor.fetchall()

    pdf.ln(10)
    pdf.cell(200, 10, txt="Lista de Professores", ln=True, align='C')
    pdf.ln(10)

    for professor in professores:
        pdf.cell(200, 10, txt=f"Nome: {professor[0]}, CPF: {professor[1]}, Email: {professor[2]}", ln=True)

    pdf.output("relatorio.pdf")
    messagebox.showinfo("Sucesso", "PDF gerado com sucesso!")

# Interface Gráfica
root = Tk()
root.title("Cadastro de Alunos e Professores")

# Labels e Entradas para Alunos
Label(root, text="Cadastro de Alunos").grid(row=0, column=0, columnspan=2)
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

Button(root, text="Cadastrar Aluno", command=lambda: cadastrar('aluno')).grid(row=5, column=0, columnspan=2)

# Labels e Entradas para Professores
Label(root, text="Cadastro de Professores").grid(row=6, column=0, columnspan=2)
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

Button(root, text="Cadastrar Professor", command=lambda: cadastrar('professor')).grid(row=11, column=0, columnspan=2)

# Botão para gerar o PDF
Button(root, text="Gerar Relatório PDF", command=gerar_pdf).grid(row=12, column=0, columnspan=2)

root.mainloop()

# Fechando a conexão ao finalizar
cursor.close()
db.close()

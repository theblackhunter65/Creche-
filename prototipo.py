import mysql.connector
from tkinter import *
from tkinter import messagebox
from fpdf import FPDF
from datetime import datetime

# Conexão com o banco de dados 
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DAVI3592043&%3/",  # Substitua pela sua senha
    database="creche"  # Certifique-se de que o banco de dados existe
)

cursor = db.cursor()

# Função para validar CPF
def validar_cpf(tipo):
    cpf = entry_cpf.get() if tipo == 'aluno' else entry_cpf_prof.get()
    tabela = 'alunos' if tipo == 'aluno' else 'professores'
    cursor.execute(f"SELECT cpf FROM {tabela} WHERE cpf = %s", (cpf,))
    resultado = cursor.fetchone()
    
    # Erro: CPF deve ter 11 dígitos e ser numérico
    if len(cpf) != 11 or not cpf.isdigit():
        messagebox.showerror("ERRO", "CPF inválido")
        return False
    
    # Erro: Se o CPF já existe, deve mostrar erro
    elif resultado:
        messagebox.showerror("ERRO", "CPF já cadastrado")
        return False
    else:
        messagebox.showinfo("Sucesso", "CPF válido")
        return True

# Função para validar e-mail
def validar_email(tipo):
    email = entry_email.get() if tipo == 'aluno' else entry_email_prof.get()
    tabela = 'alunos' if tipo == 'aluno' else 'professores'
    
    # Erro: Verificação básica de e-mail (só checa a presença de "@", não garante validade completa)
    if "@" not in email:
        messagebox.showerror("ERRO", "E-mail inválido")
        return False
    
    # Esqueceu-se de executar a query de validação antes do `fetchone()`
    cursor.execute(f"SELECT email FROM {tabela} WHERE email = %s", (email,))
    resultado = cursor.fetchone()
    
    if resultado:
        messagebox.showerror("ERRO", "E-mail já cadastrado")
        return False
    else:
        messagebox.showinfo("Sucesso", "E-mail válido")
        return True

# Função para validar nome
def validar_nome(tipo):
    nome = entry_nome.get() if tipo == 'aluno' else entry_nome_prof.get()
    
    # Erro: Nome deve ter entre 3 e 50 caracteres
    if len(nome) < 3 or len(nome) > 50:
        messagebox.showerror("ERRO", "Nome inválido")
        return False
    
    tabela = 'alunos' if tipo == 'aluno' else 'professores'
    
    # Erro de sintaxe: faltam parênteses ao final de `(nome,)`
    cursor.execute(f"SELECT nome FROM {tabela} WHERE nome = %s", (nome,))
    resultado = cursor.fetchone()
    
    if resultado:
        messagebox.showerror("ERRO", "Nome já cadastrado")
        return False
    else:
        messagebox.showinfo("Sucesso", "Nome válido")
        return True

# Função para validar data
def validar_data(tipo):
    data = entry_data.get() if tipo == 'aluno' else entry_data_prof.get()
    try:
        # Erro: `strftime` é usado para formatar uma data, não para análise; use `strptime`
        datetime.strptime(data, "%d/%m/%Y")
        messagebox.showinfo("Sucesso", "Data válida")
        return True
    except ValueError:
        messagebox.showerror("ERRO", "Data inválida")
        return False

# Função para cadastrar no banco de dados
def cadastrar(tipo):
    # Condicional para garantir que todos os campos estão válidos
    if validar_cpf(tipo) and validar_email(tipo) and validar_nome(tipo) and validar_data(tipo):
        nome = entry_nome.get() if tipo == 'aluno' else entry_nome_prof.get()
        email = entry_email.get() if tipo == 'aluno' else entry_email_prof.get()
        data = entry_data.get() if tipo == 'aluno' else entry_data_prof.get()
        cpf = entry_cpf.get() if tipo == 'aluno' else entry_cpf_prof.get()
        tabela = 'alunos' if tipo == 'aluno' else 'professores'
        
        # Erro: certifique-se de que os dados correspondem ao formato do banco de dados
        cursor.execute(f"INSERT INTO {tabela} (nome, email, data, cpf) VALUES (%s, %s, %s, %s)", (nome, email, data, cpf))
        db.commit()
        messagebox.showinfo("Sucesso", f"{tipo.capitalize()} cadastrado com sucesso")
        limpar_campos(tipo)

# Função para limpar campos de entrada
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

# Função para gerar o PDF com relatórios de alunos e professores
def gerar_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    pdf.cell(200, 10, txt="Relatório de Alunos e Professores", ln=True, align='C')
    pdf.ln(10)

    # Adicionar dados de alunos
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    for aluno in alunos:
        # Erro: certifique-se de que `aluno[1]` e `aluno[2]` correspondem a nome e e-mail
        pdf.cell(200, 10, txt=f"Nome: {aluno[1]}, Email: {aluno[2]}", ln=True)
    pdf.ln(10)

    # Adicionar dados de professores
    cursor.execute("SELECT nome, cpf, email FROM professores")
    professores = cursor.fetchall()
    for professor in professores:
        pdf.cell(200, 10, txt=f"Nome: {professor[0]}, CPF: {professor[1]}, Email: {professor[2]}", ln=True)

    pdf.output("relatorio.pdf")
    messagebox.showinfo("Sucesso", "Relatório gerado com sucesso")

# Interface gráfica
root = Tk()
root.title("Cadastro de Alunos e Professores")

# Interface para Alunos
Label(root, text="Cadastrar Aluno").grid(row=0, columnspan=2)
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

# Interface para Professores
Label(root, text="Cadastrar Professor").grid(row=6, columnspan=2)
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
Button(root, text="Gerar PDF", command=gerar_pdf).grid(row=12, column=0, columnspan=2)

root.mainloop()

# Fechar a conexão ao finalizar
cursor.close()
db.close()


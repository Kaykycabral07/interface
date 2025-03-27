import sqlite3
from tkinter import messagebox
import bcrypt
from utils import validar_email, validar_nome

def conexao_db():
    try:
        with sqlite3.connect("banco.db") as db:
            cursor = db.cursor()
            return db, cursor
    except Exception as erro:
        messagebox.showerror("ERRO", f"Erro ao conectar ao banco de dados: {erro}")
        return None, None
    
def criar_tabela():
    db, cursor = conexao_db()
    if cursor and db:
        cursor.execute("""CREATE TABLE IF NOT EXISTS registro(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL) """)
        db.commit()
       

def criar_tabela_formulario():
    db, cursor = conexao_db()
    if cursor and db:
        cursor.execute("""CREATE TABLE IF NOT EXISTS formulario(
            id INTEGER NOT NULL,
            sistema TEXT NOT NULL,
            linguagem TEXT NOT NULL,
            telefone TEXT NOT NULL,
            cor TEXT NOT NULL,
            bebida TEXT NOT NULL,
            FOREIGN KEY(id) REFERENCES registro(id))""")
        db.commit()
        



def validar_dados_registro(nome,email,senha,confirmar_senha):
    if senha != confirmar_senha:
        messagebox.showerror("ERRO", "AS SENHAS TEM QUE ESTAR IGUAIS!")
        return False
    elif not nome or not email or not senha:
        messagebox.showerror("ERRO", "PREENCHA TODOS OS CAMPOS")
        return False
    elif not validar_email(email):
        messagebox.showerror("ERRO", "INSIRA UM EMAIL VALIDO!")
        return False
    elif not validar_nome(nome):
        messagebox.showerror("ERRO", "INSIRA UM NOME VALIDO")
        return False
    return True

def criptografar_senha(senha):
    senha_bytes = senha.encode("utf-8")
    salt = bcrypt.gensalt(rounds=14)
    senha_crip = bcrypt.hashpw(senha_bytes, salt)
    return senha_crip.decode("utf-8")

def inserir_usuario_no_banco(nome,email,senha_crip):
    try:
        db, cursor = conexao_db()
        if cursor and db:
            cursor.execute("""SELECT email FROM registro WHERE email = ?""", (email,))
            if cursor.fetchone() is not None:
                messagebox.showerror("ERRO", "ESSE EMAIL JA ESTÁ CADASTRADO!")
                return False
            cursor.execute("""INSERT INTO registro(nome,email,senha) VALUES(?,?,?)""",
            (nome,email,senha_crip))
            db.commit()
            return True
    
    except Exception as erro:
        messagebox.showerror("ERRO", f" OCORREU UM ERRO: {erro}")
        return False

def registrar_dados_usuario(nome,email,senha,confirmar_senha, mostrar_inicial):
    if not validar_dados_registro(nome, email, senha, confirmar_senha):
        return

    senha_crip = criptografar_senha(senha)

    if inserir_usuario_no_banco(nome, email, senha_crip):
        messagebox.showinfo("SUCESSO", "REGISTRO CONCLUIDO")
        mostrar_inicial()

def obter_id_pelo_email(email):
    try:
        db, cursor = conexao_db()
        if cursor and db:
            cursor.execute("""SELECT id FROM registro WHERE email = ?""", (email,))
            id_usuario = cursor.fetchone()
            return id_usuario
    except Exception as erro:
        messagebox.showerror("ERRO", f"OCORREU UM ERRO: {erro}")

def inserir_dados_no_formulario(id_usuario, sistema, linguagem, telefone, cor, bebida):
    try:
        db, cursor = conexao_db()
        if cursor and db:
            cursor.execute("""INSERT INTO formulario(
            id,sistema,
            linguagem,
            telefone,
            cor,
            bebida)
            VALUES(?,?,?,?,?,?)""",
            (id_usuario, sistema, linguagem, telefone, cor, bebida))
            db.commit()
            return True
    except Exception as erro:
        messagebox.showerror("ERRO", f"OCORREU UM ERRO AO INSERIR OS DADOS: {erro}")
        return False
    

def registrar_dados_formulario(email, sistema, linguagem, telefone, cor, bebida):
    id_usuario = obter_id_pelo_email(email)
    if id_usuario is None:
        messagebox.showerror("ERRO", "Usuario não encontrado")
        return
    elif inserir_dados_no_formulario(id_usuario, sistema, linguagem, telefone, cor, bebida):
        messagebox.showinfo("SUCESSO", "FORMULÁRIO ENVIADO")
        
def verificar_senha(email, senha_digitada, mostrar_principal):
    try:
        db, cursor = conexao_db()
        if cursor and db:

            cursor.execute("""SELECT senha FROM registro WHERE email = ?""",
                                                            (email,))
            resultado = cursor.fetchone()

            if resultado:
                senha_armazenada = resultado[0]
                if bcrypt.checkpw(senha_digitada.encode("utf-8"), senha_armazenada.encode("utf-8")):
                    messagebox.showinfo("SUCESSO", "LOGIN EFETUADO")
                    mostrar_principal()
                else:
                    messagebox.showerror("ERRO", "SENHA INCORRETA")
            else:
                messagebox.showerror("ERRO", "USUÁRIO NÃO ENCONTRADO")
    except Exception as erro:
        messagebox.showerror("ERRO", f"OCORREU UM ERRO: {erro}")
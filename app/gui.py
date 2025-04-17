from customtkinter import *  # type: ignore
from db import registrar_dados_usuario, verificar_senha, criar_tabela, criar_tabela_formulario, registrar_dados_formulario
from exportar_json import exportar_banco_para_json
from tkinter import dialog, messagebox

# Configuração do tema
set_appearance_mode("light")
set_default_color_theme("dark-blue")

janela = CTk()
janela.geometry("600x600")
janela.title("REGISTRO")

frame_inicial = CTkFrame(janela)
frame_registro = CTkFrame(janela)
frame_login = CTkFrame(janela)
frame_principal = CTkFrame(janela)
frame_formulario = CTkFrame(janela)
frame_analise = CTkFrame(janela)

def mostrar_frame_inicial():
    frame_principal.pack_forget()
    frame_login.pack_forget()
    frame_registro.pack_forget()
    frame_formulario.pack_forget()
    frame_inicial.pack(fill="both", expand="True")

def mostrar_frame_registro():
    frame_inicial.pack_forget()
    frame_login.pack_forget()
    frame_principal.pack_forget()
    frame_formulario.pack_forget()
    frame_registro.pack(fill="both", expand="True")

def mostrar_frame_login():
    frame_inicial.pack_forget()
    frame_registro.pack_forget()
    frame_principal.pack_forget()
    frame_formulario.pack_forget()
    frame_login.pack(fill="both", expand="True")

def mostrar_frame_principal():
    frame_inicial.pack_forget()
    frame_registro.pack_forget()
    frame_login.pack_forget()
    frame_formulario.pack_forget()
    frame_principal.pack(fill="both", expand="True")

def mostrar_frame_formulario():
    frame_inicial.pack_forget()
    frame_registro.pack_forget()
    frame_login.pack_forget()
    frame_principal.pack_forget()
    frame_formulario.pack(fill="both", expand="True")

def mostrar_frame_analise():
    frame_inicial.pack_forget()
    frame_registro.pack_forget()
    frame_login.pack_forget()
    frame_principal.pack_forget()
    frame_formulario.pack_forget()
    frame_analise.pack(fill="both", expand="True")

def mostrar_senha_registro():
    if entrada_registro_senha.cget("show") == "*":
        entrada_registro_senha.configure(show="")
        entrada_registro_confirmar.configure(show="")
        botao_mostrar_registro.configure(text="OCULTAR SENHA", fg_color="red")
    else:
        entrada_registro_senha.configure(show="*")
        entrada_registro_confirmar.configure(show="*")
        botao_mostrar_registro.configure(text="MOSTRAR SENHA", fg_color="green")

def mostrar_senha_login():
    if entrada_login_senha.cget("show") == "*":
        entrada_login_senha.configure(show="")
        botao_mostrar_login.configure(text="OCULTAR SENHA", fg_color="red")
    else:
        entrada_login_senha.configure(show="*")
        botao_mostrar_login.configure(text="MOSTRAR SENHA", fg_color="green")

def registrar_usuario():
    nome = entrada_registro_nome.get()
    email = entrada_registro_email.get()
    senha = entrada_registro_senha.get()
    confirmar_senha = entrada_registro_confirmar.get()    

    registrar_dados_usuario(nome, email,senha, confirmar_senha,mostrar_frame_inicial)


def registrar_formulario():
    email = entrada_login_email.get()
    sistema = entrada_formulario_SO.get()
    linguagem = entrada_formulario_linguagem.get()
    telefone = entrada_formulario_telefone.get()
    cor = entrada_formulario_cor.get()
    bebida = entrada_formulario_bebida.get()
    registrar_dados_formulario(email,sistema, linguagem, telefone, cor, bebida)
    mostrar_frame_principal()

    entrada_formulario_SO.delete(0, "end")
    entrada_formulario_linguagem.delete(0, "end")
    entrada_formulario_telefone.delete(0, "end")
    entrada_formulario_cor.delete(0, "end")
    entrada_formulario_bebida.delete(0, "end")

def logar_usuario():
    email = entrada_login_email.get()
    senha = entrada_login_senha.get()
    verificar_senha(email, senha, mostrar_frame_principal)

def escolher_arquivo():
    try:
        filetypes = (
        ("Arquivos JSON", "*.json"),
        ("Todos os arquivos", "*.*"))

        filename = filedialog.askopenfilename(
        title= "Escolha um arquivo",
        initialdir="/",
        filetypes=filetypes)
        if filename:
            messagebox.showinfo("Sucesso", f"Arquivo selecionado: {filename}")
            return filename    
    except Exception as erro:        
        messagebox.showerror("Erro", f"OCORREU UM ERRO: {erro}")
        

# Cria a tabela no banco de dados se ela não existir
criar_tabela()
criar_tabela_formulario()

# Configuração dos frames (telas) da aplicação

# Tela inicial
label_inicial = CTkLabel(frame_inicial,
        text="BEM VINDO AO MEU PROGRAMA",
        font=("Arial", 20, "bold"))
label_inicial.pack(pady=20)
CTkLabel(frame_inicial, text="VOCÊ JÁ TEM UM CADASTRO?").pack()
botao_inicial_login = CTkButton(frame_inicial,
        text="LOGIN",
        font=("Arial", 12), 
        command=mostrar_frame_login)
botao_inicial_login.pack(pady=10)
CTkLabel(frame_inicial, text="DESEJA REGISTRAR?").pack()
botao_inicial_registro = CTkButton(frame_inicial,
        text="REGISTRAR",
        font=("Arial", 12),
        command=mostrar_frame_registro)
botao_inicial_registro.pack(pady=10)

# Tela de registro (cadastro)
CTkLabel(frame_registro, text="BEM VINDO AO REGISTRO",
        font=("Arial", 20, "bold")).pack(pady=20)
CTkLabel(frame_registro,
        text="INSIRA OS DADOS PARA REGISTRAR",
        font=("Arial", 16)).pack()
CTkLabel(frame_registro, text="Insira seu nome:").pack()
entrada_registro_nome = CTkEntry(frame_registro)
entrada_registro_nome.pack(pady=5)
CTkLabel(frame_registro, text="Insira seu email:").pack()
entrada_registro_email = CTkEntry(frame_registro)
entrada_registro_email.pack(pady=5)
CTkLabel(frame_registro, text="Crie uma senha:").pack()
entrada_registro_senha = CTkEntry(frame_registro, show="*")
entrada_registro_senha.pack(pady=5)
CTkLabel(frame_registro, text="confirme sua senha:").pack(pady=5)
entrada_registro_confirmar = CTkEntry(frame_registro, show="*")
entrada_registro_confirmar.pack(pady=5)
botao_registro_registrar = CTkButton(frame_registro,
        text="REGISTRO", command=registrar_usuario)
botao_registro_registrar.pack(pady=5)
botao_registro_voltar = CTkButton(frame_registro,
        text="VOLTAR", command=mostrar_frame_inicial)
botao_registro_voltar.pack(pady=25)
botao_mostrar_registro = CTkButton(frame_registro,
        text="MOSTRAR SENHA", command=mostrar_senha_registro, fg_color="green")
botao_mostrar_registro.pack(pady=5)

# Tela de login
CTkLabel(frame_login,
        text="BEM VINDO AO LOGIN", 
        font=("Arial", 20, "bold")).pack(pady=20)
CTkLabel(frame_login,
        text="INSIRA OS DADOS PARA ENTRAR",
        font=("Arial", 16)).pack()
CTkLabel(frame_login, text="Insira seu nome:").pack()
entrada_login_nome = CTkEntry(frame_login)
entrada_login_nome.pack(pady=5)
CTkLabel(frame_login, text="Insira seu email:").pack()
entrada_login_email = CTkEntry(frame_login)
entrada_login_email.pack(pady=5)
CTkLabel(frame_login, text="Insira sua senha:").pack()
entrada_login_senha = CTkEntry(frame_login, show="*")
entrada_login_senha.pack(pady=5)
botao_login = CTkButton(frame_login, text="LOGIN", command=logar_usuario)
botao_login.pack()
botao_login_voltar = CTkButton(frame_login,
    text="VOLTAR", command=lambda:[mostrar_frame_inicial(),
    entrada_login_nome.delete(0, "end"),
    entrada_login_email.delete(0, "end"),
    entrada_login_senha.delete(0, "end")])
botao_login_voltar.pack(pady=25)
botao_mostrar_login = CTkButton(frame_login,
    text="MOSTRAR SENHA", command=mostrar_senha_login, fg_color="green")
botao_mostrar_login.pack(pady=5)

# Tela principal (após login)
CTkLabel(frame_principal,
        text="BEM VINDO A PAGINA PRINCIPAL",
        font=("Arial", 20, "bold")).pack(pady=20)
botao_principal_formulario = CTkButton(frame_principal,
        text="FORMULARIO", 
        command=mostrar_frame_formulario)
botao_principal_formulario.pack(pady=10)

botao_principal_dados = CTkButton(frame_principal,
        text="MANIPULAR DADOS",
        command=mostrar_frame_analise)
botao_principal_dados.pack(pady=10)


# Tela formulario
CTkLabel(frame_formulario,
        text="BEM VINDO AO FORMULARIO",
        font=("Arial", 20, "bold")).pack(pady=20)

CTkLabel(frame_formulario,
        text="qual sistema operacional você usa?").pack(pady=5)
entrada_formulario_SO = CTkEntry(frame_formulario)
entrada_formulario_SO.pack()

CTkLabel(frame_formulario,
        text="qual sua linguagem de programação favorita?").pack(pady=5)
entrada_formulario_linguagem = CTkEntry(frame_formulario)
entrada_formulario_linguagem.pack()

CTkLabel(frame_formulario,
        text="qual marca de telefone você gosta mais?").pack(pady=5)
entrada_formulario_telefone = CTkEntry(frame_formulario)
entrada_formulario_telefone.pack()

CTkLabel(frame_formulario, text="qual sua cor favorita?").pack(pady=5)
entrada_formulario_cor = CTkEntry(frame_formulario)
entrada_formulario_cor.pack()

CTkLabel(frame_formulario, text="qual sua bebida favorita?").pack(pady=5)
entrada_formulario_bebida = CTkEntry(frame_formulario)
entrada_formulario_bebida.pack()

botao_formulario_salvar = CTkButton(frame_formulario,
        text="SALVAR", command=registrar_formulario)
botao_formulario_salvar.pack(pady=5)

botao_formulario_voltar = CTkButton(frame_formulario,
        text="VOLTAR", command=mostrar_frame_principal)
botao_formulario_voltar.pack(pady=25)

# Tela manipular dados
CTkLabel(frame_analise,
        text="MANIPULANDO DADOS",
        font=("Arial", 20, "bold")).pack(pady=20)

CTkButton(frame_analise, text="EXPORTAR_DADOS", command= exportar_banco_para_json).pack(pady=10)

CTkButton(frame_analise, text="SELECIONAR ARQUIVO", command= escolher_arquivo).pack(pady=10)

CTkButton(frame_analise,
        text="VOLTAR", 
        command=mostrar_frame_principal).pack(pady=25)



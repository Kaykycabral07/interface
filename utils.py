import re

def validar_email(email):
    # Expressão regular para validar o formato de um email
    padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(padrao, email))
        

def validar_nome(nome):
    nome = nome.strip()  # Remove espaços em branco no início e fim
    if len(nome) < 3:
        return False
    # Expressão regular para permitir apenas letras (inclusive acentuadas) e espaços
    padrao = r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$'
    return bool(re.match(padrao, nome)) 

import json
from tkinter import messagebox
from db import conexao_db
import os

ARQUIVO_JSON = os.path.join(os.path.dirname(__file__))


def exportar_tabela_para_json(NOME_TABELA):
    db, cursor = conexao_db()
    if db and cursor:
        cursor.execute(f"SELECT * FROM {NOME_TABELA}")
        colunas = [desc[0] for desc in cursor.description]
        dados = [dict(zip(colunas,linha)) for linha in cursor.fetchall()]
        return dados
    
def exportar_banco_para_json():
    try:
        tabelas = ["registro", "formulario"]
        exportacao = {}
        for tabela in tabelas:
            exportacao[tabela] = exportar_tabela_para_json(NOME_TABELA=tabela)
        with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
            json.dump(exportacao, f, ensure_ascii=False, indent=4)
        print(f"dados exportados para {ARQUIVO_JSON}")
    except Exception as erro:
        messagebox.showerror("ERRO", f"OCORREU UM ERRO:{erro}")

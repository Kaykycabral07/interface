import pandas as pd
from tkinter import messagebox
import os

ARQUIVO_JSON = os.path.join(os.path.dirname(__file__))

def importar_dados_json():
    try:
        dados = pd.read_json(ARQUIVO_JSON)
        return dados
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao importar dados do JSON: {e}")
        return None
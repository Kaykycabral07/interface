from flask import Flask,jsonify

import sqlite3

app = Flask(__name__)

def obter_dados():
        try:
            with sqlite3.connect("/home/kayky/Downloads/interface-1/app/banco.db") as db:
                cursor = db.cursor()
                cursor.execute("""SELECT * FROM formulario""")
                colunas = [col[0] for col in cursor.description]
                data = [dict(zip(colunas, row))for row in cursor.fetchall()]
                print("dados obtidos:", data)
                return data
        except Exception as erro:
            print("Erro", f"Aconteceu um erro:{erro}")
            
        
@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/formulario', methods=['GET'])
def dados_formulario():
   data = obter_dados()
   print("Dados retornados para a rota:", data)
   return jsonify(data)



if __name__ == "__main__":
    app.run(debug=True)
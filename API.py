import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__) #  Entender melhor a biblioteca utilizada (flask)
CORS(app)  # Entender melhor a biblioteca utilizada (flask_cors)

@app.route("/") # Rota utilizada para achar o URL Utilizado
def homepage():
    """Endpoint principal da API"""
    return jsonify({ # Revisar essa linha
        "message": "API de Vendas está funcionando!",
        "status": "online",
        "endpoints": [
            "/pegarvendas - Retorna o total de vendas",
            "/status - Verifica status da API"
        ]
    })

@app.route("/pegarvendas") # Rota utilizada para achar o URL Utilizado
def vendas():
    """Endpoint que retorna o total de vendas do arquivo CSV"""
    try:
        # Verifica se o arquivo dados.csv existe
        if not os.path.exists("dados.csv"): # Analisa se a pasta existe ou não 
            return jsonify({
                "error": "Arquivo dados.csv não encontrado",
                "message": "Certifique-se de que o arquivo dados.csv está na mesma pasta da API"
            }), 404
        
        # Lê o arquivo CSV
        tabela = pd.read_csv("dados.csv") # Lê o arquivo .csv
        

        if 'Vendas' not in tabela.columns: # Verifica se a coluna vendas existe
            return jsonify({
                "error": "Coluna 'Vendas' não encontrada",
                "message": "O arquivo CSV deve ter uma coluna chamada 'Vendas'",
                "colunas_encontradas": list(tabela.columns)
            }), 400

        total_vendas = tabela["Vendas"].sum() # Faz a soma e mostra o total de vendas
        
        # Retorna o resultado
        return jsonify({
            "total_vendas": float(total_vendas),
            "quantidade_registros": len(tabela),
            "status": "sucesso"
        })
    
    except pd.errors.EmptyDataError: # Tratamento de erros da biblioteca panda que podem vir a aparecer
        return jsonify({
            "error": "Arquivo CSV está vazio",
            "message": "O arquivo dados.csv não contém dados"
        }), 400
    
    except pd.errors.ParserError: # Mesma coisa do anterior
        return jsonify({
            "error": "Erro ao ler o arquivo CSV",
            "message": "Verifique se o arquivo está no formato CSV correto"
        }), 400
    
    except Exception as e:
        return jsonify({
            "error": "Erro interno do servidor",
            "message": f"Erro inesperado: {str(e)}"
        }), 500

@app.route("/status") # Procura a rota do URL que tem o status  
def status():
    """Endpoint para verificar o status da API"""
    return jsonify({
        "status": "online",
        "message": "API funcionando corretamente",
        "versao": "1.0"
    })

if __name__ == "__main__": # Informações que aparecerão na tela
    print("🚀 Iniciando API de Vendas...")
    print("📊 Endpoints disponíveis:")
    print("   - GET / (página inicial)")
    print("   - GET /pegarvendas (total de vendas)")
    print("   - GET /status (status da API)")
    print("🌐 Servidor rodando em: http://localhost:5000")
    print("⚠️  Pressione Ctrl+C para parar o servidor")
    
    app.run(host="0.0.0.0", port=5000, debug=True) # Lugar onde irá rodar o código, o host do próprio, uso do debug e a porta de entrada
    # O app.run serve para rodar e colocar o site no ar e também deixá-lo online


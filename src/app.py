# src/app.py
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from flask import Flask, render_template, request, redirect, url_for
import requests
import gerenciador

app = Flask(__name__)

def obter_conselho():
    """Consome a API Pública de conselhos e traduz para PT-BR (Requisito do Bootcamp)"""
    try:
        # 1. Busca o conselho em inglês
        resposta = requests.get('https://api.adviceslip.com/advice', timeout=5)
        if resposta.status_code == 200:
            dados = resposta.json()
            conselho_ingles = dados['slip']['advice']
            
            # 2. Traduz para português usando a API MyMemory
            url_traducao = f"https://api.mymemory.translated.net/get?q={conselho_ingles}&langpair=en|pt-br"
            resposta_traducao = requests.get(url_traducao, timeout=5)
            
            if resposta_traducao.status_code == 200:
                dados_traducao = resposta_traducao.json()
                return dados_traducao['responseData']['translatedText']
            
            # Se a tradução falhar por algum motivo, retorna em inglês para não quebrar a tela
            return conselho_ingles
    except Exception:
        pass
    return "Mantenha a mente limpa e focada."

@app.route('/')
def index():
    tarefas = gerenciador.listar_tarefas()
    conselho = obter_conselho()
    return render_template('index.html', tarefas=tarefas, conselho=conselho)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    descricao = request.form.get('descricao')
    if descricao:
        gerenciador.adicionar_tarefa(descricao)
    return redirect(url_for('index'))

@app.route('/concluir/<int:id_tarefa>')
def concluir(id_tarefa):
    gerenciador.concluir_tarefa(id_tarefa)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
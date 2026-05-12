# src/app.py
from flask import Flask, render_template, request, redirect, url_for
import requests
import gerenciador
import os

app = Flask(__name__)

def obter_conselho():
    """Função que consome a API Pública (Requisito do Bootcamp)"""
    try:
        # API pública gratuita de conselhos
        resposta = requests.get('https://api.adviceslip.com/advice', timeout=5)
        if resposta.status_code == 200:
            dados = resposta.json()
            return dados['slip']['advice']
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
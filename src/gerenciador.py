import json
import os

ARQUIVO_DADOS = 'dados.json'


def carregar_tarefas():
    if not os.path.exists(ARQUIVO_DADOS):
        return []
    with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
        return json.load(f)


def salvar_tarefas(tarefas):
    with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as f:
        json.dump(tarefas, f, indent=4)


def adicionar_tarefa(descricao):
    if not descricao or not descricao.strip():
        raise ValueError("A descrição da tarefa não pode ser vazia.")

    tarefas = carregar_tarefas()
    nova_tarefa = {
        "id": len(tarefas) + 1,
        "descricao": descricao,
        "concluida": False}
    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)
    return nova_tarefa


def listar_tarefas():
    return carregar_tarefas()


def concluir_tarefa(id_tarefa):
    tarefas = carregar_tarefas()
    for t in tarefas:
        if t["id"] == id_tarefa:
            t["concluida"] = True
            salvar_tarefas(tarefas)
            return True
    return False


def limpar_dados():
    """Função auxiliar para limpar o arquivo (útil para os testes)"""
    if os.path.exists(ARQUIVO_DADOS):
        os.remove(ARQUIVO_DADOS)

from src import gerenciador
import pytest

# Antes de cada teste, limpamos o banco de dados temporário


@pytest.fixture(autouse=True)
def preparar_ambiente():
    gerenciador.limpar_dados()
    yield
    gerenciador.limpar_dados()


def test_adicionar_tarefa_caminho_feliz():
    """Teste 1: Caminho Feliz - Adicionar uma tarefa válida"""
    tarefa = gerenciador.adicionar_tarefa("Beber 2 litros de água")

    assert tarefa["descricao"] == "Beber 2 litros de água"
    assert tarefa["concluida"] is False
    assert len(gerenciador.listar_tarefas()) == 1


def test_adicionar_tarefa_vazia_invalida():
    """Teste 2: Entrada Inválida - Tentar adicionar tarefa vazia"""
    with pytest.raises(
        ValueError, match="A descrição da tarefa não pode ser vazia."
    ):
        gerenciador.adicionar_tarefa("")

    with pytest.raises(ValueError):
        gerenciador.adicionar_tarefa("   ")  # Apenas espaços


def test_concluir_tarefa_existente():
    """Teste 3: Variação - Marcar tarefa como concluída"""
    tarefa = gerenciador.adicionar_tarefa("Ler 10 páginas de um livro")
    sucesso = gerenciador.concluir_tarefa(tarefa["id"])

    assert sucesso is True
    tarefas = gerenciador.listar_tarefas()
    assert tarefas[0]["concluida"] is True

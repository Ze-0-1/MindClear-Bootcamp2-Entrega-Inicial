# MindClear: Organizador de Rotina para Redução de Carga Mental
**Versão:** 1.0.0

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)

## Visão Geral
O **MindClear** é uma aplicação desktop minimalista desenvolvida em Python. Seu objetivo é ajudar pessoas a gerenciar suas rotinas diárias de forma simples e direta, aliviando a carga cognitiva gerada pelo excesso de informações e compromissos.

## O Problema Real
Na sociedade moderna, o acúmulo de pequenas tarefas diárias (comprar itens básicos, tomar medicamentos, enviar um e-mail importante, beber água) gera o que a psicologia chama de **sobrecarga mental** ou **fadiga decisória**. Tentar memorizar todas as micro-tarefas do dia a dia aumenta os níveis de ansiedade e reduz o foco e a produtividade.

## A Solução
O MindClear atua como um "segundo cérebro" temporário. Através de uma interface limpa e sem distrações visuais, o usuário pode descarregar rapidamente suas pendências e marcá-las como concluídas. Ao retirar a necessidade de "lembrar" das coisas, o usuário ganha espaço mental para focar na "execução".

## Público-Alvo
* Pessoas com rotinas sobrecarregadas ou que sofrem de estresse/ansiedade devido ao acúmulo de tarefas.
* Pessoas neurodivergentes (ex: TDAH) que se beneficiam de listas visuais e recompensas imediatas (marcar como concluído).
* Cuidadores e profissionais que precisam gerenciar múltiplos pequenos afazeres ao longo do dia.

## Funcionalidades Principais
* **Cadastro rápido:** Adição de tarefas em uma interface limpa.
* **Visualização clara:** Lista estruturada separando o que está pendente do que foi concluído.
* **Conclusão de tarefas:** Marcação de itens com feedback visual.
* **Privacidade e Leveza:** Armazenamento de dados local (arquivo `.json`), sem necessidade de internet ou contas em nuvem.

## Tecnologias Utilizadas
* **Linguagem:** Python 3.10+
* **Interface Gráfica (GUI):** Tkinter (Nativo do Python)
* **Armazenamento:** JSON (Manipulação de arquivos locais)
* **Testes Automatizados:** `pytest`
* **Análise Estática (Linting):** `flake8`
* **Integração Contínua (CI):** GitHub Actions

---

## Como Instalar e Executar

### Pré-requisitos
Certifique-se de ter o [Python](https://www.python.org/) instalado em sua máquina (versão 3.10 ou superior).

### 1. Clonar o repositório
```bash
git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
cd SEU_REPOSITORIO
```

### 2. Instalar dependências
O projeto principal utiliza apenas bibliotecas nativas do Python. As dependências externas são exclusivas para o ambiente de testes e linting.
```bash
pip install -r requirements.txt
```
### 3. Executar a aplicação
Estando na raiz do projeto, execute o comando abaixo para abrir a interface gráfica:
```bash
python src/app.py
```
---

## Como rodar os Testes e o Linting

Este projeto segue boas práticas de Engenharia de Software, garantindo a qualidade do código através de testes automatizados e análise estática.

Para executar os testes automatizados:

```bash
python -m pytest tests/
```
Para verificar a padronização do código (Linting):
```bash
python -m flake8 src/ tests/
```

Nota: Este projeto possui uma pipeline configurada no GitHub Actions que executa automaticamente esses comandos a cada push no repositório.


## Autor e Informações Acadêmicas
Nome do Aluno: José Gabriel Ribeiro Cecilio

Projeto: MindClear - Organizador de Rotina

Link do Repositório: https://github.com/Ze-0-1/MindClear-Bootcamp2-Entrega-Inicial.git

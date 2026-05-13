# MindClear: Organizador de Rotina para Redução de Carga Mental
**Versão:** 2.0.0 (Etapa Intermediária - Bootcamp)

[![Deploy with Vercel](https://vercel.com/button)](https://mind-clear-bootcamp2-entrega-inicia.vercel.app/)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Framework](https://img.shields.io/badge/framework-Flask-lightgrey)

## 🌐 Link do Deploy (Acesso Público)
**Acesse a aplicação online aqui:** [https://mind-clear-bootcamp2-entrega-inicia.vercel.app/](https://mind-clear-bootcamp2-entrega-inicia.vercel.app/)

---

## 📋 Visão Geral
O **MindClear** evoluiu de uma aplicação desktop para uma plataforma web minimalista. O objetivo permanece o mesmo: servir como um "segundo cérebro" para descarregar micro-tarefas diárias, reduzindo a fadiga decisória e a ansiedade. Nesta versão, o sistema integra-se com serviços externos para oferecer pílulas de sabedoria ao utilizador durante a sua jornada de organização.

## 🚀 Novidades da Etapa Intermediária
Nesta fase de evolução, o projeto implementou padrões profissionais de desenvolvimento:
* **Migração para Web:** Substituição da interface Tkinter por **Flask**, permitindo acesso via navegador e hospedagem em nuvem.
* **Consumo de API Pública (Advice Slip):** A cada carregamento, a aplicação busca um conselho aleatório para motivar o utilizador.
* **Integração com API de Tradução (MyMemory):** Como a API de conselhos é nativa em inglês, implementamos um fluxo de tradução em tempo real para exibir os conteúdos em Português (PT-BR).
* **Testes de Integração:** Criação de testes automatizados para validar a comunicação com os serviços externos de API.
* **CI/CD:** Pipeline configurada via GitHub Actions e deploy automático via Vercel.

## 🛠️ Tecnologias Utilizadas
* **Back-end:** Python 3.10+ e Flask.
* **Front-end:** HTML5 e CSS3 (Jinja2 Templates).
* **APIs Externas:** * [Advice Slip API](https://api.adviceslip.com/) (Conselhos).
  * [MyMemory API](https://mymemory.translated.net/) (Tradução).
* **Persistência:** JSON (Manipulação de arquivos locais/temporários).
* **Qualidade:** `pytest` (Testes unitários e de integração) e `flake8` (Linting).
* **Infraestrutura:** GitHub Actions (CI) e Vercel (Hospedagem/Deploy).

---

## ⚙️ Como Instalar e Executar Localmente

### 1. Clonar o repositório
```bash
git clone [https://github.com/Ze-0-1/MindClear-Bootcamp2-Entrega-Inicial.git](https://github.com/Ze-0-1/MindClear-Bootcamp2-Entrega-Inicial.git)
cd MindClear-Bootcamp2-Entrega-Inicial
```

### 2. Instalar dependências
```bash
pip install -r requirements.txt
```

### 3. Executar a aplicação
```bash
python src/app.py
```
Acesse `http://127.0.0.1:5000` no seu navegador.

---

## 🧪 Qualidade de Código

### Rodar Testes Automatizados
O projeto inclui testes de integração que validam o fluxo com as APIs externas (usando mocks para garantir estabilidade no CI).
```bash
python -m pytest tests/
```

### Verificação de Linting (Padrões de Código)
```bash
python -m flake8 src/ tests/
```

---

## 👤 Autor e Informações Acadêmicas
* **Nome:** José Gabriel Ribeiro Cecilio
* **Projeto:** MindClear - Etapa 2 (Evolução: API, Testes e Deploy)
* **Repositório:** [GitHub Repo](https://github.com/Ze-0-1/MindClear-Bootcamp2-Entrega-Inicial.git)
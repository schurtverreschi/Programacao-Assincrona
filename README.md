# Programação Assíncrona em Python

Repositório de estudos desenvolvido em **Python** com foco na resolução dos desafios práticos do curso **"Praticando Python: Programação Assíncrona"** da Alura, explorando concorrência, corrotinas, agendamento e sincronização de tarefas com a biblioteca padrão `asyncio`.

## 🎯 Objetivo do Projeto

Praticar o desenvolvimento de código assíncrono em Python aplicando `async`/`await`, criação e execução simultânea de múltiplas tarefas (`asyncio.create_task` e `asyncio.gather`), controle de tempo não bloqueante (`asyncio.sleep`) e gerenciamento de fluxos concorrentes em cenários simulados do dia a dia.

## 📁 Estrutura do Repositório

```text
.
├── .gitignore
├── README.md
├── requirements.txt
├── ex01_temporizador.py              # Temporizador assíncrono com contagem de tempo
├── ex02_duas_tarefas.py              # Execução concorrente de duas tarefas simultâneas
├── ex03_fatorial_paralelo.py         # Cálculo assíncrono/paralelo de fatoriais
├── ex04_notificacoes.py              # Simulação de envio assíncrono de notificações
├── ex05_pedidos_loja.py              # Processamento concorrente de pedidos de uma loja
├── ex06_inscricoes_cursos.py         # Gerenciamento assíncrono de inscrições em cursos
├── ex07_monitoramento_tarefas.py     # Acompanhamento de status e conclusão de tarefas
├── ex08_sensores_ambientais.py       # Coleta e leitura contínua/assíncrona de sensores
├── ex09_monitoramento_download.py    # Simulação de progresso e monitoramento de downloads
└── ex10_sistema_apostas.py           # Simulação concorrente de processamento de apostas
```

## 🧩 Exercícios e Conceitos Praticados

* **Fundamentos e Concorrência Básica (`ex01_temporizador.py`, `ex02_duas_tarefas.py`)**: introdução a corrotinas com `async def`, suspensão não bloqueante com `await asyncio.sleep()` e execução simultânea de tarefas.
* **Processamento Simultâneo (`ex03_fatorial_paralelo.py`, `ex04_notificacoes.py`)**: coordenação de múltiplas corrotinas em paralelo utilizando `asyncio.gather()` para otimizar o tempo total de execução.
* **Fluxos de Negócio Assíncronos (`ex05_pedidos_loja.py`, `ex06_inscricoes_cursos.py`)**: simulação de etapas de validação, processamento e resposta em operações independentes sem bloquear o *event loop*.
* **Monitoramento e Eventos Contínuos (`ex07_monitoramento_tarefas.py`, `ex08_sensores_ambientais.py`, `ex09_monitoramento_download.py`)**: controle do ciclo de vida de tasks, leitura periódica de dados simulados e acompanhamento de progresso em tempo real.
* **Integração de Fluxos Concorrentes (`ex10_sistema_apostas.py`)**: consolidação dos conceitos de assincronismo para coordenar múltiplas operações e resultados simultâneos.

## 🛠️ Tecnologias e Fluxo de Trabalho

* **Python 3.10+** (`asyncio`)
* **Git e GitHub** (organização do desenvolvimento utilizando **GitHub Flow** com *Issues*, *Branches* dedicadas por exercício e *Pull Requests*)

## ▶️ Como Executar Localmente

1. Clone o repositório e acesse a pasta do projeto:

```bash
git clone https://github.com/schurtverreschi/Programacao-Assincrona.git
cd programacao-assincrona
```

2. Crie e ative um ambiente virtual (opcional, recomendado):

```bash
python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate
```

3. *(Opcional)* Instale as dependências listadas no `requirements.txt`:

```bash
pip install -r requirements.txt
```

4. Execute qualquer um dos exercícios pelo terminal:

```bash
python ex01_temporizador.py
```

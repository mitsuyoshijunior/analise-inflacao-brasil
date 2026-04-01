# 📊 Análise da Inflação no Brasil (Pipeline ETL Automatizado)

## 📌 Visão Geral

Este projeto consiste na construção de um pipeline ETL automatizado para coleta, tratamento e análise de dados de inflação no Brasil.

Os dados são extraídos por meio da API oficial do Banco Central, que disponibiliza a inflação mensal. Após a extração, os dados passam por um processo de tratamento e organização utilizando Python, dividido em etapas:

- **Extract**: coleta dos dados via API
- **Transform**: limpeza, tratamento e padronização
- **Queries**: criação de métricas e colunas analíticas

Todas essas etapas são orquestradas através de um arquivo principal (`main.py`), responsável por executar o pipeline completo.

A execução do pipeline é automatizada via Agendador de Tarefas do Windows, com frequência semanal, garantindo a atualização dos dados mesmo sem intervenção manual.

Os dados tratados são armazenados automaticamente no Google Drive e utilizados como base para um dashboard interativo no Google Sheets.

---

## 🗂️ Estrutura do Projeto
analise-inflacao-brasil/

├── src/

│ ├── extract.py

│ ├── transform.py

│ ├── queries.py

│ └── main.py

├── data/ # dados gerados automaticamente (não versionados)

├── dashboard/ # informações do dashboard

├── requirements.txt

└── .gitignore


---

## ⚙️ Tecnologias Utilizadas

- Python (pandas, requests)
- Visual Studio Code
- Google Drive
- Google Sheets
- Windows Task Scheduler (Automação)

---

## 📊 Como Visualizar o Projeto

O dashboard interativo pode ser acessado pelo link abaixo:

👉 **[Acessar Dashboard](https://docs.google.com/spreadsheets/d/1J0tqH7Lc_5n6m3lnIspF6KK1LNZLJJP6yY4VXWRfLZY/edit?usp=drive_link)**

---

## 📈 Sobre o Dashboard

O dashboard foi desenvolvido no Google Sheets com base nos dados tratados automaticamente pelo pipeline.

Ele é composto pelas seguintes análises:

### 📍 Visão Geral
- Inflação do último mês
- Inflação acumulada no ano vigente
- Média da inflação dos últimos 12 meses
- Gráfico comparativo da inflação:
  - Período pré-Plano Real
  - Período pós-Plano Real

### 📅 Análise Mensal
- Evolução da inflação mês a mês
- Variação mensal

### 📆 Análise Anual
- Inflação acumulada por ano
- Ranking dos anos com maior inflação

### 🔎 Comparações Específicas
Análise comparativa entre períodos relevantes:
- **1995** – início do período pós-Plano Real  
- **2015** – crise política brasileira  
- **2020** – pandemia de COVID-19  

---

## 🚀 Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de consolidar conhecimentos em:

- Manipulação e análise de dados com Python  
- Construção de pipelines ETL  
- Automação de processos  
- Geração de insights a partir de dados reais  

Além disso, o projeto simula um fluxo de dados próximo ao utilizado em ambientes profissionais, com coleta automática, tratamento e disponibilização para visualização.

---

## 📬 Contato

Caso queira entrar em contato ou saber mais sobre o projeto:

- LinkedIn: https://linkedin.com/in/mitsuyoshijunior/
- GitHub: https://github.com/mitsuyoshijunior/
- Email: mitsuyoshijunior@gmail.com

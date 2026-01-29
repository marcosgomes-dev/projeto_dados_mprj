# 🕵️‍♂️ Desafio Técnico - Auditoria de Dados (MPRJ)

Este repositório contém a entrega final do desafio técnico de análise de dados. O projeto consiste em uma simulação de auditoria em contratos públicos, abrangendo modelagem de dados, investigação forense via SQL e desenvolvimento de um dashboard interativo em Python.

---

## 📍 Acesso Rápido aos Entregáveis

| Item Solicitado | Link de Acesso | Descrição |
| :--- | :--- | :--- |
| **1. Relatório Técnico** | [📄 Ler Relatório (PDF)](Relatorio_Tecnico.pdf) | Insights e conclusões. |
| **2. Modelo de Dados** | [🖼️ Ver Diagrama ER](docs/diagrama_ER.png) | Diagrama da Questão 1. |
| **3. Dashboard** | [💻 Ver Código Fonte](src/dashboard.py) | Script da Questão 3. |
| **4. Queries SQL** | [🔍 Ver Scripts SQL](sql/) | Scripts da Questão 2. |

---

## 🚀 Como Executar (Passo a Passo)

Para rodar o projeto localmente, abra o seu terminal e execute os **3 comandos** abaixo na ordem:

```bash
# 1. Clone o repositório
git clone [https://github.com/marcosgomes-dev/desafio-dados-mprj.git](https://github.com/marcosgomes-dev/desafio-dados-mprj.git)
cd desafio-dados-mprj

# 2. Instale as dependências
pip3 install -r requirements.txt

# 3. Execute o Dashboard
python3 -m streamlit run src/dashboard.py

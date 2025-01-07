# sprint5_heury

Projeto para o Sprint 5 do curso de Análise de Sistemas da Tripleten
Aluno: Heury Alex Sander Neves

# Explicação Inicial

Este projeto aborda um aplicativo web interativo, criado com a biblioteca **Streamlit**, que permite a visualização de dados de um arquivo CSV, sobre vendas de carros. Através desse aplicativo, o usuário poderá explorar diferentes aspectos dos dados de anúncios de carros de forma intuitiva, com gráficos interativos baseados em **Plotly Express**.

## Funcionalidades

O aplicativo oferece as seguintes funcionalidades:

1. **Histograma de Odômetro**: O usuário pode gerar um histograma que mostra a distribuição do odômetro (quilometragem) dos carros presentes no conjunto de dados.
2. **Gráfico de Dispersão**: O usuário pode gerar um gráfico de dispersão que compara o **preço** e o **ano de fabricação** dos carros.
3. **Interface Interativa**: Utilizando caixas de seleção, o usuário escolhe qual gráfico deseja visualizar. O aplicativo atualiza os gráficos dinamicamente com base nas escolhas do usuário.

## Como Usar

1. **Instalação**:

   - Certifique-se de ter o Python instalado em seu sistema.
   - Instale as dependências do projeto com o seguinte comando:
     ```bash
     pip install -r requirements.txt
     ```

2. **Executando o Aplicativo**:
   - Execute o aplicativo Streamlit com o comando:
     ```bash
     streamlit run app.py
     ```
   - Após rodar o comando, o Streamlit abrirá o aplicativo em uma página do navegador onde você poderá interagir com os gráficos.

## Requisitos

- Python 3.x
- Pandas
- Plotly
- Streamlit

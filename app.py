import pandas as pd
import plotly.express as px
import streamlit as st

# Carregar os dados
car_data = pd.read_csv('vehicles.csv')

# Converter a coluna 'model_year' para int e tratar valores ausentes
car_data['model_year'] = pd.to_numeric(car_data['model_year'], errors='coerce').fillna(
    car_data['model_year'].mode()[0]).astype(int)

# Converter a coluna 'price' para numérico, caso necessário, e tratar valores ausentes
car_data['price'] = pd.to_numeric(car_data['price'], errors='coerce')
car_data['price'] = car_data['price'].fillna(car_data['price'].mean())

# Tratar valores ausentes na coluna 'is_4wd' (convertendo para bool)
car_data['is_4wd'] = car_data['is_4wd'].fillna(0).astype(bool)

# Cabeçalho
st.header('Visualização de Dados de Vendas de Carros')

# Caixa de seleção para histograma
show_histogram = st.checkbox('Mostrar Histograma de Odômetro')

# Caixa de seleção para gráfico de dispersão
show_scatter = st.checkbox('Mostrar Gráfico de Dispersão: Preço vs. Ano')

# Se a caixa de histograma estiver marcada
if show_histogram:
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    # Criar o histograma
    fig_histogram = px.histogram(car_data, x="odometer")
    # Exibir o gráfico interativo
    st.plotly_chart(fig_histogram, use_container_width=True)

# Se a caixa de gráfico de dispersão estiver marcada
if show_scatter:
    st.write(
        'Criando um gráfico de dispersão entre Preço e Ano de Fabricação dos Carros')
    # Criar o gráfico de dispersão
    fig_scatter = px.scatter(car_data, x="model_year",
                             y="price", title="Preço vs Ano de Fabricação")
    # Exibir o gráfico interativo
    st.plotly_chart(fig_scatter, use_container_width=True)

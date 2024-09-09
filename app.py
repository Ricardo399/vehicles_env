import streamlit as st 
import pandas as pd 
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
st.header('vehicles')

hist_button = st.button('Construir histograma')

#al hacer clic en el boton
if hist_button:
    #escribir un mensaje
    st.write('Creacion de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    #construir un histograma
    fig = px.histogram(car_data, x='odometer')

    #mostrar grafico plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


chart_button = st.button('Construir grafico de dispersion')

if chart_button:
    st.write('Creacion de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True)
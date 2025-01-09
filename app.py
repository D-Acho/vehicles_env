import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv("vehicles_us.csv") # leer los datos
st.header("Todo  lo quee necesitas saber sobre la venta de coches")

hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    
disp_button = st.button('Construir diagrama de dispersión') # crear un botón
        
if disp_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')
            
    # crear diagrama
    fig = px.scatter(car_data, x="odometer", y="price")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
<<<<<<< HEAD
    
# crear una casilla de verificación
horizontal_bar= st.checkbox('Construir diagrama de barras horizontal')

if horizontal_bar: # si la casilla de verificación está seleccionada
    st.write('Grafico de barras horizontal de costos')
    
    # crear grafico de barras
    fig_horizontal_bar = px.bar(car_data, x='price', y='model', orientation='h', title='Costos de Vehículos por Año') 
    
    #mostrar gráfico horizontal
    st.plotly_chart(fig_horizontal_bar, use_container_width=True)
=======
>>>>>>> 4257ab30eadf4ea50fb3566b4ed9eb6d41d82f91

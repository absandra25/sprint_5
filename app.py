import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
st.header('Graficos de venta de autos')
car_data



st.write('Histogramas promedio del precio vs año del modelo ')
hist_button = st.button('histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    st.write('Creación de un histograma')
    fig = px.histogram(car_data , x='model_year',  title='promedio del precio por año del modelo' , y='price', histfunc='avg', color='condition')
    fig.update_layout(bargap=0.2)
    fig.show()
    st.plotly_chart(fig, use_container_width=True)
    
    
st.write('Grafico de dispersón precio vs año del modelo del auto')
g_button = st.checkbox('grafico') # crear un botón
        
if g_button: # al hacer clic 
    st.write('Creación de un grafico por año de modelo vs precio ')
    figo = px.scatter(car_data, x='model_year', y='price', color= 'model')
    figo.show()
    st.plotly_chart(figo, use_container_width=True)

st.write('Histrograma cantidad de autos que hay segun el tipo de auto')
c_histogram = st.checkbox('histograma tipo de autos')
        
if c_histogram: # al hacer clic 
    st.write('Creación de un histograma numero de autos que hay segun su tipo')
    figh = px.histogram(car_data, x='type', title='cantida de autos por tipo', color='paint_color' )
    figh.update_layout(bargap=0.2)
    figh.show()
    st.plotly_chart(figh, use_container_width=True)
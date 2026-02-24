import streamlit as st
import pandas as pd
import numpy as np

# Título de la aplicación
st.title('📊 Mi primer Dashboard con Streamlit')

# Un mensaje sencillo
st.write("Esta aplicación genera datos aleatorios y los visualiza dinámicamente.")

# Creamos un slider para que el usuario elija el número de puntos
puntos = st.slider('¿Cuántos puntos quieres ver?', 10, 100, 50)

# Generamos datos aleatorios con Pandas
chart_data = pd.DataFrame(
    np.random.randn(puntos, 3),
    columns=['Ventas', 'Costos', 'Ganancias']
)

# Mostramos un gráfico de líneas
st.line_chart(chart_data)

# Mostramos una tabla con los datos (opcional)
if st.checkbox('Mostrar tabla de datos'):
    st.table(chart_data.head())

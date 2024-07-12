import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#   Declarar el titulo de la aplicación
st.title("Streamlit App")


df = pd.read_csv('Catalogo_presupuestos.csv', encoding='utf-8', low_memory=False)
st.caption(r"A continuación se muestra la tabla \"Catálogo de presupuestos\"")
st.write(df)

#   Crear el gráfico de barras
counts = df['nombrePadron'].value_counts()

st.header("Padrones")
st.caption(r"Se muestra una grafica de barras para facilitar la lectura de la frecuencia de los padrones")

fig, ax = plt.subplots(figsize=(8, 3))
counts.plot(kind='bar', ax=ax)
ax.set_title('Frecuencia de padrones')
ax.set_xlabel('Padrones')
ax.set_ylabel('Frecuencia')
st.pyplot(fig)

#   Crear el gráfico de barras
counts = df['marca'].value_counts()

st.header("Frecuencia de Marcas de Autos")
st.caption(r"Se muestra una grafica de barras para facilitar la lectura de la frecuencia de marcas de carros")
fig, ax = plt.subplots(figsize=(20, 8))
counts.plot(kind='bar', ax=ax)
ax.set_title('Frecuencia de Marcas de Carros')
ax.set_xlabel('Marcas')
ax.set_ylabel('Frecuencia')
st.pyplot(fig)
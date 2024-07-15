import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#   Declarar el titulo de la aplicación
st.set_page_config(page_title='Streamlit App', page_icon='📈', layout='wide')

# Con la siguiente linea se pueden leer todas las hojas del archivo de Excel 
# pero el tiempo de ejecución aumenta considerablemente
# df = pd.read_excel('D:\Escritorio\Software\Streamlit\Analisis-de-Archivo.xlsx', 
# sheet_name='Catalogo de Presupuestos')


df = pd.read_csv('Catalogo_presupuestos.csv')
st.caption(r"A continuación se muestra la tabla \"Catálogo de presupuestos\"")
st.dataframe(df)

st.divider()

st.header("Total (resultados filtrados)")

# st.sidebar.header("Filtrar resultados")
padron_selection = st.multiselect("Selecciona un padrón:", options=df['nombrePadron'].unique(), placeholder="Escoge una opción")

df_selection = df.query("nombrePadron == @padron_selection")
total_filter = int(df_selection['serie'].sum())

st.caption(f"El total de los resultados obtenidos mediante el uso de los filtros es de:$ :blue[ _{total_filter}_]  MXN")
# Crear el gráfico de barras
counts = df['nombrePadron'].value_counts()

st.divider()

st.header("Padrones")
st.caption(r"Se muestra una grafica de barras para facilitar la lectura de la frecuencia de los padrones")

fig, ax = plt.subplots(figsize=(15, 3))
counts.plot(kind='bar', ax=ax)
ax.set_title('Frecuencia de padrones')
ax.set_xlabel('Padrones')
ax.set_ylabel('Frecuencia')
st.pyplot(fig)

st.divider()

# Crear el gráfico de barras
counts = df['marca'].value_counts()

st.header("Frecuencia de Marcas de Autos")
st.caption(r"Se muestra una grafica de barras para facilitar la lectura de la frecuencia de marcas de carros")
fig, ax = plt.subplots(figsize=(20, 8))
counts.plot(kind='bar', ax=ax)
ax.set_title('Frecuencia de Marcas de Carros')
ax.set_xlabel('Marcas')
ax.set_ylabel('Frecuencia')
st.pyplot(fig)

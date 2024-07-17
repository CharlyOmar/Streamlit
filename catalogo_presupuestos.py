import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#   Declarar el titulo de la aplicación
st.set_page_config(page_title='Streamlit App', page_icon='📈', layout='wide')

# Con la siguiente linea se pueden leer todas las hojas del archivo de Excel 
# pero el tiempo de ejecución aumenta considerablemente
# df = pd.read_excel('D:\Escritorio\Software\Streamlit\Analisis-de-Archivo.
# xlsx', sheet_name='Catalogo de Presupuestos')


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
st.bar_chart(df['nombrePadron'].str.capitalize().value_counts(), x_label="TRÁMITES", y_label="FRECUENCIA", height=600)
st.divider()

# Crear el gráfico de barras
counts = df['marca'].value_counts()

st.header("Frecuencia de Marcas de Autos")
st.caption(r"Se muestra una grafica de barras para facilitar la lectura de la frecuencia de marcas de carros")

st.bar_chart(df['marca'].value_counts(), x_label="MARCAS", y_label="FRECUENCIA", height=500)

#   Calcular las frecuencias de las marcas de autos
counts_marca = df['marca'].value_counts()

#   Crear el gráfico de pastel para las marcas de autos
fig, ax = plt.subplots(figsize=(12, 12))
ax.pie(counts_marca, labels=counts_marca.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio asegura el gráfico de pastel  circular
ax.set_title('Frecuencia de Marcas de Autos')
#   Mostrar el gráfico de pastel en Streamlit
st.pyplot(fig)
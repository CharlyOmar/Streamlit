import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#   Declarar el titulo de la aplicación
st.set_page_config(page_title='Streamlit App', page_icon='📈', layout='wide')

#   Con la siguiente linea se pueden leer todas las hojas del archivo de Excel pero el tiempo de ejecución aumenta considerablemente
#df = pd.read_excel('D:\Escritorio\Software\Streamlit\Analisis-de-Archivo.xlsx', sheet_name='Catalogo de Presupuestos')

st.header("Catálogo de Presupuestos")
df = pd.read_csv('D:\Escritorio\Software\Streamlit\Catalogo_presupuestos.csv')
#   st.caption(r"A continuación se muestra la tabla \"Catálogo de presupuestos\"")
#   st.dataframe(df)

col1, col2, col3 = st.columns((2, 2, 2), gap='medium')
with col1:
   col1.metric("Trámites realizados",df.nombrePadron.size)
with col2:
   col2.metric("Tipos de padrones", len(df['nombrePadron'].dropna().str.upper().unique()))
with col3:
    col3.metric("Número de usuarios", len(df['user'].dropna().str.upper().unique()))

st.divider()

st.header("Total (resultados filtrados)")
padron_selection = st.multiselect("Selecciona un padrón:", options=df['nombrePadron'].dropna().str.upper().unique(), placeholder="Escoge una opción")
df_selection = df.query("nombrePadron == @padron_selection")
total_sum = pd.to_numeric(df_selection['total'], errors='coerce').sum()
st.caption(f"El total de los resultados obtenidos mediante el uso de los filtros es de:$ :blue[ _{total_sum}_]  MXN")
st.divider()

st.header("Padrones")
st.caption(r"Se muestra una grafica de barras para facilitar la lectura de la frecuencia de los padrones")
st.bar_chart(df['nombrePadron'].str.capitalize().value_counts(), x_label="TRÁMITES", y_label="FRECUENCIA", height=600)
st.divider()

#   Crear el gráfico de barras
st.header("Frecuencia de Marcas de Autos")
st.caption(r"Se muestra una grafica de barras para facilitar la lectura de la frecuencia de marcas de carros")

st.bar_chart(df['marca'].value_counts(), x_label="MARCAS", y_label="FRECUENCIA", height=500)

#   Calcular las frecuencias de las marcas de autos
counts_marca = df['marca'].value_counts()

#   Crear el gráfico de pastel para las marcas de autos
fig, ax = plt.subplots(figsize=(12, 12))
ax.pie(counts_marca, labels=counts_marca.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio asegura que el gráfico de pastel es circular
ax.set_title('Frecuencia de Marcas de Autos')
#   Mostrar el gráfico de pastel en Streamlit
st.pyplot(fig)
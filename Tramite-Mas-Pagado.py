import streamlit as st
import pandas as pd
# import altair as alt
import plotly.express as px
# import matplotlib.pyplot as plt
# import seaborn as sns
from dateutil import parser

# Declarar el título de la aplicación
st.set_page_config(page_title="Streamlit", page_icon="📈", layout="wide")
st.header("Catálogo de Presupuestos")

# Ruta al archivo CSV
file_path = "Catalogo_presupuestos.csv"

# Tamaño de la muestra
sample_size = 150

# Cargar una muestra aleatoria del archivo
df = pd.read_csv(file_path).sample(n=sample_size, random_state=1)

# Diagnóstico: imprimir nombres de columnas
st.write("Nombres originales de las columnas: ", df.columns)

# Convertir @timestamp a datetime (asegúrate de que el nombre de la columna es correcto)
if "@timestamp" in df.columns:
    df["@timestamp"] = df["@timestamp"].apply(parser.parse)
elif "timestamp" in df.columns:
    df["timestamp"] = df["timestamp"].apply(parser.parse)
else:
    st.error("No se encontró la columna @timestamp en el archivo CSV.")
    st.stop()

# Cambiar a mayusculas los nombres de las columnas
df.columns = df.columns.str.upper()

# Renonmbrar columnas
df.rename(
    columns={
        "@TIMESTAMP": "FECHA & HORA",
        "TRAMITEID": "TRÁMITE",
        "NOMBREPADRON": "NOMBRE PADRÓN",
        "TRANSACTIONID": "TRANSACCIÓN",
        "USERID": "ID USUARIO",
        "EXECUTION_ARN": "ARN",
        "EMAIL": "CORREO",
        "USER": "USUARIO",
        "LOTEID": "LOTE",
        "FECHAVENCIMIENTO": "FECHA DE VENCIMIENTO",
        "NUMEROSERIE": "NÚMERO DE SERIE",
    },
    inplace=True,
)

# Convertir los valores de las columnas a mayusculas
# para mantener un mismo formato
df['NOMBRE PADRÓN'] = df['NOMBRE PADRÓN'].str.upper()
df['USUARIO'] = df['USUARIO'].str.upper()

# Agregar la columna NO al principio
df.insert(0, "NO.", range(1, len(df) + 1))

# Imprime los datos de la muestra obtenida
st.dataframe(df)

# Filtrar categorías con frecuecia mayor a 20
filtered_counts = df['NOMBRE PADRÓN'].value_counts()
filtered_counts = filtered_counts[filtered_counts > 20].reset_index()
filtered_counts.columns = ['NOMBRE PADRÓN', 'FRECUENCIA']

# Crear el gráfico de barras con Plotly
fig = px.bar(
    filtered_counts,
    x='NOMBRE PADRÓN',
    y='FRECUENCIA',
    color='NOMBRE PADRÓN',
    color_discrete_map={
        'Replaqueo': 'yellow',
        'Refrendo': 'red',
        'Impuesto sobre nómina': 'orange'
    },
    title="Frecuencia de los padrones",
    labels={'NOMBRE PADRÓN': 'TRÁMITES', 'FRECUENCIA': 'FRECUENCIA'} 
)

# Mostrar el gráfico de barras
st.divider()
st.header("Patrones")
st.caption("Gráfico de barras sobre la frecuencia de los padrones")
st.plotly_chart(fig, use_container_width=True)
st.divider()

"""
# Crea el gráfico con Matplotlib 
## Observación: con este gráfico no es posible interactuar con los valores 
# sino que es estatico además de que requiere la librería de matplot

st.divider()
st.header("Padrones")
st.caption(r"Grafica de barras para la lectura de la frecuencia de los padrones")

fig, ax = plt.subplots()
colors = {'Impuesto sobre nómina': 'black', 'Refrendo': 'yellow', 'Replaqueo': 'orange'}
counts.plot(kind='bar', color=[colors.get(x, 'black') for x in counts.index], ax=ax)
ax.set_title("TRÁMITES")
ax.set_xlabel("FRECUENCIA")
ax.set_ylabel("Frecuencia de los padrones")
st.pyplot(fig)
st.divider()
""" 

""" 
# Crea el gráfico de barras con Altair
# Observación: se tiene que especificar el tipo de variable que es
# asi como usar la librería Altair aunque esta opcion NO FUNCIONÓ

# Verificar los datos de 'NOMBRE PADRÓN'
# st.write(df['NOMBRE PADRÓN'].head())

# gráfico
count = df['NOMBRE PADRÓN'].str.capitalize().value_counts().reset_index()
counts.columns = ['NOMBRE PADRÓN', 'FRECUENCIA']

# Verificar los datos de 'counts'
# st.write(counts.head())

colors = alt.Scale(
    domain=['Impuesto sobre nómina', 'Refrendo', 'Replaqueo'],
    range=['red', 'yellow', 'blue']
)

chart = alt.Chart(counts).mark_bar().encode( # type: ignore
    x=alt.X('NOMBRE PADRÓN: N', title='TRÁMITES'),
    y=alt.Y('FRECUENCIA: Q', title='FRECUENCIA'),
    color =alt.Color('NOMBRE PADRÓN', scale=colors)
).properties(
    height=600,
    title="Frecuencia de los padrones"
)
st.divider()
st.header("Padrones")
st.caption(r"Grafica de barras sobre la frecuencia de los padrones")
st.altair_chart(chart, use_container_width=True)
st.divider()
""" 

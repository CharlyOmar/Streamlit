import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dateutil import parser


# Declarar el título de la aplicación
st.set_page_config(page_title="Streamlit", page_icon="📈", layout="wide")
st.header("Catálogo de Presupuestos")

# Ruta al archivo CSV
file_path = "Catalogo_presupuestos.csv"

# Tamaño de la muestra
sample_size = 50

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

# Agregar la columna NO al principio
df.insert(0, "NO.", range(1, len(df) + 1))

# Imprime los 100 datos
st.dataframe(df)

# Gráfico de barras: Tipo de trámite que más se realiza
st.subheader("Tipo de Trámite que Más se Realiza")
tramite_counts = df["TRÁMITE"].value_counts()
fig, ax = plt.subplots()
sns.barplot(x=tramite_counts.index, y=tramite_counts.values, ax=ax)
ax.set_xlabel("Tipo de Trámite")
ax.set_ylabel("Número de Trámites")
ax.set_title("Número de Trámites por Tipo")
st.pyplot(fig)

# Gráfico de líneas: Frecuencia de trámites a lo largo del tiempo
st.subheader("Frecuencia de Trámites a lo Largo del Tiempo")
df["DATE"] = df["@timestamp"].dt.date
tramites_por_fecha = df.groupby(["DATE", "ID_TRAMITE"]).size().unstack().fillna(0)
fig, ax = plt.subplots()
tramites_por_fecha.plot(ax=ax)
ax.set_xlabel("Fecha")
ax.set_ylabel("Número de Trámites")
ax.set_title("Frecuencia de Trámites por Fecha")
st.pyplot(fig)

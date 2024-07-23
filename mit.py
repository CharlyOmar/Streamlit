import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title='MIT page', page_icon='📈', layout='wide')
df = pd.read_excel('Analisis-de-Archivo.xlsx', sheet_name='MIT')

columnas_deseadas = ['user', 'tramite', 'amount', 'model', 'plate']
df_deseado = df[columnas_deseadas]

st.title("📋    ANALYTICS MIT   📈")

col1, col2 = st.columns((2,2), gap='small')
with col1:
    col1 = st.dataframe(df_deseado)
with col2:
    st.bar_chart(df_deseado['tramite'].str.upper(),
                x_label="TIPO DE TRAMITE",
                y_label="FRECUENCIA")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title='Streamlit App', page_icon='📈', layout='wide')
df = pd.read_excel('Analisis-de-Archivo.xlsx', sheet_name='SPEI')

st.title("📋    ANALYTICS   📈")

with st.container(border=True):
    st.subheader("💰 DINERO TOTAL DE ACUERDO AL BANCO 🏦")
    col1, col2, col3, col4 = st.columns((2, 2, 2, 2), gap='medium')
    with col1:
        col1.metric("Total HSBC", "{:,}".format(df[df['claveBanco'] == 'HSB']['importe'].sum()))
    with col2:
        col2.metric("Total BBVA", "{:,}".format(df[df['claveBanco'] == 'BBV']['importe'].sum()))
    with col3:
        col3.metric("Total BANAMEX", "{:,}".format(df[df['claveBanco'] == 'BAN']['importe'].sum()))
    with col4:
        col4.metric("Total BANORTE", "{:,}".format(df[df['claveBanco'] == 'BNT']['importe'].sum()))
    st.divider()

columnas_deseadas = ['referencia', 'importe', 'banco', 'tipoPago', 'fechaPago']
df_deseado = df[columnas_deseadas]

with st.container(border=True):
    col1, col2 = st.columns((2, 2), gap='large')
    with col1:
        st.subheader("📊 NÚMERO DE PAGOS REALIZADOS POR BANCO")
        st.bar_chart(df['banco'].str.upper().value_counts(), x_label="INSTITUCIONES FINANCIERAS", y_label="FRECUENCIA")
    with col2:
        st.subheader("📊 CANTIDAD DE PAGOS POR TIPO")
        st.bar_chart(df['tipoPago'].str.upper().value_counts(), x_label="TIPO DE PAGO", y_label="FRECUENCIA")

#df_selection_default = ['BANAMEX', 'HSBC', 'BANCOMER', 'BANORTE']
with st.container(border=True):
    st.subheader("🔎    FILTRAR RESULTADOS")
    col1, col2 = st.columns((2, 2), gap='medium')
    with col1:
        banco_selection = st.multiselect("📌    SELECCIONA LA INSTITUCIÓN FINANCIERA:", options=df['banco'].unique(), placeholder="Elige una opción")
    with col2:
        tipo_pago_selection = st.multiselect(" 📌   SELECCIONA EL TIPO DE PAGO:", options=df['tipoPago'].unique(), placeholder="Elige una opción")
    
    if tipo_pago_selection and banco_selection:
        df_selection = df.query("banco == @banco_selection & tipoPago == @tipo_pago_selection")
    elif tipo_pago_selection and not banco_selection: 
        df_selection = df.query("tipoPago == @tipo_pago_selection")
    elif not tipo_pago_selection and banco_selection: 
        df_selection = df.query("banco == @banco_selection")
    else:
        df_selection = df

    total_filter = int(df_selection['importe'].sum())
    st.dataframe(df_selection[columnas_deseadas], width=2000, height=500)

    with st.container(border=True):
        columna1, columna2 = st.columns((3, 2), gap='medium')
        with columna1:
            columna1.metric("TOTAL DE RESULTADOS:", "{:,}".format(len(df_selection)), delta_color='normal')
        with columna2:
            columna2.metric("IMPORTE TOTAL DE RESULTADOS:", "{:,}".format(df_selection['importe'].sum()))
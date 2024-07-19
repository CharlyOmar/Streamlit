import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title='Streamlit App', page_icon='📈', layout='wide')
df = pd.read_excel('Analisis-de-Archivo.xlsx', sheet_name='SPEI')

st.title("📉DASHBOARD SPEI📈")

with st.container(border=True):
    st.subheader("DINERO TOTAL DE ACUERDO AL BANCO")
    col1, col2, col3, col4 = st.columns((2, 2, 2, 2), gap='medium')
    with col1:
        col1.metric("Total HSBC", df[df['claveBanco'] == 'HSB']['importe'].sum())
    with col2:
        col2.metric("Total BBVA", df[df['claveBanco'] == 'BBV']['importe'].sum())
    with col3:
        col3.metric("Total BANAMEX", df[df['claveBanco'] == 'BAN']['importe'].sum())
    with col4:
        col4.metric("Total BANORTE", df[df['claveBanco'] == 'BNT']['importe'].sum())
    st.divider()

columnas_deseadas = ['referencia', 'importe', 'banco', 'tipoPago', 'fechaPago', 'tipoTarjeta']
df_seleccionado = df[columnas_deseadas]
st.dataframe(df_seleccionado, width=2000, height=500)

with st.container(border=True):
    col1, col2 = st.columns((2, 2), gap='medium')
    with col1:
        st.subheader("NÚMERO DE PAGOS REALIZADOS POR BANCO")
        st.bar_chart(df['banco'].str.upper().value_counts(), x_label="INSTITUCIONES FINANCIERAS", y_label="FRECUENCIA")
    with col2:
        st.subheader("CANTIDAD DE PAGOS POR TIPO")
        st.bar_chart(df['tipoPago'].str.upper().value_counts(), x_label="TIPO DE PAGO", y_label="FRECUENCIA")


with st.container(border=True):
    st.subheader("RESULTADOS POR FILTRO")
    col1, col2 = st.columns((2, 2), gap='medium')
    with col1:
        banco_selection = st.multiselect("Selecciona un Banco:", options=df['banco'].unique(), placeholder="Elige una opción", default='BANCOMER')
    with col2:
        tipo_pago_selection = st.multiselect("Selecciona un tipo de pago:", options=df['tipoPago'].unique(), placeholder="Elige una opción", default='TR')

    df_selection = df.query("banco == @banco_selection & tipoPago == @tipo_pago_selection")
    total_filter = int(df_selection['importe'].sum())

    st.markdown(f"**EL TOTAL DE LOS RESULTADOS OBTENIDOS MEDIANTE LOS FILTROS ES: $ :blue[ _{total_filter}_]  MXN**")
    # Crear el gráfico de barras
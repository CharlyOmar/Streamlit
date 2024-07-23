import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title='SPEI page', page_icon='📈', layout='wide')
df = pd.read_excel('Analisis-de-Archivo.xlsx', sheet_name='SPEI')

tipos_pagos = {
    'TR':'Transferencia',
    'MN':'Moneda',
    'CH':'Cheque',
    'TD':'Tarjeta de Débito',
    'TC':'Tarjeta de Crédito'
}

columnas_deseadas = ['referencia', 'importe', 'banco', 'tipoPago', 'fechaPago']
df_deseado = df[columnas_deseadas]

st.title("📋    ANALYTICS")

#Dentro del siguiente contenedor se declararon 4 columnas, en las cuales se muestra el total
# de los importes de acuerdo a cada banco. 
with st.container(border=True):
    st.subheader("💰 DINERO TOTAL DE ACUERDO AL BANCO 🏦")
    #En la siguinete linea se declaran las columnas y el ancho del espacio entre ellas como 'small' 
    col1, col2, col3, col4 = st.columns((2, 2, 2, 2), gap='small', vertical_alignment='center')
    #En la columna #1 se muestra la suma del importe de todos los valores cuya claveBanco sea igual a HSB
    with col1:
        col1.metric("TOTAL HSBC", "{:,}".format(df[df['claveBanco'] == 'HSB']['importe'].sum()))
    #En la columna #1 se muestra la suma del importe de todos los valores cuya claveBanco sea igual a BBV
    with col2:
        col2.metric("TOTAL BBVA", "{:,}".format(df[df['claveBanco'] == 'BBV']['importe'].sum()))
    #En la columna #1 se muestra la suma del importe de todos los valores cuya claveBanco sea igual a BAN
    with col3:
        col3.metric("TOTAL BANAMEX", "{:,}".format(df[df['claveBanco'] == 'BAN']['importe'].sum()))
        #En la columna #1 se muestra la suma del importe de todos los valores cuya claveBanco sea igual a BNT
    with col4:
        col4.metric("TOTAL BANORTE", "{:,}".format(df[df['claveBanco'] == 'BNT']['importe'].sum()))

with st.container(border=True):
    col1, col2 = st.columns((2, 2), gap='large')
    with col1:
        st.subheader("📊 CANTIDAD DE PAGOS POR BANCO")
        #Se crea la gráfica de barras del total de pagos por banco
        st.bar_chart(df['banco'].str.upper().value_counts(), 
                    x_label="INSTITUCIONES FINANCIERAS",
                    y_label="FRECUENCIA")
    with col2:
        st.subheader("📊 CANTIDAD DE PAGOS POR TIPO")
        #Se crea la gráfica de barras del total de pagos de acuerdo al tipo
        st.bar_chart(df['tipoPago'].str.upper().value_counts(),
                    x_label="TIPO DE PAGO",
                    y_label="FRECUENCIA")

with st.container(border=True):
    st.subheader("🔎    FILTRAR RESULTADOS")
    col1, col2 = st.columns((2, 2), gap='small')
    with col1:
        banco_selection = st.multiselect("📌    SELECCIONA LA INSTITUCIÓN FINANCIERA:",
                                        #Se obtienen los bancos existentes
                                        options=df['banco'].unique(),
                                        placeholder="Elige una opción")
    with col2:
        tipo_pago_selection = st.multiselect(" 📌   SELECCIONA EL TIPO DE PAGO:",
                                            #Se obtienen los tipos de pago
                                            options=df['tipoPago'].unique(),
                                            placeholder="Elige una opción")
    
#En las siguientes lineas se pregunta si hay un valor seleccionado
#Si no hay. Se muestra como si estuvieran seleccionados todos
#Si hay, se muestran solamente los que concuenrdan con lo seleccionado
    if tipo_pago_selection and banco_selection:
        df_selection = df.query("banco == @banco_selection & tipoPago == @tipo_pago_selection")
    elif tipo_pago_selection and not banco_selection: 
        df_selection = df.query("tipoPago == @tipo_pago_selection")
    elif not tipo_pago_selection and banco_selection: 
        df_selection = df.query("banco == @banco_selection")
    else:
        df_selection = df

    #Se suma el importe de todos los valores que concordaron con los filtros
    total_filter = int(df_selection['importe'].sum())
    st.dataframe(df_selection[columnas_deseadas], width=2000, height=500)

    with st.container(border=True):
        columna1, columna2 = st.columns((2, 2), gap='medium', vertical_alignment='center')
        with columna1:
            columna1.metric("TOTAL DE RESULTADOS:",
                            #Se muestra el resultado usando formato (se separa con coma por milesimas)
                            "{:,}".format(len(df_selection)))
        with columna2:
            columna2.metric("IMPORTE TOTAL DE RESULTADOS:",
                            #Se muestra el resultado usando formato (se separa con coma por milesimas)
                            "{:,}".format(df_selection['importe'].sum()))
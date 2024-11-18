
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Título de la app
st.title('Registro de Finanzas Personales')

# Quien elabora
st.write("Esta app fue elaborada por Felipe Devia.")

# Datos simulados para ejemplo
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame({
        'Fecha': [datetime.now() - timedelta(days=i) for i in range(10)],
        'Ingreso': [3000, 2000, 2500, 3000, 2700, 3200, 2800, 3000, 3500, 3000],
        'Gasto': [2000, 1500, 1700, 2100, 1900, 2500, 2300, 2200, 2600, 2400],
        'Meta Ahorro': [500, 400, 450, 500, 550, 600, 500, 450, 550, 500],
        'Presupuesto': [1000, 900, 950, 1000, 1100, 1200, 1000, 950, 1100, 1000]
    })
    st.session_state.data['Fecha'] = pd.to_datetime(st.session_state.data['Fecha'])

# Mostrar datos
st.subheader('Datos Financieros')
st.write(st.session_state.data)

# Seleccionar rango de fechas para el reporte
fecha_inicio = st.date_input('Selecciona la fecha de inicio', datetime.now() - timedelta(weeks=4))
fecha_fin = st.date_input('Selecciona la fecha de fin', datetime.now())

# Filtrar los datos según el rango de fechas seleccionado
data_filtrada = st.session_state.data[(st.session_state.data['Fecha'] >= pd.to_datetime(fecha_inicio)) & (st.session_state.data['Fecha'] <= pd.to_datetime(fecha_fin))]

# Cálculos de diferencia entre lo presupuestado y lo real
data_filtrada['Diferencia Ingreso'] = data_filtrada['Ingreso'] - data_filtrada['Presupuesto']
data_filtrada['Diferencia Gasto'] = data_filtrada['Gasto'] - data_filtrada['Presupuesto']
data_filtrada['Diferencia Ahorro'] = (data_filtrada['Ingreso'] - data_filtrada['Gasto']) - data_filtrada['Meta Ahorro']

# Mostrar los reportes
st.subheader('Reporte de Finanzas')
st.write(data_filtrada)

# Resumen semanal
resumen_semanal = data_filtrada.resample('W-Mon', on='Fecha').agg({
    'Ingreso': 'sum',
    'Gasto': 'sum',
    'Meta Ahorro': 'sum',
    'Presupuesto': 'sum',
    'Diferencia Ingreso': 'sum',
    'Diferencia Gasto': 'sum',
    'Diferencia Ahorro': 'sum'
}).reset_index()

st.subheader('Resumen Semanal')
st.write(resumen_semanal)

# Resumen mensual
resumen_mensual = data_filtrada.resample('M', on='Fecha').agg({
    'Ingreso': 'sum',
    'Gasto': 'sum',
    'Meta Ahorro': 'sum',
    'Presupuesto': 'sum',
    'Diferencia Ingreso': 'sum',
    'Diferencia Gasto': 'sum',
    'Diferencia Ahorro': 'sum'
}).reset_index()

st.subheader('Resumen Mensual')
st.write(resumen_mensual)

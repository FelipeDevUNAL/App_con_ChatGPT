
import streamlit as st
import pandas as pd
from datetime import datetime

# Título de la app
st.title('Registro de Finanzas Personales')

st.write("Esta app fue elaborada por Felipe Devia.")


# Crear un DataFrame vacío para guardar los datos ingresados
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=['Fecha', 'Ingreso', 'Gasto', 'Meta Ahorro', 'Presupuesto'])

# Ingreso de datos por parte del usuario
st.subheader('Ingresar Datos Financieros')

# Entrada para fecha (por defecto el día de hoy)
fecha = st.date_input('Fecha', datetime.today())

# Entrada para ingresos, gastos, meta de ahorro y presupuesto
ingreso = st.number_input('Ingreso', min_value=0, step=100)
gasto = st.number_input('Gasto', min_value=0, step=100)
meta_ahorro = st.number_input('Meta de Ahorro', min_value=0, step=100)
presupuesto = st.number_input('Presupuesto', min_value=0, step=100)

# Botón para agregar los datos al DataFrame
if st.button('Agregar'):
    # Crear un nuevo registro y agregarlo al DataFrame
    nuevo_registro = {
        'Fecha': fecha,
        'Ingreso': ingreso,
        'Gasto': gasto,
        'Meta Ahorro': meta_ahorro,
        'Presupuesto': presupuesto
    }
    
    st.session_state.data = st.session_state.data.append(nuevo_registro, ignore_index=True)
    st.success('Datos agregados correctamente')

# Mostrar los datos ingresados
st.subheader('Datos Financieros Ingresados')
st.write(st.session_state.data)

# Cálculos de la diferencia entre lo presupuestado y lo real
st.subheader('Cálculos de Diferencias')
st.session_state.data['Diferencia Ingreso'] = st.session_state.data['Ingreso'] - st.session_state.data['Presupuesto']
st.session_state.data['Diferencia Gasto'] = st.session_state.data['Gasto'] - st.session_state.data['Presupuesto']
st.session_state.data['Diferencia Ahorro'] = (st.session_state.data['Ingreso'] - st.session_state.data['Gasto']) - st.session_state.data['Meta Ahorro']

# Mostrar los cálculos con las diferencias
st.write(st.session_state.data)

# Reportes (resúmenes semanales y mensuales)
st.subheader('Resumen Semanal')

# Resumen semanal utilizando la fecha de los datos
data_semanal = st.session_state.data.set_index('Fecha').resample('W-Mon').agg({
    'Ingreso': 'sum',
    'Gasto': 'sum',
    'Meta Ahorro': 'sum',
    'Presupuesto': 'sum',
    'Diferencia Ingreso': 'sum',
    'Diferencia Gasto': 'sum',
    'Diferencia Ahorro': 'sum'
}).reset_index()

st.write(data_semanal)

# Reporte mensual
st.subheader('Resumen Mensual')
data_mensual = st.session_state.data.set_index('Fecha').resample('M').agg({
    'Ingreso': 'sum',
    'Gasto': 'sum',
    'Meta Ahorro': 'sum',
    'Presupuesto': 'sum',
    'Diferencia Ingreso': 'sum',
    'Diferencia Gasto': 'sum',
    'Diferencia Ahorro': 'sum'
}).reset_index()

st.write(data_mensual)

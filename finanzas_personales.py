import streamlit as st
import pandas as pd
from datetime import datetime

# Título de la app
st.title('Registro de Finanzas Personales')

st.write("Esta app fue elaborada por Felipe Devia.")


# Crear un DataFrame vacío para guardar los datos de ingresos, gastos, y metas
if 'ingresos' not in st.session_state:
    st.session_state.ingresos = pd.DataFrame(columns=['Fecha', 'Monto', 'Categoria'])
if 'gastos' not in st.session_state:
    st.session_state.gastos = pd.DataFrame(columns=['Fecha', 'Monto', 'Categoria'])
if 'metas' not in st.session_state:
    st.session_state.metas = {'ahorro': 0, 'presupuesto_ingresos': 0, 'presupuesto_gastos': 0, 'periodo': 'mensual'}

# Sección de ingreso de ingresos
st.subheader('Formulario de Ingresos')
fecha_ingreso = st.date_input('Fecha de Ingreso', datetime.today())
monto_ingreso = st.number_input('Monto de Ingreso', min_value=0, step=100)
categoria_ingreso = st.text_input('Categoría de Ingreso')

if st.button('Registrar Ingreso'):
    nuevo_ingreso = {
        'Fecha': fecha_ingreso,
        'Monto': monto_ingreso,
        'Categoria': categoria_ingreso
    }
    st.session_state.ingresos = st.session_state.ingresos.append(nuevo_ingreso, ignore_index=True)
    st.success('Ingreso registrado correctamente')

# Sección de ingreso de gastos
st.subheader('Formulario de Gastos')
fecha_gasto = st.date_input('Fecha de Gasto', datetime.today())
monto_gasto = st.number_input('Monto de Gasto', min_value=0, step=100)
categoria_gasto = st.text_input('Categoría de Gasto')

if st.button('Registrar Gasto'):
    nuevo_gasto = {
        'Fecha': fecha_gasto,
        'Monto': monto_gasto,
        'Categoria': categoria_gasto
    }
    st.session_state.gastos = st.session_state.gastos.append(nuevo_gasto, ignore_index=True)
    st.success('Gasto registrado correctamente')

# Sección de Metas de Ahorro y Presupuesto
st.subheader('Establecer Metas de Ahorro y Presupuesto')

# Formulario para definir metas y presupuesto
meta_ahorro = st.number_input('Meta de Ahorro', min_value=0, step=100)
presupuesto_ingresos = st.number_input('Presupuesto de Ingresos', min_value=0, step=100)
presupuesto_gastos = st.number_input('Presupuesto de Gastos', min_value=0, step=100)

# Selección del período (mensual o semanal)
periodo = st.selectbox('Periodo de la meta', ('mensual', 'semanal'))

# Guardar las metas en el estado de la sesión
if st.button('Guardar Meta y Presupuesto'):
    st.session_state.metas['ahorro'] = meta_ahorro
    st.session_state.metas['presupuesto_ingresos'] = presupuesto_ingresos
    st.session_state.metas['presupuesto_gastos'] = presupuesto_gastos
    st.session_state.metas['periodo'] = periodo
    st.success('Meta y presupuesto guardados correctamente')

# Mostrar las metas y presupuesto
st.write(f"### Meta de Ahorro: {st.session_state.metas['ahorro']}")
st.write(f"### Presupuesto de Ingresos: {st.session_state.metas['presupuesto_ingresos']}")
st.write(f"### Presupuesto de Gastos: {st.session_state.metas['presupuesto_gastos']}")
st.write(f"### Periodo: {st.session_state.metas['periodo']}")

# Mostrar los datos de ingresos y gastos
st.subheader('Resumen de Transacciones')
st.write("### Ingresos")
st.write(st.session_state.ingresos)

st.write("### Gastos")
st.write(st.session_state.gastos)

# Calcular las diferencias entre lo presupuestado y lo real para los ingresos y los gastos
st.subheader('Diferencias entre lo Real y lo Presupuestado')

# Calcular las sumas de los ingresos y los gastos
total_ingresos = st.session_state.ingresos['Monto'].sum()
total_gastos = st.session_state.gastos['Monto'].sum()

# Calcular las diferencias
diferencia_ingresos = total_ingresos - st.session_state.metas['presupuesto_ingresos']
diferencia_gastos = total_gastos - st.session_state.metas['presupuesto_gastos']

# Mostrar los resultados
st.write(f"Total Ingresos: {total_ingresos}")
st.write(f"Total Gastos: {total_gastos}")
st.write(f"Diferencia de Ingresos (Real - Presupuesto): {diferencia_ingresos}")
st.write(f"Diferencia de Gastos (Real - Presupuesto): {diferencia_gastos}")

# Comprobar si las metas fueron superadas
if total_ingresos > st.session_state.metas['presupuesto_ingresos']:
    st.write("¡Has superado el presupuesto de ingresos!")
else:
    st.write("No has superado el presupuesto de ingresos.")

if total_gastos < st.session_state.metas['presupuesto_gastos']:
    st.write("¡Has ahorrado, ya que tus gastos están por debajo del presupuesto!")
else:
    st.write("No has ahorrado, tus gastos superan el presupuesto.")

if total_ingresos >= st.session_state.metas['ahorro']:
    st.write("¡Has alcanzado tu meta de ahorro!")
else:
    st.write(f"No has alcanzado tu meta de ahorro. Te falta {st.session_state.metas['ahorro'] - total_ingresos}.")

# Reporte semanal de ingresos y gastos
st.subheader('Reporte Semanal')

# Filtrar por semana
fecha_actual = datetime.today()
semana_actual = fecha_actual.isocalendar()[1]
ingresos_semanales = st.session_state.ingresos[st.session_state.ingresos['Fecha'].dt.isocalendar().week == semana_actual]
gastos_semanales = st.session_state.gastos[st.session_state.gastos['Fecha'].dt.isocalendar().week == semana_actual]

st.write(f"### Ingresos Semanales (Semana {semana_actual})")
st.write(ingresos_semanales)
st.write(f"Total Ingresos Semana: {ingresos_semanales['Monto'].sum()}")

st.write(f"### Gastos Semanales (Semana {semana_actual})")
st.write(gastos_semanales)
st.write(f"Total Gastos Semana: {gastos_semanales['Monto'].sum()}")

# Reporte mensual de ingresos y gastos
st.subheader('Reporte Mensual')

# Filtrar por mes
mes_actual = fecha_actual.month
ingresos_mensuales = st.session_state.ingresos[st.session_state.ingresos['Fecha'].dt.month == mes_actual]
gastos_mensuales = st.session_state.gastos[st.session_state.gastos['Fecha'].dt.month == mes_actual]

st.write(f"### Ingresos Mensuales (Mes {mes_actual})")
st.write(ingresos_mensuales)
st.write(f"Total Ingresos Mes: {ingresos_mensuales['Monto'].sum()}")

st.write(f"### Gastos Mensuales (Mes {mes_actual})")
st.write(gastos_mensuales)
st.write(f"Total Gastos Mes: {gastos_mensuales['Monto'].sum()}")

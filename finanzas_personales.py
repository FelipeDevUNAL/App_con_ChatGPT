
import streamlit as st
import pandas as pd
from datetime import datetime

# Inicializar los estados de sesión para ingresos, gastos y metas si no existen
if 'ingresos' not in st.session_state:
    st.session_state.ingresos = pd.DataFrame(columns=['Fecha', 'Monto', 'Categoria'])
if 'gastos' not in st.session_state:
    st.session_state.gastos = pd.DataFrame(columns=['Fecha', 'Monto', 'Categoria'])
if 'metas' not in st.session_state:
    st.session_state.metas = pd.DataFrame(columns=['Meta', 'Monto', 'Frecuencia', 'Fecha'])

# Función para convertir fecha a datetime
def convertir_fecha(fecha):
    return datetime.strptime(str(fecha), '%Y-%m-%d')

# Formulario para seleccionar el módulo (Ingreso, Gasto o Meta)
opcion_seleccionada = st.sidebar.radio("Selecciona una opción", ('Ingreso', 'Gasto', 'Meta'))

# Formulario para ingresar datos de ingresos
if opcion_seleccionada == 'Ingreso':
    st.subheader('Formulario de Ingresos')
    fecha_ingreso = st.date_input('Fecha de Ingreso', datetime.today())  # Campo para la fecha
    monto_ingreso = st.number_input('Monto de Ingreso', min_value=0, step=100)
    categoria_ingreso = st.text_input('Categoría de Ingreso')
    
    if st.button('Registrar Ingreso'):
        nuevo_ingreso = {
            'Fecha': convertir_fecha(fecha_ingreso),  # Convertir a datetime
            'Monto': monto_ingreso,
            'Categoria': categoria_ingreso
        }
        st.session_state.ingresos = pd.concat([st.session_state.ingresos, pd.DataFrame([nuevo_ingreso])], ignore_index=True)
        st.success('Ingreso registrado correctamente')

# Formulario para ingresar datos de gastos
elif opcion_seleccionada == 'Gasto':
    st.subheader('Formulario de Gastos')
    fecha_gasto = st.date_input('Fecha de Gasto', datetime.today())  # Campo para la fecha
    monto_gasto = st.number_input('Monto de Gasto', min_value=0, step=100)
    categoria_gasto = st.text_input('Categoría de Gasto')

    if st.button('Registrar Gasto'):
        nuevo_gasto = {
            'Fecha': convertir_fecha(fecha_gasto),  # Convertir a datetime
            'Monto': monto_gasto,
            'Categoria': categoria_gasto
        }
        st.session_state.gastos = pd.concat([st.session_state.gastos, pd.DataFrame([nuevo_gasto])], ignore_index=True)
        st.success('Gasto registrado correctamente')

# Formulario para ingresar metas de ahorro
elif opcion_seleccionada == 'Meta':
    st.subheader('Formulario de Metas de Ahorro')
    meta = st.text_input('Meta de Ahorro')
    monto_meta = st.number_input('Monto Objetivo de Ahorro', min_value=0, step=100)
    frecuencia = st.radio('Frecuencia de la Meta', ['Semanal', 'Mensual'])
    fecha_meta = st.date_input('Fecha de la Meta', datetime.today())
    
    if st.button('Registrar Meta de Ahorro'):
        nueva_meta = {
            'Meta': meta,
            'Monto': monto_meta,
            'Frecuencia': frecuencia,
            'Fecha': convertir_fecha(fecha_meta)
        }
        st.session_state.metas = pd.concat([st.session_state.metas, pd.DataFrame([nueva_meta])], ignore_index=True)
        st.success('Meta de Ahorro registrada correctamente')

# Reporte de ingresos y gastos por semana o mes
if st.sidebar.checkbox('Generar Reporte'):
    reporte_opcion = st.sidebar.selectbox('Seleccionar Reporte', ['Semanal', 'Mensual'])
    semana_actual = datetime.today().isocalendar()[1]
    
    # Filtrar los ingresos y gastos por semana o mes
    if reporte_opcion == 'Semanal':
        ingresos_semanales = st.session_state.ingresos[st.session_state.ingresos['Fecha'].dt.isocalendar().week == semana_actual]
        gastos_semanales = st.session_state.gastos[st.session_state.gastos['Fecha'].dt.isocalendar().week == semana_actual]
    else:
        ingresos_semanales = st.session_state.ingresos[st.session_state.ingresos['Fecha'].dt.month == datetime.today().month]
        gastos_semanales = st.session_state.gastos[st.session_state.gastos['Fecha'].dt.month == datetime.today().month]
    
    # Mostrar reportes
    st.write(f"**Reporte {reporte_opcion}**")
    st.write(f"**Ingresos**")
    st.write(ingresos_semanales)
    st.write(f"**Gastos**")
    st.write(gastos_semanales)
    
    # Calcular y mostrar las diferencias
    ingresos_totales = ingresos_semanales['Monto'].sum()
    gastos_totales = gastos_semanales['Monto'].sum()
    
    st.write(f"**Total Ingresos:** {ingresos_totales}")
    st.write(f"**Total Gastos:** {gastos_totales}")
    st.write(f"**Balance:** {ingresos_totales - gastos_totales}")

# Reporte de metas de ahorro
if st.sidebar.checkbox('Generar Reporte de Metas de Ahorro'):
    metas_actuales = st.session_state.metas
    st.write("**Reporte de Metas de Ahorro**")
    st.write(metas_actuales)
    
    # Calcular si se ha alcanzado la meta de ahorro
    for index, meta in metas_actuales.iterrows():
        monto_actual = st.session_state.gastos[st.session_state.gastos['Fecha'] <= meta['Fecha']]['Monto'].sum()
        if monto_actual >= meta['Monto']:
            st.write(f"Meta alcanzada: {meta['Meta']} con monto ahorrado de {monto_actual}")
        else:
            st.write(f"Meta no alcanzada: {meta['Meta']} con monto ahorrado de {monto_actual}")

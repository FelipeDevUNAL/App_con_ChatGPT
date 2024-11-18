
import streamlit as st
import pandas as pd

# Título de la app
st.title("Registro de Finanzas Personales")

# Sección para ingresar presupuesto y meta de ahorro
st.header("Configuración inicial")

if 'presupuesto' not in st.session_state:
    st.session_state.presupuesto = 0.0
    st.session_state.meta_ahorro = 0.0

# Inputs para presupuesto y meta de ahorro (si no han sido ingresados previamente)
presupuesto = st.number_input(
    "Presupuesto total mensual", 
    min_value=0.0, 
    step=100.0, 
    value=st.session_state.presupuesto
)
meta_ahorro = st.number_input(
    "Meta de ahorro mensual", 
    min_value=0.0, 
    step=100.0, 
    value=st.session_state.meta_ahorro
)

# Guardar presupuesto y meta en sesión
if st.button("Guardar configuración"):
    st.session_state.presupuesto = presupuesto
    st.session_state.meta_ahorro = meta_ahorro
    st.success("¡Configuración guardada!")

st.write(f"Presupuesto actual: **{st.session_state.presupuesto:.2f}**")
st.write(f"Meta de ahorro actual: **{st.session_state.meta_ahorro:.2f}**")

# Entradas de ingresos y gastos
st.header("Ingresos y Gastos")
ingreso = st.number_input("Ingresos del día", min_value=0.0, step=100.0)
gastos = st.number_input("Gastos del día", min_value=0.0, step=100.0)

# Crear un DataFrame para almacenar los registros
if 'finanzas' not in st.session_state:
    st.session_state.finanzas = pd.DataFrame(columns=["Fecha", "Ingresos", "Gastos"])

# Botón para guardar ingresos y gastos
if st.button("Guardar registro"):
    fecha_actual = pd.to_datetime("today").strftime("%Y-%m-%d")
    nuevo_registro = pd.DataFrame([[fecha_actual, ingreso, gastos]], 
                                  columns=["Fecha", "Ingresos", "Gastos"])
    st.session_state.finanzas = pd.concat([st.session_state.finanzas, nuevo_registro], ignore_index=True)
    st.success(f"Registro guardado para {fecha_actual}.")

# Mostrar los registros de finanzas
st.subheader("Registros de Finanzas")
st.dataframe(st.session_state.finanzas)

# Cálculos globales
total_ingresos = st.session_state.finanzas["Ingresos"].sum()
total_gastos = st.session_state.finanzas["Gastos"].sum()
ahorro_real = total_ingresos - total_gastos
diferencia_presupuesto = st.session_state.presupuesto - total_gastos
diferencia_meta_ahorro = ahorro_real - st.session_state.meta_ahorro

# Resultados y alertas
st.subheader("Resultados")
st.write(f"Total de ingresos: **{total_ingresos:.2f}**")
st.write(f"Total de gastos: **{total_gastos:.2f}**")
st.write(f"Ahorro real: **{ahorro_real:.2f}**")

# Verificar presupuesto
if total_gastos > st.session_state.presupuesto:
    st.error(f"¡Has excedido el presupuesto por **{abs(diferencia_presupuesto):.2f}**!")
else:
    st.success(f"Estás dentro del presupuesto. Te sobran **{diferencia_presupuesto:.2f}**.")

# Verificar meta de ahorro
if ahorro_real >= st.session_state.meta_ahorro:
    st.success(f"¡Has alcanzado la meta de ahorro con una diferencia de **{diferencia_meta_ahorro:.2f}**!")
else:
    st.warning(f"No has alcanzado la meta de ahorro. Te faltan **{abs(diferencia_meta_ahorro):.2f}**.")


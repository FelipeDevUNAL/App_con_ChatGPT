

import streamlit as st
import pandas as pd
import numpy as np

# Título de la app
st.title("Registro de Finanzas Personales")

# Autor de la aplicación
st.write("Esta app fue elaborada por Felipe Devia.")

# Datos de presupuesto y meta de ahorro (se ingresan solo una vez)
if 'presupuesto' not in st.session_state:
    st.session_state.presupuesto = st.number_input("Presupuesto total", min_value=0.0, step=1000.0)
    st.session_state.meta_ahorro = st.number_input("Meta de ahorro mensual", min_value=0.0, step=100.0)
    st.session_state.meta_ahorro_alcanzada = None
    st.session_state.presupuesto_superado = None

# Entradas de ingresos y gastos
st.header("Ingresos y Gastos")
ingreso = st.number_input("Ingresos totales", min_value=0.0, step=1000.0)
gastos = st.number_input("Gastos totales", min_value=0.0, step=1000.0)

# Crear un DataFrame para almacenar los registros de finanzas
if 'finanzas' not in st.session_state:
    st.session_state.finanzas = pd.DataFrame(columns=["Fecha", "Ingresos", "Gastos"])

# Registrar los ingresos y gastos con la fecha actual
if st.button("Guardar registro"):
    fecha_actual = pd.to_datetime("today").strftime("%Y-%m-%d")
    nuevo_registro = pd.DataFrame([[fecha_actual, ingreso, gastos]],
                                  columns=["Fecha", "Ingresos", "Gastos"])
    st.session_state.finanzas = pd.concat([st.session_state.finanzas, nuevo_registro], ignore_index=True)
    st.success(f"Registro guardado para {fecha_actual}.")

# Mostrar los registros
st.subheader("Registros de Finanzas")
st.dataframe(st.session_state.finanzas)

# Calcular si se superó el presupuesto y si se alcanzó la meta de ahorro
total_gastos = st.session_state.finanzas["Gastos"].sum()
total_ingresos = st.session_state.finanzas["Ingresos"].sum()

# Comprobar si el presupuesto fue superado
st.session_state.presupuesto_superado = total_gastos > st.session_state.presupuesto

# Calcular si se alcanzó la meta de ahorro
ahorro_real = total_ingresos - total_gastos
st.session_state.meta_ahorro_alcanzada = ahorro_real >= st.session_state.meta_ahorro

# Mostrar resultados
st.subheader("Resumen")
st.write(f"Total de ingresos: {total_ingresos:.2f}")
st.write(f"Total de gastos: {total_gastos:.2f}")

# Verificar si el presupuesto fue superado
if st.session_state.presupuesto_superado:
    st.write("¡El presupuesto ha sido superado!")
else:
    st.write("No se ha superado el presupuesto.")

# Verificar si se alcanzó la meta de ahorro
if st.session_state.meta_ahorro_alcanzada:
    st.write(f"¡Meta de ahorro alcanzada! Ahorro real: {ahorro_real:.2f}")
else:
    st.write(f"No se alcanzó la meta de ahorro. Ahorro real: {ahorro_real:.2f}")

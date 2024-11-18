
import streamlit as st
import pandas as pd
import numpy as np

# Título de la app
st.title("Registro de Finanzas Personales")

# Entradas de presupuesto, ingresos y gastos
st.header("Ingresos y Gastos")
ingreso = st.number_input("Ingresos totales", min_value=0.0, step=1000.0)
presupuesto = st.number_input("Presupuesto total", min_value=0.0, step=1000.0)
gastos = st.number_input("Gastos totales", min_value=0.0, step=1000.0)

# Definir las metas de ahorro
meta_ahorro = st.number_input("Meta de ahorro mensual", min_value=0.0, step=100.0)

# Crear un DataFrame para almacenar los registros de finanzas
if 'finanzas' not in st.session_state:
    st.session_state.finanzas = pd.DataFrame(columns=["Fecha", "Ingresos", "Presupuesto", "Gastos", "Meta Ahorro"])

# Registrar las finanzas con la fecha actual
if st.button("Guardar registro"):
    fecha_actual = pd.to_datetime("today").strftime("%Y-%m-%d")
    nuevo_registro = pd.DataFrame([[fecha_actual, ingreso, presupuesto, gastos, meta_ahorro]],
                                  columns=["Fecha", "Ingresos", "Presupuesto", "Gastos", "Meta Ahorro"])
    st.session_state.finanzas = pd.concat([st.session_state.finanzas, nuevo_registro], ignore_index=True)
    st.success(f"Registro guardado para {fecha_actual}.")

# Mostrar los registros
st.subheader("Registros de Finanzas")
st.dataframe(st.session_state.finanzas)

# Cálculos de diferencias
st.subheader("Diferencias entre lo presupuestado y lo real")

# Calcular la diferencia semanal
finanzas_semanales = st.session_state.finanzas.set_index("Fecha").resample('W').sum()
finanzas_semanales["Diferencia Presupuesto vs Real"] = finanzas_semanales["Presupuesto"] - finanzas_semanales["Gastos"]
st.write("Reporte Semanal")
st.dataframe(finanzas_semanales[["Ingresos", "Presupuesto", "Gastos", "Diferencia Presupuesto vs Real"]])

# Calcular la diferencia mensual
finanzas_mensuales = st.session_state.finanzas.set_index("Fecha").resample('M').sum()
finanzas_mensuales["Diferencia Presupuesto vs Real"] = finanzas_mensuales["Presupuesto"] - finanzas_mensuales["Gastos"]
st.write("Reporte Mensual")
st.dataframe(finanzas_mensuales[["Ingresos", "Presupuesto", "Gastos", "Diferencia Presupuesto vs Real"]])

# Análisis de ahorro
st.subheader("Análisis de Ahorro")
ahorro_total = st.session_state.finanzas["Ingresos"].sum() - st.session_state.finanzas["Gastos"].sum()
st.write(f"Ahorro total acumulado: {ahorro_total:.2f}")
st.write(f"Meta de ahorro mensual: {meta_ahorro:.2f}")

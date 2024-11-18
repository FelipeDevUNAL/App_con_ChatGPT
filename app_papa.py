
import streamlit as st

# Título de la aplicación
st.title("Cálculo del PAPA")

st.write("Esta app fue elaborada por Felipe Devia.")


# Obtener los datos del usuario
num_materias = st.number_input("Ingrese el número de materias cursadas:", min_value=1)

materias = []
for i in range(num_materias):
    materia = {}
    materia['nombre'] = st.text_input(f"Nombre de la materia {i+1}:")
    materia['tipologia'] = st.selectbox(f"Tipología de la materia {i+1}:", options=["DISCIPLINAR OPTATIVA", "FUND. OBLIGATORIA", "FUND. OPTATIVA", "DISCIPLINAR OBLIGATORIA", "LIBRE ELECCIÓN", "TRABAJO DE GRADO"])
    materia['calificacion'] = st.number_input(f"Calificación de la materia {i+1}:", min_value=0.0, max_value=5.0)
    materia['creditos'] = st.number_input(f"Créditos de la materia {i+1}:", min_value=1)
    materias.append(materia)

# Calcular el PAPA
suma_productos = 0
total_creditos = 0
for materia in materias:
    if materia['calificacion'] > 0:
        suma_productos += materia['calificacion'] * materia['creditos']
        total_creditos += materia['creditos']

# Verificar si se puede calcular el PAPA
if total_creditos > 1:
    papa = suma_productos / total_creditos
    st.success(f"El PAPA calculado es: {papa:.2f}")
else:
    st.warning("No se puede calcular el PAPA con los datos ingresados.")

# Mostrar el desglose por tipología (opcional)
if st.checkbox("Mostrar desglose por tipología"):
    tipologias = {}
    for materia in materias:
        if materia['calificacion'] > 0:
            if materia['tipologia'] not in tipologias:
                tipologias[materia['tipologia']] = {'suma_productos': 0, 'total_creditos': 0}
            tipologias[materia['tipologia']]['suma_productos'] += materia['calificacion'] * materia['creditos']
            tipologias[materia['tipologia']]['total_creditos'] += materia['creditos']

    for tipologia, datos in tipologias.items():
        papa_tipologia = datos['suma_productos'] / datos['total_creditos']
        st.write(f"PAPA para {tipologia}: {papa_tipologia:.2f}")

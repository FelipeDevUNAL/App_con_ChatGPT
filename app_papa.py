
import streamlit as st

# Título de la app
st.title("Calculadora de PAPA")

st.write("Esta app fue elaborada por Felipe Devia.")

st.markdown("""
Esta aplicación permite calcular el **PAPA** global y por tipología de asignatura. 
Por favor, ingresa los datos de tus asignaturas cursadas.
""")

# Paso 1: Selección del número de asignaturas
st.header("Configuración inicial")
num_asignaturas = st.number_input("Número de asignaturas:", min_value=1, step=1, value=1, key="num_asignaturas_input")
aplicar_num_asignaturas = st.button("Aplicar número de asignaturas")

# Paso 2: Mostrar el formulario dinámico solo después de aplicar
if aplicar_num_asignaturas or "form_data" in st.session_state:
    # Guardar número de asignaturas en el estado de la aplicación
    if aplicar_num_asignaturas:
        st.session_state["form_data"] = [{"materia": "", "calificacion": 0.0, "creditos": 1, "tipologia": "DISCIPLINAR OPTATIVA"} for _ in range(num_asignaturas)]

    st.header("Datos de las asignaturas")

    # Crear el formulario para las asignaturas
    with st.form("form_papa"):
        for i, asignatura in enumerate(st.session_state["form_data"]):
            st.subheader(f"Asignatura {i + 1}")
            asignatura["materia"] = st.text_input(f"Nombre de la asignatura {i + 1}", value=asignatura["materia"], key=f"materia_{i}")
            asignatura["calificacion"] = st.number_input(
                f"Calificación (0.0 - 5.0) de {asignatura['materia']}", 
                min_value=0.0, max_value=5.0, step=0.1, value=asignatura["calificacion"], key=f"calificacion_{i}")
            asignatura["creditos"] = st.number_input(
                f"Número de créditos de {asignatura['materia']}", 
                min_value=1, step=1, value=asignatura["creditos"], key=f"creditos_{i}")
            asignatura["tipologia"] = st.selectbox(
                f"Tipología de {asignatura['materia']}",
                options=["DISCIPLINAR OPTATIVA", "FUND. OBLIGATORIA", "FUND. OPTATIVA", 
                         "DISCIPLINAR OBLIGATORIA", "LIBRE ELECCIÓN", "TRABAJO DE GRADO"],
                index=["DISCIPLINAR OPTATIVA", "FUND. OBLIGATORIA", "FUND. OPTATIVA", 
                       "DISCIPLINAR OBLIGATORIA", "LIBRE ELECCIÓN", "TRABAJO DE GRADO"].index(asignatura["tipologia"]),
                key=f"tipologia_{i}")
        
        # Botón para calcular
        calcular = st.form_submit_button("Calcular PAPA")

    # Procesar datos al calcular
    if calcular:
        # Filtrar asignaturas válidas
        asignaturas_validas = [
            (a["materia"], a["calificacion"], a["creditos"], a["tipologia"]) 
            for a in st.session_state["form_data"] if a["calificacion"] > 0
        ]
        
        if len(asignaturas_validas) < 2:
            st.warning("No se puede calcular el PAPA. Debes tener al menos 2 asignaturas con calificación numérica.")
        else:
            # Cálculo del PAPA global
            total_peso = sum(cal * cred for _, cal, cred, _ in asignaturas_validas)
            total_creditos = sum(cred for _, _, cred, _ in asignaturas_validas)
            papa_global = total_peso / total_creditos
            
            st.success(f"Tu PAPA global es: **{papa_global:.2f}**")
            
            # Cálculo del PAPA por tipología
            st.subheader("PAPA por tipología")
            for tipologia in set(a["tipologia"] for a in st.session_state["form_data"]):
                asignaturas_tipologia = [
                    (cal, cred) for _, cal, cred, t in asignaturas_validas if t == tipologia
                ]
                if asignaturas_tipologia:
                    peso_tipologia = sum(cal * cred for cal, cred in asignaturas_tipologia)
                    creditos_tipologia = sum(cred for _, cred in asignaturas_tipologia)
                    papa_tipologia = peso_tipologia / creditos_tipologia
                    st.write(f"- **{tipologia}**: {papa_tipologia:.2f}")

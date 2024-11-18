
import streamlit as st

# Título y descripción de la app
st.title("Calculadora de PAPA")
st.markdown("""
Esta aplicación permite calcular el **PAPA** global y por tipología de asignatura. 
Por favor, ingresa los datos de tus asignaturas cursadas.
""")

# Crear el formulario
with st.form("form_papa"):
    st.header("Datos de las asignaturas")
    
    # Listas vacías para almacenar los datos
    materias = []
    calificaciones = []
    creditos = []
    tipologias = []
    
    # Número de asignaturas
    num_asignaturas = st.number_input("Número de asignaturas:", min_value=1, step=1, value=1)
    
    # Formulario dinámico para cada asignatura
    for i in range(num_asignaturas):
        st.subheader(f"Asignatura {i + 1}")
        materia = st.text_input(f"Nombre de la asignatura {i + 1}", key=f"materia_{i}")
        materias.append(materia)
        
        calificacion = st.number_input(
            f"Calificación (0.0 - 5.0) de {materia}", min_value=0.0, max_value=5.0, step=0.1, key=f"calificacion_{i}")
        calificaciones.append(calificacion)
        
        credito = st.number_input(
            f"Número de créditos de {materia}", min_value=1, step=1, key=f"credito_{i}")
        creditos.append(credito)
        
        tipologia = st.selectbox(
            f"Tipología de {materia}", 
            options=["DISCIPLINAR OPTATIVA", "FUND. OBLIGATORIA", "FUND. OPTATIVA", 
                     "DISCIPLINAR OBLIGATORIA", "LIBRE ELECCIÓN", "TRABAJO DE GRADO"],
            key=f"tipologia_{i}")
        tipologias.append(tipologia)
    
    # Botón para enviar el formulario
    submit = st.form_submit_button("Calcular PAPA")

# Lógica de cálculo al enviar el formulario
if submit:
    # Filtrar asignaturas válidas (con calificación numérica)
    asignaturas_validas = [
        (materias[i], calificaciones[i], creditos[i], tipologias[i]) 
        for i in range(num_asignaturas) if calificaciones[i] > 0
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
        for tipologia in set(tipologias):
            asignaturas_tipologia = [
                (cal, cred) for _, cal, cred, t in asignaturas_validas if t == tipologia
            ]
            if asignaturas_tipologia:
                peso_tipologia = sum(cal * cred for cal, cred in asignaturas_tipologia)
                creditos_tipologia = sum(cred for _, cred in asignaturas_tipologia)
                papa_tipologia = peso_tipologia / creditos_tipologia
                st.write(f"- **{tipologia}**: {papa_tipologia:.2f}")

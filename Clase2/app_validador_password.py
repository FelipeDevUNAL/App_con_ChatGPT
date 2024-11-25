
import re
import streamlit as st

longitud_minima = 8
min_mayusculas = 1
min_minusculas = 1
min_numeros = 3
min_especiales = 1

def evaluar_contrasena(contrasena):
    """
    Evalúa la fortaleza de una contraseña y proporciona sugerencias detalladas.

    Args:
        contrasena: La contraseña a evaluar.

    Returns:
        Tuple: (bool, dict) indicando si la contraseña es segura y un diccionario con las sugerencias.
    """


    # Evaluaciones
    longitud_actual = len(contrasena)
    mayusculas_actual = len(re.findall(r'[A-Z]', contrasena))
    minusculas_actual = len(re.findall(r'[a-z]', contrasena))
    numeros_actual = len(re.findall(r'\d', contrasena))
    especiales_actual = len(re.findall(r'[@$!%*?&]', contrasena))

    sugerencias = {
        "longitud": max(0, longitud_minima - longitud_actual),
        "mayusculas": max(0, min_mayusculas - mayusculas_actual),
        "minusculas": max(0, min_minusculas - minusculas_actual),
        "numeros": max(0, min_numeros - numeros_actual),
        "especiales": max(0, min_especiales - especiales_actual),
    }

    # Verifica si cumple todas las reglas
    es_segura = all(valor == 0 for valor in sugerencias.values())
    return es_segura, sugerencias

def main():
    st.title("Evaluador de Contraseñas")
    st.write("Esta app fue elaborada por Felipe Devia.")

    # Input para la contraseña
    contrasena = st.text_input("Ingrese su contraseña")

    # Botón para evaluar
    if st.button("Evaluar"):
        try:
            if not contrasena:
                st.error("Por favor, ingrese una contraseña antes de evaluar.")
            else:
                es_segura, sugerencias = evaluar_contrasena(contrasena)
                if es_segura:
                    st.success("La contraseña es segura.")
                else:
                    st.error("La contraseña no cumple con los requisitos.")
                    if sugerencias["longitud"] > 0:
                        st.warning(f"- Faltan {sugerencias['longitud']} caracteres para alcanzar los {longitud_minima} caracteres mínimos.")
                    if sugerencias["mayusculas"] > 0:
                        st.warning(f"- Faltan {sugerencias['mayusculas']} letras mayúsculas.")
                    if sugerencias["minusculas"] > 0:
                        st.warning(f"- Faltan {sugerencias['minusculas']} letras minúsculas.")
                    if sugerencias["numeros"] > 0:
                        st.warning(f"- Faltan {sugerencias['numeros']} números.")
                    if sugerencias["especiales"] > 0:
                        st.warning(f"- Faltan {sugerencias['especiales']} caracteres especiales (por ejemplo, @$!%*?&).")

        except Exception as e:
            st.error(f"Ocurrió un error inesperado: {str(e)}")

if __name__ == "__main__":
    main()

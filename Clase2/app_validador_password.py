
import re
import streamlit as st

def evaluar_contrasena(contrasena):
    """
    Evalúa la fortaleza de una contraseña y proporciona sugerencias detalladas.

    Args:
        contrasena: La contraseña a evaluar.

    Returns:
        Tuple: (bool, str) indicando si la contraseña es segura y un mensaje descriptivo.
    """

    longitud_minima = 8
    min_mayusculas = 1
    min_minusculas = 1
    min_numeros = 1
    min_especiales = 1

    patron = r"^(?=.*[a-z]{" + str(min_minusculas) + ",})(?=.*[A-Z]{" + str(min_mayusculas) + ",})(?=.*\d{" + str(min_numeros) + ",})(?=.*[@$!%*?&]{" + str(min_especiales) + ",})[A-Za-z\d@$!%*?&]{" + str(longitud_minima) + ",}$"

    if re.match(patron, contrasena):
        return True, "La contraseña es segura."
    else:
        sugerencias = []
        if len(contrasena) < longitud_minima:
            sugerencias.append(f"La contraseña debe tener al menos {longitud_minima} caracteres.")
        if len(re.findall(r'[A-Z]', contrasena)) < min_mayusculas:
            sugerencias.append(f"La contraseña debe contener al menos {min_mayusculas} letras mayúsculas.")
        if len(re.findall(r'[a-z]', contrasena)) < min_minusculas:
            sugerencias.append(f"La contraseña debe contener al menos {min_minusculas} letras minúsculas.")
        if len(re.findall(r'\d', contrasena)) < min_numeros:
            sugerencias.append(f"La contraseña debe contener al menos {min_numeros} números.")
        if len(re.findall(r'[@$!%*?&]', contrasena)) < min_especiales:
            sugerencias.append(f"La contraseña debe contener al menos {min_especiales} caracteres especiales.")

        return False, ", ".join(sugerencias)

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
                es_segura, mensaje = evaluar_contrasena(contrasena)
                if es_segura:
                    st.success(str(mensaje))
                else:
                    st.error(str(mensaje))
        except Exception as e:
            st.error(f"Ocurrió un error inesperado: {str(e)}")

if __name__ == "__main__":
    main()

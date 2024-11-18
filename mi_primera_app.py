import streamlit as st

# Título de la aplicación
st.title("Mi primera app")

# Autor de la aplicación
st.write("Esta app fue elaborada por \"COLOQUE AQUÍ SU NOMBRE\".")

# Solicitar nombre al usuario
nombre_usuario = st.text_input("Por favor, escribe tu nombre:")

# Mostrar mensaje de bienvenida
if nombre_usuario:
    st.write(f"{nombre_usuario}, te doy la bienvenida a mi primera app.")

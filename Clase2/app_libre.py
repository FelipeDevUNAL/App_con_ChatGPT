

import streamlit as st
import re

# Función para resaltar las palabras prohibidas en el texto
def resaltar_palabras_prohibidas(texto, palabras_prohibidas):
    # Usar expresiones regulares para resaltar las palabras prohibidas
    for palabra in palabras_prohibidas:
        # Crear una expresión regular para encontrar las palabras
        texto = re.sub(rf'({re.escape(palabra)})', r'<mark>\1</mark>', texto, flags=re.IGNORECASE)
    return texto

# Título de la aplicación
st.title("Buscador de Palabras Prohibidas")
st.write("Esta app fue elaborada por Felipe Devia.")  

# Entrada de texto del usuario
texto_entrada = st.text_area("Ingresa el texto:", height=200)

# Entrada para las palabras prohibidas
palabras_input = st.text_area("Ingresa las palabras prohibidas (separadas por comas):", height=100)

# Procesar las palabras prohibidas
if palabras_input:
    palabras_prohibidas = [palabra.strip() for palabra in palabras_input.split(",")]

    if texto_entrada:
        # Resaltar las palabras prohibidas en el texto
        texto_resaltado = resaltar_palabras_prohibidas(texto_entrada, palabras_prohibidas)
        
        # Mostrar el texto resaltado
        st.markdown("### Texto con Palabras Prohibidas Resaltadas")
        st.markdown(f"<div style='white-space: pre-wrap'>{texto_resaltado}</div>", unsafe_allow_html=True)

        # Contar las coincidencias
        conteo_palabras = sum(texto_entrada.lower().count(palabra.lower()) for palabra in palabras_prohibidas)
        
        # Mostrar el número de coincidencias
        st.write(f"**Número total de palabras prohibidas encontradas: {conteo_palabras}**")

    else:
        st.warning("Por favor, ingresa un texto.")
else:
    st.warning("Por favor, ingresa una lista de palabras prohibidas.")

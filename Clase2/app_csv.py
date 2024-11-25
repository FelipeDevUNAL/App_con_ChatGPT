
import streamlit as st
import re
import pandas as pd
import requests

# URL del archivo CSV
URL_CSV = "https://raw.githubusercontent.com/gabrielawad/programacion-para-ingenieria/main/archivos-datos/regex/regex_productos.csv"

# Función para descargar el archivo
def descargar_archivo_csv(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"No se pudo descargar el archivo. Código de estado: {response.status_code}")

# Función para procesar una línea
def procesar_linea(linea):
    # Dividir la línea en valores separados por comas
    valores = linea.split(",")

    # Patrones regex para identificar los campos
    patrones = {
        "correo": r"\S+@\S+",
        "valor": r"\d+\.\d+",
        "telefono": r"\+57\s\d{10}",
        "fecha": r"\d{2}/\d{2}/\d{2}",
        "nombre_cliente": r"[A-Z][a-z]+(?:\s[A-Z][a-z]+)*",
        "id_producto": r"^\d+$"  # Solo números enteros
    }

    fila = {
        "Correo": None,
        "Valor": None,
        "Teléfono": None,
        "Fecha de compra": None,
        "Nombre del cliente": None,
        "ID del producto": None
    }

    # Analizar cada valor para identificarlo
    for valor in valores:
        valor = valor.strip()
        if re.match(patrones["correo"], valor):
            fila["Correo"] = valor
        elif re.match(patrones["valor"], valor):
            fila["Valor"] = valor
        elif re.match(patrones["telefono"], valor):
            fila["Teléfono"] = valor
        elif re.match(patrones["fecha"], valor):
            fila["Fecha de compra"] = valor
        elif re.match(patrones["id_producto"], valor):
            fila["ID del producto"] = valor
        elif re.match(patrones["nombre_cliente"], valor):
            if fila["Nombre del cliente"] is None:  # Tomar el primer nombre que coincida
                fila["Nombre del cliente"] = valor

    # Validar que se identificaron todos los campos necesarios
    if all(fila.values()):
        return fila
    else:
        st.warning(f"No se identificaron todos los campos en la línea: {linea}")
        return None

# Función para generar el DataFrame
def generar_dataframe():
    data = []

    # Descargar el archivo CSV
    contenido_csv = descargar_archivo_csv(URL_CSV)

    # Procesar cada línea
    for linea in contenido_csv.splitlines():
        resultado = procesar_linea(linea)
        if resultado:
            data.append(resultado)

    return pd.DataFrame(data)

# Aplicación Streamlit
def main():
    st.title("Procesador de Archivo CSV con Regex")
    st.write("Procesa un archivo CSV y genera un archivo Excel.")
    
    if st.button("Procesar Archivo y Descargar Excel"):
        try:
            df = generar_dataframe()
            if not df.empty:
                st.write("Contenido procesado:")
                st.dataframe(df)

                # Guardar el DataFrame como Excel
                excel_file = "procesado_productos.xlsx"
                df.to_excel(excel_file, index=False)
                with open(excel_file, "rb") as file:
                    st.download_button(
                        label="📥 Descargar Excel Procesado",
                        data=file,
                        file_name=excel_file,
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    )
            else:
                st.error("No se generaron datos válidos.")
        except Exception as e:
            st.error(f"Ocurrió un error: {str(e)}")

if __name__ == "__main__":
    main()

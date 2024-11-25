
import re
import pandas as pd
import requests
import streamlit as st

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
    valores = linea.split(",")
    patrones = {
        "correo": r"\S+@\S+",
        "valor": r"\d+\.\d+",
        "telefono": r"\+57\s\d{10}",
        "fecha": r"\d{2}/\d{2}/\d{2}",
        "nombre_cliente": r"[A-Z][a-z]+(?:\s[A-Z][a-z]+)*",
        "id_producto": r"^\d+$"
    }
    fila = {
        "Correo": None,
        "Valor": None,
        "Teléfono": None,
        "Fecha de compra": None,
        "Nombre del cliente": None,
        "ID del producto": None
    }

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
            if fila["Nombre del cliente"] is None:
                fila["Nombre del cliente"] = valor

    if all(fila.values()):
        return fila
    else:
        st.warning(f"No se identificaron todos los campos en la línea: {linea}")
        return None

# Función para generar el DataFrame
def generar_dataframe():
    data = []
    contenido_csv = descargar_archivo_csv(URL_CSV)
    for linea in contenido_csv.splitlines():
        resultado = procesar_linea(linea)
        if resultado:
            data.append(resultado)
    return pd.DataFrame(data)

# Aplicación Streamlit
def main():
    st.title("Procesador de Archivo CSV")
    st.write("Esta app fue elaborada por Felipe Devia.")  
    st.write("Procesa un archivo CSV y genera un archivo con la información procesada.")

    if st.button("Procesar Archivo y Descargar CSV"):
        try:
            # Generar el DataFrame procesado
            df = generar_dataframe()

            if not df.empty:
                # Mostrar un resumen del DataFrame
                st.write("Datos procesados correctamente:")
                st.dataframe(df)

                # Guardar como CSV
                csv_file = "procesado_productos.csv"
                df.to_csv(csv_file, index=False)

                # Descargar el archivo CSV
                with open(csv_file, "rb") as file:
                    st.download_button(
                        label="📥 Descargar CSV Procesado",
                        data=file,
                        file_name=csv_file,
                        mime="text/csv"
                    )
            else:
                st.error("No se generaron datos válidos.")
        except Exception as e:
            st.error(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()

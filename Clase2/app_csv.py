

import re
import pandas as pd
import requests
import streamlit as st

# URL del archivo en el repositorio
URL_CSV = "https://raw.githubusercontent.com/gabrielawad/programacion-para-ingenieria/main/archivos-datos/regex/regex_productos.csv"

# Función para descargar el archivo desde el repositorio
def descargar_archivo_csv(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"No se pudo descargar el archivo. Código de estado: {response.status_code}")

# Función para procesar cada línea del archivo y extraer la información
def procesar_linea(linea):
    patron = re.compile(
        r"(?P<nombre_cliente>[A-Z][a-z]+(?:\s[A-Z][a-z]+)*)\s+"  # Primer nombre con apellido
        r"(?P<correo>\S+@\S+)\s+"                               # Correo electrónico
        r"(?P<id_producto>\d+)\s+"                              # ID del producto (solo números)
        r"(?P<valor>\d+\.\d+)\s+"                               # Valor del producto
        r"(?P<telefono>\+57\s\d{10})\s+"                        # Teléfono
        r"(?P<fecha>\d{2}/\d{2}/\d{2})"                         # Fecha de compra
    )


    match = patron.search(linea)
    if match:
        return match.groupdict()
    else:
        return None

# Función para generar el DataFrame procesado
def generar_dataframe():
    data = []

    # Descargar el archivo CSV
    contenido_csv = descargar_archivo_csv(URL_CSV)
    
    # Procesar cada línea
    for linea in contenido_csv.splitlines():
        linea = linea.strip()
        resultado = procesar_linea(linea)
        if resultado:
            data.append({
                "Número de serie del producto": "N/A",  # Sin número de serie en el archivo
                "Valor": resultado["valor"],
                "Fecha de compra del producto": resultado["fecha"],
                "Información de contacto de clientes": f"{resultado['nombre_cliente']} | {resultado['correo']} | {resultado['telefono']}"
            })
    return pd.DataFrame(data)

# Aplicación Streamlit
def main():
    st.title("Procesador de Archivo CSV")
    st.write("Esta aplicación procesa el archivo [regex_productos.csv](https://github.com/gabrielawad/programacion-para-ingenieria/blob/main/archivos-datos/regex/regex_productos.csv) y genera un archivo Excel con la información solicitada.")
    
    # Botón para generar el Excel
    if st.button("Procesar Archivo y Descargar Excel"):
        try:
            # Generar el DataFrame procesado
            df = generar_dataframe()
            
            # Guardar como Excel
            excel_file = "procesado_productos.xlsx"
            df.to_excel(excel_file, index=False)

            # Agregar un enlace clickeable en la cabecera del archivo Excel
            st.write("Descarga el archivo procesado a continuación:")
            with open(excel_file, "rb") as file:
                st.download_button(
                    label="📥 Descargar Excel Procesado",
                    data=file,
                    file_name=excel_file,
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                )
        except Exception as e:
            st.error(f"Ocurrió un error al procesar el archivo: {str(e)}")

if __name__ == "__main__":
    main()

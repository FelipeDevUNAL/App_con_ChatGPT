
import re
import streamlit as st

def validar_nombres(nombre):
    """Valida que los nombres solo contengan caracteres alfabéticos e inicien con mayúsculas."""
    patron = r'^([A-Z][a-z]+)( [A-Z][a-z]+)*$'
    if re.match(patron, nombre):
        return True, "Nombre válido."
    errores = []
    if not nombre:
        errores.append("El campo no puede estar vacío.")
    elif not all(palabra[0].isupper() for palabra in nombre.split()):
        errores.append("Cada palabra debe iniciar con mayúscula.")
    if not nombre.replace(" ", "").isalpha():
        errores.append("Debe contener solo caracteres alfabéticos.")
    return False, " ".join(errores)

def validar_correo(correo):
    """Valida que el correo tenga un formato válido con @ y termine en .com."""
    patron = r'^[\w.-]+@[a-zA-Z]+\.(com)$'
    if re.match(patron, correo):
        return True, "Correo válido."
    errores = []
    if "@" not in correo:
        errores.append("Debe contener '@'.")
    if not correo.endswith(".com"):
        errores.append("Debe terminar en '.com'.")
    return False, " ".join(errores)

def validar_telefono(telefono):
    """Valida que el teléfono tenga exactamente 10 dígitos numéricos."""
    patron = r'^\d{10}$'
    if re.match(patron, telefono):
        return True, "Teléfono válido."
    errores = []
    if not telefono.isdigit():
        errores.append("Debe contener solo números.")
    if len(telefono) != 10:
        errores.append(f"Debe tener exactamente 10 dígitos, tiene {len(telefono)}.")
    return False, " ".join(errores)

def validar_fecha(fecha):
    """Valida el formato de la fecha en DD/MM/YYYY y verifica límites de día y mes."""
    patron = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(\d{4})$'
    if re.match(patron, fecha):
        return True, "Fecha válida."
    errores = []
    if not re.match(r'^\d{2}/\d{2}/\d{4}$', fecha):
        errores.append("Debe estar en formato DD/MM/AAAA.")
    else:
        dia, mes, _ = map(int, fecha.split("/"))
        if dia < 1 or dia > 31:
            errores.append("El día debe estar entre 01 y 31.")
        if mes < 1 or mes > 12:
            errores.append("El mes debe estar entre 01 y 12.")
    return False, " ".join(errores)

def main():
    st.title("Validador de Formularios Web")
    st.write("Esta app fue elaborada por Felipe Devia.")
    st.write("Esta aplicación valida los siguientes campos: Nombres, Correo Electrónico, Teléfono y Fecha.")

    # Campos del formulario
    nombre = st.text_input("Nombre (Ejemplo: Juan Pérez)")
    correo = st.text_input("Correo Electrónico (Ejemplo: usuario@dominio.com)")
    telefono = st.text_input("Número de Teléfono (Ejemplo: 1234567890)")
    fecha = st.text_input("Fecha (Formato DD/MM/AAAA)")

    # Botón de validación
    if st.button("Validar"):
        validaciones = []

        # Validar cada campo y agregar el resultado a la lista
        es_valido, mensaje = validar_nombres(nombre)
        validaciones.append((es_valido, "Nombre", mensaje))
        
        es_valido, mensaje = validar_correo(correo)
        validaciones.append((es_valido, "Correo Electrónico", mensaje))
        
        es_valido, mensaje = validar_telefono(telefono)
        validaciones.append((es_valido, "Teléfono", mensaje))
        
        es_valido, mensaje = validar_fecha(fecha)
        validaciones.append((es_valido, "Fecha", mensaje))

        # Mostrar resultados
        for es_valido, campo, mensaje in validaciones:
            if es_valido:
                st.success(f"{campo}: {mensaje}")
            else:
                st.error(f"{campo}: {mensaje}")

if __name__ == "__main__":
    main()

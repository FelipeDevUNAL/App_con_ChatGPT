
import streamlit as st

# Título de la app
st.title('Conversor Universal de Unidades')

st.write("Esta app fue elaborada por Felipe Devia.")


# Descripción de la app
st.write("""
    Esta app permite realizar conversiones entre diferentes unidades en varias categorías:
    - Temperatura
    - Longitud
    - Peso/Masa
    - Volumen
    - Tiempo
    - Velocidad
    - Área
    - Energía
    - Presión
    - Tamaño de Datos
""")

# Selección de categoría
category = st.selectbox('Selecciona una categoría de conversión:', [
    'Temperatura',
    'Longitud',
    'Peso/Masa',
    'Volumen',
    'Tiempo',
    'Velocidad',
    'Área',
    'Energía',
    'Presión',
    'Tamaño de Datos'
])

# Función para convertir según la categoría seleccionada
if category == 'Temperatura':
    conversion_type = st.selectbox('Selecciona el tipo de conversión:', [
        'Celsius a Fahrenheit',
        'Fahrenheit a Celsius',
        'Celsius a Kelvin',
        'Kelvin a Celsius'
    ])
    value = st.number_input('Ingresa el valor:')
    
    if conversion_type == 'Celsius a Fahrenheit':
        result = (value * 9/5) + 32
    elif conversion_type == 'Fahrenheit a Celsius':
        result = (value - 32) * 5/9
    elif conversion_type == 'Celsius a Kelvin':
        result = value + 273.15
    elif conversion_type == 'Kelvin a Celsius':
        result = value - 273.15

elif category == 'Longitud':
    conversion_type = st.selectbox('Selecciona el tipo de conversión:', [
        'Pies a metros',
        'Metros a pies',
        'Pulgadas a centímetros',
        'Centímetros a pulgadas'
    ])
    value = st.number_input('Ingresa el valor:')
    
    if conversion_type == 'Pies a metros':
        result = value * 0.3048
    elif conversion_type == 'Metros a pies':
        result = value / 0.3048
    elif conversion_type == 'Pulgadas a centímetros':
        result = value * 2.54
    elif conversion_type == 'Centímetros a pulgadas':
        result = value / 2.54

elif category == 'Peso/Masa':
    conversion_type = st.selectbox('Selecciona el tipo de conversión:', [
        'Libras a kilogramos',
        'Kilogramos a libras',
        'Onzas a gramos',
        'Gramos a onzas'
    ])
    value = st.number_input('Ingresa el valor:')
    
    if conversion_type == 'Libras a kilogramos':
        result = value * 0.453592
    elif conversion_type == 'Kilogramos a libras':
        result = value / 0.453592
    elif conversion_type == 'Onzas a gramos':
        result = value * 28.3495
    elif conversion_type == 'Gramos a onzas':
        result = value / 28.3495

elif category == 'Volumen':
    conversion_type = st.selectbox('Selecciona el tipo de conversión:', [
        'Galones a litros',
        'Litros a galones',
        'Pulgadas cúbicas a centímetros cúbicos',
        'Centímetros cúbicos a pulgadas cúbicas'
    ])
    value = st.number_input('Ingresa el valor:')
    
    if conversion_type == 'Galones a litros':
        result = value * 3.78541
    elif conversion_type == 'Litros a galones':
        result = value / 3.78541
    elif conversion_type == 'Pulgadas cúbicas a centímetros cúbicos':
        result = value * 16.387
    elif conversion_type == 'Centímetros cúbicos a pulgadas cúbicas':
        result = value / 16.387

elif category == 'Tiempo':
    conversion_type = st.selectbox('Selecciona el tipo de conversión:', [
        'Horas a minutos',
        'Minutos a segundos',
        'Días a horas',
        'Semanas a días'
    ])
    value = st.number_input('Ingresa el valor:')
    
    if conversion_type == 'Horas a minutos':
        result = value * 60
    elif conversion_type == 'Minutos a segundos':
        result = value * 60
    elif conversion_type == 'Días a horas':
        result = value * 24
    elif conversion_type == 'Semanas a días':
        result = value * 7

elif category == 'Velocidad':
    conversion_type = st.selectbox('Selecciona el tipo de conversión:', [
        'Millas por hora a kilómetros por hora',
        'Kilómetros por hora a metros por segundo',
        'Nudos a millas por hora',
        'Metros por segundo a pies por segundo'
    ])
    value = st.number_input('Ingresa el valor:')
    
    if conversion_type == 'Millas por hora a kilómetros por hora':
        result = value * 1.60934
    elif conversion_type == 'Kilómetros por hora a metros por segundo':
        result = value / 3.6
    elif conversion_type == 'Nudos a millas por hora':
        result = value * 1.15078
    elif conversion_type == 'Metros por segundo a pies por segundo':
        result = value * 3.28084

elif category == 'Área':
    conversion_type = st.selectbox('Selecciona el tipo de conversión:', [
        'Metros cuadrados a pies cuadrados',
        'Pies cuadrados a metros cuadrados',
        'Kilómetros cuadrados a millas cuadradas',
        'Millas cuadradas a kilómetros cuadrados'
    ])
    value = st.number_input('Ingresa el valor:')
    
    if conversion_type == 'Metros cuadrados a pies cuadrados':
        result = value * 10.7639
    elif conversion_type == 'Pies cuadrados a metros cuadrados':
        result = value / 10.7639
    elif conversion_type == 'Kilómetros cuadrados a millas cuadradas':
        result = value * 0.386102
    elif conversion_type == 'Millas cuadradas a kilómetros cuadrados':
        result = value / 0.386102

elif category == 'Energía':
    conversion_type = st.selectbox('Selecciona el tipo de conversión:', [
        'Julios a calorías',
        'Calorías a kilojulios',
        'Kilovatios-hora a megajulios',
        'Megajulios a kilovatios-hora'
    ])
    value = st.number_input('Ingresa el valor:')
    
    if conversion_type == 'Julios a calorías':
        result = value * 0.239006
    elif conversion_type == 'Calorías a kilojulios':
        result = value / 239.006
    elif conversion_type == 'Kilovatios-hora a megajulios':
        result = value * 3.6
    elif conversion_type == 'Megajulios a kilovatios-hora':
        result = value / 3.6

elif category == 'Presión':
    conversion_type = st.selectbox('Selecciona el tipo de conversión:', [
        'Pascales a atmósferas',
        'Atmósferas a pascales',
        'Barras a libras por pulgada cuadrada',
        'Libras por pulgada cuadrada a bares'
    ])
    value = st.number_input('Ingresa el valor:')
    
    if conversion_type == 'Pascales a atmósferas':
        result = value / 101325
    elif conversion_type == 'Atmósferas a pascales':
        result = value * 101325
    elif conversion_type == 'Barras a libras por pulgada cuadrada':
        result = value * 14.5038
    elif conversion_type == 'Libras por pulgada cuadrada a bares':
        result = value / 14.5038

elif category == 'Tamaño de Datos':
    conversion_type = st.selectbox('Selecciona el tipo de conversión:', [
        'Megabytes a gigabytes',
        'Gigabytes a Terabytes',
        'Kilobytes a megabytes',
        'Terabytes a petabytes'
    ])
    value = st.number_input('Ingresa el valor:')
    
    if conversion_type == 'Megabytes a gigabytes':
        result = value / 1024
    elif conversion_type == 'Gigabytes a Terabytes':
        result = value / 1024
    elif conversion_type == 'Kilobytes a megabytes':
        result = value / 1024
    elif conversion_type == 'Terabytes a petabytes':
        result = value / 1024

# Muestra el resultado de la conversión
st.write(f"Resultado: {result}")

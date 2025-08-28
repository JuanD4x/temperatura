import streamlit as st

# Función de conversión
def celsius_a_fahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32

# Título de la app
st.title("🌡️ Convertidor de Celsius a Fahrenheit")

# Descripción
st.write("Ingrese una temperatura en grados Celsius y conviértala a Fahrenheit.")

# Entrada del usuario
celsius = st.number_input("Temperatura en °C:", value=0.0, step=0.1)

# Botón para ejecutar la conversión
if st.button("Convertir"):
    fahrenheit = celsius_a_fahrenheit(celsius)
    st.success(f"✅ {celsius:.2f} °C equivalen a {fahrenheit:.2f} °F")

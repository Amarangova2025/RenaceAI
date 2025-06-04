
import streamlit as st
import joblib

# Cargar el modelo y el vectorizador
modelo = joblib.load("modelo_entrenado.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Configuración de la app
st.set_page_config(page_title="Renace AI - Detector de Emociones", page_icon="🌈")
st.title("🌈 Renace AI - Detector de Emociones")
st.markdown("Escribe una frase que estés sintiendo y Renace AI detectará tu emoción.")

# Entrada del usuario
frase = st.text_input("✏️ Escribe aquí tu frase:")

# Procesar y predecir
if frase:
    vector = vectorizer.transform([frase])
    emocion = modelo.predict(vector)[0]
    st.success(f"✨ Emoción detectada: **{emocion.upper()}**")
    st.balloons()

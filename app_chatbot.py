
import streamlit as st
import joblib

# Cargar modelo y vectorizador
modelo = joblib.load("modelo_entrenado.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Configurar página
st.set_page_config(page_title="Renace AI Chatbot", page_icon="💬")
st.title("💬 Renace AI - Asistente Emocional")

# Historial de conversación
if "chat" not in st.session_state:
    st.session_state.chat = []

# Entrada de usuario
frase = st.text_input("Escribe lo que estás sintiendo y pulsa Enter:")

if frase:
    # Predecir emoción
    vector = vectorizer.transform([frase])
    emocion = modelo.predict(vector)[0]

    # Guardar en historial
    st.session_state.chat.append(("👩", frase))
    st.session_state.chat.append(("🤖 Renace AI", f"Emoción detectada → {emocion.capitalize()}"))

# Mostrar conversación
for autor, texto in st.session_state.chat:
    st.markdown(f"**{autor}:** {texto}")

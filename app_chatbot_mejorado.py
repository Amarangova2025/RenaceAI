
import streamlit as st
import joblib

# Cargar modelo y vectorizador
modelo = joblib.load("modelo_entrenado.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Diccionario de respuestas empáticas por emoción
respuestas = {
    "ansiedad": "Respira profundo... estás haciendo lo mejor que puedes, y eso es suficiente. 💛",
    "culpa": "Recuerda que todos cometemos errores. Lo importante es que estás aquí, buscando sanar. 🤍",
    "confusion": "Está bien no tener todas las respuestas ahora. Confía en el proceso. 🌿",
    "tristeza": "Tu dolor es válido. Permítete sentir y sanar con amor. 💙"
}

# Configuración de la página
st.set_page_config(page_title="Renace AI - Chat Emocional", page_icon="💬")
st.title("💬 Renace AI - Asistente Emocional")

# Botón para limpiar conversación
if st.button("🧹 Limpiar chat"):
    st.session_state.chat = []

# Inicializar historial si no existe
if "chat" not in st.session_state:
    st.session_state.chat = []

# Entrada del usuario
frase = st.text_input("Escribe lo que estás sintiendo y pulsa Enter:")

if frase:
    # Predecir emoción
    vector = vectorizer.transform([frase])
    emocion = modelo.predict(vector)[0]

    # Guardar en historial
    st.session_state.chat.append(("👩", frase))
    st.session_state.chat.append(("😥 Renace AI", f"Emoción detectada → {emocion.capitalize()}"))
    st.session_state.chat.append(("💟 Renace AI", respuestas[emocion]))

# Mostrar historial de conversación
for autor, mensaje in st.session_state.chat:
    st.markdown(f"**{autor}:** {mensaje}")

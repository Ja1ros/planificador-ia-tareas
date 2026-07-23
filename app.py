import streamlit as st
import openai
import os
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Planificador IA de Tareas", page_icon="\U0001F5D3", layout="wide")

st.title("Planificador IA de Tareas y Estudio")
st.write("Genera cronogramas semanales optimizados usando inteligencia artificial.")

with st.sidebar:
    st.header("Configuracion")
    api_key_input = st.text_input("OpenAI API Key (opcional si ya esta en .env)", type="password")
    if api_key_input:
        openai.api_key = api_key_input

st.subheader("Ingresa tus tareas y objetivos")

if "tareas" not in st.session_state:
    st.session_state.tareas = []

col1, col2, col3 = st.columns(3)
with col1:
    tarea = st.text_input("Nombre de la tarea")
with col2:
    horas = st.number_input("Horas estimadas", min_value=0.5, max_value=40.0, value=2.0, step=0.5)
with col3:
    prioridad = st.selectbox("Prioridad", ["Alta", "Media", "Baja"])

if st.button("Agregar tarea"):
    if tarea:
        st.session_state.tareas.append({"tarea": tarea, "horas": horas, "prioridad": prioridad})
        st.success(f"Tarea agregada: {tarea}")

if st.session_state.tareas:
    st.subheader("Lista de tareas")
    df = pd.DataFrame(st.session_state.tareas)
    st.dataframe(df, use_container_width=True)

    if st.button("Limpiar lista"):
        st.session_state.tareas = []
        st.rerun()

    horas_disponibles = st.slider("Horas disponibles por dia", 1, 12, 4)

    if st.button("Generar cronograma con IA"):
        with st.spinner("Generando cronograma..."):
            try:
                tareas_texto = "\n".join([f"- {t['tarea']} ({t['horas']}h, prioridad {t['prioridad']})" for t in st.session_state.tareas])
                hoy = datetime.now().strftime("%Y-%m-%d")

                prompt = f"Eres un asistente experto en planificacion academica y productividad. Fecha de inicio: {hoy}. Horas disponibles por dia: {horas_disponibles}. Tareas a organizar:\n{tareas_texto}\n\nGenera un cronograma semanal (Lunes a Domingo) que distribuya estas tareas de forma optima, respetando prioridades y horas estimadas. Presenta el resultado en una tabla markdown con columnas: Dia, Tarea, Horas, Notas."

                response = openai.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "Eres un planificador experto en gestion del tiempo y estudio."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.5
                )

                cronograma = response.choices[0].message.content
                st.subheader("Cronograma generado")
                st.markdown(cronograma)

            except Exception as e:
                st.error(f"Error al generar el cronograma: {e}")
else:
    st.info("Agrega al menos una tarea para generar tu cronograma.")

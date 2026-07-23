# Planificador IA de Tareas

Planificador de estudio y tareas que genera cronogramas semanales optimizados usando Inteligencia Artificial (OpenAI GPT-4o-mini).

## Descripcion

Esta aplicacion permite registrar tareas academicas o laborales con su duracion estimada y prioridad, y utiliza un modelo de lenguaje de IA para generar automaticamente un cronograma semanal optimizado, respetando las horas disponibles por dia y las prioridades definidas por el usuario.

## Caracteristicas

- Registro de tareas con nombre, horas estimadas y prioridad (Alta, Media, Baja).
- Visualizacion de la lista de tareas en una tabla interactiva.
- Generacion automatica de cronograma semanal (Lunes a Domingo) usando IA.
- Configuracion de horas disponibles por dia.
- Interfaz simple e intuitiva construida con Streamlit.

## Tecnologias utilizadas

- Python
- Streamlit
- OpenAI API (GPT-4o-mini)
- Pandas
- python-dotenv

## Instalacion

1. Clonar el repositorio:
```
git clone https://github.com/Ja1ros/planificador-ia-tareas.git
cd planificador-ia-tareas
```

2. Instalar dependencias:
```
pip install -r requirements.txt
```

3. Configurar variables de entorno:
```
cp .env.example .env
```
Luego edita el archivo `.env` y agrega tu API Key de OpenAI.

## Uso

Ejecuta la aplicacion con:
```
streamlit run app.py
```

Luego abre tu navegador en `http://localhost:8501`, agrega tus tareas y genera tu cronograma semanal optimizado con IA.

## Licencia

Este proyecto es de uso libre para fines educativos y de portafolio.

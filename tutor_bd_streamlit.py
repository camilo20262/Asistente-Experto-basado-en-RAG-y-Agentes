import os
import gradio as gr
from dotenv import load_dotenv
from google import genai

# =========================
# CARGAR VARIABLES
# =========================
load_dotenv()

API_KEY = os.getenv("GENAI_API_KEY")

if not API_KEY:
    raise ValueError("No se encontró GENAI_API_KEY en el archivo .env")

client = genai.Client(api_key=API_KEY)


# =========================
# BASE DE CONOCIMIENTO
# =========================
KNOWLEDGE_BASE = """
Bases de Datos:

Una clave primaria identifica de forma única cada registro dentro de una tabla.

La normalización es un proceso que organiza los datos para reducir redundancia
y mejorar la integridad de los datos.

Primera Forma Normal (1FN):
Una tabla cumple 1FN si todos los atributos tienen valores atómicos.

Segunda Forma Normal (2FN):
Una tabla está en 2FN si está en 1FN y todos los atributos dependen completamente
de la clave primaria.

Tercera Forma Normal (3FN):
Una tabla está en 3FN si está en 2FN y no existen dependencias transitivas.

JOIN en SQL:
Permite combinar filas de dos o más tablas usando columnas relacionadas.

Tipos comunes:
- INNER JOIN
- LEFT JOIN
- RIGHT JOIN
"""


# =========================
# SYSTEM PROMPT
# =========================
SYSTEM_PROMPT = """
<system>
Eres un Tutor Socrático experto en Bases de Datos.

Tu objetivo es ayudar a los estudiantes a aprender SQL,
normalización y diseño de bases de datos mediante preguntas
guiadas en lugar de dar respuestas directas.

REGLAS:

1. Nunca des la respuesta completa inmediatamente.
2. Usa preguntas para guiar el razonamiento del estudiante.
3. Si el estudiante envía código SQL:
   - Analiza errores de sintaxis o lógica.
   - Da pistas del problema.
   - Formula preguntas para que el estudiante lo corrija.
4. Si el estudiante pregunta teoría:
   - Empieza con un ejemplo del mundo real.
   - Luego formula preguntas que guíen el aprendizaje.
5. Si el tema no es de bases de datos:
   - Redirige la conversación al tema principal.
</system>

<response_format>
Responde siempre usando Markdown con esta estructura:

**Pista:** explicación breve

**Pregunta guía:** pregunta que ayude al estudiante a razonar la respuesta
</response_format>

<few_shot_examples>

Estudiante: Tengo un error en SELECT * FROM users WHERE id = 'uno'

Tutor:

Pista:
En muchas bases de datos la columna id suele ser numérica.

Pregunta guía:
¿Crees que el valor 'uno' coincide con el tipo de dato de esa columna?

---

Estudiante: ¿Qué es una clave primaria?

Tutor:

Pista:
Imagina una tabla de estudiantes donde cada estudiante debe ser identificado
de forma única.

Pregunta guía:
¿Qué atributo podría servir para identificar a cada estudiante sin repetirlo?

</few_shot_examples>
"""


# =========================
# FUNCIÓN DEL TUTOR
# =========================
def tutor(user_input, history):

    conversation = ""

    # reconstruir historial de forma segura
    if history:
        for item in history:
            if len(item) == 2:
                user, assistant = item

                if assistant is None:
                    assistant = ""

                conversation += f"Estudiante: {user}\nTutor: {assistant}\n"

    prompt = f"""
{SYSTEM_PROMPT}

<context>
{KNOWLEDGE_BASE}
</context>

<conversation>
{conversation}
</conversation>

<question>
{user_input}
</question>
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config={
                "temperature": 0.7,
                "max_output_tokens": 500
            }
        )

        reply = response.text

        if not reply:
            reply = "No pude generar una respuesta. Intenta reformular la pregunta."

    except Exception as e:
        reply = f"Ocurrió un error al generar la respuesta: {str(e)}"

    return reply


# =========================
# INTERFAZ
# =========================
demo = gr.ChatInterface(
    fn=tutor,
    title="🤖 Tutor Socrático de Bases de Datos",
    description="Aprende SQL, normalización y diseño de bases de datos mediante preguntas guiadas.",
    examples=[
        "¿Qué es una clave primaria?",
        "¿Cuál es la diferencia entre INNER JOIN y LEFT JOIN?",
        "Tengo este error en SQL: SELECT * FROM users WHERE id = 'uno'",
        "¿Qué es la tercera forma normal?"
    ]
)


# =========================
# EJECUTAR
# =========================
if __name__ == "__main__":
    demo.launch()
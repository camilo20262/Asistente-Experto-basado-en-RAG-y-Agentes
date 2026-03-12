# 🤖 Tutor Socrático de Bases de Datos

Este proyecto implementa un **Asistente Académico Inteligente** diseñado para ayudar a estudiantes a aprender **Bases de Datos y SQL** mediante el **método socrático**.
El sistema guía al usuario con **preguntas y pistas** en lugar de proporcionar respuestas directas, fomentando el razonamiento y el aprendizaje activo.

El asistente utiliza **Prompt Engineering**, **Few-Shot Prompting** y una **base de conocimiento simulando RAG (Retrieval-Augmented Generation)** para responder preguntas de forma contextualizada.

---

# 🎯 Objetivo del Proyecto

Desarrollar un asistente experto capaz de:

* Guiar el aprendizaje de **conceptos de bases de datos**
* Analizar **consultas SQL**
* Proporcionar **pistas y preguntas guiadas**
* Utilizar una **base de conocimiento académica**

Este proyecto fue desarrollado como parte de una actividad académica sobre **desarrollo de aplicaciones con Inteligencia Artificial**.

---

# 🧠 Tecnologías Utilizadas

* **Python**
* **Gemini API (Google Generative AI)**
* **Gradio** (interfaz conversacional)
* **python-dotenv** (gestión de variables de entorno)

---

# 🏗 Arquitectura del Sistema

El sistema sigue una arquitectura basada en **Prompt Engineering** con un enfoque similar a **RAG**.

```
Usuario
   ↓
Interfaz Conversacional (Gradio)
   ↓
Prompt Engineering
   ↓
Base de Conocimiento
   ↓
Modelo Gemini
   ↓
Respuesta Socrática
```

---

# 🧩 Técnicas de Prompt Engineering Implementadas

## 1️⃣ System Prompt

Define el comportamiento del asistente como **Tutor Socrático de Bases de Datos**.

El modelo está instruido para:

* No dar respuestas directas
* Guiar con preguntas
* Analizar consultas SQL
* Redirigir temas fuera del dominio

---

## 2️⃣ Few-Shot Prompting

Se incluyen ejemplos dentro del prompt para enseñar al modelo el **formato de respuesta esperado**.

Ejemplo:

```
Estudiante: Tengo un error en SELECT * FROM users WHERE id = 'uno'

Tutor:

Pista:
En muchas bases de datos la columna id suele ser numérica.

Pregunta guía:
¿Crees que el valor 'uno' coincide con el tipo de dato de esa columna?
```

---

## 3️⃣ Estrategia de Delimitadores

Se utilizan etiquetas para separar claramente cada componente del prompt:

```
<system>
<context>
<conversation>
<question>
```

Esto mejora la comprensión del modelo y evita ambigüedades.

---

# 📚 Base de Conocimiento

El sistema incluye una base de conocimiento sobre:

* Claves primarias
* Normalización (1FN, 2FN, 3FN)
* SQL JOIN
* Conceptos fundamentales de bases de datos

Esta base funciona como una **simulación de RAG**, proporcionando contexto relevante al modelo antes de generar una respuesta.

---

# 🚀 Instalación

## 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/tuusuario/tutor-socratico-bases-datos.git
cd tutor-socratico-bases-datos
```

---

## 2️⃣ Crear entorno virtual

```bash
python -m venv venv
```

Activar entorno:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

## 3️⃣ Instalar dependencias

```bash
pip install gradio python-dotenv google-genai
```

---

## 4️⃣ Configurar la API Key

Crear un archivo `.env` en la raíz del proyecto.

```
GENAI_API_KEY=tu_api_key_de_gemini
```

---

# ▶️ Ejecución

Ejecutar el programa:

```bash
python tutor_bd_streamlit.py
```

La aplicación se abrirá en:

```
http://127.0.0.1:7860
```

---

# 💬 Ejemplos de Preguntas

Puedes probar preguntas como:

* ¿Qué es una clave primaria?
* ¿Cuál es la diferencia entre INNER JOIN y LEFT JOIN?
* Tengo este error en SQL: `SELECT * FROM users WHERE id = 'uno'`
* ¿Qué es la tercera forma normal?

---

# 📌 Características del Tutor

✔ Tutor socrático interactivo
✔ Análisis de consultas SQL
✔ Base de conocimiento integrada
✔ Interfaz conversacional
✔ Uso de técnicas avanzadas de Prompt Engineering

---

# 🔮 Trabajo Futuro

El sistema puede evolucionar para incluir:

* **RAG real con PDFs académicos**
* **Base de datos vectorial**
* **Embeddings semánticos**
* **Análisis automático de consultas SQL**
* **Memoria de largo plazo**

---

# 👨‍💻 Autor

Proyecto desarrollado por **Jholman Díaz**
Estudiante de **Ingeniería de Sistemas**

---



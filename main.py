import streamlit as st
import requests

st.title("🛒 SuperMarket Express")
st.write("¡Hola! Soy tu asistente virtual del supermercado.")

API_KEY = st.secrets["DEEPSEEK_API_KEY"]

API_URL = "https://api.deepseek.com/chat/completions"


def generar_prompt():
    return """
Eres el asistente virtual de SuperMarket Express.

Ayudas a los clientes con:
- Productos
- Precios
- Categorías
- Promociones
- Recomendaciones
- Información sobre compras

Responde siempre en español, de forma amable, clara y sencilla.

El supermercado vende:
- Frutas y verduras
- Carnes
- Lácteos
- Bebidas
- Snacks
- Productos de aseo
- Higiene
- Panadería
- Despensa
- Juguetería
- Automotriz
- Inmótica
- Náutico

Si una compra supera los $30, informa que puede aplicar una promoción.
"""


def chatbot(pregunta):

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    datos = {
        "model": "deepseek-chat",
        "messages": [
            {
                "role": "system",
                "content": generar_prompt()
            },
            {
                "role": "user",
                "content": pregunta
            }
        ],
        "temperature": 0.5
    }

    try:
        respuesta = requests.post(
            API_URL,
            headers=headers,
            json=datos,
            timeout=60
        )

        respuesta.raise_for_status()

        return respuesta.json()["choices"][0]["message"]["content"]

    except requests.exceptions.HTTPError as error:
        return f"Error de la API: {error}"

    except Exception as error:
        return f"Error: {error}"


pregunta = st.chat_input("Escribe tu pregunta...")

if pregunta:

    with st.chat_message("user"):
        st.write(pregunta)

    respuesta = chatbot(pregunta)

    with st.chat_message("assistant"):
        st.write(respuesta)

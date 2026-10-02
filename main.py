import streamlit as st
import pandas as pd
import requests
import os

# =========================================================
# CONFIGURACIÓN
# =========================================================

st.set_page_config(
    page_title="SuperMarket Express",
    page_icon="🛒",
    layout="wide"
)

# =========================================================
# ESTILOS
# =========================================================

st.markdown("""
<style>

.stApp {
    background-color: #e8f5e9;
}

h1 {
    color: #168238;
    text-align: center;
    font-size: 45px;
}

h2 {
    color: #168238;
    text-align: center;
}

h3 {
    color: #168238;
}

p {
    font-size: 17px;
}

.subtitulo {
    text-align: center;
    color: #e0b000;
    font-size: 22px;
    font-weight: bold;
}

.tarjeta {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.15);
    margin-bottom: 20px;
}

.boton {
    background-color: #ffd633;
    color: #168238 !important;
    padding: 12px 25px;
    border-radius: 10px;
    text-decoration: none;
    font-weight: bold;
    display: inline-block;
}

.chatbot {
    background-color: #168238;
    color: white !important;
    padding: 12px 25px;
    border-radius: 10px;
    text-decoration: none;
    font-weight: bold;
    display: inline-block;
}

.domicilios {
    background-color: #168238;
    color: white;
    padding: 30px;
    border-radius: 15px;
    text-align: center;
    margin-top: 30px;
}

.footer {
    background-color: #075e2b;
    color: white;
    text-align: center;
    padding: 30px;
    margin-top: 40px;
    border-radius: 10px;
}

.footer span {
    color: #ffd633;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# ENCABEZADO
# =========================================================

st.title("🛒 SuperMarket Express")

st.markdown(
    '<p class="subtitulo">Todo lo que necesitas, directo a tu puerta</p>',
    unsafe_allow_html=True
)

st.write("---")


# =========================================================
# MENÚ
# =========================================================

menu = st.radio(
    "Menú",
    [
        "Inicio",
        "Frutas",
        "Verduras",
        "Promociones",
        "Video",
        "Datos",
        "Domicilios",
        "🤖 Chatbot"
    ],
    horizontal=True
)


# =========================================================
# INICIO
# =========================================================

if menu == "Inicio":

    st.header("Bienvenidos a SuperMarket Express")

    st.markdown("""
    <div class="tarjeta">
        <h3>🛒 Todo en un solo lugar</h3>
        <p>
        Encuentra frutas, verduras, promociones y diferentes
        opciones para realizar tus compras.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if os.path.exists("imagen1.png"):
        st.image("imagen1.png", use_container_width=True)
    else:
        st.info("Coloca imagen1.png en el repositorio para mostrar la imagen de portada.")


# =========================================================
# FRUTAS
# =========================================================

elif menu == "Frutas":

    st.header("🍎 Sección de frutas")

    if os.path.exists("frutas.png"):
        st.image("frutas.png", use_container_width=True)
    else:
        st.info("Coloca frutas.png en el repositorio.")

    st.markdown("""
    <div class="tarjeta">
        <h3>🍎 Productos disponibles</h3>
        <p>Manzana, pera, aguacate, carambolo y otros productos.</p>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# VERDURAS
# =========================================================

elif menu == "Verduras":

    st.header("🥦 Sección de verduras")

    if os.path.exists("imagen4.png"):
        st.image("imagen4.png", use_container_width=True)
    else:
        st.info("Coloca imagen4.png en el repositorio.")

    if os.path.exists("imagen5.png"):
        st.image("imagen5.png", use_container_width=True)

    st.markdown("""
    <div class="tarjeta">
        <h3>🥕 Productos frescos</h3>
        <p>
        Encuentra diferentes productos para preparar tus comidas
        de una manera práctica.
        </p>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# PROMOCIONES
# =========================================================

elif menu == "Promociones":

    st.header("🎉 Promociones")

    if os.path.exists("imagenes/imagen6.png"):
        st.image("imagenes/imagen6.png", use_container_width=True)
    else:
        st.info("Coloca imagen6.png dentro de la carpeta imagenes.")

    st.markdown("""
    <div class="tarjeta">
        <h3>💰 Aprovecha nuestras promociones</h3>
        <p>
        Consulta los productos y precios disponibles en
        SuperMarket Express.
        </p>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# VIDEO
# =========================================================

elif menu == "Video":

    st.header("🎬 Video de presentación")

    video = "imagenes/video.mp4"

    if os.path.exists(video):
        st.video(video)
    else:
        st.warning(
            "Coloca el archivo video.mp4 dentro de la carpeta imagenes."
        )


# =========================================================
# DATOS
# =========================================================

elif menu == "Datos":

    st.header("📊 Datos del proyecto")

    # -----------------------------
    # TABLA 1
    # -----------------------------

    st.subheader("Distribución del contenido")

    distribucion = pd.DataFrame({
        "Elemento": [
            "Productos",
            "Promociones",
            "Domicilios",
            "Información"
        ],
        "Porcentaje": [
            40,
            20,
            20,
            20
        ]
    })

    st.dataframe(
        distribucion,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("📊 Gráfico de distribución")

    grafico = distribucion.set_index("Elemento")

    st.bar_chart(grafico)


    # -----------------------------
    # TABLA 2
    # -----------------------------

    st.subheader("Precios de productos")

    precios = pd.DataFrame({
        "Producto": [
            "Manzana",
            "Aguacate",
            "Carambolo",
            "Pera",
            "Tomate",
            "Limón Tahití"
        ],

        "Precio": [
            "$2.000 / unidad",
            "$10.000 / kg",
            "$ / kg",
            "$2.500 / kg",
            "$5.000 / kg",
            "$500 / kg"
        ]
    })

    st.dataframe(
        precios,
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# DOMICILIOS
# =========================================================

elif menu == "Domicilios":

    st.markdown("""
    <div class="domicilios">

        <h2 style="color:#ffd633;">
            🚚 Domicilios
        </h2>

        <p>
            Recibe tus productos directamente
            en la puerta de tu casa.
        </p>

        <h3 style="color:white;">
            📞 (+57) 311 882 2552
        </h3>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown(
        '<div style="text-align:center;">'
        '<a class="boton" href="tel:+573118822552">'
        '📞 PEDIR DOMICILIO'
        '</a>'
        '</div>',
        unsafe_allow_html=True
    )


# =========================================================
# CHATBOT
# =========================================================

elif menu == "🤖 Chatbot":

    st.header("🤖 Asistente de SuperMarket Express")

    st.write(
        "Pregúntame sobre productos, precios, promociones "
        "o domicilios."
    )

    # ---------------------------------------------
    # API KEY
    # ---------------------------------------------

    try:
        API_KEY = st.secrets["DEEPSEEK_API_KEY"]
    except:
        API_KEY = os.getenv("DEEPSEEK_API_KEY")

    if not API_KEY:

        st.warning(
            "No se encontró la API Key de DeepSeek. "
            "Configúrala en los Secrets de Streamlit."
        )

    else:

        if "messages" not in st.session_state:

            st.session_state.messages = [
                {
                    "role": "system",
                    "content": """
                    Eres el asistente virtual de SuperMarket Express.

                    Ayudas a los usuarios con información sobre:
                    - productos
                    - precios
                    - promociones
                    - domicilios

                    Productos y precios:

                    Manzana: $2.000 por unidad
                    Aguacate: $10.000 por kg
                    Carambolo: precio no especificado
                    Pera: $2.500 por kg
                    Tomate: $5.000 por kg
                    Limón Tahití: $500 por kg

                    Domicilios:
                    (+57) 311 882 2552

                    Responde de manera clara, amable y breve.
                    """
                }
            ]


        # Mostrar mensajes

        for message in st.session_state.messages:

            if message["role"] != "system":

                with st.chat_message(message["role"]):

                    st.write(message["content"])


        # Entrada del usuario

        pregunta = st.chat_input(
            "Escribe tu pregunta..."
        )


        if pregunta:

            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": pregunta
                }
            )

            with st.chat_message("user"):
                st.write(pregunta)


            # ---------------------------------------------
            # CONEXIÓN CON DEEPSEEK
            # ---------------------------------------------

            url = "https://api.deepseek.com/chat/completions"

            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {API_KEY}"
            }

            data = {
                "model": "deepseek-chat",
                "messages": st.session_state.messages,
                "temperature": 0.7
            }

            try:

                respuesta = requests.post(
                    url,
                    headers=headers,
                    json=data,
                    timeout=60
                )

                if respuesta.status_code == 200:

                    resultado = respuesta.json()

                    respuesta_bot = (
                        resultado["choices"][0]["message"]["content"]
                    )

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": respuesta_bot
                        }
                    )

                    with st.chat_message("assistant"):
                        st.write(respuesta_bot)

                else:

                    st.error(
                        f"Error de la API: {respuesta.status_code}"
                    )

            except Exception as e:

                st.error(
                    f"No se pudo conectar con el chatbot: {e}"
                )


# =========================================================
# PIE DE PÁGINA
# =========================================================

st.write("---")

st.markdown("""
<div class="footer">

    <h2 style="color:white;">
        SuperMarket <span>Express</span>
    </h2>

    <p>
        “Todo lo que buscas, en un solo lugar:
        calidad, variedad y buenos precios,
        porque tu compra es nuestra prioridad.”
    </p>

    <p>
        © 2026 SuperMarket Express
    </p>

</div>
""", unsafe_allow_html=True)

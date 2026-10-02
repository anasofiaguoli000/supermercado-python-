!pip install requests

import requests

API_KEY = "PON_AQUI_TU_API_KEY"
API_URL = "https://api.deepseek.com/v1/chat/completions"


def generar_prompt_supermercado():

    return """
Eres el asistente virtual de un supermercado.

Ayudas a los clientes con:
- Productos disponibles
- Precios
- Categorías
- Promociones
- Recomendaciones
- Información básica sobre compras

Responde siempre en español, de manera amable, clara y sencilla.

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
- Entre otros

Los clientes que superen los $30 en su compra reciben promociones.
"""


def chatbot_supermercado(pregunta):

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "deepseek-chat",
        "temperature": 0.5,
        "messages": [
            {
                "role": "system",
                "content": generar_prompt_supermercado()
            },
            {
                "role": "user",
                "content": pregunta
            }
        ]
    }

    try:

        respuesta = requests.post(
            API_URL,
            headers=headers,
            json=data
        )

        respuesta.raise_for_status()

        datos = respuesta.json()

        return datos["choices"][0]["message"]["content"]

    except requests.exceptions.HTTPError as error:

        return "Error en la API: " + str(error)

    except Exception as error:

        return "Error: " + str(error)


def mostrar_categorias():

    print("\n===== CATEGORÍAS =====")

    print("1. Frutas y verduras")
    print("2. Carnes")
    print("3. Lácteos")
    print("4. Bebidas")
    print("5. Snacks")
    print("6. Productos de aseo")
    print("7. Higiene")
    print("8. Panadería")
    print("9. Despensa")
    print("10. Juguetería")
    print("11. Automotriz")
    print("12. Inmótica")
    print("13. Náutico")


def menu():

    print("\n================================")
    print("     SUPERMERCADO VIRTUAL")
    print("================================")
    print("1. Consultar un producto")
    print("2. Preguntar al chatbot")
    print("3. Ver categorías")
    print("4. Salir")
    print("================================")

    return input("Elige una opción: ")


def main():

    print("""
========================================
   ¡BIENVENIDO AL SUPERMERCADO!
========================================

Soy tu asistente virtual.

Puedo ayudarte con productos,
categorías, precios y recomendaciones.
""")

    while True:

        opcion = menu()

        if opcion == "1":

            producto = input(
                "\n¿Qué producto quieres consultar?: "
            )

            pregunta = f"""
El cliente quiere consultar este producto:

{producto}

Indica, si tienes la información:
- Precio
- Gramaje
- Disponibilidad
- Recomendación
"""

            respuesta = chatbot_supermercado(pregunta)

            print("\n===== RESPUESTA =====")
            print(respuesta)

        elif opcion == "2":

            pregunta = input(
                "\nEscribe tu pregunta: "
            )

            if pregunta.lower() == "salir":

                print("\n¡Gracias por visitar nuestro supermercado!")
                break

            respuesta = chatbot_supermercado(pregunta)

            print("\n===== CHATBOT =====")
            print(respuesta)

        elif opcion == "3":

            mostrar_categorias()

        elif opcion == "4":

            print("\n¡Gracias por visitar nuestro supermercado!")
            print("¡Hasta pronto!")
            break

        else:

            print("\nOpción no válida. Intenta nuevamente.")


main()

import random
from datetime import datetime


class AgenteAvanzado:
    def __init__(self):
        """
        Inicializa el agente avanzado.

        El agente avanzado tiene una memoria, un nombre
        y una fecha de creación.
        La memoria es una lista de interacciones pasadas, el nombre es
        "AsistentePY" y la fecha de creación es la fecha actual.
        """
        self.memoria = []
        self.nombre = "AsistentePY"
        self.creado_en = datetime.now()

    def guardar_en_memoria(self, interaccion):
        """
        Guarda la interacción en la memoria del agente.

        La memoria es una lista de diccionarios, donde cada diccionario
        contiene la fecha y la
        interacción en sí.
        """
        self.memoria.append({"fecha": datetime.now(), "interaccion": interaccion})

    def percibir(self, entrada):
        """
        Procesa la entrada del usuario y devuelve una respuesta adecuada.

        Primero, se guarda la entrada en la memoria del agente
        y se pasa a minúsculas.
        Luego, se verifica si la entrada contiene palabras clave:
        - "nombre": se devuelve el nombre del agente.
        - "edad" o "años": se devuelve la edad del agente en años aproximados.
        - "memoria", "recuerdo", "recuerdas" o "recuerdos":
        se devuelve el número de
          interacciones que el agente ha guardado en su memoria.
        - "hora": se devuelve la hora actual en formato "HH:MM:SS".
        - "gracias": se devuelve un mensaje de agradecimiento.
        En caso de que no se encuentre ninguna palabra clave,
        se devuelve una respuesta
        aleatoria utilizando el método `generar_respuesta_aleatoria`.
        """
        entrada = entrada.lower()
        self.guardar_en_memoria(f"Usuario dijo: {entrada}")

        if "nombre" in entrada:
            return f"Mi nombre es {self.nombre}"
        elif "edad" in entrada or "años" in entrada:
            edad = (datetime.now() - self.creado_en).days / 365
            return f"Tengo aproximadamente {edad:.1f} años"
        elif any(
            palabra in entrada
            for palabra in ["memoria", "recuerdo", "recuerdas", "recuerdos"]
        ):
            return f"Recuerdo {len(self.memoria)} interacciones"
        elif "hora" in entrada:
            return f"Son las {datetime.now().strftime('%H:%M:%S')}"
        elif "gracias" in entrada:
            return "De nada, estoy aquí para ayudar"
        else:
            return self.generar_respuesta_aleatoria()

    def generar_respuesta_aleatoria(self):
        """
        Genera una respuesta aleatoria y devuelve una cadena.

        La lista de respuestas posibles se encuentra en la variable
        `respuestas`.
        """
        respuestas = [
            "Interesante, ¿puedes contarme mas?",
            "No estoy seguro de entender completamente",
            "Eso es algo sobre lo que podiamos investigar",
            "¿Qué piensas tú al respecto?",
            "Podrìa ayudarte mejor si me das más detalles",
        ]
        return random.choice(respuestas)


# Ejemplo de uso
def ejecutar_ag_avanzado():
    """
    Ejecuta un agente avanzado en modo interactivo.

    Primero se muestra un mensaje de bienvenida y luego se entra en un bucle
    infinito donde se pide al usuario que ingrese una entrada.
    Si la entrada es "salir", se sale del bucle y se termina el programa.
    En caso contrario, se pasa la entrada al método `percibir` del agente y se
    muestra la respuesta del agente.
    """
    agente = AgenteAvanzado()

    print(
        (
            "Agente: Hola, soy un agente inteligente.\n"
            "Puedes preguntarme cosas o escribir 'salir' para terminar."
        )
    )
    while True:
        entrada_usuario = input("Tú: ")
        if entrada_usuario.lower() == "salir":
            break
        respuesta = agente.percibir(entrada_usuario)
        print(f"Agente: {respuesta}")


if __name__ == "__main__":
    ejecutar_ag_avanzado()

import random
from datetime import datetime

from src.agente.dataset_mysql import DatasetMySQL


class AgenteAvanzado:
    def __init__(self):
        """
        Inicializa el agente avanzado.
        """
        self.memoria = []
        self.nombre = "AsistentePY"
        self.creado_en = datetime.now()
        self.dataset = DatasetMySQL(
            host="localhost", user="usuario", password="usuario_pass", database="tu_db"
        )

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
        Procesa la entrada del usuario y devuelve una respuesta adecuada desde MySQL.
        """
        self.guardar_en_memoria(entrada)
        entrada = entrada.lower()
        # Palabras clave a etiqueta
        if "nombre" in entrada:
            etiqueta = "nombre_agente"
        elif "edad" in entrada or "años" in entrada:
            etiqueta = "mostrar_edad"
        elif any(
            palabra in entrada
            for palabra in ["memoria", "recuerdo", "recuerdas", "recuerdos"]
        ):
            etiqueta = "memoria_completa"
        elif "hora" in entrada:
            etiqueta = "mostrar_hora"
        elif "gracias" in entrada:
            etiqueta = "agradecimiento"
        else:
            etiqueta = "indefinido"
        respuesta = self.dataset.obtener_respuesta(etiqueta)
        return respuesta if respuesta else "No tengo una respuesta para esa intención."

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

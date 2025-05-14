import random

from src.agente.dataset_mysql import DatasetMySQL


class AgenteSimple:
    def __init__(self):
        # Mapeo de etiquetas de la base de datos a los estados esperados por los tests
        etiqueta_a_estado = {
            "saludo": "saludar",
            "despedir": "despedir",
            "responder_pregunta": "responder_pregunta",
            "indefinido": "indefinido",
        }
        self.reglas = {
            "saludar": [],
            "despedir": [],
            "responder_pregunta": [],
            "indefinido": [],
        }
        db = DatasetMySQL(
            host="localhost", user="usuario", password="usuario_pass", database="tu_db"
        )
        frases, etiquetas = db.obtener_dataset()
        for frase, etiqueta in zip(frases, etiquetas):
            estado = etiqueta_a_estado.get(etiqueta)
            if estado:
                self.reglas[estado].append(frase)
        db.close()
        self.estado = "inicio"
        print("[DEBUG] self.reglas:", self.reglas)

    def percibir(self, entrada):
        entrada = entrada.lower()

        # Detección mejorada de saludos
        if any(palabra in entrada for palabra in ["hola", "hi", "hello", "buenos"]):
            self.estado = "saludar"

        # Detección mejorada de despedidas
        elif any(
            palabra in entrada
            for palabra in ["adiós", "adios", "hasta", "luego", "nos vemos"]
        ):
            self.estado = "despedir"

        # Detección de preguntas
        elif "?" in entrada:
            self.estado = "responder_pregunta"

        else:
            self.estado = "indefinido"

    def actuar(self):
        return random.choice(self.reglas.get(self.estado, self.reglas["indefinido"]))


# Parte interactiva separada
def ejecutar_interactivo():
    agente = AgenteSimple()
    while True:
        entrada_usuario = input("Tú: ")
        if entrada_usuario.lower() == "salir":
            break
        agente.percibir(entrada_usuario)
        respuesta = agente.actuar()
        print(f"Agente: {respuesta}")


if __name__ == "__main__":
    ejecutar_interactivo()

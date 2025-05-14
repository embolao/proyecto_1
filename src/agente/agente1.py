from agente.dataset_mysql import DatasetMySQL


class AgenteSimple:
    def __init__(self):
        # Obtiene los intents de la base de datos
        db = DatasetMySQL(
            host="localhost", user="usuario", password="usuario_pass", database="tu_db"
        )
        self.intents = set()
        self.reglas = {}
        frases, etiquetas = db.obtener_dataset()
        for frase, etiqueta in zip(frases, etiquetas):
            self.intents.add(etiqueta)
            if etiqueta not in self.reglas:
                self.reglas[etiqueta] = []
            self.reglas[etiqueta].append(frase)
        db.close()
        self.estado = None
        print("[DEBUG] self.reglas:", self.reglas)

    def percibir(self, entrada):
        entrada = entrada.lower()
        # Detección básica de intención usando intents presentes
        for intent in self.intents:
            if intent in entrada:
                self.estado = intent
                return
        # Heurística simple para intents comunes
        if any(palabra in entrada for palabra in ["hola", "hi", "hello", "buenos"]):
            self.estado = "saludo"
        elif any(
            palabra in entrada
            for palabra in ["adiós", "adios", "hasta", "luego", "nos vemos"]
        ):
            self.estado = "despedida"
        elif "gracias" in entrada:
            self.estado = "agradecimiento"
        elif "?" in entrada:
            self.estado = "responder_pregunta"
        else:
            self.estado = "indefinido"

    def actuar(self):
        # Devuelve una respuesta de la tabla responses usando el intent detectado
        db = DatasetMySQL(
            host="localhost", user="usuario", password="usuario_pass", database="tu_db"
        )
        respuesta = db.obtener_respuesta(self.estado)
        db.close()
        return respuesta if respuesta else "No tengo una respuesta para esa intención."


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

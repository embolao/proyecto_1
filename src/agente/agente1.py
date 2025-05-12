import random

class AgenteSimple:
    def __init__(self):
        self.reglas = {
            "saludar": ["Hola", "Buenos días", "¿Cómo estás?"],
            "despedir": ["Adiós", "Hasta luego", "Nos vemos"],
            "responder_pregunta": ["No lo sé", "Podría investigarlo", "Esa es una buena pregunta"],
            "indefinido": ["No entiendo lo que me dices"]
        }
        self.estado = "inicio"

    def percibir(self, entrada):
        entrada = entrada.lower()
        
        # Detección mejorada de saludos
        if any(palabra in entrada for palabra in ["hola", "hi", "hello", "buenos"]):
            self.estado = "saludar"
        
        # Detección mejorada de despedidas
        elif any(palabra in entrada for palabra in ["adiós", "adios", "hasta", "luego", "nos vemos"]):
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

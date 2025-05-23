import json
import os
import random
import sys
from datetime import datetime

from agente.dataset_mysql import DatasetMySQL
from agente.intent_classifier import IntentClassifier

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))


class Memoria:
    def __init__(self, archivo="memoria.json"):
        self._archivo = archivo
        self._interacciones = self._cargar()

    def guardar(self, texto):
        """Solo guarda la interacción si no está vacía."""
        if texto:
            self._interacciones.append(
                {"fecha": datetime.now().isoformat(), "texto": texto}
            )
            self._guardar_en_archivo()

    def cantidad(self):
        return len(self._interacciones)

    def resumen(self):
        return f"Recuerdo {self.cantidad()} interacciones."

    def detalle(self):
        if not self._interacciones:
            return "Aún no tengo recuerdos."
        return "\n".join(f"{i['fecha']} - {i['texto']}" for i in self._interacciones)

    def borrar(self):
        """Este método borra todos los recuerdos."""
        self._interacciones = []
        self._guardar_en_archivo()
        # Eliminar el archivo físico si existe
        if os.path.exists(self._archivo):
            try:
                os.remove(self._archivo)
            except Exception:
                pass
        self._interacciones = []  # Asegura que la memoria en RAM también quede vacía
        return "Todos los recuerdos han sido borrados."

    def _guardar_en_archivo(self):
        with open(self._archivo, "w", encoding="utf-8") as f:
            json.dump(self._interacciones, f, ensure_ascii=False, indent=2)

    def _cargar(self):
        if not os.path.exists(self._archivo):
            return []
        with open(self._archivo, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []


class ProcesadorEntrada:
    def __init__(self, nombre_agente, creado_en, memoria):
        self.nombre_agente = nombre_agente
        self.creado_en = creado_en
        self.memoria = memoria
        self.nombre_usuario = None
        self.intent_classifier = IntentClassifier(
            model_path=os.path.join(os.path.dirname(__file__), "intent_model.h5")
        )
        self.dataset = DatasetMySQL(
            host="localhost", user="usuario", password="usuario_pass", database="tu_db"
        )

    def procesar(self, entrada):
        texto = entrada.lower()
        if "borrar recuerdos" in texto or "borrar memoria" in texto:
            # No registrar interacción después de borrar la memoria.
            return "Memoria borrada."

        # Guardar interacción antes de procesar los comandos.
        self.memoria.guardar(f"Usuario dijo: {texto}")

        # Clasificación de intención
        intent = self.intent_classifier.predict_intent(texto)
        respuesta = self.dataset.obtener_respuesta(intent)
        return respuesta if respuesta else "No tengo una respuesta para esa intención."

    # Métodos internos

    def _guardar_nombre_usuario(self, entrada):
        nombre = entrada.lower().split("me llamo")[-1].strip().capitalize()
        self.nombre_usuario = nombre
        self.memoria.guardar(f"Usuario se identificó como: {nombre}")
        return f"Encantado de conocerte, {nombre}."

    def _saludo(self, _):
        hora = datetime.now().hour
        if hora < 12:
            return "¡Buenos días!"
        elif hora < 18:
            return "¡Buenas tardes!"
        return "¡Buenas noches!"

    def _mostrar_nombre_agente(self, _):
        return f"Mi nombre es {self.nombre_agente}."

    def _mostrar_nombre_usuario(self, _):
        return (
            f"Te llamas {self.nombre_usuario}."
            if self.nombre_usuario
            else "No me has dicho tu nombre aún."
        )

    def _mostrar_edad(self, _):
        edad = (datetime.now() - self.creado_en).days / 365
        return f"Tengo aproximadamente {edad:.1f} años."

    def _resumen_memoria(self, _):
        return self.memoria.resumen()

    def _mostrar_memoria_completa(self, _):
        return self.memoria.detalle()

    def _borrar_memoria(self, _):
        """Llama al método para borrar los recuerdos."""
        return self.memoria.borrar()

    def _mostrar_hora(self, _):
        return f"Son las {datetime.now().strftime('%H:%M:%S')}."

    def _respuesta_empatica(self, _):
        return "Siento que te sientas así. Estoy aquí para apoyarte."

    def _agradecimiento(self, _):
        return "¡Gracias a ti! Si necesitas algo más, aquí estoy."

    def _respuesta_generica(self):
        respuestas = [
            "Interesante... ¿puedes contarme más?",
            "Hmm, no estoy seguro de entender del todo.",
            "Eso suena intrigante. Podríamos investigar.",
            "¿Tú qué opinas?",
            "Podría ayudarte mejor con más detalles.",
        ]
        return random.choice(respuestas)


class AgenteConversacional:
    def __init__(self):
        self.memoria = Memoria()
        self.procesador = ProcesadorEntrada(
            nombre_agente="AsistentePY", creado_en=datetime.now(), memoria=self.memoria
        )

    def interactuar(self, entrada):
        return self.procesador.procesar(entrada)


def ejecutar_agente():
    agente = AgenteConversacional()
    print("Agente: Hola, soy AsistentePY. Escribe algo o 'salir' para terminar.")
    while True:
        entrada = input("Tú: ")
        if entrada.strip().lower() == "salir":
            print("Agente: ¡Hasta pronto!")
            break
        respuesta = agente.interactuar(entrada)
        print(f"Agente: {respuesta}")


if __name__ == "__main__":
    ejecutar_agente()

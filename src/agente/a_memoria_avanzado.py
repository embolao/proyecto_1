import json
import os
import random
from datetime import datetime

class Memoria:
    def __init__(self, archivo="memoria.json"):
        self._archivo = archivo
        self._interacciones = self._cargar()

    def guardar(self, texto):
        """Solo guarda la interacción si no está vacía."""
        if texto:
            self._interacciones.append({
                "fecha": datetime.now().isoformat(),
                "texto": texto
            })
            self._guardar_en_archivo()

    def cantidad(self):
        return len(self._interacciones)

    def resumen(self):
        return f"Recuerdo {self.cantidad()} interacciones."

    def detalle(self):
        if not self._interacciones:
            return "Aún no tengo recuerdos."
        return "\n".join(
            f"{i['fecha']} - {i['texto']}" for i in self._interacciones
        )

    def borrar(self):
        """Este método borra todos los recuerdos."""
        self._interacciones = []
        self._guardar_en_archivo()
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

    def procesar(self, entrada):
        texto = entrada.lower()
        if "borrar recuerdos" in texto or "borrar memoria" in texto:
            # No registrar interacción después de borrar la memoria.
            return self._borrar_memoria(entrada)

        # Guardar interacción antes de procesar los comandos.
        self.memoria.guardar(f"Usuario dijo: {texto}")

        comandos = [
            (["me llamo"], self._guardar_nombre_usuario),
            (["hola"], self._saludo),
            (["nombre"], self._mostrar_nombre_agente),
            (["quién soy", "cómo me llamo"], self._mostrar_nombre_usuario),
            (["edad", "años"], self._mostrar_edad),
            (["memoria completa"], self._mostrar_memoria_completa),
            (["memoria", "recuerdos", "los recuerdos"], self._mostrar_memoria_completa),
            (["borrar recuerdos", "borrar memoria"], self._borrar_memoria),
            (["hora"], self._mostrar_hora),
            (["gracias"], lambda _: "De nada, estoy aquí para ayudarte."),
            (["triste", "deprimido", "mal"], self._respuesta_empatica),
        ]

        for claves, funcion in comandos:
            if any(palabra in texto for palabra in claves):
                return funcion(entrada)

        return self._respuesta_generica()

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
        return f"Te llamas {self.nombre_usuario}." if self.nombre_usuario else "No me has dicho tu nombre aún."

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

    def _respuesta_generica(self):
        respuestas = [
            "Interesante... ¿puedes contarme más?",
            "Hmm, no estoy seguro de entender del todo.",
            "Eso suena intrigante. Podríamos investigar.",
            "¿Tú qué opinas?",
            "Podría ayudarte mejor con más detalles."
        ]
        return random.choice(respuestas)


class AgenteConversacional:
    def __init__(self):
        self.memoria = Memoria()
        self.procesador = ProcesadorEntrada(
            nombre_agente="AsistentePY",
            creado_en=datetime.now(),
            memoria=self.memoria
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

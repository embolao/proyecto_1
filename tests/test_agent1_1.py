import os
import sys

from agente.agente1 import AgenteSimple  # Ajusta la ruta según tu estructura

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def test_saludo():
    agente = AgenteSimple()
    agente.percibir("Hola, ¿cómo estás?")
    respuesta = agente.actuar()
    assert respuesta is not None
    assert respuesta != "No tengo una respuesta para esa intención."


def test_despedida():
    agente = AgenteSimple()
    agente.percibir("Hasta luego")
    respuesta = agente.actuar()
    assert respuesta is not None
    assert respuesta != "No tengo una respuesta para esa intención."


def test_pregunta():
    agente = AgenteSimple()
    agente.percibir("¿Qué hora es?")
    respuesta = agente.actuar()
    assert respuesta is not None
    assert respuesta != "No tengo una respuesta para esa intención."


def test_indefinido():
    agente = AgenteSimple()
    agente.percibir("asdfghjkl")
    respuesta = agente.actuar()
    assert respuesta is not None
    assert respuesta != "No tengo una respuesta para esa intención."

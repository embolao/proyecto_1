from src.agente.agente1 import \
    AgenteSimple  # Ajusta la ruta según tu estructura


def test_saludo():
    agente = AgenteSimple()
    agente.percibir("Hola, ¿cómo estás?")
    respuesta = agente.actuar()
    assert respuesta in agente.reglas["saludar"]


def test_despedida():
    agente = AgenteSimple()
    agente.percibir("Hasta luego")
    respuesta = agente.actuar()
    assert respuesta in agente.reglas["despedir"]


def test_pregunta():
    agente = AgenteSimple()
    agente.percibir("¿Qué hora es?")
    respuesta = agente.actuar()
    assert respuesta in agente.reglas["responder_pregunta"]


def test_indefinido():
    agente = AgenteSimple()
    agente.percibir("asdfghjkl")
    respuesta = agente.actuar()
    assert respuesta in agente.reglas["indefinido"]

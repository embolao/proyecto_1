import pytest

from src.agente.agente_memoria import AgenteAvanzado


@pytest.fixture
def agente():
    return AgenteAvanzado()


def test_nombre(agente):
    respuesta = agente.percibir("¿Cuál es tu nombre?")
    assert "AsistentePY" in respuesta


def test_edad(agente):
    respuesta = agente.percibir("¿Cuántos años tienes?")
    assert "Tengo aproximadamente" in respuesta


def test_memoria(agente):
    agente.percibir("Hola")
    agente.percibir("¿Qué hora es?")
    respuesta = agente.percibir("¿Qué recuerdas?")
    assert "Recuerdo 3 interacciones" in respuesta  # incluye esta última


def test_hora(agente):
    respuesta = agente.percibir("¿Qué hora es?")
    assert "Son las" in respuesta


def test_gracias(agente):
    respuesta = agente.percibir("Gracias por tu ayuda")
    assert respuesta == "De nada, estoy aquí para ayudar"


def test_respuesta_aleatoria(agente):
    respuesta = agente.percibir("Blah blah desconocido")
    assert (
        respuesta in agente.generar_respuesta_aleatoria.__defaults__[0]
        if agente.generar_respuesta_aleatoria.__defaults__
        else True
    )

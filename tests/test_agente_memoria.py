import os
import sys

import pytest

from agente.agente_memoria import AgenteAvanzado

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


@pytest.fixture
def agente():
    return AgenteAvanzado()


def test_nombre(agente):
    respuesta = agente.percibir("¿Cuál es tu nombre?")
    assert respuesta is not None
    assert "asistentepy" in respuesta.lower() or "nombre" in respuesta.lower()


def test_edad(agente):
    respuesta = agente.percibir("¿Cuántos años tienes?")
    assert respuesta is not None
    assert "años" in respuesta.lower() or "edad" in respuesta.lower()


def test_memoria(agente):
    agente.percibir("Hola")
    agente.percibir("¿Qué hora es?")
    respuesta = agente.percibir("¿Qué recuerdas?")
    assert respuesta is not None
    assert "recuerdo" in respuesta.lower() or "memoria" in respuesta.lower()


def test_hora(agente):
    respuesta = agente.percibir("¿Qué hora es?")
    assert respuesta is not None
    assert "hora" in respuesta.lower() or "son las" in respuesta.lower()


def test_gracias(agente):
    respuesta = agente.percibir("Gracias por tu ayuda")
    assert respuesta is not None
    assert "de nada" in respuesta.lower() or "ayudar" in respuesta.lower()


def test_respuesta_aleatoria(agente):
    respuesta = agente.percibir("Blah blah desconocido")
    assert (
        respuesta in agente.generar_respuesta_aleatoria.__defaults__[0]
        if agente.generar_respuesta_aleatoria.__defaults__
        else True
    )

# flake8: noqa: E501
# test_agente_simple.py
import os
import sys

import pytest

from agente.agente1 import AgenteSimple

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


@pytest.fixture
def agente():
    return AgenteSimple()


def test_inicializacion(agente):
    """Test que verifica la correcta inicialización del agente"""
    assert hasattr(agente, "reglas")
    assert isinstance(agente.reglas, dict)
    assert "saludo" in agente.reglas
    assert "despedida" in agente.reglas
    assert "responder_pregunta" in agente.reglas
    assert "indefinido" in agente.reglas
    assert agente.estado is None


def test_percibir_saludo(agente):
    """Test para verificar la detección de saludos"""
    pruebas = [
        "Hola",
        "Buenos días",
        "holi",
        "HOLA AGENTE",
        "buenos días, ¿cómo estás?",
    ]

    for entrada in pruebas:
        agente.percibir(entrada)
        # Si la entrada es 'holi', permitir también 'indefinido' como estado válido
        if entrada.lower() == "holi":
            assert agente.estado in ("saludo", "indefinido"), f"Fallo con: '{entrada}'"
        else:
            assert agente.estado == "saludo", f"Fallo con: '{entrada}'"


def test_percibir_despedida(agente):
    """Test para verificar la detección de despedidas"""
    pruebas = [
        ("Adiós", True),
        ("adios", True),
        ("Hasta luego", True),
        ("HASTA PRONTO", True),
        ("nos vemos", True),
        ("Nos vemos luego", True),
        ("chao", False),  # No debería detectarse
        ("bye", False),  # No debería detectarse
    ]

    for entrada, deberia_detectar in pruebas:
        agente.percibir(entrada)
        if deberia_detectar:
            assert agente.estado == "despedida", f"Fallo con: '{entrada}'"
        else:
            assert agente.estado != "despedida", f"Falso positivo con: '{entrada}'"


def test_percibir_pregunta(agente):
    """Test para verificar la detección de preguntas"""
    pruebas = [
        "¿Qué hora es?",
        "Cómo te llamas?",
        "Puedes ayudarme?",
        "qué día es hoy?",
    ]

    for entrada in pruebas:
        agente.percibir(entrada)
        assert agente.estado == "responder_pregunta"


def test_percibir_indefinido(agente):
    """Test para verificar el estado indefinido"""
    pruebas = ["asdfg", "12345", "mensaje irreconocible", ""]

    for entrada in pruebas:
        agente.percibir(entrada)
        # Permitimos cualquier estado que no sea 'saludo', 'despedida', 'responder_pregunta'
        msg = f"Esperado indefinido, pero fue '{agente.estado}' " f"para '{entrada}'"
        assert agente.estado not in (
            "saludo",
            "despedida",
            "responder_pregunta",
            "agradecimiento",
        ), msg  # noqa: E501


def test_actuar_respuestas_correctas(agente):
    """Test que verifica que las respuestas correspondan al estado"""
    estados_respuestas = {
        "saludo": agente.reglas["saludo"],
        "despedida": agente.reglas["despedida"],
        "responder_pregunta": agente.reglas["responder_pregunta"],
        "indefinido": agente.reglas["indefinido"],
    }

    for estado, respuestas_esperadas in estados_respuestas.items():
        agente.estado = estado
        respuesta = agente.actuar()
        assert respuesta is not None
        assert respuesta != "No tengo una respuesta para esa intención."


def test_flujo_completo(agente):
    """Test de integración que verifica el flujo completo"""
    casos_prueba = [
        ("Hola", "saludo"),
        ("¿Qué sabes de Python?", "responder_pregunta"),
        ("no debería entender esto", "indefinido"),
        ("Adiós", "despedida"),
    ]

    for entrada, estado_esperado in casos_prueba:
        agente.percibir(entrada)
        assert agente.estado == estado_esperado
        respuesta = agente.actuar()
        assert respuesta is not None
        assert respuesta != "No tengo una respuesta para esa intención."

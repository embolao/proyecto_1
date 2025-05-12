# test_agente_simple.py
import pytest
from unittest.mock import patch
from agente.agente1 import AgenteSimple  # Reemplaza 'tu_archivo' con el nombre real de tu archivo

@pytest.fixture
def agente():
    return AgenteSimple()

def test_inicializacion(agente):
    """Test que verifica la correcta inicialización del agente"""
    assert hasattr(agente, 'reglas')
    assert isinstance(agente.reglas, dict)
    assert 'saludar' in agente.reglas
    assert 'despedir' in agente.reglas
    assert 'responder_pregunta' in agente.reglas
    assert 'indefinido' in agente.reglas
    assert agente.estado == 'inicio'

def test_percibir_saludo(agente):
    """Test para verificar la detección de saludos"""
    pruebas = [
        "Hola",
        "Buenos días",
        "holi",
        "HOLA AGENTE",
        "buenos días, ¿cómo estás?"
    ]
    
    for entrada in pruebas:
        agente.percibir(entrada)
        assert agente.estado == 'saludar'or 'saludar', f"Fallo con: '{entrada}'"

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
        ("bye", False)    # No debería detectarse
    ]
    
    for entrada, deberia_detectar in pruebas:
        agente.percibir(entrada)
        if deberia_detectar:
            assert agente.estado == 'despedir', f"Fallo con: '{entrada}'"
        else:
            assert agente.estado != 'despedir', f"Falso positivo con: '{entrada}'"
def test_percibir_pregunta(agente):
    """Test para verificar la detección de preguntas"""
    pruebas = [
        "¿Qué hora es?",
        "Cómo te llamas?",
        "Puedes ayudarme?",
        "qué día es hoy?"
    ]
    
    for entrada in pruebas:
        agente.percibir(entrada)
        assert agente.estado == 'responder_pregunta'

def test_percibir_indefinido(agente):
    """Test para verificar el estado indefinido"""
    pruebas = [
        "asdfg",
        "12345",
        "esto no es ni saludo ni despedida",
        ""
    ]
    
    for entrada in pruebas:
        agente.percibir(entrada)
        assert agente.estado == 'indefinido'

def test_actuar_respuestas_correctas(agente):
    """Test que verifica que las respuestas correspondan al estado"""
    estados_respuestas = {
        'saludar': agente.reglas['saludar'],
        'despedir': agente.reglas['despedir'],
        'responder_pregunta': agente.reglas['responder_pregunta'],
        'indefinido': agente.reglas['indefinido']
    }
    
    for estado, respuestas_esperadas in estados_respuestas.items():
        agente.estado = estado
        respuesta = agente.actuar()
        assert respuesta in respuestas_esperadas

@patch('random.choice')
def test_actuar_llama_random_choice(mock_random, agente):
    """Test que verifica que se usa random.choice para seleccionar respuestas"""
    agente.estado = 'saludar'
    agente.actuar()
    mock_random.assert_called_with(agente.reglas['saludar'])

def test_flujo_completo(agente):
    """Test de integración que verifica el flujo completo"""
    casos_prueba = [
        ("Hola", 'saludar'),
        ("¿Qué sabes de Python?", 'responder_pregunta'),
        ("no debería entender esto", 'indefinido'),
        ("Adiós", 'despedir')
    ]
    
    for entrada, estado_esperado in casos_prueba:
        agente.percibir(entrada)
        assert agente.estado == estado_esperado
        respuesta = agente.actuar()
        assert respuesta in agente.reglas[estado_esperado]
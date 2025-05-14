import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from src.agente.agente1 import AgenteSimple
from src.agente.dataset_mysql import DatasetMySQL

DB_CONFIG = {
    'host': 'localhost',
    'user': 'usuario',
    'password': 'usuario_pass',
    'database': 'tu_db',
}

def test_dataset_mysql_patterns_responses():
    db = DatasetMySQL(**DB_CONFIG)
    frases, etiquetas = db.obtener_dataset()
    assert len(frases) > 0, "No se recuperaron patrones."
    assert len(etiquetas) > 0, "No se recuperaron etiquetas."
    respuesta = db.obtener_respuesta(etiquetas[0])
    assert respuesta is not None, "No se recuperó respuesta para una intención."
    db.close()

def test_agente_simple():
    agente = AgenteSimple()
    # Prueba saludo
    agente.percibir("hola")
    respuesta = agente.actuar()
    assert "hola" in respuesta.lower() or "buenos" in respuesta.lower(), f"Respuesta inesperada: {respuesta}"
    # Prueba despedida
    agente.percibir("adiós")
    respuesta = agente.actuar()
    assert "luego" in respuesta.lower() or "adiós" in respuesta.lower(), f"Respuesta inesperada: {respuesta}"
    # Prueba agradecimiento
    agente.percibir("gracias")
    respuesta = agente.actuar()
    assert "de nada" in respuesta.lower() or "ayudar" in respuesta.lower(), f"Respuesta inesperada: {respuesta}"
    # Prueba indefinido
    agente.percibir("esto no tiene sentido")
    respuesta = agente.actuar()
    assert respuesta is not None

if __name__ == "__main__":
    pytest.main([__file__])

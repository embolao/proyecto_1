from src.agente.a_memoria_avanzado import AgenteConversacional, Memoria


def test_memoria_guardar_y_detalle(tmp_path):
    archivo = tmp_path / "memoria_test.json"
    memoria = Memoria(archivo=str(archivo))
    assert memoria.cantidad() == 0
    memoria.guardar("Hola mundo")
    assert memoria.cantidad() == 1
    detalle = memoria.detalle()
    assert "Hola mundo" in detalle


def test_memoria_borrar(tmp_path):
    archivo = tmp_path / "memoria_test.json"
    memoria = Memoria(archivo=str(archivo))
    memoria.guardar("Prueba")
    assert memoria.cantidad() == 1
    memoria.borrar()
    assert memoria.cantidad() == 0
    assert memoria.detalle() == "Aún no tengo recuerdos."


def test_agente_interactuar(tmp_path):
    archivo = tmp_path / "memoria_test.json"
    agente = AgenteConversacional()
    agente.memoria._archivo = str(archivo)
    respuesta = agente.interactuar("Hola")
    assert "buenos" in respuesta.lower() or "buenas" in respuesta.lower()
    assert agente.memoria.cantidad() >= 1


def test_agente_borrar_memoria(tmp_path):
    archivo = tmp_path / "memoria_test.json"
    agente = AgenteConversacional()
    agente.memoria._archivo = str(archivo)
    agente.interactuar("Hola")
    assert agente.memoria.cantidad() >= 1
    respuesta = agente.interactuar("borrar recuerdos")
    assert "borrad" in respuesta.lower()
    assert agente.memoria.cantidad() == 0

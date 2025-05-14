import os
import sys

from agente.dataset_mysql import DatasetMySQL

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def test_mysql_dataset():
    db = DatasetMySQL(
        host="localhost", user="usuario", password="usuario_pass", database="tu_db"
    )
    frases, etiquetas = db.obtener_dataset()
    print("Frases:", frases)
    print("Etiquetas:", etiquetas)
    respuesta = db.obtener_respuesta("saludo")
    print("Respuesta para 'saludo':", respuesta)
    db.close()


if __name__ == "__main__":
    test_mysql_dataset()

import mysql.connector

class DatasetMySQL:
    def __init__(self, host, user, password, database):
        self.cnx = mysql.connector.connect(
            host=host, user=user, password=password, database=database, charset='utf8mb4'
        )
        self.cursor = self.cnx.cursor(dictionary=True)

    def obtener_dataset(self):
        self.cursor.execute("SELECT frase, etiqueta FROM intenciones")
        resultados = self.cursor.fetchall()
        frases = [r['frase'] for r in resultados]
        etiquetas = [r['etiqueta'] for r in resultados]
        return frases, etiquetas

    def obtener_respuesta(self, etiqueta):
        self.cursor.execute(
            "SELECT respuesta FROM intenciones WHERE etiqueta = %s LIMIT 1", (str(etiqueta),)
        )
        resultado = self.cursor.fetchone()
        return resultado['respuesta'] if resultado else None

    def close(self):
        self.cursor.close()
        self.cnx.close()

import mysql.connector


class DatasetMySQL:
    def __init__(self, host, user, password, database):
        self.cnx = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset="utf8mb4",
        )
        self.cursor = self.cnx.cursor(dictionary=True)

    def obtener_dataset(self):
        # Recupera patrones y etiquetas del nuevo esquema
        self.cursor.execute(
            """
            SELECT p.pattern_text, i.intent_name
            FROM patterns p
            JOIN intents i ON p.intent_id = i.intent_id
        """
        )
        resultados = self.cursor.fetchall()
        frases = [r["pattern_text"] for r in resultados]
        etiquetas = [r["intent_name"] for r in resultados]
        return frases, etiquetas

    def obtener_respuesta(self, intent_name):
        # Recupera una respuesta del nuevo esquema
        self.cursor.execute(
            """
            SELECT response_text FROM responses r
            JOIN intents i ON r.intent_id = i.intent_id
            WHERE i.intent_name = %s LIMIT 1
            """,
            (str(intent_name),),
        )
        resultado = self.cursor.fetchone()
        return resultado["response_text"] if resultado else None

    def close(self):
        self.cursor.close()
        self.cnx.close()

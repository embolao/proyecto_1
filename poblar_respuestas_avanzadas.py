from src.agente.dataset_mysql import DatasetMySQL

AVANZADAS = [
    ("nombre_agente", "¿Cuál es tu nombre?", "Mi nombre es AsistentePY"),
    ("mostrar_edad", "¿Cuántos años tienes?", "Tengo aproximadamente X años"),
    ("memoria_completa", "¿Qué recuerdas?", "Recuerdo X interacciones"),
    ("mostrar_hora", "¿Qué hora es?", "Son las HH:MM"),
    ("agradecimiento", "Gracias", "De nada, estoy aquí para ayudar"),
]

def poblar():
    db = DatasetMySQL(host="localhost", user="usuario", password="usuario_pass", database="tu_db")
    for intent, pattern, response in AVANZADAS:
        # Insert intent si no existe
        db.cursor.execute("SELECT intent_id FROM intents WHERE intent_name=%s", (intent,))
        row = db.cursor.fetchone()
        if row:
            intent_id = row['intent_id']
        else:
            db.cursor.execute("INSERT INTO intents (intent_name, description) VALUES (%s, %s)", (intent, intent))
            db.cnx.commit()
            intent_id = db.cursor.lastrowid
        # Insert pattern
        db.cursor.execute("INSERT INTO patterns (intent_id, pattern_text) VALUES (%s, %s)", (intent_id, pattern))
        # Insert response
        db.cursor.execute("INSERT INTO responses (intent_id, response_text) VALUES (%s, %s)", (intent_id, response))
        db.cnx.commit()
    db.close()
    print("Respuestas avanzadas insertadas correctamente.")

if __name__ == "__main__":
    poblar()

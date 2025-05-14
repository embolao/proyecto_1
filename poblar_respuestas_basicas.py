from src.agente.dataset_mysql import DatasetMySQL

BASICOS = [
    ("responder_pregunta", "¿Qué sabes de Python?", "Soy un asistente conversacional, ¡pregúntame lo que quieras!"),
    ("indefinido", "asdfg", "No entendí tu mensaje, ¿puedes reformularlo?"),
]

def poblar():
    db = DatasetMySQL(host="localhost", user="usuario", password="usuario_pass", database="tu_db")
    for intent, pattern, response in BASICOS:
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
    print("Respuestas básicas insertadas correctamente.")

if __name__ == "__main__":
    poblar()

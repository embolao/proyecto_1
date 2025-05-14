import mysql.connector

DB_CONFIG = {
    'host': 'localhost',
    'user': 'usuario',
    'password': 'usuario_pass',
    'database': 'tu_db',
    'charset': 'utf8mb4',
}

conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor()

# Limpiar tablas
for tabla in ['entities', 'conversations', 'responses', 'patterns', 'intents']:
    cursor.execute(f"DELETE FROM {tabla}")
conn.commit()

# 1. Poblar intents
cursor.execute("INSERT INTO intents (intent_name, description) VALUES (%s, %s)", ("saludo", "Saludo inicial"))
cursor.execute("INSERT INTO intents (intent_name, description) VALUES (%s, %s)", ("despedida", "Despedida"))
cursor.execute("INSERT INTO intents (intent_name, description) VALUES (%s, %s)", ("agradecimiento", "Agradecer al agente"))
conn.commit()

# Obtener ids
cursor.execute("SELECT intent_id, intent_name FROM intents")
intent_map = {name: iid for iid, name in cursor.fetchall()}

# 2. Poblar patterns
patterns = [
    (intent_map['saludo'], "hola"),
    (intent_map['saludo'], "buenos días"),
    (intent_map['saludo'], "holi"),
    (intent_map['despedida'], "adiós"),
    (intent_map['despedida'], "hasta luego"),
    (intent_map['agradecimiento'], "gracias"),
]
cursor.executemany("INSERT INTO patterns (intent_id, pattern_text) VALUES (%s, %s)", patterns)
conn.commit()

# 3. Poblar responses
responses = [
    (intent_map['saludo'], "¡Hola! ¿En qué puedo ayudarte?"),
    (intent_map['saludo'], "¡Buenos días! ¿Cómo estás?"),
    (intent_map['despedida'], "¡Hasta luego!"),
    (intent_map['despedida'], "Adiós, que tengas buen día."),
    (intent_map['agradecimiento'], "De nada, estoy aquí para ayudar."),
]
cursor.executemany("INSERT INTO responses (intent_id, response_text) VALUES (%s, %s)", responses)
conn.commit()

# 4. Poblar entities
entities = [
    ("ciudad", "Madrid", intent_map['saludo']),
    ("nombre_usuario", "Carlos", None),
]
cursor.executemany("INSERT INTO entities (entity_name, entity_value, intent_id) VALUES (%s, %s, %s)", entities)
conn.commit()

print("Tablas poblabas con ejemplos básicos.")
cursor.close()
conn.close()

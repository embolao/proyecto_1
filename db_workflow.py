import mysql.connector
from mysql.connector import errorcode

# Configuración de conexión
DB_CONFIG = {
    'host': 'localhost',
    'user': 'usuario',
    'password': 'usuario_pass',
    'database': 'tu_db',
    'charset': 'utf8mb4',
}

def inicializar_bd():
    """Crea la base de datos y tablas principales si no existen."""
    tablas = {
        'intents': (
            """CREATE TABLE IF NOT EXISTS intents (
                intent_id INT AUTO_INCREMENT PRIMARY KEY,
                intent_name VARCHAR(100) NOT NULL UNIQUE,
                description VARCHAR(255) DEFAULT NULL
            ) CHARACTER SET utf8mb4;"""
        ),
        'patterns': (
            """CREATE TABLE IF NOT EXISTS patterns (
                pattern_id INT AUTO_INCREMENT PRIMARY KEY,
                intent_id INT NOT NULL,
                pattern_text VARCHAR(255) NOT NULL,
                FOREIGN KEY (intent_id) REFERENCES intents(intent_id)
                    ON DELETE CASCADE ON UPDATE CASCADE
            ) CHARACTER SET utf8mb4;"""
        ),
        'responses': (
            """CREATE TABLE IF NOT EXISTS responses (
                response_id INT AUTO_INCREMENT PRIMARY KEY,
                intent_id INT NOT NULL,
                response_text VARCHAR(255) NOT NULL,
                FOREIGN KEY (intent_id) REFERENCES intents(intent_id)
                    ON DELETE CASCADE ON UPDATE CASCADE
            ) CHARACTER SET utf8mb4;"""
        ),
        'conversations': (
            """CREATE TABLE IF NOT EXISTS conversations (
                conversation_id INT AUTO_INCREMENT PRIMARY KEY,
                user_input TEXT NOT NULL,
                agent_response TEXT NOT NULL,
                intent_detected VARCHAR(100) NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            ) CHARACTER SET utf8mb4;"""
        ),
        'entities': (
            """CREATE TABLE IF NOT EXISTS entities (
                entity_id INT AUTO_INCREMENT PRIMARY KEY,
                entity_name VARCHAR(100) NOT NULL,
                entity_value VARCHAR(255) NOT NULL,
                intent_id INT DEFAULT NULL,
                FOREIGN KEY (intent_id) REFERENCES intents(intent_id)
                    ON DELETE SET NULL ON UPDATE CASCADE
            ) CHARACTER SET utf8mb4;"""
        ),
    }
    try:
        cnx = mysql.connector.connect(**DB_CONFIG)
        cursor = cnx.cursor()
        for name, ddl in tablas.items():
            cursor.execute(ddl)
            print(f"Tabla '{name}' verificada/creada.")
        cursor.close()
        cnx.close()
        print("Inicialización de base de datos completada.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def entrenamiento():
    """Simula la recuperación de patrones y respuestas, y el entrenamiento del modelo."""
    cnx = mysql.connector.connect(**DB_CONFIG)
    cursor = cnx.cursor(dictionary=True)
    cursor.execute("SELECT * FROM patterns")
    patterns = cursor.fetchall()
    cursor.execute("SELECT * FROM responses")
    responses = cursor.fetchall()
    print(f"Patrones recuperados: {len(patterns)}")
    print(f"Respuestas recuperadas: {len(responses)}")
    # Aquí iría el entrenamiento real del modelo (deep learning)
    print("[Simulación] Modelo entrenado y tokenizer guardado.")
    cursor.close()
    cnx.close()

def registrar_conversacion(user_input, agent_response, intent_detected):
    """Registra una interacción en la tabla conversations."""
    cnx = mysql.connector.connect(**DB_CONFIG)
    cursor = cnx.cursor()
    cursor.execute(
        """INSERT INTO conversations (user_input, agent_response, intent_detected) VALUES (%s, %s, %s)""",
        (user_input, agent_response, intent_detected)
    )
    cnx.commit()
    cursor.close()
    cnx.close()
    print("Conversación registrada.")

def ampliar_intencion(intent_name, description=None):
    """Permite añadir una nueva intención y actualizar el modelo."""
    cnx = mysql.connector.connect(**DB_CONFIG)
    cursor = cnx.cursor()
    cursor.execute(
        """INSERT INTO intents (intent_name, description) VALUES (%s, %s)""",
        (intent_name, description)
    )
    cnx.commit()
    print(f"Intención '{intent_name}' añadida.")
    # Aquí se podría reentrenar el modelo automáticamente
    print("[Simulación] Modelo actualizado.")
    cursor.close()
    cnx.close()

if __name__ == "__main__":
    print("1. Inicializando base de datos...")
    inicializar_bd()
    print("2. Entrenando modelo...")
    entrenamiento()
    print("3. Registrando ejemplo de conversación...")
    registrar_conversacion("Hola", "¡Hola! ¿En qué puedo ayudarte?", "saludo")
    print("4. Añadiendo nueva intención...")
    ampliar_intencion("agradecimiento", "Responde a agradecimientos del usuario")

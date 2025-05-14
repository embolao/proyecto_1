SET NAMES 'utf8mb4';
SET CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS intenciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    frase VARCHAR(255) NOT NULL,
    etiqueta VARCHAR(64) NOT NULL,
    respuesta TEXT
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

INSERT INTO intenciones (frase, etiqueta, respuesta) VALUES
  -- responder_pregunta
  ('¿Qué sabes de Python?', 'responder_pregunta', 'No lo sé'),
  ('¿Qué puedes hacer?', 'responder_pregunta', 'Podría investigarlo'),
  ('¿Eres inteligente?', 'responder_pregunta', 'Esa es una buena pregunta'),
  ('¿Puedes ayudarme?', 'responder_pregunta', 'No lo sé'),
  ('¿Cuál es tu función?', 'responder_pregunta', 'Podría investigarlo'),

  -- indefinido
  ('no entiendo', 'indefinido', 'No entiendo lo que me dices'),
  ('...', 'indefinido', 'No entiendo lo que me dices'),
  ('?', 'indefinido', 'No entiendo lo que me dices'),
  ('¿qué?', 'indefinido', 'No entiendo lo que me dices'),
  ('no sé', 'indefinido', 'No entiendo lo que me dices'),
  ('no comprendo', 'indefinido', 'No entiendo lo que me dices'),
  ('???', 'indefinido', 'No entiendo lo que me dices'),

  -- nombre_agente
  ('¿cómo te llamas?', 'nombre_agente', 'Mi nombre es AsistentePY'),
  ('tu nombre', 'nombre_agente', 'Mi nombre es AsistentePY'),

  -- mostrar_edad
  ('cuántos años tienes', 'mostrar_edad', 'Tengo aproximadamente 1.0 años'),
  ('edad', 'mostrar_edad', 'Tengo aproximadamente 1.0 años'),

  -- memoria_completa
  ('recuerdas algo', 'memoria_completa', 'Recuerdo 3 interacciones'),
  ('memoria', 'memoria_completa', 'Recuerdo 3 interacciones'),

  -- agradecimiento
  ('gracias', 'agradecimiento', 'De nada, estoy aquí para ayudar'),
  ('muchas gracias', 'agradecimiento', 'De nada, estoy aquí para ayudar'),

  -- nombre_usuario
  ('cómo me llamo', 'nombre_usuario', 'No recuerdo tu nombre aún.'),
  ('mi nombre', 'nombre_usuario', 'No recuerdo tu nombre aún.'),

  -- borrar_memoria
  ('borrar recuerdos', 'borrar_memoria', 'Memoria borrada.'),
  ('borrar memoria', 'borrar_memoria', 'Memoria borrada.'),

  -- respuesta_empatica
  ('estoy triste', 'respuesta_empatica', 'Ánimo, todo mejora.'),
  ('me siento mal', 'respuesta_empatica', 'Ánimo, todo mejora.'),

  -- saludo
  ('hola', 'saludo', '¡Buenos días! ¿Cómo estás?'),
  ('hola', 'saludo', '¡Buenas! ¿En qué puedo ayudarte?'),
  ('buenos días', 'saludo', '¡Buenos días! ¿Cómo estás?'),
  ('holi', 'saludo', '¡Buenos días! ¿Cómo estás?'),
  ('HOLA AGENTE', 'saludo', '¡Buenas! ¿En qué puedo ayudarte?'),
  ('buenas', 'saludo', '¡Buenas! ¿En qué puedo ayudarte?'),
  ('buenas tardes', 'saludo', '¡Buenas tardes! ¿Cómo estás?'),
  ('buenos días, ¿cómo estás?', 'saludo', '¡Buenos días! ¿Cómo estás?'),

  -- despedir
  ('adiós', 'despedir', 'Hasta pronto'),
  ('hasta luego', 'despedir', 'Hasta luego'),
  ('nos vemos', 'despedir', 'Nos vemos'),
  ('chau', 'despedir', 'Chau'),
  ('qué hora es', 'mostrar_hora', 'Son las 12:00'),
  ('bye', 'despedir', 'Hasta pronto');

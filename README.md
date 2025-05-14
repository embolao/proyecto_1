# Agente Conversacional: Clasificador de Intenciones

Este proyecto implementa un agente conversacional en Python capaz de clasificar intenciones de usuario y responder de forma adecuada. Utiliza un modelo de red neuronal entrenado sobre un dataset variado y embeddings semánticos en español.

## Estructura del proyecto

- `src/agente/intent_classifier.py`: Clase principal para entrenamiento, predicción y gestión del modelo de intenciones.
- `src/agente/a_memoria_avanzado.py`: Lógica del agente conversacional y procesamiento de entradas/salidas.
- `tests/test_intent_agent.py`: Pruebas automáticas del agente.

## Esquema de Base de Datos (2025)

El sistema ahora utiliza un esquema relacional moderno y flexible:

- **intents**: almacena las intenciones reconocidas por el agente.
    - intent_id (PK), intent_name, description
- **patterns**: ejemplos de frases para cada intención.
    - pattern_id (PK), intent_id (FK), pattern_text
- **responses**: posibles respuestas para cada intención.
    - response_id (PK), intent_id (FK), response_text
- **entities**: información adicional relevante (ej: ciudad, nombre_usuario).
    - entity_id (PK), entity_name, entity_value, intent_id (FK, opcional)
- **conversations**: historial de interacciones.
    - conversation_id (PK), user_input, agent_response, intent_detected, timestamp

## Flujo de Trabajo Actualizado

### 1. Inicialización
- Crea y verifica todas las tablas del nuevo esquema automáticamente.
- Soporte completo para caracteres especiales (`utf8mb4`).

### 2. Entrenamiento
- Recupera patrones y respuestas desde las tablas `patterns` y `responses`.
- Entrena el modelo de deep learning para clasificación de intenciones.
- Guarda pesos y tokenizer listos para producción.

### 3. Operación
- Clasifica la intención del usuario usando el modelo entrenado y los datos de la base.
- Busca respuestas adecuadas en la tabla `responses` según la intención detectada.
- Registra cada interacción en la tabla `conversations` para trazabilidad y mejora futura.

### 4. Ampliación
- Permite añadir nuevas intenciones, patrones, respuestas y entidades directamente en la base de datos, sin tocar el código.
- El modelo puede reentrenarse automáticamente cuando se detectan nuevas intenciones o patrones.

## Integración y Tests Automáticos

- El agente y el flujo de deep learning funcionan 100% con el nuevo esquema.
- Incluye scripts para poblar datos de ejemplo y visualizar cualquier tabla (`ver_tabla_colores.py`).
- Incluye tests automáticos (`tests/test_integracion_nuevo_esquema.py`) que validan la integración y operación real del sistema.

## Comandos útiles

- Poblar datos de ejemplo:
  ```bash
  python3 populate_new_schema.py
  ```
- Visualizar tablas con colores:
  ```bash
  python3 ver_tabla_colores.py
  ```
- Ejecutar tests automáticos:
  ```bash
  pytest tests/test_integracion_nuevo_esquema.py -v
  ```
## Pipeline de Clasificación de Intenciones

1. **Dataset**: Frases variadas para cada intención, generadas automáticamente con variantes sintéticas.
2. **Embeddings**: Se usan vectores semánticos de spaCy (`es_core_news_md`) para representar cada frase.
3. **Modelo**: Red neuronal densa (Keras) con varias capas y regularización.
4. **Entrenamiento**: El modelo se entrena automáticamente si no existe uno guardado.
5. **Predicción**: Cada frase se transforma en vector y la red predice la intención con su probabilidad.
6. **Respuestas**: El agente responde según la intención detectada.

## Requisitos

- Python 3.8+
- TensorFlow
- scikit-learn
- spaCy
- Modelo spaCy español:
  ```sh
  pip install spacy
  python -m spacy download es_core_news_md
  ```

## Ejecución y pruebas

1. Instala dependencias (usa tu entorno virtual):
   ```sh
   pip install -r requirements.txt
   python -m spacy download es_core_news_md
   ```
2. Ejecuta los tests automáticos:
   ```sh
   python3 tests/test_intent_agent.py
   ```
3. Puedes modificar el dataset en `intent_classifier.py` para añadir nuevas intenciones.

## Añadir nuevas intenciones

- Añade frases y etiqueta en el método `_generate_large_dataset()`.
- Añade la nueva intención y su respuesta en el `intent_map` de `a_memoria_avanzado.py`.
- Vuelve a ejecutar el test para reentrenar el modelo.

## Notas
- El modelo se reentrena automáticamente si modificas el dataset o borras los archivos del modelo.
- Puedes ver la intención y probabilidad predicha en consola para depuración.

6. **Respuestas**: El agente responde según la intención detectada.

## Requisitos

- Python 3.8+
- TensorFlow
- scikit-learn
- spaCy
- Modelo spaCy español:
  ```sh
  pip install spacy
  python -m spacy download es_core_news_md
  ```

## Ejecución y pruebas

1. Instala dependencias (usa tu entorno virtual):
   ```sh
   pip install -r requirements.txt
   python -m spacy download es_core_news_md
   ```
2. Ejecuta los tests automáticos:
   ```sh
   python3 tests/test_intent_agent.py
   ```
3. Puedes modificar el dataset en `intent_classifier.py` para añadir nuevas intenciones.

## Añadir nuevas intenciones

- Añade frases y etiqueta en el método `_generate_large_dataset()`.
- Añade la nueva intención y su respuesta en el `intent_map` de `a_memoria_avanzado.py`.
- Vuelve a ejecutar el test para reentrenar el modelo.

## Notas
- El modelo se reentrena automáticamente si modificas el dataset o borras los archivos del modelo.
- Puedes ver la intención y probabilidad predicha en consola para depuración.

---

Desarrollado por Embolao.

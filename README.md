# Agente Conversacional: Clasificador de Intenciones

Este proyecto implementa un agente conversacional en Python capaz de clasificar intenciones de usuario y responder de forma adecuada. Utiliza un modelo de red neuronal entrenado sobre un dataset variado y embeddings semánticos en español.

## Estructura del proyecto

- `src/agente/intent_classifier.py`: Clase principal para entrenamiento, predicción y gestión del modelo de intenciones.
- `src/agente/a_memoria_avanzado.py`: Lógica del agente conversacional y procesamiento de entradas/salidas.
- `tests/test_intent_agent.py`: Pruebas automáticas del agente.

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

---

Desarrollado por [Tu Nombre].
│   ├── __pycache__/
│   ├── agente/
│   │   ├── __init__.py
│   │   ├── __pycache__/
│   │   ├── a_memoria_avanzado.py      # Lógica principal del agente
│   │   ├── agente1.py
│   │   ├── agente_memoria.py
│   │   ├── intent_classifier.py       # Clasificador de intenciones
│   │   ├── intent_model.h5            # Modelo entrenado (Keras)
│   │   ├── intent_model.h5.encoder.pkl # Encoder de clases (pickle)
│   │   ├── intent_model.h5.tokenizer.pkl # (legacy, no se usa con spaCy)
│   ├── nombre_proyecto.egg-info/
├── tests/
│   ├── __pycache__/
│   ├── test_a_memoria_avanzado.py
│   ├── test_agent1_1.py
│   ├── test_agente1.py
│   ├── test_agente_memoria.py
│   ├── test_basico.py
│   ├── test_intent_agent.py           # Test principal del agente
├── tox.ini
├── ver_modelo.py                     # Script para visualizar modelo y encoder
```
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

Desarrollado por [Tu Nombre].

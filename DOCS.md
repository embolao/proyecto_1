# Documentación de Clases y Funciones

## IntentClassifier (`src/agente/intent_classifier.py`)

Clase encargada de entrenar, guardar, cargar y predecir intenciones a partir de texto usando embeddings spaCy y una red neuronal.

### Métodos principales

- **`__init__(self, model_path='intent_model.h5', embed_path='intent_embeds.pkl')`**  
  Inicializa el clasificador. Si existen archivos de modelo y encoder, los carga; si no, entrena desde cero.

- **`_init_or_load(self)`**  
  Carga el modelo y encoder si existen, o entrena un nuevo modelo con el dataset ampliado.

- **`_generate_large_dataset(self)`**  
  Genera automáticamente un dataset grande y variado de frases y etiquetas para cada intención.

- **`train(self, texts, labels)`**  
  Entrena la red neuronal a partir de los textos y etiquetas proporcionados. Usa embeddings spaCy para vectorizar.

- **`_load(self)`**  
  Carga el modelo, embeddings y encoder desde disco.

- **`predict_intent(self, text)`**  
  Predice la intención de una frase de entrada.  
  - Entrada: texto (str)  
  - Salida: intención (str)  
  - Muestra en consola la intención y la probabilidad para depuración.

---

## ProcesadorEntrada (`src/agente/a_memoria_avanzado.py`)

Clase que recibe el texto del usuario, predice la intención usando `IntentClassifier` y ejecuta la respuesta correspondiente.

### Métodos principales

- **`__init__(self)`**  
  Inicializa el clasificador y el mapa de intenciones a funciones de respuesta.

- **`procesar(self, entrada)`**  
  Procesa la entrada del usuario, predice la intención y ejecuta la función asociada.

- **Métodos de respuesta**  
  Cada intención tiene un método específico (por ejemplo, `respuesta_saludo`, `respuesta_agradecimiento`, etc.), que genera la respuesta del agente.

---

Para dudas sobre otras funciones, clases o ampliaciones, consulta el código fuente o pregunta directamente.

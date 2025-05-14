import os
import pickle

from tensorflow.keras.models import load_model

MODEL_PATH = os.path.join("src", "agente", "intent_model.h5")
EMBED_PATH = os.path.join("src", "agente", "intent_embeds.pkl")
ENCODER_PATH = os.path.join("src", "agente", "intent_model.h5.encoder.pkl")

print("--- Arquitectura del modelo Keras (.h5) ---")
if os.path.exists(MODEL_PATH):
    model = load_model(MODEL_PATH)
    model.summary()
    print("\n--- Pesos de cada capa ---")
    for i, layer in enumerate(model.layers):
        print(f"Layer {i} ({layer.name}):")
        for w in layer.get_weights():
            print(w.shape)
else:
    print("No se encontró el archivo", MODEL_PATH)

print("\n--- Encoder (clases de intenciones) ---")
if os.path.exists(ENCODER_PATH):
    with open(ENCODER_PATH, "rb") as f:
        encoder = pickle.load(f)
    print("Clases:", getattr(encoder, "classes_", encoder))
else:
    print("No se encontró el archivo", ENCODER_PATH)

print("\n--- Embeddings (primeras filas) ---")
if os.path.exists(EMBED_PATH):
    with open(EMBED_PATH, "rb") as f:
        embeds = pickle.load(f)
    print("Shape:", getattr(embeds, "shape", None))
    print(
        "Primeras 2 filas:",
        embeds[:2] if hasattr(embeds, "__getitem__") else embeds,
    )
else:
    print("No se encontró el archivo", EMBED_PATH)

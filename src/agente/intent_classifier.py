import os
import pickle
import random

import numpy as np
import spacy
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.layers import BatchNormalization, Dense, Dropout
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.utils import to_categorical


class IntentClassifier:
    def __init__(self, model_path="intent_model.h5", embed_path="intent_embeds.pkl"):
        self.model_path = model_path
        self.embed_path = embed_path
        self.encoder_path = model_path + ".encoder.pkl"
        self.model = None
        self.encoder = LabelEncoder()
        self.intents = []
        # usa spaCy español preentrenado
        self.nlp = spacy.load("es_core_news_md")
        self.embeddings = None
        self._init_or_load()

    def _init_or_load(self):
        if (
            os.path.exists(self.model_path)
            and os.path.exists(self.embed_path)
            and os.path.exists(self.encoder_path)
        ):
            self._load()
        else:
            frases, etiquetas = self._generate_large_dataset()
            self.train(frases, etiquetas)

    def _generate_large_dataset(self):
        # Dataset base
        base = {
            "saludo": [
                "hola",
                "buenos días",
                "buenas tardes",
                "buenas noches",
                "qué tal",
                "hey",
                "saludos",
                "cómo estás",
                "qué onda",
                "qué pasa",
                "qué hay",
                "hola amigo",
                "hola asistente",
                "buen día",
                "buenas",
            ],
            "guardar_nombre": [
                "me llamo Juan",
                "mi nombre es Ana",
                "puedes llamarme Pedro",
                "soy Laura",
                "me dicen Carlos",
                "me llamo Sofía",
                "mi nombre es Luis",
                "me llaman Paco",
                "soy Marta",
                "me llaman Pepe",
                "dime Carlos",
                "me dicen Pepe",
                "puedes llamarme Lola",
                "llámame Sergio",
                "me llamo Andrea",
            ],
            "nombre_agente": [
                "cómo te llamas",
                "quién eres",
                "cuál es tu nombre",
                "dime tu nombre",
                "cómo te puedo llamar",
                "cómo te conocen",
                "cómo te llamas tú",
                "dime cómo te llamas",
                "quién es el asistente",
                "cuál es tu apodo",
            ],
            "nombre_usuario": [
                "cómo me llamo",
                "cuál es mi nombre",
                "sabes mi nombre",
                "recuerdas mi nombre",
                "quién soy",
                "me recuerdas",
                "puedes decir mi nombre",
                "te acuerdas de mi nombre",
                "quién era yo",
                "cómo me llamaba",
            ],
            "borrar_memoria": [
                "borra mis recuerdos",
                "olvida todo",
                "borra la memoria",
                "elimina mis datos",
                "quiero empezar de cero",
                "reinicia la memoria",
                "elimina toda la información",
                "borra todo",
                "olvida mis datos",
                "resetea la memoria",
            ],
            "memoria_completa": [
                "muéstrame todos mis recuerdos",
                "qué recuerdas",
                "enséñame la memoria completa",
                "lista de recuerdos",
                "qué cosas sabes de mí",
                "historial completo",
                "qué sabes de mí",
                "muéstrame la lista de recuerdos",
                "enséñame todos los recuerdos",
                "qué tienes en la memoria",
            ],
            "mostrar_edad": [
                "cuántos años tienes",
                "qué edad tienes",
                "eres viejo",
                "desde cuándo existes",
                "cuánto tiempo llevas aquí",
                "cuál es tu edad",
                "qué edad tienes tú",
                "eres joven",
                "cuándo naciste",
                "hace cuánto existes",
            ],
            "mostrar_hora": [
                "qué hora es",
                "dime la hora",
                "me puedes decir la hora",
                "hora actual",
                "tienes la hora",
                "qué hora tienes",
                "puedes decirme la hora",
                "qué hora marca",
                "hora por favor",
                "hora exacta",
            ],
            "respuesta_empatica": [
                "estoy triste",
                "me siento mal",
                "no estoy bien",
                "estoy deprimido",
                "me siento solo",
                "ando bajoneado",
                "hoy no estoy bien",
                "estoy decaído",
                "me siento fatal",
                "ando triste",
            ],
            "agradecimiento": [
                "gracias",
                "te lo agradezco",
                "muy amable",
                "eres genial",
                "mil gracias",
                "muchas gracias",
                "gracias por tu ayuda",
                "te agradezco",
                "gracias asistente",
                "muchísimas gracias",
            ],
        }
        # Aumentar dataset con variantes sintéticas
        frases, etiquetas = [], []
        for intent, examples in base.items():
            for frase in examples:
                frases.append(frase)
                etiquetas.append(intent)
                # Variante: mayúsculas, minúsculas,
                # con signos, con palabras extra
                frases.append(frase.upper())
                etiquetas.append(intent)
                frases.append(frase.capitalize() + "!")
                etiquetas.append(intent)
                frases.append("por favor, " + frase)
                etiquetas.append(intent)
                frases.append(frase + " por favor")
                etiquetas.append(intent)
                # Variante con ruido
                if " " in frase:
                    frases.append(frase.replace(" ", "  "))
                    etiquetas.append(intent)
        # Mezclar
        combined = list(zip(frases, etiquetas))
        random.shuffle(combined)
        frases, etiquetas = zip(*combined)
        return list(frases), list(etiquetas)

    def train(self, texts, labels):
        self.intents = sorted(list(set(labels)))
        X = np.array([self.nlp(text).vector for text in texts])
        y = self.encoder.fit_transform(labels)
        y = to_categorical(y)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.1, random_state=42
        )
        self.model = Sequential(
            [
                Dense(128, activation="relu", input_shape=(X.shape[1],)),
                BatchNormalization(),
                Dropout(0.4),
                Dense(64, activation="relu"),
                Dropout(0.3),
                Dense(len(self.intents), activation="softmax"),
            ]
        )
        self.model.compile(
            loss="categorical_crossentropy",
            optimizer="adam",
            metrics=["accuracy"],
        )
        self.model.fit(
            X_train,
            y_train,
            epochs=50,
            batch_size=16,
            validation_data=(X_test, y_test),
            verbose=1,
        )
        self.model.save(self.model_path)
        # Guardar embeddings y encoder
        with open(self.embed_path, "wb") as f:
            pickle.dump(X, f)
        with open(self.encoder_path, "wb") as f:
            pickle.dump(self.encoder, f)

    def _load(self):
        self.model = load_model(self.model_path)
        with open(self.embed_path, "rb") as f:
            self.embeddings = pickle.load(f)
        with open(self.encoder_path, "rb") as f:
            self.encoder = pickle.load(f)

    def predict_intent(self, text):
        vec = self.nlp(text).vector.reshape(1, -1)
        pred = self.model.predict(vec, verbose=0)
        intent_idx = np.argmax(pred)
        prob = float(np.max(pred))
        if hasattr(self.encoder, "classes_"):
            intent = self.encoder.classes_[intent_idx]
        else:
            intent = self.intents[intent_idx] if self.intents else None
        print(
            f"[DEBUG] Texto: '{text}' | Intención: '{intent}' "
            f"| Probabilidad: {prob:.2f}"
        )
        return intent

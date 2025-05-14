import subprocess

TEST_INPUTS = [
    "hola",
    "me llamo Laura",
    "cómo te llamas",
    "qué hora es",
    "muéstrame todos mis recuerdos",
    "estoy triste",
    "gracias",
    "borra la memoria",
    "cuántos años tienes",
    "salir",
]


def test_agent():
    proc = subprocess.Popen(
        ["python3", "src/agente/a_memoria_avanzado.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    input_text = "\n".join(TEST_INPUTS) + "\n"
    out, err = proc.communicate(input=input_text, timeout=60)
    print("--- OUTPUT ---")
    print(out)
    print("--- ERRORS ---")
    print(err)
    assert "Agente: Hola, soy AsistentePY" in out
    assert "Hasta pronto" in out


if __name__ == "__main__":
    test_agent()

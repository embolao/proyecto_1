import os
import sys

from agente import hola

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def test_hola():
    assert hola() == "Hola desde nombre_proyecto"

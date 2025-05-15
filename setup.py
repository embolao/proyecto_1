from setuptools import setup, find_packages
import os

def get_version():
    # Leer la versión del archivo __init__.py
    init_path = os.path.join(os.path.dirname(__file__), 'src', 'agente', '__init__.py')
    with open(init_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('__version__'):
                return line.split('=')[1].strip().strip('\'"')
    return '0.0.0'

setup(
    name="agente",
    version=get_version(),
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy",
        "scikit-learn",
        "tensorflow",
        "spacy",
        "mysql-connector-python",
    ],
    python_requires=">=3.8",
)

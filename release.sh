#!/bin/bash

# Verificar que se proporcione un mensaje de commit
if [ $# -eq 0 ]; then
    echo "Uso: $0 'mensaje del commit'"
    exit 1
fi

# Obtener la versión actual
CURRENT_VERSION=$(python3 -c "from src.agente import __version__; print(__version__)")
echo "Versión actual: $CURRENT_VERSION"

# Preguntar por el tipo de bump (major, minor, patch)
echo "Selecciona el tipo de versión:"
echo "1) Major (X.0.0)"
echo "2) Minor (0.X.0)"
echo "3) Patch (0.0.X)"
read -p "Opción [1-3]: " VERSION_BUMP

# Actualizar la versión según la selección
IFS='.' read -r -a VERSION_PARTS <<< "$CURRENT_VERSION"
MAJOR=${VERSION_PARTS[0]}
MINOR=${VERSION_PARTS[1]}
PATCH=${VERSION_PARTS[2]}

case $VERSION_BUMP in
    1)
        MAJOR=$((MAJOR + 1))
        MINOR=0
        PATCH=0
        ;;
    2)
        MINOR=$((MINOR + 1))
        PATCH=0
        ;;
    3)
        PATCH=$((PATCH + 1))
        ;;
    *)
        echo "Opción no válida. Usando versión actual."
        ;;
esac

NEW_VERSION="$MAJOR.$MINOR.$PATCH"

echo "Nueva versión: $NEW_VERSION"

# Actualizar la versión en __init__.py
sed -i "s/__version__ = \".*\"/__version__ = \"$NEW_VERSION\"/" src/agente/__init__.py

# Actualizar el CHANGELOG.md
TODAY=$(date +%Y-%m-%d)
sed -i "s/## \[Unreleased\]/## \[Unreleased\]\n\n## \[$NEW_VERSION\] - $TODAY/" CHANGELOG.md

# Hacer commit de los cambios
git add .
git commit -m "$1"

# Crear un tag para la versión
git tag -a "v$NEW_VERSION" -m "Versión $NEW_VERSION"

echo "¡Listo! Versión $NEW_VERSION creada y etiquetada."
echo "No olvides ejecutar 'git push --follow-tags' para subir los cambios y las etiquetas."

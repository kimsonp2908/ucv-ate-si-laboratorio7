# p_ Laboratorio Ucv Kedro Poetry Gha Sonar

Este proyecto es un laboratorio de la UCV que utiliza **Kedro**, **Poetry**, **GitHub Actions** y **SonarCloud** para el procesamiento de imágenes.

## Descripción
El proyecto incluyó una tubería de procesamiento que tomó una imagen original, la rotó, aplicó un filtro de relieve y agregó un texto identificador.

## Requisitos
- Python 3.11+
- Poetry

## Instalación de Dependencias
Se utilizó Poetry para gestionar las librerías necesarias. Para instalar, ejecutó:
```bash
poetry install
```

## Ejecución del Proyecto
Para ejecutar la tubería de procesamiento de imágenes, utilizó:
```bash
poetry run kedro run --pipeline data_processing
```

## Estructura del Proyecto
- `src/lab7/pipelines/data_processing`: Contuvo la lógica del procesamiento de imágenes.
- `conf/base/catalog.yml`: Definió las entradas y salidas de datos (imágenes).
- `.github/workflows/ci.yml`: Configuró la integración continua con GitHub Actions.
- `sonar-project.properties`: Configuró el análisis de calidad con SonarCloud.

## Calidad de Código y CI/CD
- **GitHub Actions**: Ejecutó automáticamente linting (Ruff), pruebas (Pytest) y análisis de Sonar en cada push.
- **SonarCloud**: Realizó el seguimiento de la calidad y cobertura del código.

## Notas sobre la Imagen
La imagen original se encuentra en `data/01_raw/imagen.jpg`. El resultado procesado se guardó en `data/02_intermediate/imagen_procesada.jpg`.

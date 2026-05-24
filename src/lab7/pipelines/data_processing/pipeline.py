from kedro.pipeline import Pipeline, node
from .nodes import process_image

def create_pipeline(**kwargs):
    """
    Creó la tubería de procesamiento de datos para el manejo de imágenes.
    """
    return Pipeline(
        [
            node(
                func=process_image,
                inputs="imagen_original",
                outputs="imagen_procesada",
                name="process_image_node",
            )
        ]
    )

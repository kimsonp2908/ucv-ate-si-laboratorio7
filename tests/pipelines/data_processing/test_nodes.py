import pytest
from PIL import Image
from lab7.pipelines.data_processing.nodes import process_image

def test_process_image():
    """
    Verificó que la función process_image procese una imagen correctamente.
    """
    # Creó una imagen de prueba pequeña (100x100) en blanco
    test_image = Image.new("RGB", (100, 100), color="white")
    
    # Ejecutó la función de procesamiento
    processed = process_image(test_image)
    
    # Verificó que el resultado sea una instancia de Image.Image
    assert isinstance(processed, Image.Image)
    
    # Verificó que las dimensiones se mantengan o cambien según lo esperado (la rotación 45 puede cambiar el tamaño si no se recorta)
    # PIL.rotate(45) por defecto mantiene el tamaño original pero rota el contenido
    assert processed.size == (100, 100)

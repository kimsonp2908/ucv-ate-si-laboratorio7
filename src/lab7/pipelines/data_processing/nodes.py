from PIL import Image, ImageFilter, ImageDraw

def process_image(image: Image.Image) -> Image.Image:
    """
    Procesó una imagen aplicando rotación, filtros y texto.
    """
    # Rotó la imagen 45 grados
    rotated = image.rotate(45)

    # Aplicó un filtro de relieve (emboss)
    filtered = rotated.filter(ImageFilter.EMBOSS)

    # Preparó el lienzo para dibujar sobre la imagen
    draw = ImageDraw.Draw(filtered)

    # Agregó un texto identificador en la parte superior izquierda
    draw.text((20, 20), "UCV - Sistemas Inteligentes", fill="white")

    return filtered

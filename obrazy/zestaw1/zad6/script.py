from PIL import Image
import numpy as np

# Wczytanie obrazu
image_path = "zestaw1/zad6/potworek.png"
image = Image.open(image_path)

# Oryginalne wymiary obrazu
original_width, original_height = image.size

# Nowe wymiary
new_width = 600
new_height = 360

def nearest_neighbor(image, new_width, new_height):
    return image.resize((new_width, new_height), Image.NEAREST)

# Skalowanie obrazu
scaled_image_nn = nearest_neighbor(image, new_width, new_height)
scaled_image_nn.save("zestaw1/zad6/potworek_a.png")
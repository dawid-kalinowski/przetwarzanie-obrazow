from PIL import Image
import numpy as np

# Wczytanie obrazu
image_path = "zestaw1/zad6/potworek.png"  # Ścieżka do obrazu
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
scaled_image_nn.save("zestaw1/zad6/potworek_nn.png")

def extended_nearest_neighbor(image, new_width, new_height):
    # Przekształcamy obraz na tablicę NumPy
    image_array = np.array(image)
    scaled_image_array = np.zeros((new_height, new_width, 3), dtype=np.uint8)
    
    # Współczynniki skalowania
    scale_x = original_width / new_width
    scale_y = original_height / new_height
    
    for i in range(new_height):
        for j in range(new_width):
            # Obliczamy współrzędne w oryginalnym obrazie
            x1 = int(j * scale_x)
            y1 = int(i * scale_y)
            
            # Losujemy dwóch najbliższych sąsiadów
            x2 = min(x1 + 1, original_width - 1)
            y2 = min(y1 + 1, original_height - 1)
            
            # Pobieramy kolory z tych punktów
            color1 = image_array[y1, x1]
            color2 = image_array[y2, x2]
            
            # Obliczamy średnią
            avg_color = np.mean([color1, color2], axis=0)
            scaled_image_array[i, j] = avg_color

    # Przekształcamy z powrotem na obraz
    return Image.fromarray(scaled_image_array)

# Skalowanie obrazu
scaled_image_en = extended_nearest_neighbor(image, new_width, new_height)
scaled_image_en.save("zestaw1/zad6/potworek_en.png")

def bilinear_interpolation(image, new_width, new_height):
    image_array = np.array(image)
    scaled_image_array = np.zeros((new_height, new_width, 3), dtype=np.uint8)
    
    scale_x = original_width / new_width
    scale_y = original_height / new_height
    
    for i in range(new_height):
        for j in range(new_width):
            # Obliczamy współrzędne w oryginalnym obrazie
            x = j * scale_x
            y = i * scale_y
            x1, y1 = int(x), int(y)
            x2, y2 = min(x1 + 1, original_width - 1), min(y1 + 1, original_height - 1)
            
            # Interpolacja dwuliniowa
            A = image_array[y1, x1]
            B = image_array[y1, x2]
            C = image_array[y2, x1]
            D = image_array[y2, x2]
            
            # Wagi dla interpolacji
            dx = x - x1
            dy = y - y1
            color = (1 - dx) * (1 - dy) * A + dx * (1 - dy) * B + (1 - dx) * dy * C + dx * dy * D
            scaled_image_array[i, j] = np.clip(color, 0, 255)
    
    return Image.fromarray(scaled_image_array)

# Skalowanie obrazu
scaled_image_bi = bilinear_interpolation(image, new_width, new_height)
scaled_image_bi.save("zestaw1/zad6/potworek_bi.png")


def max_min_interpolation(image, new_width, new_height):
    image_array = np.array(image)
    scaled_image_array = np.zeros((new_height, new_width, 3), dtype=np.uint8)
    
    scale_x = original_width / new_width
    scale_y = original_height / new_height
    
    for i in range(new_height):
        for j in range(new_width):
            # Obliczamy współrzędne w oryginalnym obrazie
            x = j * scale_x
            y = i * scale_y
            x1, y1 = int(x), int(y)
            x2, y2 = min(x1 + 1, original_width - 1), min(y1 + 1, original_height - 1)
            
            # Zbieramy cztery sąsiednie piksele
            neighbors = [image_array[y1, x1], image_array[y1, x2], image_array[y2, x1], image_array[y2, x2]]
            
            # Wartości jasności (średnia maksymalnej i minimalnej jasności)
            brightness_values = [np.mean(pixel) for pixel in neighbors]
            min_brightness = min(brightness_values)
            max_brightness = max(brightness_values)
            
            # Obliczamy średnią z maksymalnej i minimalnej jasności
            scaled_image_array[i, j] = np.mean([min_brightness, max_brightness])
    
    return Image.fromarray(scaled_image_array)

# Skalowanie obrazu
scaled_image_mm = max_min_interpolation(image, new_width, new_height)
scaled_image_mm.save("zestaw1/zad6/potworek_mm.png")

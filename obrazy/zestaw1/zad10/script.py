from PIL import Image
import numpy as np


image_path = 'stanczyk.png'
original_image = Image.open(image_path).convert('L')

dither_matrix = np.array([
    [6, 14, 2, 8],
    [4, 0, 10, 11],
    [12, 15, 5, 1],
    [9, 3, 13, 7]
])

def variable_threshold_dithering(image_array, dither_matrix, levels):

    height, width = image_array.shape
    dither_size = dither_matrix.shape[0]
    
    # Normalizacja macierzy ditheringu do zakresu [0, 1]
    normalized_dither = dither_matrix / (np.max(dither_matrix) + 1)  # +1, by uniknąć przekroczenia zakresu
    
    # Równomierne rozłożenie poziomów szarości
    level_values = np.linspace(0, 255, levels, endpoint=True)
    
    # Przygotowanie wynikowego obrazu
    result = np.zeros_like(image_array, dtype=np.uint8)

    for y in range(height):
        for x in range(width):
            # Jasność piksela
            pixel_value = image_array[y, x]
            
            # Indeks w macierzy ditheringu (modulo, by powtarzać dla całego obrazu)
            dither_x = x % dither_size
            dither_y = y % dither_size
            
            # Obliczenie lokalnego progu
            threshold = normalized_dither[dither_y, dither_x] * 255
            
            # Przydzielanie poziomu jasności na podstawie lokalnego progu
            if pixel_value > threshold:
                new_value = next((v for v in level_values if pixel_value <= v), level_values[-1])
            else:
                new_value = next((v for v in reversed(level_values) if pixel_value >= v), level_values[0])
            
            result[y, x] = new_value
    
    return result

# Parametry ditheringu
levels = 5  # Liczba poziomów szarości (np. 5 poziomów: 0, 64, 128, 192, 255)

# Konwersja obrazu na tablicę numpy
image_array = np.array(original_image)

# Wykonanie ditheringu
dithered_array = variable_threshold_dithering(image_array, dither_matrix, levels)

# Konwersja z powrotem na obraz
dithered_image = Image.fromarray(dithered_array)

# Zapisanie i wyświetlenie obrazu
output_path = 'output.png'
dithered_image.save(output_path)
dithered_image.show()

print(f"Dithered image saved to {output_path}")

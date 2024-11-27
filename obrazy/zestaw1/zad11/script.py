import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

bayer_matrix_8x8 = np.array([
    [0, 48, 12, 60, 3, 51, 15, 63],
    [32, 16, 44, 28, 35, 19, 47, 31],
    [8, 56, 4, 52, 11, 59, 7, 55],
    [40, 24, 36, 20, 43, 27, 39, 23],
    [2, 50, 14, 62, 1, 49, 13, 61],
    [34, 18, 46, 30, 33, 17, 45, 29],
    [10, 58, 6, 54, 9, 57, 5, 53],
    [42, 26, 38, 22, 41, 25, 37, 21]
]) / 64.0

def dithering(image, levels, bayer_matrix):

    h, w = image.shape
    bayer_h, bayer_w = bayer_matrix.shape
    
    # rozciągnięcie macierzy do rozmiaru obrazu
    threshold_matrix = np.tile(bayer_matrix, (h // bayer_h + 1, w // bayer_w + 1))[:h, :w]
    
    # normalizacja obrazu do zakresu 0 1
    norm_image = image / 255.0
    
    if len(levels) == 2:  # 1-bitowy (czarno-biały)
        dithered_image = (norm_image > threshold_matrix).astype(np.uint8) * 255
    else:  # Redukcja do określonych poziomów szarości
        level_thresholds = [(levels[i] + levels[i + 1]) / 2 for i in range(len(levels) - 1)]
        dithered_image = np.zeros_like(image)
        for i, level in enumerate(levels):
            if i == 0:
                dithered_image[norm_image <= level_thresholds[i] / 255.0] = level
            elif i == len(levels) - 1:
                dithered_image[norm_image > level_thresholds[i - 1] / 255.0] = level
            else:
                mask = (norm_image > level_thresholds[i - 1] / 255.0) & (norm_image <= level_thresholds[i] / 255.0)
                dithered_image[mask] = level

    return dithered_image

# Wczytanie obrazu w skali szarości
image = Image.open("stanczyk.png").convert("L")
image_np = np.array(image)

# Dithering dla czarno-białego obrazu (1-bitowy)
bw_dithered = dithering(image_np, [0, 255], bayer_matrix_8x8)

# Dithering dla 4 poziomów szarości
gray_levels = [50, 100, 150, 200]
multi_gray_dithered = dithering(image_np, gray_levels, bayer_matrix_8x8)

# Zapis obrazów do plików
Image.fromarray(bw_dithered).save("a.png")
Image.fromarray(multi_gray_dithered).save("b.png")


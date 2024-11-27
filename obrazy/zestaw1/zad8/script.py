from PIL import Image
import numpy as np

image_path = 'stanczyk.png'
original_image = Image.open(image_path).convert('L')  # konwersja na skalę szarości

# 5 poziomów
def floyd_steinberg_dithering_gray(image_array):
    height, width = image_array.shape
    error_diffusion = np.zeros_like(image_array, dtype=float)
    result = np.zeros_like(image_array)

    def assign_level(value):
        if 0 <= value <= 19:
            return 0
        elif 20 <= value <= 39:
            return 64
        elif 40 <= value <= 59:
            return 128
        elif 60 <= value <= 119:
            return 192
        elif 120 <= value <= 255:
            return 255
        return 0    

    for y in range(height):
        for x in range(width):
            old_pixel = image_array[y, x] + error_diffusion[y, x]
            new_pixel = assign_level(old_pixel)
            result[y, x] = new_pixel
            quant_error = old_pixel - new_pixel

            # rozproszanie błędu algorytmu
            if x + 1 < width:
                error_diffusion[y, x + 1] += quant_error * 7 / 16
            if y + 1 < height:
                if x > 0:
                    error_diffusion[y + 1, x - 1] += quant_error * 3 / 16
                error_diffusion[y + 1, x] += quant_error * 5 / 16
                if x + 1 < width:
                    error_diffusion[y + 1, x + 1] += quant_error * 1 / 16

    return result

# 1 poziom
def floyd_steinberg_dithering_bw(image_array, threshold):
    height, width = image_array.shape
    error_diffusion = np.zeros_like(image_array, dtype=float)
    result = np.zeros_like(image_array)

    for y in range(height):
        for x in range(width):
            old_pixel = image_array[y, x] + error_diffusion[y, x]
            new_pixel = 255 if old_pixel >= threshold else 0
            result[y, x] = new_pixel
            quant_error = old_pixel - new_pixel

            if x + 1 < width:
                error_diffusion[y, x + 1] += quant_error * 7 / 16
            if y + 1 < height:
                if x > 0:
                    error_diffusion[y + 1, x - 1] += quant_error * 3 / 16
                error_diffusion[y + 1, x] += quant_error * 5 / 16
                if x + 1 < width:
                    error_diffusion[y + 1, x + 1] += quant_error * 1 / 16

    return result

# zadanie a
threshold = 39
bw_image_array = np.array(original_image)
bw_dithered_array = floyd_steinberg_dithering_bw(bw_image_array, threshold)

bw_dithered_image = Image.fromarray(bw_dithered_array.astype(np.uint8))
bw_dithered_image_path = 'a.png'
bw_dithered_image.save(bw_dithered_image_path)

# zadanie b
gray_image_array = np.array(original_image)
gray_dithered_array = floyd_steinberg_dithering_gray(gray_image_array)

gray_dithered_image = Image.fromarray(gray_dithered_array.astype(np.uint8))
gray_dithered_image_path = 'b.png'
gray_dithered_image.save(gray_dithered_image_path)




bw_dithered_image.show()
gray_dithered_image.show()


bw_dithered_image_path, gray_dithered_image_path

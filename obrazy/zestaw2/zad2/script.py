from PIL import Image
import numpy as np

def local_contrast(image):
    """
    Oblicza globalny kontrast lokalny obrazu na podstawie ośmiospójnego sąsiedztwa.

    Args:
        image (np.ndarray): Obraz w odcieniach szarości jako macierz numpy.

    Returns:
        float: Średnia wartość kontrastu lokalnego dla całego obrazu.
    """
    M, N = image.shape
    total_contrast = 0
    pixel_count = 0

    # Iteracja przez każdy piksel z uwzględnieniem krawędzi
    for m in range(1, M-1):  # Omijamy krawędzie (sąsiedztwo 3x3)
        for n in range(1, N-1):
            center = image[m, n]
            neighbors = [
                image[m-1, n-1], image[m-1, n], image[m-1, n+1],
                image[m, n-1],                 image[m, n+1],
                image[m+1, n-1], image[m+1, n], image[m+1, n+1]
            ]
            local_contrast = np.mean(np.abs(center - np.array(neighbors)))
            total_contrast += local_contrast
            pixel_count += 1

    # Obliczenie średniego kontrastu lokalnego
    return total_contrast / pixel_count

# Główna część programu
if __name__ == "__main__":
    # Wczytaj obraz
    input_image_path = "muchaC.png"  # Ścieżka do obrazu
    image = Image.open(input_image_path).convert("L")  # Konwersja do odcieni szarości
    image_array = np.array(image, dtype=np.float64)  # Konwersja do macierzy NumPy

    # Oblicz kontrast lokalny
    contrast_value = local_contrast(image_array)

    # Wyświetl wynik
    print(f"Kontrast lokalny = {contrast_value:.3f}")

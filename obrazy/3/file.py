from PIL import Image

def convert_to_grayscale(image_path, output_path):
    # Otwieramy obraz
    img = Image.open(image_path)
    
    # Przekształcamy obraz na format RGB (na wypadek, gdyby nie był)
    img = img.convert('RGB')
    
    # Zmieniamy obraz na odcienie szarości zgodnie z wagami kolorów
    grayscale_img = img.convert('L', (0.299, 0.587, 0.114, 0))
    
    # Zapisujemy przekształcony obraz
    grayscale_img.save(output_path)

# Ścieżki do obrazów
input_image = '3/Untitled.png'
output_image = '3/output_image_gray.png'

# Konwersja
convert_to_grayscale(input_image, output_image)

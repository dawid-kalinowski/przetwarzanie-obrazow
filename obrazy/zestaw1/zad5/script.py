from PIL import Image, ImageDraw
import random

def apply_pointillism(image_path, output_path, num_dots=100000, dot_size=5):
    original_image = Image.open(image_path)
    width, height = original_image.size
    
    # konwerscja na rgb
    image = original_image.convert('RGB')
    
    # tworzenie nowego obrazu
    draw = ImageDraw.Draw(image)
    

    for _ in range(num_dots):
        # wybieramy losowy punkt na obrazie
        x = random.randint(0, width-1)
        y = random.randint(0, height-1)
        
        # pobieramu kolor z punktu
        color = original_image.getpixel((x, y))
        
        # rysujemy koło o średnicy dot_size w wybranych kolorze
        draw.ellipse((x - dot_size, y - dot_size, x + dot_size, y + dot_size), fill=color)
    
    image.save(output_path)
    print(f"Obraz zapisany w: {output_path}")

input_image = "zestaw1/zad5/michal.jpg"
output_image = "zestaw1/zad5/przerobiony_michal.jpg"
apply_pointillism(input_image, output_image)

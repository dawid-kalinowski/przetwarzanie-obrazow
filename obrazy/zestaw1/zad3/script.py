from PIL import Image

def convert_to_grayscale(image_path, output_path):
    img = Image.open(image_path)
    
    # konwersja na rgb
    img = img.convert('RGB')
    
    # konwerscja na skalę szarości, uwzględniając przyjęte w standardzie wagi
    grayscale_img = img.convert('L', (0.299, 0.587, 0.114, 0))
    
    grayscale_img.save(output_path)

input_image = 'michal.jpg'
output_image = 'szary_michal.jpg'

convert_to_grayscale(input_image, output_image)

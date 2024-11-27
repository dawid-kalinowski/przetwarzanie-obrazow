import numpy as np
from PIL import Image


image_path = "linie.png" 
original_image = Image.open(image_path).convert("L") 
original_array = np.array(original_image)

fmin = 25
sampled_array = original_array[::fmin, ::fmin] 

Image.fromarray(sampled_array).save("linie25.png") 



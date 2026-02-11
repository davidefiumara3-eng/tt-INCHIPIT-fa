from PIL import Image
import numpy as np
# from google.colab import drive
import os

# Apriamo l'immagine (mettete il nome completo dell'immagine, comprensivo dell'estensione)
image = Image.open("tre.jpg")

# La scalo per ottenere una matrice 28x28
image = image.resize((28, 28))

# La converto in bianco e nero
image = image.convert('L')

# La converto su una libreria compatibile
image_array = np.array(image)

# La trasformo in modo tale che sia un vettore di matrici
image_array = image_array.reshape((1, 28, 28))

# La normalizzo in modo tale che i pixel bianchi abbiano valori più alti dei pixel neri
image_array = (255 - image_array)
minVal, maxVal =np.min(image_array), np.max(image_array)

image_array = (image_array - minVal) / (maxVal - minVal) * 255
with open("img.txt", "w") as file:
    for row in image_array[0]:  # Remove the first dimension
        hex_values = [f"{int(val):02X}" for val in row]
        hex_values.append("80")
        file.write('(x"' + '", x"'.join(hex_values) + '"),\n')
    hex_values = ["80" for i in range(29)]
    file.write('(x"' + '", x"'.join(hex_values) + '")\n')
        

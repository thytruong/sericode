from PIL import Image

# Choix des caractères ASCII du plus clair au plus sombre
ASCII_CHARS = [" ", ".", ":", "-", "=", "+", "*", "#", "%", "@"]
# [ ] construire un tableau de png avec les noms de fichier

# Chargement de l'image
image_path = "moon.jpg"  # modifier avec le chemin de ton image
image = Image.open(image_path)

# Redimensionnement width fixe et hauteur proportionnelle
new_width = 150
width, height = image.size
ratio = height / width
new_height = int(new_width * ratio *0.5)
image = image.resize((new_width, new_height))

# Conversion en niveaux de gris
image = image.convert("L")

# Récupération des pixels
pixels = image.getdata()

# Conversion des pixels en caractères ASCII
ascii_str = ""
for pixel_value in pixels:
    # [ ] choisir index dans le tableau de png
    index = pixel_value * (len(ASCII_CHARS) - 1) // 255
    # [ ] prendre le fichier dans le répertoire de png
    ascii_str += ASCII_CHARS[index]
    # [ ] stitch carré de png sur la série existante

# Construction des lignes selon largeur d'image
ascii_image = ""
for i in range(0, len(ascii_str), new_width):
    ascii_image += ascii_str[i:i+new_width] + "\n"

# Affichage dans le terminal
print(ascii_image)

# [ ] reconstruire l'image résultante
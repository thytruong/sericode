from PIL import Image

# Charger l'image et convertir en mode CMJN
image_path = "moon.jpg"  # modifier par ton fichier
image = Image.open(image_path).convert("CMYK")

# Redimensionner pour limiter le nombre de pixels (ex largeur 50)
new_width = 50
width, height = image.size
ratio = height / width *0.5
new_height = int(new_width * ratio)
image = image.resize((new_width, new_height))

# Accéder aux pixels
pixels = list(image.getdata())

# Afficher les valeurs CMJN pixel par pixel
for y in range(image.height):
    ligne = ""
    for x in range(image.width):
        c, m, j, n = pixels[y * image.width + x]
        ligne += f"({c:3},{m:3},{j:3},{n:3}) "
    print(ligne)

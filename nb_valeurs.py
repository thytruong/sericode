from PIL import Image

# Charger l'image
image_path = "HMDS7025.jpg"  # modifier avec le chemin de ton image
image = Image.open(image_path)

# Redimensionner pour limiter le nombre de pixels (ex largeur 50)
new_width = 50
width, height = image.size
ratio = height / width
new_height = int(new_width * ratio)
image = image.resize((new_width, new_height))

# Conversion en niveaux de gris
image = image.convert("L")

# Récupérer les pixels en liste
pixels = list(image.getdata())

# Affichage des valeurs de gris ligne par ligne
for y in range(image.height):
    ligne = ""
    for x in range(image.width):
        gris = pixels[y * image.width + x]
        ligne += f"{gris:3} "
    print(ligne)

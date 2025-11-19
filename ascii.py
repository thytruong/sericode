from PIL import Image

# Liste des caractères ASCII du plus clair au plus foncé
ASCII_CHARS = [" ", ".", ":", "-", "=", "+", "*", "#", "%", "@"]

def resize_image(image, new_width=80):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
    return image.convert("L")  # Convertit en niveaux de gris

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value * (len(ASCII_CHARS) - 1) // 255]
    return ascii_str

def main(image_path):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Erreur lors de l'ouverture de l'image : {e}")
        return

    image = resize_image(image)
    image = grayify(image)
    ascii_str = pixels_to_ascii(image)

    # Séparer la chaine en lignes pour respecter la largeur
    ascii_len = len(ascii_str)
    width = image.width
    ascii_image = "\n".join([ascii_str[i:(i + width)] for i in range(0, ascii_len, width)])

    # Afficher le résultat dans la console
    print(ascii_image)

    # Écrire dans un fichier texte
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)

# Exemple d'utilisation
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Usage : python ascii_art.py chemin/vers/image.jpg")

from PIL import Image


# Ouvrir et afficher l'image
img = Image.open("cn.jpg")
img.show()


# Dimensions
largeur, hauteur = img.size
print("largeur : ", largeur)
print("hauteur : ", hauteur)

# Obtenir la couleur (R, G, B) d'un pixel
R, G, B = img.getpixel((0, 0))  # pix de coord (0, 0)
print(R, G, B)


# Modifier la couleur (R, G, B) d'un pixel
img.putpixel((0, 0), (255, 0, 0))
    # le pixel de coord (0, 0) passe en rouge



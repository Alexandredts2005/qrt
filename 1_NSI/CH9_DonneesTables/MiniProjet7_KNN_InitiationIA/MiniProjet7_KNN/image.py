from PIL import Image

# ouverture de l'image initiale
img = Image.open("bob.png")

# récupération de ses dimensions
largeur, hauteur = img.size
print(f"L'image a ", largeur, " colonnes et ", hauteur, "lignes.")


print("Le pixel du coin haut gauche a pour couleur ", img.getpixel((0,0)))
print("Le pixel du coin bas droit a pour couleur ", img.getpixel((largeur-1, hauteur-1)))

# liste des coordonnées de la zone comportant des pixels dégradés
liste_deg = [(col, lig)  for col in range(250, 321) for lig in range(30, 101)]
print(len(liste_deg))

# une liste des coordonnées des points de la zone dégradée mais privée des pixels dégradés
liste_nondeg = [(col, lig) for col in range(250, 321) for lig in range(30, 101) if img.getpixel((col,lig)) != (255,0,0)]
print(len(liste_nondeg))

s = 0
for l in liste_deg:
    for m in liste_nondeg:
        if l != m:
            s = s + 1
print(s)
def rotation(img_px, x, y, t):

    if t > 1 :
        t = t//2
        for i in range(x, x + t):
            for j in range (y, y + t):
                temp = img_px[i][j]
                img_px[i][j] = img_px[i][t + j]
                img_px[i][t + j] = img_px[t + i][t + j]
                img_px[t + i][t + j] = img_px[t + i][j]
                img_px[t + i][j] = temp

        rotation(img_px, x , y , t)
        rotation(img_px, x + t , y , t)
        rotation(img_px, x , y + t, t)
        rotation(img_px, x + t, y + t , t)



from PIL import Image
img = Image.open("bob_carre.jpg")


largeur, hauteur = img.size
print(largeur, hauteur)
img_px = [[[0] for i in range(hauteur)] for j in range(largeur)]

for x in range(largeur):
    for y in range(hauteur):
        img_px[x][y] = img.getpixel((x , y))

rotation (img_px,0,0,largeur)


imgr = Image.new('RGB', (largeur, hauteur))
for x in range(largeur):
    for y in range(hauteur):
        imgr.putpixel((x,y),img_px[x][y])

imgr.show()

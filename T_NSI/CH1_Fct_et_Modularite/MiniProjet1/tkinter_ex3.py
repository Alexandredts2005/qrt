from tkinter import *

racine = Tk()

# les labels
label1 = Label(racine, text="votre prénom :")
label1.grid(row=1, column=1, sticky="E", padx=10)
label2 = Label(racine, text="votre nom :")
label2.grid(row=2, column=1, sticky="E", padx=10)
label3 = Label(racine, text="votre ville :")
label3.grid(row=3, column=1, sticky="E", padx=10)

labelValider = Label(racine, text="") # label de la chaîne de validation
labelValider.grid(row=4, column=1, columnspan=2, sticky="W",padx=10)

# les entrées
entree1 = Entry(racine)
entree1.grid(row=1, column=2)
entree1.focus_set()
entree2 = Entry(racine)
entree2.grid(row=2, column=2)
entree3 = Entry(racine)
entree3.grid (row=3, column=2)

# le cannevas et son image (232x245)
cannevasImg = Canvas(racine, width=245, height=258, bg="pink")
photo = PhotoImage(file="bob.png")
image = cannevasImg.create_image(124, 131, image=photo)
cannevasImg.grid(row=1, column=3, rowspan=4, padx=10, pady=10)

# les boutons et leur gestion
def valider () :
    chaine = entree1.get()+" // "+ entree2.get()+ " // "+ entree3.get()
    labelValider.config(text=chaine)
def initialiser ():
    labelValider.config(text="")
    entree3.delete (0, END)
    entree2.delete (0, END)
    entree3.delete (0, END)
    entree1.focus_set()
    
boutonQuitter = Button(racine, text="Quitter", command=racine.destroy)
boutonQuitter.grid(row=5, column=3, pady=10)
boutonValider = Button(racine, text="Valider", command=valider)
boutonValider.grid(row=5, column=1, pady=10)
boutonInitialiser = Button(racine, text="Réinitialiser", command=initialiser)
boutonInitialiser.grid(row=5, column=2, pady=10)

racine.mainloop()


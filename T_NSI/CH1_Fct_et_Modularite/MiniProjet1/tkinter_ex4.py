from tkinter import *

racine = Tk()
racine.title("Calculatrice")
racine.minsize(300,200)

# Titre (Label)
titre = Label(racine, text="Saisir un calcul : ")
titre.pack()
# Frame (cadre)
cadre = Frame(racine)
cadre.pack()

# Saisie de l'expression mathématique : Entrée (Entry)
expression = StringVar()
expression.set("6*7")   # texte par défaut affiché dans l'entrée
entree = Entry(cadre, textvariable=expression, width=30)
entree.pack()

# Résultat du calcul
resultat = StringVar()
sortie = Label(cadre, textvariable=resultat)
sortie.pack()

def calculer():
   resultat.set(eval(expression.get()))
   
# Bouton pour exécuter les calculs
bouton = Button(cadre, text="Calculer", command=calculer)
bouton.pack()

quitter = Button(racine, text="Quitter", command=racine.destroy)
quitter.pack()
racine.mainloop()




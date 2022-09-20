import tkinter as tk

## Fonctions
def question():
    intro = tk.Label(fenetre, text="quelle est la réponse ?")
    intro.grid(column=0, row=0, sticky="W", padx=40)
    
    radioval = tk.IntVar()
    choix = ["reponse 1", "reponse 2", "reponse 3"]
    for i in range(3):
        objet = tk.Radiobutton(fenetre, text=choix[i], var=radioval, value=i)
        objet.grid(column=0, row=i+1)
    labelValue = tk.Label(fenetre, textvariable=radioval)
    labelValue.grid(column=2, row=5, sticky="E", padx=40)
    quitter = tk.Button(fenetre, text="Quitter", command=fenetre.destroy)
    quitter.grid(column=0, row=5)

### Programme principal
# /!\ 1 seule instance de tkinter appelée
fenetre = tk.Tk()
fenetre.geometry("400x300")
labelValue = tk.Label(fenetre, text="bienvenue !")
commencer = tk.Button(fenetre, text="démarrer", command=question)
labelValue.grid(column=0, row=0)
commencer.grid(column=0, row=1 )
fenetre.mainloop()


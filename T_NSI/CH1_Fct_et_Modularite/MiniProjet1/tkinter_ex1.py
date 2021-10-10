import tkinter as tk

racine = tk.Tk()
label = tk.Label(racine, text="J'adore Python !")
bouton = tk.Button(racine, text="Quitter", command=racine.destroy)
bouton["fg"] = "red"
label.pack()
bouton.pack()
racine.mainloop()
print("C'est fini !")



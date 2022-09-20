import tkinter as tk

class Qcm():
    """classe définissant la fenêtre principale du programme"""
    
    def __init__(self):
        """ Fenêtre d'accueil pour démarrer """
        
        self.fenetre = tk.Tk()
        self.fenetre.geometry("400x300")
        self.labelValue = tk.Label(self.fenetre, text="bienvenue !")
        self.commencer = tk.Button(self.fenetre, text="démarrer", command=self.passage)
        self.labelValue.grid(column=0, row=0)
        self.commencer.grid(column=0, row=1 )
        self.fenetre.mainloop()
        
    def passage(self):
        """ Méthode qui détruit l'instance tk précédente et relance
        la nouvelle instance par la méthode question """
        self.fenetre.destroy()
        self.question()
        
    def question(self):
        """ Fenêtre de la question 1 du QCM """
        self.fenetre2 = tk.Tk()
        intro = tk.Label(self.fenetre2, text="quelle est la réponse ?")
        intro.grid(column=0, row=0, sticky="W", padx=40)
    
        radioval = tk.IntVar()
        choix = ["reponse 1", "reponse 2", "reponse 3"]
        for i in range(3):
            objet = tk.Radiobutton(self.fenetre2, text=choix[i], var=radioval, value=i)
            objet.grid(column=0, row=i+1)
        
        labelValue = tk.Label(self.fenetre2, textvariable=radioval)
        #print( "valeur radio :", radioval.get())
        
        labelValue.grid(column=2, row=5, sticky="E", padx=40)
        quitter = tk.Button(self.fenetre2, text="Quitter", command=self.fenetre2.destroy)
        quitter.grid(column=0, row=5)
        
        self.fenetre2.mainloop()


Essai = Qcm()

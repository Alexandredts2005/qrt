print("__________________________________________________")
print("Bienvenue sur le jeu Devine un nombre,tt entre 0 et 100")
print("__________________________________________________")

run = True

while run:
    nbre = int(input("Joueur 1 : quel nombre proposes-tu ? "))
    print("Joueur 2 à ton tour !\n")
    
   
    maxi = 3
    coups = 0
    while coups < maxi :
        joue = int(input("Joueur 2 : quel est ce nombre à ton avis ?"))
        
        if joue != nbre:
            print("non, ce n'est pas ça !\n")
            print("... il te reste ", maxi - coups - 1, " coups à jouer.\n")
            coups = coups + 1
        else:
            coups = maxi
    
    if nbre == joue:
        print("Bravo tu as gagné !")
    else:
        print(" :-[     loose ...")
    run = False
        
# Créé par lvannier, le 22/01/2022 en Python 3.4
from FILE import *


class Arbre_binaire:
    """
    Classe implémentant un arbre binaire dont les noeuds sont caractérisés par
    - une valeur (de type quelconque)
    - un fils gauche et un fils droit
    Les enfants gauche et droit sont eux-mêmes des arbres
    """
    def __init__(self, gauche = None, valeur = None, droit = None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit

    def est_vide(self):
        if self.valeur == None:
            return True
        else:
            return False


    def get_valeur(self):
        """
        Accesseur de la valeur de l'arbre
        """
        return self.valeur


    def get_gauche(self):
        """
        Accesseur du fils gauche
        """
        return self.gauche

    def get_droit(self):
        """
        Accesseur du fils droit
        """
        return self.droit

    def set_valeur(self, valeur):
        """
        Mutateur de la valeur du noeud
        """
        self.valeur = valeur


    def set_gauche(self, arbre):
        """
        Mutateur du fils gauche
        """
        self.gauche = arbre

    def set_droit(self, arbre):
        """
        Mutateur du fils droit
        """
        self.droit = arbre

    def taille(self):
        if self.est_vide():
            return 0

        if self.gauche == None and self.droit == None:
            return 1

        elif self.gauche == None:
            return 1 + self.droit.taille()

        else:
            return 1 + self.gauche.taille()

    def taillebis(self):
        if self == None:
            return 0
        else:
            return 1 + Arbre_binaire(self.gauche).taillebis()+Arbre_binaire(self.droit).taillebis()

    def hauteur(self):
        if self.est_vide():
            return 0

        if self.gauche == None and self.droit == None:
            return 1

        elif self.gauche == None:
            return 1 + self.droit.hauteur()

        elif self.droit == None:
            return 1 + self.gauche.hauteur()
        else:
            return 1 + max(self.gauche.hauteur() , self.droit.hauteur())


    def parcours_largeur(self):
        f = CREER_FILE_VIDE()
        ENFILER(f,self)
        parcours = []
        while not EST_VIDE(f):
            noeud_en_cours = DEFILER(f)
            parcours.append(noeud_en_cours.valeur)
            if noeud_en_cours.gauche != None:
                ENFILER(f, noeud_en_cours.gauche)
            if noeud_en_cours.droit != None:
                ENFILER(f, noeud_en_cours.droit)
        return parcours


    def parcours_prefixe(self):
        parcours = []
        parcours.append(self.valeur)
        if self.gauche != None:
            parcours.append(self.gauche.parcours_prefixe())
        if self.droit != None:
            parcours.append(self.droit.parcours_prefixe())
        return parcours


    def parcours_postfixe(self):
        parcours = []
        if self.gauche != None:
            parcours.append(self.gauche.parcours_postfixe())
        if self.droit != None:
            parcours.append(self.droit.parcours_postfixe())
        parcours.append(self.valeur)
        return parcours

    def affiche(self):
        """permet d'afficher un arbre"""

        if self.gauche == None and self.droit == None:
            return self.valeur
        elif self.gauche == None:
            return [self.valeur,self.droit.affiche()]
        elif self.droit == None:
            return [self.valeur, self.gauche.affiche()]
        else:
            return [self.valeur,self.gauche.affiche(),self.droit.affiche()]

a = Arbre_binaire()
b = Arbre_binaire(None, 3, )
c = Arbre_binaire(None, 2, )
d = Arbre_binaire (c , 1 , b)
f4 = Arbre_binaire(None, 4, None)
f5 = Arbre_binaire(None, 5, None)
f6 = Arbre_binaire(None, 6, None)
N2 = Arbre_binaire(f4, 2 , f5)
N3 = Arbre_binaire(None, 3, f6)
e = Arbre_binaire(N2 , 1, N3)

f = Arbre_binaire(Arbre_binaire(Arbre_binaire(None,5,None),8,Arbre_binaire(None,10, None)),11, Arbre_binaire(Arbre_binaire(None,13,None),14,Arbre_binaire(None,15,None)))
print(e.valeur)
print(e.affiche())
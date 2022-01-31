# Créé par lvannier, le 22/01/2022 en Python 3.4
from FILE import *
from PILE import *
import graphviz

class Arbre_binaire_recherche:
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

    def dessiner(self) -> None:
        """
        Représente l'arbre avec graphviz (https://graphviz.org/)
            $ sudo apt update
            $ sudo apt install graphviz
            $ sudo python3 -m pip install graphviz
        """
        key = 0
        pile = []

        g = graphviz.Graph(format="png")
        g.node(str(key), str(self.valeur))
        EMPILER(pile, (self, key))

        while not EST_VIDE(pile):
            enCours, enCours_key = DEPILER(pile)
            if enCours.gauche:
                key += 1
                g.node(str(key), str(enCours.gauche.valeur))
                EMPILER(pile, (enCours.gauche, key))
                g.edge(str(enCours_key), str(key))
            else:
                key += 1
                g.node(str(key), style='invis')
                g.edge(str(enCours_key), str(key), style="invis", weight="20")
            if enCours.droit:
                key += 1
                g.node(str(key), str(enCours.droit.valeur))
                EMPILER(pile, (enCours.droit, key))
                g.edge(str(enCours_key), str(key))
            else:
                key += 1
                g.node(str(key), style='invis')
                g.edge(str(enCours_key), str(key), style="invis", weight="20")

        g.render(view=True)

        return None


    def set_valeur(self, valeur):
        """ Mutateur de la valeur du noeud """
        self.valeur = valeur

    def set_gauche(self, arbre):
        """ Mutateur du fils gauche """
        self.gauche = arbre

    def set_droit(self, arbre):
        """ Mutateur du fils droit """
        self.droit = arbre

    def taille(self):
        """ Taille de l'arbre"""
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
            return 1 + Arbre_binaire_recherche(self.gauche).taillebis()+Arbre_binaire_recherche(self.droit).taillebis()

    def hauteur(self):
        """ Hauteur de l'arbre"""
        if self.est_vide():
            return 0
        if self.gauche == None and self.droit == None:
            return 1
        elif self.gauche == None:
            return 1 + self.droit.hauteur()
        elif self.droit == None:
            return 1 + self.gauche.hauteur()
        else:
            return 1 + max(self.gauche.hauteur(), self.droit.hauteur())


    def parcours_largeur(self):
        f = CREER_FILE_VIDE()
        ENFILER(f, self)
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
    
    def parcours_infixe(self):

        ## A COMPLETER ##
        
        
        return 


    def recherche(self,x):
        
        ## A COMPLETER ##
            
        return 
        
    def ajout(self,x):
        
        ## A COMPLETER ##
        
        return
        
    def minimum(self):
       
       
       ## A COMPLETER ##
        
       return 
        


a = Arbre_binaire_recherche()
b = Arbre_binaire_recherche(None, 3, )
c = Arbre_binaire_recherche(None, 2, )
d = Arbre_binaire_recherche (c , 1, b)
f4 = Arbre_binaire_recherche(None, 4, None)
f5 = Arbre_binaire_recherche(None, 5, None)
f6 = Arbre_binaire_recherche(None, 6, None)
N2 = Arbre_binaire_recherche(f4, 2, f5)
N3 = Arbre_binaire_recherche(None, 3, f6)
e = Arbre_binaire_recherche(N2 , 1, N3)

f = Arbre_binaire_recherche(Arbre_binaire_recherche(Arbre_binaire_recherche(None, 5, None),8,Arbre_binaire_recherche(None,10, None)),11, Arbre_binaire_recherche(Arbre_binaire_recherche(None,13,None),14,Arbre_binaire_recherche(None,15,None)))


f.dessiner()

#print(e.minimum())
#print(" Parcours infixe : ", f.parcours_infixe())
#f.ajout(12)
#f.dessiner()



import bisect
    # la bibliothèque bisect permet d'insérer dans une liste, en gardant la liste triée

# CLASSE Arbre_Huffman
class Arbre_Huffman:
        def __init__ (self, lettre, nbocc, g = None, d = None):
            """ lettre : lettre concernée
                nbocc : nombre d'occurences de la lettre"""
            self.lettre = lettre
            self.nbocc = nbocc
            self.gauche = g
            self.droite = d
            
        def __lt__ (self, other):
            """ Méthode qui permet de comparer 2 arbres
            renvoie True si  le nombre d'occurences de l'arbre A (self)
            est strictement supérieur à celui de l'arbre B (other), False sinon"""
            return self.nbocc > other.nbocc
        
        def est_feuille(self):
            """renvoie True si l'arbre est une feuille"""
            return ################################
        
# FONCTIONS UTILISEES
def compte_occurences(texte) -> dict:
    """renvoie un dictionnaire avec chaque caractère du texte pour clé
    et le nombre d'apparitions de ce caractère pour valeur
    Par exemple pour "TOTO", on obtient le dict. {"T": 2, "O": 2} """
    occ = dict()
    for car in texte:
        if car not in occ:
            #####################################
        occ[car] = occ[car] + 1
    return #####################################

def contruit_feuilles(texte) -> list:
    """renvoie une liste des feuilles de départ de l'arbre de Huffman"""
    dic_occurences = compte_occurences(texte)
    liste_feuilles = []
    for lettre, occ in dic_occurences.items():
        liste_feuilles.append(Arbre_Huffman(lettre, occ))
        
    return liste_feuilles
            

def fusionne(gauche, droite) -> Arbre_Huffman:
    """réalise la fusion de deux arbres, selon la méthode vue partie B"""
    nbocc_total = #####################################
    return Arbre_Huffman(None, nbocc_total, gauche, droite)


def parcours(arbre, chemin_en_cours, dico):
    """" parcourt l'arbre de huffman pour trouver le codage de chaque carectère"""
    if arbre == None:
        return
    if arbre.est_feuille():
        dico[arbre.lettre] = chemin_en_cours
    else:
        parcours(arbre.gauche, chemin_en_cours + [0], dico)
        ###################################################
        
def codage_Huffman(texte) -> dict:
    """détermine le codage de Huffman optimal pour le texte donné en paramètre"""
    liste_arbres = contruit_feuilles(texte) #on récupère toutes les feuilles de départ
    liste_arbres.sort()   # et on les trie par ordre d'occurences décroissant
    while len(liste_arbres) > 1:    #tant qu'il reste au moins deux arbres
        droite = liste_arbres.pop()         #on récupère la dernière valeur : la plus petite et on la supprime
        gauche = liste_arbres.pop()         #idem
        new_arbre = fusionne (gauche, droite)   #on fusionne les deux arbres
        bisect.insort(liste_arbres, new_arbre)   #on insère l'arbre fusionné dans la liste qui reste triée
    arbre_huffman = liste_arbres.pop() # il n'y a plus qu'un arbre dans la liste : celui cherché
    
    dico = {}
    parcours(arbre_huffman, [] , dico) #récupère les codes de chaque caractère 
    return dico #renvoie le dictionnaire des codes
        
# SCRIPT PRINCIPAL
with open("texte.txt") as chaine:
    texte = chaine.read()
    texte = texte.strip("\n")
print(texte) 
print(codage_Huffman(texte))
        
                
        
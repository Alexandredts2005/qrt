
from classe_graphe_pondere_correction import *
from creation_graphe import g

def dijkstra(g, depart : str) -> list :
    """
    Met en place l'algorithme de Dijskstra

    g est un graphe représenté par sa matrice d'adjacence
    depart est le nom du sommet de départ

    Renvoie le dictionnaire associant à chaque sommet son prédecesseur dans le plus
    court trajet issue de depart
    """

    visites = []
    distances = {}
    predecesseurs = {}
    sommets = g.sommets()
    for s in sommets :
        distances[s] = float('Inf')
        predecesseurs[s] = None

    distances[depart] = 0

    # On effectue l'algorithme tant que tous les sommets n'ont pas été explorés
    while len(visites) < len(sommets) :
        # Choix du sommet non visité le plus proche
        d_min = float('inf')
        for s in sommets :
            # déterminer le sommet a le plus proche
            # à compléter
            if s not in visites and ...
        
        # On ajoute ce sommet à la liste des sommets visités
         # à compléter

        # On recalcule les trajets vers les autres sommets
        for v in g.voisins(a) :
            if distances[v] > distances[a] + g.arc(a,v) :
                distances[v] = # à compléter
                predecesseurs[v] = a
    
    return(predecesseurs)

def trajet(g, depart, arrivee) -> list :
    """déterminer le trajet le plus court entre le sommet depart et le sommet arrivee"""
    
    p = dijkstra(g, depart)

    trajet = [arrivee]
    d = 0

    enCours = arrivee

    while p[enCours] != depart :
        trajet.append(p[enCours])
        d = d + g.arc( # à compléter
        enCours = # à compléter

    trajet.append(# à compléter
    d = d + g.arc(p[enCours], enCours)

    return trajet[::-1], d

print(trajet(g, 'E', 'S'))


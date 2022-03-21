from classe_graphe_pondere_correction import *

g = Graphe_P()
g.ajouter_arc('A', 'D', 2)
g.ajouter_arc('A', 'G', 2)
g.ajouter_arc('B', 'A', 1)
g.ajouter_arc('C', 'B', 1)
g.ajouter_arc('C', 'G', 3)
g.ajouter_arc('D', 'G', 4)
g.ajouter_arc('D', 'S', 7)
g.ajouter_arc('E', 'A', 5)
g.ajouter_arc('E', 'B', 3)
g.ajouter_arc('E', 'C', 2)
g.ajouter_arc('F', 'D', 1)
g.ajouter_arc('F', 'S', 6)
g.ajouter_arc('G', 'F', 4)

#g.afficher()

#print(g.voisins('A'))
#print(g.sommets())



class Graphe_P:
    '''Graphe pondéré représenté par un dictionnaire d'adjacence'''

    def __init__(self):
        self.adj={}

    def affiche(self):
        for k in self.adj:
            print(k, self.adj[k])

    def ajouter_sommet(self,s):
        if s not in self.adj:
            self.adj[s] = {}

    def ajouter_arc(self, s1, s2, p):
        """ajoute l'arc de s1 à s2 en lui affectant le poids p"""
        self.ajouter_sommet(s1)

        # à compléter
       
    def arc(self,s1,s2):
        """ renvoie le poids de l'arc de s1 à s2"""
        for s in self.adj[s1].keys():
       # à compléter
  

    def sommets(self):
        s=[]
        for k in self.adj:
            s.append(k)
        return s

    def voisins(self, s):
        """ renvoie la liste des voisins du sommet s"""
        # à compléter
     












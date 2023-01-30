class Pile:
   """
   Représentation d'une pile, implémentée grâce aux listes python.
   """

   def __init__(self):
      """
      Crée une pile vide
      """
      self.pile = []

   def est_vide(self):
      """
      Renvoie True ssi la pile est vide.
      """
      return len(self.pile) == 0

   def taille(self):
      """
      Renvoie la taille de la pile (en nombre d'éléments empilés)
      """
      return len(self.pile)

   def empiler(self, valeur):
      """
      Empile un nouvel élément
      """
      self.pile.append(valeur)

   def depiler(self):
      """
      Dépile et renvoie la valeur de l'élément placé au sommet
      Déclenche une erreur si la pile est vide.
      """
      if self.est_vide():
         raise IndexError("Dépiler sur une pile vide")
      else:
         return self.pile.pop()

pile = Pile()
pile.taille()
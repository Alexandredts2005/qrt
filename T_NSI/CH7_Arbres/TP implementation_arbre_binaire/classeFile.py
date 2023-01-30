class File:
   """
   Représentation d'une file, implémentée grâce aux listes python.
   """

   def __init__(self):
      """
      Crée une file vide
      """
      self.file = []

   def est_vide(self):
      """
      Renvoie True ssi la file est vide.
      """
      return len(self.file) == 0

   def taille(self):
      """
      Renvoie la taille de la file (en nombre d'éléments emfilés)
      """
      return len(self.file)

   def enfiler(self, valeur):
      """
      Enfile un nouvel élément.
      """
      self.file.append(valeur)

   def defiler(self):
      """
      Défile et renvoie la valeur de l'élément placé premier
      dans la file (le plus ancien).

      Déclenche une erreur si la file est vide.
      """
      if self.est_vide():
         raise IndexError("Défiler sur une file vide")
      else:
         return self.file.pop(0)

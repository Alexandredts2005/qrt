# Créé par lvannier, le 21/11/2021 en Python 3.4
def CREER_FILE_VIDE():
    """crée une file vide"""
    return []

def EST_VIDE(F):
    if len(F) == 0:
        return True
    else:
        return False

def ENFILER(F,x):
    """ajoute la valeur x à la queue de la file F"""
    F.append(x)

def DEFILER(F):
    """renvoie la tête de la file F et la supprime"""
    if not EST_VIDE(F):
        temp = F[0]
        del (F[0])
        return temp
    else:
        return False








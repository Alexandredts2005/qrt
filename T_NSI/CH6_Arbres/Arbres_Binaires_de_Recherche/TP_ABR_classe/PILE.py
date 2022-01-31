# Créé par lvannier, le 21/11/2021 en Python 3.4


def CREER_PILE_VIDE():
    """crée une pile vide"""
    return []

def EST_VIDE(P):
    if len(P) == 0:
        return True
    else:
        return False


def EMPILER(P,e):
    """ empile la valeur e au sommet de la liste P"""
    P.append(e)



def DEPILER(P):
    """renvoie la valeur du sommet de la pile et la supprime"""
    if not EST_VIDE(P):
        return P.pop()
    else:
        return False





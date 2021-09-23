# Module qcm.py pour le passage du QCM


def affiche_correction(QCM, i):
    """ fonction qui affiche la correction à la question i
    --> renvoie un tuple avec (indice de la réponse , réponse correcte)"""
    
    assert type(QCM) != 'list', "QCM doit être un tableau."
    assert i >= 0 and i <= 2, "i est compris entre 0 et 2."
    
    # A CODER !
    
    return correction


def affichageQCM(QCM, i):
    ''' permet d'afficher la question n°i du QCM contenue dans le tableau QCM.
    les réponses sont ensuite proposées (l'étoile indiquant la bonne réponse est supprimée lors de l'affichage)'''
    
    assert type(QCM) != 'list', "QCM doit être un tableau."
    assert i >= 0 and i <= 2, "i est compris entre 0 et 2."
    
     # A CODER !
    

def score_reponse(QCM, rep, i):
    """ calcul le score de la question n°i en fonction de la réponse
    --> renvoie 0 ou 1"""
    
    assert type(QCM) != 'list', "QCM doit être un tableau."
    assert rep > 0 and rep <= 3, "rep est compris entre 1 et 3."
    assert i >= 0 and i <= 2, "i est compris entre 0 et 2."
    
    # A CODER !   
   
    if rep_correcte == rep:
        return 1
    else:
        return 0

def passageQCM(QCM):
    ''' fonction de passage de QCM. Pour chaque question :
     --> affiche la question puis les 3 propositions (fonction affichageQCM)
     --> récupère le numéro de la réponse du candidat dans un tableau
     --> affiche la correction  (fonction affiche_correction)
     --> comptabilise le score (fonction score_reponse)'''
    
    assert type(QCM) != 'list', "QCM doit être un tableau."
    
    score = 0
    
    # A CODER !

        
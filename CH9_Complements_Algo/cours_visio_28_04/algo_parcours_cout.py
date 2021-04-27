# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 16:32:15 2021

@author: lvannier
"""


# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 16:26:08 2021

@author: lvannier
"""




def recherche(tab, v):
    k = 0 #compteur d'opérations
    for i in range(0, len(tab)-1):
        k = k + 1
        if tab[i]==v:
            return True,k
    return False,k

n=1000
L = [i for i in range(n)]



print(recherche(L, n))




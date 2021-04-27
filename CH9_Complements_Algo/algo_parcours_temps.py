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


from time import time

start=time()

def recherche(tab, v):
    for i in range(0, len(tab)-1):
        if tab[i]==v:
            return True
    return False

n=100000
L = [i for i in range(n)]



print(recherche(L, 100000000))


end=time()
print(end-start)